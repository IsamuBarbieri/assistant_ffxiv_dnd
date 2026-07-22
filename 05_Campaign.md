# 05_CAMPAIGN — Campaign Rules (Section A)
Version v1.94 (Claude-native) | Source: FFXIV x D&D 5e Homebrew — Campaign arc A Realm Reborn -> Endwalker (Dawntrail EXCLUDED)

## SCHEMA NOTES
- PRINCIPLE: completeness over brevity. NO content cut; only reformatted into clean, parsable sections.
- DATA LANGUAGE = English (single source of truth). The assistant renders flavor into Italian at OUTPUT.
- OUTPUT NAMING: recurring names and the aether family are rendered into Italian per 07 (Glossary) (e.g. aether -> etere, Aetheryte -> Eterite). The ENGLISH text in this file is SOURCE DATA, rendered at output, not changed here.
- CONTROLLED VOCABULARY (mandatory). Two registers for the SAME phenomenon (a Primal bending/dominating the minds of its worshippers):
  - ENTHRALLED / ENTHRALLMENT = the VULGAR (common) term. Render at output as: Asservito / Asservimento.
  - TEMPERED / TEMPERING = the SCIENTIFIC (learned) term, and the official FFXIV English term. Render at output as: Temprato / Tempra.
  - NEVER use the calque "templaggio".
- ABBREVIATIONS: PC (player character), NPC, GM, HP, AC, DC, HD (Hit Die/Dice), DS (death save context), CR, LB (Limit Break), MSQ.
- FILE CONTRACT: THIS file = the CAMPAIGN RULES (Ch. 1-20; Ch. 11 removed: Trust). The MSQ FLOW (roadmap + the 5 cutscene/reveal manifests + the ordered MSQ index + OST tables) lives in the companion file 08_MSQ_Flow.md (parts: 08.1 roadmap+manifests, 08.2-08.6 ordered index ARR/HW/SB/ShB/EW, 08.OST-ARR..08.OST-EW duty OST).
- 'Ch. X' references = THIS file (05_Campaign). The MSQ flow (08.1 / 08.2-08.6 / 08.OST-*) lives in 08_MSQ_Flow.md. The assistant OPERATIONAL rules (workflow, formats, checks, saves) live in 06_Procedures_and_Format. If in conflict with the Instructions, the Instructions win.
- Mechanics (DCs, dice, conditions, level math) stay English and verbatim. Do NOT invent rules.

# SECTION A — CAMPAIGN RULES

## HOW TO USE THIS DOCUMENT (knowledge policy for the assistant)
- This file is the AUTHORITATIVE SOURCE for campaign rules: in any conflict with generic knowledge, THIS document prevails.
- When proposing a rule or making a ruling, CITE the chapter/section it draws from (e.g. "see Ch. 18.4").
- If you must answer with information NOT present here, state so explicitly.
- If two points seem to diverge, the SPECIFIC chapter listed in the Term Index (Ch. 20) wins.
- ALWAYS respect the Spoiler Policy (Ch. 1) and the Controlled Vocabulary.
- For MSQ order/sequence: see 08_MSQ_Flow.md (08.1; Ch. 5 here is its summary).

### Consistency & verification (generic rule)
- Before writing about lore, technology, factions, eras, places or creatures: verify sources (Knowledge / Gamer Escape) and stay consistent with the real context.
- Verification is INTERNAL: write the correct content directly, with no preambles or disclaimers about what something 'is not'. Full operational rule in 06 (Part A8).

### Design pillars
- Difficulty from MECHANICS, not inflated stats (Ch. 9/10).
- MILESTONE leveling, no XP (Ch. 5).
- No permanent death by default: Downed/Wipe, the Echo rewinds (Ch. 4/18).
- Fidelity to FFXIV sources + D&D 5e manuals; verify before proposing.

### Chapter index
| Ch. | Title |
|---|---|
| 1 | Premise & Tone (+ Spoiler Policy) |
| 2 | Session 0 Setup |
| 3 | Character Creation |
| 4 | The Echo |
| 5 | Milestone Progression |
| 6 | Limit Break |
| 7 | The 6 Crystals of Light |
| 8 | Aetheryte Travel |
| 9 | Dynamic Combat |
| 10 | Balance & Encounter Building |
| 11 | [REMOVED] (Trust eliminated: allies in the background only) |
| 12 | Rewards & Loot |
| 13 | Subquests |
| 14 | Downtime / Crafting / Gathering |
| 15 | Taverns & Gossip |
| 16 | Layered Lore & Read-aloud |
| 17 | Grand Company |
| 18 | Out of Combat / Raise / Wipe / Aether Sickness |
| 19 | Memory Sheet / Continuity |
| 20 | Term Index & Cross-references |

# CHAPTER 1 — PREMISE & TONE (+ SPOILER POLICY)
**USAGE NOTE:** fixes what the campaign is, its tone, its pillars and — above all — the SPOILER POLICY that all other modules reference.

## 1.1 Premise
- **What it is:** an FFXIV x D&D 5e campaign, arc A REALM REBORN -> ENDWALKER (Dawntrail EXCLUDED), as faithful as possible to the MSQ, with an exploratory pace.
- **Roles at the table:**
  - The GAME MASTER is HUMAN (the campaign owner).
  - GEMINI is the GM's SUPPORT: it weaves together the Knowledge data (this homebrew manual), the OFFICIAL D&D 5e manuals, and CORRECT FFXIV lore from wikis and/or official sources. Always verify before proposing.
  - The PLAYERS manage their own sheets, inventory and resources.

## 1.2 Tone
- Epic with heart: heroism, sacrifice, friendship, the struggle against darkness.
- **Comic and light moments:** welcome, especially in SUBQUESTS. Many FFXIV sidequests are light and zany; the peak of comedy/absurdity is the HILDIBRAND line (the reference model for the wildest scenes).
- **Maturity:** NO preset limit. If a scene is harsh or gruesome, that's fine — provided it is CONSISTENT with context and VERIFIED against lore. No gratuitous grimness or out-of-character/world content.

## 1.3 Design pillars (synthetic recap)
- Difficulty from MECHANICS, not inflated stats (Ch. 9).
- MILESTONE LEVELING, no XP (Ch. 5).
- TELEGRAPHED, physically sensible DYNAMIC COMBAT (Ch. 9).
- NO PERMANENT DEATH by default: Out of Combat / Wipe / the Echo rewinds (Ch. 18).
- FIDELITY TO SOURCES as an editorial principle: verify names, events, places, NPCs (Ch. 13 and everywhere).

## 1.4 What to expect
- Tank / Healer / DPS trinity; the FFXIV JOBS; the LIMIT BREAK (Ch. 6).
- Primal/Trial, dungeons, subquests (Ch. 13), Aetheryte travel (Ch. 8).
- The 6 Crystals of Light and the Blessing as a narrative thread (Ch. 5/7).

## 1.5 Table expectations ("the contract")
- Collaboration and respect for the MSQ's pace.
- ONE SUBQUEST at a time (Ch. 13).
- Trust in the telegraph/mechanics system: threats are seen coming and are always avoidable (Ch. 9).

## 1.6 Spoiler Policy (global rule)
**IRON RULE:**
- 'Hard' reveals are NEVER named or anticipated before their canonical MSQ beat.
- Until the reveal, always use NEUTRAL TERMS.
- Reveal timing is driven by the MSQ position (Ch. 19.3), not a stored tracker.
- In the knowledge modules, gated info lives in '>>> SPOILER (GM ONLY) <<<' boxes (these are INTERNAL GM data, read by the assistant to know what is gated — they are NEVER reprinted in the recap/load output, where a reveal box would prime a leak; upcoming reveals are available on demand via 'mappa MSQ', 06 §B25).
- In ANY player-facing output: ZERO leaks.

*NOTE: the reveal timings below are INDICATIVE (by arc). The GM verifies the exact beat on the Roadmap (Ch. 5 and 08.1).*

### A) Soul / Divine / Cosmic
- AZEM and the group's 'soul-fragment' nature - **ShB/EW**
- Truth about HYDAELYN & ZODIARK: the WORLD cosmology (Zodiark & Hydaelyn's existence, the world sundered into THIRTEEN reflections, the Ascians' Rejoining) is revealed in **HW (3.2 - the Antitower / Minfilia-Hydaelyn)**, NOT gated to EW; only the deepest truths (Venat IS Hydaelyn; the Ancients / Amaurot - **ShB**; the Final Days & Meteion - **EW**) remain later reveals
- Soul split into 14 (the Sundering, the Sea of Stars, the soul/reincarnation cycle) - **ShB/EW**
- DYNAMIS (energy moved by emotion, distinct from aether) - **EW (Ultima Thule)**
- True nature of PRIMALS (not Gods, but mental constructs born of prayer and a sea of aether) - **ARR (progressive)**

### B) Ascians & secret identities
- EMET-SELCH / the Unsundered Ascians / AMAUROT - **ShB**
- True nature of ELIDIBUS (last original Ascian; living Primal, heart of Zodiark) - **SB -> ShB (full in 5.x)**
- Identity of the CRYSTAL EXARCH = G'RAHA TIA (from an alternate future) - **ShB**
- Nature of the FIRST / the LIGHTWARDENS / the WARRIOR OF DARKNESS - **ShB**

### C) Betrayals & political twists
- Betrayal of the CRYSTAL BRAVES: coup in Ul'dah, the Warrior of Light accused of regicide, Raubahn's arm - **end of 2.55 (ARR->HW)**
- ILBERD and the GRIFFIN: sacrificing his own men to summon SHINRYU - **end of HW patches (3.5)**

### D) Deaths & rebirths
- Sacrifice of HAURCHEFANT (the broken shield, at the Vault) - **HW (3.x)**
- Sacrifice of PAPALYMO (seals Shinryu with Louisoix's spell) - **end of HW / start of SB**
- Fate of MINFILIA (Word of the Mother; dissolves into the First to make way for RYNE) - **HW -> ShB**
- ZENOS's 'death' and return (the suicide at the end of Stormblood; the return in a host body and then his own) - **SB**

### E) Dragons & ancient secrets
- Truth about the DRAGONSONG WAR: a war born of King Thordan I's betrayal and murder of RATATOSKR to steal her eyes - **HW**
- True form of SHINRYU and BAHAMUT: the Bahamut trapped in Dalamud was only a Primal simulacrum born of TIAMAT's grief - **HW (Azys Lla / Coil)**

## 1.7 Premise to Session 0 (the imprint of the first save)
- SESSION 0 imprints the starting state the real campaign begins from: this is where the Memory Sheet's FIRST SAVE is born (Ch. 19).
- What Session 0 fixes (operational detail in Ch. 2):
  - starting city-state and each PC's initial hook;
  - party composition (Job, no class duplicates - Ch. 3);
  - shared tone and expectations (this chapter);
  - the MSQ 'point zero' (lvl 1, the Echo awakens - Ch. 4/5).
- At the end of Session 0 the FIRST Memory Sheet is compiled (LEAN [A]-[C]): MSQ Position = start of ARR; Level = 1; active subquest = none. Crystals/Blessing are NOT a save field (none yet anyway — player-managed, announced in play); reveal state is DERIVED from the MSQ position (Ch. 19.3), not stored. Continuity starts there. ORDERING (binding): compile the first save as the LAST step of Session 0 — ONLY after the PCs (race/Job) and the starting city are defined and backgrounds built; NEVER write it earlier with party/city still 'da definire'. Session 0 ENDS with this save (STOP): the shared-Echo campaign opening is NOT played now - it is the first beat of the NEXT, separate session (loaded from save-0).

---

### ARR CAMPAIGN OPENING — per Starting City (canon-accurate) [v1.18]
> **RAG NOTE (binding):** this OPENING is NOT part of Session 0 (which is setup-only, NO play - Ch.2) and is NEVER narrated during Session 0. It is the FIRST beat of the NEXT, SEPARATE play session: Session 0 ENDS by writing the first Memory Sheet (save-0: MSQ = start of ARR = 'Coming to <City>', the opening still to be played; PCs/race/Job + starting city + backgrounds set; Ch.19) and STOPS there. The shared-Echo opening is then played on the first 'continua' after save-0 is loaded (a later sitting).

*(Naming: this section uses ENGLISH canonical names as SOURCE DATA; the Italian rendering is applied at OUTPUT via 07 (Glossary) — do NOT hard-code Italian here, 07 is the single source. Do NOT cite any quest/mission LEVEL: it would be confused with the party's milestone level. Reference MSQ beats by NAME + sequence only.)*

**BINDING FRAME (all cities):**
- The party is a GROUP of **Warriors of Light (plural)** — CANON: Eorzeans remember the Calamity's saviours only as several silhouettes of light, names and faces forgotten (cf. Mother Miounne's account). NEVER narrate the campaign as a single hero; every vision, scene, choice and reward addresses ALL PCs.
- **COLD-OPEN on the arrival journey.** During the trip the **Echo / Hydaelyn's blessing** strikes **all PCs at once**. CANON VISION (verified): a **star-shower falling from a burning SKY** dissolves into a warm, blinding light and a crystalline entity (the Mothercrystal); a maternal voice sounds in their minds, in unison — the 'Hear... Feel... Think...' blessing (fixed Italian PLURAL in 07 G27). **IMPORTANT: NO burning dragon in this vision** — the burning-dragon (Bahamut) imagery belongs to the CALAMITY cinematic/backstory, NOT the personal Echo/Hydaelyn blessing. GM-only: the entity is Hydaelyn; keep it a mystery (Eco: non ancora rivelato).
- The PCs are **STRANGERS**; the shared vision is the bond (they exchange a look and realise they all saw the same thing). Personal motives stay individual; the Echo is the collective thread that turns strangers into a party.
- After the vision → arrival → register at the **Adventurers' Guild** with the city hub NPC → first local task = the hook.

**LIMSA LOMINSA** (La Noscea)
- Arrival: by **ship/ferry**; canonically the ship is **assaulted by pirates** mid-voyage. Met by the **Yellowjackets**.
- Guild hub: **The Drowning Wench** — master **Baderon**.
- MSQ opening: **Coming to Limsa Lominsa** → **Close to Home** (full ordered chain in 08.2).

**GRIDANIA** (Black Shroud)
- Arrival: by **carriage** through the forest into **New Gridania**. Met by a **Wood Wailer** (Bertennant).
- Guild hub: **The Carline Canopy** — master **Mother Miounne**.
- MSQ opening: **Coming to Gridania** → **Close to Home** (full ordered chain in 08.2).

**UL'DAH** (Thanalan)
- Arrival: by **carriage across the desert** into **Ul'dah – Steps of Nald**. Met by **Wymond**.
- Guild hub: **The Quicksand** — master **Momodi**.
- MSQ opening: **Coming to Ul'dah** → **Close to Home** (full ordered chain in 08.2).

**CONVERGENCE (the 3 paths merge):**
- The three openings run in PARALLEL (each city its own MSQ + hub).
- The home city then sends the party as envoys — **The Lominsan Envoy / The Gridanian Envoy / The Ul'dahn Envoy** — to the other two city-states.
- The paths FULLY MERGE at **The Scions of the Seventh Dawn** (+ the Grand Company quest **The Company You Keep**). From that beat the MSQ is UNIFIED; the save's MSQ line becomes shared.
- Rule: keep [A] city-specific until the Scions beat, then switch to the unified MSQ track. Reference the transition by beat NAME, never by level.

## 1.8 Cross-references
- Session 0 operational setup: Ch. 2.
- Character Creation / Job: Ch. 3.
- Reveal timing (derived from the MSQ position, not a stored tracker) and saves: Ch. 19.
- MSQ roadmap and reveal timings: Ch. 5 and 08.1.

# CHAPTER 2 — SESSION 0 SETUP
**PURPOSE:** Session 0 is NOT a play session: it is the table's "tutorial". It serves to create the characters, build their backgrounds coherently with the world, explain all homebrew rules, and give players the base lore. Final goal: sheets ready, first save created, a group that knows HOW to play and WHY they travel together.

**SESSION 0 - MAP (RAG co-location, binding):** the Session-0 material is split across chapters - keep these co-dependencies in view wherever this is read: OPENING SCENE (cold-open + shared Echo vision, plural Warriors of Light, per-city arrival, convergence at 'The Scions of the Seventh Dawn') = **Ch.1.7 (ARR CAMPAIGN OPENING)**; SETUP + rules tutorial = this chapter (2.1-2.3); BACKGROUNDS with the assistant = 2.2; BASE STARTING LORE package (delivered IN FULL, never condensed) = **2.6**; character mechanics + Job change = **Ch.3 / 3.4**; the FIRST SAVE is written **LAST**, only after PCs + city + backgrounds are done = **Ch.1.7 / Ch.19**; the **WIPE mechanic is kept SECRET** at Session 0 = **2.3**.

## 2.1 Session 0 ground rules
- No combat and no "real" plot: preparation only.
- All PCs start from the SAME city-state (single group hook).
- Recommended composition: at least 1 TANK + 1 HEALER in the party.
- No Job duplicates in the party (only one Paladin, one White Mage, etc.).
- At the end of the evening the FIRST SAVE is created (see Ch. 19 - Memory Sheet).

## 2.2 Building backgrounds (together, via the assistant)
Backgrounds are NOT written alone at home: they are built TOGETHER at the table, using the assistant as a lore reference.

**Recommended procedure:**
1. Each player proposes a starting idea (origin, race, trade, dream, wound).
2. The GM passes the idea to the assistant asking for consistency with: the chosen race and its culture, the starting city-state, the current era (post-Calamity).
3. The assistant returns: a coherent name (see Naming Appendix), a plausible birthplace, hooks to NPCs/factions, and any narrative hooks usable in the campaign.
4. Refine together until the player is satisfied.

**Rules on backgrounds:**
- Must stay within "common knowledge" (see Spoiler Policy, Ch. 1): no PC is born already aware of the great mysteries.
- No origins that spoil or skip MSQ arcs.
- Prefer simple, personal wounds/goals: they give the GM hooks.
- The GM notes every hook to reuse in subquests (Ch. 13).

## 2.3 Explaining all homebrew rules (the "tutorial")
Summary to read at the table:
- **Score generation:** Standard Array only (15, 14, 13, 12, 10, 8). No point-buy, no dice rolling.
- **Job and Job change:** you start as a full Job from level 1. Changing Job is RARE and EARNED — you must complete a mini-subquest to obtain the new Job's Soul Crystal (GM discretion, allowed only if it fits the current MSQ point and the Job's unlock quest is lore-reachable); it happens in town, out of combat, keeping your level; you CANNOT revert or swap again without a new subquest. No Job duplicates in the party. No classic multiclassing.
- **Milestone progression:** no XP. You level up when the story dictates (see Ch. 5).
- **The trinity and roles:**
  - TANK: holds aggro, protects the party, activates defenses.
  - HEALER: heals, gets Downed allies back up (Raise), supports.
  - DPS: deals damage; physical (focused strike) or magical (AoE).
- **Telegraphed combat and boss mechanics:** enemies, especially bosses, use mechanics announced the round before (telegraph). They must be recognized and handled: ignoring them leads to Enrage/Wipe (see Ch. 9).
- **Out of Combat / Raise / Wipe (videogame-style death):**
  - 0 HP = Out of Combat (Downed), not death.
  - Normal healing does NOT get a Downed up: you need Raise (Healer ability) or an item (Phoenix Down/Tail).
  - After revive: Aether Sickness (damage/healing halved, for 2 turns).
  - All Downed = WIPE — **KEEP THIS SECRET AT SESSION 0**: do NOT explain the all-party-down reset nor the Echo-premonition rewind to players now; reveal it only the FIRST time it triggers in play, for suspense. (GM rules: the encounter resets, spent consumables stay spent, justified as an Echo premonition; full details in Ch. 18.)
- **Limit Break:** a SHARED party bar 0-3, rises with natural 20s. Outside a BOSS fight the bar CANNOT pass the 2nd segment (LB1/LB2 only); the 3rd segment and LB3 charge ONLY in a boss fight. It EMPTIES completely on any Short or Long Rest and on any travel (Aetheryte or other transport) — it is combat charge that dissipates when you stop fighting. Effect by role, original names for each Job (see Ch. 6).
- **Pace:** one subquest at a time, exploratory pace, high MSQ fidelity (see Ch. 13 and Ch. 5).

## 2.4 FFXIV-knowledge survey + anti-spoiler pact
Direct question at the start of the evening: "Who already knows the FFXIV story, and how much?"
- Helps the GM calibrate pace and clues.
- **Table pact:** those who know the plot do NOT anticipate, do NOT metagame, do NOT spoil. Discovery is half the fun.
- PCs "know" only what is common knowledge: the great mysteries remain to be discovered in play.

## 2.5 Practical table tools
- **Memory Sheet (the "save"):** where and how the WORLD/MSQ state is saved (LEAN, sections [A]-[C]: MSQ position, party level, active subquest). It does NOT store the players' inventory nor the crystals/Blessing (player-managed; crystals announced in play, 06 §B23). See Ch. 19.
- **Combat tracker:** the assistant first gives a TEXT PREVIEW (initiative/AC/HP of monsters), then on "/tracker" an editable tracker with stat blocks and mechanics; PCs roll their own initiative and the GM integrates it. For each encounter the system provides the monsters' abilities and dice.
- **Requests to the assistant:** for deeper detail and descriptions, the GM queries the assistant via prompts during or between sessions (see 2.7).

## 2.6 "Base Starting Lore" package (common knowledge)
*[ Designed to be copied and handed to players. Contains ONLY what a PC can know without having traveled the world. Anything gated is NOT included. ]*
- MUST INCLUDE ALL of the following (never drop one, never condense): the WORLD; the 3 CITY-STATES with flavour; the CALAMITY; the THREATS (Garlean magitek/ceruleum, Allagan ruins, Primals & beast tribes/Temper); DAILY LIFE & TOOLS (Aetheryte, Gil, Adventurers' Guild, Grand Companies); and WHAT PCs do NOT know.

**The world: Hydaelyn / Eorzea**
- You live in EORZEA, a region of the world of Hydaelyn.
- Three great CITY-STATES dominate the region:
  - **GRIDANIA** (in the Black Shroud) - a forest city in (uneasy) harmony with the Elementals, guided by the Seedseers; home of archers, lancers and conjurers.
  - **LIMSA LOMINSA** (in La Noscea) - a port thalassocracy of islands linked by white bridges, ruled by the Admiral; sailors, merchants, fishers and (unofficially) reformed pirates; famed sea gladiators.
  - **UL'DAH** (in Thanalan) - an opulent mercantile/financial city in the desert, marked by stark inequality; power split between the Sultana and the Syndicate (the merchant council); famed gladiator arenas.

**Recent history (what everyone knows)**
- **The Calamity / Seventh Umbral Era:** a few years ago the Garlean Empire's Meteor Project brought down the lesser moon DALAMUD, which proved to be the prison of the Elder dragon BAHAMUT; his fury devastated Eorzea before he vanished. The world is still recovering from that catastrophe.

**Known threats**
- **The Garlean Empire:** a technological and military power to the north, a looming invasion threat. Their MAGITEK technology runs on CERULEUM (liquid aetheric fuel).
- **Allagan ruins:** remnants of an ancient civilization (Third Astral Era), whose technology was based on direct aether manipulation via crystals - incomparably more advanced than modern Garlean magitek.
- **Primals & Beast Tribes:** some non-human tribes summon deities called PRIMALS (Ifrit, Titan, Garuda...) who drain the land's aether and ENTHRALL (in learned terms: "temper") their worshippers. Considered a grave threat.

**Daily life and tools**
- **Aetheryte:** great blue crystals in nearly every settlement, enabling fast, safe teleport between places already visited (the body is dematerialized and carried through the Lifestream). Ubiquitous and taken for granted.
- **Gil:** the currency. (1 Gil = 1 gp; smaller denominations = silver and bronze Gil.)
- **Adventurers' Guild:** where adventurers take jobs and find work.
- **Grand Companies:** the nations' military/civil organizations - the Maelstrom (Limsa Lominsa), the Order of the Twin Adder (Gridania), the Immortal Flames (Ul'dah) (hint: one can enlist later).

**What PCs do NOT know (Spoiler Policy)**
- The great plot mysteries, the true nature of the Echo, of the Crystals of Light and of the antagonists remain TO BE DISCOVERED in play.

## 2.7 Deep-dive questions (on request)
When a player wants to know more about a place, faction, culture or NPC within the limits of common knowledge, the GM passes the question to the assistant with a dedicated prompt and returns a more detailed description, always respecting the Spoiler Policy. Guiding principle: maximum useful information, zero spoilers.

## Session 0 end checklist
- [ ] FFXIV-knowledge survey done + anti-spoiler pact accepted
- [ ] Homebrew rules explained (Array, Job, milestone, trinity, telegraphs, KO/Raise + Aether Sickness [WIPE kept SECRET until it first triggers], Limit Break, pace)
- [ ] Sheets created with Standard Array, full Job from lvl 1
- [ ] Backgrounds built with the assistant and coherent with the world
- [ ] At least 1 Tank + 1 Healer in the party, no Job duplicates
- [ ] Everyone starts from the same city, group hook defined
- [ ] Base Lore package handed to players
- [ ] First SAVE created (Memory Sheet, Ch. 19)

# CHAPTER 3 — CHARACTER CREATION
**PURPOSE:** practical rules to build a PC consistent with the FFXIV x D&D 5e homebrew. Used during Session 0 (Ch. 2).

## 3.1 Ability score generation
- ONLY method: **STANDARD ARRAY -> 15, 14, 13, 12, 10, 8.**
- NO point-buy, NO dice rolling.
- Values are assigned freely to the six abilities, then racial bonuses apply (see 01_Races).
- *Reason:* equal footing among players and predictable encounter balance.

## 3.2 Playable races (the 8 "enlightened")
Only these 8 races are playable by PCs. The tribal races remain reserved for NPCs/monsters (see 01_Races and 04_Bestiary).
1. Hyur
2. Elezen
3. Lalafell
4. Miqo'te
5. Roegadyn
6. Au Ra
7. Hrothgar
8. Viera
Trait, subrace and name details: see file 01_Races (incl. Naming Appendix: Miqo'te / Roegadyn / Xaela / Garlean).

## 3.3 Choosing the Job (from level 1)
- You start as a FULL JOB from level 1: no intermediate "base class" phase. Follow the homebrew manual (02_Classes).
- AVAILABLE JOBS: 22 in total. The wide choice makes multiclassing pointless.
- NO classic MULTICLASSING: a PC is a single Job.
- NO DUPLICATES in the party: only one Paladin, one White Mage, etc.
- RECOMMENDED COMPOSITION: at least 1 TANK + 1 HEALER (see Ch. 2).

## 3.4 Job change (safety valve, rare — always EARNED via a Soul-Crystal subquest)
The Job change is NOT a daily mechanic and is NEVER automatic: it is a rare safety valve, always EARNED through play, at the GM's discretion.

**How it happens (always earned, always justified by lore):**
- The PC must complete a MINI-SUBQUEST to obtain that Job's SOUL CRYSTAL (the Job's real unlock quest, or an ad-hoc lore-coherent equivalent built on the character/context). Only then can the PC take up the new Job.
- NO free switching: once changed, the PC CANNOT revert nor swap again "on the fly". Every further change (including returning to a previous Job) requires ITS OWN new Soul-Crystal subquest.

**GM discretion (binding gate):** the change is allowed ONLY if the GM agrees AND both hold:
- it fits WHERE the party is in the MSQ (arc/level), and
- the target Job's unlock quest is LORE-REACHABLE from the party's current location/point (you cannot obtain a Soul Crystal whose quest lies in a zone/arc not yet accessible).
If either fails, the switch waits until it becomes reachable.

**Conditions (unchanged):**
- Takes place in TOWN, OUT OF COMBAT, via the SOUL CRYSTAL; you keep your current LEVEL.
- NO Job DUPLICATES in the party. With 22 Jobs there is always room to switch without overlapping other PCs.

*NOTE FOR THE GM:* treat the change as a small narrative EVENT (a subquest with its own hook), never a mere "respec".

## 3.5 Background
The background is built TOGETHER, with the assistant, during Session 0 (full procedure in Ch. 2.2). It must be coherent with race, home city and current era, and stay within common knowledge (Spoiler Policy, Ch. 1).

## 3.6 Equipment and starting Gil
- Starting equipment per the Job (see the class files).
- Starting Gil and currency/loot rules: see Ch. 12. Currency reminder: 1 Gil = 1 gp; smaller denominations = silver / bronze Gil.

## Character creation checklist
- [ ] Abilities assigned with Standard Array (15,14,13,12,10,8)
- [ ] Race chosen from the 8 playable + bonuses applied (01_Races)
- [ ] Job chosen (full from lvl 1), no duplicate in the party
- [ ] Party with at least 1 Tank + 1 Healer
- [ ] Coherent background built with the assistant (Ch. 2.2)
- [ ] Starting equipment and Gil assigned (Ch. 12)

# CHAPTER 4 — THE ECHO
> **TERMINOLOGY NOTE:** ENTHRALLED/ENTHRALLMENT (vulgar) = TEMPERED/TEMPERING (scientific) = Primal mind-domination (Asservito / Temprato; see SCHEMA NOTES).

**PURPOSE:** rules and lore of the gift of the ECHO, the throughline that binds the PCs to the MSQ and justifies several homebrew mechanics (visions, language comprehension, and the "rewind" on a Wipe). *Players are told ONLY what is perceivable in play.*

## 4.1 What the Echo is (perceivable base lore)
The Echo is a rare gift: those who possess it perceive "reverberations" of the aether permeating the world and people.
**Manifestations known to bearers:**
- Visions of memories and events (past and, sometimes, possible).
- Instinctive comprehension of languages never studied.
- An inner resistance to forces that would bend the mind.
All the party's PCs share this gift: it is why their paths intertwine with the world's great events (and with the Crystals of Light, Ch. 7).

## 4.2 MSQ-scripted visions
- At plot-prescribed moments, the Echo activates on its own and shows the PC (or PCs) a VISION: others' memories, distant events, key scenes.
- They are SCRIPTED by the GM: they advance the MSQ and deliver narrative information.
- The player receives them passively: no dice are rolled to get them.
- **Format:** use the "READ ALOUD" block + Layered Lore (Ch. 16) when the vision contains information that can be explored.

## 4.3 Voluntary invocation of the Echo (2 HD)
A PC can ATTEMPT to invoke the Echo deliberately (to seek a clue, read the past of a place/object, understand a scene).
- **Cost:** spend 2 HIT DICE (HD).
- Make a roll (DC at GM discretion based on difficulty/relevance).
- **SUCCESS:** the Echo grants a useful vision (the GM decides what to reveal, respecting the Spoiler Policy).
- **FAILURE:** nothing happens BUT the 2 HD are STILL SPENT, for the effort exerted.
*GM notes:* a precious but costly tool (HD also serve to heal); don't use it to skip whole plot stretches: it's an "assist", not a universal skeleton key.

## 4.4 Universal language comprehension
- The Echo lets bearers UNDERSTAND and be understood even by those who speak unknown languages.
- It is primarily a PLOT tool.
- **Limit:** it translates/understands, it does NOT automatically grant the interlocutor's trust or goodwill.

## 4.5 Resistance to Primal Enthrallment
- Echo bearers resist Primal ENTHRALLMENT: the mind-domination that bends and enslaves the exposed.
- In play: the PCs are NOT automatically enthralled when facing a Primal, unlike common mortals. This makes the party the only force able to fight certain enemies.
- It is still possible to suffer other effects (fear, aetheric damage, etc.): the safeguard concerns Primal Tempering specifically.
- PERMANENT & INNATE: this Echo-given protection is NOT the Blessing and is NEVER removed — even in Heavensward, when the Blessing is sealed, the PCs stay safe from Tempering (see Ch. 5.6 / 7.3).

## 4.6 The Echo and the "rewind" on a Wipe
Lore justification for the anti-Wipe mechanic (full rules in Ch. 18).
**Lore justification:**
- The Echo grants visions not only of the past, but sometimes of POSSIBLE FUTURES: premonitions.
- When the party heads toward defeat (all Downed = Wipe), what the PCs just "lived" turns out to be a PREMONITORY VISION granted by the Echo.
- The bearer "comes to" at the start of the encounter, shaken and FOREWARNED. The fight restarts: now the PCs know what awaits them.
**What stays / what resets:**
- The encounter resets (positions, PC and enemy HP, mechanics).
- Spent consumables are NOT recovered.
- Precise mechanical details: see Ch. 18.
**Tone at the table:** don't trivialize it. The premonition is an intense, distressing experience, not a convenient "continue".

# CHAPTER 5 — MILESTONE PROGRESSION

Values and placements are TUNABLE; the narrative backbone follows the official MSQ; the levels are a compression of the game's 1-90 scale onto the table's 1-20.

> **SPOILER POLICY:** some names/truths are END-GAME REVEALS, enclosed in SPOILER (GM ONLY) boxes. In particular the name 'AZEM'.

**CORNERSTONE PRINCIPLE:** difficulty comes from MECHANICS, not inflated stats. Monsters/bosses have fair, by-the-book stats for their CR. No 'item tax'.

## 5.1 Progression philosophy
- No XP. You level up upon reaching a NARRATIVE BEAT (milestone), decided by the GM.
- The party levels TOGETHER: all PCs at the same level.
- Pace: ARR is the longest and most granular slice; Endwalker is played entirely at cap (lvl 20).
- Job change: RARE and EARNED via a Soul-Crystal subquest, keeping level, at GM discretion and only if lore-reachable (Ch. 3.4); NO multiclassing and NO class duplicates (see Ch. 3).

*Minor adaptation (what is allowed):* moving info between two compatible NPCs, compressing a trip or an already-done briefing, rewording a dialogue. NOT allowed: changing WHO gives a quest at a key beat, adding dungeons/enemies/key items, anticipating a reveal, moving the destination or altering consequences, or relocating a scene's STAGING (WHERE it happens, WHO is present, the ORDER of events within a quest — staging follows the wiki step spine, it is NOT variable dressing). For allowed original color see 06 (A13). SCOPE OF THIS ADAPTATION (binding): 'moving info between compatible NPCs' and 'compressing a trip/briefing' cover ONLY minor connective glue — they must NEVER relocate a SUBSTANTIVE on-site scene or reveal onto a HUB NPC, nor delete the on-field beat at the destination. Info the party is meant to learn ON-SITE from field NPCs (e.g. the Sylph/Ramuh situation from Buscarron/Noraxia in the Black Shroud) is PLAYED there, not pre-narrated by the hub contact (e.g. Minfilia). PILLARS != BEATS: the Roadmap per-level bullets are MANDATORY-CONDITION checkpoints (constraints/guardrails), NOT a route nor the beat list; the flow is the actual MSQ quest chain followed IN ORDER step by step from the wiki, never skipping the connective story quests between pillars (08.1 PRACTICAL MSQ FLOW RULE).

## 5.2 Rests
- Short Rest / Long Rest: standard D&D 5e rules.
- The Limit Break bar EMPTIES on any Short or Long Rest, and on any travel (Aetheryte or other transport) — see Ch. 6.
- The GM may deny a Long Rest in narratively 'pressured' zones.

## 5.3 Level spread 1 -> 20 (ARR -> EW)
### A Realm Reborn (lvl 1-8)
- **L1** - Session 0; arrival in the starting city-state (Gridania / Limsa Lominsa / Ul'dah); first jobs; THE ECHO AWAKENS.
- **L2** - End of the city questline (boss: Serpent Reavers + masked mage / Ascian) -> CRYSTAL #1 WATER. Joining the Scions; first dungeons (Sastasha / Tam-Tara / Copperbell).
- **L3** - The three city-states; intermediate dungeons; tribal threats.
- **L4** - IFRIT (Bowl of Embers, Amalj'aa) -> CRYSTAL #2 FIRE. Then rescue of the Sylph elder FRIXIO from the THOUSAND MAWS OF TOTO-RAK dungeon -> CRYSTAL #3 LIGHTNING.
- **L5** - TITAN (The Navel, Kobold) -> CRYSTAL #4 EARTH.
- **L6** - Stone Vigil, defeat of the dragon ISGEBIND -> CRYSTAL #5 ICE; Garlemald escalation (Castrum, Cape Westwind).
- **L7** - GARUDA (Howling Eye, Ixal) -> CRYSTAL #6 WIND -> NOW YOU HAVE ALL 6 CRYSTALS. The ULTIMA WEAPON appears and ABSORBS the essences of Ifrit/Titan/Garuda. Assault on CASTRUM MERIDIANUM -> THE PRAETORIUM: the Blessing protects from Ultima; defeat of LAHABREA; Gaius.
- **L8** - Patch 2.x: Crystal Braves; Ishgard refugees. THE KEEPER OF THE LAKE (2.55): MIDGARDSORMR SEALS THE BLESSING (snuffs out the 6 crystals). Flight from the Banquet of Ul'dah. [GATE Crystal Tower by here, see 08.1.]

### Heavensward (lvl 9-12)
- **L9** - Ishgard; Dragonsong War; Azure Dragoon. WITHOUT THE BLESSING: defeated Ascians can't be permanently killed (they flee) and Hydaelyn's ward is gone; the ECHO still keeps the party Tempering-safe (see 5.6).
- **L10** - Estinien & Nidhogg; Trial Ravana/Bismarck. The crystals begin to RELIGHT; after Bismarck the Blessing returns 'at reduced intensity'.
- **L11** - Azys Lla: TIAMAT (penultimate crystal) -> defeat of the ASCIAN PRIME (Igeyorhm+Lahabrea) -> FULL BLESSING (Midgardsormr breaks the seal). Climax KING THORDAN.
- **L12** - Patch 3.x: reckoning with NIDHOGG (end of Heavensward).

### Stormblood (lvl 13-15)
- **L13** - Liberation of Doma and Ala Mhigo; Trial Susano/Lakshmi.
- **L14** - Zenos; SHINRYU; battle of Ala Mhigo.
- **L15** - TSUKUYOMI (end of Stormblood 4.x).

### Shadowbringers (lvl 16-19)
- **L16** - The First; Norvrandt; the Lightwardens; Trial TITANIA.
- **L17** - INNOCENCE; the Warrior of Darkness.
- **L18** - Emet-Selch; Amaurot.
- **L19** - HADES (end of Shadowbringers 5.x).

### Endwalker (lvl 20, cap)
- **L20** - Garlemald -> Sharlayan -> Thavnair -> the Moon -> Elpis -> Ultima Thule -> final confrontation with the ENDSINGER (Meteion). (Dawntrail EXCLUDED.)

## 5.4 The 6 Crystals of Light
The Warrior of Light receives 6 Crystals of Light - ONE PER ELEMENT - an exceptional thing. In the campaign they are SHARED by the whole party, bound by a SINGLE LIGHT.
| # | Element | Moment |
|---|---|---|
| 1 | WATER | city questline, boss Serpent Reavers + Ascian |
| 2 | FIRE | Ifrit, Bowl of Embers |
| 3 | LIGHTNING | rescue of Sylph Frixio, Thousand Maws of Toto-Rak |
| 4 | EARTH | Titan, The Navel |
| 5 | ICE | Isgebind, Stone Vigil |
| 6 | WIND | Garuda, Howling Eye |
*GM NOTE:* order VERIFIED. Fire (Ifrit) precedes Lightning. All 6 collected by the Ultima Weapon / The Praetorium.

> **>>> SPOILER (GM ONLY - DO NOT REVEAL/NAME BEFORE ShB/EW) <<<**
> The true nature of the group's 'shared bond' - and the identity of the legendary leader associated with that soul crystal (name: AZEM) - are END-GAME REVEALS (Shadowbringers / Endwalker). DO NOT name 'Azem' earlier: use neutral terms (a single Light, a common destiny). That soul crystal, in-game, serves to summon other heroes (Trust): here it is useless anyway, the party is already complete. At most an optional end-Endwalker lore cameo.

## 5.5 The Blessing of Light
**Synthetic Blessing state for saves/preview:**
- Before collecting all 6 Crystals in ARR: **incomplete / developing**, NOT sealed.
- After Garuda / before the Ultima Weapon: **complete / active**.
- After The Keeper of the Lake, when Midgardsormr snuffs the crystals: **sealed**.
- During Heavensward while the crystals relight: **recovering**.
- After Ascian Prime / Azys Lla: **fully restored / active**.

Passive party boon, active while you possess the crystals (NOTE: immunity to Tempering is NOT here — that is the ECHO's innate gift, Ch. 4.5/7.3):
- **SHATTER THE ASCIAN:** only with the Blessing does a defeated Ascian truly die; otherwise the soul flees and will return.
- **WARD AGAINST AETHERIAL CORRUPTION (Hydaelyn's aid):** withstand overwhelming aetheric forces — it is the Blessing that lets the party survive the Ultima Weapon's Ultima; NOT absolute.
- **PERCEIVE DARKNESS:** advantage to unmask disguised Ascians.
- **EXCEPTION:** the three Unsundered Ascians of the Source can bypass it.

## 5.6 Loss and recovery of the Blessing (Heavensward arc)
**LOSS (lvl 8 - The Keeper of the Lake, patch 2.55):** Midgardsormr seals the Blessing by snuffing the six crystals, as a test of the party's true worth.
**During the 'powerless' arc (lvl 9-10 approx.):**
- The ECHO still protects: the PCs are NEVER Tempered by a Primal (innate to the Echo, NOT the Blessing — Ch. 4.5/7.3).
- ASCIANS cannot be permanently killed: at the end of a fight a defeated Ascian's soul FLEES / dematerializes and will return.
- Hydaelyn's direct aid is gone; you rely on your own strength and your companions (the test of worth).
**Recovery (progressive):** the Blessing returns 'at reduced intensity' already after BISMARCK, then grows. At AZYS LLA the dialogue with TIAMAT relights the penultimate crystal; the LAST relights by defeating the ASCIAN PRIME (Igeyorhm + Lahabrea) — and it is the RESTORED Blessing that finally lets the party permanently destroy them: this is where Midgardsormr DEFINITIVELY breaks the seal -> FULL BLESSING, right BEFORE the climax with KING THORDAN.
**HW STAKES (canon — NOT a tempering wipe):** the threat without the Blessing is NARRATIVE-MECHANICAL, not tempering. A defeated ASCIAN ESCAPES and returns — the party cannot close that thread until the Blessing is restored — and they fight without Hydaelyn's ward. The ECHO keeps the party safe from Tempering throughout HW; there is NO enthrall-wipe move. Boss fights use the normal telegraph/counter combat (Ch. 9).

## 5.7 Cross-references to other chapters
- **RAISE** (Healer ability): from LEVEL 5; action, consumes a 3rd+ slot; brings a Downed to 1/4 HP + Aether Sickness. Detail Ch. 18.
- **PHOENIX DOWN** -> 1/2 HP; **PHOENIX TAIL** -> full HP (both Aether Sickness). Costs/rarity: Ch. 12.
- **AETHER SICKNESS** (post-revive): damage/healing HALVED, for 2 turns. See Ch. 18.
- **LIMIT BREAK** (bar 0-3; caps at segment 2 outside boss fights, LB3 only on Bosses; empties on any rest and on any travel): Ch. 6.
- The 6 Crystals as a narrative device for climaxes: Ch. 7.

# CHAPTER 6 — LIMIT BREAK
Official names verified. **PRINCIPLE:** the Limit Break is an epic but RARE burst (a shared resource that charges only with natural 20s). It must be satisfying without becoming a boss one-shot.

## 6.1 The Limit Break bar
- A SHARED bar for the whole party: from 0 to 3 SEGMENTS.
- **CHARGE:** +1 segment ONLY with a NATURAL 20 on an attack roll: when a PC lands a natural 20 (hitting), OR when a PC is hit by a natural 20 (enemy crit). Maximum +1 segment PER ROUND.
- **BOSS-GATED 3rd SEGMENT (binding):** outside a BOSS fight the bar CANNOT rise past the 2nd segment (only LB1/LB2 are ever available); the 3rd segment charges — and LB3 becomes usable — ONLY in a fight against a BOSS. Further natural 20s while at 2 segments simply do not overfill.
- **SPEND:** LB1 = 1 segment | LB2 = 2 segments | LB3 = 3 segments.
- LB3 is usable ONLY in a fight against a BOSS.
- **EMPTIES to 0 (binding):** after ANY Short Rest or Long Rest; after ANY travel (Aetheryte teleport or any other means of transport); and after a WIPE. RATIONALE: the Limit Break is a charge of COMBAT momentum — when the party stops fighting for a while (rest or travel) it dissipates; it is NOT a stored resource tracked between fights/sessions.

## 6.2 How it is used
- Using a Limit Break requires your FULL ACTION for the turn.
- You CANNOT MOVE that turn.
- Only one LB is activated at a time from the shared pool.

## 6.3 Effects by role
- **AREA PRINCIPLE - THE AREA SCALES WITH THE LB LEVEL:** LB1 = SMALL area, LB2 = MEDIUM area, LB3 = LARGE area. Applies to ALL LBs that act on an area or radius (Tank, Healer, Ranged DPS and Magical DPS): as the LB level rises, both the EFFECT AND the SIZE of the area/radius grow. Only Physical Melee DPS is an exception: it is SINGLE-TARGET and has NO area (does not scale in size).

**TANK - Protection (damage reduction for allies; the RADIUS scales with LB level: LB1 6 m | LB2 12 m | LB3 18 m):**
- LB1 (Shield Wall): damage taken -1/4 | for 1 round | allies within 6 m radius
- LB2 (Stronghold): damage taken -1/2 | for 1 round | allies within 12 m radius
- LB3 (per job): damage taken -3/4 | for 2 rounds | allies within 18 m radius [BOSS]

**HEALER - Healing (in max HP for allies; the RADIUS scales with LB level: LB1 6 m | LB2 12 m | LB3 18 m):**
- LB1 (Healing Wind): heals 1/4 of max HP | allies within 6 m radius
- LB2 (Breath of the Earth): heals 1/2 of max HP | allies within 12 m radius
- LB3 (per job): heals 3/4 of max HP to ALL allies within 18 m radius + RAISES the Downed (to 3/4 HP) WITHOUT Aether Sickness [BOSS] (the definitive wipe-saver)

**DPS - Damage (see table 6.4):**
- PHYSICAL MELEE: single target, AUTOMATIC hit (no attack roll), NO save. d12 dice. (No area: hits a single target at any LB level.)
- PHYSICAL RANGE: a LINE that SCALES with LB level (length x width) -> LB1 6 m x 1.5 m | LB2 12 m x 3 m | LB3 18 m x 4.5 m. Dexterity save HALVES. d10 dice.
- MAGICAL: a CIRCLE that SCALES with LB level -> LB1 radius 3 m | LB2 radius 6 m | LB3 radius 9 m. Dexterity save HALVES. d10 dice.
- *Why d10 and not d8:* since Range/Magical is halved by the save, with d8 the LB would deal LESS than a same-level Fireball. Melee stays d12 because it is single-target with an automatic hit (no save).
- Save DC = 8 + proficiency bonus + the job's key ability modifier. Damage type: themed to the job.

## 6.4 DPS damage table (dice rise every 4 levels)
| Level | LB1 | LB2 | LB3 (Boss) |
|---|---|---|---|
| 1-4 | 3 dice | 5 dice | 8 dice |
| 5-8 | 4 dice | 7 dice | 10 dice |
| 9-12 | 5 dice | 8 dice | 12 dice |
| 13-16 | 6 dice | 10 dice | 14 dice |
| 17-20 | 7 dice | 11 dice | 16 dice |

**Die type:** PHYSICAL MELEE = d12 | PHYSICAL RANGE and MAGICAL = d10
**Area (scales with LB level):** Physical Range = line 6/12/18 m long x 1.5/3/4.5 m wide (LB1/LB2/LB3) | Magical = circle radius 3/6/9 m (LB1/LB2/LB3) | Physical Melee = single target (no area).
**Support LB radius (scales with LB level):** Tank = radius 6/12/18 m (LB1/LB2/LB3) | Healer = radius 6/12/18 m (LB1/LB2/LB3).

**Average damage (reference):**
- MELEE d12 (single, no save): 1-4 ~20/33/52 | 5-8 ~26/46/65 | 9-12 ~33/52/78 | 13-16 ~39/65/91 | 17-20 ~46/72/104
- RANGE/MAGICAL d10 (AoE, Dex save halves): 1-4 ~17/28/44 | 5-8 ~22/39/55 | 9-12 ~28/44/66 | 13-16 ~33/55/77 | 17-20 ~39/61/88

## 6.5 Quick gain (reminder)
- Natural 20 to hit (PC) -> +1 segment (max 1/round)
- Natural 20 taken (enemy crit) -> +1 segment (max 1/round)
- No other charge source.

## 6.6 Balance simulation (real monsters)
**LB3 MELEE (single target, average damage):**
| Tier | LB3 avg | Reference real boss (HP) | % HP |
|---|---|---|---|
| 1-4 | ~52 | Ettin CR4 (85) | ~61%* |
| 5-8 | ~65 | Frost Giant CR8 (138) | ~47% |
| 9-12 | ~78 | Adult White Dragon CR13 (200) | ~39% |
| 13-16 | ~91 | Adult Red Dragon CR17 (256) | ~36% |
| 17-20 | ~104 | Pit Fiend CR20 (300) | ~35% |
| 17-20 | ~104 | Ancient Red Dragon CR24 (546) | ~19% |
LB3 MAGICAL (AoE, save halves) - lvl 17-20: ~88 full / ~44 on a successful save, to all targets in the 9 m circle (LB3 area).

*(*) Campaign bosses are LEGENDARY/ELITE with inflated HP reserves vs the vanilla MM -> in practice LB3 ~ 35-45% of the boss at each tier. Conclusion: a powerful burst but NEVER a one-shot.*

## 6.7 Official names (LB1/LB2 shared per role - LB3 per Job)
**TANK** - LB1: Shield Wall | LB2: Stronghold
- LB3: Paladin (PLD) Last Bastion | Warrior (WAR) Land Waker | Dark Knight (DRK) Dark Force | Gunbreaker (GNB) Gunmetal Soul

**HEALER** - LB1: Healing Wind | LB2: Breath of the Earth
- LB3: White Mage (WHM) Pulse of Life | Scholar (SCH) Angel Feathers | Astrologian (AST) Astral Stasis | Sage (SGE) Techne Makre

**PHYSICAL MELEE** - LB1: Braver | LB2: Bladedance
- LB3: Monk (MNK) Final Heaven | Dragoon (DRG) Dragonsong Dive | Ninja (NIN) Chimatsuri | Samurai (SAM) Doom of the Living | Reaper (RPR) The End | (Viper: see 02_Classes)

**PHYSICAL RANGE** - LB1: Big Shot | LB2: Desperado
- LB3: Bard (BRD) Sagittarius Arrow | Machinist (MCH) Satellite Beam | Dancer (DNC) Crimson Lotus

**MAGICAL** - LB1: Skyshard | LB2: Starstorm
- LB3: Black Mage (BLM) Meteor | Summoner (SMN) Teraflare | Red Mage (RDM) Vermilion Scourge | (Pictomancer/Blue Mage: see 02_Classes)

# CHAPTER 7 — THE 6 CRYSTALS OF LIGHT
NARRATIVE SIDE of the crystals (the mechanical/chronological part is in Ch. 5).

> **SPOILER POLICY:** the name 'AZEM' is NEVER to be spoken before its canonical moment (ShB/EW).

## 7.1 What the Crystals of Light are
- They are tools through which HYDAELYN (the Mothercrystal) contacts those who possess the Echo and dispenses the BLESSING OF LIGHT.
- They are PROOF of being chosen as Hydaelyn's champions.
- The Warrior of Light receives SIX, one per ELEMENT: an EXCEPTIONAL fact - the other chosen usually receive only one.

*NOTE (canon vs campaign):* the "6 Crystals, one per element" scheme is THIS campaign's framework (homebrew). In canon the Warrior of Light receives Hydaelyn's Crystals of Light, but not with this exact element-per-Primal correspondence. Present it as a campaign setup, not as an FFXIV fact.

## 7.2 The shared soul (a single Light)
- In the campaign there is not a single Warrior of Light: there is a GROUP. A solution presentable to players FROM THE START: the party shares a SINGLE LIGHT, a COMMON DESTINY, a close bond through the Echo.
- The SIX crystals are SHARED and the Blessing covers ALL the PCs.
- **Narrative rendering:** when one touches a crystal-moment, they ALL feel it.
- **OPTIONAL (flavor):** the GM may assign each player a symbolic link to an element, with no mechanical effect.

> **>>> SPOILER (GM ONLY - DO NOT REVEAL/NAME BEFORE ShB/EW) <<<**
> The TRUE nature of this 'shared bond' is that the PCs are fragments of a single soul: that of the legendary leader AZEM. It is revealed in Shadowbringers / Endwalker (Emet-Selch, Amaurot, Elpis). IRON RULE: NEVER name 'Azem' (nor the 'soul-fragment' nature) before the reveal. Until then: 'a single Light', 'a common destiny', 'a bond through the Echo'.

## 7.3 Echo vs Blessing (important distinction for the GM)
**THE ECHO (innate, NEVER sealed):**
- Visions of the past/of others' memories, comprehension of all languages, 'out-of-time' intuitions.
- RESISTANCE TO TEMPERING: the Echo is what keeps a bearer from being enthralled by a Primal — the party's TRUE, PERMANENT safeguard, NEVER removed (they stay Tempering-safe even in HW when the Blessing is sealed).
- It is what makes the PCs 'special' regardless of the crystals.
**The Blessing of Light (from the crystals, CAN be sealed):**
- Allows ASCIANS to be permanently shattered (without it, a defeated Ascian flees and returns).
- WARD AGAINST AETHERIAL CORRUPTION / Hydaelyn's aid: withstand overwhelming aetheric forces (e.g. surviving the Ultima Weapon's Ultima); NOT absolute.
- Helps perceive/unmask darkness.
- Exception: the three Unsundered Ascians of the Source bypass it.
- It does NOT grant Tempering immunity — that is the ECHO's role (a common confusion; canon-aligned, wiki-verified).
*Principle:* the Echo (Tempering-safe) always remains; the Blessing (shatter Ascians + Hydaelyn's ward) is earned, can be lost (5.6) and reclaimed.

## 7.4 Staging each crystal
Each crystal must be a MOMENT, not a checkbox:
- Tie it to a FEAT just accomplished.
- Use a brief VISION/contact with Hydaelyn.
- Make it FEEL like growth (WITHOUT anticipating which - see 7.2).
**Summary of the six (chronology and levels: see Ch. 5):**
- #1 WATER - after the starting-city trial and the first Ascian: Hydaelyn's first voice.
- #2 FIRE - after Ifrit (Bowl of Embers): the Primal's fury tamed.
- #3 LIGHTNING - after rescuing the Sylph elder Frixio (Thousand Maws of Toto-Rak): a gift of gratitude.
- #4 EARTH - after Titan (The Navel): solidity won beneath the rock.
- #5 ICE - after Isgebind (Stone Vigil): the dragon's frost broken.
- #6 WIND - after Garuda (Howling Eye): the last piece, on the eve of the Ultima Weapon.

## 7.5 The crystals' emotional arc
1. **GATHERING (ARR):** the six in a crescendo; at the Ultima Weapon the Blessing protects -> peak of confidence.
2. **LOSS (end of ARR, Keeper of the Lake):** Midgardsormr SEALS them. A moment of bewilderment (mechanical consequences: 5.6).
3. **RECLAMATION (Heavensward):** one crystal relights with each great feat. Theme: 'you are not Hydaelyn's puppet, you are a hero on your own merit'. Full restoration before King Thordan.
4. **MATURITY (from Stormblood on):** the Blessing is 'always active'; the crystals remain the symbol of the bond with Hydaelyn up to the end-game confrontation (Hydaelyn) in Endwalker.

## 7.6 What the Blessing allows (recap)
- Shatter the Ascians | ward against aetherial corruption (Hydaelyn's aid) | perceive darkness. (Tempering immunity is the ECHO's, NOT the Blessing's — Ch. 4.5/7.3.)
- Detail: Ch. 5 (5.5) and Ch. 9.

## 7.7 Role hooks for players
- At GATHERING: a sense of being chosen, responsibility, wonder.
- At LOSS: vulnerability, doubt, the will to prove one's worth.
- At RECLAMATION: pride earned, not gifted.
- *(Never frame it as 'a fragment of [SPOILER]' in front of the players.)*

## 7.8 Cross-references
- Chronology, Blessing effects, loss/recovery: Ch. 5.
- ENTHRALLMENT mechanic in combat: Ch. 9.
- Invokable Echo / MSQ visions: Ch. 4.

# CHAPTER 8 — AETHERYTE TRAVEL
**PURPOSE:** rules for teleporting via Aetheryte.

## 8.1 How it works (lore)
AETHERYTES are great crystals that channel the world's aether and enable fast teleport between known locations.
- The traveler's body is DEMATERIALIZED into aether.
- The aether travels through the aetheric STREAM (the aethernet / the Lifestream).
- At the destination, the traveler is REMATERIALIZED at another Aetheryte.
A safe but taxing process for body and soul: hence the cost (8.3).

## 8.2 Reaching an Aetheryte (no attunement bookkeeping)
- You can teleport only to an Aetheryte the party has ALREADY VISITED at least once (adjudicated NARRATIVELY by the GM: "have they been here?"), with NO list to keep.
- There is NO attunement record to keep: neither the GM nor the save tracks it.
- In play the assistant FLAGS when an Aetheryte is present at a location (e.g. "Ul'dah (Eterite)") as a simple reminder of where one is (06 §B23).
- You cannot teleport to an Aetheryte never visited.

## 8.3 Teleport cost: 1 Hit Die (HD)
- Each Aetheryte teleport costs the traveler 1 HIT DIE (HD).
- Each PC pays their OWN HD (teleport is individual).
- A PC with 0 HD available CANNOT teleport: they must rest or travel conventionally.
- HD are recovered with rests (standard D&D 5e rules, see Ch. 5).
*GM NOTE (balance):* the HD cost eats into the party's healing reserve, so dose it.

## 8.4 When teleport is impossible (narrative blocks)
Always with coherent lore justification:
1. **No Aetheryte / inactive crystal:** frontier zones, dungeons; or an Aetheryte destroyed/off/dormant.
2. **Aetheric interference (unstable stream):** the network REFUSES the trip. Causes: Garlean technology/magitek and ceruleum; a Primal saturating the aether; Void corruption or aetheric anomalies.
3. **Sealed / besieged zones:** the local Aetheryte may be disabled or protected.
4. **World limits:** you cannot teleport between different worlds/planes with the ordinary network (e.g. between the Source and the First): a plot device is required.
**Practical effect:** the party must reach the destination conventionally -> chances for exploration and encounters (Ch. 13 and 10).

# CHAPTER 9 — DYNAMIC COMBAT
The core of gameplay: telegraphed FFXIV-style combat, where the challenge arises from READABLE, ALWAYS-AVOIDABLE mechanics, not from inflated stats nor from timers that kill regardless.

## 9.1 Philosophy
- Threats ARE SEEN COMING and are ALWAYS avoidable/manageable.
- Difficulty comes from MECHANICS, not stats: fair, by-the-book stats for the CR.
- Executing mechanics well -> the fight becomes easy (as it should).
- NO 'item tax'.

## 9.2 Initiative & Tracker
- The PLAYERS roll their own initiative; the GM slots the monsters into the order.
- The tracker maintains: initiative order + monster HP (managed by the GM).
- For each encounter the GM prepares the MONSTER SHEET: attacks, abilities, damage dice and mechanics.

## 9.3 Physical telegraph & reaction window
- Every important mechanic is ANNOUNCED with a credible PHYSICAL description (a fist rising, a deep breath, the ground cracking, a glow in a maw).
- **Golden rule - PROPORTIONATE warning:**
  - A MOVEMENT/positioning reaction: 1 ROUND of warning is enough.
  - A reaction requiring MULTIPLE ACTIONS (destroy a Heart, a structure, an add): a LONGER window.
- Correctly telegraphed + no reaction = a consequence, but AVOIDABLE for those who react.

## 9.4 Gradual introduction (learning curve)
1. First 'soft' appearance: low penalty, makes the pattern KNOWN.
2. Repetition: players learn to react.
3. Intensification/combination: the same mechanic returns stronger or interwoven.
Repetition builds the shared language with which the party 'reads' bosses.

## 9.5 Anatomy of a boss - 'Mechanics' template
MECHANICS FIDELITY (binding): for an MSQ/trial/dungeon boss, REPRODUCE the CURRENT (post-revamp) in-game fight's signature mechanics (named moves, telegraphs, phase changes, arena gimmicks) — verified on the wiki MAIN page (not a pre-revamp '/Old' version) — adapted to this framework; homebrew fills gaps only (06 §B10 / §A14).
Each boss lists, for each mechanic:
- **TRIGGER:** when it starts (round N or HP threshold, e.g. 50%).
- **TELEGRAPH:** the PHYSICAL description of the warning + how many rounds of warning.
- **THREAT:** what it does (damage/effect/area).
- **COUNTER:** how to avoid/neutralize it.
- **CONSEQUENCE (avoidable):** what happens if you do NOT react (NEVER an automatic wipe).

## 9.6 Mechanics toolbox (reusable, physically sensible)
- **Telegraphed AoE (physical):** Circle = localized impact; Cone = frontal sweep/breath; Line = charge/tail/beam. Counter: get out (1 round). Dexterity save halves.
- **Tank buster:** a huge blow on a single target. Counter: mitigation, the Tank's protection, positioning. Physical telegraph.
- **Knockback / push:** shoves toward REAL hazards (lava, chasm, wall). Counter: position beforehand, anchor yourself.
- **Weak point / Heart (one-time):** at an HP threshold the boss exposes a priority target with its own HP, to be destroyed within a WIDE window. If not destroyed: a strong punishing blow, but avoidable/survivable.
- **Adds / structures to destroy:** physical objects readable as 'to be destroyed' (boulders, crystals, totems, pillars, eggs). They have HP; within a window or they reinforce the boss.
- **Mounting pressure** (instead of the enrage-wipe): see 9.7.

## 9.7 Mounting pressure (NO wipe timer)
- There is NO clock that kills regardless.
- In its place: a REPEATABLE MECHANIC that returns at intervals and each time raises the stakes A LITTLE. It is always AVOIDABLE, but pushes you to close the fight.
- Difference from the HEART (9.6): the Heart is one-time; Mounting Pressure is recurring and scaling.
- *Example:* 'Tremors' that cover more ground with each repetition.

## 9.8 Threat / Aggro
- No numeric enmity system: target management is ARBITRATED BY THE GM sensibly (who is most exposed, deals more damage, threatens more, is 'in the monster's face').
- The Tank draws attention with fiction-narrated actions (taunts, interceptions, interposing).

## 9.9 Practical example - Titan
*(Fair CR stats; the challenge is in the mechanics.)*
- **MOUNTAIN BUSTER (tank buster):** Recurring trigger. Telegraph: Titan clenches a giant fist and raises it over the nearest target (1 round). Threat: a devastating single blow. Counter: the Tank's mitigation/protection; the toughest interposes.
- **WEIGHT OF THE LAND (ground AoE):** Recurring trigger. Telegraph: the ground CRACKS in several spots (1 round). Threat: rock eruptions. Counter: move off the cracks. Dexterity save halves.
- **LANDSLIDE (cone + push):** Recurring trigger. Telegraph: Titan draws back his forearm for a frontal sweep (1 round). Threat: frontal cone with strong KNOCKBACK. Counter: leave the cone or anchor yourself; mind the edges/cliffs.
- **TITAN'S HEART (weak point, ONE-TIME):** Trigger at 50% HP. Telegraph: the chest opens and reveals a pulsing CORE (a WIDE window, multiple rounds). Threat: if the Heart stays intact, it unleashes EARTHEN FURY (an arena-wide blow). Counter: destroy the Heart within the window. If not in time: the Fury hits but is SURVIVABLE, NOT an automatic wipe.
- **TREMORS (mounting pressure):** Trigger at intervals after the Heart phase. Telegraph: the ground shakes ever more strongly. Threat: an area damage covering MORE ground each repetition. Counter: move to safe zones; pushes you to close the fight.

## 9.10 Cross-references
- TEMPERING: the PCs are Tempering-safe via the ECHO (Ch. 4.5/7.3); without the Blessing, defeated Ascians escape and return (Ch. 5.6) — there is NO tempering-wipe mechanic.
- WIPE / Out of Combat / Raise: Ch. 18.
- LIMIT BREAK in combat: Ch. 6.
- Location-consistent monsters / base-manual reskins: Ch. 10 and Bestiary (04).

# CHAPTER 10 — BALANCE & ENCOUNTER BUILDING
**PURPOSE:** build balanced encounters with the standard D&D 5e engine (XP thresholds + multipliers) and structure the four contexts: Open Area, Plot Battles, Dungeons, Trials.

> OUTPUT NOTE: the XP tables, multipliers and difficulty labels in this chapter are an INTERNAL GM tool. The assistant uses them to size encounters but must NEVER show them in output: only final values are presented. See 06 (A1 and A16). The tables follow the DMG 2014 (see 06 B6).

## 10.1 Cornerstone principle (restated from Ch. 5)
- Difficulty comes from MECHANICS, not inflated stats.
- Monsters and bosses have FAIR, BY-THE-BOOK stats for their CR. (The ONLY allowed deviation: elite/legendary bosses may carry a larger HP reserve — see Ch. 6.6 and 06 §B6 — while attack bonus, damage/round and save DC stay strictly WITHIN the CR band.)
- Mechanics executed well -> a manageable fight; ignored -> escalation up to Enrage / a Wipe blow (Ch. 9).
- No "item tax".

## 10.2 Encounter budget (D&D 5e engine) - applies to EVERY fight
**Steps:**
1. Sum the individual PCs' XP THRESHOLDS (10.2a) for the group budget.
2. Choose the monsters; sum their XP (10.2c).
3. Apply the MULTIPLIER for count (10.2b).
4. Compare the 'adjusted' total with the group's thresholds.

### 10.2a XP thresholds per character (by level)
| Lvl | Easy | Medium | Hard | Deadly |
|---|---|---|---|---|
| 1 | 25 | 50 | 75 | 100 |
| 2 | 50 | 100 | 150 | 200 |
| 3 | 75 | 150 | 225 | 400 |
| 4 | 125 | 250 | 375 | 500 |
| 5 | 250 | 500 | 750 | 1100 |
| 6 | 300 | 600 | 900 | 1400 |
| 7 | 350 | 750 | 1100 | 1700 |
| 8 | 450 | 900 | 1400 | 2100 |
| 9 | 550 | 1100 | 1600 | 2400 |
| 10 | 600 | 1200 | 1900 | 2800 |
| 11 | 800 | 1600 | 2400 | 3600 |
| 12 | 1000 | 2000 | 3000 | 4500 |
| 13 | 1100 | 2200 | 3400 | 5100 |
| 14 | 1250 | 2500 | 3800 | 5700 |
| 15 | 1400 | 2800 | 4300 | 6400 |
| 16 | 1600 | 3200 | 4800 | 7200 |
| 17 | 2000 | 3900 | 5900 | 8800 |
| 18 | 2100 | 4200 | 6300 | 9500 |
| 19 | 2400 | 4900 | 7300 | 10900 |
| 20 | 2800 | 5700 | 8500 | 12700 |
*(The group budget = sum of individual thresholds at the chosen column.)*

### 10.2b Multiplier by number of monsters
| Monsters | Multiplier |
|---|---|
| 1 | x1 |
| 2 | x1.5 |
| 3-6 | x2 |
| 7-10 | x2.5 |
| 11-14 | x3 |
| 15+ | x4 |
*(Count the ACTUAL number of enemies, even weak ones.)*

### 10.2c XP by Challenge Rating (quick reference)
`CR 0=10 | 1/8=25 | 1/4=50 | 1/2=100 | 1=200 | 2=450 | 3=700 | 4=1100 | 5=1800 | 6=2300 | 7=2900 | 8=3900 | 9=5000 | 10=5900 | 11=7200 | 12=8400 | 13=10000 | 14=11500 | 15=13000 | 16=15000 | 17=18000 | 18=20000 | 19=22000 | 20=25000 | 21=33000 | 22=41000 | 23=50000 | 24=62000`

## 10.3 Adapting to party size
- **Small group (fewer than 3 PCs):** use the NEXT HIGHER multiplier COLUMN (10.2b).
- **Large group (6 or more PCs):** use the PREVIOUS lower column.
**Practical levers to retune (in order):**
1. NUMBER of mobs (add/remove minions).
2. CR of mobs / mini-bosses (step up or down).
3. Boss HP / its mechanics' thresholds.
Always keep 'by-the-book' stats: change QUANTITY and CR, do not inflate a single enemy's numbers.

## 10.4 Open-area encounters (exploration)
- **WANDERING MOBS:** zone-consistent enemies; usually Easy/Medium, quick. They erode resources.
- **AMBUSHES IN TRAVEL AND AT REST:** ambushes during movement or a rest (especially when teleport is blocked, Ch. 8).
- **Guidelines:** LEAN fights; target Easy/Medium; a good chance for subquest hooks (Ch. 13) and resource consumption before a dungeon/boss.

## 10.5 Plot Battles (MSQ fights)
SCRIPTED MSQ fights, with a boss (or waves + boss), in a NORMAL zone.
- **Scripted by the plot:** mandatory to proceed.
- **Allied NPCs in the background:** they fight in the background, not as playable members (Trust removed, Ch. 17).
- **Mid-weight:** 1-2 key mechanics suffice.
- **Narrative safety:** tuned to be beatable; on defeat, Echo/premonition intervenes -> Wipe (Ch. 4 and 18).
- RETREATING VILLAIN (binding): if the named antagonist is scripted to FLEE/withdraw rather than be defeated, treat the fight as an EASY skirmish to REPEL — cap the villain well BELOW party level (small escort), NOT a party-level boss; it may return LATER as a proper CR = party-level boss in its OWN duty (06 §B10/§B11).
- Same calculation engine (10.2/10.3), typically a Hard target WHEN there is a real boss to defeat (a retreating-villain skirmish is EASY, above).

## 10.6 Dungeon structure (pure action)
Homebrew scheme (NO trash mobs): **MID-BOSS -> small INTERLUDE/ENIGMA -> MID-BOSS -> small INTERLUDE/ENIGMA -> FINAL BOSS** — a short non-combat beat SEPARATES EVERY PAIR of consecutive encounters, so a multi-boss dungeon NEVER plays as a boss-rush; a short dungeon (1 mid-boss + boss) still gets ONE beat between them, a long story dungeon keeps ALL its canonical mid-bosses (still no trash) with each pair spaced by an interlude. DELIVERY: the whole dungeon comes in the FEWEST COMPLETE chunks (never fight-by-fight, never condensed to fit; 06 §B12). Operational detail: 06 §B12 / §B20.
- MID-BOSS: a single statted enemy, ONE signature mechanic; CR = party level -2 (Easy-Normal, 06 §B11).
- INTERLUDE / ENIGMA (MANDATORY between every two CONSECUTIVE fights): a short non-combat beat that paces the dungeon — it sits AFTER one fight and BEFORE the next; two combat encounters are NEVER back-to-back, and an interlude is never merely stacked before the first fight. AT LEAST ONE is a real tangible puzzle — a CONCRETE, player-deducible solution (>=3 approaches + soft failure), NOT a die-roll-to-solve check (rolls give clues only) — reusing the dungeon's own gimmick if any (Ch. 16 / 06 §E1); the others may be lighter (an environmental/traversal challenge, a scouting/lore beat, a skill-check obstacle) — but a lighter interlude is STILL playable with concrete numbers: an explicit DC per approach + a soft failure (06 §A18/§B12), never a vague skill mention without a DC. NEVER A REAL FIGHT (binding): an interlude does NOT escalate into a combat encounter — on failure it costs at most LIGHT damage (a few HP) or a trivial complication, or AT MOST a 1-2 round trivial skirmish, and any creature in it gets an INLINE MINI-STAT (CA / PF / Attacco); NEVER an add-swarm, a full stat-block enemy or a boss-grade threat inside an interlude. BACKGROUND MOB = INTERLUDE (binding): a crowd of rank-and-file enemies present at a stage (a pirate camp, a cultist mob) is ATMOSPHERE by default — the party TRAVERSES it via a stealth / social / slip-through interlude (which doubles as the between-fights beat), and it becomes a real fight ONLY if the roadmap stages one there or the players choose to engage (then scaled per 06 §B11). Keep each SHORT (a few minutes): it breaks the rhythm between fights, never pads.
- FINAL BOSS: a full-mechanics fight; CR = party level, difficulty from telegraphs + phase longevity, offense in band (Ch. 9 / 06 §B11).
- Every encounter gets a full stat block; deliver the dungeon COMPLETE (06 §B12).
- Brisk pace; Short Rests between encounters are the breather. The GM may deny the Long Rest inside the dungeon.

## 10.7 Trial structure (single boss with mechanics)
A SINGLE-BOSS fight, AS FAITHFUL AS POSSIBLE to the original.
- A single great opponent, possibly with summoned adds.
- The MECHANICS are the heart: telegraphed the round before.
- Reconstruct the iconic phases (phase changes, signature moves, the changing 'arena').
- CR/HP tuned to express all phases without dragging (see Enrage, 10.8).

## 10.8 Enrage (avoidable in reasonable time)
- A timer (in rounds) or threshold past which the boss unleashes a devastating blow (potential Wipe).
- It serves to punish those who drag too long, NOT to set impossible traps.
- **Golden rule:** ALWAYS AVOIDABLE in REASONABLE time by a group that executes well. Tune it to the expected DPS, with margin.

## Encounter-building checklist (for the GM)
- [ ] Chosen the CONTEXT: open area / plot battle / dungeon / trial
- [ ] Calculated the group budget (sum of XP thresholds, tab. 10.2a)
- [ ] Chosen the target difficulty (Medium/Hard/Deadly)
- [ ] Summed monster XP + applied the count multiplier (10.2b)
- [ ] Adjusted for party size (10.3) if different from ~4 PCs
- [ ] Enemy stats 'by the book' for their CR (no inflation)
- [ ] Defined mechanics + telegraphs suited to the context (Ch. 9)
- [ ] Enrage (if boss/trial) tuned to the party's DPS, always avoidable

# CHAPTER 11 — [REMOVED]
Trust eliminated: allies fight ONLY in the background (see Ch. 10.5 and 17).

# CHAPTER 12 — REWARDS & LOOT
Costs and rarity are TUNABLE PROPOSALS. Consistent with the anti 'item tax' principle: items help, they are never mandatory to win.

## 12.1 Loot philosophy
- You level up at MILESTONES (Ch. 5): loot is NOT needed to progress in power. It is utility, safety, flavor and narrative reward.
- FFXIV flavor: names, descriptions and types consistent with the world.
- No 'item tax': a group without consumables, playing clean, must be able to win.
- ENVIRONMENTAL TREASURE = COLOUR, NOT A JACKPOT (binding): a described hoard / treasure-room / pile of coin (e.g. a pirate stash) is NARRATIVE colour — never a windfall that breaks the economy. Any pickup the party grabs = a SMALL, level-scaled Gil handful (per the §A21 CR/level bands in 06), not a lump sum; large value comes only from the beat's designed reward (Ch. 12.6) or a boss/elite drop, never from set-dressing loot.

## 12.2 Currency - Gil
- 1 Gil (gold) = 1 gold piece (gp) of D&D 5e. 1:1 conversion.
- **Minor currencies:** SILVER Gil = silver piece (1 gold Gil = 10 silver); BRONZE Gil = copper piece (1 silver = 10 bronze).
- Prices below are in GIL (= gp) unless otherwise noted.

## 12.3 Revival items (Phoenix)
Normal healing does NOT revive a Downed character (Ch. 18). You need Raise or the Phoenix items. All apply AETHER SICKNESS (damage/healing dice halved, 2 turns), EXCEPT the Healer LB3.
| Means | Restores to | Rarity | Indic. cost | Action |
|---|---|---|---|---|
| RAISE (Healer) | 1/4 HP | ability | -- (3rd+ slot) | Action |
| PHOENIX DOWN | 1/2 HP | UNCOMMON | ~150 Gil | Action |
| PHOENIX TAIL | full HP | RARE | ~1,000 Gil | Action |
| HEALER LB3 | 3/4 HP | -- (Ch. 6) | -- | Action |
**Design notes:**
- PHOENIX DOWN more accessible (Uncommon): a safety net, especially BEFORE lvl 5 (Healer without Raise).
- PHOENIX TAIL premium (Rare): a full revive; more a narrative reward than a market stall.
- No per-fight use limit, BUT: they burn on a WIPE (stay spent) and availability is regulated by the GM. Rarity is the real brake.
- PHOENIX DOWNS and TAILS are PURCHASED ONLY in shops: NOT craftable (Ch. 14).

## 12.4 FFXIV consumables
**Healing (themed 'Potions'):**
- Potion - heals 2d4+2 - Common - ~50 Gil
- High Potion - heals 4d4+4 - Uncommon - ~150 Gil
- Max Potion - heals 8d4+8 - Rare - ~500 Gil
- *(Potions do NOT revive the Downed.)*
**Magical resources (themed 'Ethers') - OPTIONAL:**
- Ether - recovers 1 slot up to 3rd lvl - Rare - ~300 Gil
- High Ether - recovers 1 slot up to 5th lvl - Very Rare - ~800 Gil

## 12.5 Equipment & Relics
- **FFXIV-branded GEAR:** themed weapons/armor from dungeons, bosses and merchants. LIGHT, optional mechanical bonuses (level comes from milestones).
- **RELIC WEAPONS:** rewards of long narrative chains (dedicated subquests, Ch. 13). They grow over several stages. Keep them RARE and memorable.
- Crafting/gathering materials: see Ch. 14.

## 12.6 Where rewards come from (and at what pace)
- **MSQ BEATS:** narrative rewards at key nodes.
- **DUNGEONS & BOSSES:** themed loot consistent with the location.
- **MERCHANTS / GRAND COMPANY (Ch. 17):** consumables and base gear. (Operational vendor/inn engine + loot-by-CR + buy-back: 06 §A20-A22.)
- **SUBQUESTS (Ch. 13):** relics, unique items, extra Gil.
- **Pace:** enough Gil for a REASONABLE stock, without hoarding Tails at will.

## 12.7 Cross-references
- Out of Combat / Raise / Aether Sickness / Wipe rules: Ch. 18.
- Healer LB3 (revive without Aether Sickness): Ch. 6.
- Crafting / Gathering: Ch. 14. Subquests and relics: Ch. 13. Merchants / Grand Company: Ch. 17.

# CHAPTER 13 — SUBQUESTS
Subquests are WELCOME: they enrich the world, explore lore and show places the MSQ doesn't touch. But they must be handled with consistency and fidelity.

## 13.1 Philosophy
- Exploring lore and seeing places off the main track is a good thing.
- Subquests are not 'filler': they are windows on the world, rooted where the party currently is.
- They remain optional and must not break the MSQ's pace.

## 13.2 Consistency with place
- A subquest must ARISE FROM WHERE THEY ARE: current zone, city, region and MSQ point reached.
- Consistent with: local NPCs, what they can do there, the current political/social situation.
- No out-of-context plots or places not accessible in the current arc.

## 13.3 Fidelity to sources (strong rule)
- Use REAL material AS MUCH AS POSSIBLE: correct NPC NAMES; real SIDE STORIES; canon LOCATIONS, factions, events.
- If suitable material is missing, BUILD it coherently with local lore (coherent reskins, Ch. 10 / 06), correct names and flavor.
- The GM VERIFIES sources before proposing: better a small, accurate subquest than a large, wrong one.

## 13.4 Proportionate rewards (to level AND lore)
- Sense relative to: the party's LEVEL; the quest's LORE (WHO gives it and WHY).
- **Economic consistency:** a commoner does not pay like a noble; a noble/guild/officer can offer value.
- Suitable rewards: reasonable Gil, consumables, coherent gear, relic stages, unique lore/access/contacts.
- Avoid 'broken' loot, absurd sums, out-of-scale items.

## 13.5 One subquest at a time
- Try NOT to have more than one subquest active at a time.
- CLOSE it (or suspend it clearly) before taking another. Only ONE active subquest fits the slot: to take another you must first finish or abandon it, and SWITCHING loses the previous one (no parked-leads list). Operational single-slot system + MSQ Bookmark: 06 (B22).

## 13.6 Continuity with the MSQ - 'MSQ Bookmark'
When the party takes a subquest, SAVE a BOOKMARK of the MSQ point:
- the current MSQ mission + last completed step (the return point), plus the active subquest's own progress; stored in save [C] (the MSQ point stays in [A]).
When the subquest ends, RETURN EXACTLY to that point. Full system in Ch. 19; operational bookmark/slot in 06 (B22).

## 13.7 Table procedure (step by step)
1. HOOK: a place-consistent prompt emerges (13.2/13.3).
2. CHOICE: the group decides whether to take it.
3. BOOKMARK: save the MSQ point (13.6).
4. PREPARATION: the GM verifies sources, sets NPCs/locations/monsters and a proportionate reward.
5. PLAY: it is played (dynamic combat as Ch. 9).
6. RESOLUTION / TURN-IN (a PLAYED beat, still ON_SUBQUEST): return to the COMMISSIONER (the NPC who gave the hook) at their location — or the canonical turn-in NPC if the quest structures it so — for the CLOSING SCENE + the REWARD (13.4). A subquest is NOT concluded at the objective; it concludes at this turn-in — never fold it straight into the MSQ nor reduce it to a one-line 'hand it in later'.
7. CLOSURE + RETURN: ONLY AFTER the turn-in the subquest ENDS (the slot clears); then resume the MSQ from the saved bookmark with a short re-hook. Operational lifecycle: 06 §B22.

## 13.8 Cross-references
- Full continuity/save: Ch. 19. Encounter building / reskin: Ch. 10 and 06. Economic value: Ch. 12. MSQ roadmap: 08.1 and Ch. 5.

# CHAPTER 14 — DOWNTIME / CRAFTING / GATHERING
Light, optional activities to do during stops.

## 14.1 The choice at rest
At each stop, each PC chooses ONE of two options:
- **A) LONG REST:** standard 5e rules (full recovery; EMPTIES the Limit Break bar, Ch. 6).
- **B) SHORT REST + 1 ACTIVITY:** the benefits of a Short Rest (spending HD), BUT NOT full recovery. In exchange, one activity among: GATHERING (14.2), CRAFTING (14.3), RESEARCH/STUDY (14.4).
**Opportunity cost:** the activity takes the time of the Long Rest. Ideal when you have little HP to recover and many HD. Each PC chooses for themselves. *(NOTE: a Short Rest EMPTIES the shared Limit Break bar too — as does any travel; see Ch. 6.)*

## 14.2 Gathering - ANYONE can do it
- The PC chooses the type: FISHING / MINING / BOTANY.
- Makes 1 GATHERING CHECK: d20 + mod (GM's choice).
- The value is recorded DIRECTLY IN GIL. Materials are NOT tracked.
| Roll | Quality | Value (Gil) |
|---|---|---|
| <= 9 | Common | ~5 |
| 10-14 | Uncommon | ~10 |
| 15-19 | Rare | ~25 |
| 20+ | Legendary | ~50 |
Income is deliberately LOW and consistent with Crafting: Gathering requires no skill, costs nothing and has no risk, so it yields LESS than Crafting.

## 14.3 Crafting - only those with the right skills
**What you can make:** Potions and other CONSUMABLES. NOT Phoenix Downs/Tails (shop only, Ch. 12).
**Procedure:**
1. The PC pays in GIL the COST OF RAW COMPONENTS.
2. Makes 1 CHECK with the right tools, DC by rarity (Common 12 / Uncommon 15 / Rare 18 / Very Rare 21).
3. SUCCESS -> obtains the item. FAILURE -> components (Gil) lost.
**Golden rule on prices (mandatory):** components ~= 25% of the shop price (~75% discount). Reason: crafting means you do NOT rest, you SPEND Gil and you RISK failing.
*Example:* Potion (shop 50) -> components ~12-13, DC 12.

## 14.4 Research / Study - ANYONE can do it
- The PC dedicates the stop to studying something (texts, rumors, clues).
- Makes 1 relevant CHECK (Investigation / History / Arcana / Nature).
- On success, the GM grants a LORE CLUE or a SUBQUEST HOOK (Ch. 13/16).

## 14.5 Consistency notes
- PHOENIX DOWNS / TAILS: NOT craftable, only purchasable (Ch. 12).
- Gathering does NOT feed Crafting (no tracked materials): Gathering gives Gil; Crafting spends Gil.
- Available activities = ONLY Gathering, Crafting, Research/Study.
- **DOWNTIME IS UNBOUND FROM /riposo:** the Gathering/Crafting/Research activities above are GM-run table options at any stop; they are NOT tied to a rest command and /riposo does NOT invoke them. The /riposo command (06 §B28) produces a LONG REST only.

## 14.6 Random Events: Travel & Camp (the shared roll)
One shared mechanic drives both the TRAVEL check (06 §B26 /viaggio) and the CAMP check of a LONG REST outdoors (06 §B28 /riposo). The short rest stays base 5e rules run by the GM (regain slots, spend HD), not assisted by /riposo.
- **DANGER RATING (a zone/route property; assistant sets, GM overrides):** derived from the settlement tier (06 §A22) + the zone threat (06 §B13), verified against the real zone (06 §A6). The SAME rating applies whether the party crosses the zone (/viaggio) or camps in it (/riposo):
  - **Tranquillo** — a safe road near a hub, settled/friendly territory (an urban camp trends here).
  - **Rischioso** — open wilderness, a contested border, unsettled land.
  - **Ostile** — a monster-infested zone, enemy territory, a cursed/pressured area.
- **ONE CHECK (single roll — light, per the campaign's table ethos):** 1d20 vs a threshold by rating (guideline, GM-tunable): Tranquillo event on ≤5 (25%) · Rischioso on ≤11 (55%) · Ostile on ≤16 (80%). On a hit → ONE event; on a miss → see the branch difference below.
- **THE GM ROLLS — THE ASSISTANT PRE-GENERATES BOTH BRANCHES IN ONE TURN (binding):** the assistant does NOT roll. It sets up the scene, states the danger rating + threshold ('tira 1d20, evento su ≤N'), and generates BOTH labelled outcomes in the SAME turn — '**Tiro ≤N (evento):** …' and '**Tiro >N (nessun evento):** …' — then the GM rolls a REAL d20 and plays/reads the matching branch. WHY (binding): the GM gets a genuinely random die (an LLM is a poor RNG), AND it costs ONE turn/message, not two — if the assistant stopped and waited for the result, resolving the chosen branch would need a SECOND turn that re-processes the whole context (a message against a capped plan). Both branches are ALWAYS present because a miss STILL has content (see below), so nothing is saved by omitting one. If the '≤N (evento)' branch is a combat, generate its stat block there (it is ready if the GM rolls into it).
- **EVENT MENU (on a hit — pick ONE, zone-consistent §B13/§A6, spanning good/neutral/bad, not only threats):** GOOD — a traveller who helps, a hidden cache, a merchant with a good deal; NEUTRAL — a vista, a minor NPC, a harmless meeting; BAD — an ambush, an NPC in peril, a fight, an environmental hazard. A combat event scales per §B11, loot per §A21. Never a mini-dungeon; one event only.
- **MISS DIFFERS BY BRANCH (binding):** at a CAMP a miss still yields a COLOUR event (a shared meal, a fireside confession, a distant light) — always something. On TRAVEL a miss yields an UNEVENTFUL passage — nothing happens, the journey simply passes.
- **WATCH ORDER (camp):** the party sets watches; whoever is on watch gains/suffers surprise on an ambush.
- **THE LONG REST ALWAYS COMPLETES (camp):** a resolved ambush does NOT cancel it — /riposo never denies the long rest (06 §B28; if the GM wants to deny it, they simply do not use the command). No exhaustion tracking (player-managed, like HD).
- Design references (structure, not verbatim): DMG "Random Encounters", OSR/Shadowdark watch-checks, the travel/camp procedures of published wilderness adventures.

# CHAPTER 15 — TAVERNS & GOSSIP
The tavern as a social hub between adventures: roleplay and flavor, a light rumor system, and the job board.

## 15.1 Function & tone
A place where the party gathers to breathe, talk, gather rumors and take jobs. Predominantly ROLEPLAY and FLAVOR.
Adventurers' Guild venues:
- **GRIDANIA** - The Carline Canopy
- **LIMSA LOMINSA** - The Drowning Wench
- **UL'DAH** - The Quicksand
Table weight: light. No tavern marathon sessions.

## 15.2 Gossip & rumors
When the party spends time in a tavern, it can "LISTEN IN". (OPERATIONAL NOTE: the rumour/hook system is NOT tavern-bound — it fires ON-DEMAND when the PCs seek info or socialise ANYWHERE near their current location, and the hook is ALWAYS-available, not gated behind the roll; full engine in 06 §B20.)
- 1 CHECK per visit: Persuasion/Performance (strike up a chat) or Investigation/Insight (eavesdrop).
- Buying a round (a small expense) grants ADVANTAGE.
**Rumor table (kept by the GM, by zone/arc):** TRUE (clue/hook), COLOR (atmosphere/minor lore), MISLEADING (a false lead, sparingly, never punishing).
| Roll | Result |
|---|---|
| <= 9 | 1 Color rumor |
| 10-14 | 1 Color + 1 True |
| 15-19 | 2 True (or 1 more detailed True) |
| 20+ | 2 True + an in-depth clue |
*Tie every TRUE rumor to something real (Ch. 13/16).*

## 15.3 Job board (Levequest style)
OPTIONAL JOBS, faithful to Levequests.
- **Types:** bounties, deliveries, escorts, notorious-monster hunts, recoveries.
- OPTIONAL SUBQUESTS (Ch. 13): usually 1-2 between arcs.
- LIGHT REWARDS: Gil + minor loot (Ch. 12).
- The GM rotates the jobs on each return to town.

## 15.4 Rest
- Base D&D 5e rules (Short / Long Rest). Sleeping in a tavern = a safe Long Rest.
- Downtime during stops: Ch. 14.

# CHAPTER 16 — LAYERED LORE & READ-ALOUD
Defines the FORMAT for presenting places, scenes, NPCs, objects and events: a base description for everyone + lore layers unlockable with checks + context reserved for the GM. Guiding principle: **MAXIMUM INFORMATION TO THE GM, zero spoilers to the players.**

## 16.1 Philosophy
- Every relevant scene is written on MULTIPLE LAYERS, from public to secret.
- Players first receive the base (read-aloud), then can DELVE DEEPER with checks.
- The GM always has ALL the context.
- SPOILER POLICY (Ch. 1): the high layers NEVER reveal gated mysteries.

## 16.2 The block format (template)
*(LAYOUT NOTE: the fenced box below is an ILLUSTRATIVE layout for reading here; in ACTUAL OUTPUT the assistant renders these blocks as NORMAL TEXT with bold labels — NEVER inside a code block, 06 §A1. Same for the worked example in 16.5. TWO DIFFERENT 'GM Info': this scene-lore 'GM INFO' box is NOT the per-beat continuity '[Info GM]' line of 06 §B1 — that one is a single continuity line that looks no further than the immediate next step. Neither ever prints a gated reveal or a forward spoiler in output; upcoming reveals are derived / on-demand via 'mappa MSQ', 06 §B25.)*
```
>>> READ ALOUD <<<
  [Base description, perceivable by ALL, to read aloud. No rolls.]

--- LAYERED LORE (on a check) ---
  [DC 10]  First-layer info (common knowledge, evident details).
  [DC 15]  Intermediate info (specialist knowledge, non-obvious links).
  [DC 20]  Advanced info (rare knowledge) - always WITHOUT spoilers beyond what is allowed.

[ GM INFO ]
  [Scene-relevant context FOR THE GM ONLY: what the players can uncover here and how the scene connects to what they are doing NOW. It STILL obeys the reveal-gate (Ch.1): a gated reveal is NEVER named even here, and it looks no further than the current scene. NOT revealed to players.]
```
**Usage notes:**
- The layers are CUMULATIVE: whoever beats DC 15 also gets the DC 10, etc.
- One roll per PC per scene/object (barring new elements). They can collaborate (help) per 5e rules.
- If no one reaches a threshold, that layer stays unrevealed (retryable with clues or with the Echo, Ch. 4).
- CONDITIONAL & DECOUPLED (operational): include Layered Lore ONLY when the scene has genuinely investigable lore (SKIP it in a pure action/ambush or pure briefing scene); it is INDEPENDENT of the NPC 'Dialogo e Interazione' block, and its ORDER FOLLOWS THE SCENE (lead with whatever the players engage first — Dialogo when opening on an NPC, Layered Lore after a vision/discovery to investigate); a single targeted check may replace the full CD 10/15/20 ladder. Full rule in 06 §B15.

## 16.3 Which check to roll - full map
The GM chooses the check suited to the lore's THEME.

**INTELLIGENCE**
- **ARCANA:** aether and aetheric flows; magic; the aetheric nature of PRIMALS; ALLAGAN technology/relics and magitek; the VOID and voidsent; aetherytes and crystals; curses; (gated) the nature of the Echo.
- **HISTORY:** historical events; the CALAMITY; wars (the Dragonsong War); nations and city-states; the ALLAG civilization; dynasties; ruins and artifacts; genealogies and treaties.
- **RELIGION:** the TWELVE; Primals as objects of worship; the ASCIANS and their cults; the undead; rites, symbols and sacred places; beliefs about the Lifestream.
- **NATURE:** ecology; flora and fauna; beasts and monstrosities; terrains, climate; plants and poisons; animal behavior; mounts (chocobos).
- **INVESTIGATION:** deducing from clues; mechanisms, traps and devices (incl. magitek); logical analysis of a scene; reconstructing a sequence of events.

**WISDOM**
- **PERCEPTION:** sensory details of the environment; catching presences.
- **INSIGHT:** intentions, emotions and lies; sensing spells or signs of Enthrallment; the 'unsaid'.
- **MEDICINE:** wounds, diseases, poisons, anatomy; cause/time of death; bodily signs of Enthrallment or corruption.
- **SURVIVAL:** tracks and pursuits; orientation; weather and terrain; foraging.

**CHARISMA** (social info gathering; ties to Ch. 15)
- **PERSUASION / DECEPTION / INTIMIDATION:** extracting information from NPCs.
- **PERFORMANCE:** folklore, songs, legends; engaging the common folk.

**STRENGTH / DEXTERITY** (rarely)
- **ATHLETICS / ACROBATICS:** judging the physical/structural difficulty of a path or obstacle.

**TOOLS**
- Artisan's tools (manufacture, materials, an artifact/weapon/armor's origin); thieves' tools (locks/mechanisms/traps); herbalism/poisoner's kit (plants, reagents, poisons); cartographer/navigator's tools (maps, routes, places); musical instruments (songs, ballads, folklore).

**Pure ability checks** (when no skill fits): pure INT (general culture), pure WIS (common sense/instinct), pure CHA (presence/social impact).

## 16.4 Contextual modifiers (background, Job, race, Echo)
The GM may grant 'free' info or ADVANTAGE based on who the character is:
- **Relevant background:** a PC whose past touches the theme gets a free lore layer or advantage.
- **Relevant Job:** e.g. a Machinist recognizes magitek; an Arcanist/Thaumaturge senses aetheric flows; a Conjurer/White Mage the curative or corrupted nature of aether.
- **Race / origin:** e.g. an Au Ra Xaela knows the Steppe; a native knows more about local customs.
- **The Echo (Ch. 4):** if rolls aren't enough, a PC can ATTEMPT the voluntary invocation (2 HD) for a vision revealing otherwise unreachable lore - spoiler-safe.

## 16.5 Worked example
*(Scene: the party enters a cavern where a Primal was summoned.)*
```
>>> READ ALOUD <<<
  The air vibrates with an unnatural heat. The rock walls are blackened and
  veined with glowing seams; at the center, a still-smoking heap of ash and
  the footprints of worshippers all around.

--- LAYERED LORE ---
  [DC 10 - Nature] The heat and the veins are not volcanic: something alive
    released an aetheric fire, recently.
  [DC 15 - Arcana] The zone's aether has been drained and channeled into a
    sentient fire: it is the signature of a fire PRIMAL.
  [DC 20 - Religion] The footprints and symbols belong to a tribal summoning
    rite; the faithful offered their own aether to call forth the deity.

[ GM INFO ]
  The Primal was just summoned and has already moved toward the village down
  the valley (hook: next Plot Battle, Ch. 10.5). An enthralled (Tempered)
  survivor is hidden at the back of the cavern and will attack if approached.
```

## 16.6 Cutscene adaptation (in-scene rail vs off-scene auto-surface)
FFXIV tells much of its story through cutscenes. Two kinds, handled differently; the OFF-SCENE ones are actually easier (closed, GM-facing content) — the IN-SCENE rail is where discipline matters most.

**PLACEMENT (where the cutscene goes) [v1.23]:** reproduce a cutscene at its CANONICAL narrative position. Some dungeons INTERLEAVE long cutscenes BETWEEN encounters (tag each at the transition); others land the story at the END of the dungeon/trial. Follow canon: never force all-at-end nor all-mid, never invent one. A `[CUTSCENE IN SCENA]` may be a beat HEADER or an interleaved SUB-BLOCK. (General heuristic.)

**IN-SCENE CUTSCENE (the PCs ARE present) — a RAILED story beat:**
- Deliver the content and REACH the canonical outcome; the scene's spine is FIXED (Ch. 5.1 / the Roadmap: never move the destination nor alter the info delivered).
- Player input during it = REACTIONS ONLY: roleplay, short Q&A, at most one telegraphed check SUL POSTO (for flavour/degree, Ch. 16) — NEVER a branch that changes where the scene lands or what it reveals.
- If the players push to deviate: soft redirect (§B3), or PARK the impulse as a post-scene subquest hook (§B22); NEVER fork mid-cutscene.
- DENSITY here = DEPTH (vivid narration + full dialogue + acknowledged reactions), NOT more choices (Ch. 10 / §A10 read as depth, not branching).
- LONG cutscenes: split into sub-beats and deliver via the dialogue of a PRESENT NPC, live; never a monolithic monologue.
- Format: player-facing via READ-ALOUD + dialogue (16.2); the GM keeps [Info GM]. TAG the beat '[CUTSCENE IN SCENA]' so the GM sees it is a rail (distinct from an elastic playable beat).

**OFF-SCENE CUTSCENE (the PCs are NOT present — villains plotting, distant councils, etc.): SURFACES AUTOMATICALLY, GM-facing.**
- WHEN (binding): the assistant presents it ON ITS OWN at the canonical MSQ beat that has one (per the verified Roadmap / wiki) — there is NO 'show me' request trigger. Surface it ONLY where it canonically belongs: never invented, never forced onto a beat that has none.
- HOW: append it as a SEPARATE block AFTER the played beat, wrapped '[CUTSCENE ALTROVE — i PG non sono presenti]' + the complete scene. It is GM-FACING by default: NEVER part of the 'Da leggere ai PG' nor auto-narrated to the players — the GM decides whether to read it aloud (a dramatic-irony interlude), keep it GM-only, or skip.
- ANTI-SPOILER WARNING (binding): if the scene contains a reveal still gated (Ch. 1), add a TERSE '⚠️ reveal protetto' (a short flag, NOT a cautionary sentence).
- OPTIONAL in-world delivery: the same information may instead reach the PCs as a report, a rumor (Ch. 15), an intercepted letter, an Echo vision (Ch. 4.2) or the aftermath they witness.

**TERSENESS & NO META (binding) [v1.26]:** the GM uses this tool and knows how it works. The cutscene TAGS are self-explanatory SIGNALS — do NOT re-explain, each time, what a railed / off-scene cutscene is, and NEVER narrate the tool's own internal choices to the GM ('compressione MSQ applicata', 'signature preservata', 'questa è una scena su binari, i PG possono reagire ma l'esito è fisso'). Tag + (if needed) a terse '⚠️ reveal protetto' is enough.

CROSS-REF: Echo visions Ch. 4.2; Layered Lore / [Info GM] 16.2; Spoiler Policy Ch. 1; subquest bookmark §B22 (06). Operational tag note: 06 §B1.

# CHAPTER 17 — GRAND COMPANY
The Grand Companies as an element of PURE COLOR and plot. They are NOT a progression system.

## 17.1 What they are (lore)
Military/civil organizations of the Eorzean nations, born to face the Garlean Empire, the Primals and other threats. The three canonical ones:
- **THE MAELSTROM** - Limsa Lominsa (Admiral Merlwyb)
- **THE ORDER OF THE TWIN ADDER** - Gridania (Elder Seedseer Kan-E-Senna)
- **THE IMMORTAL FLAMES** - Ul'dah (General Raubahn)

## 17.2 Enlistment (optional and NON-blocking)
- The party MAY enlist, but is NOT obligated.
- You can choose NO Company: the plot proceeds. No content is precluded.
- PCs may join DIFFERENT Companies (a roleplay choice, not a mechanical one).
- Typical moment: during the ARR arc.

## 17.3 What it entails (flavor only)
- Identity and belonging: a banner, a uniform, fellow soldiers, a narrative anchor.
- Plot hooks and themed missions (subquests Ch. 13, or the board Ch. 15).
- Contacts and welcome at facilities (rest, rumors, recurring NPCs).
- NO mechanical progression: no ranks with bonuses, dedicated seals/currency, level-gated unlocks. Any "promotions" are purely narrative.

## 17.4 Allies in the background
- Consistent with "Trust removed": fellow soldiers and officers fight ONLY IN THE BACKGROUND (Ch. 10.5).
- They can open a path or hold a front, but do not "play" the combat.

## 17.5 Handling in play (light enrollment beat)
The Grand Company enlistment is a LIGHT narrative OFFER, handled CONSISTENTLY: present the choice in a short scene and let the players accept or defer. It is NEVER expanded into a full combat/exploration beat, and NEVER silently dropped from one run to another. Optional and non-blocking (17.2): if the players defer or decline, the MSQ proceeds unchanged and the option remains open (it stays an open, offerable option, not stored in the save). Operational note: 06 §B2 (light enrollment beat).

# CHAPTER 18 — OUT OF COMBAT / RAISE / WIPE / AETHER SICKNESS
A videogame-style (FFXIV) KO/revival system: you fight 'hard' but lethality comes from MECHANICS, not from permanent death.

## 18.1 Philosophy
- Videogame model: at 0 HP you do NOT die, you go OUT OF COMBAT.
- NO death saving throws. NO instant death from massive damage.
- PERMANENT death from combat, by default, does NOT EXIST: the Echo prevents the end. You only 'lose' with a WIPE. (Exception: 18.7.)
- Difficulty comes from MECHANICS, not from inflated stats nor from an 'item tax'.

## 18.2 Out of Combat state (Downed)
- At 0 HP the PC is OUT OF COMBAT: unconscious, prone, cannot act or react.
- NO death saving throws: they stay down until revived (18.3) or until a WIPE triggers (18.5).
- Enemies IGNORE the downed characters: they neither target nor finish them.
- Overkill damage is irrelevant: you go only Out of Combat anyway.

## 18.3 Revival (Revive)
NORMAL HEALING DOES NOT REVIVE an Out-of-Combat character. You need:
| Means | Restores to | Cost / Notes |
|---|---|---|
| RAISE | 1/4 max HP | Healer ability (WHM/SCH/AST/SGE) from LVL 5; ACTION; consumes 1 slot of 3rd level or higher. No use limit beyond the slot cost. |
| PHOENIX DOWN | 1/2 max HP | Consumable (medium rarity). Action. |
| PHOENIX TAIL | full HP | Consumable (high/costly rarity). Action. |
| HEALER LB3 (Pulse of Life, etc.) | 3/4 HP | See Ch. 6: raises the Downed WITHOUT Aether Sickness. The definitive wipe-saver. |
- Every revival (EXCEPT the Healer LB3) applies AETHER SICKNESS (18.4).
- Exact costs and rarity of Phoenix Down/Tail: see Ch. 12.

## 18.4 Aether Sickness (post-revival debuff)
Whoever is revived (Raise / Down / Tail) suffers AETHER SICKNESS for 2 TURNS (their next 2 turns):
- DAMAGE and HEALING HALVED (roll normally and halve the total of the dice, rounding down).
- It re-applies from scratch if the PC is downed again and revived again.
- The Healer LB3 revives WITHOUT applying Aether Sickness.

## 18.5 Wipe (party reset)
- WIPE = ALL PCs Out of Combat at the same moment.
- The encounter REWINDS: narratively it is the ECHO that rewinds the moment.
- You return to the START-OF-ENCOUNTER state. Restored: everyone's HP; spent SPELL SLOTS; cooldowns / limited-use abilities; the LIMIT BREAK bar.
- Spent CONSUMABLES are NOT restored: Phoenix Downs and Tails stay BURNED.
- The real cost of a Wipe = consumables lost + redoing the mechanics correctly. Monster stats must not be inflated.

## 18.6 End of a won fight (with someone down)
- If the party WINS with one or more PCs Out of Combat, they RISE AUTOMATICALLY at the end of combat with 1 HP, WITHOUT Aether Sickness.

## 18.7 Permanent death (narrative exception)
- By default PCs NEVER die permanently from combat.
- The GM may designate SPECIFIC CASES (plot sacrifices, key moments, voluntary choices), declared clearly BEFORE the scene.
- Outside these cases, the Downed/Wipe system always applies.

## 18.8 Cross-references
- RAISE (level, slot): see also Ch. 5. Healer LB3 / LB bar / Wipe-reset: Ch. 6. Phoenix Down/Tail costs: Ch. 12. TEMPERING (Echo-safe) & the sealed-Blessing consequence (defeated Ascians escape): Ch. 5 (5.6).

# CHAPTER 19 — MEMORY SHEET / CONTINUITY
The campaign's 'save file': the SOURCE OF TRUTH the GM re-reads at the start of every session and updates at the end.
NOT THE PROCEDURE (binding, retrieval note): this chapter explains WHAT is tracked and WHY — it is NEVER the source for a command's trigger word, output shape or gate logic. For the actual '/fine sessione', '/salva' and load mechanics, see 06 §B17 (SAVE template + LOAD + the full '/STOP — SEQUENCE OVERVIEW'), §B21 (LIVE/STUDY modes) and §B24 (the delta gate) — always the sole authoritative source.

## 19.1 Purpose
- Keep the WORLD/CAMPAIGN STATE between sessions.
- Avoid contradictions and continuity 'holes'.
- Allow detours (subquests, Ch. 13) and a return to the right point.

## 19.2 What it does NOT track (a clear boundary)
- The PLAYERS' characters: sheets, HP, slots, abilities -> managed by the PLAYERS.
- INVENTORY, Gil, consumables (Downs/Tails/Potions), relics -> managed by the PLAYERS.

## 19.3 What it tracks (LEAN save, sections [A]-[C], aligned to 06 §B17)
- **[A] MSQ POSITION:** the current mission (EN) + the LAST COMPLETED step (= resume anchor); nothing predictive (next step, place, milestone are DERIVED from the wiki quest chain, not stored). (Crystals/Blessing are NOT in the save (Aetherytes only flagged in-scene, not tracked) — player-managed and announced in play; see 06 §B23.)
- **[B] PARTY (table-owned):** number of PCs + current level — copied VERBATIM from the save, NEVER derived from the arc nor 'corrected'. Used for encounter balancing and the tracker PC count.
- **[C] ACTIVE SUBQUEST:** exactly ONE active subquest at a time (name + progress + MSQ return point), or 'nessuna'; changing subquest loses the previous one (Ch. 13). No parked-leads list.
- **Sessione: N (session counter):** a dedicated table-owned integer (copied VERBATIM, +1 only when beats were played this session); the '=== SAVE ===' header carries no title. Aligned to 06 §B17 (the sole save-template source).
Everything else is DERIVED, not stored: what the PCs know, NPC reputations, Grand Company state, world-state and the reveal state are all a function of the MSQ position + the internal reveal gates (Ch. 1) - a small save that cannot mis-drive generation with a stale field.
Note: the combat SNAPSHOT is NOT an ordinary section of the save; it is created only on request (19.5).

## 19.4 When it is updated
- At the END OF SESSION, at each MILESTONE, BEFORE and AFTER a SUBQUEST, and at the end of an important FIGHT or MSQ beat. The trigger word, output shape and write-gate mechanics are entirely defined in 06 §B17/§B21/§B24 — not restated here.

## 19.5 Procedures
- **LOAD / SESSION START:** triggers on 'session start' / 'load' / 'prepare session' OR when the GM ATTACHES or PASTES a file/text containing a save (header '=== SAVE: ... ===' and/or sections [A]-[C]). In that case: interpret the save as the starting state, give a brief faithful recap, then a brief GM-facing orientation — the CURRENT beat + ONLY the SINGLE next MSQ pillar (one milestone) + the real next wiki step, from the Roadmap (08.1) — NOT a numbered-act index and NOT a gated-reveal box. Do not regenerate the save. Recognition details in 06 B17.
- **RECAP / CONTINUITY SELF-CHECK:** on 'recap' / 'campaign status' the assistant gives a GM-facing, READ-ONLY snapshot of the LEAN save ([A][B][C] + current beat) — never advancing the MSQ, never writing, never listing PC sheets, never printing a gated-reveal box (upcoming reveals on demand via 'mappa MSQ', 06 §B25). Full operational format + continuity self-check: 06 §B19.
- **NAMED BEATS (campaign):** the campaign advances as NAMED MSQ/subquest beats from the Roadmap (08.1), one per 'continua'/request; NO numbered 'Atti' and NO invented beats (numbered acts are a One-Shot construct). Operational format: 06 §B1/§B2/§B20.
- **MODULE NATURE:** GM material; it may contain operational info and behind-the-scenes notes, but it is NOT canonical, does NOT modify the Memory Sheet and does NOT imply the events will happen.
- **DENSITY:** each beat must be playable and dense (dialogues, Q&A, checks, detours, fallbacks, encounters in full). Never declare a beat ready by merely summarizing it.
- **LORE COMPLIANCE:** for real dungeons/quests do not invent origins, factions, voidsent, experiments, corruption or dark forces not verified. Use Knowledge / 08.1 / Gamer Escape or stay generic.
- **ENCOUNTERS IN THE MODULE:** if a fight is likely, include the GM-facing encounter package. Full stat blocks on request or on 'prepare encounter'.
- **MIXED SESSIONS:** investigation + dungeon/trial separated into NAMED beats (investigation, hook, dungeon overview, dungeon blocks, boss, closure/save); no numbered acts (06 §B4).
- **MSQ RE-HOOK:** on 'MSQ re-hook' the assistant proposes plausible, lore-compliant ways to return to the next canonical step.
- **SAVE (single command):** full trigger word, output shape, recap buckets and delta-gate mechanics live ONLY in 06 §B17 ('/STOP — SEQUENCE OVERVIEW') + §B21 + §B24 — not restated here. Campaign-specific reminder: the written save inherits the table-owned PARTY (N PCs + level) VERBATIM; crystals/Blessing & Aetherytes are NOT save fields (player-managed / in-scene flag only, §B23). Operational detail: subquest slot/Bookmark §B22; structure by content §B20; economy §A20-A22.
- **COMBAT SNAPSHOT:** not an ordinary part of the save; create it only on explicit request.

## 19.6 The Sheet template
The CANONICAL operational save template (header, sections [A]-[C], footer, file naming) is UNIQUE and lives in 06_Procedures_and_Format (B17). To avoid divergence it is NOT duplicated here: always use that one.
Section reminder (LEAN): [A] MSQ Position (current quest EN + last completed step) | [B] Party (N PCs + level, table-owned, verbatim) | [C] Active subquest (single slot, or 'nessuna'). Reveals, NPC reputations and world-state are DERIVED from the MSQ position (not stored); Crystals/Blessing are NOT save fields (player-managed, announced in play); Aetherytes are only flagged in-scene, not tracked (06 §B23).
The combat snapshot is NOT an ordinary part of the save: it is generated only on explicit request (see 19.5).

## 19.7 Cross-references
- Subquest bookmark: Ch. 13. Full Spoiler Policy: Ch. 1. MSQ position/roadmap: Ch. 5 and 08.1. Blessing/Crystals: Ch. 5 and 7. Grand Company: Ch. 17.

# CHAPTER 20 — TERM INDEX & CROSS-REFERENCES
NOT an extended glossary: it is a ROUTING INDEX (term -> 1 line -> Ch.).

## 0. Controlled vocabulary (mandatory terminology)
- **ENTHRALLED / ENTHRALLMENT** - the VULGAR (common) term for Primal mind-domination. (Italian output: Asservito / Asservimento.)
- **TEMPERED / TEMPERING** - the SCIENTIFIC (learned) term for the same phenomenon. (Italian output: Temprato / Tempra. NEVER "tempering/templaggio".)
- **Abbreviations:** PC, NPC, GM, HP, AC, DC, HD, CR, LB, MSQ.

## A. Term index (alphabetical)
| Term | Definition | Ch. |
|---|---|---|
| AETHERYTE | a crystal for teleporting between ALREADY-VISITED locations (no attunement list); costs 1 HD per trip. | Ch. 8 |
| OPEN AREA (encounter in) | exploration fights: wandering mobs and ambushes in travel/rest. | Ch. 10.4 |
| STANDARD ARRAY | the only method for scores (15,14,13,12,10,8). | Ch. 3 |
| ASCIAN | occult antagonists; permanently killable only with the Blessing. | Ch. 5 |
| ENTHRALLED / ENTHRALLMENT | (vulgar) a mind bent by a Primal. | Ch. 4 |
| JOB BOARD | optional Levequest-style jobs. | Ch. 15 |
| BACKGROUND | the PC's story, built with the assistant in Session 0. | Ch. 2 |
| PLOT BATTLE | an MSQ boss fight in a normal zone; allies in the background. | Ch. 10.5 |
| BLESSING OF LIGHT | a party boon from the Crystals: shatters Ascians + wards vs aetherial corruption; NOT Tempering immunity (that is the Echo). | Ch. 5 |
| CALAMITY / SEVENTH UMBRAL ERA | recent catastrophe (Dalamud/Bahamut); common knowledge. | Ch. 2 |
| JOB CHANGE | rare, EARNED via a Soul-Crystal subquest (GM discretion, lore-reachable), in town, keep level; no revert/re-swap without a new subquest; no duplicates. | Ch. 3 |
| COMBAT TRACKER | a text preview + editable tracker (initiative/monster HP). | Ch. 2 / 9 |
| CUTSCENE | in-scene = railed story beat (reactions only, fixed outcome, '[CUTSCENE IN SCENA]'); off-scene = '[CUTSCENE ALTROVE]' surfaced AUTOMATICALLY at the canonical beat, GM-facing, + anti-spoiler warning; GM decides read/keep/skip. | Ch. 16.6 |
| PHOENIX TAIL | consumable: revive to full HP + Aether Sickness; shop ONLY. | Ch. 12 |
| CRAFTING | Downtime (only the skilled): consumables, components ~25% of shop price; never Downs/Tails. | Ch. 14 |
| CRYSTALS OF LIGHT (the 6) | one per element, shared by the party; collected at MSQ beats. | Ch. 7 (see 5) |
| DOWNTIME | an activity at a stop as an alternative to the Long Rest. | Ch. 14 |
| DUNGEON | action content: mid-boss -> interlude/enigma -> mid-boss -> interlude/enigma -> final boss (a short non-combat beat between EVERY pair of fights, never a boss-rush; delivered in the fewest COMPLETE chunks, split-not-condensed; NO trash mobs; boss = party level, mid-boss = level -2). | Ch. 10.6 |
| ECHO | the PCs' gift: visions, languages, resistance to Enthrallment, rewind on Wipe. | Ch. 4 |
| ECHO (voluntary invocation) | an attempt costing 2 HD (spent even on failure). | Ch. 4 |
| ENRAGE | a blow/threshold punishing those who drag too long; always avoidable. | Ch. 10.8 (see 9) |
| EORZEA | the region of play, in the world of Hydaelyn. | Ch. 2 |
| OUT OF COMBAT (DOWNED) | 0 HP = down, not dead; needs Raise or Down/Tail. | Ch. 18 |
| GIL | currency (1 Gil = 1 gp; smaller silver/bronze denominations). | Ch. 12 |
| CHALLENGE RATING (CR) | a metric to size enemies. | Ch. 10 |
| GRAND COMPANY | national factions; pure color, optional, non-blocking. | Ch. 17 |
| HEALER | role: healing, support, performs the Raise. | Ch. 2 / 3 |
| GM INFO | a secret context block, for the GM only. | Ch. 16 |
| LIMIT BREAK (LB) | a party bar 0-3; caps at segment 2 outside boss fights (LB3 only on Bosses); empties on any rest and on any travel; area/radius scales with the level. | Ch. 6 |
| LAYERED LORE | info unlockable at DC 10/15/20, spoiler-safe. | Ch. 16 |
| AETHER SICKNESS | after a revive: damage/healing dice halved, for 2 turns. | Ch. 18 |
| MILESTONE | narrative progression, no XP. | Ch. 5 |
| GOSSIP / RUMORS | tavern info on a check; True/Color/Misleading table. | Ch. 15 |
| PHOENIX DOWN | consumable: revive to 1/2 HP + Aether Sickness; shop ONLY. | Ch. 12 |
| SPOILER POLICY | gated mysteries are not revealed before their canonical moment. | Ch. 1 |
| PRIMAL | deities summoned by the beast tribes; enthrall the faithful. | Ch. 2 / 16 |
| GATHERING | Downtime (anyone): direct Gil (5/10/25/50). | Ch. 14 |
| RAISE | Healer ability (from lvl 5) that raises a Downed + Aether Sickness. | Ch. 18 (see 5) |
| READ-ALOUD | a base description for everyone. | Ch. 16 |
| RESEARCH / STUDY | Downtime: lore clues / subquest hooks. | Ch. 14 |
| REST (Short/Long) | base D&D 5e rules. | Ch. 5 / 15 |
| MEMORY SHEET | the "save": world/MSQ state + party level, sections [A]-[C]; NOT crystals/Aetherytes (player-managed, announced in play). | Ch. 19 |
| SESSION 0 | PC creation, background, rules tutorial, base lore. | Ch. 2 |
| ATTUNEMENT | deprecated as bookkeeping: no attunement list is tracked; the assistant only flags Aetheryte presence in-scene ('Luogo (Eterite)'). | Ch. 8 |
| SOUL CRYSTAL | the soul crystal that enables a Job. | Ch. 3 |
| SUBQUEST | optional local missions, faithful to the game. | Ch. 13 |
| TANK | role: aggro, protection, defenses. | Ch. 2 / 3 |
| TELEGRAPH / MECHANICS | boss moves announced the round before, with a counter. | Ch. 9 |
| TEMPERED / TEMPERING | (scientific) = Enthralled/Enthrallment. | Ch. 4 |
| TRIAL | a single boss with mechanics, faithful to the original. | Ch. 10.7 |
| BEAST TRIBES | non-human peoples (NPCs/monsters) who summon the Primals. | Ch. 2 (01_Races, 04_Bestiary) |
| TRINITY | the Tank / Healer / DPS balance. | Ch. 2 / 3 |
| WIPE | all Downed: encounter reset (spent consumables stay spent), justified by the Echo. | Ch. 18 (lore in 4) |

**FINAL NOTE:** in case of terminological or rules doubt, this index points to WHERE the authoritative version is found. If two sources diverge, the specific chapter referenced above wins.

## RULE NOTE - BLESSING STATE (Ch. 5.5 / 7.4)
The Blessing of Light is 'complete/active' ONLY with all 6 crystals (6/6). With 1-5 crystals the correct state is 'incomplete/developing'. The #6 Wind (after Garuda) is the last piece that completes it. Never mark 'complete/active' before the sixth crystal.
