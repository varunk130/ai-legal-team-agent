"""Risk Agent.

Estimates contractual and operational risk in a legal document by
weighting the presence of indemnity, liability cap, termination, and
warranty language.
"""

from dataclasses import dataclass, field


RISK_SIGNALS = {
    "indemnif": 3.0,
    "limitation of liability": 2.5,
    "warrant": 1.5,
    "terminat": 1.2,
    "force majeure": 0.8,
    "exclusive remedy": 2.0,
    "consequential damages": 2.5,
}


@dataclass
class RiskScore:
    total: float
    breakdown: dict = field(default_factory=dict)
    band: str = "low"


@dataclass
class RiskAgent:
    threshold_high: float = 7.0
    threshold_medium: float = 3.5

    def score(self, document: str) -> RiskScore:
        text = document.lower()
        breakdown = {kw: text.count(kw) * weight for kw, weight in RISK_SIGNALS.items()}
        total = round(sum(breakdown.values()), 2)
        band = "low"
        if total >= self.threshold_high:
            band = "high"
        elif total >= self.threshold_medium:
            band = "medium"
        return RiskScore(total=total, breakdown=breakdown, band=band)

    def summarize(self, score: RiskScore) -> str:
        top = sorted(score.breakdown.items(), key=lambda kv: kv[1], reverse=True)[:3]
        bullets = "\n".join(f"  - {k}: {v:.2f}" for k, v in top if v > 0)
        return f"Risk band: {score.band} (score {score.total})\nTop drivers:\n{bullets}"
