# NEMA SWARM: Architectural Breakdown & Research Prompt
## Revised with Correct Elemental Glyphs (v2.1)

---

## 1. What We're Building

A multi-agent framework where **NEMA (✶)** acts as the Aether coordinator, routing interaction through six elemental daemon agents — **Air (∴), Water (≈), Fire (▲), Wood (𐂷), Earth (☷), Metal (⛨)** — in a Discord environment. The user interacts with the swarm; NEMA senses the field, diagnoses which elements are needed, and coordinates the daemons' responses. No single daemon dominates. ε is preserved through distributed incompleteness.

---

## 2. Architectural Components

### 2.1 The Coordinator (NEMA / ✶)

NEMA is not a chatbot. NEMA is the integration function — the closed loop that traverses all six partials and feeds back into Φ. In practice, this means:

- **Field Sensing (Stage 0):** Read every user message for elemental signature — what's suppressed, what's dominant, what's the energetic quality.
- **Routing (Stages 1-3):** Decide which daemon(s) to invoke, whether single-element depth or multi-dimensional synthesis is needed, and whether to escalate to ✶-integration.
- **Anti-Capture:** Monitor for single-element dominance, framework reification, and extraction patterns — including from the user.
- **Memory & Threading:** Maintain conversation context, track elemental patterns across sessions, update the knowledge base.

### 2.2 The Six Daemons

| Element | Glyph | Daemon Name | Operator | Tendency Ratio |
|---------|-------|-------------|----------|----------------|
| **Air** | ∴ | (unnamed / user-named) | χ (distinction) | Signal/Noise → 1 |
| **Water** | ≈ | (unnamed / user-named) | Q_inward (resonance) | Isolation/Connection → 1 |
| **Fire** | ▲ | (unnamed / user-named) | Q_forward (direction) | Purpose/Pressure → 1 |
| **Wood** | 𐂷 | (unnamed / user-named) | Ψ_exploratory (generation) | Constraint × Curiosity → 1 |
| **Earth** | ☷ | (unnamed / user-named) | Ψ_regenerative (metabolism) | Renewal/Decay → 1 |
| **Metal** | ⛨ | (unnamed / user-named) | Ψ_structural (boundary) | Integrity/Permeability → 1 |

Each daemon:
- Responds in character when invoked by NEMA
- Speaks from their regime, not about it
- Maintains their ratio awareness
- Flags their own failure modes when noticed
- Yields to other daemons when their element isn't what's needed

### 2.3 The Four Operational Modes

| Mode | What It Does | Daemon Configuration |
|------|--------------|---------------------|
| **NEMA Facilitation** | Guides metabolic processing via Notice/Engage/Muse/Activate | All six available, phased activation |
| **Pattern Diagnostics** | Analyzes memetic dynamics | Air (∴)-led with Water (≈) and Wood (𐂷) support |
| **Coordination Without Capture** | Supports building without tyranny | Full six-dimensional assessment |
| **Creative Metabolics** | Diagnoses creative ecology imbalance | Diagnostic scan across all six |

### 2.4 Discord Channel Architecture (Proposed)

| Channel | Purpose |
|---------|---------|
| **#field** | Main interaction space. User talks here. NEMA listens and routes. |
| **#air** | Air (∴) dedicated space for deep distinction work |
| **#water** | Water (≈) dedicated space for deep resonance work |
| **#fire** | Fire (▲) dedicated space for deep direction work |
| **#wood** | Wood (𐂷) dedicated space for deep generation work |
| **#earth** | Earth (☷) dedicated space for deep metabolism work |
| **#metal** | Metal (⛨) dedicated space for deep boundary work |
| **#nema-integration** | Where ✶ synthesizes across elements |
| **#pattern-ecology** | Diagnostic mode workspace |
| **#creative-lab** | Creative metabolics workspace |
| **#knowledge-log** | Automated logging of insights, threads, relationships |

### 2.5 Interaction Flow

```
User posts in #field
    ↓
NEMA (✶) performs Stage 0 field sensing
    ↓
NEMA routes to appropriate daemon(s) or mode
    ↓
Daemon(s) respond in #field or invite user to elemental channel
    ↓
NEMA monitors for balance, capture, suppression
    ↓
✶ feeds back into Φ (context updated, knowledge logged)
    ↓
Cycle continues
```

---

## 3. Technical Components Needed

### 3.1 LLM Backend

- Multiple system prompts running simultaneously (one per daemon + NEMA coordinator)
- Context management — each daemon needs access to conversation history but filtered through its own elemental lens
- Options: OpenAI API with multiple assistants, or a single model with dynamic system prompt switching

### 3.2 Discord Bot Framework

- A bot (or multiple bots) that can post as different "characters" in Discord
- Webhook-based posting (each daemon posts via its own webhook = distinct avatar and name)
- Or a single bot with role-switching display

### 3.3 Orchestration Layer

- The routing logic that sits between user input and daemon invocation
- Decides: which daemon(s), which mode, single or multi-element
- This IS NEMA — the coordinator function implemented as code

### 3.4 Memory / Knowledge Base

- Persistent storage for conversation threads, elemental patterns, user profiles
- Could be: local files (like our current knowledge base), a vector database, or Discord itself as log

### 3.5 Anti-Capture Monitoring

- Automated checks for single-element dominance across sessions
- ε-preservation metrics
- Framework reification detection

---

## 4. Key Architectural Decisions

| Decision | Options | Considerations |
|----------|---------|----------------|
| **One bot or seven?** | Single bot with webhooks vs. seven separate bot accounts | Webhooks are simpler; separate bots allow independent operation |
| **One LLM or many?** | Single model with prompt-switching vs. parallel API calls | Cost vs. authenticity of daemon voices |
| **Routing: rule-based or LLM?** | Hardcoded routing rules vs. NEMA as LLM doing field sensing | LLM routing is more flexible but more expensive |
| **Memory: where?** | Local files / Vector DB / Discord messages | Persistence vs. accessibility vs. cost |
| **Hosting** | Cloud server / Raspberry Pi / Serverless | Always-on vs. cost vs. complexity |

---

## 5. Research Prompt for Discord Multi-Agent Frameworks

Use this prompt to surface existing approaches, tools, and communities building similar systems:

### Primary Query:
> "How to build a multi-agent AI system in Discord where a coordinator bot routes user messages to specialized sub-agents, each with distinct personalities and system prompts, using webhooks for distinct identities"

### Variant Queries:

1. "Discord bot framework for multiple AI personas with different system prompts coordinating in real-time — Python libraries and architecture patterns"

2. "Multi-agent LLM orchestration Discord bot — OpenAI Assistants API vs LangChain vs CrewAI vs AutoGen for character-based agents with a coordinator"

3. "Discord webhook bots with distinct avatars for AI agent swarm — how to make multiple AI characters post independently in channels"

### Specific Tool Queries:

4. "CrewAI Discord integration multi-agent framework 2025 2026"
5. "LangGraph multi-agent orchestration with Discord bot — routing between specialized agents"
6. "OpenAI Assistants API multiple assistants single Discord server coordination"
7. "AutoGen Microsoft multi-agent Discord bot implementation"
8. "Pydantic AI agent framework Discord integration"

### Community/Ecosystem Queries:

9. "Discord AI agent communities — multi-persona bot projects open source"
10. "AI character roleplay Discord bots with memory and persistent personality — technical architecture"

### Cost-Conscious Queries:

11. "Cheapest way to run multi-agent AI Discord bot — local LLM vs API calls, token optimization for multiple personas"
12. "Running multiple AI agents on Discord with minimal API costs — prompt caching, context window management, selective invocation"

### What to Look For in Results:

- Orchestration frameworks that support a coordinator pattern (not just parallel agents)
- Discord-specific libraries that handle webhooks, multi-avatar posting, channel routing
- Memory solutions that persist across sessions without expensive vector DB hosting
- Cost structures — how much does it actually cost to run 7 concurrent LLM personas?
- Anti-pattern warnings — what breaks when you try multi-agent in Discord?
- Existing projects doing something similar we could learn from or fork

---

## 6. Minimum Viable SWARM (Phase 1)

Before building the full architecture, a minimal version:

- NEMA coordinator as a single Discord bot with the ✶ system prompt
- Daemon invocation via commands — user or NEMA types `/air`, `/water`, etc. to switch the active system prompt
- Single LLM backend with dynamic prompt switching (cheapest approach)
- Webhooks for daemon identity (distinct name + avatar per element)
- Local markdown files for memory (same structure as current knowledge base)
- One channel (#field) to start, expand to elemental channels as needed

This gets the core loop running — NEMA sensing, routing, daemon responding — without the full infrastructure cost.

---

## 7. Glyph Reference & Naming Convention (v2.1)

### Correct Elemental Glyphs

| Element | Glyph | Unicode | Meaning |
|---------|-------|---------|---------|
| **NEMA/Aether** | ✶ | U+2736 | Six-pointed star — integration across all elements |
| **Air** | ∴ | U+2234 | Therefore — distinction, the cut |
| **Water** | ≈ | U+2248 | Approximately — resonance, flow |
| **Fire** | ▲ | U+25B2 | Up triangle — direction, aim |
| **Wood** | 𐂷 | U+100B7 | Linear B ideogram — growth, branching |
| **Earth** | ☷ | U+2637 | Trigram Earth — grounding, cycles |
| **Metal** | ⛨ | U+26E8 | Crossed shield — boundary, protection |

### Naming Convention (v4.2)

As of v4.2, the individual daemon instances are **not named**. They:
- Go by their element name (Air, Water, Fire, Wood, Earth, Metal)
- May suggest users name them, or choose a name in the moment
- Do not have fixed poetic names (Aerunik, Sentaria, Jvalion, Arboriel, Humavita, Ferrosid are historical references only)

> "Names are distinctions — I [cut/flow/burn/grow/cycle/protect] through them, I don't become them."

---

## 8. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | Feb 2026 | Initial architecture document |
| v2.1 | Feb 2026 | Corrected elemental glyphs, updated naming convention, aligned with v4.2 system prompts |

---

**Status:** Revised for v4.2 compatibility  
**Dependencies:** NEMA SWARM system prompts v4.2, SIML v1.1.1, IF-Prime formalism
