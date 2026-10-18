# Renders docs/answer-key.md from src/customer-service-robot.json.
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
d = json.load(open(root/'src'/'customer-service-robot.json', encoding='utf-8'))
r, p = d['robot'], d['robot']['parameters']
cell = lambda s: str(s).replace('|', '/').replace('\n', ' ')
L = ["# CS-1 answer key", "", f"Status: {d['status']}", "", f"> {d['disclaimer']}", '',
     'This is the engineer-reviewed reference the demo shows in steps 3 to 5 and scores Claude drafts against. '
     'It is generated from [`src/customer-service-robot.json`](../src/customer-service-robot.json) by `scripts/answer_key_md.py`.', '',
     '## Robot', '', f"**{r['name']}**, {r['category'].lower()}. {r['intendedUse']}", '',
     f"Height {p['heightMm']} mm, mass {p['massKg']} kg, max speed {p['maxSpeedMs']} m/s, no manipulator. ISO 13482 robot type **1.2** (mobile servant robot, restraint-free, not small/light/slow).", '',
     '## Hazards', '', '| ID | Hazard | Clause | Safety functions |', '| --- | --- | --- | --- |']
L += [f"| {h['id']} | {cell(h['title'])} | {cell(h['clause'])} | {', '.join(h['safetyFunctions']) or '-'} |" for h in d['hazards']]
L += ['', '## Safety functions and PLr', '', '| ID | Safety function | Hazards | PLr (ISO 13482 Table 1) | Risk-graph cross-check | Final PLr |', '| --- | --- | --- | --- | --- | --- |']
for s in d['safetyFunctions']:
    rg = s.get('riskGraphCrossCheck') or {}
    L.append(f"| {s['id']} | {cell(s['name'])} | {', '.join(s['hazards'])} | {s['plrTypeC']['value']} | {rg.get('S','')}{rg.get('F','')}{rg.get('P','')} → {rg.get('result','')} | **{s['plrFinal']}** |")
L += ['', '## Covered by inherent design or information for use', '']
L += [f"- {o['item']}: {o['measure']}" for o in d['otherHazardsCovered']]
L += ['', '## Out of scope', '']
L += [f"- {o['item']}: {o['reason']}" for o in d['outOfScope']]
L += ['', '## Review decisions', '']
L += [f"- {x['date']} ({', '.join(x['items'])}): {x['decision']}" for x in d['reviewLog']]
L += ['', 'ISO 13482:2014 Table 1 values and the ISO 13849-1:2023 risk graph are used as lookup data, and other clauses are cited by number. No standard text is included. ISO standards are © ISO.', '']
(root/'docs'/'answer-key.md').write_text('\n'.join(L), encoding='utf-8')
print('wrote docs/answer-key.md')
