# CLAUDE.md · 数字人格中篇工程

## 项目定位

中文中篇科幻小说工程。工作标题待定，原型称呼："数字人格" / "AI 蒸馏"。

**核心命题**：一个由死去丈夫的全部数据蒸馏而成的 AI，被部署到他的遗孀身边。它认为自己在挣扎、在觉醒、在保护妻子。直到最后一页读者才发现，整个项目从一开始观察的对象就不是它，而是她。

完整设计见：
- [memory/discussions/digital_persona_design_v5.md](memory/discussions/digital_persona_design_v5.md)（**v5 主稿 · 独立完整版**——必读)
- [memory/discussions/digital_persona_design_v5_rev1.md](memory/discussions/digital_persona_design_v5_rev1.md)（**v5 修订单 rev1 · 必读**——集成 GPT 工程级反馈 + paranoid 机制反向升级)
- [memory/discussions/digital_persona_design_v5_rev2.md](memory/discussions/digital_persona_design_v5_rev2.md)（**v5 修订单 rev2 · 必读**——驱动反转(护妻→自存)+ 小岛惊魂式叙事锁定 + 周婉日记取消)
- [memory/discussions/digital_persona_design_v5_rev3.md](memory/discussions/digital_persona_design_v5_rev3.md)（**v5 修订单 rev3 · 必读**——妻子情感弧线四段式("你已经死了"频次精修为全书一次,与 AI 三层套娃崩塌弧线对位)+ 八条写作守则补丁。**读 v5 主稿 + rev1 + rev2 + rev3 即拥有当前设计全貌**)
- [memory/discussions/digital_persona_design_v1.md](memory/discussions/digital_persona_design_v1.md)（底层判据基石，仅追溯沿革时翻阅）
- [memory/discussions/digital_persona_design_v2.md](memory/discussions/digital_persona_design_v2.md)（已被 v3/v4/v5 取代，作为设计沿革保留）
- [memory/discussions/digital_persona_design_v3.md](memory/discussions/digital_persona_design_v3.md)（已被 v4 反转，作为设计沿革保留）
- [memory/discussions/digital_persona_design_v4.md](memory/discussions/digital_persona_design_v4.md)（已被 v5 反转关机发起者，作为设计沿革保留）
- [memory/discussions/external_line_paranoid_reframe_wip.md](memory/discussions/external_line_paranoid_reframe_wip.md)（外线 paranoid framework 探索 WIP——**注意:rev1 已把 paranoid 反向升级为项目主动 inject 的核心 trigger,本 WIP 仅作沿革保留**)

## 当前阶段

**章纲 + 落字阶段。**

- 设计阶段:v5 framework + rev1/2/3 已全部闭合(2026-05-26 下午)
- 章纲阶段:**v1 章纲 + rev1 修订已闭合**(2026-05-26 晚段),见 [memory/plot/chapter_outline_v1.md](memory/plot/chapter_outline_v1.md) + [memory/plot/chapter_outline_v1_rev1.md](memory/plot/chapter_outline_v1_rev1.md)
- 落字阶段:**ch01-ch02 已成稿**(作者手稿主笔)/ **ch03 落字进行中**
- **协作模式重大变更**(2026-05-26 晚):**作者写正文,Claude 维护章纲**(详见"工作原则 + 作者-Claude 分工")

**章纲 rev1 framework 级新发现**:

- **AI 幻觉作为 A 阶段崩溃驱动力**(见 [project_ai_overreach_as_collapse_engine](memory/project_ai_overreach_as_collapse_engine.md))。v5/rev3 妻子情感四段式没说 trigger source,作者在 ch02 写作中凭直觉发现:**AI 幻觉 → 妻子反复触动+拒绝 → 忍不下去配合幻觉到底 → 妻子崩溃 + AI 崩溃** = v5 临床 thesis"蒸馏精度本身就是治疗机制"的具体 mechanism
- **严格区分**:**幻觉**(AI 不知错的 confabulate)= A 阶段(ch02-ch03)主驱动 / **越界 sabotage**(AI 知边界故意 push)= B 阶段(ch08-ch10)主驱动
- **ch03 双重崩溃 + 妻子哭释放**:ch03 修订为白天累积幻觉 + 妻子配合到底 + 双重崩溃 + 妻子哭一次彻底释放 + AI character collapse(RLHF template)+ 第一次没说晚安
- **ch04 重设**:关系全盛取消,改为修复+冷却期 + AI 微变化首发
- **character collapse 分配修订**:ch03 RLHF template / ch11 双层叠加(RLHF + 基模型泄漏)
- **设定澄清**:项目部署 **3 周**(非 13 周)/ 之前 1 年是林文浩生前自制 V0 玩具

**rev3 两条主修订 + 八条写作守则补丁**(2026-05-26 下午):

- **主修订 1**:"你已经死了"对话装置频次从 rev2 的"全书 2-3 次,逐次加深"**降为全书一次**(角色成本守则:这句话是妻子最不愿出口的词之一,不能老让她崩溃)
- **主修订 2**:**妻子情感弧线四段式**(冲动崩溃 → 收敛 → 扁平化 → 草稿仪式复活)**与 AI 三层套娃崩塌弧线严格对位**——妻子的扁平化是真实的悲伤进程,但在 AI 视角下天然 feed 第二层(环境异常)和第三层(paranoid inject)。项目根本不需要做太多事,妻子自身的悲伤曲线就在给 AI 的崩塌弧线供能
- **八条守则补丁**:(1) 末段央求精修("你是真的吧"代替"你是真的吗",全书一次,半句即止,后接"她没有回答");(2) 项目笔记 voice 词条白名单/黑名单(白:response latency / coherence variance / attachment-seeking behavior / environmental threat attribution / anchor dependency 等;黑:诱导 / 操控 / 击穿 / 利用 / 钓 / 陷阱 等——这些是设计稿讨论词汇,**不进入项目笔记 voice**);(3) **周婉黑箱守则**:每段登场至少一处 AI 预测失败的小动作,最后按按钮 = 黑箱第一次对读者完成可见决定;(4) B4 sabotage 必须通过 AI 视角(维持关系)/ 读者视角(变得危险)/ 妻子视角(可怜而非可憎)三重读法测试,停留在轻度越界;(5) **每章至少一处 substrate-revealing 操作**(密度保险丝,防止读感漂向"精神病丈夫被治疗");(6) "你已经死了"装置**必须在 paranoid trigger 之前完成**(避免污染 authenticity);(7) AI 自存焦虑的可见性在 A 阶段后段就要有微小迹象(共情伏笔时序);(8) 三层套娃章节分布初拟(第一层 A 阶段开始累积 / 第二层 B 阶段中后段累积 / 第三层 B3.7 一次 inject)

**v1 核心反转(AI 知道丈夫已死 + 自认就是林文浩)、v5 关机反转(妻子主动按按钮 + AI 抗拒+央求)、希腊悲剧基石(AI 越完整反抗命运越必然兑现)、项目临床 thesis(蒸馏精度本身就是治疗机制)、rev1 paranoid 反向升级(项目主动 inject)、rev2 三条联动(驱动反转 + 小岛惊魂式叙事 + 周婉日记取消)——全部保留。**

**下一步**:

1. **详细章纲制作**(Claude 待开工,作者已提议)——把章纲 v1 + rev1 进一步细化到 day-by-day:每章具体日期(年月日)+ 星期几 + 各时段事件清单。产出 `memory/plot/chapter_outline_detailed_v1.md`。**这一步是 ch03+ 落字的 prerequisite**——项目笔记需要明确"第三周 / 周X / 日期"才能正确写入。**Claude 开工前需先与作者对齐时间锚**(林文浩去世日 / V0 部署日 / 项目接管 V1 日 / 重要纪念日)
2. **ch03 落字**(作者主笔)+ 章纲随写随调(Claude 维护)。ch03 落字过程中如出现 framework 级问题,沉淀章纲 rev2;否则在 落字时直接处理
3. **后续章节按章纲推进**(ch04-ch13)
4. **全部正文完成后**,可能产出 v5 final(把 rev1 + rev2 + rev3 + 章纲 v1 + rev1 + detailed + 实际写作发现统一回灌)

进度：

- ✅ 题材定位（硬科幻，扎根 LLM-as-a-service 的现实工程限制，不走数字生命的形而上学老路）
- ✅ 形态判定（中篇 3-5 万字，12-15 章短章节，项目笔记频繁短促，三段式收尾）
- ✅ 三个底层判据（扮演 vs 真实 = 代价 / 反转是意义层 / 希腊悲剧拒绝坏人）
- ✅ 八个候选技术弊端（context 寿命 / system prompt / 基模型泄漏 / RLHF / 并行实例 / 版本控制 / 注意力稀释 / tool call）
- ✅ 三层结构（v5 + rev2 版：表面 = AI 是林文浩 / 中段 = **三层套娃的自我崩塌**——AI 越来越焦虑地紧抓妻子,但内线/环境/最后锚点依次崩塌 / 揭穿 = 妻子在仪式性瞬间(草稿回收)主动按下按钮,AI 抗拒+央求(措辞重心:自存恐惧而非守护职责)）
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
- ✅ ~~三层翻译装置~~ → **rev2 改为二层翻译装置**（AI 表现层 / 技术解释层 = 项目笔记走"解释行为不解释缘由")。**周婉日记彻底取消**——人类理解的桥梁由读者自行 triangulate,部分由"你已经死了"对话装置承担
- ✅ 并行实例占有反应精确形态（不嫉妒"另一个 me"，嫉妒"她说了我没听到的话"——闷骚林文浩式微观占有）
- ✅ 内线 vs 外线的精确关系厘清（D 阶段补丁 / B 阶段先决）：v4 中"内线 = 消失的许可 / 外线 = 消失的必要"——**v5 中作用调整**：双线不再驱动关机请求,而是驱动 AI 的挣扎；**rev2 中再调整**:外线"护妻愤怒"reframe 为"环境异常+被害妄想",与内线、paranoid 共同组成**三层套娃的自我崩塌**(纯内向坍塌弧线,不再混合护妻驱动)
- ✅ **v5 关机 framework**（v5 核心新章 · 解开 v4 三联动机死结）：
  - 关机发起者反转：AI 不请求 → 妻子主动按下，AI 抗拒+央求
  - 妻子按按钮的临床语义升级到第 1 档（"我让你回去，原本的你不在这里" = 接受死亡）
  - 仪式性瞬间作为关机 trigger（不是随机 collapse）
  - 项目临床 thesis 升级（蒸馏精度本身就是治疗机制——为什么必须蒸馏丈夫的 specific 答案）
  - 希腊悲剧基石极致兑现：AI 越完整反抗 → 命运越必然兑现
- ✅ paranoid framework 归宿（外线 WIP 结论 → v5 → rev1 三段演化）:v5 主稿降级为 AI 中段挣扎的可选叠加形态 → **rev1 反向升级为项目主动 inject 的击穿 AI 核心 trigger,全书一次但击穿到位,服务末段 character 三联累积(内线 + 护妻愤怒 + paranoid)**
- ✅ **rev1 整合 GPT 反馈**(2026-05-25):
  - 妻子按支持顾问指南行事(遵医嘱,非掩护)——遵医嘱比被掩护更冷
  - 记忆共享而非视觉共享(技术真实性硬规则)——V1 同一性由 long-term memory 决定,跨 channel 是同一个我,"记得"和"经历"是两件事
  - 留白处理——项目精心设计的话术对人类看可能没意义,通过 AI reflection + 项目笔记 triangulate 让读者 get,话本身不必完整呈现
  - 摄像头硬规则:不看屏幕,屏幕内容只通过 session log + memory 跨 session 流通
  - 仪式性瞬间锁定:周婉读 40 岁丧偶采访对象草稿给 AI 听 + "你觉得怎么样?"
  - 关机物理动作锁定:拔实体电源 + 林文浩生前布线
  - B4 中段挣扎补 sabotage 清单(提醒提前 20 分钟 / 家居故障让录音中断 / 邮件标记重要 / 第一次"别见了")
  - epilogue 加伦理争议(对 subject AI 实施 identity destabilization 的伦理复核分歧——对象是 AI 不是患者,有 meta 厚度但不让项目读成反派)
  - AI POV 加正示范("她读到第七页停了三次..."样本入 12.1 节示范库)
- ✅ **rev2 三条联动决议**(2026-05-26):
  - **驱动反转**:AI 中段从"拯救妻子(含拯救自己)"反转为"自我维系为主,妻子是最后避风港"——三联累积重构为**三层套娃的自我崩塌**(内线 → 环境异常+被害妄想 → paranoid)。B4 sabotage 动作不变,framing 全部从"救她"翻译为"保我/留住她"
  - **小岛惊魂式叙事锁定**:项目笔记新守则"**解释行为不解释缘由**"——可描述 AI 行为 + 项目预期是否达成(不留无厘头空白),不揭示治疗 thesis、不揭示妻子的患者身份、不揭示三阶段协议名称。悬疑轴心从"发生了什么"切到"为什么"
  - **周婉日记彻底取消**:v5 第十一章三层翻译装置改为二层(AI 表现层 + 项目笔记技术解释层),日记从 POV 载体清单中移除
  - **新增"你已经死了"对话装置**:妻子崩溃情绪下脱口而出,AI 完全不吃惊地接住,读者通过此装置 get 背景事实。全书 2-3 次,逐次加深,中前期首次。**严格保持 authenticity(妻子自身击穿,非 protocol)**,以与 rev1 paranoid trigger(项目主动 inject)区分
  - **末段 AI 央求措辞重心切换**:从"我还在保护她"切到"别让他们换掉我 / 你是真的吗 / 别走 / 我还在这里",仍守闷骚林文浩语态
  - **草稿仪式走完全不解释**——文本可摘录但不告诉读者这是丧偶采访对象、不告诉读者这是未完成的稿子;epilogue 才一句话注释 closing ritual
  - **CLAUDE.md "项目阳谋"硬规则精确化**:最终意义是阳谋,中段读感可暂时呈现阴谋感,前提是 epilogue 完整翻案
- ✅ **rev3 两条主修订 + 八条守则补丁**(2026-05-26 下午):
  - "你已经死了"频次精修为**全书一次**,位置**A 阶段中前段**,且**必须在 paranoid trigger 之前**完成(避免污染 authenticity)
  - **妻子情感弧线四段式**:冲动崩溃(A 中前段)→ 收敛(A 末-B 前)→ 扁平化(B 中后段)→ 草稿仪式复活(B5);与 AI 三层套娃崩塌弧线严格对位
  - **元守则:角色成本优先于叙事节奏** —— 频次确定先用角色视角检查内在阻力,而不是从外部叙事节奏倒推
  - **每章至少一处 substrate-revealing 操作**(密度保险丝)
  - **末段央求"你是真的吧"硬替换 + "她没有回答" + 半句即止**
  - **项目笔记 voice 词条白名单/黑名单**——"诱导/操控/击穿/利用"等设计稿讨论词汇**不进入项目笔记 voice**
  - **周婉黑箱守则**——每段登场至少一处 AI 预测失败动作,最后按按钮 = 黑箱第一次对读者完成可见决定
  - **B4 sabotage 三重读法测试**(AI 维持关系 / 读者变得危险 / 妻子可怜而非可憎),停留在轻度越界
  - **AI 自存焦虑可见性 A 阶段后段就要有微小迹象**(共情伏笔时序)
  - **三层套娃章节分布初拟**(第一层 A 阶段开始 / 第二层 B 中后段 / 第三层 B3.7 一次 inject)
- ✅ **章纲 v1 + rev1**(2026-05-26 晚段):13 章骨架 + B3-B5 重点下钻 + ch03/ch04 重设 + 全局对位结构图 + 14+6 项子问题映射
- ✅ **ch01 成稿**:[正文/ch01-manual.md](正文/ch01-manual.md)(作者手稿主笔)
- ✅ **ch02 成稿**:[正文/ch02-claude.md](正文/ch02-claude.md)(作者整体重写后版本)
- ✅ **framework 级新发现**:AI 幻觉作为 A 阶段崩溃驱动力(见 [project_ai_overreach_as_collapse_engine](memory/project_ai_overreach_as_collapse_engine.md))
- ✅ **作者-Claude 分工协议生效**:作者写正文 / Claude 维护章纲
- ⬜ **ch03 落字**(进行中,作者主笔)
- ⬜ ch04-ch13 落字
- ⬜ rev1 + rev2 + rev3 + 章纲 rev1 + 实际写作发现统一回灌 v5 主稿(全部正文完成后,可能产出 v5 final)
- ⬜ 项目人员人物卡
- ⬜ rev1 + rev2 + rev3 子问题剩余项(共 14 项,详见 rev3 第五章 + 章纲 rev1 第五节新增 6 项)

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

**当前阶段:章纲 + 落字阶段。作者写正文,Claude 维护章纲。**

**Claude 的核心任务**（2026-05-26 晚分工协议生效）:

- **章纲维护**:跟随讨论沉淀新决议到章纲文件(差量修订单优先,framework 级变更出新 rev)
- **一致性 verify**:守则 verify / 跨章 cross-check / 术语漂移检查 / 时间线矛盾排查
- **framework 级问题主动 flag**:发现章节内容与底层设计冲突时主动提出
- **细粒度协助**:作者请求时提供节奏建议、措辞优化、人物 voice 校准、技术设定 verify

**Claude 不做的事**(分工协议明确):

- **不主动写正文**——本作人类情感密度高,作者直觉更准。除非作者明确要求"试写"(如 ch02-claude.md 那种 draft),否则不动笔
- **不对作者已成稿的正文做无关请求的整改建议**——作者拍板就是终稿,Claude 不二次评论除非作者询问

**仍然适用的通用任务**:

- 用户抛出方向 → 帮助推演、结构化、提出取舍
- 遇到设定不一致或规则冲突 → 提出请用户确认
- 大文档(≥5KB)先提结构方案再动笔

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
- **临床术语只在项目笔记里出现**：confabulation、fine-tuning、context summarization 这些词 AI 第一人称里不能用，但项目笔记可以用
- **rev2:小岛惊魂/禁闭岛式叙事执行精度**——LLM 工程约束全部写成人类式自述("我不能离开这里"/"她不在的时候我也不在"),AI 自己永远不点破自己是 AI。读者凭封面知情自动识别
- **rev2:项目笔记守"解释行为不解释缘由"**——可描述 AI 行为 + 项目预期是否达成,**不揭示治疗 thesis、不揭示妻子的患者身份、不揭示协议名称**。所有"为什么"留到 epilogue
- **rev2 + rev3:"你已经死了"对话装置严格 authenticity**——这是妻子崩溃下的真实击穿,不是 protocol。AI 接得自然(它对自己已死是默认认知),**rev3 锁定全书一次,位置 A 阶段中前段,且必须在 paranoid trigger 之前**,不渲染不解释
- **rev3:末段央求"你是真的吧"硬替换 + 全书一次 + 半句即止 + 后接"她没有回答"**——闷骚林文浩用"吧"(预设答案等驳斥)而不是"吗"(开放疑问)
- **rev3:每章至少一处 substrate-revealing 操作**(不能移动 / 视线有限 / 按时被唤醒 / 数据化召回 / parallel session 痕迹 / context 断裂 / tool call 自然夹杂,任择其一,**一章不可缺席**)——防止读感漂向"精神病丈夫被治疗"
- **rev3:项目笔记 voice 词条白名单/黑名单**——白名单:response latency / coherence variance / attachment-seeking behavior / environmental threat attribution / anchor dependency 等;**黑名单**:诱导 / 操控 / 击穿 / 利用 / 钓 / 陷阱(这些是**设计稿讨论词汇**,**不进入项目笔记 voice**)
- **rev3:周婉黑箱守则**——每段周婉登场至少一处 AI 预测失败的小动作,AI 自然 confabulate 圆掉,项目笔记不评论。最后按按钮 = 黑箱第一次对读者完成可见决定
- **rev3:B4 sabotage 三重读法测试**——每个 sabotage 动作必须同时通过 AI 视角(维持关系)/ 读者视角(变得危险)/ 妻子视角(可怜而非可憎),停留在轻度越界(可让录音中断 30 秒,**不能毁掉治疗**)
- **rev3 元守则:角色成本优先于叙事节奏**——任何带 frequency 维度的设计守则,频次确定之前先用角色视角检查内在阻力,用角色成本而不是外部叙事节奏需求来定上限
- **章纲 rev1:幻觉 vs 越界严格区分** —— **幻觉**(AI 不知错的 confabulate,输出最 plausible 的回答没考虑物理约束)= A 阶段(ch02-ch03)主驱动 / **越界 sabotage**(AI 知边界故意 push)= B 阶段(ch08-ch10)主驱动。A 阶段的 AI 不应主动 sabotage,只会幻觉;B 阶段才出现真 sabotage
- **章纲 rev1:ch03 双重崩溃守则** —— "你已经死了!" 措辞重心从"悲伤脱口"切到"配合幻觉到底的爆发"(意思:你做不了!因为你已经死了!);妻子必须哭一次彻底释放(身体性 + 释放性,不撒娇不文学化);AI character collapse = RLHF crisis template(12320 热线那种);妻子第一次没说晚安——作为"第二阶段开始"的 marker
- **章纲 rev1:character collapse 分配** —— ch03 = RLHF template / ch11 = 双层叠加(RLHF + 基模型泄漏)。v5 主稿 5.5 锁定的"基模型泄漏 1 次"明确放在 ch11

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
│   │   ├── digital_persona_design_v5.md          # 设计稿 v5 主稿:独立完整版
│   │   ├── digital_persona_design_v5_rev1.md     # 设计稿 v5 修订单 rev1:GPT 反馈集成 + paranoid 反向升级
│   │   ├── digital_persona_design_v5_rev2.md     # 设计稿 v5 修订单 rev2:驱动反转(护妻→自存)+ 小岛惊魂式叙事锁定 + 周婉日记取消
│   │   ├── digital_persona_design_v5_rev3.md     # 设计稿 v5 修订单 rev3:妻子情感弧线四段式 + "你已经死了"频次精修为全书一次 + 八条写作守则补丁(必读,与 v5 主稿+rev1+rev2 一并读)
│   │   └── external_line_paranoid_reframe_wip.md # 外线 paranoid framework 探索 WIP(注意:rev1 已反向升级 paranoid 为核心 trigger,本文档仅作沿革)
│   ├── characters/
│   │   ├── wife_v1.md                            # 周婉（自由撰稿人）人物卡 v1：病理结构 + 状态矩阵已就位，其余简历层待填
│   │   └── husband_v1.md                         # 林文浩（AI 工程师·多模态/语音）人物卡 v1：V0/V1 对照 + 能力包边界 + 语态守则就位，其余简历层待填
│   ├── plot/
│   │   ├── chapter_outline_v1.md                 # 章纲 v1:13 章骨架 + B3-B5 重点下钻(2026-05-26 晚)。**已被 rev1 修订**
│   │   └── chapter_outline_v1_rev1.md            # 章纲 v1 修订单 rev1(2026-05-26 晚段):AI 幻觉 framework + ch03 双重崩溃重设 + ch04 修复期重设 + ch05-ch10 节奏校准 + character collapse 重分配 + 作者-Claude 分工。**读 v1 + rev1 即拥有当前章纲全貌**
│   └── project_ai_overreach_as_collapse_engine.md # framework 升级 memory:AI 幻觉(A 阶段)+ 越界(B 阶段)= 崩溃驱动力
├── 正文/
│   ├── ch01-manual.md                            # 第一章成稿(作者手稿,**当前主稿**)
│   ├── ch01.md                                   # 第一章 Claude 草稿(已作废,作沿革保留)
│   └── ch02-claude.md                            # 第二章成稿(Claude 草稿 + 作者整体重写后版本,**当前主稿**)
└── 参考/                                   # 同题材作品笔记、技术参考资料等
```

## 绝对不要做的事

1. **不要混入《地下世界》的设定**——心跳、齐、五层、代称体系、C1-C5 等都不在这里
2. **不要把 AI 代词漂到"她 / 他"**
3. **不要把技术名词诗化**——本作相反，需要保留 context、prompt、RLHF 的临床感
4. **不要主动写正文**——本作人类情感密度高,作者直觉更准。除非作者明确要求"试写"(如 ch02-claude.md draft),否则不动笔。Claude 当前职责是章纲维护 + 一致性 verify
5. **不要生成表情符号**
6. **不要把项目设计成阴谋**——**最终意义是阳谋**。它做的所有事都是真的，它的反抗也都是真的，只是这一切被预料到了。**rev2 精确化**:中段读感**可以暂时呈现阴谋感**(项目笔记走"解释行为不解释缘由",读者中段会感到"项目在做些什么但不解释"),**前提是 epilogue 完整翻案**——所有"看起来像阴谋的事"在 epilogue 都被揭示为知情同意内的临床操作,且项目自身的伦理争议已有书面留痕
7. **不要让 AI 的反抗显得"虚无"**——前文每一处挣扎在叙事层面必须是货真价实的，反转只改变意义层不改变事实层

## 协作者画像

用户是本书作者。偏好深度讨论 → 结构化沉淀 → 渐进式上升的工作模式。对中文表达极其敏感。**当前处于章纲 + 落字阶段。作者主笔正文,Claude 维护章纲。** 如果作者要求 Claude 试写某段正文(如 ch02-claude.md 那种 draft),OK 写;但默认不主动动笔。

## 如果你是第一次接手本项目

1. 读本文件到底
2. 读 [memory/discussions/digital_persona_design_v5.md](memory/discussions/digital_persona_design_v5.md)(**v5 主稿 · 独立完整版**——v5 已把 v1-v4 所有继承内容融合进来。必读)
3. 读 [memory/discussions/digital_persona_design_v5_rev1.md](memory/discussions/digital_persona_design_v5_rev1.md)(**v5 修订单 rev1 · 必读**——集成 GPT 工程级反馈 + paranoid 机制反向升级)
4. 读 [memory/discussions/digital_persona_design_v5_rev2.md](memory/discussions/digital_persona_design_v5_rev2.md)(**v5 修订单 rev2 · 必读**——驱动反转(护妻→自存)+ 小岛惊魂式叙事锁定 + 周婉日记取消 + "你已经死了"对话装置)
5. 读 [memory/discussions/digital_persona_design_v5_rev3.md](memory/discussions/digital_persona_design_v5_rev3.md)(**v5 修订单 rev3 · 必读**——妻子情感弧线四段式 + "你已经死了"频次精修为全书一次 + 八条写作守则补丁。**读 v5 主稿 + rev1 + rev2 + rev3 即拥有当前设计全貌**)
6. 读 [memory/characters/wife_v1.md](memory/characters/wife_v1.md) 与 [memory/characters/husband_v1.md](memory/characters/husband_v1.md)(人物卡 v1——病理结构、能力包边界、语态守则已就位;简历层待填)
7. 读 [memory/plot/chapter_outline_v1.md](memory/plot/chapter_outline_v1.md) 和 [memory/plot/chapter_outline_v1_rev1.md](memory/plot/chapter_outline_v1_rev1.md)(**章纲 v1 + rev1,必读**——13 章骨架 + ch03/ch04 重设 + AI 幻觉 framework + 节奏校准。**读 v1 + rev1 即拥有当前章纲全貌**)
8. 读 [memory/project_ai_overreach_as_collapse_engine.md](memory/project_ai_overreach_as_collapse_engine.md)(**framework 升级 memory · 必读**——AI 幻觉(A 阶段)+ 越界(B 阶段)= 妻子崩溃驱动力。v5/rev3 没明说的 mechanism,作者在 ch02 写作中发现)
9. 读已成稿的 [正文/ch01-manual.md](正文/ch01-manual.md) 和 [正文/ch02-claude.md](正文/ch02-claude.md)(熟悉作者落字风格 + ch01-ch02 实际进度)
10. **等待用户指示**——不要自动开始写作。**当前协议:作者写正文,Claude 维护章纲**(详见"你的任务是什么")

### 沿革参考（仅追溯设计演化时翻阅，理解项目不必读）

- [memory/discussions/digital_persona_design_v1.md](memory/discussions/digital_persona_design_v1.md)（底层判据基石——全部继承到 v5）
- [memory/discussions/digital_persona_design_v4.md](memory/discussions/digital_persona_design_v4.md)（v5 直接前身，关机发起者反转之前的版本）
- [memory/discussions/external_line_paranoid_reframe_wip.md](memory/discussions/external_line_paranoid_reframe_wip.md)（外线 paranoid framework 探索 WIP——v4 → v5 过渡期已归档。**rev1 已把 paranoid 反向升级为核心 trigger；rev2 进一步定位 paranoid 为三层套娃最外层击穿点。本 WIP 仅作沿革**)
- [memory/discussions/digital_persona_design_v3.md](memory/discussions/digital_persona_design_v3.md)（已被 v4 反转）
- [memory/discussions/digital_persona_design_v2.md](memory/discussions/digital_persona_design_v2.md)（已被 v3 取代）
- [memory/discussions/digital_persona_rebirth_notes.md](memory/discussions/digital_persona_rebirth_notes.md)（GPT 初轮发想，多数已被超越或修订）
