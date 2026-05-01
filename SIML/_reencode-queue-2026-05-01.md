# SIML re-encode queue — 2026-05-01

16 stragglers from prefix-migrate.py that have content but no `elemental_signature.dominant`. Re-encode each through simlab so the signature gets populated, then re-run `prefix-migrate.py --apply` to fold them into the elemental taxonomy.

## How to process

Each entry below has a copy-pasteable `encode.sh` invocation that uses the existing `insight.md` content as the source. The encoder will write a fresh term dir under whatever prefix matches the new dominant; you then `git rm` the old straggler dir.

Tip: if the May 1 orchestrator PR has merged, you can pass `--series auto` and the prefix is picked from the dominant. Until then, eyeball the term name and pick a series letter (`A`/`B`/`E`/`F`/`M`/`W`/`X`/`Z`) — wrong guesses get auto-corrected on the next migration run.

## Queue

### Z001_Consider_Meta_Posture
- **insight.md**: 8,033 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/Z001_Consider_Meta_Posture/insight.md \
    --name-hint "Consider_Meta_Posture" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/Z001_Consider_Meta_Posture
  ```

### C207_Ineffable_Intelligence
- **insight.md**: 7,841 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C207_Ineffable_Intelligence/insight.md \
    --name-hint "Ineffable_Intelligence" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C207_Ineffable_Intelligence
  ```

### E023_Bioregional_Pilgrimage
- **insight.md**: 8,954 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/E023_Bioregional_Pilgrimage/insight.md \
    --name-hint "Bioregional_Pilgrimage" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/E023_Bioregional_Pilgrimage
  ```

### C189_Symbiogenesis
- **insight.md**: 9,852 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C189_Symbiogenesis/insight.md \
    --name-hint "Symbiogenesis" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C189_Symbiogenesis
  ```

### C190_Holobiont
- **insight.md**: 8,288 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C190_Holobiont/insight.md \
    --name-hint "Holobiont" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C190_Holobiont
  ```

### C191_Bur_Oak_Blight
- **insight.md**: 7,644 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C191_Bur_Oak_Blight/insight.md \
    --name-hint "Bur_Oak_Blight" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C191_Bur_Oak_Blight
  ```

### C192_Intercultural_Communication_Principles
- **insight.md**: 6,724 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C192_Intercultural_Communication_Principles/insight.md \
    --name-hint "Intercultural_Communication_Principles" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C192_Intercultural_Communication_Principles
  ```

### C193_Second_Probe_Referral
- **insight.md**: 6,159 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C193_Second_Probe_Referral/insight.md \
    --name-hint "Second_Probe_Referral" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C193_Second_Probe_Referral
  ```

### C194_Compost_Time
- **insight.md**: 8,514 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C194_Compost_Time/insight.md \
    --name-hint "Compost_Time" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C194_Compost_Time
  ```

### C195_LIFO_Delayering
- **insight.md**: 7,333 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C195_LIFO_Delayering/insight.md \
    --name-hint "LIFO_Delayering" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C195_LIFO_Delayering
  ```

### C196_Yin_Yang
- **insight.md**: 4,525 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C196_Yin_Yang/insight.md \
    --name-hint "Yin_Yang" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C196_Yin_Yang
  ```

### C199_River_Mouth
- **insight.md**: 8,701 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C199_River_Mouth/insight.md \
    --name-hint "River_Mouth" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C199_River_Mouth
  ```

### C200_Food_Waste_Under_Capitalism
- **insight.md**: 12,087 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C200_Food_Waste_Under_Capitalism/insight.md \
    --name-hint "Food_Waste_Under_Capitalism" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C200_Food_Waste_Under_Capitalism
  ```

### C205_odot_consider
- **insight.md**: 7,178 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C205_odot_consider/insight.md \
    --name-hint "odot_consider" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C205_odot_consider
  ```

### C207_Reinforcement_Learning_Superlearners
- **insight.md**: 10,693 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/C207_Reinforcement_Learning_Superlearners/insight.md \
    --name-hint "Reinforcement_Learning_Superlearners" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/C207_Reinforcement_Learning_Superlearners
  ```

### Z002_LOOM
- **insight.md**: 5,611 bytes
- **Re-encode** (paste into terminal):
  ```bash
  bash ~/Projects/nema_harness/skills/simlab/encode.sh \
    --source-file ~/repos/nema-swarm/SIML/terms/Z002_LOOM/insight.md \
    --name-hint "LOOM" \
    --series auto
  # then, if the new term landed cleanly:
  git -C ~/repos/nema-swarm rm -r SIML/terms/Z002_LOOM
  ```
