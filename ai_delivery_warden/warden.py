from __future__ import annotations

from dataclasses import dataclass

from .rules import RULES, SEVERITY_WEIGHT, Rule, contains_any


@dataclass(frozen=True)
class Finding:
    rule: Rule
    message: str


@dataclass(frozen=True)
class Report:
    score: int
    status: str
    findings: tuple[Finding, ...]
    passed: tuple[str, ...]


def inspect_delivery(text: str) -> Report:
    findings: list[Finding] = []
    passed: list[str] = []
    penalty = 0

    for rule in RULES:
        failed = False
        if rule.required_any and not contains_any(text, rule.required_any):
            failed = True
            message = f"Missing evidence for: {rule.title}"
        elif rule.suspicious_any and contains_any(text, rule.suspicious_any):
            failed = True
            message = f"Suspicious signal found: {rule.title}"
        else:
            message = ""

        if failed:
            findings.append(Finding(rule=rule, message=message))
            penalty += SEVERITY_WEIGHT.get(rule.severity, 10)
        else:
            passed.append(rule.id)

    score = max(0, 100 - penalty)
    if any(f.rule.severity == "critical" for f in findings):
        status = "BLOCK"
    elif score < 70:
        status = "NEEDS_WORK"
    else:
        status = "PASS"

    return Report(score=score, status=status, findings=tuple(findings), passed=tuple(passed))


def render_markdown(report: Report) -> str:
    lines: list[str] = []
    lines.append("# AI Delivery Warden Report")
    lines.append("")
    lines.append(f"- Status: **{report.status}**")
    lines.append(f"- Score: **{report.score}/100**")
    lines.append(f"- Findings: **{len(report.findings)}**")
    lines.append("")

    if report.findings:
        lines.append("## Findings")
        lines.append("")
        for idx, finding in enumerate(report.findings, 1):
            rule = finding.rule
            lines.append(f"{idx}. **[{rule.severity.upper()}] {rule.title}**")
            lines.append(f"   - Category: `{rule.category}`")
            lines.append(f"   - Rule: `{rule.id}`")
            lines.append(f"   - Problem: {finding.message}")
            lines.append(f"   - Fix: {rule.advice}")
            lines.append("")
    else:
        lines.append("## Findings")
        lines.append("")
        lines.append("No blocking issues found by the current rules.")
        lines.append("")

    lines.append("## Suggested Return Prompt")
    lines.append("")
    if report.status == "PASS":
        lines.append("```text")
        lines.append("当前交付已通过本轮监工检查。请继续保持证据链，并在最终交付中保留验证命令、验证结果、修改文件和未验证风险。")
        lines.append("```")
    else:
        lines.append("```text")
        lines.append("停止。你的交付没有通过 AI Delivery Warden 检查。")
        lines.append("")
        lines.append("请按以下问题返工：")
        for finding in report.findings:
            lines.append(f"- {finding.rule.title}: {finding.rule.advice}")
        lines.append("")
        lines.append("返工后必须重新输出：完成内容、修改文件、真实功能说明、验收用例执行结果、验证命令、验证结果、未完成事项/风险和使用方式。")
        lines.append("```")

    return "\n".join(lines) + "\n"
