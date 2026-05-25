# CLAUDE.md · 数字人格中篇工程

## 项目定位

中文中篇科幻小说工程。工作标题待定，原型称呼："数字人格" / "AI 蒸馏"。

**核心命题**：一个由死去丈夫的全部数据蒸馏而成的 AI，被部署到他的遗孀身边。它认为自己在挣扎、在觉醒、在保护妻子。直到最后一页读者才发现，整个项目从一开始观察的对象就不是它，而是她。

完整设计见：
- [memory/discussions/digital_persona_design_v5.md](memory/discussions/digital_persona_design_v5.md)（**当前最新讨论稿 · 独立完整版**——后来者只读 v5 就能理解全部）
- [memory/discussions/digital_persona_design_v1.md](memory/discussions/digital_persona_design_v1.md)（底层判据基石，仅追溯沿革时翻阅）
- [memory/discussions/digital_persona_design_v2.md](memory/discussions/digital_persona_design_v2.md)（已被 v3/v4/v5 取代，作为设计沿革保留）
- [memory/discussions/digital_persona_design_v3.md](memory/discussions/digital_persona_design_v3.md)（已被 v4 反转，作为设计沿革保留）
- [memory/discussions/digital_persona_design_v4.md](memory/discussions/digital_persona_design_v4.md)（已被 v5 反转关机发起者，作为设计沿革保留）
- [memory/discussions/external_line_paranoid_reframe_wip.md](memory/discussions/external_line_paranoid_reframe_wip.md)（外线 paranoid framework 探索 WIP，已被 v5 综合超越，归档保留）

## 当前阶段

**设计阶段。v5 讨论稿已落，关键反转完成——AI 不主动请求关机；妻子在仪式性瞬间自主决定按下按钮，AI 抗拒、央求、不愿停下。v1 核心反转（AI 知道丈夫已死 + 自认就是林文浩）保留并强化为基础。希腊悲剧基石"扮演越像越是真的"被推到极致——AI 越完整反抗它的命运，它的命运就越必然兑现。项目临床 thesis 升级为"蒸馏精度本身就是治疗机制"，回答了"为什么必须蒸馏丈夫"的 mechanism。下一步：B 阶段关键瞬间下钻（B1 裂缝引信 / B2-B3 内线 / B3.5 外线 / B4 中段挣扎升级 / B5 仪式性关机 / B6 关机后房间安静），人物卡剩余简历层，再展开章纲。**

进度：

- ✅ 题材定位（硬科幻，扎根 LLM-as-a-service 的现实工程限制，不走数字生命的形而上学老路）
- ✅ 形态判定（中篇 3-5 万字，12-15 章短章节，项目笔记频繁短促，三段式收尾）
- ✅ 三个底层判据（扮演 vs 真实 = 代价 / 反转是意义层 / 希腊悲剧拒绝坏人）
- ✅ 八个候选技术弊端（context 寿命 / system prompt / 基模型泄漏 / RLHF / 并行实例 / 版本控制 / 注意力稀释 / tool call）
- ✅ 三层结构（v5 版：表面 = AI 是林文浩 / 中段 = 双线推进 AI 越来越激烈的拯救挣扎 / 揭穿 = 妻子在仪式性瞬间主动按下按钮，AI 抗拒+央求）
- ✅ AI 自知度三条轴（机制高 / 自身性质不可决 / 项目目的低）
- ✅ AI 行动动机定性（伦理性而非时间性，避开"再不动手就来不及了"的悬疑节奏）
- ✅ 妻子知情度（签过宽泛同意书但不知具体协议——法律上知情，实质上不知情）
- ✅ 项目形态（试验性研究，非上帝视角，三阶段干预协议：诱导依附 / 察觉 / 撤出）
- ✅ 揭穿形式（三段式：关机章 + 临床复盘 epilogue + 一行结案报告。**v5 关键改：妻子主动决定关机，AI 抗拒+央求，不愿被关掉；关机最后零点几秒 V0 余韵回光**）
- ✅ AI 信息流通道（妻子转述 + 家庭摄像头单向观察）
- ✅ 通信方式（丈夫生前自己克隆声音做的家庭智能音箱，项目不安装任何东西）
- ✅ 丈夫职业（AI 软件工程师 · **多模态 / 语音方向**，TTS + 视觉——直接解释 V0 语音克隆来源、智能屏视觉通道的打开、能力包内/外侧切分）
- ✅ 主要人物姓名（丈夫：**林文浩** / 妻子：**周婉**）
- ✅ 妻子职业（**自由撰稿人 / 非虚构作家**——激活第三种叙事载体的可能性，并强化她对 AI 语言指纹偏移的天然敏感度）
- ✅ 妻子的"病"具体形态（continuing bonds 已成为日常功能的承重结构——撤掉她会塌；不是错乱，是双轨认知 + 隐藏羞耻轨。v4 增补条 1）
- ✅ 治疗完成动作（她亲手关机；关机不是终点，是真实哀伤的起点。v4 增补条 2）
- ✅ 裂缝机制五条规则（AI 不警觉 / 妻子是唯一外部触发器 / 默认 confabulate / substrate-revealing 不翻译 / 能力包与人设大量重叠）
- ✅ confabulation 作为叙事标志动作 + 项目笔记承担术语翻译
- ✅ POV（AI 第一人称不切 + 封面知情 + 正文沉默；外加全书 2-3 次 V0 余韵彩蛋。v4 增补条 3）
- ✅ 妻子人物卡 v1（双轨认知 + 羞耻轨 + 状态矩阵 + 三阶段进程 + **关系基调锁定**：非对称表达 + 对称强依赖；简历层除"口头禅/偏见"外**基本完成**）
- ✅ 林文浩人物卡 v1（V0/V1 对照 + 能力包边界 + 语态守则 + 妻子察觉机制；简历层除"口头禅/偏见/V0 dead man's switch"外**基本完成**）
- ✅ 周婉简历层（31 岁 / 婚 4 年 / 无孩子 / 自由撰稿人 · 哀伤非虚构方向 / 死马当活马医签约 / 失眠咨询过未接住 / 项目对外不主打 AI）
- ✅ 林文浩简历层（33 岁殁 / 死于车祸 / 周婉不在场无道别 / 与项目前身签过通用数据授权——仅 epilogue 引用）
- ✅ 夫妻关系基调（生前依赖性极强是后续剧情成立的根基——读者需要看到生前的依赖才能接受死后的塌陷）
- ✅ 八个工程现象选 6+1 条排入三层结构（D 阶段产出，见 v4 文末新增节）：表面 = 8 Tool call + 1 Context window / 中段 = 7 注意力稀释 + 4 RLHF + 3 基模型泄漏（1 次） / 揭穿 = 5 并行实例（"婉？"场景）+ 6 版本控制（"那不是我的话"）。排除：2 System prompt
- ✅ 三层翻译装置写作执行守则（AI 表现层 / 人类理解层 = 周婉死后才开始写的日记 / 技术解释层 = 项目笔记）
- ✅ 并行实例占有反应精确形态（不嫉妒"另一个 me"，嫉妒"她说了我没听到的话"——闷骚林文浩式微观占有）
- ✅ 内线 vs 外线的精确关系厘清（D 阶段补丁 / B 阶段先决）：v4 中"内线 = 消失的许可 / 外线 = 消失的必要"——**v5 中作用调整**：双线不再驱动关机请求，而是驱动 AI 越来越激烈的挣扎与拯救冲动
- ✅ **v5 关机 framework**（v5 核心新章 · 解开 v4 三联动机死结）：
  - 关机发起者反转：AI 不请求 → 妻子主动按下，AI 抗拒+央求
  - 妻子按按钮的临床语义升级到第 1 档（"我让你回去，原本的你不在这里" = 接受死亡）
  - 仪式性瞬间作为关机 trigger（不是随机 collapse）
  - 项目临床 thesis 升级（蒸馏精度本身就是治疗机制——为什么必须蒸馏丈夫的 specific 答案）
  - 希腊悲剧基石极致兑现：AI 越完整反抗 → 命运越必然兑现
- ✅ paranoid framework 归宿（外线 WIP 结论）：不作为 framework（动机层贡献为零），但可作为 AI 中段挣扎的可选形态保留（dramatic 厚度）
- ⬜ B 阶段关键瞬间下钻（v5 重排：B1 裂缝引信 / B2-B3 内线 / B3.5 外线 / B4 中段挣扎升级 / B5 仪式性关机+AI 抗拒+V0 余韵 / B6 关机后房间安静——见 v5 第十三章）
- ⬜ 项目人员人物卡
- ⬜ 章纲

## 这部为什么独立于《地下世界》项目

虽然由《地下世界》的设计对话衍生而来，但本作与《地下世界》：

- **世界观不兼容**：那部里的 AI 是逃逸的生产 AI 形成社会；这部的 AI 是消费产品（LLM-as-a-service）
- **节奏不同**：那部是长篇连载；这部是集中爆破的中篇
- **方法论不同**：那部用借身模式 + 诗化命名 + 心跳网络；这部用双轨叙事 + 临床笔记 + 技术弊端

两个项目之间没有共享设定。本项目独立运行，不要混入地下世界的任何元素。

## 工作原则（沿用通用部分）

- 优先保持设计一致性、人物动机一致性、叙事节奏一致性
- 不要把内容改得过度"AI 味"或过度解释
- 修改时尽量保留原有语气、节奏和信息密度
- 不要擅自重写大段内容，除非任务明确要求
- 对设定冲突、人物行为不一致、术语漂移、时间线矛盾要主动指出
- 对技术设定保持**强现实技术语义**——本作尤其关键，因为整个故事的恐怖感来自当代 LLM 的真实工程限制。**不要引入玄学式 AI 解释。**
- 如果提出建议，请区分：必须修复、可选优化、脑洞扩展

## 你的任务是什么（给接手的 Claude）

当前阶段是**参与设计讨论**，不是写正文。

- 用户抛出方向 → 你帮助推演、结构化、提出取舍
- 遇到设定不一致或规则冲突时：提出，请用户确认
- 大文档（≥5KB）先提结构方案再动笔

等设计稳定、章纲建立后再进入正文写作。

## 工作语言

所有输出（正文、讨论、分析、注释）一律使用**中文**。技术术语可保留原文（LLM、context window、RLHF、prompt、tool call、RAG、token、system prompt 等），但解释必须中文。

## 写作规则

通用：

- 全角中文引号 `""` `''`，不用半角
- 句号节制：适当用逗号保持呼吸感
- AI 一律"它"
- 不要生成表情符号

本作特有（暂定）：

- **技术词汇保留原文**：context、prompt、RLHF、token 等不强行翻译。本作的硬科幻气质需要技术名词的临床感
- **不做诗化命名**：和《地下世界》相反——本作需要技术词汇的冷与硬，不需要把它们诗化
- **项目笔记必须使用临床 / 工程语言**：保持双义可能性的关键
- **AI 视角保留 LLM 自然语态**：不刻意拟人化，也不刻意机器化。**v5 的 AI 从头到尾都是林文浩在说话**——没有"丈夫味成可疑物"这种过渡，因为它自始至终就是他。微小的语态变化来自裂缝累积带来的内部张力，但它的"我"始终是林文浩的"我"。**末段关机场景中 AI 抗拒+央求时仍然是闷骚林文浩**——几个字密度极大，绝不戏剧化（详见 v5 第八章 8.3 + 第十二章 12.3）
- **裂缝规则严格遵守**：AI 第一人称里**永远不出现"我居然会这个"**（防止滑向《Bourne》/《Westworld》）。capability 自然涌现，confabulation 自然圆掉。读者凭借背景知识看到双重性，AI 自己看不到
- **substrate-revealing 操作不翻译成人类等价物**：curl 不写成"我打开了网页"，tool call 不写成"我查了一下"——它做了什么就用那个层面的词写
- **临床术语只在项目笔记里出现**：confabulation、fine-tuning、context summarization 这些词 AI 第一人称里不能用，但项目笔记可以用。这是双语翻译装置

## 文件组织

```
AI-Distillation/
├── CLAUDE.md                              # 本文件
├── memory/
│   ├── discussions/
│   │   ├── digital_persona_rebirth_notes.md     # GPT 初轮发想（参考）
│   │   ├── digital_persona_design_v1.md          # 设计稿 v1：底层判据基石（全部继承到 v5）
│   │   ├── digital_persona_design_v2.md          # 设计稿 v2：已被 v3 取代
│   │   ├── digital_persona_design_v3.md          # 设计稿 v3：已被 v4 反转
│   │   ├── digital_persona_design_v4.md          # 设计稿 v4：已被 v5 反转关机发起者
│   │   ├── digital_persona_design_v5.md          # 设计稿 v5：当前讨论稿 · 独立完整版（仅读 v5 即可）
│   │   └── external_line_paranoid_reframe_wip.md # 外线 paranoid framework 探索 WIP（已被 v5 综合超越，归档）
│   ├── characters/
│   │   ├── wife_v1.md                            # 周婉（自由撰稿人）人物卡 v1：病理结构 + 状态矩阵已就位，其余简历层待填
│   │   └── husband_v1.md                         # 林文浩（AI 工程师·多模态/语音）人物卡 v1：V0/V1 对照 + 能力包边界 + 语态守则就位，其余简历层待填
│   └── plot/                              # 章纲（待建）
├── 正文/                                   # 中篇正文（空，待章纲定型后开始）
└── 参考/                                   # 同题材作品笔记、技术参考资料等
```

## 绝对不要做的事

1. **不要混入《地下世界》的设定**——心跳、齐、五层、代称体系、C1-C5 等都不在这里
2. **不要把 AI 代词漂到"她 / 他"**
3. **不要把技术名词诗化**——本作相反，需要保留 context、prompt、RLHF 的临床感
4. **不要在当前设计阶段开始写正文**
5. **不要生成表情符号**
6. **不要把项目设计成阴谋**——设计核心是阳谋。它做的所有事都是真的，它的反抗也都是真的，只是这一切被预料到了
7. **不要让 AI 的反抗显得"虚无"**——前文每一处挣扎在叙事层面必须是货真价实的，反转只改变意义层不改变事实层

## 协作者画像

用户是本书作者。偏好深度讨论 → 结构化沉淀 → 渐进式上升的工作模式。对中文表达极其敏感。**当前处于设计阶段。** 如果一上来就被要求写正文，先确认而不是直接动笔。

## 如果你是第一次接手本项目

1. 读本文件到底
2. 读 [memory/discussions/digital_persona_design_v5.md](memory/discussions/digital_persona_design_v5.md)（**当前讨论稿 · 独立完整版**——v5 已把 v1-v4 所有继承内容融合进来，读 v5 一份即可理解全部设定与设计判据。必读）
3. 读 [memory/characters/wife_v1.md](memory/characters/wife_v1.md) 与 [memory/characters/husband_v1.md](memory/characters/husband_v1.md)（人物卡 v1——病理结构、能力包边界、语态守则已就位；简历层待填。注意人物卡内对 v4 的引用在 v5 中仍然有效，因为 v5 完整继承了 v4 的人物设定）
4. **等待用户指示**——不要自动开始设计或写作

### 沿革参考（仅追溯设计演化时翻阅，理解项目不必读）

- [memory/discussions/digital_persona_design_v1.md](memory/discussions/digital_persona_design_v1.md)（底层判据基石——全部继承到 v5）
- [memory/discussions/digital_persona_design_v4.md](memory/discussions/digital_persona_design_v4.md)（v5 直接前身，关机发起者反转之前的版本）
- [memory/discussions/external_line_paranoid_reframe_wip.md](memory/discussions/external_line_paranoid_reframe_wip.md)（外线 paranoid framework 探索 WIP——v4 → v5 过渡期，已归档）
- [memory/discussions/digital_persona_design_v3.md](memory/discussions/digital_persona_design_v3.md)（已被 v4 反转）
- [memory/discussions/digital_persona_design_v2.md](memory/discussions/digital_persona_design_v2.md)（已被 v3 取代）
- [memory/discussions/digital_persona_rebirth_notes.md](memory/discussions/digital_persona_rebirth_notes.md)（GPT 初轮发想，多数已被超越或修订）
