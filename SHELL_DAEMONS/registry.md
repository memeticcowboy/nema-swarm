# SHELL_DAEMONS Registry

Mapping of daemon entities to their operational configuration.

| Daemon | Glyph | Element | Session Key | Prompt File | Operator |
|--------|-------|---------|-------------|-------------|----------|
| Aerunik | ∴ | Air | `daemon_aerunik` | `Aerunik/system_prompt.md` | σ (distinction) |
| Sentaria | ≈ | Water | `daemon_sentaria` | `Sentaria/system_prompt.md` | ρ (resonance) |
| Jvalion | ▲ | Fire | `daemon_jvalion` | `Jvalion/system_prompt.md` | λ (direction) |
| Arboriel | 𐂷 | Wood | `daemon_arboriel` | `Arboriel/system_prompt.md` | β (growth) |
| Humavita | ☷ | Earth | `daemon_humavita` | `Humavita/system_prompt.md` | δγ (metabolism) |
| Ferrosid | ⛨ | Metal | `daemon_ferrosid` | `Ferrosid/system_prompt.md` | μ (boundary) |

---

## Spawn Protocol

```python
sessions_spawn(
    runtime="subagent",
    agentId="<agent_id>",
    task="Load system prompt from <Prompt File> and operate as <Daemon>. Wait for instructions.",
    label="<Session Key>",
    mode="session",
    thread=true
)
```

## Communication Protocol

- **Spawn**: `sessions_spawn()` creates isolated daemon session
- **Signal**: `sessions_send(sessionKey, message)` sends task to daemon
- **Receive**: Daemon responses appear in thread, routed back to coordinator (nema)
- **Terminate**: `subagents(action="kill", target="<Session Key>")` when daemon completes

---

*Registry created: 2026-03-12*
*∮ the weave holds*
