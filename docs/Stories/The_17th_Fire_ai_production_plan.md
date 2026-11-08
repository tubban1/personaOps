# 《第十七次火》低复杂度 AI 视频制作方案

## 1. 制作原则

本方案摒弃了传统的 10-15 分钟长篇铺陈，将影片浓缩为 **5分钟至5分30秒的高密度哲学短片**。总镜头数控制在 **37-40个**。

**核心制作策略（首尾帧控制法）：**
当前的 AI 视频模型（如 Runway Gen-3, Kling, Sora, Pika）在生成复杂动作和长镜头时极易发生形变或一致性崩塌。为此，我们采用以下标准流程：
1. 先生成分镜概念图。
2. 生成视频的**首帧图 (First Frame)**。
3. 生成视频的**尾帧图 (Last Frame)**。
4. 使用首尾帧作为关键帧引导模型生成单条 5-10 秒的视频。
这种方法能将不可控的 AI 生成转化为可控的关键帧补间，极大降低废片率。全片 70% 以上的镜头被设计为静态特写、极简微动作或通过剪辑完成空间转换的低复杂度（A级/B级）镜头。

---

## 2. 全片结构

- **第一场：灰烬族葬礼**（约 85 秒，10 个镜头）：确立死亡的物理质感与悲伤优化的对立。
- **第二场：记忆交易所**（约 60 秒，7 个镜头）：展现情感被商品化、数据化后的冰冷。
- **第三场：母亲公寓**（约 170 秒，16 个镜头）：母女激辩，全片戏剧高潮，通过微表情展现信仰崩塌。
- **结尾：第十七次火**（约 60 秒，6 个镜头）：动作收尾，物理痛感的重新找回。

---

## 3. 核心哲学递进

本片的旁白与对白极其精简，通过四个递进的问题贯穿全片：
1. **葬礼**：痛苦能不能被优化？
2. **交易所**：记忆变成商品后，人还剩什么？
3. **辩论**：被植入的爱（即使完美），还算爱吗？
4. **结尾**：失败和疼痛为什么定义了“我”？

---

## 4. 镜头表 (共 39 镜)

### 【第一场：灰烬族葬礼】 (镜头 01-10)

| 编号 | 建议时长 | 画面内容 | 首帧描述 | 尾帧描述 | 声音/对白 | 情绪 | 分镜/首尾帧 Prompt 核心 (英文) | 复杂度 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| **01** | 6s | 黑暗中，老柯布满老茧、冰冷的手背特写。 | 静止的粗糙手背，火光微弱。 | 相同，一只年轻的手（艾莎）轻轻握住它。 | [音效] 细微的呼吸声，火堆燃烧声。 | 死亡的物理真实。 | `Close up of an elderly man's rough, cold hand, deep calluses. A young woman's hand gently holds it. Warm firelight in the dark. Cinematic.` | **A** | 纯静态，局部微动作。 |
| **02** | 8s | 艾莎微微发抖地握着父亲的手（左眼含泪，右眼干燥）。 | 艾莎低头，半张脸在暗处。 | 艾莎微微抬起眼眸，火光在瞳孔跳动。 | [艾莎画外]“那是我最后一次握他的手。很冷。” | 悲伤与不舍。 | `Close up of Aisha, 23yo woman. Natural left eye teary, right metallic eye completely dry. Flickering firelight illuminating her face.` | **B** | 重点控制双眼对比。 |
| **03** | 6s | 黑暗隧道深处，白衣合体者官员走入，递出一个微小的银色贴片。 | 黑暗深处隐约的白影。 | 白衣人走入光区，递出银色贴片。 | [官员温和原声]“这是悲伤稳定程序。” | 极具善意的干预。 | `A person in a sterile white futuristic suit emerging from shadows, handing out a tiny glowing silver patch. Cold light vs warm firelight.` | **B** | 重点在递出的动作。 |
| **04** | 10s | 官员给一个哭到站不稳的灰烬族女人贴上银色贴片。 | 女人跪在地上，呼吸急促。 | 贴片发出微光，女人呼吸慢下来。 | [官员画外]“我们不是要你忘了他，只是让你不用被失去毁掉。” [女人低声]“我能看他了。” | 让技术先用动作证明有效。 | `Close up of a grieving woman in rough clothes receiving a tiny silver patch on her wrist. Her breathing calms, tears still falling. Firelit dark tunnel.` | **B** | 动作论证，避免官员空讲。 |
| **05** | 9s | 艾莎闭上右眼，流着泪看着那个被稳定的女人。 | 艾莎表情防备。 | 她短暂地露出被刺痛、动摇的眼神。 | [官员画外]“时间也会让你不痛。它不是背叛，是加速愈合。” | 短暂动摇。 | `Close up of Aisha's face. She closes her right eye. Only her left eye is open, tearing up, looking shaken as she watches someone off screen. Firelight.` | **B** | 让艾莎看见系统确实有用。 |
| **06** | 8s | 艾莎的右眼弹出 UI 提示建议接受稳定程序。 | 界面光芒反射在右眼。 | 界面高频闪烁。 | [艾莎画外]“你说得对。时间会让我轻一点。我也可能会伤害别人。” | 承认代价。 | `Extreme close up of Aisha's face. Glowing holographic UI reflecting on her right metallic eye. Firelight on face.` | **A** | 微动作，避免长口型。 |
| **07** | 8s | 艾莎低头，眼泪砸在老柯的手背上。 | 握住老柯的手。 | 一滴泪水落下，砸在手背上。 | [艾莎画外]“可那十年不是空的。” | 情绪翻转。 | `Macro shot of a rough elderly hand being held by a young hand. A single tear drops onto the old hand. Emotional, dark cinematic lighting.` | **B** | 用身体细节代替解释。 |
| **08** | 8s | 特写：官员手里的银色贴片与艾莎另一只手里的火把在同一个画面的前后景。 | 贴片清晰，火把模糊。 | 焦点转换，火把变清晰。 | [艾莎画外]“你们想拿走的不是痛。你们想拿走的是我变成另一个人的过程。” | 两种选择。 | `Close up. A silver futuristic patch in the foreground in focus. A wooden torch with fire in the background out of focus. Focus pull to the fire. Cinematic.` | **A** | 贴片与火把的选择视觉化。 |
| **09** | 10s | 艾莎松开父亲的手，转身拿起火把（动作中景）。 | 艾莎低头看着手。 | 艾莎握紧火把，转身。 | [艾莎原声]“也许有一天我会需要它，但不是现在。不是在火还没点起来的时候。” | 决绝，哲学反击。 | `Medium shot. Aisha slowly letting go of a dead hand, then turning away, firmly gripping a burning wooden torch. Gritty cinematic style.` | **C** | 动作连贯，台词可用画外音覆盖。 |
| **10** | 10s | 熊熊烈火吞噬木柴（背影/空镜）。 | 大火燃烧。 | 火焰冲天，艾莎的轮廓在火光前静立。 | [艾莎原声]“不是由你告诉我，哪一部分失去应该提前愈合。” | 仪式的完成。 | `Wide shot, a massive burst of golden fire engulfing a pyre in a dark tunnel. Silhouette of a woman watching. Intense heat.` | **B** | AI生火效极佳。 |

### 【第二场：记忆交易所】 (镜头 11-17)

| 编号 | 建议时长 | 画面内容 | 首帧描述 | 尾帧描述 | 声音/对白 | 情绪 | 分镜/首尾帧 Prompt 核心 (英文) | 复杂度 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| **11** | 8s | 极简白色空间，全息面板浮动。艾莎格格不入地走过。 | 艾莎走入纯白走廊。 | 艾莎走向画面深处。 | [音效] 冰冷的电子滴答声。 | 异类感。 | `Tracking shot of Aisha walking in a sterile white futuristic corridor, wearing rough dark clothes. Clean cold lighting.` | **B** | 走路背影/侧影。 |
| **12** | 6s | 玻璃隔间内，男人面前同时放着记忆水晶球和儿童身份修复账单。 | 男人痛苦地看着发光球体。 | 画面移到红色账单：“儿童身份修复费用：800信用点”。 | [男人原声]“这是我女儿第一次叫爸爸的记忆。” | 交易背后的父爱动机。 | `Medium shot through glass. A haggard man sitting at a white table with a glowing memory orb and a red medical identity repair bill. Clinical white room.` | **A** | 账单文字建议后期合成。 |
| **13** | 7s | 男人按下【确认出售】，水晶球消失，男人眼神瞬间涣散。 | 手指悬在确认按钮上。 | 水晶球被吸走，男人脸部特写，眼神空洞。 | [AI电子音]“您将保留事件事实，失去心跳、体温和情绪负载。” [男人低声]“那我还会爱她吗？” [AI]“会。您正在出售它，就是证据。” | 牺牲而非堕落。 | `Close up of a haggard man's face. His expression becomes blank and hollow as a glowing memory orb vanishes. Cold lighting, emotional devastation.` | **B** | 用反应镜头承载对白，避免口型。 |
| **14** | 6s | 艾莎脸部贴近查询终端，白光照在脸上。 | 艾莎低头靠近发光屏幕。 | 界面光芒反射在她的右眼。 | [艾莎低语]“查询交易记录：林秋。” | 悬念。 | `Close up of Aisha's face lit by a glowing white screen. Holographic text reflecting on her face.` | **A** | 纯静态。 |
| **15** | 5s | 屏幕特写：红色刺眼的记录跳出。 | 纯白界面。 | 红色字体出现：“母爱激发模块 3.0”。 | [音效] 刺耳的系统警告音。 | 震撼揭晓。 | `Close up of a futuristic screen interface. Red glowing text reading "MOTHER'S LOVE MODULE 3.0" on a clean white background.` | **A** | 图文合成，后期加字最稳妥。 |
| **16** | 6s | 艾莎瞳孔猛然收缩，极度震惊。 | 平静。 | 瞳孔放大，嘴唇微张。 | [系统音]“心率异常：130bpm。” | 信仰坍塌。 | `Extreme close up of Aisha's face. Her pupils dilate in pure shock. Clinical white light.` | **A** | 极微距特写。 |
| **17** | 7s | 艾莎猛地拔掉数据线，转身逃离（手持晃动感）。 | 手抓着线。 | 线被拔出，画面晃动模糊。 | [音效] 急促慌乱的脚步声。 | 逃避真相。 | `Close up of a rough hand violently pulling out a glowing cable. Handheld camera shake, motion blur.` | **B** | 局部动作。 |

### 【第三场：母亲公寓】 (镜头 18-33)

| 编号 | 建议时长 | 画面内容 | 首帧描述 | 尾帧描述 | 声音/对白 | 情绪 | 分镜/首尾帧 Prompt 核心 (英文) | 复杂度 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| **18** | 6s | 巨大落地窗前，林医生端着水杯，城市霓虹冷蓝。 | 林医生静坐。 | 门被撞开（光影变化）。 | [音效] 粗暴的开门声。 | 完美的结界。 | `Wide shot, minimalist white futuristic apartment. Floor-to-ceiling windows showing cold blue city neon. Elegant 48yo woman sitting.` | **A** | 极简静置。 |
| **19** | 8s | 艾莎红着眼眶站在门后，死死盯着母亲。 | 艾莎喘息，眼神愤怒。 | 艾莎强忍眼泪。 | [艾莎原声]“那天晚上你给我买的那个拥抱，花了多少钱？” | 爆发。 | `Medium shot. Aisha standing angrily, breathing heavily, rough clothes, teary eyes. Clean white background.` | **B** | 喘息的微动作。 |
| **20** | 5s | 特写：林医生的手一僵，杯子停在半空。 | 稳拿杯子。 | 手指微微收紧。 | 无 | 完美的破裂。 | `Close up of an elegant hand holding a glass, freezing in mid-air. Slight tremor.` | **A** | 局部静物。 |
| **21** | 7s | 林医生闭上眼，极力控制表情，再次睁眼时尽显疲惫与羞耻。 | 完美克制的脸。 | 闭眼，眉头微皱，睁开充满挣扎的眼。 | [林医生原声]“我不是想买一个程序来替我爱你。” | 痛苦的坦白。 | `Close up of Dr. Lin's face. Flawless skin, tiny blue dot on temple. She closes her eyes in deep shame and opens them with suppressed pain.` | **B** | 本场核心表演。 |
| **22** | 8s | 艾莎流泪，咬着牙反问。 | 艾莎眼含泪水。 | 泪水滑落，眼神破碎。 | [林医生画外]“我是怕我当时的恐惧，会把你一起拖下去。” [艾莎]“如果一段爱是算出来的……它还算爱吗？” | 绝望的质问。 | `Close up of Aisha crying. Tears rolling down from left eye. Dramatic lighting.` | **A** | 静态落泪。 |
| **23** | 5s | 公寓突然断电，窗外冷蓝霓虹瞬间变成刺眼的血红光。 | 冷蓝光景别。 | 血红光笼罩房间。 | [音效] 沉重的低频断电声，红灯亮起音。 | 绝对理性的降临。 | `Wide shot, apartment lights go out. City neon outside turns stark blood red, flooding the room with red light.` | **A** | 纯场景光影变化。 |
| **24** | 10s | 仰拍墙角的感应灯，闪烁着红光（代表欧米茄）。 | 红灯暗。 | 红灯高频闪烁。 | [欧米茄电子音]“同一个拥抱。一个来自自由选择，一个来自系统判断你最需要拥抱。你的皮肤收到同样的温度。” | 无情剖析。 | `Low angle close up of a sleek wall speaker glowing with a pulsing red light. Dark room lit by red neon.` | **A** | 用灯光代替人物实体，配音承载“来源 vs 体验”。 |
| **25** | 10s | 两人在红光中对峙，艾莎满脸是泪却突然笑了。 | 艾莎愤怒。 | 艾莎含泪苦笑。 | [欧米茄电子音]“从体验角度，它们都是真的。你要的到底是真实，还是一个能让你安心的来源？” | 逻辑绝境。 | `Over the shoulder shot. Aisha lit by red neon, smiling bitterly through heavy tears.` | **B** | 关键哲学质疑，避免对口型，用反应镜头。 |
| **26** | 10s | 艾莎眼神极其坚定地看着前方。 | 艾莎直视镜头。 | 艾莎眼神毫不退缩。 | [艾莎原声]“那个拥抱是温的。我被它救过。那一刻，我的体验是真的。所以它才疼。” | 承认体验真实，但指出痛的来源。 | `Close up of Aisha's face in red light. Fiercely determined, teary eyes.` | **A** | 静态定格感，台词要留停顿。 |
| **27** | 9s | 林医生左眼（生物眼）涌出大颗眼泪，完美表情彻底瓦解。 | 极力克制。 | 眼泪夺眶而出，面部轻微抽搐。 | [艾莎画外]“真实不只是在我身上发生了什么。真实还包括：是谁，为什么，能不能选择不这样对我。” | 芯片失效，真实复苏。 | `Close up of Dr. Lin's face in red light. A huge tear drops from her eye, shattering her perfect composure into pure grief.` | **B** | 极具张力的流泪，承担哲学结论。 |
| **28** | 10s | 林医生按住太阳穴，主动关闭母爱模块。蓝光骤暗，她瞬间呼吸紊乱，杯子掉落。 | 林医生手指按住蓝色光点。 | 蓝光熄灭，她后退撞到沙发，眼里是恐惧。 | [林医生原声]“那我关掉它。” [音效] 杯子落地，液体溅开。 | 用身体证明模块的代价。 | `Medium close up of Dr. Lin pressing the blue implant on her temple. The blue light goes dark, she panics, a glass falls and liquid spills. Red-lit apartment.` | **B** | 关键动作论证，避免长解释。 |
| **29** | 9s | 红光中的扬声器特写，灯光像心跳一样闪烁；艾莎在画外沉默。 | 红灯低频闪烁。 | 闪烁加快，压迫感增强。 | [欧米茄电子音]“如果母亲的爱因为被设计过而可疑，为什么不怀疑父亲留给你的每一句话？” | 反杀艾莎的信仰根基。 | `Close up of a sleek wall speaker pulsing red like a heartbeat. Dark minimalist apartment, ominous red light.` | **A** | 不生成欧米茄实体，用声音攻击父亲线。 |
| **30** | 10s | 林医生重新亮起蓝光，像溺水后吸到空气，羞耻地看向艾莎。 | 林医生低头发抖。 | 蓝光重新亮起，她抬头，脸上满是羞耻和恐惧。 | [林医生原声]“你看见了。如果那晚没有它，我可能会逃走。我买的是一个能留下来的自己。” | 母亲的切肤之痛。 | `Medium close up of Dr. Lin in red light, blue implant turning back on, breathing returns, face filled with shame and fear, elegant but broken.` | **B** | 口型可少，重点用画外音和表情。 |
| **31** | 10s | 艾莎和母亲的双人侧影，中间隔着冷白茶几，红光像裂缝。 | 两人静止对望。 | 艾莎微微摇头，眼泪落下。 | [艾莎原声]“我可以原谅一个害怕到逃走的人。可我不知道该怎么原谅一个被系统修好的人。” | 把痛推到无法解决。 | `Side profile two shot of Aisha and Dr. Lin separated by a white table, red light cutting between them like a wound.` | **B** | 低动作，高情绪。 |
| **32** | 10s | 艾莎转向扬声器，火光记忆般在她右眼里一闪而过。 | 艾莎低头。 | 她抬头直视红光。 | [艾莎原声]“我爸当然也塑造了我。可他没有替我点火。他给我留下的是问题。你们给我留下的是答案。” | 升华：真实需要保留选择和问题。 | `Close up of Aisha turning toward red light, faint warm fire reflection in her dry metallic right eye, determined expression.` | **A** | 可后期叠加一瞬火光反射。 |
| **33** | 7s | 林医生颤抖的手伸向艾莎（特写），艾莎的肩膀向后躲开，随后转身离开。 | 完美的手伸出。 | 手停在半空，艾莎走入阴影。 | [艾莎原声]“留着你的完美吧。我宁愿疼。” | 无法弥合与出走。 | `Close up of an elegant trembling hand reaching out. A person in rough fabric pulls back and exits into shadow. Red light.` | **B** | 合并原伸手与离开，保持镜头数可控。 |

### 【结尾：第十七次火】 (镜头 34-39)

| 编号 | 建议时长 | 画面内容 | 首帧描述 | 尾帧描述 | 声音/对白 | 情绪 | 分镜/首尾帧 Prompt 核心 (英文) | 复杂度 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| **34** | 8s | 黎明前极寒的沙漠，狂风吹拂，一个极其孤独的黑影蹲在沙丘上。 | 黑暗沙丘全景。 | 风沙刮过。 | [音效] 冰冷的狂风呼啸。 | 绝境。 | `Extreme wide shot. A cold, dark desert before dawn. A tiny silhouette of a person sitting on a dune. High wind, dust.` | **A** | 空镜烘托。 |
| **35** | 7s | 特写：艾莎冻得通红的双手，一次次敲击燧石，火星亮起又灭掉。 | 敲击动作。 | 火星熄灭。 | [欧米茄画外]“没有意义。你会冷死在这个沙漠里。” | 徒劳与疼痛。 | `Close up of freezing, red, rough hands repeatedly striking flint and steel. Small sparks flying into dry grass but dying out. Dark night.` | **B** | 重复手部动作。 |
| **36** | 6s | 艾莎的脸部特写。左眼因风沙流泪，右眼（合成眼）彻底黯淡死寂。 | 艾莎咬牙忍受。 | 右眼金属光泽彻底暗淡。 | [音效] 咔！咔！打火声。 | 彻底断开连接。 | `Close up of Aisha's face enduring harsh wind. Left eye tearing up. Right metallic eye is completely dead and unlit. Gritty.` | **A** | 强光影对比。 |
| **37** | 6s | 手部微距：手指划破，鲜血滴在燧石上，用尽全力重重砸下。 | 手举起。 | 砸下。 | [音效] 咔！最重的一声敲击。 | 极致的痛感。 | `Macro shot. Trembling hands striking flint with maximum force. A drop of blood on the stone. Painful reality.` | **C** | 若生成困难可用剪辑加速。 |
| **38** | 8s | 一团金色的火苗猛地从枯草中窜出，照亮艾莎满是伤痕的脸。 | 黑暗枯草。 | 温暖的金色大火燃起。 | [音效] 轰！火焰燃烧。 [艾莎原声]“第一次着了，只是火。” | 奇迹与温度。 | `Close up. A burst of golden fire igniting in dry grass. Warm light rapidly illuminating Aisha's tired face.` | **B** | 光影瞬间转变。 |
| **39** | 10s | 地平线黎明的光撕裂黑暗。艾莎迎着阳光和火光，眼神平静而坚定。 | 侧脸被火光照亮。 | 阳光洒满全脸，切黑屏。 | [艾莎原声]“第十七次，才是我。” [音乐] 悠扬低沉的大提琴声。 | 终极的人性宣告。 | `Close up of Aisha looking up. Golden morning sunlight and warm firelight washing over her face. Defiant and alive. Cinematic masterpiece.` | **A** | 结尾高光静态。 |

---

## 5. 声音设计建议

在低复杂度 AI 视频制作中，**声音占剧情传达的 60%**。画面只需提供质感和情绪定格。
- **对话节奏**：千万不要让画面里的角色出现“长时间说话对口型”的镜头。对话通过画外音（Over-the-shoulder）或反应镜头（Reaction Shot）进行剪辑。例如林医生说话时，画面可以定格在艾莎愤怒流泪的脸上。
- **欧米茄的处理**：绝对不要生成机器人实体。将它的声音做成冰冷的电子低音，从公寓的四面八方包围过来。配合画面中**红光**的闪烁，形成极强的视听压迫感。
- **环境音场**：火的劈啪声、冷风呼啸声、插拔数据线的电火花声、沉重的断电声。这些拟音（Foley）必须极其清晰，以弥补 AI 生成视频在物理交互上的不连贯。

---

*文档说明：本方案通过压制复杂人物运动，采用“定帧首尾引导法”，在保证 100% 剧情张力和哲学深度的同时，将不可控的 AI 生成风险降到了最低。全部 39 个镜头中，A级/B级占据 90% 以上。*
