# PersonaOps 测试手册 (Testing)

## 🧪 1. 概述
系统采用领域测试与 E2E 冒烟测试相结合的验证策略。

## ⚙️ 2. 执行测试

### A. 全量测试
```bash
python3 -m unittest discover tests
```

### B. 按领域运行
```bash
python3 -m unittest tests/test_core_paths.py
```

## 🛠️ 3. 测试关注领域

### 1. 资源探测与路径 (Critical)
验证在任何环境下都能定位到 `data/` 目录。
- **关联文件**：`tests/test_core_paths.py`

### 2. E2E 全链路冒烟 (Critical)
验证从内容计划 -> 资产包 -> 模拟发布 -> 审计全闭环逻辑。
- **关联文件**：`tests/test_end_to_end.py`

### 3. 驱动与发布验证 (In-Progress)
验证 XHS/Instagram 驱动程序对不同 Caption 长度与格式的适配。

## 📊 4. 自动化测试建议
1.  **Mock 优先**：默认测试在 `mock_mode=True` 下运行，以确保离线闭环。
2.  **清理逻辑**：建议在 CI 运行后清理 `data/assets/` 下的临时测试产物。
3.  **覆盖率要求**：生产级别逻辑需具备至少 80% 的单元测试覆盖率。

---
*Owl Lab Quality Assurance*
