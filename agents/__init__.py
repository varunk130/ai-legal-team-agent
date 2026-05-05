"""Agent registry for the AI Legal Team.

Exposes the four specialist agents that collaborate on legal document
analysis: compliance, risk, strategy, and redline suggestions.
"""

from .compliance_agent import ComplianceAgent
from .risk_agent import RiskAgent
from .strategy_agent import StrategyAgent
from .redline_agent import RedlineAgent

__all__ = [
    "ComplianceAgent",
    "RiskAgent",
    "StrategyAgent",
    "RedlineAgent",
]
