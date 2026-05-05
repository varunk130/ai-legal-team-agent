"""Strategy Agent.

Translates compliance findings and risk scores into a recommended
negotiation posture and a prioritized list of asks for counsel.
"""

from dataclasses import dataclass
from typing import Sequence

from .compliance_agent import ComplianceFinding
from .risk_agent import RiskScore


@dataclass
class StrategyRecommendation:
    posture: str
    priorities: list[str]
    rationale: str


@dataclass
class StrategyAgent:
    aggressive_band: str = "high"

    def recommend(
        self,
        findings: Sequence[ComplianceFinding],
        risk: RiskScore,
    ) -> StrategyRecommendation:
        posture = self._posture(risk)
        priorities = self._priorities(findings, risk)
        rationale = (
            f"Posture '{posture}' chosen because risk band is "
            f"{risk.band} and {len(findings)} compliance findings were detected."
        )
        return StrategyRecommendation(
            posture=posture,
            priorities=priorities,
            rationale=rationale,
        )

    def _posture(self, risk: RiskScore) -> str:
        if risk.band == self.aggressive_band:
            return "negotiate-hard"
        if risk.band == "medium":
            return "targeted-redlines"
        return "accept-with-clarifications"

    def _priorities(
        self,
        findings: Sequence[ComplianceFinding],
        risk: RiskScore,
    ) -> list[str]:
        ordered = sorted(
            findings,
            key=lambda f: {"high": 0, "medium": 1, "low": 2}.get(f.severity, 3),
        )
        priorities = [f"[{f.severity}] {f.framework}: {f.clause}" for f in ordered[:5]]
        if risk.band == "high":
            priorities.insert(0, "Cap liability and tighten indemnity scope")
        return priorities
