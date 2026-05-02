# AI Delivery Warden

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CLI](https://img.shields.io/badge/Type-CLI-black)
![Bilingual](https://img.shields.io/badge/Docs-EN%20%2F%20中文-orange)

**EN:** A local quality gate for AI-generated product and code deliveries.  
**中文：** 一个本地运行的 AI 交付监工工具，用来检查 AI 写完后的交付说明、交接内容和代码变更是否真的可验收。

> **EN:** No evidence, no delivery.  
> **中文：** 没有证据，不算交付。

AI coding agents are fast, but they often ship half-finished pages, fake buttons, mock data, missing tests, vague handoffs, accidental scope creep, and "should work" confidence without proof.

AI 编程 Agent 很快，但也经常交付半成品、假页面、假按钮、mock 数据、缺失测试、粗糙交接、擅自分期，以及“应该可以”这种没有证据的自信。

AI Delivery Warden does **not** write code for you. It reviews the agent's delivery and asks the uncomfortable questions before you accept the work.

AI Delivery Warden **不负责写代码**。它负责在你接受 AI 交付前，先替你问那些最容易被糊弄过去的问题。

If this saves you from accepting one fake AI delivery, a star would mean a lot.  
如果它帮你挡过一次 AI 半成品交付，欢迎点个 Star。

```bash
python3 -m ai_delivery_warden.cli examples/bad_delivery_zh.md --lang zh
```

---

## Why This Exists / 为什么做这个

**EN:** AI coding agents are becoming the new junior delivery team. They can move fast, but they need supervision: acceptance criteria, verification evidence, rollback plans, scope boundaries, and recoverable handoffs.

**中文：** AI 编程 Agent 正在变成新的“初级交付团队”。它们很快，但必须有人监督：验收标准、验证证据、回滚方案、影响范围、交接质量，一个都不能少。

This project is for people who are tired of:

这个项目适合受够了这些问题的人：

- "I finished it" with no tests / “我做完了”，但没有测试
- UI-only features / 只有页面，没有真实业务
- Mock data sold as real delivery / 用 mock 数据冒充真实交付
- "MVP first, real API later" / “先做 MVP，后续再接真实接口”
- Vague handoffs nobody can resume / 交接写得太粗，下一窗口完全接不上
- Users becoming the QA team / 最后变成用户自己当测试员

---

## Quick Demo / 快速演示

Bad delivery gets blocked:

坏交付会被拦住：

```bash
$ python3 -m ai_delivery_warden.cli examples/bad_delivery_zh.md --lang zh

# AI 交付监工报告
- 状态：BLOCK
- 分数：0/100
- 问题数：8
```

Good delivery passes:

好交付会通过：

```bash
$ python3 -m ai_delivery_warden.cli examples/good_delivery_zh.md --lang zh

# AI 交付监工报告
- 状态：PASS
- 分数：100/100
- 问题数：0
```

## How It Works / 工作原理

```mermaid
flowchart LR
    A["User Prompt<br/>用户需求"] --> B["AI Coding Agent<br/>开发 Agent"]
    B --> C["Delivery Note / Handoff / Git Diff<br/>交付说明 / 交接 / 代码变更"]
    C --> D["AI Delivery Warden<br/>AI 交付监工"]
    D --> E{"Quality Gate<br/>验收门禁"}
    E -->|PASS| F["Accept Delivery<br/>接受交付"]
    E -->|BLOCK| G["Return Prompt<br/>返工口令"]
    G --> B

    D -. checks .-> H["Project Context<br/>项目上下文"]
    D -. checks .-> I["Acceptance Criteria<br/>验收标准"]
    D -. checks .-> J["Verification Evidence<br/>验证证据"]
    D -. checks .-> K["Real Data Flow<br/>真实数据流"]
    D -. checks .-> L["Rollback / Scope / Handoff<br/>回滚 / 范围 / 交接"]
```

---

## What It Catches / 它能抓什么

| EN | 中文 |
|---|---|
| No evidence that the agent read the project | 没有证据证明 AI 读过项目 |
| Missing acceptance criteria | 缺少验收标准 |
| Missing verification commands or results | 缺少验证命令或验证结果 |
| Fake UI or mock data risk | 假页面 / mock 数据风险 |
| Unauthorized phasing such as "MVP first" or "later" | 未经允许擅自分期，比如“先做 MVP”“后续再接” |
| Weak handoff notes that cannot restore context | 交接太粗，无法恢复现场 |
| Missing backup or rollback plan | 缺少备份或回滚方案 |
| Vague confidence such as "should work" | “应该可以”“理论上没问题”这类无证据自信 |
| Scope boundary not declared | 没有说明影响范围 |

---

## When To Use It / 什么时候用

| EN | 中文 |
|---|---|
| Before accepting an AI coding agent's delivery | 接受 AI 编程 Agent 交付前 |
| Before merging AI-generated code | 合并 AI 生成代码前 |
| Before trusting a handoff note | 相信交接文档前 |
| When an agent says "should work" | AI 说“应该可以”时 |
| When you suspect mock data or fake UI | 怀疑有 mock 数据或假页面时 |

---

## Install / 安装

```bash
git clone https://github.com/miaoxin1979/ai-delivery-warden.git
cd ai-delivery-warden
python3 -m pip install -e .
```

You can also run it without installation from the project directory:

也可以不安装，直接在项目目录里运行：

```bash
python3 -m ai_delivery_warden.cli examples/bad_delivery_zh.md --lang zh
```

---

## Usage / 使用

### English report

```bash
warden examples/bad_delivery.md
```

### 中文报告

```bash
warden examples/bad_delivery_zh.md --lang zh
```

### Review stdin / 检查标准输入

```bash
cat examples/bad_delivery.md | warden
```

### Review a delivery note plus current git diff / 同时检查交付说明和当前 git diff

```bash
warden delivery.md --git-diff --lang zh
```

### Write a report / 输出报告到文件

```bash
warden delivery.md --lang zh --output warden-report.md
```

---

## Real Workflow / 真实使用流程

```mermaid
sequenceDiagram
    participant U as User / 用户
    participant A as AI Agent / AI开发者
    participant W as Warden / 交付监工

    U->>A: Ask for a feature / 提需求
    A->>U: Delivery note + code changes / 交付说明和代码变更
    U->>W: Run warden delivery.md --lang zh
    W->>U: PASS or BLOCK report / 通过或阻塞报告
    alt BLOCK
        U->>A: Paste return prompt / 粘贴返工口令
        A->>U: Fix and resubmit / 返工后重新交付
    else PASS
        U->>U: Accept delivery / 接受交付
    end
```

---

## Example Output / 输出示例

```text
# AI 交付监工报告

- 状态：BLOCK
- 分数：0/100
- 问题数：8

## 问题清单

1. [CRITICAL] 缺少验证证据
   - 返工要求：没有命令输出、截图、接口返回或数据证据前，不接受交付。
```

---

## Status Meaning / 状态含义

| Status | EN | 中文 |
|---|---|---|
| PASS | No blocking issue found by current rules | 当前规则没有发现阻塞问题 |
| NEEDS_WORK | Issues found, but not critical | 有问题，需要补充 |
| BLOCK | Critical delivery risk found | 存在关键交付风险，不建议接受 |

---

## Philosophy / 理念

**EN:** AI Delivery Warden treats an AI agent like a delivery team, not a chatbot. The agent must prove the work is complete with context, acceptance criteria, real data flow, verification evidence, and a recoverable handoff.

**中文：** AI Delivery Warden 把 AI 当成交付团队来管理，而不是聊天助手。AI 必须用项目上下文、验收标准、真实数据流、验证证据和可恢复交接来证明自己真的完成了。

---

## Roadmap / 路线图

- Configurable rule packs / 可配置规则包
- JSON output for automation / JSON 输出，方便自动化
- GitHub PR review mode / GitHub PR 审查模式
- Screenshot and Playwright evidence checks / 截图和 Playwright 验证证据检查
- Handoff quality scoring / 交接质量评分
- Secret and destructive-change detection / 密钥和危险改动检测
- Project-specific rule files such as `WARDEN.md` / 支持项目级 `WARDEN.md` 规则文件

---

## Contributing / 参与贡献

Issues and rule suggestions are welcome.

欢迎提交 issue、规则建议和真实的 AI 糊弄案例。

Good first contributions:

适合先做的贡献：

- Add new suspicious phrases / 增加新的可疑表达
- Add new rule categories / 增加新的规则分类
- Improve Chinese and English wording / 优化中英文文案
- Add JSON output / 增加 JSON 输出
- Add GitHub PR mode / 增加 GitHub PR 模式

---

## Star History / Star 记录

If this project resonates with you, please consider starring it so more people can find it.

如果这个项目戳中了你的痛点，欢迎点个 Star，让更多人看到它。

---

## License / 许可证

MIT
