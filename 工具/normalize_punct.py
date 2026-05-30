"""
蒸馏 — 标点规范化 + 错字提示工具

用法:
    python 工具/normalize_punct.py                # 默认改写 正文/蒸馏 全文.md
    python 工具/normalize_punct.py <file.md>      # 改写指定文件
    python 工具/normalize_punct.py --dry <file>   # 只看报告不写回

行为:
- 在中文上下文中,把半角标点替换为全角(逗号/分号/冒号/问号/叹号/括号)。
- 把直引号替换为弯引号("/"  '/')。 智能配对:以行为单位交替决定开/合。
- 把全角空格 / 多余空格的细节保持原样,不动。
- **跳过 fenced code block (``` ... ```) 和 inline code (`...`)**,避免破坏代码 / 文件名。
- 英文上下文(如 "8:35"、"0.41"、"don't")不受影响。
- 错字按词表提示,不自动改(语义敏感,需作者拍板)。

幂等:重复运行无副作用。

如果需要新增词条到错字表,改 TYPO_HINTS。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "正文" / "蒸馏 全文.md"

CHN = r"[一-鿿]"
CHN_RE = re.compile(CHN)

# 错字提示词表(key=出现的串,value=建议)。
# 不会自动改,只在报告里列出 + 行号,作者自己定夺。
TYPO_HINTS: list[tuple[str, str]] = [
    ("关上了们", "关上了门"),
    ("只能门锁", "智能门锁"),
    ("我得妻子", "我的妻子"),
    ("大会会产生", "大概会产生"),
    ("Ai智能体", "AI智能体"),
    ("席位的差异", "细微的差异?(语义存疑)"),
    ("有时候去工业", "有时候去公园?(下文有公园)"),
    ("下午11点41分", "上午11点41分?(时序看应是上午)"),
    ("看和我的眼神", "看着我的眼神 / 看我的眼神?"),
    ("搞了一些", "高了一些?(语调升高语境)"),
]


# ---------------------------------------------------------------------------
# 分段:把 fenced code / inline code 切出来保护
# ---------------------------------------------------------------------------
_PROTECT_RE = re.compile(r"```.*?```|`[^`\n]+`", re.DOTALL)


def split_protected(text: str) -> list[tuple[bool, str]]:
    """返回 [(is_protected, content), ...]。"""
    segments: list[tuple[bool, str]] = []
    last = 0
    for m in _PROTECT_RE.finditer(text):
        if m.start() > last:
            segments.append((False, text[last : m.start()]))
        segments.append((True, m.group(0)))
        last = m.end()
    if last < len(text):
        segments.append((False, text[last:]))
    return segments


# ---------------------------------------------------------------------------
# 中文上下文标点替换
# ---------------------------------------------------------------------------
_PUNCT_RULES = [
    (",", "，"),
    (";", "；"),
    (":", "："),
    ("?", "？"),
    ("!", "！"),
]


def normalize_punct(text: str) -> str:
    for half, full in _PUNCT_RULES:
        h = re.escape(half)
        # 前是中文 或 后是中文
        text = re.sub(rf"(?<={CHN}){h}|{h}(?={CHN})", full, text)

    # 括号:中文一侧(包括前是空格/标点+后是中文 这种 case)
    # 简化策略:括号内包含至少一个汉字时,整对替换
    text = re.sub(
        r"\(([^()\n]*[一-鿿][^()\n]*)\)",
        r"（\1）",
        text,
    )
    return text


# ---------------------------------------------------------------------------
# 引号规范化
# ---------------------------------------------------------------------------
def smart_double_quotes(text: str) -> str:
    """直双引号 " → "/"。按行分别处理,行内交替开/合。"""
    out_lines: list[str] = []
    for line in text.split("\n"):
        if '"' not in line:
            out_lines.append(line)
            continue
        chars: list[str] = []
        is_open = True
        for ch in line:
            if ch == '"':
                chars.append("“" if is_open else "”")
                is_open = not is_open
            else:
                chars.append(ch)
        out_lines.append("".join(chars))
    return "\n".join(out_lines)


def smart_single_quotes(text: str) -> str:
    """直单引号 ' → '/'。只在中文上下文中替换(避免误改英文 don't 之类)。"""
    out_lines: list[str] = []
    for line in text.split("\n"):
        if "'" not in line:
            out_lines.append(line)
            continue
        chars = list(line)
        n = len(chars)
        is_open = True
        for i, ch in enumerate(chars):
            if ch != "'":
                continue
            prev_is_chn = i > 0 and CHN_RE.match(chars[i - 1])
            next_is_chn = i + 1 < n and CHN_RE.match(chars[i + 1])
            if not (prev_is_chn or next_is_chn):
                # 视为英文撇号,不动
                continue
            chars[i] = "‘" if is_open else "’"
            is_open = not is_open
        out_lines.append("".join(chars))
    return "\n".join(out_lines)


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def normalize(text: str) -> str:
    out: list[str] = []
    for is_protected, seg in split_protected(text):
        if is_protected:
            out.append(seg)
            continue
        seg = normalize_punct(seg)
        seg = smart_double_quotes(seg)
        seg = smart_single_quotes(seg)
        out.append(seg)
    return "".join(out)


def diff_locations(old: str, new: str) -> list[tuple[int, str, str]]:
    """返回 [(line_no, old_line, new_line)] 仅取被改动的行。"""
    diffs: list[tuple[int, str, str]] = []
    o_lines = old.split("\n")
    n_lines = new.split("\n")
    for i, (o, n) in enumerate(zip(o_lines, n_lines), start=1):
        if o != n:
            diffs.append((i, o, n))
    return diffs


def report_typos(text: str) -> list[tuple[int, str, str]]:
    """扫描错字词表,返回 [(line, hit, suggest)]。"""
    findings: list[tuple[int, str, str]] = []
    for needle, suggest in TYPO_HINTS:
        idx = 0
        while True:
            i = text.find(needle, idx)
            if i < 0:
                break
            line_no = text[:i].count("\n") + 1
            findings.append((line_no, needle, suggest))
            idx = i + len(needle)
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=str(DEFAULT_PATH))
    parser.add_argument("--dry", action="store_true", help="只报告不写回")
    args = parser.parse_args(argv)

    path = Path(args.path)
    if not path.exists():
        print(f"文件不存在: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8")
    new = normalize(text)

    diffs = diff_locations(text, new)
    if diffs:
        print(f"== 标点规范化 ==  {len(diffs)} 行变更")
        for line_no, o, n in diffs[:60]:
            print(f"  L{line_no}")
            print(f"    - {o}")
            print(f"    + {n}")
        if len(diffs) > 60:
            print(f"  ...({len(diffs)-60} 行未展示)")
    else:
        print("== 标点规范化 == 无变更(已规范)")

    if not args.dry and diffs:
        path.write_text(new, encoding="utf-8")
        print(f"已写回 {path}")

    findings = report_typos(new)
    print()
    print(f"== 错字提示 ==  共 {len(findings)} 条")
    if not findings:
        print("  (无)")
    for line_no, hit, suggest in findings:
        print(f"  L{line_no}: {hit!r} → {suggest}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
