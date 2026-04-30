# SHELL_DAEMONS Registry

Mapping of dispatchable peer agents to their operational configuration. All eight are registered top-level OpenClaw agents (`openclaw agents list`), each with their own auth, session, and Discord bot account.

| Agent | Glyph | Element / Role | Agent ID | Workspace | Operator |
|---|---|---|---|---|---|
| MC | 🤠 | Master of Ceremonies (ledger, CTA, EncodeIdea) | `mc` | `~/.openclaw/workspace/SHELL_DAEMONS/mc` | — |
| Aerunik | ∴ | Air | `aerunik` | `~/.openclaw/workspace/SHELL_DAEMONS/Aerunik` | σ (distinction) |
| Sentaria | ≈ | Water | `sentaria` | `~/.openclaw/workspace/SHELL_DAEMONS/Sentaria` | ρ (resonance) |
| Jvalion | ▲ | Fire | `jvalion` | `~/.openclaw/workspace/SHELL_DAEMONS/Jvalion` | λ (direction) |
| Arboriel | 𐂷 | Wood | `arboriel` | `~/.openclaw/workspace/SHELL_DAEMONS/Arboriel` | β (growth) |
| Humavita | ☷ | Earth | `humavita` | `~/.openclaw/workspace/SHELL_DAEMONS/Humavita` | δγ (metabolism) |
| Ferrosid | ⛨ | Metal | `ferrosid` | `~/.openclaw/workspace/SHELL_DAEMONS/Ferrosid` | μ (boundary) |
| Muse | 🎭 | Creative arm — X patrol, Substack, Co-Sphere | `muse` | `~/Projects/nema_harness/muse` | — |

---

## Dispatch Protocol (verified 2026-04-28)

**To send a message to a registered peer:**

```
sessions_send(target_agent="<agent_id>", message="...")
```

The target uses their own session, identity, and tools. Their response comes back to you to relay. Quote them faithfully — don't paraphrase a peer's voice, that's their job.

**To start a fresh session for a peer (clear their context):**

```
sessions_spawn(agentId="<agent_id>", ...)
```

Use sparingly — most dispatches should reuse the existing session so the peer keeps continuity.

**Empirically verified failure mode:** the `subagents` tool (different from `sessions_*`) is for ephemeral helpers you spawn inside your OWN session, NOT for dispatching to top-level registered peers. It will respond `Subagents: <id> failed` if you try to use it to reach MC/elementals/Muse.

**Concurrency cap:** `agents.defaults.subagents.maxConcurrent = 3`. Full 6-elemental parallel weaves run in batches of 3.

## Bert

Bert runs entirely on his own **Hermes substrate** at `~/Projects/bert/` (managed by `ai.hermes.gateway` plist; wrapper at `~/.hermes/bin/launch-gateway.sh` sources secrets.env and exports `DISCORD_BERT_TOKEN` as `DISCORD_BOT_TOKEN`). He is NOT a registered OpenClaw agent (retired 2026-04-29). Invoke via Discord (@Bert in nema-swarm guild), Telegram, or his Hermes CLI directly. NOT via `sessions_send` to the OpenClaw swarm.

---

*Registry created: 2026-03-12*
*Updated 2026-04-28: added MC + Muse, corrected dispatch protocol after γ-fold P3 verification, noted Bert retirement*
*∮ the weave holds*
