"""Orchestrator for the AI Legal Team.

Coordinates the four specialist agents and assembles a unified report.
"""

from dataclasses import dataclass, field

from agents import (
    ComplianceAgent,
    RedlineAgent,
    RiskAgent,
    StrategyAgent,
)


@dataclass
class LegalReport:
    summary: str
    compliance: list = field(default_factory=list)
    risk: object = None
    strategy: object = None
    redlines: list = field(default_factory=list)


@dataclass
class LegalTeamOrchestrator:
    compliance: ComplianceAgent = field(default_factory=ComplianceAgent)
    risk: RiskAgent = field(default_factory=RiskAgent)
    strategy: StrategyAgent = field(default_factory=StrategyAgent)
    redline: RedlineAgent = field(default_factory=RedlineAgent)

    def run(self, document: str) -> LegalReport:
        findings = self.compliance.analyze(document)
        risk = self.risk.score(document)
        strategy = self.strategy.recommend(findings, risk)
        redlines = self.redline.suggest(document)

        summary = (
            f"Compliance findings: {len(findings)} | "
            f"Risk: {risk.band} ({risk.total}) | "
            f"Strategy: {strategy.posture} | "
            f"Redlines: {len(redlines)}"
        )

        return LegalReport(
            summary=summary,
            compliance=findings,
            risk=risk,
            strategy=strategy,
            redlines=redlines,
        )
