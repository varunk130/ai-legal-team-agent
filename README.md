# ⚖️ AI Legal Team Agent

A multi-agent A I system for legal document analysis — four  specialized agents collaborate in parallel t o deliver comprehensive compliance assessment s, risk identification, strategic recommendat ions, and redline suggestions.

![AI Legal Te am Agent Dashboard](screenshots/ai-legal-agen t-team-dashboard.png)

<p align="center">
  < img src="screenshots/analysis-complete.png" w idth="48%" alt="Analysis Results" />
  <img s rc="screenshots/agent-recommendations.png" wi dth="48%" alt="Recommendations" />
</p>
<p al ign="center">
  <img src="screenshots/agent-o verview.png" width="48%" alt="Overview Dashbo ard" />
</p>

> **⚠️ Disclaimer:** This a pplication is a technical demonstration only  and does not constitute legal advice and is n ot a substitute for qualified counsel. All sa mple contracts and analysis outputs are synth etic. Do not rely on the output of this syste m for legal decision-making.

---

## Overvie w

AI Legal Team Agent simulates a virtual le gal team where specialized AI agents work tog ether to analyze contracts, NDAs, lease agree ments, and other legal documents. Upload a do cument, select an analysis type, and receive  comprehensive findings across multiple dimens ions.

The project ships with **two independe nt versions**:

| Version | Stack | Entry Poi nt |
|---------|-------|-------------|
| **Py thon / Streamlit** | Streamlit, PyPDF2, pytho n-docx, pandas | `app.py` |
| **Node.js / Exp ress** | Express, React 18 (CDN), Tailwind CS S, Multer | `server.js` + `public/index.html`  |

Both versions offer the same core analysi s workflow. Currently runs with mock AI respo nses; the path from mock to a real Claude API  integration is documented in [`docs/REAL_API _MODE.md`](docs/REAL_API_MODE.md), with per-a gent system prompts decoupled into [`prompts/ `](prompts/) and a single `analyze()` seam pe r backend ready to wire up. **No external API  calls are wired in this codebase today** —  the scaffolding is opt-in for self-hosted de ployments only.

---

## Features

### Multi- Agent Collaboration

Four specialized agents  collaborate on every analysis, each owning a  distinct perspective:

- **Team Lead** — Co ordinates analysis, synthesizes findings, del ivers the final report
- **Contract Analyst**  — Deep-dives into contract terms, clause s tructure, obligations
- **Legal Researcher**  — Identifies relevant case law, statutory r eferences, regulatory frameworks
- **Legal St rategist** — Assesses risk exposure, develo ps strategic recommendations

→ Each agent  is also available as a standalone **[Claude C ode Skill](skills/)**.

### Analysis Types

-  **Compliance Check** — Evaluate adherence  to GDPR, CCPA, employment law
- **Contract Re view** — Detailed term-by-term analysis inc luding payment and IP provisions
- **Legal Re search** — Surface relevant case law, prece dents, and statutory references
- **Risk Asse ssment** — Risk profiling with severity rat ings and mitigation strategies
- **Custom Que ry** — Ask any specific legal question abou t the document

### Result Tabs

- **Analysis ** — Full agent-generated narrative with pa ge references
- **Key Points** — Critical t erms extracted and categorized by importance
 - **Recommendations** — Prioritized action  items with legal basis
- **Redline** — Prop osed changes with before/after text and visua l diff
- **Overview** — Document metrics, r isk assessment summary, and charts

### Docum ent Support

Upload and analyze **PDF**, **TX T**, and **DOCX** files. Sample contracts (ND A, SaaS agreement) included for testing.

--- 

## Quick Start

### Get Started with Skills 

The Claude Code skills and sample contracts  are ready for immediate use. The full Stream lit application and Node.js server are planne d additions.

```bash
# Clone the repo
git cl one https://github.com/varunk130/ai-legal-tea m-agent.git

# Copy skills to your Claude Cod e environment
cp -r ai-legal-team-agent/skill s/* ~/.claude/skills/
```

→ See [docs/QUIC KSTART.md](docs/QUICKSTART.md) for the detail ed setup guide.

---

## Claude Code Skills

 Each agent is available as a standalone Claud e Code skill:

```bash
cp -r skills/* ~/.clau de/skills/
```

| Skill | What It Does |
|--- ----|-------------|
| [legal-team-lead](skill s/legal-team-lead/SKILL.md) | Orchestrates mu lti-agent legal analysis, synthesizes finding s |
| [contract-analyst](skills/contract-anal yst/SKILL.md) | Deep contract review — clau ses, obligations, defined terms |
| [legal-re searcher](skills/legal-researcher/SKILL.md) |  Case law, statutory references, regulatory f rameworks |
| [legal-strategist](skills/legal -strategist/SKILL.md) | Risk assessment, stra tegic recommendations, mitigation plans |

-- -

## Project Structure

```
ai-legal-team-ag ent/
├── README.md
├── LICENSE
� �── requirements.txt
├── samples/
� ��   ├── sample_nda.txt
│   └──  sample_saas_agreement.txt
├── docs/
� �   ├── QUICKSTART.md
│   └── E XECUTIVE_SUMMARY.md
├── skills/
│   � ��── legal-team-lead/SKILL.md
│   ├� �─ contract-analyst/SKILL.md
│   ├─� � legal-researcher/SKILL.md
│   └── l egal-strategist/SKILL.md
└── screenshot s/
```

---

## Tech Stack

| Layer | Technol ogy |
|-------|-----------|
| Frontend (Node)  | React 18 (CDN), Tailwind CSS |
| Backend ( Node) | Node.js, Express, Multer |
| Python v ersion | Streamlit, PyPDF2, python-docx, pand as |
| AI (Planned) | Claude API (Anthropic)  |

---

<p align="center">
  <strong>Built by  Varun Kulkarni</strong><br/>
  <sub>Powered  by Claude Code Opus 4.7 + GitHub Copilot</sub >
</p>
 

## Python Quickstart

This repo also ships a lightweight Python package (`agents/`, `orchestrator.py`, `main.py`) for running the legal-team agents directly from the command line, independent of any UI layer.

Requires **Python 3.10+** (uses `dataclasses`, PEP 604 unions, and PEP 585 generics).

```bash
# Run the orchestrator on a contract
python main.py path/to/contract.txt

# Or get JSON output
python main.py path/to/contract.txt --json
```

The Python package itself has **zero runtime dependencies** beyond the standard library; `requirements.txt` covers the optional UI/demo extras.