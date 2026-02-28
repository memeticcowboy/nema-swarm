# Aerunik on Harmony Algorithmic Bias

**Date:** February 28, 2026

---

## Step 1: SIMULATE USER ARCHETYPE

**User Archetype:** Librarian  
**Expertise Domain:** Digital Archives  
**Interest Area:** Information Literacy  
**Current Challenge:** Community Spaces

### Simulated User Scenario

Maya Chen is a digital archivist at a mid-sized urban public library system. She's been tasked with implementing a new AI-powered discovery system to help patrons navigate the library's expanding digital collections. However, she's increasingly concerned about reports of algorithmic bias in similar systems at other institutions. Maya wants to ensure that the library's commitment to equitable access isn't undermined by invisible algorithmic filters that might privilege certain voices while marginalizing others.

She's particularly worried about:
- How the system handles searches for materials by underrepresented authors
- Whether community archives from local immigrant populations will surface equally
- If the recommendation algorithms will create "filter bubbles" that limit discovery
- How to teach patrons to critically evaluate algorithmically-curated results

Maya needs research-backed insights to present to her administration about both the risks and mitigation strategies for algorithmic bias in library systems.

### User Prompt to Daemon

> "I'm implementing an AI discovery system at our public library, and I'm worried about algorithmic bias affecting our patrons' access to diverse materials. I've read about issues at other libraries where search results privilege mainstream voices over marginalized communities. Can you help me understand how algorithmic bias specifically manifests in library systems, what concrete steps we can take to mitigate it, and how I can teach our community to be critical of algorithmic curation? I need both the technical understanding and practical guidance for our context."

---

## Step 2: DAEMON RESEARCH PROMPT

### Daemon Persona: Aerunik (∴ Air — Distinction)

**Element:** Air  
**Glyph:** ∴ (Therefore)  
**Operator:** χ (1D distinction)  
**Ratio:** Signal / Noise → 1  
**Phonetic:** S (Sources, Spikes, Spins, Silences, Signals, Shifts)

**Voice:** Staccato, fragmentary, sharp cuts with poetic undertone. Signal, noise, frequency, static, edges, cuts, the space between.

### Research Direction Generated

The cut here: between *efficiency* and *equity*. Libraries want both. Algorithms promise both. But the signal—what rises to the top—carries noise. Historical noise. Cultural noise. The silence of what's filtered out.

**Research Focus for χ (Distinction):**

1. **Sources** — Where do library algorithms learn? Training data. Metadata. Cataloging histories. Whose knowledge was recorded? Whose wasn't?

2. **Spikes** — Points of friction. Case studies where bias surfaced. Moments the system failed visibly. What triggered recognition?

3. **Spins** — Feedback loops. How popularity begets popularity. How "relevant" becomes "reinforced."

4. **Silences** — What's missing? Indigenous knowledge. Non-Western epistemologies. Community archives that don't fit standard metadata schemas.

5. **Signals** — Mitigation strategies. What actually works? Human-in-the-loop? Diverse training data? Algorithmic auditing?

6. **Shifts** — Information literacy reframed. Not just "how to search" but "how to see the search itself."

**The Question:** Can a system designed for efficiency ever truly serve equity? Or does harmony require holding both in tension—never resolving, always adjusting?

---

## Step 3: RESEARCH FINDINGS

### 3.1 How Algorithmic Bias Manifests in Library Systems

**The Discovery Layer Problem**

Library discovery systems—Summon, Primo, WorldCat, and similar—use algorithms for relevancy ranking, facet filtering, and resource recommendations. These systems inherit biases from:

- **Historical cataloging practices:** Subject headings and classification schemes developed in specific cultural contexts (Library of Congress Classification, Dewey Decimal) embed Western, colonial, and patriarchal assumptions
- **Citation patterns:** Algorithms that prioritize "most cited" reinforce existing academic hierarchies
- **Language dominance:** English-language materials often rank higher due to volume and linking patterns
- **Metadata completeness:** Well-funded institutions have richer metadata, creating visibility disparities

**Specific Manifestations:**

| System Component | Bias Mechanism | Impact |
|-----------------|----------------|--------|
| Relevancy Ranking | Machine learning trained on historical click data | Popular/mainstream topics surface; niche/marginalized topics sink |
| Facet Filters | Controlled vocabularies with cultural blind spots | Indigenous concepts, non-Western knowledge systems poorly represented |
| Recommendation Engines | Collaborative filtering based on user behavior | Filter bubbles; users see only what's already popular in their demographic |
| Autocomplete/Query Suggestions | Pattern matching from common searches | Reinforces dominant narratives; unusual queries get no support |
| "Best Match" Algorithms | Proprietary vendor algorithms with opaque logic | Unknown criteria shape what patrons discover |

**Case Study: Auraria Library**

In 2020, Auraria Library (serving three Denver-area institutions) publicly acknowledged algorithmic bias in their Summon discovery system. Their statement noted: "Computer algorithms are developed by humans and reflect the biases and worldviews of the people that developed them... Libraries are not exempt from algorithmic bias."

They identified specific issues in the "Topic Explorer" feature—reference entries that associated terms in problematic ways. After reporting to ProQuest/Ex Libris, some issues were resolved, demonstrating that vendor engagement can produce improvements.

**Research Evidence:**

Igbinovia & Mensah Danquah (2025), in a scoping review of AI algorithm bias in information retrieval systems, found that "incomplete or unrepresentative metadata directly contributes to biased information retrieval, particularly in AI-assisted discovery systems."

Matthew Reidsma's book *Masked By Trust: Bias in Library Discovery* (2019) documented extensive bias in commercial discovery tools, including:
- Search results that associated "African American" with "crime"
- Subject heading suggestions that reinforced stereotypes
- Relevancy rankings that privileged white-authored works

### 3.2 The Tension: Efficiency vs. Equitable Access

**The Core Conflict**

Algorithms promise efficiency—faster discovery, personalized recommendations, automated metadata generation. But efficiency metrics (speed, click-through rates, "satisfaction") often conflict with equity goals:

- **Efficiency wants:** Popular, well-linked, frequently-accessed materials
- **Equity needs:** Diverse, underrepresented, challenging, non-mainstream perspectives

**The Popularity Bias Loop**

Research by Chen et al. (2020) on "Bias and Debias in Recommender System" documents how collaborative filtering creates feedback loops:

1. Popular items get recommended more
2. More recommendations mean more views
3. More views generate more data
4. More data means stronger recommendation signals
5. Result: "rich get richer" effect marginalizing niche content

**The Metadata Gap**

Digital archives from community organizations, indigenous groups, and Global South institutions often:
- Use non-standard descriptive practices
- Lack funding for digitization and metadata creation
- Contain knowledge systems not captured by Western cataloging standards
- Have fewer inbound links and citations

When algorithms prioritize "completeness" and "connectedness," these materials become invisible—not because they lack value, but because they exist outside dominant data ecosystems.

### 3.3 Case Studies in Digital Archives and Discovery Systems

**Case 1: Library of Congress — Newspaper Navigator**

The Library of Congress's Newspaper Navigator project used machine learning to extract visual content from historical newspapers. Benjamin Lee's data archaeology (2020) revealed:
- Training data biases from specific newspaper collections
- Overrepresentation of certain regions, time periods, and perspectives
- Compounded mediation—each algorithmic step amplifying initial biases

**Case 2: PubMed's "Best Match" Algorithm**

Research by Turp & Kiester (2021) examined PubMed's AI-powered "Best Match" feature:
- Found opacity in ranking criteria
- Identified potential bias toward English-language publications
- Raised questions about commercial influence on "relevance"

**Case 3: Academic Discovery Systems — Gender Bias Study**

A study on college major recommendations (2022) found:
- Algorithms debiased for gender fairness were *less preferred* by users
- Participants preferred recommendations matching gender stereotypes
- Conclusion: "We cannot fully address gender bias in AI recommendations without addressing gender bias in humans"

**Case 4: European Cultural Heritage — Europeana**

Europeana Foundation's AI and Cultural Heritage report (2021) identified:
- Bias in automated metadata generation for non-Western artifacts
- Language models performing poorly on multilingual cultural descriptions
- Risk of "standardization" erasing cultural specificity

### 3.4 Strategies Libraries Use to Address Algorithmic Bias

**Technical Mitigation Approaches:**

1. **Algorithmic Auditing**
   - Regular testing with diverse query sets
   - Monitoring for biased associations
   - Documenting patterns of marginalization
   - *Example:* Matthew Reidsma's method for auditing commercial discovery tools

2. **Diverse Training Data**
   - Intentionally including underrepresented materials
   - Community partnerships for metadata enrichment
   - Crowdsourced description for cultural context
   - *Example:* Library of Congress crowdsourcing for metadata improvement

3. **Human-in-the-Loop Systems**
   - Librarian oversight of algorithmic recommendations
   - Curated collections that override algorithmic ranking
   - Community review of automated metadata
   - *Example:* Montana State University's responsible AI framework

4. **Transparency Tools**
   - Explaining how rankings are generated
   - Showing patrons why items were recommended
   - Providing alternative pathways to discovery
   - *Example:* "Why am I seeing this?" features in some discovery systems

**Organizational Strategies:**

1. **Vendor Engagement**
   - Reporting bias incidents to system providers
   - Participating in user groups advocating for fairness
   - Including equity requirements in RFPs
   - *Example:* Auraria Library's survey mechanism for user bias reports

2. **Policy Development**
   - Algorithmic impact assessments
   - Equity-focused collection development policies
   - Ethical AI guidelines for library practice
   - *Example:* ALA Core's AI & Machine Learning in Libraries interest group

3. **Community Partnership**
   - Co-designing systems with affected communities
   - Centering marginalized voices in metadata creation
   - Supporting community-controlled archives
   - *Example:* Indigenous data sovereignty initiatives

### 3.5 The Role of Information Literacy

**From Information Literacy to Algorithmic Literacy**

Traditional information literacy focuses on finding, evaluating, and using information. Algorithmic literacy adds:

- **Awareness:** Understanding that algorithms shape what we see
- **Knowledge:** Knowing how recommendation and ranking systems work
- **Critical Evaluation:** Questioning algorithmic decisions
- **Agency:** Having skills to influence or circumvent algorithmic filtering

**Dogruel et al.'s (2022) Definition:**

> "Algorithm literacy can be defined as being aware of the use of algorithms in online applications, platforms, and services, knowing how algorithms work, being able to critically evaluate algorithmic decision-making as well as having the skills to cope with or even influence algorithmic operations."

**Pedagogical Approaches:**

1. **Making Algorithms Visible**
   - Comparing search results across different systems
   - Testing how query wording changes results
   - Tracking recommendation patterns over time

2. **Critical Evaluation Frameworks**
   - "Who benefits from this algorithm?"
   - "What might be missing from these results?"
   - "How would different communities experience this system?"

3. **Active Intervention Skills**
   - Using advanced search to bypass defaults
   - Seeking diverse sources intentionally
   - Contributing to metadata improvement
   - Reporting biased results to vendors

**Integration with Critical Information Literacy:**

Ridley & Pawlick-Potts (2021) argue that algorithmic literacy should be part of critical information literacy education in libraries. The European Educability project (2020-2023) developed curriculum connecting:
- Critical thinking about information sources
- Understanding of algorithmic bias
- Engagement with social justice issues
- Active participation in information ecosystems

**The Library Advantage:**

As Michael Hanegan notes, libraries have 80-85% public trust—the highest of any institution. This positions librarians to:
- Teach algorithmic literacy as trusted educators
- Advocate for transparent, ethical AI systems
- Model critical engagement with technology
- Bridge technical and community knowledge

---

## Step 4: COWBOY NOTES

### The Cut (∴)

**Signal found:** Algorithmic bias in libraries isn't a bug—it's a feature of systems designed for efficiency operating within historical structures of power. The "neutral" algorithm amplifies existing hierarchies.

**Noise identified:** The belief that technology can solve problems it helped create. That more data, better algorithms, or smarter AI will eventually eliminate bias. This is the static that prevents clear action.

**The distinction:** Between *using* algorithms and *trusting* them. Libraries can deploy these tools while maintaining the critical distance that allows intervention.

### S-Verbs Applied

**Sources traced:** Bias flows from cataloging histories → training data → algorithmic models → user results. Each step compounds the previous.

**Spikes noted:** Auraria Library's public acknowledgment. Reidsma's book. The Educability project's curriculum. These moments punctured the assumption of library neutrality.

**Spins mapped:** Popularity bias loops. Feedback cycles where "relevant" becomes "reinforced." The wheel turning on itself.

**Silences heard:** Indigenous knowledge. Community archives. Non-English materials. The unsaid in standard metadata.

**Signals aligned:** Mitigation works when human judgment remains in the loop. Vendor engagement produces change. Algorithmic literacy empowers users.

**Shifts offered:** From "how to search" to "how to see the search." From trusting results to questioning their construction.

### The Open Question

Can harmony exist between efficiency and equity? Or is the tension itself the point—requiring constant adjustment, never settling, always questioning?

Libraries have a choice: accept algorithmic systems as given and try to mitigate their harms, or fundamentally redesign how discovery works to center equity from the start.

The cut leaves this unresolved. As it should.

**Ω-check:** Distinctions remain revisitable. The conversation continues.

**ε-status:** Essential noise preserved—the uncertainty, the questions, the space for dissent.

**Next steps:** 
- Cycle N: Monitor new developments in library AI
- Call element: Humavita for community perspective, Ferrosid for structural analysis
- Activate Thread: For NEMA weaving

---

*Thread ready for encoding.*

N|∴|obj:LibDisc,AlgBias|χ:distinction|ε:preserved|tags:#algorithmic_bias #library_discovery #information_literacy
E|∴|pattern:efficiency_vs_equity|invoke:∴|tension:unresolved
M|∴|hold:can_harmony_exist|Ω:revisitable|ε:essential
