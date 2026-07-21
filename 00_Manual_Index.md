# 00_MANUAL_INDEX - General Index, Conventions & Routing (for the assistant)
Version v1.22 (Claude-native)

## SCHEMA NOTES
- PURPOSE: this file is a lightweight INDEX / ROUTING + CONVENTIONS layer. It does NOT duplicate rules or lore - it points to where the authoritative content lives. (Duplication across files is avoided on purpose.)
- DATA LANGUAGE = English (single source of truth). The assistant renders flavor into Italian at OUTPUT.
- KNOWLEDGE-FILE PRECEDENCE: the knowledge files are the AUTHORITATIVE source (data + rules). In conflict with generic/training knowledge, the files prevail. Operational behavior lives in the Campaign INSTRUCTIONS (control layer) and in the FORMATS of 06; data files are not commands.
- CITATION: cite across files ONLY in the short form "NN (Section)" (e.g. "06 §A8", "05 Ch. 1"). NEVER print a file's name/extension in user output (see 06 §A1).

# FILE STRUCTURE (9 knowledge files, sequential 00-08)
| File | Contents |
|---|---|
| 00 (Manual_Index) | This file: index, conventions, routing. |
| 01 (Races) | PC race build data: 8 playable races + Garlean (optional) + beast tribes, Naming Appendix, and Role Action Feats (Ch. 4). |
| 02 (Classes) | The 22 Jobs (classes): progression, subclasses, resources, mimicries/artes/strikes. |
| 03 (Spells) | Spell lists by caster Job + homebrew spell descriptions (metric). |
| 04 (Bestiary) | Monsters by creature class -> genus -> species + Primals. |
| 05 (Campaign) | Campaign RULES only: Section A (Ch. 1-20). [The MSQ flow was split out to 08 (MSQ_Flow).] |
| 06 (Procedures_and_Format) | assistant operational formats, procedures & SHARED RULES (Parts A-E). |
| 07 (Glossary) | Naming SYSTEM (method + parenthesis test + element map + validated examples) and ALL binding renderings: aether family, coined/game terms, demonyms, places/hubs (ARR-DT), factions/orgs/titles, taverns/NPCs, race clans, class (Job) names, villain epithets, the Void & enemy/cosmology terms, Primals/summons, beast tribes, the ability/spell-name policy (G24), recurring FF monster names (G25), Dawntrail/Tural names (G26; OUT OF SCOPE for the Campaign) and iconic phrases (G27). |
| 08 (MSQ_Flow) | The MSQ FLOW (split from 05): 08.1 = MSQ Roadmap ARR->EW + the 5 CANONICAL CUTSCENE & REVEAL MANIFESTS (ARR/HW/SB/ShB/EW); 08.2-08.6 = the ordered MSQ index (giver + steps + Next); 08.OST-ARR..08.OST-EW = duty OST tables; 08.OST-SCENE-ARR..EW = scene/mood OST tables (city/zone/cutscene). |
Sequential numbering 00-08, no gaps (08 = the MSQ flow, split from 05).

# HOW TO USE THIS SET (knowledge policy)
- For details not present in the files (see 06 §A14, split by purpose): Gamer Escape primary for LORE/canon/reveal (Loremonger for dialogues); ConsoleGamesWiki primary for MSQ chain order / next-step / patch tags.
- When a rule is drawn from a file, name the section/chapter it came from - but only if useful to the GM, and never in-scene.

# GLOBAL CONVENTIONS
- Rules data in ENGLISH (single source of truth); OUTPUT to the user in ITALIAN.
- MEASUREMENTS in METRIC (1.5 m = 5 ft); decimal POINT in data, render with comma at output (1,5 m).
- TWO-LEVEL NAMING: narrative text in Italian (English) at first occurrence; save keys and wiki queries in pure ENGLISH (full method + all renderings in 07 (Glossary)).
- Moves/abilities/traits/actions: FFXIV/FF-iconic NAMES are KEPT in their original form (07 G24); the effect/description is in Italian. FFXIV proper names stay English in the data, rendered per 07 at output.
- RECURRING NAMES & AETHER FAMILY: rendered per 07 (Glossary) (binding) - e.g. aether -> etere, Aetheryte -> Eterite. The English in the knowledge files is SOURCE DATA, rendered at output.
- MONSTER NAMES: FF-iconic recurring monsters rendered per 07 (Glossary) G25 (e.g. Morbol -> Molboro, Tonberry -> Tomberry, Bomb -> Piros) - binding; FFXIV-original creatures/tribes per 07 G23 or the method (07 G1).
- DAWNTRAIL NAMES: Tural place/dungeon/trial/tribe names per 07 (Glossary) G26 - binding for Loremonger/One-Shot (Campaign stays ARR-EW).
- Mechanics (DCs, dice, conditions, feature names, CR) stay English and verbatim. Do NOT invent.

### Controlled vocabulary (Primal mind-domination)
- ENTHRALLED / ENTHRALLMENT = VULGAR (common). Italian output: Asservito / Asservimento.
- TEMPERED / TEMPERING = SCIENTIFIC (learned), the official FFXIV English term. Italian output: Temprato / Tempra.
- Never "tempering/templaggio" in Italian output.

### Consistency & verification (generic rule)
- Before writing about specific elements (lore, technology, factions, eras, places, creatures): verify sources and stay consistent with the real context. Verification is INTERNAL: no preambles/disclaimers in output (do not explain what something 'is not'). Operational detail in 06 §A8.

### Spoiler policy
- Hard reveals are never anticipated before their canonical beat. Full rule in 05 (Campaign) Ch. 1.

# JOBS & PLAYABLE RACES (pointers)
- The 22 Jobs by role (4 Tank / 4 Healer / 6 Physical Melee / 3 Physical Ranged / 5 Magical; no party duplicates) -> 02 (Classes); Italian names 07 G18; party rules 05 Ch. 3.
- The 8 "enlightened" playable races (+ Garlean/Padjal optional; tribal/beast-tribe = NPC/monster) -> 01 (Races); 05 Ch. 3.2.

# QUICK ROUTING
- Races -> 01 (Races).
- Naming (method + all renderings: places, factions, classes, villains, Primals, beast tribes, MONSTER names, Dawntrail/Tural, ability-name policy) -> 07 (Glossary).
- Jobs / classes / equipment (incl. Machinist) -> 02 (Classes).
- Spells (lists + homebrew descriptions) -> 03 (Spells).
- Role Action Feats -> 01 (Races) Ch. 4.
- Monster / Primal stat blocks -> 04 (Bestiary); construction & anchoring rules -> 06 §B6; monster NAME renderings -> 07 (Glossary) G25/G23.
- Campaign rules -> 05 (Campaign) Section A.  - MSQ order/sequence -> 08.1 (the FULL ARR->EW quest-by-quest ordered chain is cached in 08.2 (ARR) + 08.3 (HW) + 08.4 (SB) + 08.5 (ShB) + 08.6 (EW); campaign FINALE = the quest Endwalker, then the epilogo, 06 §B27).
- MSQ manifests (canonical cutscenes/reveals per beat, reveal/spoiler timing) -> 08.1 (per-arc Beat Manifests); read-only audit via 06 §B25 "mappa MSQ" (Campaign) or as READ-ONLY reference by the Loremonger role.
- Operational FORMATS & SHARED RULES -> 06 (Procedures_and_Format).
- Limit Break (LB1/LB2 by role, LB3 by Job) -> 05 Ch. 6.
- Memory Sheet / save template -> 06 §B17 (referenced by 05 Ch. 19).

# ONE-SHOT NOTE
The One-Shot mode uses the same knowledge but a separate assistant. Templates and constraints in 06 (Procedures_and_Format) Part C. Normal PCs, no Echo/Crystals/Blessing, no direct Primals; scope is unlimited by arc (06 §A19).

END OF FILE - 00_Manual_Index (index, conventions, routing for the 00-08 knowledge set).