"""Compliance Agent.

Reviews a legal document against a configurable set of regulatory
frameworks (GDPR, HIPAA, SOC 2, etc.) and produces a structured
findings report.
"""

from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class ComplianceFinding:
    framework: str
    clause: str
    severity: str
    excerpt: str
    recommendation: str


@dataclass
class ComplianceAgent:
    frameworks: tuple = ("GDPR", "HIPAA", "SOC2")
    findings: list = field(default_factory=list)

    def analyze(self, document: str) -> list[ComplianceFinding]:
        """Run a heuristic pass over the document and emit findings."""
        results: list[ComplianceFinding] = []
        for fw in self.frameworks:
            for clause, severity in self._scan(document, fw):
                results.append(
                    ComplianceFinding(
                        framework=fw,
                        clause=clause,
                        severity=severity,
                        excerpt=self._excerpt(document, clause),
                        recommendation=self._recommend(fw, clause),
                    )
                )
        self.findings = results
        return results

    def _scan(self, doc: str, framework: str) -> Iterable[tuple[str, str]]:
        keywords = {
            "GDPR": [("data subject", "high"), ("processor", "medium")],
            "HIPAA": [("PHI", "high"), ("BAA", "medium")],
            "SOC2": [("audit log", "medium"), ("access control", "high")],
        }
        for kw, sev in keywords.get(framework, []):
            if kw.lower() in doc.lower():
                yield kw, sev

    def _excerpt(self, doc: str, clause: str, span: int = 80) -> str:
        idx = doc.lower().find(clause.lower())
        if idx < 0:
            return ""
        start = max(0, idx - span)
        end = min(len(doc), idx + len(clause) + span)
        return doc[start:end].strip()

    def _recommend(self, framework: str, clause: str) -> str:
        return f"Review '{clause}' for alignment with {framework} obligations."
