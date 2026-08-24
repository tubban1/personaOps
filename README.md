<div align="center">

```text
 ██████╗ ███████╗██████╗ ███████╗██████╗ ███╗   ██╗██████╗  ██████╗ ███████╗
 ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔══██╗██╔═══██╗██╔════╝
 ██████╔╝█████╗  ██████╔╝███████╗██║  ██║██╔██╗ ██║██║  ██║██║   ██║███████╗
 ██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║  ██║██║╚██╗██║██║  ██║██║   ██║╚════██║
 ██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║██████╔╝╚██████╔╝███████║
 ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝
```

# PersonaOps — Industrial AI Persona Operating System

**Unified Autonomous AI Persona Operating Framework Built with Python, FastAPI, Streamlit, & Playwright**

[ 🇺🇸 **English** ](./README.md) • [ 🇨🇳 **中文文档** ](./README_CN.md)

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=mit)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Playwright](https://img.shields.io/badge/Playwright-Automated-45BA4B?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-DALL--E--3%20%7C%20VectorEngine-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=github-actions)](https://github.com/tubban1/personaOps)

</div>

---

## 💡 What is PersonaOps?

`personaOps` is an industrial-grade, fully closed-loop AI persona operating system. It integrates persona planning, brand alignment, interaction sensing, high-fidelity media production, and multi-platform distribution into a unified autonomous execution engine.

---

## ⚡ Key Features

<table width="100%">
<tr>
<td width="50%" valign="top">

### 🎭 1. Persona & Brand Domain Modeling
* **Persona Sovereignty Contract**: Defines "who I am" and "who I serve".
* **ContentBrain Narrative Engine**: Automated generation of time-continuous `PostPlan`s.

</td>
<td width="50%" valign="top">

### 🧠 2. Interaction Sensing & Risk Control
* **Audience Intent Recognition**: Real-time sensing of comments, likes, and DMs.
* **Risk & Compliance Filter**: Automated sensitive word detection & safety alerts.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎨 3. High-Fidelity Media Pipeline
* **Dual Media Engine**: HTML/CSS template rendering combined with AI image generation (DALL-E 3).
* **`MediaPackage` Contract**: Lossless visual output tailored for social platforms.

</td>
<td width="50%" valign="top">

### 🚀 4. Multi-Platform Automated Driver
* **Playwright Driver**: Automated physical execution for Xiaohongshu (XHS) & Instagram.
* **Audit Domain**: Token cost & financial audit ledger tracking every action.

</td>
</tr>
</table>

---

## 🛠️ Architecture & Workflow

```mermaid
graph TD
    A[🎭 Persona & Brand Config] -->|Brand Alignment| B(🧠 ContentBrain Narrative Engine)
    B -->|PostPlan Contract| C(🎨 MediaCoordinator Visual Production)
    C -->|AI Painting & Templates| D(📦 MediaPackage)
    D -->|Playwright Automation| E(🚀 Multi-Platform Publisher)
    E -->|Publish to XHS / Instagram| F[📱 Social Media Channels]
    E -->|Write Audit Record| G(📊 AuditLedger Financial Tracking)
```

---

## 📁 Directory Structure

```
personaOps/
├── app/                 # ContentBrain, MediaCoordinator, Publisher, & Audit
├── data/entities/       # Persona & Brand JSON schema configs
├── docs/                # Architecture specification whitepapers
├── main.py              # CLI entry point
└── dashboard_main.py    # Streamlit/Dash operations dashboard
```

---

## ⚡ Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt
playwright install chromium

# 2. Run default persona pipeline
python3 main.py
```

---

## 🤝 License

Released under the **MIT License**.
