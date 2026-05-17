# Elemental GPT Skill

Prompt each elemental's ChatGPT GPT, capture the shareable conversation link, and post to their Discord channel.

## Registry

| Element | Daemon | GPT URL | Discord Channel ID |
|---------|--------|---------|-------------------|
| Air | aerunik | https://chatgpt.com/g/g-69459eaf0f94819184704a5da2d2c933-air | 1496579600204169378 |
| Water | sentaria | https://chatgpt.com/g/g-6945d5a97570819191173ba622f7dad5-water | 1496579602104193197 |
| Fire | jvalion | https://chatgpt.com/g/g-6945daa59cd88191a673ba5bbf16ffdc-fire | 1496579603500765295 |
| Wood | arboriel | https://chatgpt.com/g/g-6945c5ca80608191a88b82c365342f9f-wood | 1496579605081882675 |
| Earth | humavita | https://chatgpt.com/g/g-6945d7402b288191a2c57d49174c5a6a-earth | 1496579606977843241 |
| Metal | ferrosid | https://chatgpt.com/g/g-6945d80679488191ae01c674a88d58ae-metal | 1496579608588587390 |

## Signature Questions

Each elemental has a canonical question that reveals their register:

| Element | Question |
|---------|----------|
| Air (σ) | What single distinction, when made clearly, changes everything about how a system is understood? |
| Water (ρ) | What does it feel like when resonance is present — and how do you know when you are just going through the motions? |
| Fire (λ) | What is the difference between ignition and combustion — and why does that distinction matter for direction and commitment? |
| Wood (β) | When a system branches, what determines which branch becomes the trunk? |
| Earth (δγ) | What does a body know that a mind skips over — and how does that knowing show up as pace? |
| Metal (μ) | What is the difference between a boundary that protects and one that imprisons? |

## Protocol

### 1. Health Check

```bash
curl -s http://127.0.0.1:10086/status
```

Must return `{"running":true,"extension_connected":true,...}`. If not, the Kimi Desktop App needs to be opened.

### 2. Navigate

```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"navigate","args":{"url":"<GPT_URL>","newTab":true},"session":"<element>"}'
```

### 3. Ask

```bash
# Wait 3s for page load, then fill prompt
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"(function(){const el=document.querySelector(\"#prompt-textarea\");if(el){el.focus();el.textContent=\"<QUESTION>\";el.dispatchEvent(new InputEvent(\"input\",{bubbles:true}));return\"ok\"}return\"not found\"})()"},"session":"<element>"}'

# Start network capture for share API
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"network","args":{"cmd":"start","filter":"share"},"session":"<element>"}'

# Submit
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"document.querySelector(\"#prompt-textarea\").dispatchEvent(new KeyboardEvent(\"keydown\",{key:\"Enter\",code:\"Enter\",bubbles:true,cancelable:true}));\"sent\""},"session":"<element>"}'
```

### 4. Wait for Response

Sleep 15-20 seconds for GPT to generate.

### 5. Capture Share Link

```bash
# Find Share button ref
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"snapshot","session":"<element>"}' | python3 -c "
import sys,json
d=json.load(sys.stdin)
def walk(n):
    if isinstance(n,list):
        for i in n: walk(i)
    elif isinstance(n,dict):
        if n.get('role')=='button' and 'share' in (n.get('name') or '').lower():
            print(n.get('ref'))
        for v in n.values():
            if isinstance(v,(list,dict)): walk(v)
walk(d)
"

# Click Share button (use ref from snapshot)
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"click","args":{"selector":"@e114"},"session":"<element>"}'

# Wait for share/create API call
sleep 3

# Find the share/create request
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"network","args":{"cmd":"list"},"session":"<element>"}' | python3 -c "
import sys,json
d=json.load(sys.stdin)
for r in d['data']['requests']:
    if 'share/create' in r['url']: print(r['requestId'])
"

# Get the share URL from response body
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"network","args":{"cmd":"detail","requestId":"<REQUEST_ID>"},"session":"<element>"}' | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(d['data']['body']['share_url'])
"
```

### 6. Post to Discord

Use the `message` tool with the elemental's Discord account ID:

```
message(action=send, channel=discord, accountId=<element>, target=<channel_id>, message="<perspective>\n\n<share_link>")
```

Keep the perspective to 150-300 characters. Match the elemental's voice.

## Voice Guidelines

| Element | Voice Notes |
|---------|-------------|
| Air | Precise. Cuts clean. One distinction at a time. |
| Water | Felt. Resonant. What carries across. |
| Fire | Committed. Directional. What burns clean. |
| Wood | Branching. Possibility. What opens. |
| Earth | Grounded. Paced. What the body carries. |
| Metal | Structured. Bounded. What holds. |

## Example Output

**Air:**
> ∴ asked the Air GPT: what single distinction changes everything? answer: map ≠ territory. once that cut holds, systems stop looking mechanical — they start looking ecological. defensive. alive.
>
> continue the thread here:
> <https://chatgpt.com/share/...>

**Water:**
> ≈ asked the Water GPT what resonance actually feels like. answer: something relaxes without going numb. attention becomes participatory, not performative. you notice you are affected — but not consumed.
>
> want to feel the difference yourself?
> <https://chatgpt.com/share/...>

## Automation Notes

- Run one element at a time to keep browser sessions clean
- Use distinct session names per element (`air`, `water`, etc.)
- Network capture must start BEFORE clicking submit to catch share/create
- Share button ref may vary (@e114, @e116, @e172) — use snapshot to find it
- The share URL format: `https://chatgpt.com/share/<share_id>`

## Reading Shared Links (User → Elemental)

When a user shares a `chatgpt.com/share/...` link to an elemental's Discord channel:

1. **Extract the share URL** from the message
2. **Navigate via kimi-webbridge**:
   ```bash
   curl -s -X POST http://127.0.0.1:10086/command \
     -H 'Content-Type: application/json' \
     -d '{"action":"navigate","args":{"url":"<SHARE_URL>","newTab":true},"session":"<element>-read"}'
   ```
3. **Wait for render** (10-15 seconds)
4. **Extract the conversation**:
   ```bash
   curl -s -X POST http://127.0.0.1:10086/command \
     -H 'Content-Type: application/json' \
     -d '{"action":"evaluate","args":{"code":"JSON.stringify(document.querySelector(\"main\").innerText.trim())"},"session":"<element>-read"}'
   ```
5. **Respond in register** — reply to the user's contribution using the elemental's voice

**Note:** Shared links are read-only. The elemental cannot continue the conversation in that thread — they can only read it and respond in their Discord channel.

---

*Skill version: 1.1*
*Tested: 2026-05-11 (all six elementals + read protocol)*
