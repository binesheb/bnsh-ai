# Control Center API Contract

Initial endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | /api/health | Control API health |
| GET | /api/system | CPU/RAM/GPU/runtime summary |
| GET | /api/models | Published model catalog |
| GET | /api/models/:id | Model metadata |
| GET | /api/models/:id/status | Local installation status |
| POST | /api/models/:id/install | Start installation |
| DELETE | /api/models/:id | Remove installed model |
| GET | /api/activity | Recent activity |

Future endpoints:

- /api/chat
- /api/runtime
- /api/training
- /api/evaluation
- /api/evolution
- /api/knowledge
- /api/teachers
- /api/learning
- /api/settings

All mutating operations must return an operation identifier so the UI can display progress and errors.
