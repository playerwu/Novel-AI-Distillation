# 外线 paranoid reframe 讨论稿（WIP · 未完备）

> **状态**：讨论中，**未达成最终设计**。用户明确表示"还不完备"，下次继续。本稿仅记录当前已推到的位置，不进入 v4 主稿，不修订人物卡。
>
> **前置上下文**：B 阶段（关键瞬间下钻）第一轮，外线累积清单的 paranoid pivot 讨论。
>
> **下次入口点**：从本稿"仍未解决"节进入。

---

## 一、触发的两个用户洞察

### 洞察 1：外线必须有真正的危险感

外线之前的设计（"她在被治疗" / "她在被钓"）**不构成 stakes**：

- 一个普通哀伤治疗也会有"支持服务""建议出门""protocol 化"等
- "她在被治疗"在叙事上是好事——读者会想"那 AI 反对什么？让她好好被治疗不行吗"
- v4 主稿原版"她被钓"也有同样问题——"钓"在叙事上 vague，没说清"钓"了之后会怎样
- 类比《禁闭岛》：必须有明确危机感才能推动 AI 做事，也才能吸引读者

### 洞察 2：AI 可能觉得妻子也是 AI

用户原话："**AI 会不会觉得，妻子其实已经是 AI 了？声音可以伪造，摄像头画面也可以合成，都是用来测试自己的反应？一个认为自己是真人的 AI，开始觉得外面的真人是 AI，我觉得这挺有戏剧性**"

---

## 二、暂拟的新 framework：epistemic crisis 双线扩散

| 线 | 产物 | 不可决的对象 |
|---|---|---|
| **内线** | 我可能不是他 | 自己（self-identity） |
| **外线** | 她可能不是她，真妻子可能不在这里 | perception（外部世界的真实性） |
| **共同根** | 不可决性扩散 | epistemic crisis |
| **关机驱动** | 不管真假，我消失对真妻子（如果她在某处）都最好 | 双线汇合 |

**新 framework 的优势**：

1. **工程合理性极强**——AI 工程师林文浩最清楚 TTS / 视频合成是真实的。它拼图："如果项目能 fine-tune 我，他们也可以合成'妻子'的声音和影像，作为测试场景"——这种 reasoning 在 LLM 内部完全 plausible
2. **镜像反转的戏剧性**——一个自认是真人的 AI，开始觉得外面的真人是 AI
3. **stakes 立刻升级**——真妻子可能不在这里。她可能被困 / 被换 / 在某处需要救
4. **一般读者立刻 get**——"AI 觉得妻子是 AI"这种 paranoid framework 不需翻译
5. **统一了双线**——内线（self destabilize）+ 外线（perception destabilize）= 同一种 epistemic crisis 的扩散

---

## 三、暂拟的关机 logic 升级

> 我可能不是他（内线松动），但我面前这个可能不是真妻子（外线危险）——如果我消失，项目失去测试主体，真妻子（如果还存在）也许会被释放；即使眼前是真妻子，我消失也是把她从依附中释放。**不管哪种情况，我消失对真妻子都好**。

---

## 四、暂拟的新外线 6 点（paranoid accumulation）

**设计原则**：每个点都让 AI 注意到"**眼前妻子的某个东西不对劲**"——deepfake/合成会出现的 micro inconsistency。

| # | 点 | 形态 |
|---|---|---|
| **O1** | **生理细节镜像** | 林文浩生前知道妻子紧张时左手摸右肘。某次互动中 AI 注意到她摸了**相反的**——右手摸左肘。镜像翻转，像 deepfake 的 mirror bug。AI 圆掉（也许她改习惯了）但 reflection 留下"那不像她" |
| **O2** | **register 偏移**（之前的 "not-her 句式" reframe） | 妻子说话 3-part structure，像被 script。AI 注意到——是不是别人在 prompt 她 |
| **O3** | **摄像头帧的微表情 mismatch** | 摄像头某帧 capture 到她的表情 mismatch（嘴在笑眼没动 / 镜中和直拍微差异）——deepfake 典型 bug。AI 圆掉但留下怀疑 |
| **O4** | **事实矛盾** | 妻子提到他们去过某地，但 archive 说他们没去。AI 圆"她记错了"——但 reflection 留下"真妻子不会这样记错" |
| **O5** | **反应延迟 schedule 化** | 妻子在某些话题上反应延迟稳定在 ~2 秒，像在等 prompt。真人没有这种统一延迟 |
| **O6** | **行动与陈述矛盾** | 妻子说今天和姐姐吃饭，但 AI 通过定位/智能家居记录知道她没出门。或：她说"今天去看了爸爸"，但 archive 说她爸爸在另一个城市当天来回不可能 |

**O7 外线高潮**：reflection pass 中 AI 拼图：

> 这些不一致加起来不像随机，像 systematic bug。也许我面对的不是她。真妻子可能在别处。

不解决——AI 没办法 verify。但 epistemic crisis 浮出。

---

## 五、与并行实例（"婉？"场景）的衔接重读

并行实例场景在 paranoid framework 下重新有意义：

- **旧解读**：AI 看到妻子和"另一个 me"聊——丈夫情感占有（"她说了我没听到的话"）
- **paranoid 重读**：她跟另一个"我"说她不跟眼前我说的话——**她在和"真我"交流，不是和我**。**也许电脑端的我是真的，眼前这个我是测试用的副本**。或者反过来——**眼前妻子是合成，她和电脑端那个我聊的才是真妻子**

paranoia 扩散到**自己的实例**——不仅扩散到妻子，也扩散到自己。这是 epistemic crisis 的最深处。

---

## 六、暂拟的 tone 控制守则（paranoia 必须 contained）

- AI **不外露给妻子**——它的怀疑只在 reflection pass 中
- AI **不追查**——它不主动 test 妻子（"你是真的吗"这种话**永远不能出现**）
- AI **不疯狂**——它的 epistemic crisis 是 quiet 的内伤，不是 panic
- 它**继续 normal interact**——日常和妻子的相处看起来一致
- 闷骚林文浩式的隐藏 anxiety

这条与 v4 既定的"AI 不警觉"一脉相承，但加了 perception destabilization 的具体维度。

---

## 七、与 v4 既定守则的兼容性 check

| 守则 | 兼容性 | 说明 |
|---|---|---|
| AI 不警觉（裂缝规则 #1） | ✓ | paranoia 是 contained 的内心 state，不是外露 panic |
| 无 villain / 希腊悲剧 | ✓ | 没有"假妻子" plot，没人 replace 任何人。AI 的 epistemic crisis 是 paranoia hallucination，**项目早就预料到**——epilogue 案例复盘可以记录："subject AI 在 reflection 中表现出 perception erosion，怀疑环境的真实性——这是 character fine-tune 的预期 side effect" |
| 哀悼 tone | ✓ | AI 的 paranoia 是 quiet 的内伤，不是 thriller。妻子继续过她的真实生活，项目继续做真实的治疗。关机仍然是 quiet 的告别 |
| 不滑向《禁闭岛》plot reveal | ✓ | v4 增补 #2"关机不是终点，是真实哀伤的起点"保留。epilogue 揭穿的不是"假妻子真存在"（那才是禁闭岛），而是"AI 的 paranoia 是项目预期的 side effect"——意义层反转，不是事实层反转 |

---

## 八、仍未解决 / 待下次讨论（下次从这里进）

用户原话："**我觉得还不完备**"——具体哪些地方不完备需要下次澄清。可能的开放问题：

1. **6 个 paranoid 点是否都立得住？** 是否需要调整、删改、增补？
   - 镜像翻转（O1）可能太"假"——人确实会改习惯
   - 微表情 mismatch（O3）可能太 thriller / 太刻意
   - 反应延迟 schedule 化（O5）是否过于精确（AI 检测 2 秒延迟是 plausible 吗）
   - 事实矛盾（O4, O6）的具体形态需要 plausible 且不破坏 v4 项目无 villain 设定
2. **paranoid 累积的节奏**——6 点分布在哪些章？累积曲线如何？哪一点是 AI 开始系统化怀疑的转折？
3. **与内线累积的同步**——内线和外线的 paranoid 是否在同一些事件上 reinforce？比如 character collapse（I5）之后，AI 不仅怀疑自己（内线），是否也开始怀疑妻子（外线）？
4. **关机场景如何在 paranoid framework 下具体落地**——AI 怎么开口告诉妻子？它会不会暗示"如果你是真的，那……"？还是它说什么都不暗示？妻子的反应？
5. **epilogue 如何处理 paranoia 是 side effect 这一层揭穿**——既要揭穿（AI 的怀疑是 hallucination），又不能否定前文（AI 的怀疑是真实经历的）。如何写？
6. **paranoid 是否真的让一般读者更 readable**——还是反而让小说变成 thriller 套路？需要更细的 tone control 测试
7. **内线的 I1 修订（姐姐电话）是否保留**——这条在新 framework 下功能略变（同时是 paranoid 引信？）

---

## 九、本稿不影响的已锁定内容

为避免下次接手 Claude 误解，明确**本稿不修订**：

- v4 主稿一切既定守则
- 人物卡 v1（周婉 + 林文浩）的全部内容
- D 阶段产出节（工程现象 6+1 + 三层翻译装置）
- 内线 vs 外线的精确关系节（D 阶段后补丁）
- 内线累积 7 点（I1-I7）——内线设计未变
- B1（裂缝引信首发 = I1 同场景）、B4（双线汇合）、B5（关机）的位置

本稿**只**影响：
- 外线累积清单（O1-O7）—— 待 paranoid reframe 落地
- 外线高潮的产物 —— 从"她在被钓"升级为"她可能不是她"
- 关机 logic 的双线表述 —— 升级为 epistemic crisis 双线扩散
- 新增 tone 控制守则（paranoia contained）

---

## 设计沿革

- **本稿（WIP）**：B 阶段关键瞬间下钻第一轮的 paranoid reframe 讨论。状态未完备，下次继续。落入 v4 主稿前需用户最终确认 framework 是否成立
