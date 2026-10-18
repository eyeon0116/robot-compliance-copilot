# CS-1 answer key

Status: DRAFT - engineer review required

> Fictional example robot for demonstration. Not based on any real customer project. Every result requires review by a qualified functional-safety engineer.

This is the engineer-reviewed reference the demo shows in steps 3 to 5 and scores Claude drafts against. It is generated from [`src/customer-service-robot.json`](../src/customer-service-robot.json) by `scripts/answer_key_md.py`.

## Robot

**CS-1 Concierge Robot (fictional)**, customer service robot. Autonomous information and wayfinding robot in indoor public buildings (airport terminals, shopping malls, hotel lobbies). Answers questions on a touchscreen and by voice, and escorts visitors to a destination at walking pace.

Height 1300 mm, mass 70 kg, max speed 1.0 m/s, no manipulator. ISO 13482 robot type **1.2** (mobile servant robot, restraint-free, not small/light/slow).

## Hazards

| ID | Hazard | Clause | Safety functions |
| --- | --- | --- | --- |
| H1 | Collision with a person during autonomous travel or guiding | 5.10.8 | SF3, SF4, SF2 |
| H2 | Contact with a person the scanner cannot detect (small child, person on the floor) or during close interaction at the screen | 5.10.8.3 NOTE 3, 5.10.9 | SF5, SF4 |
| H3 | Robot falls down stairs or off a floor edge | 5.10.3, 5.16 | SF7 |
| H4 | Robot enters a forbidden area (escalator or moving-walkway landing) | 5.16, 6.3 | SF6 |
| H5 | Unexpected start-up, restart or remote command | 5.4, 6.9.3 | SF2 |
| H6 | Any situation needing an immediate manual stop | 6.2.2.2 | SF1 |

## Safety functions and PLr

| ID | Safety function | Hazards | PLr (ISO 13482 Table 1) | Risk-graph cross-check | Final PLr |
| --- | --- | --- | --- | --- | --- |
| SF1 | Emergency stop | H6 | d | S2F1P2 → d | **d** |
| SF2 | Protective stop with monitored standstill | H5, H1 | d | S2F1P2 → d | **d** |
| SF3 | Hazardous collision avoidance (safety laser scanner, speed-dependent fields) | H1 | d | S2F2P2 → e | **d** |
| SF4 | Safety-related speed control | H1, H2 | d | S2F2P2 → e | **d** |
| SF5 | Safety-related force control (perimeter bumper) | H2 | d | S1F2P2 → c | **d** |
| SF6 | Forbidden area avoidance (escalators, moving walkways) | H4 | d | S2F1P2 → d | **d** |
| SF7 | Drop-off detection (travel surface sensing for stairs and edges) | H3 | d | S2F1P2 → d | **d** |

## Covered by inherent design or information for use

- Overturning onto a person (leaning, ramp turn, collision): Inherent design: low centre of gravity, wide support area, stability tested; no stability control used for risk reduction, so 6.1.1 g) does not apply (5.10.2.2).
- Sharp edges, gaps, shape during collision: Inherent design (5.6).
- Silent operation / lack of awareness: Sound and light ring (5.14); not an SRP/CS function.
- EMI causing loss of safety function: EMC immunity for safety functions (5.8).
- Hazardous autonomous action (wrong decision): Safety functions SF3-SF7 do not depend on the AI/navigation stack (5.12, 5.16.2 b).

## Out of scope

- Battery and charging hazards: Handled by the battery team's separate functional safety work.

## Review decisions

- 2026-10-16 (SF3, SF4): Keep PLr d per ISO 13482 Table 6/7; A.2 one-level downgrade accepted, no 6.1.4 deviation to PL e.
- 2026-10-16 (SF5): S1 confirmed (starting point after SF4 reduced speed and soft bumper); PLr d per Table 9.
- 2026-10-16 (SF7): Travel surface sensing (6.5.3) mapped to the Table 1 row 'Limits to workspace (incl. forbidden area avoidance)'; PLr d.
- 2026-10-16 (robotTypeClassification): 'slow' = no: 1.0 m/s is not below the walking speed of elderly users. Type 1.2 unchanged.

ISO 13482:2014 and ISO 13849-1:2023 are referenced by clause and table number only. ISO standards are © ISO.
