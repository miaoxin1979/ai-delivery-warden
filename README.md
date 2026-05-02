# AI Delivery Warden

**A local quality gate for AI-generated product and code deliveries.**

[中文说明](README.zh-CN.md)

AI coding agents are fast. They also ship half-finished pages, fake buttons, missing tests, vague handoffs, accidental scope creep, and "should work" confidence without proof.

AI Delivery Warden is a small local CLI that reviews an AI agent's delivery notes, handoff, and optional git diff against real-delivery rules.

It does not write code for you. It asks the uncomfortable questions before you accept the work.

## What It Catches

- No evidence that the agent read the project
- Missing acceptance criteria
- Missing verification commands or results
- Fake UI or mock data risk
- Unauthorized phasing such as "MVP first" or "later"
- Weak handoff notes that cannot restore context
- Missing backup or rollback plan
- Vague confidence such as "should work"
- Scope boundary not declared

## Install

```bash
git clone https://github.com/YOUR_NAME/ai-delivery-warden.git
cd ai-delivery-warden
python3 -m pip install -e .
```

## Usage

Review an AI delivery note:

```bash
warden examples/bad_delivery.md
```

Chinese report:

```bash
warden examples/bad_delivery_zh.md --lang zh
```

Review stdin:

```bash
cat examples/bad_delivery.md | warden
```

Review a delivery note plus the current git diff:

```bash
warden delivery.md --git-diff
```

Write a report:

```bash
warden delivery.md --output warden-report.md
```

## Example Output

```text
# AI Delivery Warden Report

- Status: BLOCK
- Score: 0/100
- Findings: 9

## Findings

1. [CRITICAL] Missing verification evidence
   - Fix: Reject the delivery until commands, outputs, screenshots, API responses, or data evidence are provided.
```

## Philosophy

AI Delivery Warden is built around a simple rule:

> No evidence, no delivery.

It is inspired by the practical pain of managing AI agents that say work is complete before it is usable.

The intended workflow:

```text
Prompt AI agent
↓
Agent delivers code / notes / handoff
↓
Run AI Delivery Warden
↓
If blocked, paste the return prompt back to the agent
↓
Agent fixes and re-submits
```

## Roadmap

- Configurable rule packs
- Chinese and English output modes
- JSON output for automation
- GitHub PR review mode
- Screenshot and Playwright evidence checks
- Handoff quality scoring
- Secret and destructive-change detection
- Project-specific rule files such as `WARDEN.md`

## License

MIT
