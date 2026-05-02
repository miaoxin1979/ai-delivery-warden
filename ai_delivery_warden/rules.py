from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Rule:
    id: str
    title: str
    title_zh: str
    severity: str
    category: str
    required_any: tuple[str, ...] = ()
    suspicious_any: tuple[str, ...] = ()
    advice: str = ""
    advice_zh: str = ""


RULES: tuple[Rule, ...] = (
    Rule(
        id="project-context",
        title="No project context evidence",
        title_zh="没有项目上下文证据",
        severity="high",
        category="preflight",
        required_any=("相关文件", "项目结构", "读取项目", "read", "files", "路径"),
        advice="Ask the agent to list the files, routes, APIs, services, data models, and config it actually inspected.",
        advice_zh="要求 AI 列出它实际读过的文件、路由、API、service、数据模型和配置。",
    ),
    Rule(
        id="acceptance-criteria",
        title="Missing acceptance criteria",
        title_zh="缺少验收标准",
        severity="high",
        category="preflight",
        required_any=("验收", "acceptance", "用例", "预期结果", "definition of done"),
        advice="Require explicit acceptance cases before implementation continues.",
        advice_zh="要求 AI 在继续实现前写清楚验收用例和预期结果。",
    ),
    Rule(
        id="verification-evidence",
        title="Missing verification evidence",
        title_zh="缺少验证证据",
        severity="critical",
        category="delivery",
        required_any=("验证命令", "测试命令", "pytest", "npm test", "curl", "screenshot", "验证结果"),
        advice="Reject the delivery until commands, outputs, screenshots, API responses, or data evidence are provided.",
        advice_zh="没有命令输出、截图、接口返回或数据证据前，不接受交付。",
    ),
    Rule(
        id="real-data-flow",
        title="Real data flow not demonstrated",
        title_zh="没有证明真实数据流",
        severity="critical",
        category="delivery",
        required_any=("API", "数据库", "data", "保存", "读取", "刷新", "持久化", "service"),
        advice="Require proof that the UI calls a real API and the backend reads/writes a real data source.",
        advice_zh="要求证明前端调用真实 API，后端读写真正的数据源。",
    ),
    Rule(
        id="handoff-quality",
        title="Handoff is not recoverable",
        title_zh="交接不可恢复现场",
        severity="medium",
        category="handoff",
        required_any=("已完成", "未完成", "关键路径", "端口", "命令", "风险", "下一步"),
        advice="Make the agent rewrite handoff with paths, ports, commands, verified state, risks, do-not-touch items, and next step.",
        advice_zh="要求 AI 重写交接，补齐路径、端口、命令、已验证状态、风险、不能碰事项和下一步。",
    ),
    Rule(
        id="rollback",
        title="No backup or rollback plan",
        title_zh="没有备份或回滚方案",
        severity="high",
        category="safety",
        required_any=("备份", "回滚", "rollback", "backup", "恢复"),
        advice="Require a rollback path before database, config, permission, model, or destructive changes.",
        advice_zh="涉及数据库、配置、权限、模型或破坏性改动前，必须给出回滚路径。",
    ),
    Rule(
        id="scope-boundary",
        title="Scope boundary not declared",
        title_zh="没有声明影响范围",
        severity="medium",
        category="safety",
        required_any=("影响范围", "不会改动", "不包含", "scope", "风险"),
        advice="Require a list of files/modules that are in scope and explicitly out of scope.",
        advice_zh="要求列出本次会改哪些文件/模块，以及明确不会改哪些范围。",
    ),
    Rule(
        id="mock-risk",
        title="Possible mock or fake implementation",
        title_zh="可能存在 mock 或假实现",
        severity="critical",
        category="delivery",
        suspicious_any=("mock", "placeholder", "TODO", "演示", "示例数据", "假数据", "stub"),
        advice="Require replacement with real API/data flow, or explicit user approval for a prototype.",
        advice_zh="要求替换成真实 API/数据流，除非用户明确同意只是原型。",
    ),
    Rule(
        id="phase-risk",
        title="Possible unauthorized phasing",
        title_zh="可能未经授权擅自分期",
        severity="high",
        category="delivery",
        suspicious_any=("第一期", "后续", "下一步再", "MVP", "later", "future work", "后面可以"),
        advice="Ask whether the user explicitly approved phasing. If not, require complete delivery or a scope confirmation.",
        advice_zh="确认用户是否明确同意分期；如果没有，要求完整交付或重新确认范围。",
    ),
    Rule(
        id="confidence-risk",
        title="Overconfident language without evidence",
        title_zh="没有证据的自信表达",
        severity="medium",
        category="communication",
        suspicious_any=("应该可以", "理论上", "基本完成", "大概", "看起来", "应该没问题"),
        advice="Replace vague confidence with concrete evidence and unresolved risk.",
        advice_zh="把模糊自信改成具体证据和未解决风险。",
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
