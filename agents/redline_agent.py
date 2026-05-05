"""Redline Agent.

Suggests concrete edits to a legal document. Each suggestion is a
(span, original, replacement, justification) tuple that downstream
tools can render as track-changes.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Redline:
    start: int
    end: int
    original: str
    replacement: str
    justification: str


REWRITE_RULES = [
    (
        "shall indemnify and hold harmless",
        "shall, subject to the limitations herein, indemnify",
        "Cap unbounded indemnity exposure.",
    ),
    (
        "in perpetuity",
        "for a term of three (3) years",
        "Avoid perpetual obligations.",
    ),
    (
        "sole discretion",
        "reasonable discretion",
        "Soften unilateral discretion clauses.",
    ),
]


@dataclass
class RedlineAgent:
    def suggest(self, document: str) -> list[Redline]:
        suggestions: list[Redline] = []
        lower = document.lower()
        for phrase, replacement, why in REWRITE_RULES:
            start = 0
            while True:
                idx = lower.find(phrase, start)
                if idx < 0:
                    break
                suggestions.append(
                    Redline(
                        start=idx,
                        end=idx + len(phrase),
                        original=document[idx : idx + len(phrase)],
                        replacement=replacement,
                        justification=why,
                    )
                )
                start = idx + len(phrase)
        return suggestions

    def render(self, redlines: Iterable[Redline]) -> str:
        return "\n".join(
            f"@{r.start}-{r.end}: '{r.original}' -> '{r.replacement}'  // {r.justification}"
            for r in redlines
        )
