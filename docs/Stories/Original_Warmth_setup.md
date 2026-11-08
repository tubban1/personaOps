# 《原始温度 (Original Warmth)》 - AI 视觉一致性基础设定 (Setup)

在正式按分镜表跑图之前，**必须先完成本设定表的生成**。
通过固定人物和场景的“视觉锚点图 (Base Image)”，在后续的分镜生成中作为**参考图（Image Prompt / Character Reference）**输入，这是保证全片 3 分钟视觉一致性的唯一方法。

---

## 一、 核心人物视觉锚点 (Character Reference)

### 1. 艾莎 (Aisha) - 冲突与痛苦的容器
**角色定调**：粗糙、真实、带着一种疲惫的狠劲。她从底层来，身上带着赛博朋克世界边缘的尘土气。
**核心特征**：
- **右眼**：明显的廉价合成机械眼（不要做成炫酷的高级眼，要像是一块突兀的金属，永远干涩）。
- **左眼**：正常的生物眼（会流血、流泪）。
- **穿着**：深灰色、有磨损和油污的重型夹克，内搭深色粗布T恤。

**【AI 生图提示词库：艾莎】**
> **正脸参考图 (Front Portrait)**:
> `Cinematic portrait of Aisha, a 23-year-old gritty woman in a near-future dystopian world. Her right eye is a visibly artificial metallic right eye with a dry glassy surface and faint blue reflection, not sleek, slightly outdated, while her left eye is a normal human brown eye. She has messy, slightly oily dark hair. Wearing a worn-out, heavy dark grey jacket with rough textures. Harsh contrast lighting. Ultra-detailed, photorealistic, 8k.`
> 
> **侧脸参考图 (Side Profile)**:
> `Side profile portrait of Aisha, a 23-year-old gritty woman. Showcasing a visibly artificial metallic right eye with a dry glassy surface and faint blue reflection, slightly outdated. Messy dark hair, worn-out dark jacket. Dark background, dramatic side lighting.`

*操作建议：用这组词跑出最满意的一张脸后，固定 Seed，作为艾莎的所有分镜底图。*

---

### 2. 林医生 (Dr. Lin) - 完美的虚假
**角色定调**：极度整洁、高贵、优雅，但有一种不可侵犯的塑料感。她依靠技术隔离了痛苦。
**核心特征**：
- **脸部**：皮肤完美无瑕，没有皱纹（45岁像30岁）。
- **关键植入物**：右侧太阳穴有一个微小的环形发光体（母爱模块），散发柔和的**蓝光**。
- **穿着**：极其极简的纯白色高领居家服，面料垂坠感极好。

**【AI 生图提示词库：林医生】**
> **正脸参考图 (Front Portrait)**:
> `Cinematic portrait of Dr. Lin, an elegant 45-year-old Asian woman who appears in her mid-30s due to technological enhancement. Flawless smooth skin, perfectly groomed dark hair pulled back. On her right temple, there is a very small, elegant glowing blue circular implant. She wears a minimalist, pure white high-neck silk loungewear. Soft, clinical cold white lighting. Ultra-detailed, photorealistic, 8k.`
> 
> **情绪崩溃测试图 (Emotion Breakdown Test)**:
> `Cinematic portrait of Dr. Lin, an elegant 45-year-old Asian woman who appears in her mid-30s due to technological enhancement, in pure white minimalist clothing. The blue implant on her temple is turned off. Her flawless face is distorted by intense panic and fear, tears welling up in her eyes. Dramatic red ambient lighting. Ultra-detailed.`

*操作建议：确保林医生的白衣服和发光模块在任何光线下都清晰可见。*

---

## 二、 核心场景视觉锚点 (Scene Reference)

### 1. 冰冷的完美公寓 (Dr. Lin's Apartment)
这是全片 95% 的发生地。
**场景定调**：不像家，像一个没有人类情感的手术室或极简美术馆。
**核心元素**：
- 纯白色冷色调，没有多余的杂物，白色的沙发，透明的玻璃茶几。
- 巨大的落地窗，窗外是近未来科幻城市的克制灯光（作为背景失焦）。

**【AI 生图提示词库：常态公寓】**
> **全景底图 (Wide Shot - Normal)**:
> `Wide shot of a hyper-minimalist futuristic living room. Completely sterile and clinical. White sofa, transparent glass coffee table, no personal belongings. A giant floor-to-ceiling window overlooking a near-future sterile sci-fi city with restrained futuristic city lights and a distant cityscape. The indoor lighting is cold white and blue. Cinematic lighting, architectural photography, 8k.`

### 2. 欧米茄的红光降临 (The Red Room)
这是短片中段最大的视觉转折。当欧米茄介入时，公寓原本的冷白光瞬间被切断，变成压迫感极强的红色。
**核心元素**：
- 墙壁上的隐形扬声器矩阵亮起红灯。
- 整个房间被深红色的警报光笼罩，窗外的城市灯光也被红色吞噬。

**【AI 生图提示词库：红光公寓】**
> **全景底图 (Wide Shot - Red Light)**:
> `Wide shot of a hyper-minimalist futuristic living room bathed entirely in ominous, deep red emergency lighting. A sleek wall speaker grid is glowing with intense red light. Dark heavy shadows. The sci-fi cityscape outside the window is also tinted red. Oppressive and dramatic atmosphere. Cinematic lighting, 8k.`

---

## 三、 视觉资产使用指南

**【全局通用负面提示词 (Negative Prompt)】**
在生成所有人物和场景时，**务必全局挂载**以下负面词，以压制廉价的赛博朋克风和卡通感，确保画面呈现高级的电影质感：
> `no anime, no cartoon, no glossy superhero armor, no exaggerated cyberpunk fashion, no colorful neon overload, no robot body, no extra facial implants, no duplicated eyes, no deformed hands`

1. **先做加法，再做减法**：在 Midjourney/Kling 等工具中，先生成这 6 张基础参考图（艾莎 2 张、林医生 2 张、公寓 2 张）。
2. **垫图生成（Image-to-Image / Cref）**：
   - 制作分镜表里的**第 03-08 镜**时，强制挂载【常态公寓】背景和对应的【角色正面参考图】。
   - 制作分镜表里的**第 09-22 镜**时，强制挂载【红光公寓】背景，提示词中强调 `Red dramatic lighting`。
3. **保持光效高于动作**：如果 AI 无法完美还原林医生“摔破杯子”的复杂动作，退而求其次：只要保证**太阳穴的蓝光熄灭**，且脸上出现极度的**恐慌表情**，观众的情绪就能完美衔接。光效就是这片子的动作戏。
