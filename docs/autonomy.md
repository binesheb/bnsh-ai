# ARIV Autonomy Levels

ARIV's continuous-learning system uses explicit autonomy levels.

| Level | Capability | Production weight changes |
|---|---|---|
| 0 | Manual research and training | Manual |
| 1 | Automated data discovery | Manual |
| 2 | Automated dataset construction | Manual |
| 3 | Automated training experiments | Manual |
| 4 | Automated evaluation and candidate generation | Manual approval |
| 5 | Policy-controlled promotion | Only if explicitly enabled |

The default deployment should operate at **Level 2 or below**.

Higher levels require additional safeguards, logging, rollback, and release policy configuration.

## Principle

Autonomy should increase the speed of research, not remove accountability from model releases.
