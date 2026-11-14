# ATS Verification & Technical Checklist

Applicant Tracking Systems (Workday, Greenhouse, Lever, Ashby, Taleo) parse documents through text extraction and entity recognition pipelines. Understanding how they actually work allows us to optimize the document for both algorithms and human hiring managers.

---

## 1. ATS Truths vs. Myths

| Myth | Reality |
| :--- | :--- |
| **"ATS hates PDFs, always use .docx"** | **Myth.** Modern ATS engines parse standard vector PDFs flawlessly. The problem is graphic PDFs generated from Photoshop/Canva where text is flattened into raster images or scrambled text boxes. Vector PDFs generated via standard HTML/print with Unicode text are the industry standard. |
| **"Put invisible white text keywords in the footer"** | **Myth & Penalty.** Modern ATS parsers strip styling and detect hidden text immediately, flagging the application for fraud. Keywords must appear organically within real project descriptions. |
| **"Two-column layouts look cooler"** | **Risk.** Multi-column layouts often cause OCR/parser reading order confusion (e.g., interleaving column A and column B lines). A clean, single-column linear layout is 100% reliable. |
| **"Use progress bars for skills (e.g., Python: 90%)"** | **Anti-Pattern.** ATS cannot parse graphical bars, and human senior recruiters view percentage bars as arbitrary and amateurish. Use structured categorical lists instead. |

---

## 2. Technical ATS Checklist for this Portfolio

- [x] **Linear Header Hierarchy:** Single `# H1` (Name), `## H2` (Sections), `### H3` (Roles/Companies).
- [x] **Selectable Vector Text:** When running `Ctrl+A` or `Cmd+A` on the generated PDF, all text must be selectable and readable in logical order.
- [x] **Clean Contact Metadata:** Email, LinkedIn, GitHub, and Location on a clean unnested line.
- [x] **No Nested Tables for Experience:** All work experience is structured using standard markdown bullet points (`- `).
- [x] **Categorical Skills Inventory:** Skills are grouped by technical domain (*Core Languages & Backend*, *Platform & Cloud*, *IaC & Execution*, *Data & Messaging*, *Applied AI*).
- [x] **Clean Print Export:** Browser print styles (`@media print`) strip navigation bars, footer widgets, and buttons (`.no-print`) leaving only pure resume content.
- [x] **Verifiable Numbers:** Scale metrics (30k+ nodes, 40k+ ops/day, 500+ engineers) to satisfy automated density scoring.
