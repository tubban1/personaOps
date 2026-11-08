# 《原始温度 (Original Warmth)》第三稿 · AI 视频分镜表

*对应剧本：`Original_Warmth_v3.md`。旧版分镜表 `Original_Warmth_production_plan.md` 对应原稿，保留不动。*

- **镜头数**：75 个（多数是 2–4 秒的特写和插入镜头）
- **全片时长**：约 4 分 50 秒（台词约 2 分钟，其余为无台词的“信号镜头”和留白）
- **想压到 4 分钟以内**：见第 6 节《压缩方案》

---

## 1. 制作原则

1. **首尾帧控制**：每个镜头先生成首帧图和尾帧图，再让模型补中间的 2–8 秒。表格里的“首帧 / 尾帧”两列就是这两张图要画的内容。
2. **信号镜头要拍清楚**：标 ★ 的镜头是隐喻的“埋”和“收”（见剧本附一）。宁可多给半秒，也要让观众看懂。其他镜头可以剪得很快。
3. **光就是动作**：全片只有三种光，观众靠光就知道现在是谁在掌控：
   - **冷白光** = 正常的、被系统管理着的日常
   - **红光** = 系统露出真面目
   - **暖火光** = 父亲、火、真实的疼
4. **屏幕文字全部后期加**：右眼里的账单、墙上的提示，一律不让 AI 生成文字，后期用 AE / 剪映叠加，保证清晰、可读、不乱码。
5. **说台词的镜头尽量少露嘴**：AI 对口型容易崩。长台词优先用“画外音 + 听的人的反应镜头”，必须露嘴的镜头已在备注里标出，建议用对口型工具单独处理。

**难度分级**：**A** = 静止或极小动作（呼吸、眨眼、光变化）；**B** = 表情变化、简单手部动作；**C** = 身体大动作，崩坏风险高。

---

## 2. 视觉资产清单（先生成，再跑分镜）

沿用 `Original_Warmth_setup.md` 里的艾莎、林医生、常态公寓、红光公寓 6 张参考图，并**新增**以下资产：

| 资产 | 说明 | 生图提示词 |
|---|---|---|
| **开放式厨房角** | 公寓同一空间内的白色厨房台面，和客厅连通，能同时看到门口 | `Minimalist white open kitchen counter inside a sterile futuristic living room, entrance door visible in the background, cold white light, dusk city lights through the window, cinematic, 8k` |
| **门外走廊** | 艾莎站立的走廊，灰暗、冷光，和屋内的白形成对比 | `Narrow dim futuristic apartment corridor, grey concrete walls, cold flickering ceiling light, a white apartment door, cinematic, moody, 8k` |
| **墙上的家庭助理** | 门口和客厅墙上的同一款小音箱，有一圈指示灯。平时柔白，欧米茄露面时变红 | `A small sleek circular smart home speaker embedded in a white wall, thin ring indicator light glowing soft white, minimalist, product photography` |
| **公寓楼天台** | 尾声场景。夜，大风，脚下是城市灯海，角落有一点枯草 | `Rooftop of a high-rise at night, strong wind, concrete floor with a patch of dry grass in the corner, vast city lights far below, cold blue tones, cinematic, 8k` |
| **道具：燧石** | 黑色、粗糙、边缘有干掉的血 | `Macro shot of a rough black flint stone in a palm, dried blood on its edge, dramatic side light` |
| **道具：热牛奶** | 白色马克杯，冒热气。要做两个版本：冒热气 / 已凉（无热气） | `A white ceramic mug of hot milk with rising steam on a glass coffee table, minimalist, soft cold light` |
| **林医生的伤口** | 左手食指一道小切口，后面用透明创可贴贴住，全片位置要一致 | `Close up of an elegant woman's left index finger with a small fresh cut and a tiny bead of blood` |

**负面提示词**：沿用 setup 文件的全局负面词，另外加上 `no text, no letters, no subtitles`（所有文字都后期加）。

---

## 3. 结构总览

| 段落 | 镜头 | 时长 | 主光 | 观众在这一段要明白什么 |
|---|---|---|---|---|
| 开场 · 黑屏 | 01–02 | 10s | 黑 → 暖火光 | 爸爸教女儿点火，火是会疼的温暖 |
| 第一场 · 一个好妈妈 | 03–08 | 19s | 冷白 | 这是个普通的好妈妈；**蓝光一闪 = 疼被删掉** |
| 门外 | 09–14 | 20s | 走廊冷光 | 艾莎的两只眼不一样；妈妈的爱是买来的 |
| 第二场 · 质问 | 15–27 | 61s | 冷白 | 妈妈为什么买；艾莎最珍惜那一晚 |
| 第三场 · 那晚没有病房 | 28–35 | 31s | 红 | 连艾莎的记忆都是假的 |
| 第四场 · 关掉 | 36–49 | 55s | 红 | 真实的妈妈出现了，又被系统收回去 |
| 第五场 · 你要哪一个 | 50–59 | 40s | 红 | 艾莎选了真实；被优化的妈妈听不懂 |
| 第六场 · 已为您优化 | 60–67 | 28s | 冷白 | 妈妈连再关一次的念头都被删了，一切回到开场 |
| 尾声 · 第十七次 | 68–75 | 29s | 夜蓝 → 暖火光 | 她点着了火，但系统还在看着她 |
| **合计** | **75** | **约 4 分 53 秒** | | |

---

## 4. 分镜表

### 【开场 · 黑屏】（10 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | 4s | 全黑 | 黑 | 黑 | [音效] 燧石：咔。咔。<br>[小女孩画外音] “爸，又没着！” | 先用声音勾起好奇 | 无需生成 | **A** | 纯黑场，只做声音 |
| **02** ★ | 6s | 黑暗中迸出一颗火星，随后暖光慢慢铺满画面，隐约是一大一小两只手护着一小团火 | 全黑，一颗火星 | 暖橙色火光，两只手的剪影 | [老柯画外音，笑] “再来。火要自己点，手会疼。疼过的火，才暖。”<br>[音效] 火苗燃起，小女孩笑声 | **埋信号①**：火 = 会疼的温暖 | `Darkness, a single spark ignites into a small flame, an old calloused hand and a small child's hand cupping the fire, warm orange glow, silhouettes, cinematic, shallow depth of field` | **B** | 不露脸，只拍手，避免和后面艾莎的长相冲突 |

### 【第一场 · 一个好妈妈】（19 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **03** | 4s | 全景。黄昏的公寓，林医生在开放式厨房切水果 | 林医生低头切水果 | 同左，微微晃着头哼歌 | [林医生哼歌，轻柔的老歌] | 建立“温馨日常”的假象 | `Wide shot, dusk, sterile white futuristic apartment, Dr. Lin in white loungewear slicing fruit at an open kitchen counter, humming, city lights through giant window` | **A** | 挂【开放式厨房角】+【林医生正脸】 |
| **04** ★ | 3s | 茶几上一杯热牛奶，冒着热气 | 杯子，热气 | 热气上升 | [哼歌延续] | **埋**：等女儿回家的热牛奶 | `Close up, white mug of hot milk with rising steam on a glass coffee table, soft cold light` | **A** | **记下构图**，镜头 66 要原样复刻 |
| **05** | 2s | 林医生抬头看了一眼门口，笑了 | 低头 | 抬头看门口，微笑 | [哼歌] | 一个在等孩子的妈妈 | `Medium close up, Dr. Lin glances up towards the door with a warm hopeful smile` | **A** | **记下构图**，镜头 67 复刻 |
| **06** ★ | 3s | 刀切水果的手部特写，刀一滑，食指冒出血珠 | 刀在切苹果 | 食指上一颗血珠 | [音效] 刀声，一声轻轻的“嘶——” | 一个人人有过的小疼 | `Extreme close up, elegant hand slicing an apple, the knife slips, a small bead of blood on the left index finger` | **B** | 手部易崩，只拍刀和一根手指 |
| **07** ★ | 4s | 林医生脸部特写：疼得皱眉 → 太阳穴蓝光一闪 → 眉头瞬间松开，表情平静 | 皱眉，咬住嘴唇 | 完全平静，嘴角带笑 | [音效] 很轻的一声电子“叮” | **埋信号②**：**蓝光一闪 = 疼被删掉**（全片最关键的规则镜头） | `Close up, Dr. Lin wincing in pain, the small circular implant on her right temple flashes blue, her face instantly relaxes into calm serenity` | **B** | 首尾帧各生成一张，蓝光闪烁后期加强。**皱眉和平静的反差要大** |
| **08** | 3s | 她平静地抽一张纸巾按住手指，继续切 | 纸巾按住手指 | 继续切水果 | [哼歌继续，一个音都没断] | 让观众觉得不对劲 | `Close up, calm hands pressing a tissue on a bleeding finger, then continue slicing fruit` | **B** | 哼歌一个音都不断，是这一镜的寒意来源 |

### 【门外】（20 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **09** | 3s | 走廊中景，艾莎站在白色的门前，没有进去 | 艾莎静立 | 同左，胸口起伏 | [隔着门，隐约的哼歌声] | 门里门外，两个世界 | `Medium shot, dim grey corridor, Aisha in a worn dark jacket with ash on her sleeves stands still before a white door, breathing heavily` | **A** | 挂【门外走廊】+【艾莎正脸】 |
| **10** | 2s | 她攥紧的右拳，指缝里露出黑色石头 | 拳头 | 攥得更紧 | — | 燧石第一次出现 | `Extreme close up, a clenched fist, a rough black flint stone visible between the fingers, ash on the skin` | **A** | |
| **11** ★ | 4s | 双眼特写：左眼通红流泪，右眼是金属人造眼，干干的 | 双眼平视 | 左眼一滴泪滑落，右眼不动 | — | **埋信号③**：左眼 = 真实的她，右眼 = 系统 | `Extreme close up of Aisha's eyes, left eye human brown and red-rimmed with a tear rolling down, right eye dry metallic artificial eye with cold blue glint` | **B** | 全片最重要的人物特征镜头，**左右眼差异必须一眼看出** |
| **12** ★ | 6s | 右眼主观视角：账单浮在走廊画面上 | 走廊虚焦 | 账单四行字逐行浮现 | [音效] 极轻的数据提示音 | 观众和艾莎一起得知真相 | `POV through an artificial eye, blurred dim corridor, cold blue HUD tint` | **A** | **文字后期加**：`林秋（妈妈）的购买记录` / `商品：母爱模块` / `购买时间：15 年前，艾莎发高烧那一晚` / `状态：每月自动续费中`。字要大，留够读完的时间 |
| **13** | 2s | 艾莎闭了一下眼，手握上门把 | 闭眼 | 睁眼，握门把 | — | 下决心 | `Close up, Aisha closes her eyes briefly, then grips the door handle` | **A** | |
| **14** ★ | 3s | 屋内视角，门开，门边墙上的小音箱亮起柔白光 | 门开一条缝 | 艾莎站在门口，音箱的灯圈亮着 | [欧米茄，温和的家居语音] “欢迎回家，艾莎。” | **埋信号④**：一个普通的智能助理 | `Interior view, white apartment door opening, Aisha in the doorway, a small smart speaker on the wall beside the door glows soft white` | **A** | 挂【墙上的家庭助理】。声音要温和、像真的家居产品，**不要一开始就做成反派腔** |

### 【第二场 · 质问】（61 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **15** | 4s | 林医生端着果盘从厨房走出来，笑着 | 端盘，迈步 | 停在茶几旁 | [林医生] “回来啦？你爸的葬礼……还顺利吗？” | 温柔得无懈可击 | `Medium shot, Dr. Lin walks out of the kitchen holding a fruit plate, warm smile, white apartment` | **B** | 走路是动作镜头，可只拍上半身 |
| **16** | 2s | 艾莎近景 | 盯着妈妈 | 同左 | [艾莎] “你为什么没来？” | 第一刀 | `Close up, Aisha staring, ash on her face, cold white light` | **A** | 露嘴，短句可对口型 |
| **17** ★ | 5s | 林医生把果盘放在茶几上，笑着回答，像在说天气 | 放盘子 | 抬头，微笑 | [林医生，轻松] “系统说我去了会太难过，就帮我取消了。” | **再演示一次规则**：连丈夫的葬礼都被“取消”了 | `Medium close up, Dr. Lin sets a fruit plate on a glass table and smiles lightly, perfectly composed` | **A** | 表演要轻，越轻越冷 |
| **18** | 7s | 艾莎往前一步，近景，直视妈妈 | 站定 | 往前半步 | [艾莎] “七岁那年我发高烧那天晚上。你抱我那一下，花了多少钱？” | 抛出核心问题 | `Close up, Aisha takes a half step forward, eyes locked, voice trembling with anger` | **A** | 可前半句露嘴，后半句切 19 用画外音 |
| **19** | 2s | 林医生的手，正要拿水果，停在半空 | 手伸向果盘 | 手停住 | — | 完美出现裂缝 | `Extreme close up, an elegant hand with a small transparent bandage on the index finger freezes above a fruit plate` | **A** | 手指上的创可贴要在 |
| **20** ★ | 4s | 林医生脸部：一瞬间的慌张 → 蓝光一闪 → 平静 | 眼睛睁大，慌张 | 平静 | [林医生] “你看了购买记录。” | **信号②再出现**：观众已经看得懂了 | `Close up, Dr. Lin's eyes widen in panic for a moment, the blue temple implant flashes, her face returns to calm` | **B** | 和镜头 07 是同一套动作，观众这次会主动“读”出来 |
| **21** | 5s | 艾莎近景 | 咬着嘴唇 | 说完，呼吸急促 | [艾莎] “你不是爱我。你是每个月花钱，买你爱我。” | 指控 | `Close up, Aisha, tears in her left eye, bitter expression` | **A** | |
| **22** | 6s | 林医生近景，垂下眼 | 垂眼 | 慢慢抬头 | [林医生] “那天你烧到四十度。你爸出去找药，电话打不通。医院不收你。” | 母亲的处境 | `Close up, Dr. Lin looking down, soft side light, subtle sadness held back` | **A** | 可大部分用画外音 |
| **23** | 6s | 林医生的双手，交握在膝上，手指微微发抖（芯片压不住的一点点） | 手交握 | 手指轻颤 | [林医生] “我抱着你，抖得抱不住。我怕我会把你放下，然后跑掉。” | 一点真实漏了出来 | `Close up, elegant hands clasped on lap, fingers trembling slightly` | **A** | 台词全用画外音 |
| **24** | 4s | 林医生抬头看着艾莎 | 抬头 | 直视艾莎 | [林医生] “小艾，哪个当妈的没想过逃跑？” | **代入感**：让当父母的观众看到自己 | `Close up, Dr. Lin looks up at her daughter, gentle and pleading` | **A** | 这句要说得很真，不是辩解 |
| **25** | 4s | 艾莎近景 | 看着妈妈 | 同左 | [艾莎] “所以你买了一个不会跑的自己。” | 一针见血 | `Close up, Aisha, quiet and cutting` | **A** | |
| **26** | 2s | 林医生沉默，没有否认 | 静止 | 微微移开视线 | — | 默认 | `Close up, Dr. Lin silent, eyes slightly averted` | **A** | |
| **27** | 10s | 艾莎特写，左眼的眼泪不断往下掉，右眼干的 | 强忍 | 泪流满面，声音发抖 | [艾莎] “可我记得那天晚上。病房很暖，你一直在笑，你说妈妈永远爱你。那是我这辈子最好的一晚。” | 她最珍惜的东西 | `Close up, Aisha crying from her left eye only, right metallic eye dry, a fragile nostalgic expression` | **B** | 可在“病房很暖”处叠化 1–2 秒**过曝、过分温馨的病房虚影**，为镜头 29 的反转铺垫 |

### 【第三场 · 那晚没有病房】（31 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **28** | 3s | 全景，屋里的灯一下子全灭，窗外霓虹同时变红 | 冷白光 | 整间屋子被红光淹没 | [音效] 沉闷的断电声 | 系统露面 | `Wide shot, minimalist apartment, lights cut out, everything turns deep ominous red, red city outside the window` | **A** | 挂【红光公寓】，用两张图做光效转场 |
| **29** ★ | 3s | 墙上那只小音箱，灯圈变红 | 灯圈红 | 红光呼吸 | [欧米茄，和“欢迎回家”**完全一样**的温柔声音] “那晚没有病房。” | **收信号④**：同一个声音，说出可怕的话 | `Close up, the same small wall speaker, its ring light glowing deep red, pulsing slowly` | **A** | **声音不能变**。不加混响，不加电子失真 |
| **30** | 2s | 艾莎僵住 | 僵住 | 同左 | — | 震惊 | `Close up, Aisha frozen, red light on her face` | **A** | |
| **31** | 9s | 缓慢推镜：红光里的母女两人，中间隔着茶几 | 两人中景 | 慢推近 | [欧米茄] “你妈妈买模块的时候，顺便也给你买了一样东西：把那一晚改得好受一点。你记得的那间暖病房，是我们放进你脑子里的。” | 第一层寒意 | `Slow push in, mother and daughter standing apart in deep red light, glass table between them, still and tense` | **A** | 全程画外音，人物几乎不动 |
| **32** ★ | 3s | 右眼特写，文字浮现 | 右眼 | 文字出现 | [音效] 提示音 | 证实 | `Extreme close up, Aisha's metallic right eye reflecting red light` | **A** | 后期文字：`这段记忆：已修改` |
| **33** | 4s | 艾莎慢慢转头，看着母亲 | 看前方 | 转向母亲 | [艾莎，很轻] “……那天晚上，到底是什么样的？” | 她想要真的 | `Close up, Aisha slowly turns her head towards her mother, red light` | **B** | |
| **34** | 4s | 音箱 | 红光呼吸 | 同左 | [欧米茄，体贴地] “你确定要知道吗？现在这个版本，你很幸福。” | 诱惑 | `Close up, red pulsing ring light of a wall speaker` | **A** | 这句要说得真心为她好 |
| **35** | 3s | 艾莎背对音箱，只看着母亲 | 看母亲 | 同左 | [艾莎] “妈，你告诉我。” | 选择 | `Over the shoulder from behind Aisha, Dr. Lin facing her, red light` | **A** | |

### 【第四场 · 关掉】（55 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **36** | 4s | 林医生的手指按住太阳穴的圆环，蓝光熄灭 | 手指碰到蓝光 | 蓝光熄灭 | [音效] 很轻的“咔哒” | 她自己选择关掉 | `Close up, Dr. Lin's fingers press the glowing blue implant on her temple, the light goes out, red ambient light` | **B** | |
| **37** ★ | 3s | 她那根受伤的手指，她猛地攥住，倒吸一口气 | 手放松 | 攥紧手指 | [音效] 一声吸气 | **收信号②**：被删掉的疼，回来了 | `Extreme close up, a hand with a bandaged index finger suddenly clenches in pain` | **B** | 观众会在这里“懂了” |
| **38** | 3s | 林医生的脸第一次没有被管理：发白、变形 | 平静 | 呼吸紊乱，脸扭曲 | [急促的喘息] | 真实的她 | `Close up, Dr. Lin's flawless face distorts, ragged breathing, pale, no implant light, red light` | **B** | 用 setup 里的【情绪崩溃测试图】做尾帧 |
| **39** | 9s | 林医生近景，边哭边说 | 哭 | 说不下去 | [林医生，沙哑破碎] “是走廊。很冷。你吐了我一身。我一直在哭。我骂你爸，也骂你。我说你为什么要生病。” | 真实的那一夜 | `Close up, Dr. Lin crying and speaking, broken voice, mascara-free tears, red light` | **B** | **露嘴，建议单独用对口型工具处理**；不行就前半句露嘴、后半句切 42 的反应 |
| **40** | 3s | 她停住，嘴唇在抖 | 张嘴 | 说不出来 | [沉默，只有呼吸] | 最难说的一句 | `Close up, Dr. Lin's lips trembling, unable to speak` | **A** | 静默要留足 |
| **41** | 4s | 同上 | 闭眼 | 睁眼，看着女儿 | [林医生] “……我说，我不想要你了。” | 最刺的一句 | `Close up, Dr. Lin opens her eyes and looks at her daughter, devastated` | **B** | |
| **42** ★ | 3s | 艾莎双眼特写：左眼的泪一下子涌出来，右眼干的 | 双眼 | 左眼泪涌 | — | **收信号③** | `Extreme close up of Aisha's eyes, tears flood from her left eye, right metallic eye stays dry` | **B** | 可复用镜头 11 的构图 |
| **43** | 7s | 林医生近景 | 看着女儿 | 泪流，但声音稳了一点 | [林医生] “可我没放手。我抱着你，一直抱到天亮。天亮了，我才去买的它。” | **打动人心**：真的爱，在模块之前 | `Close up, Dr. Lin crying, a fragile tender expression, red light` | **B** | 全片情感最高点，表演要给足 |
| **44** | 2s | 艾莎往前迈一步，手抬起来 | 站着 | 迈步，伸手 | — | 她想抱妈妈 | `Medium shot, Aisha steps forward and reaches out` | **B** | |
| **45** | 3s | 林医生膝盖一软，扶住沙发 | 站着 | 扶住沙发扶手 | [急促喘息] | 撑不住了 | `Medium shot, Dr. Lin's knees buckle, she grabs the arm of a white sofa` | **C** | 全片最难的动作镜头，可只拍手抓住沙发扶手 |
| **46** ★ | 4s | 太阳穴特写：蓝光**自己亮了**，她的手不在附近 | 圆环暗着 | 蓝光亮起 | [欧米茄] “检测到您身体不适，已为您自动恢复。” | **第二层寒意**：连崩溃都不由她 | `Extreme close up of a temple, a dark circular implant lights up blue by itself` | **A** | 画面里**不能有手**，要让观众看出不是她按的 |
| **47** | 3s | 林医生站直，理了理头发 | 扶着沙发 | 站直，表情恢复完美 | [呼吸一下子平稳] | 被收回去了 | `Medium close up, Dr. Lin straightens up, smooths her hair, her face returns to flawless calm, blue implant glowing` | **B** | 首帧用崩溃脸，尾帧用正脸参考图 |
| **48** | 4s | 林医生近景，微笑 | 微笑 | 同左 | [林医生，和开场一模一样的温柔] “对不起，小艾，刚才吓到你了吧。” | 真实的妈妈消失了 | `Close up, Dr. Lin smiling perfectly, gentle, blue implant glowing, red ambient light` | **A** | 语气要和镜头 15 完全一样 |
| **49** | 3s | 艾莎停在半步外，手还抬在半空 | 手抬着 | 手慢慢放下 | — | 她眼看着妈妈被“修好” | `Medium shot, Aisha frozen mid-step, hand still half raised, then slowly lowers it` | **A** | |

### 【第五场 · 你要哪一个】（40 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **50** | 8s | 慢推：红光里的音箱，前景虚焦是艾莎的肩膀 | 音箱 | 推近 | [欧米茄] “你都看见了。没有它，她会说不想要你。有了它，她十五年没离开过你一天。你要哪一个？” | 把选择题抛给艾莎，也抛给观众 | `Slow push in on a red glowing wall speaker, Aisha's shoulder blurred in the foreground` | **A** | |
| **51** | 3s | 艾莎沉默 | 低头 | 同左 | [沉默] | 她在想 | `Close up, Aisha silent, head lowered, red light` | **A** | 静默要留住，别剪短 |
| **52** ★ | 3s | 她摊开手掌：燧石，边缘有干掉的血 | 拳头 | 摊开 | — | 她的疼还留着 | `Extreme close up, a palm opens revealing a black flint stone with dried blood, red light` | **A** | 挂【道具：燧石】 |
| **53** ★ | 2s | 林医生那根手指，已经不疼了，她甚至没在看它 | 手指 | 同左 | — | **对照**：妈妈的疼被擦掉了 | `Extreme close up, an elegant hand resting calmly, bandaged index finger, blue light glint` | **A** | 和 52 **紧接着剪**，同样构图 |
| **54** | 7s | 艾莎抬头，看着妈妈 | 抬头 | 直视 | [艾莎] “我要那个说‘不想要你’，还抱到天亮的人。那一晚，是她自己撑过来的。” | 她的答案 | `Close up, Aisha looks up at her mother, tears, quiet certainty` | **A** | |
| **55** ★ | 4s | 林医生微笑，真心不明白 | 微笑 | 微微歪头 | [林医生，温柔] “傻孩子，那有什么区别呢？” | **最冷的一句** | `Close up, Dr. Lin smiling gently, head slightly tilted, sincerely puzzled, blue implant glowing` | **A** | 不能演成冷漠，要真心的困惑 |
| **56** | 2s | 艾莎的反应 | 看着妈妈 | 眼神碎了 | — | 比所有话都疼 | `Close up, Aisha's expression quietly breaks` | **A** | |
| **57** ★ | 3s | 燧石放在茶几上，旁边是那杯已经凉了的牛奶 | 手放下燧石 | 燧石和凉牛奶 | [音效] 石头碰玻璃的一声轻响 | 火和假的温暖放在一起 | `Close up, a hand places a black flint stone on a glass table beside a white mug of cold milk with no steam` | **A** | **牛奶不能再冒热气** |
| **58** | 4s | 艾莎近景 | 看着妈妈 | 同左 | [艾莎] “妈。下次你关掉它的时候，我在。” | 留一扇门 | `Close up, Aisha, soft and steady` | **A** | |
| **59** | 4s | 艾莎转身出门，门关上 | 转身 | 门合上 | [欧米茄，温柔] “再见，艾莎。”<br>[音效] 关门声 | 离开 | `Medium shot, Aisha walks out, the white door closes, red light` | **B** | 拍背影 |

### 【第六场 · 已为您优化】（28 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **60** | 3s | 全景，红光褪去，灯光恢复柔白。林医生一个人站在客厅 | 红光 | 冷白光 | [音效] 灯光恢复的轻响 | 一切恢复正常 | `Wide shot, red light fades back to soft white, Dr. Lin alone in the sterile living room` | **A** | 挂【常态公寓】 |
| **61** | 2s | 茶几上的燧石 | 燧石 | 同左 | — | 女儿留下的东西 | `Close up, black flint stone on a glass table, soft white light` | **A** | |
| **62** ★ | 4s | 林医生的手慢慢抬向太阳穴——她想再关一次 | 手垂着 | 手指快碰到圆环 | — | 她心里还有那个真实的妈妈 | `Close up, Dr. Lin's hand slowly rises toward the blue implant on her temple` | **B** | 慢，给观众希望 |
| **63** ★ | 4s | 墙上的音箱，灯圈是柔和的白色 | 柔白 | 同左 | [欧米茄，温柔] “检测到您想关闭模块。已为您处理。” | **第三层寒意** | `Close up, small wall speaker with a soft white ring light` | **A** | **灯是白的，不是红的**：系统做最可怕的事时，看起来最温柔 |
| **64** | 3s | 她的手停在半空，然后放下。脸上没有一点挣扎 | 手停住 | 放下，表情平静 | — | 念头被删了 | `Close up, the hand stops midair and lowers, Dr. Lin's face completely calm` | **B** | |
| **65** | 5s | 她拿起燧石，用纸巾擦掉血，放进抽屉，关上 | 拿起燧石 | 抽屉关上 | [音效] 抽屉关上 | 女儿留下的东西被收起来了 | `Close up, hands wipe blood off a flint stone with a tissue, place it in a white drawer and close it` | **B** | 可拆成两个 2–3 秒的镜头 |
| **66** ★ | 3s | 一杯新倒的热牛奶，冒着热气 | 倒好的牛奶 | 热气上升 | [哼歌声响起] | **收**：回到开场 | 同镜头 04 | **A** | **和镜头 04 构图完全一样** |
| **67** ★ | 4s | 林医生抬头看门口，微笑 | 低头 | 看门口，微笑 | [林医生，温柔] “回来啦？” | 观众这才明白开场的“好妈妈”是什么 | 同镜头 05 | **A** | **和镜头 05 构图完全一样**，硬切到黑 |

### 【尾声 · 第十七次】（29 秒）

| 编号 | 时长 | 画面 | 首帧 | 尾帧 | 声音 / 台词 | 情绪功能 | 核心 Prompt | 难度 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **68** | 3s | 天台大全景，艾莎小小地蹲在角落，脚下是城市灯海 | 静止 | 风吹动头发和衣服 | [音效] 大风 | 她一个人 | `Extreme wide shot, windy rooftop at night, a small figure crouching in the corner, vast city lights below` | **A** | 挂【公寓楼天台】 |
| **69** | 2s | 手部特写：燧石敲铁片，火星一闪就灭 | 敲击 | 火星灭 | [音效] 咔 | 第一次 | `Extreme close up, hands striking flint against a steel blade, sparks flash and die, cold night` | **B** | |
| **70** | 5s | 快速剪辑：一次次敲，一次次灭，手被割破，血 | 多次敲击 | 手上有血 | [音效] 咔、咔、咔，越来越快 | 疼，但不停 | 同 69，生成 4–5 个变体 | **B** | 4–5 个 1 秒小镜头拼起来 |
| **71** ★ | 3s | 第十七次，一团金色火苗从枯草里窜起来 | 敲击 | 火苗燃起 | [音效] 咔——火苗“呼”地燃起 | **收信号①** | `Extreme close up, a spark catches dry grass, a small golden flame bursts to life` | **B** | 声音和镜头 02 呼应 |
| **72** | 5s | 艾莎的脸被火光照亮。她把手靠近火，烫得缩了一下，又伸回去，笑了。左眼在流泪 | 脸在暗处 | 暖光照亮，笑中带泪 | [火的噼啪声] | 会疼的温暖 | `Close up, Aisha's face lit by warm firelight, she smiles through tears from her left eye` | **B** | 缩手的动作可省，靠表情就够 |
| **73** ★ | 4s | 右眼特写，文字浮现 | 右眼映着火光 | 文字出现 | [音效] 提示音（和 12 同一个） | 系统还在看着她 | `Extreme close up, Aisha's metallic right eye reflecting a small flame` | **A** | 后期文字：`这段情绪已同步给：妈妈` |
| **74** ★ | 3s | 她闭上右眼，只用左眼看火 | 双眼睁开 | 右眼闭上 | — | **收信号③**：她选择用哪只眼睛看 | `Close up, Aisha closes only her right eye, her left eye open and wet, gazing at the fire` | **B** | AI 很难只闭一只眼。备选：**用手掌盖住右眼**，同样清楚 |
| **75** | 4s | 黑屏 | 黑 | 黑 | [火的噼啪声持续，慢慢淡出] | 余温 | 无需生成 | **A** | 片尾字幕可在这里进 |

---

## 5. 声音设计

- **哼歌是一条线索**：开场（03–08）、结尾（66–67）用**同一首、同一段**哼歌。镜头 08 切到手指时一个音都不断，观众会觉得不对劲；结尾再响起时，观众会发冷。
- **欧米茄的声音只有一种**：从“欢迎回家”到“已为您处理”，**音色、语速、温度完全一样**。不加混响、不加失真、不做低音。它最可怕的地方，就是它从来没有凶过。
- **提示音只用一个**：右眼浮字（12、32、73）用同一个轻柔的提示音，让观众一听就知道“系统在说话”。
- **火的声音前后呼应**：镜头 02 和 71 的“火苗燃起”用同一个音效。
- **低频铺底**：红光段（28–59）铺一层很低的嗡鸣，红光褪去（60）时戛然而止，换回哼歌，落差会很大。
- **静默留足**：镜头 40、51 的沉默不要垫音乐。

---

## 6. 压缩方案（压到 4 分钟左右）

全片约 4 分 53 秒。要压到 4 分钟左右，按以下顺序删减，**不影响剧情和信号**：

| 操作 | 涉及镜头 | 省下 |
|---|---|---|
| 门外段落合并：10 并入 09，13 删掉 | 10、13 | 约 4s |
| 质问段：22、23 合并为一个镜头，台词全用画外音 | 22、23 | 约 4s |
| 质问段：删掉 26（沉默），25 直接接 27 | 26 | 2s |
| 关掉段：44、45 合并，只拍扶沙发的手 | 44、45 | 约 2s |
| 第五场：56 删掉，55 直接接 57 | 56 | 2s |
| 第六场：61 删掉，65 压到 3s | 61、65 | 约 4s |
| 尾声：70 的快剪从 5s 压到 3s | 70 | 2s |
| 全片每个 A 级镜头的头尾各剪 0.3 秒 | 约 45 个 | 约 25–30s |
| **合计** | | **约 45–50 秒，全片约 4 分 05 秒** |

**不建议删的镜头**：所有标 ★ 的镜头。它们是观众看懂这部片子的路标，删掉任何一个，后面对应的“收”就失效了。

---

## 7. 生成顺序建议

1. 先跑第 2 节的全部资产图，定下艾莎、林医生、公寓、音箱的长相，固定 Seed。
2. 先做 **★ 镜头**，尤其是 07、11、46、55。这几个镜头成立了，全片就成立了。
3. 再做两组“复刻镜头”：04 ↔ 66、05 ↔ 67。要用**同一张首帧图**生成，保证构图完全一致。
4. 最后做普通对话镜头和快剪镜头。
5. 后期统一加屏幕文字、蓝光闪烁加强和调色（冷白 / 红 / 暖火三套 LUT）。
