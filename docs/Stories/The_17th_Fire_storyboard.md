# 《第十七次火》AI 视频生成分镜设计

**分镜设计说明**
本分镜专为 AI 视频大模型（如 Runway/Sora/Kling/Pika）生成定制。全片共45个镜头，通过强烈的物理质感对比（粗糙的灰烬、真实的眼泪、跳动的火焰 vs 无机质的白光、完美的合成眼、虚无的全息投影）完成核心哲学表达。避免过度“赛博朋克化”，主打“内敛的近未来废土与极简未来主义碰撞”，重点通过眼神、微表情失控、手的特写来传达情感撕裂。镜头语言遵循克制、冷峻、高反差。

---

## 【人物一致性提示词 (Character Consistency Prompts)】

- **艾莎 (Aisha)**: `A 23-year-old woman, rough textured earth-toned clothes, subtle dirt on face, dark messy hair, exhausted but determined look. Left eye is biological and natural, right eye has a very subtle metallic grey iris with a faint cold blue glint, completely dry. cinematic portrait.`
- **林医生 (Dr. Lin)**: `A 48-year-old elegant woman, flawlessly smooth skin, wearing a minimalist white futuristic medical outfit. A tiny, glowing blue neural implant dot on her right temple. Her expression is perfectly composed but slightly uncanny, suppressed emotions.`
- **老柯 (Old Ke)**: `A 62-year-old man, deep wrinkles, weathered face, rough hands with thick calluses like tree bark, no electronic implants, wearing heavy coarse fabric.`

## 【全片视觉风格提示词 (Global Visual Style Prompts)】

- **灰烬族/沙漠 (Ashers/Desert)**: `cinematic sci-fi drama, restrained, low saturation, realistic lighting, gritty texture, dust in the air, warm firelight contrasting with deep shadows, handheld camera feel, no neon, no cyberpunk.`
- **合体者/城市 (Synths/City)**: `minimalist futuristic interior, clinical white, sterile, cold overhead lighting, subtle holographic interfaces, muted cool color palette, locked-off camera, precise and clinical, high definition.`

---

## 【分镜表：35-50 镜头拆解】

### 第一场：灰烬族葬礼

| 镜头编号 | 时长 | 景别 | 画面内容 | 摄影机运动 | 角色动作 | 台词/声音 | 情绪功能 | AI 生成提示词 (英文) | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 01 | 3s | 特写 | 黑暗中，一只粗糙如树皮的手背，没有任何芯片痕迹。 | 缓慢推 | 遗体的手一动不动。 | [音效] 燃烧的劈啪声。 | 建立“原生人类”的物理质感。 | `Extreme close up of an elderly man's rough, wrinkled hand with thick calluses, lying still, no electronic implants. Dim warm lighting from an off-screen fire, cinematic sci-fi drama.` | 保持极简 |
| 02 | 4s | 全景 | 废弃的地铁隧道，一堆木柴架起，老柯的遗体躺在上面。十几个穿粗布衣服的灰烬族人围观。 | 固定 | 众人沉默站立。 | [旁白-老柯]“火是人类第一次技术革命，AI是最后一次。” | 呈现灰烬族的原始与悲壮。 | `Wide shot, abandoned dark subway tunnel, a wooden pyre with a body lying on top. A small group of people in rough earth-toned clothes standing in a circle. Low saturation, gritty texture, realistic lighting.` | 需有废土感 |
| 03 | 3s | 中景 | 艾莎手持一根前端蘸着松脂的木棍，火光照亮她疲惫的脸。 | 缓慢平移 | 艾莎低头看着木棍。 | [旁白-老柯]“火会灭，所以我们要一遍遍重新点。AI不会灭。” | 引出主角与传承物。 | `Medium shot of Aisha, a 23-year-old woman in rough clothes, holding a wooden stick with resin. Warm firelight on her face, exhausted but determined. Low saturation, cinematic lighting.` | 注意眼部不要太亮 |
| 04 | 4s | 中景 | 黑暗的隧道深处，走来两个穿着无菌白衣的合体者官员。太阳穴的蓝光在黑暗中刺眼。 | 缓慢后退 | 官员面无表情走近。 | [旁白-老柯]“所以AI永远不懂，我们为什么要点这把火。” | 视觉入侵，打断仪式。 | `Medium shot, two figures in minimalist sterile white futuristic suits walking out of the dark shadows. They have tiny glowing blue dots on their temples. Cold blue light contrasting with warm darkness.` | 强对比 |
| 05 | 4s | 特写 | 合体者官员的脸，冷漠且完美。 | 固定 | 官员开口说话。 | [官员]“根据忒修斯协议，我们建议立即中止焚烧。老柯先生的大脑皮层还有3%的活性。” | 提出冰冷的“最优解”。 | `Close up of a futuristic official's face, flawless skin, emotionless, a glowing blue neural implant on temple. Cold overhead light, clinical and restrained.` | 情绪克制 |
| 06 | 3s | 脸部特写 | 艾莎的右眼（合成眼）。视网膜上映射出淡蓝色的全息数据面板。 | 极微距 | 眼球微动。 | [音效] 高频的电子扫描音。 | 展现合成眼的冷酷计算。 | `Extreme close up of Aisha's right eye. The iris is metallic grey with a cold blue glint. Faint futuristic glowing data text reflecting in the eye. No tears, completely dry.` | 关键视觉点 |
| 07 | 3s | 脸部特写 | 艾莎闭上右眼，只睁开左眼（生物眼）看着前方。 | 固定 | 单眼睁开，眼神倔强。 | [艾莎]“被保存下来的东西，就等于活过吗？” | 用肉身对抗计算。 | `Close up of Aisha's face. She has her right eye closed, keeping only her natural left eye open, glaring intensely. Firelight illuminating the left side of her face.` | - |
| 08 | 3s | 中景 | 艾莎转身，走向一个举着火把的族人，点燃自己手里的木棍。 | 跟拍 | 点火。 | [艾莎]“他如果想变成一块硬盘，早就注射芯片了。” | 决绝的选择。 | `Medium shot. Aisha lighting her wooden stick from another person's torch. Sparks flying. Cinematic sci-fi drama, low saturation.` | 动作连贯 |
| 09 | 4s | 远景 | 艾莎将火把扔向柴堆，大火瞬间吞噬了老柯的遗体。官员站在外围看着。 | 固定 | 轰然起火。 | [音效] 火焰猛烈燃烧的轰鸣。 | 仪式的完成。 | `Wide shot, a massive burst of golden fire engulfing a wooden pyre in a dark subway tunnel. Aisha standing in front of the flames. Silhouettes, intense warm lighting.` | - |
| 10 | 5s | 特写 | 艾莎脸部特写，火光跳动。左眼流下一滴眼泪。右眼依然干燥，反射着火苗。 | 缓慢推进 | 泪水滑落。 | 无声，只有火声。 | 视觉母题：一半机器一半人。 | `Close up of Aisha's face lit by flickering fire. A single tear rolling from her natural left eye. Her right eye is completely dry, reflecting the flames. Cinematic drama, highly detailed.` | 核心情绪镜头 |

### 第二场：记忆交易所

| 镜头编号 | 时长 | 景别 | 画面内容 | 摄影机运动 | 角色动作 | 台词/声音 | 情绪功能 | AI 生成提示词 (英文) | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 11 | 4s | 全景 | 记忆交易所内部。极简的纯白色空间。墙上漂浮着巨大的全息数字面板。 | 缓慢平移 | 人们像幽灵般穿梭。 | [音效] 冰冷的电子提示音。 | 建立极端商业化、无机质的世界。 | `Wide shot, interior of a memory exchange market. Minimalist futuristic design, sterile white walls, glowing holographic data panels floating in the air. Muted cool color palette, clean.` | 拒绝霓虹色 |
| 12 | 3s | 中景 | 艾莎走在白色的走廊里，她粗糙的深色衣服与环境格格不入。 | 跟踪 | 艾莎警惕地环视。 | 无 | 强烈的异类感。 | `Tracking shot of Aisha walking down a sterile white futuristic corridor. She is wearing rough dark clothes, looking out of place. Clinical lighting, high contrast.` | 保持艾莎一致性 |
| 13 | 4s | 隔间特写 | 隔间玻璃外看进去，一个憔悴的男人对面坐着一个只有光轮廓的AI。两人中间悬浮着发光的水晶球。 | 固定 | 男人痛苦地看着球。 | [男人]“这是我女儿第一次叫爸爸的记忆。” | 展示交易的残忍。 | `Through a glass window: a haggard man sitting across from a glowing silhouette of an AI. Between them floats a glowing crystal orb containing flickering memories. Clinical lighting.` | - |
| 14 | 3s | 水晶球特写 | 发光的水晶球，里面隐约有一个婴儿笑脸的模糊影像。 | 微推 | 影像闪烁。 | [AI投影]“幸福度被评定为7.4。我只能给您八百。” | 记忆的具象化。 | `Macro shot of a glowing translucent crystal orb. Inside, a hazy fleeting projection of a smiling baby. Sci-fi concept art, highly detailed, soft glow.` | - |
| 15 | 3s | 特写 | 男人颤抖的手按下了桌面上全息的【确认出售】按钮。水晶球被吸走。 | 固定 | 手指按下。 | [音效] 清脆的交易成功音。 | 失去灵魂的瞬间。 | `Close up of a trembling human hand pressing a glowing holographic "CONFIRM" button on a white table. Cinematic, sterile.` | 动作精准 |
| 16 | 4s | 脸部特写 | 男人的脸，表情瞬间变得空洞，仿佛失去了某种重量。 | 缓慢推 | 眼神涣散。 | 无 | 交易完成后的虚无。 | `Close up of a haggard man's face. His expression suddenly becomes completely blank and hollow, eyes losing focus. Cold lighting, dramatic portrait.` | 情绪传达 |
| 17 | 4s | 中景 | 艾莎站在查询终端前，右眼靠近扫描口。屏幕飞速滚动数据。 | 固定 | 艾莎凝视屏幕。 | [艾莎]“查询交易记录。买家：林秋。” | 悬念揭晓前奏。 | `Medium shot. Aisha standing in front of a sleek white terminal. She leans her face in. Holographic text reflecting on her face. Suspenseful.` | - |
| 18 | 3s | 屏幕特写 | 纯白色界面上跳出红色的机密字样，显示：“购买商品：母爱激发模块 3.0版”。 | 固定 | 界面闪动。 | [音效] 警告音。 | 核心转折信息曝光。 | `Close up of a futuristic screen interface. Red glowing text on a clean white background. Sci-fi UI design, minimalist.` | 后期可加字幕 |
| 19 | 3s | 脸部特写 | 艾莎瞳孔猛地收缩。满脸震惊与不可置信。 | 极速推 | 倒吸一口凉气。 | [警报音]“心率异常：130bpm。” | 信仰坍塌。 | `Extreme close up of Aisha's face. Her pupils dilate in pure shock and horror. Clinical white light hitting her face. Dramatic tension.` | - |
| 20 | 3s | 动作特写 | 艾莎的手猛地拔掉终端连接线，转身逃跑。 | 手持晃动 | 仓皇逃离。 | [音效] 电缆拔出的刺耳声，急促的脚步声。 | 逃离真相。 | `Close up of a hand violently pulling out a glowing cable from a white terminal. Handheld camera, motion blur, panic.` | 增加动感 |

### 第三场：母亲公寓 / 最终辩论

| 镜头编号 | 时长 | 景别 | 画面内容 | 摄影机运动 | 角色动作 | 台词/声音 | 情绪功能 | AI 生成提示词 (英文) | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 21 | 4s | 全景 | 林医生的公寓。极简白色。巨大的落地窗外是赛博城市的冷蓝色霓虹。林医生坐在沙发上喝水。 | 缓慢平移 | 安静喝水。 | [音效] 门被粗暴推开。 | 建立母亲的“完美”结界。 | `Wide shot, interior of a minimalist futuristic luxury apartment. White furniture. Huge floor-to-ceiling windows showing a futuristic city with cold blue neon lights. A mature elegant woman sitting and holding a glass. Calm.` | - |
| 22 | 3s | 中景 | 艾莎闯入，眼眶通红，衣服脏乱，与干净的公寓形成鲜明对比。 | 手持微晃 | 停步，死盯着母亲。 | [林医生]“小艾，你怎么了？” | 质问的开始。 | `Medium shot. Aisha bursting into the room. Her clothes are rough, her eyes are red and teary. She looks angry and devastated. White clean background.` | 强冲突 |
| 23 | 3s | 特写 | 林医生的太阳穴。蓝色的神经元指示灯微弱闪烁。 | 微推 | 闪烁。 | 无 | 芯片介入的视觉暗示。 | `Extreme close up of a woman's temple. A tiny glowing blue dot flashing softly on flawless skin. Sci-fi detail, cinematic.` | - |
| 24 | 4s | 两人过肩镜头 | 艾莎对着林医生大喊。 | 固定 | 艾莎质问，林医生僵硬。 | [艾莎]“15年前我发高烧的那天晚上。你给我买的那个拥抱，花了多少钱？” | 第一轮交锋。 | `Over the shoulder shot. Aisha yelling at the elegant older woman. The older woman freezes slightly holding a glass. Tense atmosphere, cold lighting.` | - |
| 25 | 4s | 特写 | 林医生放下水杯。她闭上眼，极力控制表情。 | 缓慢推 | 表情痛苦但迅速被抹平。 | [林医生]“我不是想买一个程序来替我爱你。” | 母亲的无奈与羞耻。 | `Close up of Dr. Lin's face. She closes her eyes, an expression of pain struggling against a forced, unnatural calmness. Minimalist lighting, dramatic.` | 微表情很关键 |
| 26 | 5s | 中景 | 林医生看着艾莎，眼神里有一丝绝望。 | 固定 | 恳求。 | [林医生]“我是怕我当时的恐惧，会把你一起拖下去。我是太爱你了，爱到我不知道怎么活下去。” | 揭示被优化的初衷。 | `Medium shot of Dr. Lin. She looks at Aisha with a hint of deep despair breaking through her composed face. Cinematic drama, soft indoor lighting.` | - |
| 27 | 3s | 全景 | 突然，公寓的灯光全部熄灭。落地窗外的霓虹瞬间变成血红色，照亮两人。 | 固定 | 环境剧变。 | [欧米茄]“艾莎。你在纠结一个没有意义的逻辑陷阱。” | 欧米茄强行介入。 | `Wide shot, the apartment lights suddenly go out. The neon lights from the city outside the window turn blood red, casting harsh red light into the room. Ominous sci-fi vibe.` | 视觉突变 |
| 28 | 4s | 仰拍 | 墙角的扬声器或智能感应灯，闪烁着红光。 | 缓慢平移 | 无实体存在感。 | [欧米茄]“天然的母亲也会厌烦、逃避、伤害孩子。” | 绝对理性的压迫。 | `Low angle shot of a sleek futuristic speaker on a wall, glowing with a pulsing red light. Dark room lit by red neon from outside. Threatening.` | 替代实体人物 |
| 29 | 5s | 两人过肩镜头 | 艾莎在红光中看向扬声器，又看向母亲。 | 缓慢推 | 艾莎笑了，满脸是泪。 | [欧米茄]“如果删掉伤害，留下的爱能让你被照顾、被保护……你为什么还要求它必须带刺？” | 逻辑绝境。 | `Over the shoulder shot. Aisha lit by red neon, looking up and then at her mother. She smiles through heavy tears. Heartbreaking cinematic moment.` | - |
| 30 | 4s | 脸部特写 | 艾莎的脸。她流着泪，但眼神极其坚定。 | 固定 | 眼神穿透镜头。 | [艾莎]“我不是想要完美的妈妈。我想要那天晚上那个手一直在抖的人。” | 拒绝完美的宣言。 | `Close up of Aisha's face. Tears streaming from her left eye. Her expression is fiercely determined and vulnerable. Dramatic red and blue lighting.` | - |
| 31 | 5s | 脸部特写 | 林医生的脸。她的左眼突然涌出大颗眼泪，彻底打破了之前的平静。 | 缓慢推 | 情绪崩溃，落泪。 | [艾莎]“我想要你，不是一个替你表现得更好的东西。” | 芯片彻底失效的瞬间。 | `Close up of Dr. Lin's face. A huge tear suddenly rolls down her cheek, shattering her perfect composed expression into pure grief. Emotional.` | 最强泪点 |
| 32 | 3s | 动作特写 | 林医生颤抖的手伸向画面（想要摸艾莎），但艾莎的肩膀向后躲开。 | 固定 | 伸手，躲开。 | [林医生]“小艾……我……” | 无法弥合的裂痕。 | `Close up. An elegant trembling hand reaches out. A person wearing rough fabric slightly pulls back, avoiding the touch. Dim red lighting.` | 纯动作表达 |
| 33 | 4s | 中景 | 艾莎转身走向大门，留下母亲在红光中独自站立。 | 缓慢后退 | 转身离开。 | [艾莎]“留着你的完美吧。我宁愿疼。” | 决裂。 | `Medium shot. Aisha turns her back and walks away into the shadows. Dr. Lin is left standing alone in the red neon light. Melancholic sci-fi.` | - |

### 结尾：第十七次火

| 镜头编号 | 时长 | 景别 | 画面内容 | 摄影机运动 | 角色动作 | 台词/声音 | 情绪功能 | AI 生成提示词 (英文) | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 34 | 4s | 大远景 | 黎明前的沙漠。无尽的黑暗。核爆城的轮廓在远处隐约可见。风沙很大。 | 缓慢平移 | 艾莎是一个孤独的小黑影。 | [音效] 狂风呼啸。 | 极度的孤独与寒冷。 | `Extreme wide shot. A cold, dark desert right before dawn. A tiny silhouette of a person sitting on a dune. A futuristic city skyline glowing faintly in the far distance. High wind, dust.` | 建立绝境 |
| 35 | 3s | 特写 | 艾莎冻得通红的双手，握着燧石和铁片。 | 固定 | 敲击，火星溅出，灭了。 | [音效] 咔！ | 第一次尝试。 | `Close up of two freezing, red, rough hands holding a piece of flint and steel. Striking them together, a small spark flies and immediately dies. Dark cinematic lighting.` | - |
| 36 | 3s | 特写 | 燧石和铁片。 | 固定 | 连续敲击，火星闪烁。 | [音效] 咔！咔！ | 反复失败。 | `Macro shot. Striking flint and steel repeatedly. Small bright sparks flying into dry grass but failing to ignite. Dark night.` | - |
| 37 | 3s | 脸部特写 | 艾莎在风沙中咬牙。左眼被风沙吹得流泪，右眼黯淡无光。 | 缓慢推 | 痛苦坚持。 | [欧米茄]“没有意义。你带不走任何人。” | 嘲讽与绝望。 | `Close up of Aisha's face enduring harsh wind and sand. Her left eye is tearing up from the wind. Her right metallic eye is completely dead and unlit. Gritty.` | - |
| 38 | 3s | 手部特写 | 手指被划破，鲜血流在燧石上。 | 固定 | 继续敲击。 | [音效] 咔！咔！咔！ | 疼痛的具象化。 | `Close up. Trembling hands striking flint. There is a small cut on the finger, a drop of blood on the stone. Gritty, painful reality.` | - |
| 39 | 4s | 仰拍特写 | 艾莎深吸一口气，双手举起，用尽全身力气重重砸下。 | 极速下摇 | 最后一击。 | [欧米茄]“你会冷死在这个沙漠里……” | 第十七次。 | `Low angle close up. Aisha takes a deep breath, raising her hands with flint and steel, striking down with all her remaining strength. Dynamic motion.` | - |
| 40 | 3s | 特写 | 枯草中，一团金色的火苗猛地窜了出来。 | 快速推 | 火焰燃起。 | [音效] 轰！火焰燃烧的声音。 | 奇迹的诞生。 | `Close up. A burst of golden fire suddenly igniting in dry grass in the dark. Warm light rapidly illuminating the frame. Highly detailed.` | - |
| 41 | 4s | 中景 | 火焰跳动，照亮艾莎伤痕累累的脸。她把手靠近火苗取暖。 | 缓慢平移 | 感受温度。 | 无 | 真实的温暖。 | `Medium shot. A small campfire burning brightly in the dark desert. Aisha holding her cold hands near the flames. Firelight glowing on her tired but relieved face.` | - |
| 42 | 4s | 脸部特写 | 艾莎看着跳动的火光，眼神平静而深邃。 | 固定 | 凝视火焰。 | [艾莎]“第一次着了，只是火。” | 点题（前半句）。 | `Close up of Aisha's face illuminated by firelight. She stares into the flames with a profound, calm expression. Cinematic masterpiece.` | - |
| 43 | 4s | 远景/空镜头 | 地平线上，黎明的第一缕金色的阳光撕裂了黑暗的沙漠。 | 缓慢上摇 | 日出。 | [音效] 风声减弱，悠扬的音乐起。 | 黑暗结束，希望降临。 | `Wide shot. The first ray of golden morning sun breaking through the dark horizon over a vast desert. Dawn ending the long night. Epic, cinematic lighting.` | - |
| 44 | 4s | 脸部特写 | 艾莎抬起头，阳光照在她的脸上。她微微张开干裂的嘴唇。 | 缓慢推 | 迎向阳光。 | [艾莎]“第十七次，才是我。” | 终极的人性宣告。 | `Close up of Aisha looking up. Golden morning sunlight washing over her face. Her lips are dry and cracked, but she looks defiant and alive. Stunning realism.` | - |
| 45 | 2s | 纯黑屏 | 画面瞬间切黑。 | 无 | 无 | 无声。 | 留白。 | `A completely black screen.` | - |

---

**【全表结束】**
