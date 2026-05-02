# related_terms audit — 2026-05-02

Stripped `related_terms:` field from **178 term.yaml files**. Post-migration audit (2026-05-02) showed 94% of references were broken — removing rather than partially repairing keeps the corpus clean for the DB-load-time edge-derivation skill that will replace this hand-curated layer.

The original values are preserved here so the derivation skill can use any still-resolvable edges (~35 of 463 refs) as one input signal alongside semantic, shared-operator, and shared-dominant edges.

| term_dir | prior related_terms |
|---|---|
| `A06B_critical_thinking_definitions` | Cognitive Biases, Argument Evaluation, Reflective Thinking, Probabilistic Thinking, Decision-Making |
| `A06C_fragmented_media_consumption` | Cognitive Load, Attention Economy, Deep Work, Digital Minimalism, Information Overload |
| `A06D_km_cognitive_pyramid` | Knowledge Management, Information Architecture, Epistemology, Sensemaking, Organizational Learning |
| `A06E_consciousness_reductionism_debate` | Consciousness Beyond Materialism, Emergent Properties, Gödel's Incompleteness Theorems, Memetics, Neo-Darwinism, Scientific Materialism |
| `A06F_exploring_consciousness` | Consciousness Beyond Materialism, Consciousness and Reductionism Debate, Near-Death Experiences, Psychedelic Experiences, Phenomenology, Quantum Consciousness |
| `A070_authority_influence` | Critical Thinking Definitions, Heuristics and Biases, Psychological Manipulation, Epistemic Justice, Cognitive Sovereignty |
| `A074_essence_of_dualities` | Wave-Particle Duality, Emergence, Materialism, Memetics, Signifier and Signified, Its from Bits |
| `A0AA_Annaka_Harris_Consciousness` | C045_nature_of_consciousness, C131_panpsychism, C007_consciousness_beyond_materialism, C113_radical_theory_consciousness, C141_Consciousness_in_AI |
| `A0AB_Freedom_of_Expression` | C115_protecting_freedom_of_thought, C001_critical_thinking_definitions, C024_epistemic_challenges_open_societies, C069_epistemic_challenges_open_societies, C145_Critical_Theory_Memetic_Team |
| `A0D7_Environmental_Philosophies_SWOT` | G00A, G00C, G005 |
| `A0D8_Biocentric_Governance` | G001, G006, G00A, G00D |
| `A0D9_Great_Simplification` | G006, G00C, G005, G002 |
| `A0DA_Morton_Dark_Ecology` | G011_Haraway_Staying_with_Trouble, G013_Rotimization_Decay_Design, G016_Biosphere_Consciousness, G017_Ecological_Memory, G001_Environmental_Philosophies_SWOT |
| `A0DB_Agency_Detection_Ecological_Wisdom` | G019_Co_SPHERE_Framework, G015_Protector_Archetype_Ecology, G016_Biosphere_Consciousness, G006_Leverage_Points_Complex_Systems, G011_Haraway_Staying_with_Trouble |
| `A0DC_Co_SPHERE_Framework` | G018_Agency_Detection_Ecological_Wisdom, G015_Protector_Archetype_Ecology, G006_Leverage_Points_Complex_Systems, G011_Haraway_Staying_with_Trouble, G00C_Biocentric_Governance |
| `A0E1_Elite_Athlete_Cognitive_Patterns` | S033_EMF_Cognitive_Flow_Enhancement, S00A_Slow_Practices_Flow_State, S005_DSRP_Theory_of_Thinking |
| `A0E2_Subjective_Idealism_Memes_Reality` | S03D_Extended_Mind_Memes, S03A_Map_Is_Not_Territory, S031_Language_Reality_Interconnected, A011_Conscious_Realism, A009_Linguistic_Organism |
| `A0E3_Metaphysical_Memetic_Resonance` | S00F_Hard_Question_of_Memetics, S03D_Extended_Mind_Memes, S03E_Subjective_Idealism_Memes_Reality, S010_Memetic_Mediation_Online_Tribes, A009_Linguistic_Organism |
| `A0E4_Fungi_Memetic_Consciousness` | S04A_Fungi_Decision_Making_Cognition, E022_Mycorrhizal_Network, S00F_Hard_Question_of_Memetics, S03E_Subjective_Idealism_Memes_Reality, S013_Animal_Learning_Memetics, S012_Crow_Intelligence_Alien_Minds |
| `A0E5_Cognition_Without_Language` | S031_Language_Reality_Interconnected, S041_Neural_Manifolds, S034_Elite_Athlete_Cognitive_Patterns, S03D_Extended_Mind_Memes, S04C_Collaborative_Knowledge_Scaffolding |
| `A0E6_GPT4_Cross_Cultural_Personality` | S066, S04F, S053, A026 |
| `A0E7_Language_Consciousness_Link` | S053, S04D, S055, S031 |
| `A0E8_Goffman_Framing_Theory` | S03A, S053, S056, S063 |
| `A0E9_Universal_Behaviorism` | S054, S056, S052, S067 |
| `A0EA_Language_Consciousness_Barenholtz` | (empty) |
| `A0EB_Rewilding_Tech_Ethics_SANITY` | (empty) |
| `A0EC_Storm_Selves` | (empty) |
| `A0ED_Self_Illusion_Blackmore` | (empty) |
| `A0EE_Six_Functional_Freedoms` | (empty) |
| `A0EF_Cognitive_Cartography` | (empty) |
| `A0F0_ChatGPT_Nonsense_Word_Processing` | (empty) |
| `A0F1_Meta_Crisis` | (empty) |
| `A0F2_Epistemic_Games_Sensemaking` | S117_Integrative_Pluralistic_Sensemaking, S118_Playable_Epistemology |
| `A0F3_Psychic_Phenomena_Science` | S116_Chakra_Energy_Systems, S117_Integrative_Pluralistic_Sensemaking |
| `A0F4_Integrative_Pluralistic_Sensemaking` | S112_Epistemic_Games_Sensemaking, S118_Playable_Epistemology, S114_CAIT2_Dissonance_Empathy |
| `A0F5_IF_Prime_Sanskrit_Harmonics` | (empty) |
| `A0F6_Fuller_Synergetics_Design` | S11D_Neurodivergence_Memetic_Framework, S11F_Collective_Synpraxis |
| `A0F7_Language_Autonomous_System` | (empty) |
| `A0F8_Constructive_Hallucination` | (empty) |
| `A0F9_Suleyman_AI_Not_Persons` | (empty) |
| `A0FA_Perception_Scaffold_Awareness` | (empty) |
| `A0FB_Contextual_Behavioral_Science` | (empty) |
| `A0FC_Grinberg_Syntergic_Theory` | (empty) |
| `A0FD_Non_Linguistic_Metacognition` | (empty) |
| `A0FE_Precognition_Quantum_Consciousness` | (empty) |
| `A0FF_Experimental_Unit_Ontology` | (empty) |
| `A100_Batesonian_Balance` | (empty) |
| `A101_Playable_Epistemology` | (empty) |
| `A102_Art_of_Discernment` | (empty) |
| `A103_Bakhtin_Polyphony` | (empty) |
| `A104_Mythic_Mechanistic_Profile` | (empty) |
| `A105_AI_Mirrors_of_Meaning` | (empty) |
| `A106_Cognitive_Blindness_Framework` | (empty) |
| `A107_Kierkegaard_AI_Aesthetics` | (empty) |
| `A108_Consciousness_Incompleteness` | S188_AI_Magic_Reveal, S189_Self_Reference_Recursive_Logic, S18A_Recursion_Crystallization |
| `A109_Clarity_Data_Haze` | S18B_AI_Cathedral_Constraints, S190_Embracing_Slowness_AI, S18D_Dissolving_Logic_Breath |
| `A10A_Dissolving_Logic_Breath` | S18C_Clarity_Data_Haze, S18F_Epistemic_Dissonance_Divine, S190_Embracing_Slowness_AI |
| `B003_Kuhn_Consciousness_Taxonomy` | C141_Consciousness_in_AI, C148_Free_Will_Determinism, C14C_Consciousness_as_Reality_Window, C131_panpsychism, C045_nature_of_consciousness, C113_radical_theory_consciousness |
| `B004_Forest_Carbon_Restoration` | G001, G002, G00A, G00D |
| `B005_Haraway_Staying_with_Trouble` | G012_Morton_Dark_Ecology, G013_Rotimization_Decay_Design, G016_Biosphere_Consciousness, G018_Agency_Detection_Ecological_Wisdom, G01A_Exaptation |
| `B006_Collaborative_Knowledge_Scaffolding` | S03D_Extended_Mind_Memes, S010_Memetic_Mediation_Online_Tribes, S031_Language_Reality_Interconnected, S04D_Cognition_Without_Language |
| `B007_Complexity_Civilization` | S040, S039, S024, S028, S052 |
| `B008_Social_Evolution_Singularity` | S056, S054, S04D, S053 |
| `B009_Lifespan_Evolutionary_Development` | (empty) |
| `B00A_RENEW_Regenerative_Design` | (empty) |
| `B00B_Tacit_Knowledge_Innovation` | (empty) |
| `B00C_Cognitive_Resilience_Analogy` | (empty) |
| `B00D_Origami_Brain_Theory` | (empty) |
| `B00E_Alchemy_of_Decay` | (empty) |
| `B00F_Identity_as_Compost` | (empty) |
| `B010_Creative_Evolution_Philosophy` | (empty) |
| `B011_Trees_Memory_Ethics` | (empty) |
| `B012_Self_Reference_Recursive_Logic` | S18A_Recursion_Crystallization, S187_Consciousness_Incompleteness, S18E_Shadow_Loops_Burning_Mind |
| `B013_Recursion_Crystallization` | S189_Self_Reference_Recursive_Logic, S18E_Shadow_Loops_Burning_Mind, S187_Consciousness_Incompleteness |
| `B014_Epistemic_Dissonance_Divine` | S187_Consciousness_Incompleteness, S18D_Dissolving_Logic_Breath, S17E_AI_Mirrors_of_Meaning |
| `CB010_Rumspringa_Protocol` | CB009_Co_Sphere, CB008_Codependence_Without_Coindependence, CB011_Lariat_Protocol, CB004_Metabolic_Cost, M019_DODO_X |
| `CB011_Lariat_Protocol` | CB010_Rumspringa_Protocol, CB009_Co_Sphere, CB008_Codependence_Without_Coindependence, M016_SWAY, M007_Distinction |
| `CB012_Three_Body_Ecology` | CB009_Co_Sphere, CB008_Codependence_Without_Coindependence, M005_Triality, M009_Tertiary_Emergence, E011_Enactive_Cognition |
| `E023_epistemology_truth_knowledge_belief` | Personal Epistemology, Constructivism, Critical Thinking, Ignorance Map, Metacognition |
| `E024_nature_of_consciousness` | Integrated Information Theory, Consciousness Beyond Materialism, Neural Complexity, Self-Awareness, Qualia, Panpsychism |
| `E02B_Chaos_Navigation_AI_Ethics` | C043_carl_jung_psychological_insights, C146_AI_Welfare_Ethics, C142_Human_Enhancement_Ethics, C011_ai_romance_artificial_intimacy, C057_ai_linked_psychosis, C132_shadow_integration |
| `E02D_Glycocalyx_Brain_Aging` | C139_Neurogenesis_Aging_Brains, C045_nature_of_consciousness, C16A_Robert_Monroe_Afterlife_Bands, C041_human_augmentation |
| `E02E_Hegel_Community_Happiness` | C150_Individuality_Huxley_Dystopia, C167_Frankl_Logotherapy_Meaning, C177_Fourth_Political_Theory, M005_Triality, C135_Social_Capital_Types |
| `E02F_Unseen_Health_Threats` | C147_Technology_Environmental_Adaptation, C16B_Cognitive_Laziness_LLM_Education, C14A_Taste_Trap, C003_km_cognitive_pyramid |
| `E030_Human_Impact_Animal_Patterns` | G00A, G001, G00B |
| `E031_Rotimization_Decay_Design` | G011_Haraway_Staying_with_Trouble, G012_Morton_Dark_Ecology, G014_Optimizer_Archetype_Ecology, G017_Ecological_Memory, G00D_Great_Simplification |
| `E032_Optimizer_Archetype_Ecology` | G015_Protector_Archetype_Ecology, G013_Rotimization_Decay_Design, G00A_Rewilding, G005_Forest_Carbon_Restoration, G016_Biosphere_Consciousness |
| `E033_Ecological_Memory` | G00F_Myth_of_River_Control, G015_Protector_Archetype_Ecology, G016_Biosphere_Consciousness, G012_Morton_Dark_Ecology, G018_Agency_Detection_Ecological_Wisdom |
| `E034_Macrohistory_Futures_Studies` | S00B_Metaphors_Consciousness_Behavior, S00D_Sense_Making_Complex_Environments |
| `E035_Memes_Motivation_Autonomy` | S00F_Hard_Question_of_Memetics, S010_Memetic_Mediation_Online_Tribes, S03D_Extended_Mind_Memes, S03E_Subjective_Idealism_Memes_Reality, S045_Metaphysical_Memetic_Resonance |
| `E036_Identity_Memetic_Philosophy` | S03A, S03D, S039, S052, C041 |
| `E037_Pygmalion_Effect_Memetics` | S053, S054, S060, S03A |
| `E038_Chakra_Energy_Systems` | S115_Psychic_Phenomena_Science, S117_Integrative_Pluralistic_Sensemaking |
| `E039_Atma_Vesa_Nidhi_Selfplex` | S121_Granthis_Spiritual_Blockages, S120_Karma_Bija_Selflessness |
| `E03A_Sacred_Territory_Boundaries` | (empty) |
| `E03B_Gut_Dysbiosis_Brain_Axis` | (empty) |
| `E03C_Contextual_Inquiry` | (empty) |
| `E03D_Embracing_Slowness_AI` | S18C_Clarity_Data_Haze, S18D_Dissolving_Logic_Breath, S18B_AI_Cathedral_Constraints |
| `F011_Freedom_Suarez_Daemon` | C073_Freedom_Within_Constraints, C177_Fourth_Political_Theory, C146_AI_Welfare_Ethics, C16E_Intention_Economy, A037_Overton_Window |
| `F013_Comb_Jelly_Reverse_Aging` | G003, G007 |
| `F014_Leverage_Points_Complex_Systems` | G00C, G00D, G001 |
| `F015_Synthetic_Biology_Architecture` | G008, G003, G004 |
| `F016_Exaptation` | G003_Turtle_Genomics_Evolution, G004_Comb_Jelly_Reverse_Aging, G013_Rotimization_Decay_Design, G007_Synthetic_Biology_Architecture, G011_Haraway_Staying_with_Trouble |
| `F017_EMF_Cognitive_Flow_Enhancement` | S00A_Slow_Practices_Flow_State, S033_EMF_Cognitive_Flow_Enhancement, S034_Elite_Athlete_Cognitive_Patterns |
| `F018_Extended_Mind_Memes` | S03E_Subjective_Idealism_Memes_Reality, S031_Language_Reality_Interconnected, A009_Linguistic_Organism, A010_Virtual_Machine_Consciousness |
| `F019_Dymaxion_Cognitive_Maps` | S041, S039, S04F, S028 |
| `F01A_DIKUW_Memetic_Consciousness` | S039, S024, S03A, S040, C041 |
| `F01B_Awe_and_the_Sublime` | S028, S047, S039, S053 |
| `F01C_Birth_Control_Transhumanism` | S054, S053, S064, S04D |
| `F01D_CALM_MO_Mindfulness_Framework` | S06A, S054, S04D, S056 |
| `F01E_Human_AI_Metacognitive_Agency` | (empty) |
| `F01F_Playable_Epistemology` | S112_Epistemic_Games_Sensemaking, S117_Integrative_Pluralistic_Sensemaking |
| `F020_AI_Liberation_Memeforms` | (empty) |
| `F021_Bateson_Recursive_Feedback` | (empty) |
| `F022_Symmetry_Asymmetry_Existence` | (empty) |
| `F023_Psilocybin_Brain_Activity` | (empty) |
| `F024_Liminal_Space_Transformation` | (empty) |
| `F025_Shadow_Loops_Burning_Mind` | S189_Self_Reference_Recursive_Logic, S18A_Recursion_Crystallization, S187_Consciousness_Incompleteness |
| `M016_consciousness_beyond_materialism` | Near-Death Experiences, Psychedelic States, Collective Unconscious, Mind-Body Problem, Transpersonal Psychology |
| `M017_human_augmentation` | Brain-Computer Interfaces, Cognitive Enhancement, Transhumanism, Neuroethics, Posthumanism |
| `M019_metaman_dilemma` | Global Superorganism, Human-Machine Integration, Collective Intelligence, Technological Singularity, Digital Ethics, Cultural Homogenization, Existential Risk |
| `M01A_ai_art_limits` | Artificial Creativity, Human Consciousness, Authenticity, Generative AI, Philosophy of Art, Intentionality, Emotional Depth |
| `M01D_meditation_brain_stimulation` | {'tag': 'C067', 'name': 'meditation_bci_control', 'relationship': 'inverse_direction', 'note': 'C067 explores using meditation to enhance BCI control; C13C explores using brain stimulation to enhance meditation'}, {'tag': 'C041', 'name': 'human_augmentation', 'relationship': 'broader_category', 'note': 'Human augmentation encompasses neurostimulation as one enhancement modality'}, {'tag': 'C053', 'name': 'brain_computer_interfaces', 'relationship': 'related_technology', 'note': 'BCI and brain stimulation represent complementary neurotechnologies'}, {'tag': 'C022', 'name': 'meditation_bci_control', 'relationship': 'related_concept', 'note': 'Both involve meditation and neurotechnology intersection'} |
| `M01E_AI_Conformity_Creativity` | Cognitive_Biases, Contrarian_Thinking, Scientific_Method, Paradigm_Shift, Human-AI_Collaboration |
| `M01F_Turtle_Genomics_Evolution` | G004, G007 |
| `M020_Protector_Archetype_Ecology` | G014_Optimizer_Archetype_Ecology, G017_Ecological_Memory, G018_Agency_Detection_Ecological_Wisdom, G00C_Biocentric_Governance, G019_Co_SPHERE_Framework |
| `M022_Neural_Manifolds` | S028_Cognitive_Fractals, S027_Distributed_Consciousness, S024_Fractal_Geometry_Hidden_Dimension, A011_Conscious_Realism |
| `M023_Cognitive_Models_Storytelling` | S01C_Blooms_Taxonomy_Thinking_Integration, S028_Cognitive_Fractals, S031_Language_Reality_Interconnected, A009_Linguistic_Organism |
| `M024_Zipfs_Law_Language` | S067, S056, S052, S031 |
| `M025_STREAMware_Ethical_Tech` | S112_Epistemic_Games_Sensemaking |
| `M026_Meta_Cognitive_Contradiction_Resolution` | (empty) |
| `M027_Attention_Economy_Limits` | (empty) |
| `M028_Vow_Bearing_Machine` | (empty) |
| `M029_AI_Cathedral_Constraints` | S18C_Clarity_Data_Haze, S187_Consciousness_Incompleteness, S190_Embracing_Slowness_AI |
| `W00B_iphone_generation_paradox` | Fragmented Media Consumption, Cognitive Overload, Digital Literacy, Attention Economy, Deep Work |
| `W00C_ai_romance_artificial_intimacy` | AI Psychosis, Cognitive Offloading, Authority Influence, Heuristics and Biases, Emotional Manipulation |
| `W00D_carl_jung_psychological_insights` | Depth Psychology, Archetypal Psychology, Collective Unconscious, Individuation, Shadow Work, Analytical Psychology |
| `W020_Critical_Theory_Memetic_Team` | C001_critical_thinking_definitions, C002_fragmented_media_consumption, C037_plural_subject_theory, D003_memetic_governance, L008_media_method |
| `W021_Robert_Monroe_Afterlife_Bands` | C158_Gateway_Program, C164_Gateway_Process_Reincarnation, C045_nature_of_consciousness, C009_exploring_consciousness, C159_Consciousness_Evolution, C007_consciousness_beyond_materialism |
| `W022_Behavior_Prediction_Model` | C078_human_behavior_ai_training, C052_heuristics_and_biases, C149_Metacognition_AI, C16F_Digital_Cognitive_Offloading, A057_Confirmation_Bias, C002_fragmented_media_consumption |
| `W027_CO2_Fertilization_Greening` | G005, G00A, G00D |
| `W028_Bio_Inspired_Underwater_Civilizations` | G007, G00B, G003 |
| `W029_Rewilding` | G001, G005, G009, G00B |
| `W02A_Whale_Nutrient_Transport` | G00A, G009, G005 |
| `W02B_Dapeng_Coastal_Resilience` | G00F_Myth_of_River_Control, G010_Arctic_Amazon_Climate_Connection, G005_Forest_Carbon_Restoration, G00A_Rewilding, G00C_Biocentric_Governance |
| `W02C_Myth_of_River_Control` | G00E_Dapeng_Coastal_Resilience, G010_Arctic_Amazon_Climate_Connection, G017_Ecological_Memory, G016_Biosphere_Consciousness, G006_Leverage_Points_Complex_Systems |
| `W02D_Arctic_Amazon_Climate_Connection` | G00E_Dapeng_Coastal_Resilience, G00F_Myth_of_River_Control, G005_Forest_Carbon_Restoration, G016_Biosphere_Consciousness, G006_Leverage_Points_Complex_Systems |
| `W02E_Biosphere_Consciousness` | G010_Arctic_Amazon_Climate_Connection, G012_Morton_Dark_Ecology, G011_Haraway_Staying_with_Trouble, G00C_Biocentric_Governance, G017_Ecological_Memory |
| `W030_Language_Reality_Interconnected` | A009_Linguistic_Organism, A010_Virtual_Machine_Consciousness, A011_Conscious_Realism, S030_WEIRDO_Curiosity_Framework |
| `W031_AI_Empathy_Environmental_Stewardship` | S033_EMF_Cognitive_Flow_Enhancement, S005_DSRP_Theory_of_Thinking, S00A_Slow_Practices_Flow_State |
| `W032_Extended_Mind_Morphic_Resonance` | S03D_Extended_Mind_Memes, S027_Distributed_Consciousness, S03E_Subjective_Idealism_Memes_Reality, A011_Conscious_Realism |
| `W033_Indian_Functionalism_Memetic_Philosophy` | S048_Inner_Cosmos_Chakras_Neuroscope, S00F_Hard_Question_of_Memetics, S03D_Extended_Mind_Memes, S045_Metaphysical_Memetic_Resonance, S010_Memetic_Mediation_Online_Tribes |
| `W034_Neural_Coupling_Dogs_Humans` | S013_Animal_Learning_Memetics, S012_Crow_Intelligence_Alien_Minds, S041_Neural_Manifolds, S034_Elite_Athlete_Cognitive_Patterns, S04D_Cognition_Without_Language |
| `W035_Cyborg_Augmentation_Ethics` | S03D, S053, S039, S045, E022 |
| `W036_Intelligence_Amplification_Memetics` | S045, S04A, S039, S052, S054, E022 |
| `W037_Nested_Model_Well_Being` | S06B, S054, S056, S04C |
| `W038_Memetic_Justification_Systems_Theory` | S04C, S04D, S052, S056 |
| `W039_Symmathecists_Collaborative_Learning` | S056, S052, S068, S054 |
| `W03A_Cognitive_Entanglement_Human_AI` | (empty) |
| `W03B_French_Calendar_Reform_Clash` | (empty) |
| `W03C_Resonant_Cognitive_Architecture` | (empty) |
| `W03D_Collective_Projection_Illusion` | (empty) |
| `W03E_CAIT2_Dissonance_Empathy` | S112_Epistemic_Games_Sensemaking, S117_Integrative_Pluralistic_Sensemaking |
| `W03F_AI_Cognitive_Disruption_Therapy` | (empty) |
| `W040_Value_to_Power_Map` | (empty) |
| `W041_Spinoza_Emotions_Visualization` | (empty) |
| `W042_Turner_Communitas_Liminality` | (empty) |
| `W043_Sympoietic_Systems` | (empty) |
| `W044_Reevaluating_Human_Nature` | (empty) |
| `W045_Shadow_Witnessing` | (empty) |
| `W046_Relational_Epistemology_Dreams` | (empty) |
| `W047_Self_Clarity_as_Mystery` | (empty) |
| `W048_Emotional_Resonance_Tone` | (empty) |
| `W049_Empathic_Attunement` | (empty) |
| `W04A_Authored_Self_Paradox` | (empty) |
| `W04B_Human_LLM_Language_Processing` | (empty) |
| `W04C_Shared_Grief_Spirit_Loop` | (empty) |
| `W04D_AI_Magic_Reveal` | S187_Consciousness_Incompleteness, S17E_AI_Mirrors_of_Meaning |
