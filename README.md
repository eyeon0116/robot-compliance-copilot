# Robot Compliance Copilot

A first-draft functional-safety tool for engineers at small robot makers. Describe a service robot, and the Copilot drafts the ISO 13482 robot type, a standards map, a hazard list with safety functions and required performance levels (PLr), a traceability map and a gap report.

Every output is a draft for an engineer to review and sign off. The tool does not certify anything and does not replace a conformity assessment.

## Local mode

This public build runs entirely in the browser by rules: nothing you type leaves the page, and no API key is involved. For any robot you describe, the robot type and the standards map are worked out by rules. Hazards, safety functions and PLr are shown for the bundled example, **CS-1 Concierge Robot**, a fictional customer service robot with an engineer-reviewed answer key. Claude drafting for your own robot (form filling, hazard drafts and "Run the test") is an opt-in feature of the claude.ai version of the demo and is hidden here.

## Try it

- Live demo: _link added after deployment_ (GitHub Pages)
- Locally: open `index.html` in a browser.

## How it is built

| Path | What it is |
| --- | --- |
| `index.html` | The whole app (generated, single file, no framework) |
| `claude-shim.js` | Lets the page run outside claude.ai (local mode, file downloads) |
| `src/template.html` | Page source |
| `src/customer-service-robot.json` | Reviewed CS-1 answer key |
| `scripts/build.py` | Builds `index.html` from the two files above |

Rebuild after editing anything in `src/`:

```bash
python3 scripts/build.py
```

## Deploy

The site is static. GitHub Pages serves `index.html` from the `main` branch root (Settings → Pages → Deploy from a branch → `main` / `/ (root)`).

## Standards

The tool uses the robot-type PL values of ISO 13482:2014 Table 1 and the ISO 13849-1:2023 risk graph as lookup data. No standard text is included. ISO standards are © ISO; get the standards themselves from ISO or your national standards body.

## Rights

© 2026 the Robot Compliance Copilot author. All rights reserved. The code is published for hackathon review and is not licensed for reuse.
