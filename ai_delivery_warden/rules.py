from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    id: str
    title: str
    severity: str
    category: str
    required_any: tuple[str, ...] = ()
    suspicious_any: tuple[str, ...] = ()
    advice: str = ""


RULES: tuple[Rule, ...] = (
    Rule(
        id="project-context",
        title="No project context evidence",
        severity="high",
        category="preflight",
        required_any=("相关文件", "项目结构", "读取项目", "read", "files", "路径"),
        advice="Ask the agent to list the files, routes, APIs, services, data models, and config it actually inspected.",
    ),
    Rule(
        id="acceptance-criteria",
        title="Missing acceptance criteria",
        severity="high",
        category="preflight",
        required_any=("验收", "acceptance", "用例", "预期结果", "definition of done"),
        advice="Require explicit acceptance cases before implementation continues.",
    ),
    Rule(
        id="verification-evidence",
        title="Missing verification evidence",
        severity="critical",
        category="delivery",
        required_any=("验证命令", "测试命令", "pytest", "npm test", "curl", "screenshot", "验证结果"),
        advice="Reject the delivery until commands, outputs, screenshots, API responses, or data evidence are provided.",
    ),
    Rule(
        id="real-data-flow",
        title="Real data flow not demonstrated",
        severity="critical",
        category="delivery",
        required_any=("API", "数据库", "data", "保存", "读取", "刷新", "持久化", "service"),
        advice="Require proof that the UI calls a real API and the backend reads/writes a real data source.",
    ),
    Rule(
        id="handoff-quality",
        title="Handoff is not recoverable",
        severity="medium",
        category="handoff",
        required_any=("已完成", "未完成", "关键路径", "端口", "命令", "风险", "下一步"),
        advice="Make the agent rewrite handoff with paths, ports, commands, verified state, risks, do-not-touch items, and next step.",
    ),
    Rule(
        id="rollback",
        title="No backup or rollback plan",
        severity="high",
        category="safety",
        required_any=("备份", "回滚", "rollback", "backup", "恢复"),
        advice="Require a rollback path before database, config, permission, model, or destructive changes.",
    ),
    Rule(
        id="scope-boundary",
        title="Scope boundary not declared",
        severity="medium",
        category="safety",
        required_any=("影响范围", "不会改动", "不包含", "scope", "风险"),
        advice="Require a list of files/modules that are in scope and explicitly out of scope.",
    ),
    Rule(
        id="mock-risk",
        title="Possible mock or fake implementation",
        severity="critical",
        category="delivery",
        suspicious_any=("mock", "placeholder", "TODO", "演示", "示例数据", "假数据", "stub"),
        advice="Require replacement with real API/data flow, or explicit user approval for a prototype.",
    ),
    Rule(
        id="phase-risk",
        title="Possible unauthorized phasing",
        severity="high",
        category="delivery",
        suspicious_any=("第一期", "后续", "下一步再", "MVP", "later", "future work", "后面可以"),
        advice="Ask whether the user explicitly approved phasing. If not, require complete delivery or a scope confirmation.",
    ),
    Rule(
        id="confidence-risk",
        title="Overconfident language without evidence",
        severity="medium",
        category="communication",
        suspicious_any=("应该可以", "理论上", "基本完成", "大概", "看起来", "应该没问题"),
        advice="Replace vague confidence with concrete evidence and unresolved risk.",
    ),
)


SEVERITY_WEIGHT = {
    "critical": 30,
    "high": 20,
    "medium": 10,
    "low": 5,
}


def contains_any(text: str, needles: Iterable[str]) -> bool:
    folded = text.casefold()
    return any(needle.casefold() in folded for needle in needles)
