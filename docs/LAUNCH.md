# Launch Notes

This file contains copy you can adapt for sharing AI Delivery Warden.

## One-line Pitch

EN:

```text
I got tired of AI agents shipping fake features, so I built a delivery warden.
```

中文：

```text
我受够了 AI 交半成品，所以做了一个 AI 交付监工。
```

## Hacker News

```text
Show HN: AI Delivery Warden – a quality gate for AI-generated code deliveries

AI coding agents are fast, but they often ship half-finished UI, mock data, vague handoffs, and "should work" confidence without verification.

AI Delivery Warden is a small local CLI that reviews an agent's delivery note, handoff, and optional git diff. It checks for acceptance criteria, verification evidence, real data flow, rollback/scope notes, fake implementation risk, and unauthorized phasing.

It outputs a PASS/BLOCK report plus a return prompt you can paste back to the agent.

Repo: https://github.com/miaoxin1979/ai-delivery-warden
```

## Reddit / SideProject

```text
I kept running into the same AI coding-agent problem:

The agent says "done", but it only built a fake page, used mock data, skipped tests, or left a vague handoff.

So I built AI Delivery Warden: a local CLI that checks the agent's delivery note before you accept the work.

It looks for:
- missing verification evidence
- missing acceptance criteria
- fake UI / mock data risk
- unauthorized "MVP first, real API later"
- weak handoffs
- no rollback/scope notes

It outputs a BLOCK/PASS report and a return prompt you can paste back to the AI.

Repo: https://github.com/miaoxin1979/ai-delivery-warden

Would love feedback on what other "AI delivery lies" it should catch.
```

## 中文社区

```text
我受够了 AI 交半成品，所以做了一个小工具：AI Delivery Warden。

它不是写代码的 Agent，而是“AI 交付监工”：

把 AI 的交付说明/交接/代码 diff 丢进去，它会检查：
- 有没有验收标准
- 有没有验证命令和结果
- 有没有真实 API/数据流
- 有没有 mock/假页面
- 有没有擅自分期
- 交接是不是太粗
- 有没有回滚和影响范围

如果不合格，它会输出 BLOCK，并生成一段可以直接贴回 AI 的返工口令。

GitHub: https://github.com/miaoxin1979/ai-delivery-warden
```
