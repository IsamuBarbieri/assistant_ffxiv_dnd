# 08.0 — CONVENZIONI GLOBALI (una volta sola)
- MANIFEST (08.1): backbone LOCKED di cutscene/reveal; riprodurre ogni pin, mai droppare/inventare, GATED nascosti. Pin: IN-SCENA / ALTROVE / VISIONE DELL'ECO / REVEAL / GATED.
- INDICE (08.2-08.6): catena quest reale (giver + step + [duty] + Next). Ordine autoritativo (06 §A14, CGW); reveal-gate 05 Ch.1 + manifest; dialoghi Gamer Escape. Cachati per OGNI quest: ordine, nome, Next MSQ risolto; giver/step spine SOLO dove mostrati (minoranza) — per il resto lo step spine si recupera live (06 §A14).
- MARCATORI DI CONDENSAZIONE `[COND: …]` (binding, 06 §B2): marcano le SOLE quest condensabili. NON INNESCANO NULLA: la condensazione è **innescata dal GM con `/riassumi`**, mai automatica — `/continua` gioca sempre la prossima quest come beat normale, marcata o no. I marcatori DEFINISCONO L'ESTENSIONE del ponte: dove comincia il tratto, dove si ferma (alla prima quest NON marcata, che si gioca in pieno) e cosa ci entra dentro. `[COND: fetch]` = consegna/commissione pura · `[COND: relay]` = relay sociale a basse poste (parla ad A che manda a B, senza scelta/rivelazione/scontro) · `[COND: parallel → <convergenza>]` = cluster di micro-obiettivi paralleli. REGOLA D'ORO: **NON marcato = SI GIOCA**, sempre; un buco nella marcatura costa tempo al tavolo, mai contenuto. MAI `[COND]` su: una quest che nomina una DUTY istanziata, una quest che porta una cutscene/reveal pinnata nei manifest (08.1), una quest-pillar, o qualunque caso dubbio. I marcatori si aggiungono SOLO in una passata di marcatura rivista dal GM, MAI a runtime.
- MARCATORE `[CUT: <motivo>]` (binding, più forte di `[COND]`): la quest è FUORI dalla campagna — MAI giocata, MAI riassunta in un bridge, MAI usata come bersaglio di '[Info GM] apre'. La catena SCAVALCA la voce e il Next della quest precedente punta direttamente alla prima quest non tagliata. Si usa per contenuto che questo homebrew non implementa (precedente già in uso: le fetch-errand del Crystal Tower). La voce resta nell'indice solo come traccia canonica.
- OST (08.OST-*): temi di duty/scena risolti da queste tabelle (06 §A23); titoli in inglese (chiave di ricerca).
- Fonte ordine: ConsoleGamesWiki. Niente livelli-quest. Gap: 06 §A14, mai improvvisare.

# 08_MSQ_FLOW — MSQ Roadmap, Cutscene/Reveal Manifests & Ordered Index
Version v3.37 | Source: FFXIV x D&D 5e Homebrew — Campaign arc A Realm Reborn -> Endwalker (Dawntrail EXCLUDED)

> SCHEMA / USAGE (binding): this is the MSQ FLOW file (split out of 05). References to 'Section A' and to 'Ch. X' point to 05_Campaign.md. AUTHORITATIVE for MSQ order/sequence: consult the ordered index (08.2-08.6) FIRST for order/next-step/giver/step spine (over model memory). The 5 manifests (in 08.1) are the LOCKED cutscene/reveal backbone. If in conflict with the Instructions (06/master), the Instructions win.

> FILE CONTENTS (part map):
>  - 08.1 — MSQ ROADMAP (ARR->EW): the sequential map (arcs, zones, bosses, crystals, gates) + a compact POINTER to the flow behaviour (which lives ENTIRELY in 06 + the Campaign instructions; this file is pure DATA) + the REVAMPED-DUTY LOCKs + the 5 CANONICAL CUTSCENE & REVEAL MANIFESTs (one per expansion, inside its arc).
>  - 08.2-08.6 — ORDERED MSQ INDEX (giver + step spine + single Next): 08.2 ARR (openings->2.55) · 08.3 Heavensward · 08.4 Stormblood · 08.5 Shadowbringers · 08.6 Endwalker.
>  - 08.OST-ARR .. 08.OST-EW — DUTY OST TABLES: the music themes for every MSQ duty (ARR->EW), CGW/GE-verified. 08.OST-SCENE-ARR..EW — SCENE/MOOD OST TABLES (city / zone / cutscene themes), wiki-verified (added v3.14).
>  (Split out of 05; renumbered to this clean 08.x scheme in v2.0. All files reference these codes.)

# 08.1 — MSQ ROADMAP (ARR -> EW)

**PURPOSE:** the campaign's sequential map. It says WHAT happens and in what order (arcs, zones, bosses, crystals, gates). The RULES live in Section A.
Reference: see Section A Ch. 5 (Milestone Progression); this file is its detail. Order verified against community progression guides.

**TOTAL NARRATIVE ARC:** A Realm Reborn -> end of Endwalker (the confrontation with the Endsinger). NO post-Endwalker patches. Dawntrail EXCLUDED.

**LEVELS (milestone compression, no XP):** ARR 1-8 | HW 9-12 | SB 13-15 | ShB 16-19 | EW 20 (cap)
*NOTE: the campaign runs on milestone levels 1-20 (Ch. 5); beats are identified by NAME and sequence, not by in-game level numbers.*

**LEGEND:** `[GATE]`=mandatory to proceed | `[REC]`=recommended (unlocks valuable trials/dungeons/alliances) | `[OPT]`=optional, zone-themed | `[CUT]`=low-value/unreachable fetch.

**LOGICAL-THREAD RULE:** activate a quest only if the PCs can reach it (ZONE consistency + MSQ point); its lore must not foreshadow events not yet occurred. No hooks from the other side of the world.

**PRACTICAL MSQ FLOW RULE (POINTER — this file is PURE DATA):**
- BEHAVIOUR lives in 06 + the Campaign instructions, NEVER here: how to walk the flow (one wiki step per 'continua'; sub-beat granularity and the DUNGEON/TRIAL fewest-complete-chunks carve-out — 06 §B2/§B12), connective story beats, the FETCH/CONNECTIVE AUTO-CONDENSE, compression & SIGNATURE PRESERVATION (06 §B12), STORY-FLOW FIDELITY & STAGING-IS-FLOW (06 §B2), the strict CONTINUITY HANDOFF, and the [Info GM]/orientation rules — ATOMIC STEP, SPINE-SOURCED, ORDER AUTHORITY & NO RESURRECTION (06 §B1/§B2). Flow-behaviour tweaks land in 06 + tplC ONLY; this file does not change for them.
- DATA this file supplies (binding): the Roadmap order + the per-level PILLARS = MANDATORY-CONDITION checkpoints (a fixed canonical NPC/place, a gated reveal, a crystal, a required outcome) — CONSTRAINTS/guardrails, NOT the beat list: the playable flow is ALWAYS the ordered quest chain cached in 08.2-08.6, walked IN ORDER (authoritative over model memory, no live fetch needed); the 5 FROZEN CUTSCENE & REVEAL MANIFESTS; the ordered index (giver + step spine + single Next) = the SPINE from which 'apre <quest>' and 'prossimo step wiki' are READ (06 §B1 SPINE-SOURCED) and the ORDER AUTHORITY over any drafted or remembered pointer; the ARR REVAMPED-DUTY LOCK; the 08.OST-* duty tables.
- DATA KERNEL (binding here): a duty / manifest cutscene / reveal / crystal / named-boss / Scions scene is ALWAYS played in full, NEVER condensed; never create MSQ objectives, dungeons, enemies, places or items NOT present in the save, this roadmap or Gamer Escape (06 §A6).
- FALLBACK: if a next step is not resolvable from this index, resolve per 06 §A14 (ConsoleGamesWiki = chain order primary; Gamer Escape = lore/NPC/dialogue) or STOP at the last certain step and flag a 1-line GM Note — never improvise.

**OPERATIONAL MSQ RULES** (acts-based module workflow, anti-invention lore, mixed investigation+dungeon session, MSQ re-hook): see 06_Procedures_and_Format Parts A and B (sections A6, B1, B3, B4). Removed here to avoid redundancy with 06.

**CURRENT DUTY VERSIONS (binding):** reproduce every duty (dungeon/trial) in its CURRENT / LIVE version as documented on the wiki MAIN page (Gamer Escape / Console Games Wiki) — NOT a '/Old' pre-revamp subpage, nor older memory. MANY ARR duties were revamped, mostly in Patch 6.1: Castrum Meridianum & The Praetorium were streamlined (8→4 players; current Castrum bosses = The Black Eft → Magitek Vanguard F-1 → Livia; the Praetorium KEEPS the magitek-armour ride → Mark II Magitek Colossus → Nero → Gaius); the ULTIMA WEAPON became its OWN trial (The Porta Decumana / The Ultimate Weapon), NOT part of the Praetorium; Cape Westwind (Rhitahtyn) and The Steps of Faith (6.2) became solo instance battles; several ARR dungeons had trash/bosses trimmed. IGNORE the MMO player-count label (solo/4/8) — always build for the ACTUAL party (Ch.10.3); what carries over is the CONTENT (bosses/layout/mechanics/cutscene placement). If current-vs-old is ambiguous, prefer the current page + a 1-line GM Note. (Illustrations, not a closed list; verify each duty on the wiki.)

**ARR REVAMPED-DUTY LOCK (binding — for these duties use ONLY the current data below):**
*Most ARR duties keep their ORIGINAL bosses/gimmicks (6.1 mostly trimmed trash) — for those the normal 'current version' rule + wiki suffice. The few duties below were STRUCTURALLY changed; the model's memory is stale on them and wiki pages list the OLD bosses/mechanics too, so use ONLY this and NEVER re-add a retired boss/gimmick.*
- **The Thousand Maws of Toto-Rak** (5.3 rework): gimmick = ACTIVATE TERMINALS (Confession Chamber terminal -> Fool's Rest terminal -> open the Abacination Chamber door), NOT the retired 'collect Photocells' hunt. Roster: mini-boss COEURL O' NINE TAILS (encountered TWICE) - despite the feline-sounding NAME it is an OCHU (plant / Seedkin), NOT a coeurl: render it as a carnivorous plant (NAME != NATURE, 06 §A3) - then the final boss GRAFFIAS (a diremite/banemite: green-goo puddles, Fleshy Pod adds, destructible tail at 50%). The dungeon TRASH theme is Vilekin (spiders/mites), but the Coeurl O' Nine Tails mini-boss ITSELF is a plant.
  - **NO MAGITEK / ALLAGAN (binding, observed family-wide drift):** Toto-Rak is an ANCIENT GELMORRAN prison overgrown by the wood, NOT a Garlean or Allagan site. The 'terminals' are OLD AETHERIC/organic-hydraulic mechanisms of Gelmorran make — living crystal, root-fed conduits, carved stone — NEVER 'magitek consoles', Allagan tech, ceruleum, or Garlean machinery. The word 'terminal' here is a translation of an antique mechanism; do NOT let it prime a sci-fi reframe. The puzzles resolve through organic/aetheric means (clear a root, channel aether, read carved glyphs), never by 'rewiring circuits'.
- **Castrum Meridianum** (6.1): EXACTLY 3 bosses — The Black Eft -> Magitek Vanguard F-1 -> Livia sas Junius (final). There is NO 'Magitek Colossus Rubricatus' (that boss belongs to the retired 8-player version).
- **The Praetorium** (6.1): keeps the magitek-armour ride, then Mark II Magitek Colossus (fought on foot) -> Nero tol Scaeva -> Gaius van Baelsar. The ULTIMA WEAPON is NOT here — it is its own trial, The Porta Decumana.
- **Cape Westwind** (Rhitahtyn sas Arvina): now a SOLO instance battle (was an 8-player trial).
- **The Steps of Faith** (6.2; the dragon Vishap): now a SOLO instance battle.
IGNORE the MMO player-count in all cases — build for the actual party (Ch.10.3). For any OTHER ARR duty not listed here, use its current wiki version normally (gimmick usually intact).

**FLOW NOTE (no side gates):** the campaign has NO side gates. The CRYSTAL TOWER is INLINE MANDATORY MSQ FLOW - SEEDED at 'Laying the Foundation' (2.1) and PLAYED as a fixed contiguous arc after 'Build on the Stone' (end of 2.1), triggered by CID's arrival at the Rising Stones, exiting to 2.2 'Still Waters'. See the CRYSTAL TOWER ARC block (end of Arc 1) and the 08.2 bridge node. All other mandatory content is already within the MSQ spine.

---

## The Blessing of Light = the 6 Crystals (key mechanic)
**WHAT IT IS (spoiler-safe lore):** the Blessing of Light is a divine protection tied to Hydaelyn and to the 6 ELEMENTAL crystals (Water, Fire, Lightning, Earth, Ice, Wind) the group collects through its own feats. It wards against aetheric corruption, lets one safely contain large amounts of Light, and is what lets a defeated Ascian be permanently destroyed. (Resistance to Primal TEMPERING is the ECHO's innate gift, NOT the Blessing — Section A Ch. 4.5/7.3.)

> **>>> SPOILER EW / GM ONLY - DO NOT REVEAL BEFORE THE CANONICAL BEAT <<<**
> The Blessing is the Traveler's Ward, Venat/Hydaelyn's spell, tied to the story of the Ancients and the seat of Azem.

**FLOW IN THE CAMPAIGN:**
- **ARR:** all 6 are collected (complete by lvl 7). It is the Blessing that saves the PCs from the Ultima Weapon.
- **End of ARR (L8, Keeper of the Lake 2.55):** MIDGARDSORMR SEALS the Blessing and SNUFFS the crystals.
- **HW:** they relight ONE AT A TIME with great feats (partial after Bismarck, L10) until FULL RESTORATION after the Ascian Prime (L11, Midgardsormr breaks the seal).
- **SB onward:** the Blessing is INTACT. Without the Blessing (only in HW) defeated Ascians can't be permanently killed (they flee) and Hydaelyn's ward is gone; the ECHO still keeps the party Tempering-safe -> see Section A Ch. 5.6.

**COLLECTION ORDER (ARR):** #1 WATER L2 | #2 FIRE L4 | #3 LIGHTNING L4 | #4 EARTH L5 | #5 ICE L6 | #6 WIND L7 (completes) | SEAL L8.

---

## CANONICAL CUTSCENE & REVEAL MANIFESTS — SHARED PURPOSE & LEGEND (binding, applies to the 5 expansion manifests — ARR / HW / SB / ShB / EW — plus the separate Crystal Tower manifest)
**PURPOSE:** each manifest is the PRECISE, LOCKED story backbone of its arc: it PINS the cutscenes/reveals that MUST appear at each beat and the ones that MUST stay hidden. They are DATA, not generation — the assistant reproduces them at the SAME beat EVERY time (NEVER omit on regeneration, NEVER invent an extra, NEVER move it) and KNOWS them without fishing from the wiki (the wiki stays available for everything ELSE, primarily exact DIALOGUE, Gamer Escape primary). It also makes a return to the MSQ after a subquest clean and exact. Each is a MANIFEST (what must not be dropped), NOT a scene-by-scene script; each complements the per-level BEAT entries below it and the STORY-FLOW FIDELITY rule. Cutscene placement/tags per Ch.16.6 (`[CUTSCENE IN SCENA]` = players present, rail; `[CUTSCENE ALTROVE]` = off-scene, GM-facing); reveal gating per Ch.1. This is the block the `mappa MSQ` audit (06 §B25) reads. All beats below are WIKI-VERIFIED; where a patch tag in a manifest differs from a rough tag in the per-level Lvl blocks, THE MANIFEST PREVAILS.
**LEGEND (all 6 manifests):** `IN-SCENA` = mandatory in-scene cutscene (rail) | `ALTROVE` = mandatory off-scene cutscene (GM-facing, PCs genuinely ABSENT, + `⚠️ reveal protetto` if it carries a gated reveal) | `VISIONE DELL'ECO` = a vision delivered by the Echo: the PCs EXPERIENCE it (so it is read to them, not GM-facing) but are not present at the place/time shown — it is neither ALTROVE nor IN-SCENA, and it hits the WHOLE party by default (06 §B1 ECHO VISIONS) | `REVEAL` = what becomes KNOWN at this beat (record as known here, state derived, Ch.19.3) | `GATED` = must NOT be named/anticipated yet.
**Per-manifest specifics only** (Blessing-of-Light state, revamped-duty locks, unique structural notes) are given under each arc's manifest heading below; the PURPOSE/LEGEND above is NOT repeated there.

## Arc 1 - A Realm Reborn (lvl 1-8)
**REMINDER:** starting cities (Gridania/Ul'dah/Limsa) -> Scions. MSQ Primals: Ifrit, Titan, Garuda, Ultima Weapon. Antagonists: Gaius + Lahabrea. Crystals: all 6 in ARR, sealed at L8. Gate: Crystal Tower (Mor Dhona, L8).

### ARR CANONICAL CUTSCENE & REVEAL MANIFEST (binding — anti-drop / anti-invent — FROZEN v3.0, wiki-audited)
**SPECIFICS:** all 6 elemental crystals are collected across ARR, sealed at L8 end (see Blessing of Light block above). No Enthrallment mechanic in ARR. Revamped-duty lock: see the ARR REVAMPED-DUTY LOCK block above (Toto-Rak, Castrum Meridianum, The Praetorium, Cape Westwind, Steps of Faith).

#### L1 — The Echo awakens
- VISIONE DELL'ECO: cold-open SHARED Echo vision on the arrival journey (Hydaelyn/Mothercrystal; 'Hear... Feel... Think...'); hits the WHOLE party — this is the precedent that fixes the party-wide default; NO burning dragon (Ch.1.7).
- GATED: the nature of the Echo and of Hydaelyn (Reveal: Eco = NO).

#### L2 — City climax · Water crystal · the Scions
- IN-SCENA: the city-questline climax (campaign framing: Serpent Reavers / a local primal plot) -> Hydaelyn's first voice -> Crystal #1 WATER.
- IN-SCENA (LATER in the L2 chain, AFTER the first dungeons — NOT at the Water-crystal climax): the FORMAL joining of the Scions of the Seventh Dawn at the Waking Sands — canonical beat 'The Scions of the Seventh Dawn' (Minfilia; Thancred, Y'shtola, Papalymo, Yda). WIKI-VERIFIED ORDER within L2: city-questline climax + Water crystal at Sastasha ('It's Probably Pirates') -> Sastasha -> Tam-Tara Deepcroft ('Fire in the Gloom') -> Copperbell Mines ('Into a Copper Hell') -> THEN the Scions meeting; NEVER place Minfilia's meeting before Sastasha / the Water crystal.
- REVEAL: the Ascians exist only as a SHADOWY BACKGROUND force / foreshadowing — there is NO named on-screen Ascian confrontation yet. The first NAMED Ascian appears later (Lahabrea at Toto-Rak, L4). A masked figure may at most be GLIMPSED as foreshadowing (campaign color), never named here.
- GATED: Ascian names/goals, Zodiark, the source of the party's tempering-immunity.

#### L3 — Three cities · tribal threats
- IN-SCENA: the beast tribes (Amalj'aa, Kobold, Sylph, Ixal, Sahagin) and their Primal worship are established; the tempered/enthralled faithful are shown.
- REVEAL: Primals drain the land's aether and TEMPER (enthrall) their worshippers (common knowledge).

#### L4 — Ifrit (Fire) · Toto-Rak (Lightning)
- IN-SCENA: Ifrit (Bowl of Embers) — the Amalj'aa summon Ifrit; the tempering wave hits the party but the ECHO lets them RESIST (proof they are special) -> Crystal #2 FIRE.
- IN-SCENA [Toto-Rak, BEFORE the boss]: LAHABREA appears and NAMES HIMSELF ('Lahabrea of the Ascians, servant to the one true god'), mocks the defeat of Ifrit and calls the Echo an 'irksome anomaly in the aether', then unleashes the banemite (= the boss Graffias). [WIKI-VERIFIED]
- VISIONE DELL'ECO [Toto-Rak, AFTER the boss]: Echo-flashback — Garlean soldiers discuss their failure to compel the sylphs to summon Ramuh; a masked figure alludes to an 'ultimate weapon'. Hits the WHOLE party. ⚠️ reveal protetto (the 'ultimate weapon' hint).
- IN-SCENA: the sylph elder Frixio is freed -> Crystal #3 LIGHTNING. FRIXIO IS A SYLPH (binding): third-person idiolect ('Frixio vi ringrazia', 'Frixio non dimentica'), leaf/petal features, floats — NEVER moogle traits ('kupo', pom-pom, wings-of-a-bat); he is a plant-spirit, not a moogle.
- REVEAL: LAHABREA is named (an Ascian, 'servant of the one true god'); the Ascians resent the Echo. FROM THIS BEAT ON the masked man may be called Lahabrea. (This supersedes any 'keep all Ascians unnamed' save note for later beats.)
- GATED: Lahabrea possessing Thancred; the full nature of the Ultima Weapon.

#### L5 — Titan (Earth)
- IN-SCENA: the COMPANY OF HEROES — the Scions seek out the scattered veteran mercenaries once famed for felling Titan and Leviathan in a past age (disbanded after the Calamity); from them the party learns of the aetheryte that leads into Titan's sanctuary in O'Ghomoro. [WIKI-VERIFIED]
- IN-SCENA: the Kobolds summon TITAN (The Navel) -> Crystal #4 EARTH.

#### L6 — Stone Vigil (Ice) · Garlean escalation
- IN-SCENA: Isgebind at the Stone Vigil -> Crystal #5 ICE.
- IN-SCENA: Cid Garlond and the Enterprise enter the story; the Garlean threat escalates. (Cape Westwind / Rhitahtyn sas Arvina is fought LATER, at L7 during Operation Archon — AFTER Garuda; see L7.)
- REVEAL: Gaius van Baelsar's XIVth Legion is the imminent Garlean threat over Eorzea.
- GATED: the Lahabrea-Thancred link.

#### L7 — Garuda (Wind) · Ultima Weapon · Castrum -> Praetorium -> Porta Decumana
- IN-SCENA: Garuda (Howling Eye) — the Ixal summon Garuda -> Crystal #6 WIND -> Blessing COMPLETE.
- IN-SCENA: the ULTIMA WEAPON appears and ABSORBS the essences of Ifrit / Titan / Garuda.
- IN-SCENA: Cape Westwind — defeat Rhitahtyn sas Arvina (Gaius's officer) during Operation Archon, AFTER Garuda and BEFORE Castrum Meridianum (now a solo instance, §A14).
- IN-SCENA [Castrum Meridianum]: Operation Archon; 3 bosses — The Black Eft -> Magitek Vanguard F-1 -> Livia sas Junius (final). (No retired 'Rubricatus'; see the REVAMPED-DUTY LOCK.)
- IN-SCENA [The Praetorium]: the magitek-armour ride; Gaius van Baelsar's long speech ('Eorzea built on lies...'); Mark II Magitek Colossus; Nero tol Scaeva; Gaius defeated. [WIKI-VERIFIED]
- IN-SCENA [The Porta Decumana]: Ultima Weapon fight — the Blessing strips its stolen essences; LAHABREA is revealed to be POSSESSING THANCRED (speaking through / controlling him); after Gaius falls Lahabrea takes over; the party defeats Lahabrea and he is EXPELLED from Thancred (the Light banishes the Darkness). [WIKI-VERIFIED]
- REVEAL: Lahabrea was possessing Thancred all along; the Ultima Weapon / the Ultima spell; Gaius defeated.
- GATED: the Zodiark/Hydaelyn cosmic truth, the Rejoining, the Ascian endgame.

#### L8 — Post-ARR: the Seventh Astral Era (2.1-2.55) — ARR's densest story stretch, split by patch
*(All beats below are wiki-verified. The CRYSTAL TOWER gate — Labyrinth of the Ancients / Syrcus Tower / World of Darkness — runs across 2.1-2.5, complete before HW.)*

##### 2.1 (A Realm Awoken):
- IN-SCENA: the Scions LEAVE the Waking Sands and found THE RISING STONES (Revenant's Toll, Mor Dhona) to escape Syndicate/Lolorito entanglement; Minfilia's guardian F'lhaminn revealed alive.
- IN-SCENA: a white-robed Ascian, ELIDIBUS the Emissary, visits Minfilia and speaks of ending hostilities through the Echo.
- IN-SCENA: Good King Moggle Mog (the Mogglesguard) — an Ascian-orchestrated summoning; it dissolves into aether, confirming Ascian involvement.
- REVEAL: ELIDIBUS is named (an Ascian Emissary); the Ascians actively manipulate beast-tribe summonings.
- GATED: Elidibus's TRUE nature (a living Primal / the heart of Zodiark) — SB->ShB.

##### 2.2 (Through the Maelstrom):
- IN-SCENA: the Doman refugee crisis (Lady Yugiri); the Syndicate/Lolorito deny sanctuary; Raubahn & Alphinaud reroute the Domans to Revenant's Toll.
- IN-SCENA: the Sahagin summon LEVIATHAN; the party defeats it aboard the Whorleater. [Trial]
- ALTROVE / REVEAL: Urianger brings dire news — the Isle of Val (home of the Students of Baldesion) is destroyed by a cataclysmic spell.

##### 2.3 (Defenders of Eorzea):
- IN-SCENA: the sylphs summon RAMUH (The Striking Tree); Ramuh RECOGNIZES the party's Crystal of Light and grants a trial by combat rather than immediate destruction. [Trial]
- IN-SCENA: the CRYSTAL BRAVES are FOUNDED by Alphinaud — a realm-wide force beyond national borders. [sets up the 2.55 betrayal]
- REVEAL: Teledji Adeledji's conspiracy seed (Omega, an Allagan weapon beneath the Carteneau Flats); and HYDAELYN has fallen SILENT since the Empire's defeat.

##### 2.4 (Dreams of Ice):
- IN-SCENA: Ishgard reaches out — Ser Aymeric (and Lord Haurchefant at Camp Dragonhead) requests aid watching Midgardsormr's remains but REFUSES to rejoin the Alliance.
- IN-SCENA: 'Lady Iceheart' and her heretics summon SHIVA by offering her own body as the vessel (Snowcloak dungeon -> The Akh Afah Amphitheatre). [dungeon + trial]
- REVEAL: Lady Iceheart = YSAYLE (a future Heavensward ally); (side) the Ivy = Flame Marshal Eline Roaille, the imperial spymaster, unmasked.

##### 2.5 (Before the Fall, Part 1):
- IN-SCENA [An Uninvited Ascian]: Moenbryda & the party field-test aetheric syphons (white auracite); NABRIALES 'the Paragon' steals the broken Tupsimati and opens a rift; the party pursues into the void; MOENBRYDA sacrifices her own life-force so the party can DESTROY Nabriales PERMANENTLY (the FIRST permanent Ascian kill) — and dies. [WIKI-VERIFIED]
- NOTE (CT inlined - see the CRYSTAL TOWER ARC block, end of Arc 1): the World of Darkness raid (the Cloud of Darkness driven back) is a MID-ARC beat of the inlined Crystal Tower arc, NOT its conclusion and NOT tied to 2.5 here; the CT arc is played contiguously after 'Build on the Stone' and CLOSES at 'The Light of Hope' (G'raha seals himself). Do NOT stage a CT conclusion / tower-sealing at 2.5.
- REVEAL: an Ascian can be permanently destroyed with enough Light + white auracite; the Ascians serve 'the one true god'.

*2.55 (Before the Fall, Part 2) — the ARR->HW bridge:*
- IN-SCENA [The Keeper of the Lake]: MIDGARDSORMR's specter — Hydaelyn marks the party as Her chosen; Midgardsormr STRIPS the Blessing (snuffs the 6 crystals, Ch.5.6) and binds himself to them as a tiny vessel (the Dragonsong War truth begins; Garlean Agrius wreck).
- IN-SCENA [The Steps of Faith]: the Dravanian Horde (the dragon Vishap) sieges Ishgard; the party defends the bridge (now a SOLO instance, §A14).
- ALTROVE / IN-SCENA [The Parting Glass — the Bloody Banquet of Ul'dah]: Sultana Nanamo Ul Namo is POISONED; the party is FRAMED for regicide; Raubahn kills Teledji in fury, then Ilberd SEVERS Raubahn's arm and reveals the CRYSTAL BRAVES betrayal (Monetarist agents); the Scions scatter (Y'shtola/Minfilia collapse the tunnel); flight via the Enterprise to Coerthas (Haurchefant). [WIKI-VERIFIED]
- REVEAL: Ilberd and the Crystal Braves are traitors (the coup in Ul'dah); the Blessing is now SEALED — so in HW defeated Ascians can't be permanently killed and Hydaelyn's ward is gone; the ECHO still protects from Tempering (Ch.5.6).
- GATED: the fates of Minfilia / Y'shtola (kept ambiguous); all Heavensward reveals.

### Lvl 1 - The Echo awakens
- **BEAT:** see ARR Manifest L1 above.
- **ZONE:** starting city + starting zones (Black Shroud / La Noscea / Thanalan).
- **GM NOTES:** the Echo is the party's shared gift (Warriors of Light).
- `[REC]` Hildibrand - "The Three Collectors" (Ul'dah).

### Lvl 2 - Crystal #1 (Water) + the Scions
- **BEAT:** see ARR Manifest L2 above.
- **ZONE:** starting city; Vesper Bay (Waking Sands).
- **MSQ DUNGEONS (order):** Sastasha -> The Tam-Tara Deepcroft -> Copperbell Mines.
- *** WATER CRYSTAL (#1) ***

### Lvl 3 - The three cities / tribal threats
- **BEAT:** see ARR Manifest L3 above.
- **ZONE:** Thanalan / Black Shroud / La Noscea.
- **GM NOTES:** seed Enthrallment.
- `[OPT]` optional ARR themed dungeons. `[CUT]` courier between disconnected zones.

### Lvl 4 - Ifrit (Fire) + Frixio (Lightning)
- **BEAT:** see ARR Manifest L4 above.
- **ZONE:** Thanalan (Amalj'aa); Black Shroud (Sylph).
- **MSQ TRIAL:** The Bowl of Embers (IFRIT). **MSQ DUNGEON:** Thousand Maws of Toto-Rak.
- *** FIRE CRYSTAL (#2) + LIGHTNING (#3) ***
- **GM NOTES:** Ifrit = first school of MECHANICS (Eruption, Nail, Incandescence).
- **TRIAL PIN (Ifrit / The Bowl of Embers):** FIRE. Arena = a volcanic crater with a raised rim (the rim/edges are SAFE from the Vulcan Burst knockback — no fall-death here). Boss = a towering demon of living red flame, great curved horns, cloven hooves. Wipe/phase = the INFERNAL NAIL at 50% → Hellfire if the Nail isn't destroyed in time. (Moves: Incinerate, Eruption, Vulcan Burst, Radiant Plume.) [CGW-verified]

### Lvl 5 - Titan (Earth)
- **BEAT:** see ARR Manifest L5 above.
- **ZONE:** La Noscea (O'Ghomoro).
- **MSQ DUNGEONS (order):** Haukke Manor -> Brayflox's Longstop.
- **MSQ TRIAL:** The Navel (TITAN).
- *** EARTH CRYSTAL (#4) ***
- **GM NOTES:** Titan = Landslide (knockback), Weight of the Land, Titan's Heart (see Section A Ch. 9).
- **TRIAL PIN (Titan / The Navel):** EARTH. Arena = a bare rocky platform INSIDE the volcanic caldera at O'Ghomoro — magma/lava in the SURROUNDINGS is canon (it IS inside a volcano), so volcanic ambience is fine; but the platform itself is rock and TITAN IS NOT A FIRE CREATURE. Instant-death = knocked OFF the platform edge by the shockwave (Landslide) into the depths below (a FALL — not a lava-pool boss theme). Boss = a BIPEDAL colossus of living brown ROCK: a massive torso on stout rock legs, glowing molten cracks between the plates; he STANDS and STOMPS (Tumult / Geocrush) — NOT a legless torso anchored to the ground, NOT obsidian dripping fire. Phase = the HEART exposed at 50% → Earthen Fury if not destroyed (survivable). (Moves: Rock Buster, Mountain Buster tank buster, Weight of the Land, Landslide, Tumult, Rock Tomb/Granite Gaol.) [CGW-verified] FAILURE SHAPES (observed): Titan as a fire/magma primal (he is EARTH — only the ENVIRONMENT is volcanic); Titan drawn 'legless' (he has legs and stomps).
- `[REC]` Thornmarch (GOOD KING MOGGLE MOG) - OPTIONAL trial (not MSQ).

### Lvl 6 - Stone Vigil / Isgebind (Ice)
- **BEAT:** see ARR Manifest L6 above.
- **ZONE:** Coerthas (Stone Vigil).
- **MSQ DUNGEON:** The Stone Vigil (Isgebind).
- *** ICE CRYSTAL (#5) ***
- **GM NOTES:** pivot toward Garlemald; introduce Cid and the Enterprise.

### Lvl 7 - Garuda (Wind) + Ultima Weapon + Praetorium (Climax 2.0)
- **BEAT:** see ARR Manifest L7 above.
- **ZONE:** northern Black Shroud; Castrum Meridianum; The Praetorium.
- **MSQ TRIAL:** The Howling Eye (GARUDA); Cape Westwind (RHITAHTYN, solo, AFTER Garuda); The Porta Decumana (ULTIMA WEAPON).
- **TRIAL PIN (Garuda / The Howling Eye):** WIND. Arena = a high stone aerie with DESTRUCTIBLE STONE PILLARS used as cover (hide behind a pillar for Mistral Song; the hazard is wind, not a fall). Boss = a harpy — a winged woman with taloned feet and storm-grey plumage. Adds = Razor Plumes (kill fast); phase-2 = Eye of the Storm (whirlwind with a safe eye). (Moves: Downburst, Wicked Wheel, Slipstream, Mistral Song, Aerial Blast.) [CGW-verified]
- **TRIAL PIN (Ultima Weapon / The Porta Decumana):** NOT a primal — a Garlean MAGITEK superweapon that ABSORBED the aether of Ifrit/Titan/Garuda; theme = magitek + the three stolen aspects (fire/earth/wind), climaxing in ULTIMA. Arena = the Porta Decumana battle platform. Boss = a colossal humanoid war-machine. Reproduces the absorbed primals' signature moves, then Ultima (05 Ch.9 / §B10). [WIKI-VERIFIED via 08.1]
- **MSQ DUNGEONS (order):** Castrum Meridianum -> The Praetorium.
- *** WIND CRYSTAL (#6) -> BLESSING OF LIGHT COMPLETE ***
- **GM NOTES:** the finale of the "first film". Spoiler: of the Ascians, only Lahabrea. STRUCTURE (binding, CURRENT post-6.1 versions — 06 §A14): this finale spans MULTIPLE beats — Castrum Meridianum (The Black Eft → Magitek Vanguard F-1 → Livia sas Junius) → The Praetorium (magitek-armour ride → Mark II Magitek Colossus → Nero tol Scaeva → Gaius van Baelsar) → The Porta Decumana (the Ultima Weapon, its OWN trial; Lahabrea expelled from the possessed ally here) — ONE major fight per 'continua', NEVER a single boss-rush (06 §B12). Reproduce each boss's canonical mechanics (06 §B10). Ignore the MMO player-count; build for the party.

### Lvl 8 - Post-ARR (2.1-2.55): the Braves, the Tower, the Seal
- **BEAT:** see ARR Manifest L8 (2.1-2.55) above.
- **ZONE:** Mor Dhona; Coerthas (Snowcloak); Ul'dah; The Keeper of the Lake.
- **MSQ TRIALS (order):** The Whorleater (LEVIATHAN, 2.2) -> The Striking Tree (RAMUH, 2.3) -> The Akh Afah Amphitheatre (SHIVA, 2.4).
- **TRIAL PIN (Leviathan / The Whorleater):** WATER. Arena = the pitching DECK of the ship Whorleater; hazard = Body Slam knockback/slide across the tilting deck. Boss = a vast blue sea-serpent — its HEAD and TAIL are two separate targets that mirror HP. Wipe = Tidal Wave unless the ELEMENTAL CONVERTER is triggered in time. (Moves: Body Slam, Tidal Roar, Dread Tide tank buster, Spinning Dive, Grand Fall.) [CGW-verified]
- **TRIAL PIN (Ramuh / The Striking Tree):** LIGHTNING. Arena = a forest clearing at the Striking Tree where LIGHTNING ORBS accumulate on the ground (raising his damage — collect/manage them). Boss = a towering white-bearded storm-sage, robed, a staff of levin in hand. Adds = Grey Arbiters → Judgment Bolt wipe if they survive. (Moves: Shock Strike tank buster, Thunderstorm, Chaotic Strike/Terror, Rolling Thunder tethers.) [CGW-verified]
- **TRIAL PIN (Shiva / The Akh Afah Amphitheatre):** ICE. Arena = an icy amphitheatre whose EDGE freezes anyone who touches it into a boulder, with Thin Ice sliding (Permafrost = hold still). Boss = an elegant azure ice-woman (the heretic Iceheart's borrowed primal form), cycling sword/staff/unarmed stances. Phase = Diamond Dust (party AoE after adds) + Dreams of Ice stacking soft-enrage. (Moves: Icebrand conal tank buster, Glacier Bash stun, Icicle Impact.) [CGW-verified]
- **MSQ DUNGEONS:** Snowcloak (2.4); The Keeper of the Lake (2.55).
- **CRYSTAL TOWER (inline mandatory MSQ flow - see the CRYSTAL TOWER ARC block at the end of Arc 1):** seeded at 'Laying the Foundation' (2.1), played as a fixed ~13-beat arc after 'Build on the Stone' via CID, exit to 2.2 'Still Waters'. Lore: Allagan / Xande / Cloud of Darkness / Bahamut=Dalamud / G'raha (ShB Exarch = GATED). Complete before HW.
- *** END OF L8: MIDGARDSORMR SNUFFS THE 6 CRYSTALS (Blessing sealed) ***
- **GM NOTES:** without the Blessing, in HW defeated Ascians can't be permanently killed (they flee); the ECHO still keeps the party Tempering-safe.
- `[REC]` Hildibrand continues; Primal Fear -> Odin; Relic -> Chimera/Hydra.
- *END OF ARC 1 -> flight to Coerthas: HEAVENSWARD begins (lvl 9).*

---

---

## CRYSTAL TOWER ARC (binding - INLINE MANDATORY MSQ FLOW; FROZEN v3.13, wiki-audited)
**WHAT / WHERE:** the Allagan Crystal Tower, unearthed by the Seventh Umbral Calamity, looming over Mor Dhona. Run by the NOAH expedition (NOAH = Nominated Observers of Artifacts Historical - the backronym coined by G'RAHA TIA; a collective of the Sons of Saint Coinach: RAMMBROES, the Garlond Ironworks: CID/Biggs/Wedge, the Students of Baldesion: G'RAHA, and the Adventurers' Guild) camped at Saint Coinach's Find. Played as ONE fixed contiguous arc, NOT a side gate. NO MID-ARC EXIT: between the raids (Labyrinth -> For Prosperity -> Syrcus Tower -> World of Darkness -> The Light of Hope) the 'prossimo step' / [Info GM] handoff ALWAYS points to the NEXT Crystal Tower beat, NEVER to the mainline MSQ - do NOT print 'riprende la 2.2' / 'Still Waters' / 'parlare con Y'shtola' and do NOT insert a return-to-Mor-Dhona / Minfilia / Y'shtola bridge scene mid-arc; the mainline 2.2 (Still Waters) resumes ONLY after 'The Light of Hope' is played (per the EXIT anchor). This is the SETUP for the ShB Crystal Exarch reveal (08.1 ShB L18).

**CANONICAL QUESTLINE (wiki-verified - Chronicles of a New Era, The Crystal Tower):** Legacy of Allag (2.1; giver Outlandish Man, Mor Dhona; PREREQ 'The Ultimate Weapon') -> Sanding It Down (2.1) -> A Performance for the Ages (2.1) -> [Labyrinth of the Ancients raid, 2.1] -> For Prosperity (2.2) -> [Syrcus Tower raid, 2.3] -> [The World of Darkness raid, 2.4] -> The Light of Hope (2.5; giver Rammbroes, Mor Dhona; 'end of the MSQ requirement'). NAMING (binding): the CUT fetch-errands **Sanding It Down** and **A Performance for the Ages** are NEVER surfaced as played beats NOR as an [Info GM] 'apre' target (Cid already sourced the crystals - one line; see CAMPAIGN DIVERGENCE); the arc's beats/[Info GM] use ONLY the substantive CT questline quests (Legacy of Allag -> For Prosperity -> The Light of Hope) plus the duty names.

**CAMPAIGN DIVERGENCE (custom entry - binding; this part is intentionally more custom than canon):** the ENTRY HOOK is REPLACED. In canon the party is hooked by the Outlandish Man (Legacy of Allag) and gathers four beast-tribe crystals before the way opens. In THIS campaign that fetch-chain is CUT: after 'Build on the Stone', CID comes IN PERSON to THE RISING STONES (Le Pietre Risorte, Revenant's Toll) - a visit to the Scions' new home AND the news that the Garlond Ironworks have finished the crystal fangs and cracked the Tower's Allagan defenses. Cid already sourced the needed crystals at the Ironworks (a one-line nod, NEVER a fetch beat). Cid then escorts the party east and introduces them to the rest of NOAH. The DUTIES and the rest of the questline (Labyrinth -> Syrcus -> World of Darkness -> The Light of Hope) stay canonical.

**ENTRY ANCHOR (MSQ) - binding:**
- SEED at 'Laying the Foundation' (2.1, first arrival at Revenant's Toll): SLAFBORN / a Son of Saint Coinach notes the Calamity-unearthed Tower and the NOAH expedition camped at Saint Coinach's Find (Rammbroes, G'raha, Cid) who CANNOT yet breach the Allagan defenses. INTEREST ONLY; the Tower is HARD-LOCKED.
- NO PULL-FORWARD: if the party goes early, NOAH is at work but the way is still sealed - soft diegetic defer ('we'll send word once we breach it'). Do NOT start the arc early (prevents MSQ desync / skipped 2.1 beats).
- FIXED TRIGGER (custom): after 'Build on the Stone' (Rising Stones founded, end of 2.1), CID ARRIVES IN PERSON AT THE RISING STONES - he wants to see the Scions' new home, and he brings word that the crystal fangs are finished and the Tower's defenses can be broken. This ON-SITE arrival (NOT the canonical Outlandish Man) is the hook -> the CRYSTAL TOWER ARC begins as a FIXED, contiguous MSQ beat. The Legacy-of-Allag crystal-gathering errands are CUT (Cid has already procured the crystals at the Ironworks - one line, never played).
- PLAY IN FULL (binding, anti-dry): Entry-1 = Cid's arrival at the Rising Stones + the narrated JOURNEY BRIDGE east to Saint Coinach's Find (vivid, never a jump-cut) + Cid INTRODUCES the party to Rammbroes and G'raha at the NOAH camp; the recruitment + G'raha introduction is a SUBSTANTIVE beat played in FULL, NEVER hard-condensed nor announced as condensed (A1).
- ENTRY-2 = at the TOWER GATE (southeast of Saint Coinach's Find), CID demonstrates the finished crystal fangs on the Allagan elemental-statue defenses; the defenses shatter; the party steps into the Labyrinth of the Ancients. (The gate breach is a set-piece - keep it whole; do NOT burn it inside Entry-1's dialogue.)
- EXIT: on 'The Light of Hope', return to the 2.2 opener 'Still Waters' (Mor Dhona -> same zone; clean handoff; NO MSQ pieces skipped, because all of 2.1 through Build on the Stone is already complete).
- MANDATORY: the arc MUST be completed before the jump to Heavensward (loose end: the Tower & G'raha's fate).

**[A] SAVE CONVENTION during the CT arc (binding - answers 'do we save the quest or the dungeon name?'):** the save [A] 'Missione MSQ corrente (EN)' during this arc = the owning CT QUESTLINE QUEST - **Legacy of Allag** (Entry-1/Entry-2 + Labyrinth of the Ancients), **For Prosperity** (Syrcus Tower), **The Light of Hope** (The World of Darkness + the seal) - NEVER a DUTY/raid name. A duty is played INSIDE the quest, so 'Labyrinth of the Ancients' / 'Syrcus Tower' / 'The World of Darkness' belong in 'Ultimo step completato' (e.g. 'completato il Labyrinth of the Ancients'), NEVER in the mission field. These three CT questline titles are VALID [A] mission titles for MISSION-IN-INDEX (06 §B24) even though they are not listed in the 08.2 chain index - treat them as index-valid for the duration of the CT arc. (This mirrors normal MSQ: the mission is always the owning quest, the dungeon is its [duty] step.)

### CRYSTAL TOWER CANONICAL CUTSCENE & REVEAL MANIFEST (binding - anti-drop / anti-invent - FROZEN v3.13, wiki-audited)
**SPECIFICS:** same role & legend as the other 5 manifests (shared block above). The full beat-by-beat IN-SCENA sequence (Entry-1/Entry-2/Labyrinth/Syrcus/World of Darkness/The Light of Hope) is NOT repeated here — it lives in the CRYSTAL TOWER SPINE below, which carries the identical binding weight (never drop/invent/reorder a beat listed there). This block adds only the REVEAL/GATED data not already explicit in the spine:
- REVEAL (record as known here, state derived, Ch.19.3): G'raha & the Royal Eye; the Allagan/Xande/Amon/Cloud-of-Darkness history; BAHAMUT = DALAMUD; the Tower sealed with G'raha inside.
- GATED (WARNING ShB): that G'raha will RETURN as the CRYSTAL EXARCH, and the ~200-year-future origin (payoff ShB L18) - NEVER named or anticipated here. (The self-seal 'wake when Eorzea reaches Allagan heights' IS shown here - that part is NOT gated.)

### CRYSTAL TOWER SPINE (coarse, encounter/lore-anchored - ~13 beats; duties in FEWEST COMPLETE CHUNKS, never micro-sliced; ALWAYS played in full, never condensed - DATA KERNEL 08.1)
- **[Entry-1 - Cid at the Rising Stones + recruitment/lore, FULL substantive beat]** CID arrives at THE RISING STONES (sees the Scions' new home; brings word the crystal fangs are ready); the narrated journey east to Saint Coinach's Find (vivid bridge, NEVER a one-line jump-cut, NEVER announced as condensed); the NOAH camp; Cid introduces RAMMBROES + Sons of Saint Coinach; MEETING G'RAHA (enthusiasm, the Royal Eye mystery, the Tower's history) - room to breathe. (The crystal-gathering errands are CUT - Cid already sourced them at the Ironworks, one line.)
- **[Entry-2 - breach/enter, the Tower gate]** at the Tower gate CID demonstrates the crystal fangs on the elemental defenses; the Allagan defenses shatter; step into the Labyrinth.
- **[Labyrinth of the Ancients]** canonical roster (wiki): BONE DRAGON -> [Atomos] -> THANATOS -> [Vassago] -> KING BEHEMOTH -> PHLEGETHON. The FOUR named bosses are the ONLY statted fights; the TWO alliance-gates (**Atomos**, **Vassago**) are NON-COMBAT ENIGMA-INTERLUDES (§B12 / §E1) - pinned as puzzles, NEVER a statted fight and NEVER a Pacchetto Incontro (we already have 4 bosses - do NOT add a 5th). The puzzle CONTENT is left to §E1/§B12 - only the non-combat tag is pinned here. Duties in FEWEST COMPLETE CHUNKS:
  1. Enter the labyrinth (Allagan guardians/traps); BONE DRAGON (adds: PLATINAL - destroy them to stop its revival) -> [Atomos enigma].
  2. THANATOS (invulnerable except under the Magic Pot's Astral Light; SANDMAN adds strike the pots) -> [Vassago enigma] -> KING BEHEMOTH (Comet-cover / Ecliptic Meteor / Iron Giant add).
  3. PHLEGETHON (final) -> G'raha debrief (Allagan revolutionary; first Allag exposition).
- **[Syrcus Tower - 4 beats]**
  1. Doga & Unei help open the gate; ascent into the principal spire; SCYLLA.
  2. The Allagan truth (Xande / Amon / the Cloud-of-Darkness pact); BAHAMUT = DALAMUD lore; The Braid (Doga's/Unei's clones) + GLASYA LABOLAS.
  3. AMON (the technologist who resurrected Xande).
  4. XANDE (final): the nihilist wish; the Voidgate opens.
- **[The World of Darkness - 3 beats]**
  1. Into the void: ANGRA MAINYU / QUEEN SCYLLA.
  2. The void gauntlet: FIVE-HEADED DRAGON / ATOMOS / CERBERUS. (4-PG milestone conversion: group the minor bosses into coherent chunks per 06 B12 signature-preservation; keep the setpiece whole.)
  3. CLOUD OF DARKNESS (final): the void's sovereign driven back.
- **[The Light of Hope - 1 beat, closer]** THE SEAL: Doga & Unei infuse G'raha; the SALINA/DESCH lineage revealed; G'raha SEALS HIMSELF in the Tower with the Royal Eye. Rammbroes @ Mor Dhona -> RETURN to the MSQ (2.2 'Still Waters'). (This beat is LOAD-BEARING for the ShB L18 Exarch reveal - ALWAYS played in full.)

### BAHAMUT / DALAMUD (lore tie) + optional deep-dive
- The Syrcus exposition beat makes the Bahamut -> iron-sphere -> DALAMUD link explicit (why it matters: it is the very thing tied to the Calamity the campaign opens after). Render as lore/depth, reveal-gated as above.
- `[REC]` (optional, NOT mandatory): **The Binding Coil of Bahamut** - a substantial subquest tied to the Bahamut/Dalamud thread, unlockable from Mor Dhona / the Waking Sands (zone-synergic with the CT hub). Available alongside/after the CT arc; reveal-gated; never on the critical path.

**OST (in 08.OST-ARR; corrected v3.17):** Labyrinth of the Ancients = (ambient) Hubris / (battle) Ever Upwards / (final Phlegethon) Tumbling Down; Syrcus Tower = (ambient) Out of the Labyrinth / (battle) Shattered / (final Xande) Tumbling Down; World of Darkness = (ambient) Blind to the Dark / (battle) Hamartomania / (Cloud of Darkness, final) The Reach of Darkness. NOTE: 'Out of the Labyrinth' is the SYRCUS theme (the Labyrinth is HUBRIS) - the entry beat uses HUBRIS (ambient) then EVER UPWARDS at the fights.

## Arc 2 - Heavensward (lvl 9-12)
**REMINDER:** Dragonsong War; Ishgard; Estinien (Azure Dragoon) vs NIDHOGG; KING THORDAN; ASCIAN PRIME (Igeyorhm + Lahabrea). Crystals: gradual relighting, full restoration at L11. ENTHRALLMENT active until the Blessing returns. No side gate.

### HEAVENSWARD CANONICAL CUTSCENE & REVEAL MANIFEST (binding — anti-drop / anti-invent — FROZEN v3.0, wiki-audited)
**SPECIFICS:** HW carries the SEALED-BLESSING arc: OFF from L9 (defeated Ascians can't be permanently killed, Hydaelyn's ward gone; the ECHO still keeps the party Tempering-safe, Ch.5.6), relights PARTIALLY after Bismarck (L10), FULLY restored at the Ascian Prime (L11) — announce each transition per §B23. No HW revamped-duty lock (duties intact, use current wiki version).

#### L9 — Ishgard & the Dragonsong War (HW 3.0 opening)
- IN-SCENA: fleeing the Ul'dah coup, the party reaches ISHGARD; House Fortemps (Count Edmont) shelters them, vouched for by HAURCHEFANT. The Blessing is SEALED -> defeated Ascians can't be permanently killed (they flee) and Hydaelyn's ward is gone; the ECHO still protects from Tempering (Ch.5.6).
- IN-SCENA: meet Ser AYMERIC (Lord Commander of the Temple Knights) and ESTINIEN (the Azure Dragoon); the Dragonsong War, the Holy See and the heretics are established.
- IN-SCENA: YSAYLE (formerly 'Lady Iceheart') joins the party as a guide toward the dragons.
- Dungeons: The Dusk Vigil -> Sohm Al.
- GATED: the Dragonsong War's true origin (revealed at L10); the deeper Ascian cosmology.

#### L10 — The truth, Ravana, the Aery, THE VAULT (Haurchefant), Bismarck (HW 3.0 mid)
- IN-SCENA: the Churning Mists; HRAESVELGR tests Ysayle; **THE DRAGONSONG WAR TRUTH** — 1200 years ago King Thordan I and his knights slew RATATOSKR (Nidhogg & Hraesvelgr's sister), tore out and devoured her eyes for dragon-power, shattering the peace Saint Shiva had forged. [WIKI-VERIFIED]
- IN-SCENA: RAVANA (Thok ast Thok) — the Gnath primal, quelled to keep a third faction out of the war.
- IN-SCENA [The Aery]: ESTINIEN slays NIDHOGG and takes the great wyrm's TWO EYES.
- IN-SCENA [The Vault]: storming the Vault to reach the Archbishop; **HAURCHEFANT DIES** — he throws himself in front of Aymeric and the party to take a holy blast unleashed by Archbishop Thordan VII (via the Heavens' Ward). [WIKI-VERIFIED]
- IN-SCENA: BISMARCK (The Limitless Blue) — the Sea of Clouds primal; wins the key to Azys Lla. (ORDER note, verified on two sources: the Sea of Clouds ZONE is visited earlier, but the Bismarck TRIAL -- The Limitless Blue -- is fought HERE, AFTER The Vault and just before Azys Lla.) After Bismarck the crystals RELIGHT partially (reduced Blessing, §B23).
- REVEAL: the Dragonsong War's true origin; Haurchefant's death.
- GATED: Nidhogg's eyes will become a curse (patches); the Ascian cosmology.

#### L11 — Azys Lla, Ysayle's death, the Ascian Prime (Lahabrea's end), King Thordan (HW 3.0 climax)
- IN-SCENA: the assault on AZYS LLA (the Allagan floating isle); **YSAYLE DIES** — she takes Shiva's form to help disable the Agrius-class airship Gration and is shot down while shielding Cid's airship, perishing in a bloom of blue aether. [WIKI-VERIFIED]
- IN-SCENA: TIAMAT — the bound dragon recounts the Allag / Meracydia history; the dialogue relights the PENULTIMATE crystal.
- IN-SCENA [Aetherochemical Research Facility]: the ASCIAN PRIME — LAHABREA and IGEYORHM fuse; the party shatters the Prime back into two and DESTROYS Igeyorhm (Blessing / white auracite). Then Archbishop THORDAN VII KILLS Lahabrea and ABSORBS his aether to fuel his ascension — **Lahabrea's true, final end**. This relights the LAST crystal -> the BLESSING is FULLY RESTORED (Midgardsormr breaks the seal). [WIKI-VERIFIED]
- IN-SCENA [The Singularity Reactor]: KING THORDAN and his Heaven's Ward (the Knights of the Round) ascend to god-knights; the party defeats them and Thordan falls.
- REVEAL: Lahabrea permanently destroyed; the Blessing fully restored; Thordan's ascension and fall.
- GATED: the full Zodiark/Hydaelyn cosmology (touched next beat); Nidhogg's eyes endure.

#### L12 — the HW patches (3.1-3.5): Nidhogg's return, the cosmology, Shinryu
##### 3.1 (As Goes Light, So Goes Darkness):
- IN-SCENA: Ishgard's faith crisis after the truth; the search for a future where man and dragon may coexist (Saint Endalim's Scholasticate).
- IN-SCENA: the WARRIORS OF DARKNESS (strangers from another world) appear and clash with the party; the Void Ark / Sky Pirates arc opens.
- GATED: the Warriors of Darkness' true origin (the First) — ShB.

##### 3.2 (The Gears of Change):
- IN-SCENA [The Antitower]: the Scions find MINFILIA merged with Hydaelyn in the aetherial sea; **the cosmology is revealed** — Light & Dark once in balance; Zodiark's overreach; Hydaelyn banished him (as the moon); reality fractured into THIRTEEN reflections; the Ascians engineer Calamities to REJOIN the worlds (seven already consumed). **MINFILIA sacrifices herself** to pass on this truth (the Word of the Mother). [WIKI-VERIFIED] — NOTE: this OVERLAPS Ch.1.6's EW-gated 'Hydaelyn & Zodiark' entry; canon REVEALS this cosmology HERE (HW 3.2): REVEAL it — Zodiark and Hydaelyn's existence, the world split into THIRTEEN reflections, and the Ascians' REJOINING. It is NOT gated to EW (Ch.1.6 A updated). Defer ONLY the deepest truths: that Venat IS Hydaelyn and the Ancients/Amaurot (ShB), and the Final Days / Meteion / Elpis (EW).
- IN-SCENA: the peace conference at Falcon's Nest (Aymeric + the dragon Vidofnir; the Shiva/Hraesvelgr relief) is SHATTERED when ESTINIEN, now POSSESSED by NIDHOGG through the two eyes, lances Vidofnir — the 'final chorus' begins.
- REVEAL: the Zodiark/Hydaelyn origin + the 13 reflections + the Rejoining (see note); Minfilia's sacrifice; Estinien possessed by Nidhogg.

##### 3.3 (Revenge of the Horde):
- IN-SCENA [Sohr Khai]: the party rides Hraesvelgr's kin; Hraesvelgr duels Nidhogg's shade, loses a wing and entrusts ONE of his own EYES to the party for power.
- IN-SCENA [The Final Steps of Faith]: empowered by Hraesvelgr's eye, the party defeats Nidhogg's shade on the Steps of Faith bridge; with Alphinaud — aided by the spirits of HAURCHEFANT and YSAYLE — they wrest Nidhogg's two eyes from Estinien's armour and cast them into the abyss; **ESTINIEN is freed and survives**. [WIKI-VERIFIED — this trial is PATCH 3.3, not 3.56]
- REVEAL: the Dragonsong War ends; Estinien saved.

##### 3.4 (Soul Surrender):
- IN-SCENA: aftermath — a new dawn in Ishgard; Estinien recovers; the Warriors of Darkness thread continues/closes. A quieter bridge patch.

*3.5 (The Far Edge of Fate) — the bridge to Stormblood:*
- IN-SCENA: the fragile peace of Ishgard is sealed (Aymeric; man and dragon).
- IN-SCENA [Baelsar's Wall]: ILBERD, revealed as THE GRIFFIN, sacrifices his own Ala Mhigan followers and himself and uses NIDHOGG'S EYES to summon the primal SHINRYU — a nihilistic bid to ignite open war with Garlemald.
- IN-SCENA: PAPALYMO sacrifices himself, casting Louisoix's binding spell, to SEAL Shinryu in a prison of light. [WIKI-VERIFIED]
- REVEAL: Ilberd = the Griffin; Shinryu summoned; Papalymo's death.
- GATED: Shinryu's escape, Zenos and the Ala Mhigan/Doman liberation — SB.

### Lvl 9 - Ishgard and the Dragon War
- **BEAT:** see HW Manifest L9 above.
- **ZONE:** Coerthas Western Highlands; Ishgard (Foundation/Pillars); Dravania.
- **>> WITHOUT THE BLESSING:** defeated Ascians escape/return and Hydaelyn's ward is gone; the ECHO still keeps the party Tempering-safe (Section A Ch. 5.6).
- **MSQ DUNGEONS (order):** The Dusk Vigil -> Sohm Al.
- **GM NOTES:** dark/gothic tone; faith, dogma, heretics and dragons.

### Lvl 10 - Ravana, Nidhogg, Bismarck
- **BEAT:** see HW Manifest L10 above.
- **ZONE:** The Churning Mists (Ravana/Gnath); Dravania (Aery); The Sea of Clouds (Bismarck).
- **MSQ DUNGEON/TRIAL (ORDER):** Thok ast Thok (RAVANA) -> The Aery (Estinien slays NIDHOGG) -> The Vault -> The Limitless Blue (BISMARCK).
- *** CRYSTALS: partial relighting after Bismarck (reduced Blessing) ***
- `[REC]` Gods of Eld -> Warring Triad: Sephirot, Sophia, Zurvan (Ishgard).
- `[REC]` Void Ark (Shadow of Mhach) alliance: "Sky Pirates", Ishgard.

### Lvl 11 - Azys Lla, Ascian Prime & King Thordan (Climax 3.0)
- **BEAT:** see HW Manifest L11 above.
- **ZONE:** Azys Lla; Aetherochemical Research Facility; Singularity Reactor.
- **MSQ DUNGEON/TRIAL (ORDER):** The Great Gubal Library -> The Aetherochemical Research Facility (ASCIAN PRIME) -> The Singularity Reactor (KING THORDAN).
- *** BLESSING OF LIGHT FULLY RESTORED (seal broken) ***
- **GM NOTES:** double climax (Ascian Prime + Thordan).

### Lvl 12 - Post-HW (3.1-3.56): the end of the Dragon War
- **BEAT:** see HW Manifest L12 (3.1-3.56) above.
- **ZONE:** Ishgard; The Churning Mists (Sohr Khai); Gyr Abania (Baelsar's Wall).
- **MSQ DUNGEONS:** The Antitower (3.2); Sohr Khai (3.3); Xelphatol (3.4); Baelsar's Wall (3.5).
- **MSQ TRIAL:** The Final Steps of Faith (NIDHOGG, 3.3).
- **GM NOTES:** the WARRIORS OF DARKNESS (3.1-3.4, from the First) are ShB lore seeds.
- *END OF ARC 2 -> Baelsar's Wall: STORMBLOOD begins (lvl 13).*

---

## Arc 3 - Stormblood (lvl 13-15)
**REMINDER:** liberation of ALA MHIGO (Gyr Abania) and DOMA (Othard); antagonist ZENOS yae Galvus; SHINRYU; TSUKUYOMI. Blessing INTACT. No side gate.

### STORMBLOOD CANONICAL CUTSCENE & REVEAL MANIFEST (binding — anti-drop / anti-invent — FROZEN v3.0, wiki-audited)
**SPECIFICS:** in SB the Blessing is INTACT throughout (the HW Enthrallment mechanic, Ch.5.6, does NOT apply here). No SB revamped-duty lock (duties intact, use current wiki version).

#### L13 — The Ala Mhigan Resistance & the liberation of Doma (SB 4.0, part 1)
- IN-SCENA: aftermath of Baelsar's Wall — Shinryu, sealed by Papalymo, is dragged underground by the awakened Allagan weapon OMEGA (the Omega-raid seed); the party joins the ALA MHIGAN RESISTANCE at Rhalgr's Reach (Conrad, Lyse, M'naago, Alphinaud, Alisaie).
- IN-SCENA: YDA IS LYSE — she confesses she took her late sister Yda's name and mask after Yda's death; she casts them off and fights openly as herself.
- IN-SCENA [Rhalgr's Reach attack]: ZENOS yae Galvus storms the Reach, routs the Resistance and CRUSHES the party in a one-sided duel, sparing them out of contempt (not yet 'worthy prey'). Establishes Zenos as the relentless hunter and the Garlean Viceroy of Ala Mhigo.
- IN-SCENA: the voyage to Othard — Kugane; the Ruby Sea (the Kojin, the Confederacy); the Kojin summon SUSANO (The Pool of Tribute).
- IN-SCENA: the Azim Steppe — Bardam's Mettle and the NADAAM; Hien unites the Xaela and wins the right to lead; the Steppe's aid is secured.
- IN-SCENA [Doma Castle]: the liberation of Doma with Lord HIEN; the castle is FLOODED to break the garrison; Gosetsu buys time (presumed lost, later found alive).
- REVEAL: Yda's true identity (Lyse); Zenos is the Garlean crown prince/Viceroy and the party's personal nemesis.
- GATED: Zenos's artificial-Echo ('Resonant') nature and his ultimate fate; the Ascian behind the Garlean throne.

#### L14 — Lakshmi, the liberation of Ala Mhigo, Shinryu & Zenos (SB 4.0 climax)
- IN-SCENA: the Qalyana Ananta summon LAKSHMI (Emanation); FORDOLA's artificial 'Resonant' Echo helps bring her down. [Emanation is BEFORE Castrum Abania — verified.]
- IN-SCENA: the push into Gyr Abania — Castrum Abania; Specula Imperatoris; the Lochs; the storming of ALA MHIGO. CONRAD falls; LYSE takes up leadership of the Resistance; Fordola is defeated and taken.
- IN-SCENA [The Royal Menagerie]: ZENOS binds himself to the primal SHINRYU (via his artificial Resonance) and rides it; the party defeats both Shinryu and Zenos.
- IN-SCENA: ZENOS'S SUICIDE — savouring at last a 'worthy' foe, he thanks the party as his only friend and takes his own life with his blade.
- REVEAL: Ala Mhigo is free; Zenos apparently dead (Ch.1.6 D).
- GATED: the Ascian who will take Zenos's empty body; that the real Zenos survives.

#### L15 — Post-SB patches (4.1-4.56): Tsukuyomi, the false Zenos & the call to the First
*(All beats wiki-verified. The Blessing stays INTACT throughout SB.)*

##### 4.1 (The Legend Returns):
- IN-SCENA: Ala Mhigo rebuilds; Fordola imprisoned; Lyse leads the Resistance; the Domans go home (Doma's reconstruction, Yugiri, Hien).
- ALTROVE / REVEAL: ZENOS'S BODY IS MISSING from where it lay — an Ascian has claimed it. ⚠️ reveal protetto (the Ascian-in-Zenos thread).
- Dungeon: The Drowned City of Skalla.

##### 4.2 (Rise of a New Sun):
- IN-SCENA: Gosetsu is found alive with an AMNESIAC YOTSUYU (now 'Tsuyu'); ASAHI sas Brutus (Yotsuyu's adoptive step-brother) arrives under a banner of peace to arrange a prisoner exchange — secretly a fanatical Zenos-worshipper.
- ALTROVE: a physician tends a stirring patient — Zenos's body, alive. ⚠️ reveal protetto.
- Dungeon: The Burn.

*4.3 (Under the Moonlight) — Tsukuyomi:*
- IN-SCENA: confronted by her abusive adoptive parents, YOTSUYU's memories return; at the prisoner exchange Asahi triggers a summoning and Yotsuyu becomes the primal TSUKUYOMI (Castrum Fluminis). After her defeat she kills Asahi and dies. [WIKI-VERIFIED — this trial is PATCH 4.3, not 4.1.]
- REVEAL: Zenos's body is confirmed alive and worn by an Ascian (still unnamed here).

##### 4.4 (Prelude in Violet):
- IN-SCENA: the hunt for the truth of Zenos's resurrection; Hien reactivates the Allagan 'Seiryu's Wall' and the Burn is identified as fallen Azys Lla (Y'shtola). Dungeon: Hells' Lid.
- IN-SCENA [the Shadowhunter]: GAIUS van Baelsar is revealed ALIVE and confirms the Ascian wearing Zenos's body is ELIDIBUS the Emissary.
- ALTROVE [Garlemald]: EMPEROR VARIS zos Galvus and ELIDIBUS — the Empire was founded with Ascian aid; they intend to trigger further Calamities to REJOIN the reflections. ⚠️ reveal protetto (reinforces the HW 3.2 cosmology with the Empire's role).
- REVEAL: ELIDIBUS is the Ascian in Zenos's body; the Garlean-Ascian pact and the Rejoining agenda.
- GATED: Elidibus's TRUE nature (a living Primal, the heart of Zodiark — ShB 5.x); the First / the Warrior of Darkness (ShB).

*4.5 / 4.56 (A Requiem for Heroes) — the bridge to Shadowbringers:*
- IN-SCENA: the Alliance drives on Garlemald — the battle of THE GHIMLYT DARK.
- IN-SCENA: the REAL ZENOS reclaims his own body, casting ELIDIBUS out (who departs for the First), and overwhelms the party in another duel.
- IN-SCENA [the call to the First]: an ENIGMATIC FIGURE (unnamed — the Crystal Exarch) reaches across worlds and bids the party come to the First; ESTINIEN saves the Warrior before Zenos's killing blow. The Scions' spirits begin to be drawn away; the party is directed to the CRYSTAL TOWER to cross to the First.
- REVEAL: the real Zenos lives and has his body back; a summons from another world.
- GATED: everything Shadowbringers (Norvrandt, the Lightwardens, the Warrior of Darkness, the Crystal Exarch = G'raha Tia).

### Lvl 13 - The rebellion: Gyr Abania and Othard
- **BEAT:** see SB Manifest L13 above.
- **ZONE:** Gyr Abania (Rhalgr's Reach, Fringes/Peaks/Lochs); Othard.
- **MSQ DUNGEON/TRIAL (ORDER):** The Sirensong Sea -> The Pool of Tribute (SUSANO) -> Bardam's Mettle -> Doma Castle -> Emanation (LAKSHMI) -> Castrum Abania. (NOTE: Castrum Abania is the HINGE into the L14 Gyr Abania assault — the SB Manifest narrates it under L14; treat the L13/L14 split as SOFT.)
- **GM NOTES:** themes of liberation and identity; Zenos the relentless hunter.

### Lvl 14 - Zenos, Shinryu and the battle of Ala Mhigo (Climax 4.0)
- **BEAT:** see SB Manifest L14 above.
- **ZONE:** The Lochs; Ala Mhigo.
- **MSQ DUNGEON/TRIAL (ORDER):** Ala Mhigo -> The Royal Menagerie (SHINRYU).
- **GM NOTES:** Zenos = a boss with personal mechanics (see Section A Ch. 9).

### Lvl 15 - Post-SB (4.1-4.56): Tsukuyomi and the shadow of the Ascians
- **BEAT:** see SB Manifest L15 (4.1-4.56) above.
- **ZONE:** Yanxia (Castrum Fluminis); Gyr Abania; Garlemald (intro).
- **MSQ DUNGEON/TRIAL (ORDER):** The Drowned City of Skalla (4.1) -> The Burn (4.2) -> Castrum Fluminis (TSUKUYOMI, 4.3) -> Hells' Lid (4.4) -> The Ghimlyt Dark (4.5).
- **GM NOTES:** 4.5 sets up the call to the First: a direct hook to ShB.
- `[REC]` Return to Ivalice alliance: "Dramatis Personae", Kugane.
- `[REC]` The Four Lords -> Byakko, Suzaku, Seiryu (Ruby Sea).
- `[REC]` Monster Hunter collab -> Rathalos (The Great Hunt), Kugane.
- `[REC]` Hildibrand (SB) -> Kugane Ohashi (trial), Kugane.
- *END OF ARC 3 -> the call to the First: SHADOWBRINGERS begins (lvl 16).*

---

## Arc 4 - Shadowbringers (lvl 16-19)
**REMINDER:** the FIRST (Norvrandt); the PCs = WARRIOR OF DARKNESS; snuff the LIGHTWARDENS to bring back the night; TITANIA, INNOCENCE; EMET-SELCH / Amaurot; HADES. No side gate.

> **LIGHT NOTE (PURELY NARRATIVE - no mechanic):** thanks to the Blessing of Light, the PCs can ABSORB the Lightwardens' Light without becoming Sin Eaters. BUT the Blessing is NOT infallible: in lore the Light accumulates and at the climax (after Innocence) risks transforming the bearer, averted by the plot (Ardbert's intervention / the return of night). Render it ONLY as narrative tension (descriptions, doubts, signs of corruption): NO tracker, threshold or mechanical penalty.

### SHADOWBRINGERS CANONICAL CUTSCENE & REVEAL MANIFEST (binding — anti-drop / anti-invent — FROZEN v3.0, wiki-audited)
**SPECIFICS:** the Blessing is INTACT in ShB (no Enthrallment mechanic); the accumulating LIGHT is narrative tension only (see LIGHT NOTE above — NO tracker). ShB is the deep-lore arc: many long IN-SCENA cutscenes — render as DEPTH, never as branching (Ch.16.6). No ShB revamped-duty lock (duties intact).

#### L16 — Arrival in the First; Il Mheg & Titania (ShB 5.0, part 1)
- IN-SCENA: the CRYSTAL EXARCH summons the party across the Rift to the FIRST; they wake in NORVRANDT under an endless day-lit sky and reach THE CRYSTARIUM. He warns of a looming EIGHTH UMBRAL CALAMITY of Light and asks the party to become the WARRIOR OF DARKNESS and snuff the LIGHTWARDENS to restore the night. (The other Scions are drawn over across the arc: Y'shtola, Thancred with RYNE, Urianger, Alphinaud, Alisaie.)
- IN-SCENA: the FLOOD OF LIGHT — a century ago primordial Light drowned Norvrandt and birthed the Sin Eaters; it was halted by MINFILIA and her companions (her sacrifice; her successor line leads to Ryne).
- IN-SCENA: EULMORE, the decadent city feasting under the shadow of the end (Vauthry); Kholusia.
- IN-SCENA [The Dancing Plague]: TITANIA, the pixie king, the Lightwarden of IL MHEG; on its defeat the party absorbs the Light and NIGHT returns to Il Mheg (Feo Ul becomes the new Titania).
- Dungeons: Holminster Switch -> Dohn Mheg -> The Qitana Ravel.
- REVEAL: the First, the Flood of Light, the Sin Eaters, the Lightwardens, the party as the Warrior of Darkness; EMET-SELCH appears as a sardonic, ambiguous 'ally'.
- GATED: Emet-Selch's true nature; the Exarch's identity; Vauthry's Lightwarden origin; the soul of Azem.

#### L17 — Amh Araeng, Mt. Gulg & Innocence (ShB 5.0, part 2)
- IN-SCENA: Amh Araeng with RYNE (the trolley, the Talos, Nabaath Areng); the Rak'tika Greatwood (the Night's Blessed, Y'shtola's home).
- IN-SCENA: the WARRIORS OF DARKNESS of Heavensward are revealed to have been FROM THE FIRST — Ardbert's band came to the Source hoping to trigger a Calamity that would save their own dying, Light-flooded world.
- IN-SCENA [The Crown of the Immaculate]: VAUTHRY, ruler of Eulmore, ascends into the Lightwarden INNOCENCE (Mt. Gulg); on his defeat night returns to Kholusia — but the party has now drunk SO MUCH Light it risks turning into a Sin Eater itself (narrative tension only, LIGHT NOTE; Ardbert's spirit lingers at the party's side).
- Dungeons: Malikah's Well -> Mt. Gulg.
- REVEAL: the Warriors of Darkness were of the First; Vauthry's Lightwarden origin; the party's mounting Light-sickness.
- GATED: the Exarch = G'raha; Emet-Selch's Unsundered nature; Amaurot / the soul of Azem.

#### L18 — The Exarch's gambit, Emet-Selch & Amaurot (ShB 5.0, part 3)
- IN-SCENA: overflowing with Light, the party nearly transforms; the CRYSTAL EXARCH tries to ABSORB the Light into himself and vanish through the Rift to spare them — and his identity breaks open: he is G'RAHA TIA, returned through the Crystal Tower from ~200 years in the future to avert the Eighth Umbral Calamity.
- IN-SCENA [Amaurot]: EMET-SELCH is revealed as an UNSUNDERED ASCIAN — Solus zos Galvus, the founding father of Garlemald — and leads the party down into AMAUROT, his recreation of the ancient capital of the Ancients, to argue that the sundered are but half-lives unworthy of the world.
- IN-SCENA: THE SOUL OF AZEM — the party (and Ardbert) are revealed to be fragments of AZEM, the fourteenth seat of the Convocation of Fourteen, who opposed Zodiark's summoning. [This is the canonical AZEM reveal — record this reveal as known here (state derived, Ch.19.3); the campaign's 'a single Light' framing now has its name.]
- REVEAL: the Exarch = G'raha Tia; Emet-Selch = Solus / an Unsundered Ascian; the Sundering, the Convocation, Zodiark's summoning, and the party's Azem soul.
- GATED: the deepest cosmology finale (Venat IS Hydaelyn; the Final Days; Meteion — EW); Elidibus's true nature (5.3).

#### L19 — Hades, then the patches (5.1-5.5): the end of the Ascians
- IN-SCENA [The Dying Gasp]: the confrontation with HADES (Emet-Selch's true name and primal form) in the depths of the Tempest; at the brink ARDBERT's spirit MERGES with the party, granting the strength to prevail; Emet-Selch dies asking only to be REMEMBERED ('Remember us... remember that we once lived'). Night is fully restored to Norvrandt.
- REVEAL: Hades/Emet-Selch's fall; the tragedy of the Ancients.

##### 5.1 (Vows of Virtue, Deeds of Cruelty):
- IN-SCENA: the displaced Scions' souls begin to DETERIORATE on the First; G'raha and Urianger devise a return to their Source bodies via white-auracite SPIRIT VESSELS (G'raha's Allagan craft). (Side: YoRHa: Dark Apocalypse alliance opens — Komra.)

##### 5.2 (Echoes of a Fallen Star):
- IN-SCENA: the spirit vessels return most of the Scions' minds to their bodies on the Source.
- ALTROVE / REVEAL: ELIDIBUS possesses ARDBERT's body and roams the First preaching the gospel of the 'Warrior of Light' to gather faith and strengthen himself. ⚠️ reveal protetto.

*5.3 (Reflections in Crystal) — The Seat of Sacrifice:*
- IN-SCENA: ELIDIBUS, wearing the Warrior-of-Light shape, is confronted and revealed to be a PRIMAL — the HEART OF ZODIARK, sacrificed by the Ancients to summon their god, left with no will of his own but the single purpose of 'Salvation'; G'raha binds him into the Crystal Tower and the party defeats him — the TRUE END of the original Ascian trio.
- IN-SCENA: G'RAHA TIA, crystallising from overusing the Tower, transfers his soul into a spirit vessel and crosses to the SOURCE, formally joining the Scions of the Seventh Dawn.
- REVEAL: Elidibus's true nature (a living primal, the Heart of Zodiark) and his end; G'raha on the Source.
- GATED: everything Endwalker (surfaced only as 5.5 seeds below).

*5.5 (Death Unto Dawn) — the bridge to Endwalker:*
- IN-SCENA: FANDANIEL (a Sundered Ascian freed by Elidibus's fall) schemes to recreate the FINAL DAYS via aether-draining towers; ZENOS returns, hunting the party for their promised battle; the Grand Company of Eorzea unites the Alliance and the beast tribes; a woman in white warns that the star's fate now rests with the party -> Endwalker.
- GATED: the Final Days, Meteion, Venat = Hydaelyn, Ultima Thule (all EW).

### Lvl 16 - Norvrandt and the first Lightwardens
- **BEAT:** see ShB Manifest L16 above.
- **ZONE:** Lakeland (Crystarium); Kholusia (Eulmore); Il Mheg.
- **MSQ DUNGEON/TRIAL (ORDER):** Holminster Switch -> Dohn Mheg -> The Qitana Ravel -> The Dancing Plague (TITANIA, Lightwarden of Il Mheg).
- **GM NOTES:** introduce the ambiguous EMET-SELCH; the price of absorbed Light (narrative tension only, see LIGHT NOTE).

### Lvl 17 - Innocence and the Warrior of Darkness
- **BEAT:** see ShB Manifest L17 above.
- **ZONE:** Amh Araeng; Mt. Gulg; The Rak'tika Greatwood.
- **MSQ DUNGEON/TRIAL (ORDER):** Malikah's Well -> Mt. Gulg -> The Crown of the Immaculate (INNOCENCE).
- **GM NOTES:** the absorbed Light reaches its peak: risk of Sin Eater (narrative only, see LIGHT NOTE).

### Lvl 18 - Emet-Selch and Amaurot
- **BEAT:** see ShB Manifest L18 above.
- **ZONE:** The Tempest (Amaurot). **MSQ DUNGEON:** Amaurot.
- **GM NOTES:** the lore core (Azem's soul; the group's bond with the Ancients). Heavy revelations: respect the canonical beat.

### Lvl 19 - Hades (Climax 5.0) and the return
- **BEAT:** see ShB Manifest L19 (+ patches 5.1-5.5) above.
- **ZONE:** The Tempest; Source (post).
- **MSQ TRIAL (ORDER):** The Dying Gasp (HADES) -> The Seat of Sacrifice (ELIDIBUS, 5.3).
- **GM NOTES:** Hades = an epic phased boss (see Section A Ch. 9).
- `[REC]` YoRHa: Dark Apocalypse alliance: "Word about Komra", Kholusia.
- `[REC]` Sorrow of Werlyt -> Ruby/Emerald/Diamond Weapon (The Lochs).
- `[OPT]` EDEN raid (Eden's Gate/Verse/Promise): ShB optional raid content.
- *END OF ARC 4 -> return to the Source: ENDWALKER begins (lvl 20).*

---

## Arc 5 - Endwalker (lvl 20, cap)
**REMINDER:** the Final Days; ZODIARK and HYDAELYN; the journey toward the source of despair (Meteion); ELPIS (the Ancients' past); ULTIMA THULE; the final confrontation with the ENDSINGER. Level CAP at 20. No side gate. No post-EW patches. Dawntrail EXCLUDED.

### ENDWALKER CANONICAL CUTSCENE & REVEAL MANIFEST (binding — anti-drop / anti-invent — FROZEN v3.0, wiki-audited)
**SPECIFICS:** EW is played entirely at CAP (milestone L20), so this manifest is organized by STORY PHASE (zone), not by level. This arc lands the DEEPEST gated reveals (Venat = Hydaelyn, the Final Days, Meteion, Dynamis) — after ShB almost nothing remains gated. The Blessing is INTACT. Duty order: Zot -> Babil -> Storm's Crown -> Vanaspati -> The Dark Inside -> Ktisis Hyperboreia -> The Aitiascope -> The Mothercrystal -> The Dead Ends -> The Final Day (the Aitiascope is cleared BEFORE the Mothercrystal, same quest). No EW revamped-duty lock.

**Phase 1 — Sharlayan & Thavnair: the Final Days begin**
- IN-SCENA: return to the Source; OLD SHARLAYAN (the Forum; Fourchenault refuses to act; Krile); the Scions regroup and split toward Thavnair and Garlemald.
- IN-SCENA: THAVNAIR / Radz-at-Han (Vrtra, the Satrap, Matsya); the FINAL DAYS strike — despair turns people into BLASPHEMIES (aether-beasts born of anguish) under a burning sky.
- IN-SCENA [The Tower of Zot]: the Magus Sisters (Telophoroi agents); the plot around the towers rising across the star.
- REVEAL: the Final Days are HERE (blasphemies from despair); FANDANIEL and the Telophoroi are raising towers worldwide.
- GATED: Meteion; the true origin of the Final Days; Venat = Hydaelyn; Dynamis.

**Phase 2 — Garlemald: the fallen empire, Zenos & Fandaniel**
- IN-SCENA: GARLEMALD in ruin and winter; the Eorzean/Alliance relief effort; ZENOS (back in his OWN body) stalks the party, caring only for their promised duel.
- ALTROVE [the towers]: FANDANIEL — the Sundered Ascian (the persona of Amon) — gleefully nihilistic, allied with Zenos, means to trigger the Final Days for pure OBLIVION (not the Rejoining). ⚠️ reveal protetto (his end-goal / Meteion link).
- IN-SCENA [The Tower of Babil]: the magitek tower; the primal ANIMA bound within.
- IN-SCENA [Storm's Crown]: BARBARICCIA, an Archfiend of the Telophoroi.
- REVEAL: Fandaniel wants annihilation, not the Ascians' Rejoining; Zenos's single obsession.
- GATED: Meteion / the source of despair; Venat = Hydaelyn.

**Phase 3 — Mare Lamentorum (the Moon): Zodiark's truth**
- IN-SCENA: the MOON; the LOPORRITS (built by Hydaelyn as an ark to shelter mankind); the truth of ZODIARK — the Ancients summoned him NOT as a villain but to SAVE the star from the FIRST Final Days, sacrificing half their own number; Venat later opposed further sacrifice.
- IN-SCENA [Vanaspati]: back on the star, a land overrun as the Final Days spread (blasphemy).
- IN-SCENA [The Dark Inside]: ZODIARK is confronted and defeated — but this strips the star of its ancient ward, laying it bare to the Final Days.
- REVEAL: Zodiark was the Ancients' grief-born SAVIOUR (the Ascians' framing overturned); the Sundering reframed.
- GATED: Venat = Hydaelyn (imminent); Meteion; Dynamis.

**Phase 4 — Elpis (the past): Venat, Hermes & Meteion**
- IN-SCENA [time-travel to ELPIS]: the ancient world before the Sundering; VENAT (who will become Hydaelyn); HYTHLODAEUS and EMET-SELCH as they once were; the concept-creature workshops.
- IN-SCENA: HERMES — the future FANDANIEL — and his singing bird METEION, sent among the stars to find other life and the meaning of existence; she returned with only DESPAIR (all life ends), and that despair BECAME the Final Days.
- IN-SCENA [Ktisis Hyperboreia]: the pursuit of Hermes/Meteion; the catastrophe's origin is laid bare.
- REVEAL: the Final Days spring from Meteion's despair-song; Hermes = Fandaniel; VENAT WILL BECOME HYDAELYN and sunder Zodiark — the deepest cosmology truth.
- GATED: Dynamis and the Endsinger's final form (Ultima Thule) — the last remaining gate.

**Phase 5 — Hydaelyn's farewell & the launch**
- IN-SCENA: return to the present; VENAT IS HYDAELYN, fully confirmed; she asks to be TESTED so she may pass on her strength.
- IN-SCENA [The Aitiascope]: the rift the ship crosses on the way toward the source of despair.
- IN-SCENA [The Mothercrystal]: HYDAELYN (Venat) — the party battles her; she entrusts her power and her hope, then fades.
- REVEAL: Hydaelyn = Venat; her farewell and final gift.

**Phase 6 — Ultima Thule & the Endsinger (the finale)**
- IN-SCENA: ULTIMA THULE, the edge of the universe strewn with THE DEAD ENDS (civilizations that surrendered to despair); DYNAMIS is revealed — a force powered by EMOTION and will, not aether: the strength of hope.
- IN-SCENA: one by one the companions FALL to open the path and are BROUGHT BACK by the party's refusal to despair (Dynamis) — Y'shtola, Thancred, Urianger, Estinien, Alphinaud, Alisaie, G'raha.
- IN-SCENA [The Dead Ends]: the passage through the graveyard of fallen civilizations.
- IN-SCENA [The Final Day]: THE ENDSINGER (Meteion's ultimate form) — the final confrontation, won by hope/Dynamis. THE CAMPAIGN'S CLIMAX.
- IN-SCENA [epilogue duel]: ZENOS returns for the promised one-on-one, taking a dragon's form — the Warrior's personal last battle that closes the saga.
- REVEAL: Dynamis / the power of hope; the Endsinger defeated; the star saved. END OF CAMPAIGN.
- GATED: nothing further — the campaign closes here (Dawntrail EXCLUDED, Ch.1 / 06 §A19).

### Lvl 20 - The Final Days (the whole EW arc)
Level CAP: all of EW is played at 20. **ZONES in order:** Old Sharlayan / Labyrinthos -> Thavnair (Radz-at-Han) -> Garlemald -> Mare Lamentorum (the Moon) -> Elpis (the past) -> Ultima Thule.

**Sub-beats, dungeons/trials in verified MSQ order:**
1. The Tower of Zot - [Thavnair/border - Magus Sisters]
2. The Tower of Babil - [Garlemald]
3. Storm's Crown - BARBARICCIA - [Telophoroi / Archfiends]
4. Vanaspati - [Thavnair, Final Days / Blasphemy]
5. The Dark Inside - ZODIARK
6. Ktisis Hyperboreia - [Elpis - the past, Venat/Hermes]
7. The Aitiascope - [toward Ultima Thule]
8. The Mothercrystal - HYDAELYN
9. The Dead Ends - [Ultima Thule]
10. The Final Day - ENDSINGER  *** FINAL CLIMAX / END OF CAMPAIGN ***

**GM NOTES:** the grand finale of the whole saga (ARR->EW). Themes: Azem's soul, the Blessing, the group's bond, the power of hope (Dynamis) and the companions' sacrifices at Ultima Thule. Maximum emotional weight; LB3 at full availability for the climax.
- `[REC]` Myths of the Realm alliance: "A Mission in Mor Dhona", Old Sharlayan.
- `[REC]` Hildibrand (EW) -> The Gilded Araya (trial), Radz-at-Han.
- *THE CAMPAIGN CLOSES ON THE ENDSINGER. No 6.x patches. Dawntrail EXCLUDED.*

### CAMPAIGN FINALE & EPILOGUE (binding — terminal beat; detail 06 §B27)
- The MSQ spine TERMINATES at the quest **Endwalker** — the TERMINAL beat.
- On its climax (The Dead Ends -> The Final Day / the Endsinger -> the Zenos duel) the LIVE marker enters **[CAMPAGNA CONCLUSA]** and stops offering 'continua' past 6.0 (patches 6.1+ OUT OF SCOPE, Ch.1 / 06 §A19); the wiki flow-driver stops here.
- The assistant then OFFERS (never forces) a closing **EPILOGO**: the canonical denouement (homecoming, the Scions' reunion, honouring the fallen, Krile joining, Meteion with the Loporrits), woven with GM-supplied original-colour re-injected per the lean save.
- Save after finale: [A] Endwalker (completata) · [C] nessuna. Closing marker: '— fine della campagna —'.

---

## Quick Gate / Unlock alignment (whole campaign)
- **Crystal Tower:** INLINE MANDATORY MSQ FLOW (no longer a side gate) - SEEDED at 2.1 'Laying the Foundation', PLAYED as a fixed ~13-beat arc after 'Build on the Stone' (CID trigger), EXIT to 2.2 'Still Waters'. Mor Dhona. Complete before HW. Lore: Allagan / Xande / Cloud of Darkness / Bahamut=Dalamud / G'raha (ShB Exarch = GATED).
- `[REC]` **The Binding Coil of Bahamut** (ARR, Mor Dhona) - optional deep-dive tied to the CT Bahamut/Dalamud lore.
- `[REC]` Hildibrand: ARR (Ul'dah) -> SB (Kugane, Kugane Ohashi) -> EW (Radz-at-Han, Gilded Araya).
- `[REC]` Primal Fear -> Odin (ARR); Relic -> Chimera/Hydra (ARR); Moggle Mog (ARR).
- `[REC]` Warring Triad (HW); Void Ark alliance (HW).
- `[REC]` Return to Ivalice alliance (SB); Four Lords (SB); Rathalos (SB).
- `[REC]` YoRHa alliance (ShB); Sorrow of Werlyt (ShB). `[OPT]` Eden (ShB).
- `[REC]` Myths of the Realm alliance (EW).
- `[OPT]` Optional dungeons per expansion: zone-themed, never on the critical path.
- `[CUT]` Minor fetch quests not tied to the current zone/MSQ.
- **EXCLUDED:** Bozja / Save the Queen; all post-Endwalker patches; Dawntrail.

*[END OF ROADMAP - ARR -> EW COMPLETE AND VERIFIED.]*

# 08.2 — ORDERED MSQ INDEX (AUTHORITATIVE DATA) — A REALM REBORN (2.0 -> 2.55)

**STATUS:** merged in v1.55 (with the 3 fixes applied). Single source = Console Games Wiki (every quest walked via its `Next`); name-scaffold cross-checked on Gamer Escape. ~330 quests in PLAY ORDER: 3 starting-city openings + base 2.0 + patches 2.1-2.55.

(convenzioni: vedi 08.0)

**FOLDED BACKFILLS (read at their noted positions):** Shadow of Darkness / The Bear and the Young'uns' Cares / Wilred Wants You (inst.3 -> belong in inst.2); The Scions of the Seventh Dawn quest + The Company You Keep (inst.5 -> belong in inst.1); Fool Me Twice (inst.7 -> belongs in inst.6).

**FIXES APPLIED IN v1.55 (all three done, not merely noted):**
1. ORDER — Garuda (Lady of the Vortex) is BEFORE Cape Westwind (Operation Archon); the roadmap L6/L7 was corrected to match (Cape Westwind moved to L7).
2. ENVOY — the three Envoy quests are canonical in inst.0 (CGW-verified givers); inst.1's duplicate sub-steps were removed.
3. PENDING — Best-laid Schemes giver filled (Ilberd, Wellwick Wood, GE-verified); the phantom 'Warrior of Light' transition removed (The Ultimate Weapon -> The Price of Principles direct, GE-verified).

---

## TRIAL PINS — HW → EW (element/theme · arena + real instant-death/hazard · boss visual · signature moves) [CGW-verified]
Read this (or, for ARR, the inline TRIAL PIN in the 08.2 index) BEFORE building any MSQ trial (06 §B10 TRIAL LORE-FIDELITY + §B20). Theme the arena, the boss's body, the move imagery and the damage types to the ELEMENT below — NEVER bleed another primal's element onto the one you are writing (the observed failure: Titan, an EARTH primal, written with magma/obsidian imagery). Longevity via phase gates + Legendary Resistance + legendary actions, offense in band (06 §B11 carve-out).

**Heavensward**
- **Vishap (The Steps of Faith):** DRAGON (fire/earth breath) — a DEFENSE / siege trial, NOT a standard single-boss: build it as a timed DEFENSE of the Steps of Faith BRIDGE at Ishgard as the Dravanian Horde advances toward the city, protecting the three wards ('Daniffen's Collar') with Temple Knights / dragoons / cannons at your side. Boss = a great horned wyrm. Hazard = ward destruction / the horde breaking through (a DPS-race stand). Moves: Flame Breath, Fireball, Seismic Shriek, Body Slam, Earth Shaker, Earthrising (Exaflares), Scorching Breath (final ward-breaker).
- **Bismarck (The Limitless Blue):** WIND / SKY ('Lord of the Mists'). Arena = a floating rock platform adrift in the Sea of Clouds (the platform has its OWN HP — a wipe if it collapses); instant-death = FALLING off the edge. Boss = a colossal pale sky-WHALE (its Chitin Carapace and Corona become targetable). Moves: Cetacean Rage (dive), Breach Blast; add / weather (thunder-rain) phases.
- **Ravana (Thok ast Thok):** the GNATH insect-primal of WAR & blades (no classical element — theme = conquest/steel). Arena = the Gnath hive-arena; its walls CRUMBLE after the ultimate, opening edges to be knocked off. Boss = a four-armed insectile warrior-god wielding curved swords, cycling offensive/defensive stances. Moves: Prelude to Slaughter / Slaughter, Chandrahas (~60% adds → Falling Laughter), Surpanakha, Rose of Hate/Conquest, Pillars of Heaven (raid-wide + knockback).
- **King Thordan (The Singularity Reactor):** HOLY / LIGHT (Archbishop Thordan VII ascended on the Eye's aether + a millennium of prayer). Arena = the Singularity Reactor, Azys Lla. Boss = a golden-armoured knight-king with a holy lance, flanked by the spectral KNIGHTS OF THE ROUND. Moves: Ascalon's Mercy / Might, Ancient Quaga, The Dragon's Eye / Gaze, Knights of the Round → Ultimate End (survive it by managing the knights first).
- **Nidhogg (The Final Steps of Faith):** the great WYRM, DRAGON-FURY / FIRE (furious red flames). Arena = the Steps of Faith bridge; lethal succession of AoE zones (positioning-crucial). Boss = an immense one-eyed dragon of black scale and red fury (a humanoid form in a mid phase, back to the fire-dragon at the climax). Moves: Akh Morn, Deafening Bellow, Hot Wings / Hot Tail (safe zones along his body), Geirskogul (line); a P2 add DPS check.

**Stormblood**
- **Susano (The Pool of Tribute):** STORM / LIGHTNING kami (Far-Eastern 'great kami'). Arena = the Blessed Treasury on the Isle of Zekki; hazard = Dark Clouds casting line-AoE Paralysis. Boss = a giant blue-skinned storm-god wielding the vast blade Ame-no-Murakumo. Phase = Ame-no-Murakumo (interrupt or wipe; a tank holds the pinning crystal). Moves: Assail (tank buster), Rasen Kaikyo, Yata No Kagami (knockback), Stormsplitter, Ama-no-iwato.
- **Lakshmi (Emanation):** the ANANTA primal, theme = illusion / desire / blissful oblivion. Arena = Emanation, Gyr Abania; instant-death = FALLING off the platform edges. Boss = a serene multi-armed azure goddess enthroned on a lotus. Gimmick = the VRIL shield (grab one to survive her devastating hits). Moves: Target Left / Right (blue pools / cross), stack markers; opens with the Dreaming Kshatriya adds to drop her barrier.
- **Shinryu (The Royal Menagerie):** an ALL-ELEMENT DRAGON of pure violence (fused with Zenos; a Corrupted-Aether bar cycles water/wind/fire/lightning/earth/ice — the six primals' ults). Arena = large platforms over the void in three stages (falling off = instantly fatal; P3 breakable outer grid). Boss = a colossal white-and-blue serpentine dragon with vast wings. Moves: the absorbed ults (Tidal Wave, Aerial Blast, Hellfire, Judgment Bolt, Earthen Fury, Diamond Dust), Akh Morn, Tail Slam, Burning Chains; an Active Time Maneuver between phases.
- **Tsukuyomi (Castrum Fluminis):** DARK / LUNAR divinity of night and the moon. Arena = a platform that SPLITS into sections (Selenomancy); hazard = section debuff stacks → Doom (swap sections to reset). Boss = an elegant lunar goddess (Yotsuyu's form) in dark-and-silver robes. Moves: Torment Unto Death (tank buster), Zashiki-Asobi (fan explosions), Nightfall, Lunacy (stack), Dark / Bright Blade (arena cleave); a P2 Suffering gauge.

**Shadowbringers**
- **Titania (The Dancing Plague):** the fallen FAERIE KING — FAE / nature, a Lightwarden. Arena = Il Mheg; P2 carpets the arena in GRASS (Midsummer Night's Dream). Boss = a small, uncanny fae king in a white dress, shell crown, stone sceptre, crystal shoes. Moves: the RUNE attacks (Divination cone tank buster, Water / Flame / Frost / Mist / Growth Runes), the fae adds Puck / Peaseblossom / Mustardseed, 'Being Mortal'.
- **Innocence (The Crown of the Immaculate):** LIGHT / holy judgement, a Lightwarden — fought within a GIANT TALOS born of the realm's collective hope. Boss = a radiant winged golden youth-god wielding a great sword. Moves: Righteous Bolt (tank buster), Winged / Rightful Reprobation (embedded swords → line AoEs), Flaming Sword (keep the Immaculate Authority meter below 100).
- **Hades (The Dying Gasp):** DARKNESS / ancient creation-magic (Emet-Selch). Arena = a circular platform over the drowned ruins of AMAUROT in the Tempest; the outer railing is destroyed mid-fight → fall to your doom. Boss = a robed ancient in black-and-gold Ascian garb who TRANSFORMS into a monstrous dark titan rooted to the north. Moves: Kokytos (all HP to 1), Bad Faith, Dark Eruption, Shadowspread, Broken Faith, Echoes of the Lost, Captivity.
- **Elidibus (The Seat of Sacrifice):** LIGHT — the WARRIOR OF LIGHT incarnate ('mankind's first hero'). Arena = the Seat of Sacrifice; hazard = Sword of Light cutting a lethal triangle into the floor. Boss = a red-and-white armoured knight wielding a blade of light he imbues with elements. Moves: Coruscant Saber (ring vs centre by the ring-cue), Terror Unleashed (party to 1 HP), Absolute Fire III / Blizzard III, Summon Wyrm; an ATM intermission.

**Endwalker**
- **Zodiark (The Dark Inside):** the GOD OF DARKNESS, a primordial deity awoken prematurely. Arena = a single-sided platform — players can FALL OFF the open edge. Boss = a colossal eldritch dark deity. Moves: Kokytos (all HP to 1), Exoterikos (beams → triangle/square AoEs), Styx (stack), Paradeigma (summons behemoths / snakes), Astral Flow (platform rotation), Astral Eclipse (meteor pattern).
- **Hydaelyn (The Mothercrystal):** the GODDESS OF LIGHT, the Will of the star — a test of worth. Arena = a radiant crystalline platform whose OUTER EDGE instantly kills on touch. Boss = a luminous crystalline goddess who cycles weapon forms (Dancer chakrams / White Mage staff / Paladin sword-and-shield). Moves: Hero's Radiance (raid-wide), Mousa's Scorn (tank buster), Parhelion (chakram lines); a crystal phase where the Conviction bar must not reach 100.
- **The Endsinger (The Final Day):** DESPAIR / oblivion incarnate (cosmic nihilism, Meteion's gathered despair). Arena = a fragment at the EDGE OF THE UNIVERSE — knockbacks (Galaxias) can hurl you off. Boss = an otherworldly winged harbinger, a purple-glowing maw and eyes. Moves: Elegeia (raid-wide + orbs), Galaxias (knockback meteor), Elenchos (lines), Death's Embrace (cones), Ultimate Fate (needs LB3); Kakodaimon adds + a Despair gauge; P2 'Prayers of Hope' damage race.
- **Zenos (solo duel, after the Endsinger):** NOT a primal/trial — a one-on-one SWORDSMAN DUEL vs Zenos viator Galvus (build as a single elite humanoid duelist, not a mechanics-trial). Arena = the barren field at world's end.

## 08.OST — TEMI DUTY (consolidato; uso: vedi 08.0)
#### GENERIC ARR DUNGEON BATTLE THEMES (binding)
dungeon battle = The Promise of Plunder (early dungeons: Sastasha / Tam-Tara / Copperbell / Toto-Rak) or A Fell Air Falleth (later dungeons) · mid-boss = A Fine Death · final boss = Nemesis — unless a boss-specific theme is noted below.
- Sastasha — (ambient) From the Depths · (battle) The Promise of Plunder · (mid-boss) A Fine Death · (final) Nemesis
- The Tam-Tara Deepcroft — (ambient) Slumber Disturbed · (battle) The Promise of Plunder · (mid-boss) A Fine Death · (final) Nemesis
- Copperbell Mines — (ambient) Below · (battle) The Promise of Plunder · (mid-boss) A Fine Death · (final) Nemesis
- The Thousand Maws of Toto-Rak — (ambient) A Thousand Screams · (battle) The Promise of Plunder · (mid-boss) A Fine Death · (final) Nemesis
- Haukke Manor — (ambient) The Maiden's Lament · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis
- Brayflox's Longstop — (ambient) Lipflaps on Longstops · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis
- The Stone Vigil — (ambient) Cold Salvation · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis
- Snowcloak — (ambient) The Warrens · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis · EXCEPTIONS: (mid-boss) Persistence · (final) Pennons Aloft
- Castrum Meridianum — (ambient) The Emperor's Wont · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis · EXCEPTION: (final, Livia) Steel Reason
- The Praetorium — (ambient) Penitus · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis · EXCEPTIONS: (Nero) Steel Reason · (Gaius, final) Bite of the Black Wolf
- The Keeper of the Lake — (ambient) Silver Tears · (battle) A Fell Air Falleth · (mid-boss) A Fine Death · (final) Nemesis · EXCEPTION: (Midgardsormr, final) Primogenitor
- The Bowl of Embers (IFRIT) — Primal Judgment (CGW-listed; the iconic Ifrit track is often 'Fallen Angel')
- The Navel (TITAN) — Weight of a Whisper -> Weight of His Will -> Weight of the World -> Heartless -> Under the Weight
- The Howling Eye (GARUDA) — Fallen Angel
- The Whorleater (LEVIATHAN) — Wreck to the Seaman -> Through the Maelstrom
- The Striking Tree (RAMUH) — Thunder Rolls
- The Akh Afah Amphitheatre (SHIVA) — Footsteps in the Snow -> Oblivion
- The Porta Decumana (ULTIMA WEAPON) — The Maker's Ruin -> Ultima
- Cape Westwind (RHITAHTYN) — Steel Reason (imperial battle theme; solo instance)
CRYSTAL TOWER (gate):
- Labyrinth of the Ancients — (ambient) Hubris · (battle) Ever Upwards · (final, Phlegethon) Tumbling Down
- Syrcus Tower — (ambient) Out of the Labyrinth · (battle) Shattered · (final, Xande) Tumbling Down
- The World of Darkness — (ambient) Blind to the Dark · (battle) Hamartomania · (Cloud of Darkness, final) The Reach of Darkness
#### GENERIC HW DUNGEON BATTLE THEMES (binding)
mid-boss & final-boss fights = Ominous Prognisticks (unless a boss-specific theme is noted); HW open-world/zone battle = Melt.
- The Dusk Vigil — (ambient) Descent · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- Sohm Al — (ambient) Slumber Eternal · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- The Aery — (ambient) Roar of the Wyrm · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- The Vault — (ambient) Hallowed Halls · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- The Great Gubal Library — (ambient) Ink Long Dry · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- The Antitower — (ambient) Upon the Rocks · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- The Aetherochemical Research Facility — (ambient) Imagination · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- Sohr Khai — (ambient) Apologies · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- Xelphatol — (ambient) Grounded · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- Baelsar's Wall — (ambient) Another Brick · (mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks
- Thok ast Thok (RAVANA) — Unbending Steel
- The Limitless Blue (BISMARCK) — Limitless Blue (fase 1) · Woe That Is Madness? (fase 2)
- The Singularity Reactor (KING THORDAN) — Heroes
- The Final Steps of Faith (NIDHOGG) — Freefall · Revenge of the Horde
---
#### GENERIC SB DUNGEON BATTLE THEMES (binding)
dungeon battle/mid-boss = To the Fore · dungeon final boss = Triumph (pattern confirmed by the Bardam’s Mettle row below); SB open-world/zone battle = Looping in the Deepest Fringes.
- The Sirensong Sea — Dawnbound · EXCEPTIONS: (mid-boss) Persistence · (final) Triumph (CGW-verified)
- Castrum Abania — (ambient) Alienus · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- Ala Mhigo — (ambient) Liberty or Death · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- The Drowned City of Skalla — (ambient) Far From Home · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- The Burn — (ambient) Down Where Daemons Dwell · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- Hells' Lid — (ambient) Answer on High · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- Bardam's Mettle — (ambient) Most Unworthy · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- Doma Castle — (ambient) Gates of the Moon · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- The Ghimlyt Dark — (ambient) A Pall Most Murderous · (battle) To the Fore · (mid-boss) To the Fore · (final) Triumph
- The Pool of Tribute (SUSANO) — Revelation
- Emanation (LAKSHMI) — Beauty's Wicked Wiles
- The Royal Menagerie (SHINRYU) — The Worm's Tail
- Castrum Fluminis (TSUKUYOMI) — Wayward Daughter
---
#### GENERIC ShB DUNGEON BATTLE THEMES (binding)
dungeon boss fights (mid & final) = Insatiable (unless a boss-specific theme is noted); ShB open-world/zone battle = Rencounter.
- Holminster Switch — (ambient) To Fire and Sword · (mid-boss) Insatiable · (final) Insatiable
- Dohn Mheg — (ambient) Figments · (mid-boss) Insatiable · (final) Insatiable
- The Qitana Ravel — (ambient) Unwound · (mid-boss) Insatiable · (final) Insatiable
- Malikah's Well — (ambient) Deep Down · (mid-boss) Insatiable · (final) Insatiable
- Mt. Gulg — (ambient) In the Belly of the Beast · (mid-boss) Insatiable · (final) Insatiable
- Amaurot — (ambient) Mortal Instants · (mid-boss) Insatiable · (final) Insatiable
- The Dancing Plague (TITANIA) — What Angel Wakes Me
- The Crown of the Immaculate (INNOCENCE) — Insanity
- The Dying Gasp (HADES) — Invincible
- The Seat of Sacrifice (ELIDIBUS) — Echoes in the Dark · To the Edge
---
#### GENERIC EW DUNGEON BATTLE THEMES (binding)
dungeon mid-boss = In the Arms of War · dungeon final boss = Finality (consistent with the verified Ktisis Hyperboreia / The Dead Ends rows); EW open-world/zone battle = Unbowed.
- Vanaspati — (ambient) As the Sky Burns · (mid-boss) In the Arms of War · (final) Finality
- The Tower of Zot — (ambient) Tower of Zot · (mid-boss) In the Arms of War · (final) Finality
- The Tower of Babil — (ambient) Garlemald Express · (mid-boss) In the Arms of War · (final) Finality
- Ktisis Hyperboreia — (ambient) Miracle Works · (mid-boss) On Blade's Edge · (final) Finality
- The Aitiascope — (ambient) The Aetherial Sea · (mid-boss) In the Arms of War · (final) Finality
- The Dead Ends — (ambient) Of Countless Stars · (mid-boss) On Blade's Edge · (final) Finality
- The Dark Inside (ZODIARK) — Endcaller
- The Final Day (ENDSINGER) — The Final Day
- Storm's Crown (BARBARICCIA) — Battle with the Four Fiends (Buried Memory)
- The Mothercrystal (HYDAELYN) — Your Answer

## 08.OST-SCENE-ARR..EW — SCENE / MOOD OST TABLES (city / zone / cutscene) — added v3.14

**USE (binding, 06 §A23 SCENE-OST-FROM-CACHE):** for open-world ZONE music, a CITY/settlement, or a story CUTSCENE/mood moment, resolve the track from THESE tables — never guess from memory. Titles are the ENGLISH OST names (search key; 07 governs prose display only, never the query). CITY THEMES: where TWO themes exist (day / night) OUTPUT BOTH 🎵 links so the GM picks. A 'to verify' entry falls back to §A23 SEARCH-FIRST (English place/scene descriptor) — NEVER invent a title (§A23 NO COINED TITLES). KEY SCENES = the pinned emotional cutscene tracks; anchor each to the SAME manifest beat (08.1) every time (duty/boss/trial themes stay in 08.OST-ARR..EW). Sources: Fandom + Gamer Escape OST tracklists + Eorzea Songbook.

**RECURRING MOOD THEMES (binding — how FFXIV actually scores cutscenes):** most story cutscenes have NO bespoke track — the game REUSES a small set of situational MOOD themes (sad / tense / Ascian / Primal / Garlean / reflective), mixed freely across scenes, largely shared from ARR onward. A KEY SCENE below WITHOUT a bespoke composed track resolves to the FITTING MOOD theme here (or SEARCH-FIRST if unsure); the bespoke ones (Answers, Dragonsong, Revolutions, The Worm's Tail, Who Brings Shadow, Endcaller, The Final Day, Flow...) are genuine composed set-pieces and stay as-is. VERIFIED recurring set (reused across 2.0+ cutscenes; source: reused-tracks list + Eorzea Songbook):
- SAD / grief / farewell: Where the Heart Is · Tears for Mor Dhona
- ECHO / visions: The Echo
- TENSE / general threat: Unspoken
- ASCIAN (Ascian scenes): Without Shadow
- PRIMAL (primal threat): Wrath of the Eikons
- GARLEAN (the Empire): Imperial Will · Meteor
- REFLECTIVE / title / hope: Prelude - Rebirth
Later expansions REUSE these AND add their own emotional/tense themes; when the specific expansion theme is not cached, apply SEARCH-FIRST (English descriptor) — NEVER a coined title (NO COINED TITLES).

### 08.OST-SCENE-ARR
CITIES (day / night):
- Limsa Lominsa — I Am the Sea / A Sailor Never Sleeps
- Gridania — Wailers and Waterwheels / Dance of the Fireflies
- Ul'dah — A New Hope / Sultana Dreaming
ZONES:
- Black Shroud — Serenity
- Thanalan — To the Sun
- La Noscea — On Westerly Winds
- Coerthas — Fealty
- Mor Dhona — Intertwined
KEY SCENES (manifest beat -> track):
- Opening / the Echo vision (L1) — The Echo (the vision theme) · Prelude - Rebirth (title theme). BOUND TO L1 ONLY: 'The Echo' is the OPENING-VISION theme — do NOT reuse it for later Hydaelyn/crystal beats (see the next row).
- CRYSTAL OBTAINED / Hydaelyn speaks ('Hear... Feel... Think...') — any of the 6 elemental crystals, at its canonical beat (L2 Water, L4 Fire, L4 Lightning, L5 Earth, L6 Ice, L7 Wind) — Prelude - Rebirth (the title/Hydaelyn theme)
- Scion HQ scenes (Waking Sands / Rising Stones) — The Waking Sands
- Overworld boss (lead-in Ifrit / Titan / Garuda) — Torn from the Heavens
- Mor Dhona / Crystal Tower, Allagan-lore melancholy — Now I Know the Truth
- Crystal Tower (arc theme) — The Crystal Tower
- Climax L7 (Praetorium -> Ultima Weapon) — Answers
- ARR epilogue — The Seventh Sun / Dawn of a New Era
- Moenbryda's death (2.5) — Where the Heart Is (recurring grief theme)
- Bloody Banquet of Ul'dah / The Parting Glass (2.55) — Without Shadow (the Ascian scene) + Where the Heart Is (betrayal/flight, grief) [recurring themes]
- G'raha seals himself (The Light of Hope) — The Crystal Tower (arc theme) + Where the Heart Is (farewell)

### 08.OST-SCENE-HW
CITIES (day / night):
- Ishgard — Solid / Night in the Brume (lower city); upper city: Nobility Obliges / Nobility Sleeps
ZONES:
- Coerthas Western Highlands — Against the Wind / Black and White
- Dravanian Forelands — Painted Foothills / Painted Skies
- Dravanian Hinterlands — Missing Pages / The Silent Regard of Stars
- The Churning Mists — Landlords / Skylords
- The Sea of Clouds — Lost in the Clouds / Close to the Heavens
- Azys Lla — Order Yet Undeciphered
KEY SCENES:
- HW opening (FMV) — Heavensward
- Vocal theme / credits — Dragonsong
- Haurchefant's death (The Vault, L10) — Dragonsong
- Thordan's rise/fall — Heroes Never Die -> Heroes
- Estinien freed (Final Steps of Faith, 3.3) — Freefall / Revenge of the Horde
- Ysayle's death (Azys Lla, L11) — Footsteps in the Snow (Ysayle's Shiva theme, reused at Azys Lla)
- Minfilia's sacrifice (Antitower, 3.2) — Where the Heart Is (recurring sacrifice/farewell theme)
- Papalymo's death (3.5) — Scale and Steel (Shinryu summoning / sacrifice; The Far Edge of Fate)

### 08.OST-SCENE-SB
CITIES (day / night):
- Kugane — Crimson Sunrise / Crimson Sunset
- Rhalgr's Reach — Impact
ZONES:
- The Fringes — Beyond the Wall / Hope Forgotten
- The Peaks — On High / The Stone Remembers
- The Lochs — Songs of Salt and Suffering / Old Wounds
- The Ruby Sea — Liquid Flame
- Yanxia — A Father's Pride / A Mother's Pride
- The Azim Steppe — Drowning in the Horizon / He Rises Above
KEY SCENES:
- Main theme / vocal — Revolutions
- Zenos (theme) — The Measure of His Reach
- Ala Mhigo, assault / liberation (L14) — Liberty or Death
- Zenos's suicide — The Worm's Tail
- Tsukuyomi / Yotsuyu (4.3) — Nightbloom / Lunacy / Wayward Daughter
- Yda is Lyse (L13) — recurring emotional theme (Where the Heart Is; SEARCH-FIRST for a specific SB track)
- The call to the First (4.56) — the Shadowbringers motif / recurring theme (SEARCH-FIRST)

### 08.OST-SCENE-ShB
CITIES (day / night):
- The Crystarium — The Dark Which Illuminates the World / Knowledge Never Sleeps
ZONES:
- Lakeland — The Source / Unchanging, Everchanging
- Kholusia — Unmatching Pieces
- Il Mheg — Fierce and Free / The Faerie Ring
- Amh Araeng — Sands of Amber / Sands of Blood
- The Rak'tika Greatwood — Civilizations / A Hopeless Race
- The Tempest — Full Fathom Five (upper) / 'Neath Dark Waters (Amaurot)
KEY SCENES:
- Main theme / vocal — Shadowbringers / Tomorrow and Tomorrow
- Amaurot (descent) — Mortal Instants
- Hades / Emet-Selch's death (L19) — Who Brings Shadow -> Invincible
- The Exarch is G'raha (reveal, L18) — The Dark Which Illuminates the World (recurring Crystarium/Exarch theme)
- Elidibus (Seat of Sacrifice, 5.3) — To the Edge (not on the base ShB OST; SEARCH-FIRST)

### 08.OST-SCENE-EW
CITIES (day / night):
- Old Sharlayan — The Ewer Brimmeth / The Nautilus Knoweth
ZONES:
- Thavnair — Divine Words / Prayers Repeated
- Radz-at-Han (MSQ) — Twilit Terraces
- Garlemald — White Snow, Black Steel / Black Steel, Cold Embers
- Mare Lamentorum — One Small Step
- Elpis — Sky Unsundered / Stars Long Dead
- Ultima Thule — Echoes in the Distance / Close in the Distance
KEY SCENES:
- Main theme / vocal — Endwalker - Footfalls
- Venat / Elpis (instanced battle) — Flow Together
- Zodiark (The Dark Inside) — Endcaller
- Hydaelyn's farewell (Mothercrystal) — Answers + Your Answer (+ Answers Piano Version)
- Endsinger (The Final Day) — The Final Day
- Ultima Thule / the companions fall and return (Dynamis) — Close in the Distance + Dynamis + Flow

---

**Scope:** the three starting-city opening chains (levels 1-15), which run BEFORE INSTALLMENT 1. Name-scaffold from Gamer Escape (Level 1-15 page). **Endpoints CGW-VERIFIED** (each opener + each envoy). All opening quests are overworld (NO duties); the first dungeon (Sastasha) appears only after convergence, in INSTALLMENT 1.

## CONVERGENCE (CGW-VERIFIED)
- The player picks ONE starting city -> plays that city's opening chain to its ENVOY quest at L15.
- **All three envoys -> Next: `Call of the Sea`** (shared). `Call of the Sea` -> `It's Probably Pirates` (Sastasha) = start of INSTALLMENT 1.
- Envoy exclusivity: `The Lominsan Envoy` (Limsa-start only) / `The Gridanian Envoy` (Gridania-start only) / `The Ul'dahn Envoy` (Ul'dah-start only). All visit the other two cities' leaders by airship (direct city-to-city), then Bartholomew.

---
## LIMSA LOMINSA opening (Sea) — giver of #1: Ryssfloh (Yellowjacket), Limsa Lominsa
1. Coming to Limsa Lominsa   [CGW Next: 'So It Begins' — minor Limsa-opener variance vs GE's 'Close to Home (Limsa Lominsa)'; both are early openers]
2. Close to Home (Limsa Lominsa)
3. On to Summerford `[COND: relay]`
4. Dressed to Call `[COND: fetch]`
5. Lurkers in the Grotto
6. Washed Up `[COND: parallel → Double Dealing]`
7. Double Dealing
8. Loam Maintenance `[COND: fetch]`
9. Plowshares to Swords
10. Just Deserts
11. Sky-high `[COND: relay]`
12. Thanks a Million `[COND: fetch]`
13. Relighting the Torch `[COND: fetch]`
14. On to the Drydocks `[COND: fetch]`
15. Without a Doubt `[COND: relay]`
16. Righting the Shipwright `[COND: fetch]`
17. Do Angry Pirates Dream
18. Victory in Peril
19. Men of the Blue Tattoos `[COND: fetch]`
20. Feint and Strike
21. High Society `[COND: fetch]`
22. A Mizzenmast Repast
23. **The Lominsan Envoy** (giver: Merlwyb, Command Room) -> Baderon -> airship to Gridania (Serpent honor guard, Nophica's Altar) -> airship to Ul'dah (Flame honor guard) -> Bartholomew (Hustings Strip) -> **Next: Call of the Sea**

## GRIDANIA opening (Forest) — giver of #1: Bertennant, New Gridania
1. Coming to Gridania   (-> Mother Miounne, Carline Canopy; register as an adventurer) -> Next: Close to Home
2. Close to Home (Gridania)
3. To the Bannock `[COND: relay]`
4. Passing Muster `[COND: fetch]`
5. Chasing Shadows
6. Eggs over Queasy `[COND: fetch]`
7. Surveying the Damage `[COND: fetch]`
8. A Soldier's Breakfast `[COND: fetch]`
9. Spirithold Broken
10. On to Bentbranch `[COND: relay]`
11. You Shall Not Trespass `[COND: fetch]`
12. Don't Look Down `[COND: fetch]`
13. In the Grim Darkness of the Forest `[COND: relay]`
14. Threat Level Elevated `[COND: parallel → Leia's Legacy]`
15. Migrant Marauders `[COND: fetch]`
16. A Hearer Is Often Late `[COND: relay]`
17. Salvaging the Scene `[COND: fetch]`
18. Leia's Legacy
19. Dread Is in the Air `[COND: fetch]`
20. To Guard a Guardian
21. Festive Endeavors `[COND: fetch]`
22. Renewing the Covenant
23. **The Gridanian Envoy** (giver: Kan-E-Senna, the Lotus Stand) -> Miounne -> airship to Ul'dah (present missive to Zanthael, Bulwark Hall) -> airship to ... -> present missive to Bartholomew (Hustings Strip) -> **Next: Call of the Sea**

## UL'DAH opening (Desert) — giver of #1: Wymond, Ul'dah - Steps of Nald
1. Coming to Ul'dah   (-> Momodi) -> Next: Close to Home
2. Close to Home (Ul'dah)
3. We Must Rebuild `[COND: relay]`
4. Nothing to See Here `[COND: parallel → Underneath the Sultantree]`
5. Underneath the Sultantree
6. Step Nine `[COND: fetch]`
7. Prudence at This Junction `[COND: fetch]`
8. Out of House and Home `[COND: fetch]`
9. Way Down in the Hole
10. Takin' What They're Givin' `[COND: relay]`
11. Supply and Demands `[COND: fetch]`
12. Give It to Me Raw `[COND: fetch]`
13. The Perfect Swarm `[COND: fetch]`
14. Last Letter to Lost Hope `[COND: fetch]`
15. Passing the Blade `[COND: fetch]`
16. Following Footfalls `[COND: relay]`
17. Storms on the Horizon `[COND: relay]`
18. Oh Captain, My Captain
19. Secrets and Lies `[COND: fetch]`
20. Duty, Honor, Country
21. A Matter of Tradition `[COND: fetch]`
22. A Royal Reception
23. **The Ul'dahn Envoy** (giver: Raubahn, Ul'dah - Steps of Nald) -> Momodi -> airship to Gridania (Zanthael/Bulwark Hall) -> airship (Serpent honor guard, Nophica's Altar) -> **Next: Call of the Sea**

---
## HANDOFF TO INSTALLMENT 1
**Call of the Sea** (shared, post-envoy) -> **It's Probably Pirates** (Sastasha, first dungeon) -> ... = INSTALLMENT 1 (convergence L15 -> Sylph arc).

> Note: openings verified at ENDPOINTS on CGW (openers + all three envoys + convergence to Call of the Sea). The 23-step bodies are the GE-scaffold play order (overworld only, no duties). Bind to 06 §A14: for any single opening step's detail, resolve on CGW at play-time (uncertainty gate).

> **CONDENSATION COVERAGE — all three openings ARE MARKED (binding):** every quest in the three city bodies was individually resolved on ConsoleGamesWiki (steps + presence of any fight / instanced-solo duty / named story NPC) before being marked — NEVER from the title, which is the method proven unsafe. The pass corrected several titles that read like errands but are not: `Lurkers in the Grotto` (solo duty + Y'shtola's first appearance), `Chasing Shadows` (solo duty + Yda/Papalymo + a Hydaelyn vision), `Underneath the Sultantree` (solo duty vs voidsent + Thancred + Hydaelyn), `Way Down in the Hole` / `Spirithold Broken` / `Just Deserts` (each the city's masked-mage/Ascian encounter), and the three Carteneau ECHO-VISION banquets (`A Mizzenmast Repast` · `Renewing the Covenant` · `A Royal Reception`) — all PLAYED. The three chains are structurally parallel, so each city gets equivalent treatment and the campaign stays REPEATABLE whichever origin is chosen. NOTE: the wiki also shows these bodies DO contain solo duties (correcting the older "overworld only, no duties" line above) — which is exactly why the per-quest resolution was required.

[dungeons/duties] in square brackets are duties contained inside the quest that names them.

---

## ARR — INSTALLMENT 1: L15 convergence -> Ifrit -> Grand Company -> Sylph gate (VERIFIED, CGW)

### Convergence — the Envoy quest (one of three by starting city; all converge to Call of the Sea)

> The three Envoy quests (The Gridanian / Lominsan / Ul'dahn Envoy) are covered with CGW-VERIFIED givers in INSTALLMENT 0 (openings); each ends -> `Call of the Sea`. Use inst.0 as canonical; the older loosely-worded envoy sub-steps previously here are removed.

### Shared chain

**Call of the Sea** — giver: wherever your Envoy ended (Gridania-start variant: Bartholomew, Ul'dah)
- -> Baderon (The Drowning Wench, Limsa): speak twice (job offer + briefing)
- Next: It's Probably Pirates
- Note: the starting-city variants all converge on Baderon.

**It's Probably Pirates** — giver: Baderon (Limsa Lominsa Upper Decks)
- V'mellpa (ferry docks): directions to Sastasha -> Seasoned Adventurer (Hall of the Novice): group-combat training -> Yellowjacket (Sastasha entrance): briefing -> [Sastasha] -> report to Baderon (Drowning Wench)
- Next: Call of the Forest
- Roster note: the Sastasha entrance NPC is a GENERIC Yellowjacket (NOT "V'mah Tia"); V'mellpa is at the ferry docks; Commodore Reyner appears ONLY in a cutscene at the Drowning Wench and sends the player nowhere — there is NO "Coral Tower" authorization step.

**Call of the Forest** — giver: Baderon (Limsa)
- -> Miounne (The Carline Canopy, Gridania): briefing
- Next: Fire in the Gloom

**Fire in the Gloom** — giver: Mother Miounne (New Gridania)
- Miounne (briefing) -> Lewin (Bowlord): purge the Lambs of Dalamud from [Tam-Tara Deepcroft] -> Gods' Quiver Bow (Quiverman): extra info -> [Tam-Tara Deepcroft] -> report to Miounne
- Next: Call of the Desert

**Call of the Desert** — giver: Mother Miounne (New Gridania)
- -> Momodi (The Quicksand, Ul'dah)
- Next: Into a Copper Hell

**Into a Copper Hell** — giver: Momodi (Ul'dah - Steps of Nald)
- Painted Mesa (The Quicksand): info on Copperbell Mines -> Stone Torch: entrance permission -> [Copperbell Mines] (defeat the hecatoncheires) -> report to Painted Mesa -> Solo Duty (the bodyguards) -> Momodi
- Next: The Scions of the Seventh Dawn

**The Scions of the Seventh Dawn** — giver: Momodi (Ul'dah - Steps of Nald) [CGW-verified] — steps: go to the Waking Sands (Vesper Bay) -> speak with the Scion (Minfilia)
- Formal joining of the Scions / first Minfilia meeting at The Waking Sands (Vesper Bay) — AFTER the three dungeons (never before Sastasha / the Water crystal).
- Next: A Wild Rose by Any Other Name (confirmed: that quest's giver is Minfilia at the Waking Sands)

**A Wild Rose by Any Other Name** — giver: Minfilia (The Waking Sands)
- Thancred: investigate a crystal robbery + abductions (primal-related) -> Isembard (Camp Drybone, Eastern Thanalan)
- Next: Unsolved Mystery

**Unsolved Mystery** — giver: Isembard (Eastern Thanalan) `[COND: fetch]`
- retrieve ripe corpses from the eastern road -> deliver them to Isembard (Camp Drybone)
- Next: What Poor People Think

**What Poor People Think** — giver: Isembard (Eastern Thanalan) `[COND: relay]`
- Ungust (deliver Isembard's note) -> Commonfolk (0/3) -> Ungust -> report to Isembard
- Next: A Proper Burial

**A Proper Burial** — giver: Isembard (Eastern Thanalan)
- Marques (outside the Church of Saint Adama Landama) -> lay + bury the embalmed corpse -> report to Marques -> Sister Ourcen -> Isembard (Camp Drybone)
- Next: For the Children

**For the Children** — giver: Isembard (Eastern Thanalan)
- Uncombed Urchin (Golden Bazaar) -> Sister Ourcen (rescue her from undead soldiers)
- Next: Amalj'aa Wrong Places

**Amalj'aa Wrong Places** — giver: Isembard (Eastern Thanalan)
- Thancred (Amalj'aa encampment) -> show him the leaflet -> Sister Ourcen (Camp Drybone inn) -> Thancred -> warn Isembard
- Next: Dressed to Deceive

**Dressed to Deceive** — giver: Isembard (Eastern Thanalan)
- Thancred (pose as impoverished souls) -> locals at Camp Drybone (in disguise) -> Thancred (pond north of Sandgate: confront the false priest) -> report to Minfilia (Waking Sands)
- Next: Lord of the Inferno (salta 'Life, Materia and Everything', tagliata — vedi sotto)

**Life, Materia and Everything** — giver: Minfilia (The Waking Sands) `[CUT: la MATERIA non esiste in questo homebrew]`
- Mutamix Bubblypots (the Bonfire): materia-enhancement demo -> Minfilia
- TAGLIATA (binding): l'unico contenuto della quest è la demo del sistema materia, che questo homebrew non implementa (nessun altro file lo cita). MAI giocata, MAI riassunta, MAI bersaglio di 'apre': 'Dressed to Deceive' chiude direttamente su **Lord of the Inferno**. Voce conservata solo come traccia canonica.
- Next (canonico, non usato): Lord of the Inferno

**Lord of the Inferno** — giver: Minfilia (The Waking Sands)
- Flame Sergeant (Camp Drybone): briefing -> Flame Sergeant (the Invisible City) -> Solo Duty (defeat the Amalj'aa) -> Flame Sergeant (in the cave) -> [IFRIT — The Bowl of Embers, trial] -> Thancred (Camp Drybone) -> Scion (Waking Sands) -> Minfilia (final debrief)
- Next: A Hero in the Making
- Manifest tie: CRYSTAL #2 FIRE at Ifrit (08.1, L4).

**A Hero in the Making** — giver: Minfilia (The Waking Sands)
- Tataru (locations of the remembrance services) -> Kan-E-Senna (Mih Khetto's Amphitheatre, Gridania) -> Raubahn (Royal Promenade, Ul'dah) -> Merlwyb (Stateroom, Limsa) -> Minfilia (report + CHOOSE a Grand Company)
- Next: The Company You Keep (Twin Adder / Maelstrom / Immortal Flames — by the chosen GC)

**The Company You Keep** — giver: Serpent Officer (Twin Adder) / Storm Officer (Maelstrom) / Flame Officer (Immortal Flames), by chosen GC
- steps [GE-verified, Twin Adder variant; Maelstrom/Immortal Flames mirror with their own officer + home city]: speak with the personnel officer (Adders' Nest) -> SE of Nine Ivies, determine the fate of the airship + crew -> defeat the imperial soldiers -> report to the personnel officer. Giver location: The Waking Sands (the Solar).
- Next (by GC): Wood's Will Be Done (Twin Adder) / Till Sea Swallows All (Maelstrom) / For Coin and Country (Immortal Flames) — the three variants converge to Sylph-management.

**Wood's Will Be Done** (Twin Adder variant; Maelstrom = Till Sea Swallows All; Immortal Flames = For Coin and Country) — giver: Serpent Personnel Officer (New Gridania)
- swear the oath of allegiance -> Scion (Waking Sands): news of Biggs & Wedge joining the Scions
- Next: Sylph-management

**Sylph-management** — giver: Minfilia (The Waking Sands)
- Vorsaile Heuloix (the Adders' Nest): sylph-investigation briefing
- Next: We Come in Peace

**We Come in Peace** — giver: Vorsaile Heuloix (New Gridania)
- Mitainie (Westshore Pier): transport -> Amelain (the Hawthorne Hut): sylphic-culture briefing
- Next: Sylphic Studies

**Sylphic Studies** — giver: Rolfe Hawthorne (East Shroud) `[COND: parallel → First Impressions]`
- Ysabel (etiquette) -> Blaisette (nature/pranks) -> Monne (sustenance) -> report to Rolfe
- Next: First Impressions

**First Impressions** — giver: Rolfe Hawthorne (East Shroud)
- Rosa Hawthorne (preferred gift) -> Curious Tussock (Honey Yard: use amber syrup, slay the ochu) -> present the milkroot to Rolfe
- Next: First Contact

**First Contact** — giver: Rolfe Hawthorne (East Shroud)
- Rolfe (wraps the offering) -> Amelain (letter from the Elder Seedseer for Komuxio) -> Komuxio (perform the dance emote; accepts the milkroot + letter as proof of peace)
- Next: Dance Dance Diplomacy

**Dance Dance Diplomacy** — giver: Yda (Little Solace) `[COND: parallel → Presence of the Enemy]`
- dance for the sylphs of Little Solace (0/3) -> report to Yda
- Next: Forest Friend

**Forest Friend** — giver: Papalymo (East Shroud) `[COND: fetch]`
- Imedia (advice) -> slay a ziz gorlin, slay a gall gnat, obtain 3 brownie brushes -> Komuxio (Little Solace)
- Next: Presence of the Enemy

---

## ARR — INSTALLMENT 2: Sylph/Ixal diplomacy -> Toto-Rak (Frixio) -> Little Ala Mhigo (VERIFIED, CGW)

**Presence of the Enemy** — giver: Komuxio (East Shroud)
- talk to residents of Little Solace & the Hawthorne Hut (unfamiliar sightings) -> investigate signs of imperial incursion in the forest -> deliver the quartermaster's log
- Next: Brotherly Love

**Brotherly Love** — giver: Komuxio (East Shroud) `[COND: relay]`
- Claxio -> Komuxio -> find Claxio -> report to Komuxio
- Next: Spirited Away

**Spirited Away** — giver: Komuxio (East Shroud)
- Vorsaile Heuloix (Adders' Nest: request Twin Adder aid to find the missing sylph elder) -> Giah Molkoh (Bentbranch Meadows: Wood Wailers' help) -> Buscarron (Buscarron's Druthers: any news of the elder)
- Next: Druthers House Rules

**Druthers House Rules** — giver: Buscarron (South Shroud) `[COND: fetch]`
- douse the Mead-soaked Midlander with water -> report to Buscarron
- Next: Never Forget

**Never Forget** — giver: Buscarron (South Shroud) `[COND: relay]`
- Baensyng (Hawkers' Alley, Limsa) -> Kyokyoroon (give a fresh chicken egg) -> Wineburg (Lominsan ferry docks) -> Ahldfoet (Aleport) -> Teteroon (Memeroon's Trading Post, upper La Noscea: deliver the scarlet earring)
- Next: Microbrewing

**Microbrewing** — giver: Teteroon (Upper La Noscea) `[COND: fetch]`
- slay coeurl pups, collect 3 coeurl pup whiskers -> deliver to Teteroon
- Next: Like Fine Wine

**Like Fine Wine** — giver: Teteroon (Upper La Noscea) `[COND: fetch]`
- receive the Qiqirn Firewater -> deliver it to Buscarron (the Druthers)
- Next: Sylphish Concerns

**Sylphish Concerns** — giver: Buscarron (South Shroud) `[COND: parallel → Nouveau Riche]`
- investigate the areas where sylphs were sighted (0/5) -> report to Buscarron
- Next: Nouveau Riche

**Nouveau Riche** — giver: Buscarron (South Shroud)
- Laurentius (several talks) -> defeat him and his party -> report to Buscarron
- Next: Into the Beast's Maw

**Into the Beast's Maw** — giver: Buscarron (South Shroud)
- Bloisirant (permission to enter) -> [Thousand Maws of Toto-Rak] (find Frixio) -> report to Buscarron -> Dellexia
- Next: A Simple Gift
- Manifest tie: CRYSTAL #3 LIGHTNING (rescue of the sylph elder Frixio), 08.1 L4. Toto-Rak reworked gimmick = activate terminals (see ARR REVAMPED-DUTY LOCK, 08.1); roster = Coeurl O' Nine Tails (an OCHU/plant despite the name; mini-boss, x2) + Graffias (final).

**A Simple Gift** — giver: Buscarron (South Shroud) `[COND: fetch]`
- Knolexia (Little Solace: deliver the Azeyma Rose Oil)
- Next: Believe in Your Sylph

**Believe in Your Sylph** — giver: Komuxio (East Shroud)
- Frixio (discuss peace) -> Vorsaile Heuloix (deliver Frixio's missive)
- Next: Back from the Wood

**Back from the Wood** — giver: Vorsaile Heuloix (New Gridania)
- Tataru -> Minfilia (the Waking Sands)
- Next: Shadow of Darkness

**Shadow of Darkness** — giver: Minfilia (the Waking Sands)
- Swift (Hall of Flames: a sighting of the masked man in eastern Thanalan) -> Hihibaru (Highbridge)
- Next: Highbridge Times

**Highbridge Times** — giver: Hihibaru (Eastern Thanalan)
- 3 merchants at Highbridge (info on the masked man) -> Hihibaru
- Next: Ratting It Out  (CGW 'Next' field shows Where There Is Smoke; Ratting It Out is the intervening step per chain order)

**Ratting It Out** — giver: Hihibaru (Eastern Thanalan) `[COND: fetch]`
- search the Qiqirn lair SE of Highbridge -> deliver the undecipherable letter
- Next: Where There Is Smoke

**Where There Is Smoke** — giver: Hihibaru (Eastern Thanalan)
- use a smoldering coal on the ash-covered ground NE of Highbridge (arrange a rendezvous) -> defeat the summoned Bandit -> present the Ward of the Destroyer
- Next: On to Little Ala Mhigo

**On to Little Ala Mhigo** — giver: Hihibaru (Eastern Thanalan)
- Hihira (Little Ala Mhigo) -> Gundobald (leader of the refugee settlement)
- Next: Tea for Three

**Tea for Three** — giver: Gisilbehrt (Southern Thanalan) `[COND: parallel → Meeting with the Resistance]`
- deliver a cup of sweet Thanalan tea to Osric, Angry River, Yayazuku
- Next: Foot in the Door

**Foot in the Door** — giver: Gisilbehrt (Southern Thanalan) `[COND: relay]`
- Minfilia (the Waking Sands, Vesper Bay)
- Next: Meeting with the Resistance

**Meeting with the Resistance** — giver: Minfilia (the Waking Sands)
- Haribehrt (storage area: about the Ala Mhigan Resistance) -> Albreda (Quarrymill, South Shroud: mention Haribehrt -> referred to Meffrid)
- Next: Killing Him Softly

**Killing Him Softly** — giver: Meffrid (South Shroud)
- Albreda (convince the hamlet to aid the wounded man) -> Charline (the Hearer: permission) -> report to Meffrid
- Next: Helping Horn

**Helping Horn** — giver: Meffrid (South Shroud) `[COND: fetch]`
- slay antelope stags (0/4 horns) -> deliver to Meffrid -> Buscarron -> Faramund (herbal ointment)
- Next: He Ain't Heavy

**He Ain't Heavy** — giver: Meffrid (South Shroud)
- Albreda (about Gallien) -> Meffrid (instructions) -> Gallien (track him down)
- Next: Come Highly Recommended

**Come Highly Recommended** — giver: Meffrid (South Shroud) `[COND: fetch]`
- receive Meffrid's Recommendation -> Gundobald (Little Ala Mhigo: show the letter)
- Next: The Bear and the Young'uns' Cares

**The Bear and the Young'uns' Cares** — giver: Gundobald (Southern Thanalan) `[COND: parallel → Wilred Wants You]`
- speak with the 4 youths of Little Ala Mhigo (about the masked man) -> report to Gundobald
- Next: Wilred Wants You

**Wilred Wants You** — giver: Hremfing (Southern Thanalan)
- Wilred (rendezvous at the rocky area N of the settlement) -> defeat him & his cronies, question him -> report to Gundobald
- Next: Big Trouble in Little Ala Mhigo

**Big Trouble in Little Ala Mhigo** — giver: Gundobald (Southern Thanalan)
- Wilred -> Riled Youth -> Riled Lass -> collect Map of Zanr'ak + Hunting Knife (evidence) -> Gundobald -> (battle) -> Wilred -> Gundobald
- Next: Back to Square One

---

## ARR — INSTALLMENT 3: masked-man investigation -> Haukke Manor -> Company of Heroes (Titan buildup) (VERIFIED, CGW)

**Back to Square One** — giver: Gundobald (Southern Thanalan)
- Gundobald -> Minfilia (report all that transpired)
- Next: Terror at Fallgourd

**Terror at Fallgourd** — giver: Minfilia (the Waking Sands)
- Noraxia (masked-man details) -> Medrod (Fallgourd Float; soothe him to recount his experience)
- Next: Ziz Is So Ridiculous

**Ziz Is So Ridiculous** — giver: Aideen (North Shroud) `[COND: fetch]`
- slay 3 ziz -> report to Aideen
- Next: Rock of Rancor

**Rock of Rancor** — giver: Aideen (North Shroud) `[COND: fetch]`
- firesand stick on the rock SW -> gather 5 lightning-aspected crystals -> deliver to Aideen
- Next: Power of Deduction

**Seeing Eye to Winged Eye** — giver: Ivaurault (North Shroud)
- investigate the rocky area W (the winged eyeball) -> report
- Next: Power of Deduction   [parallel side-thread; converges with Rock of Rancor at Power of Deduction]

**Power of Deduction** — giver: Medrod (North Shroud)
- Ivaurault (info) -> search for a maiden's corpse W of Fallgourd -> present the ravaged corpse to Aethelmaer
- Next: Secret of the White Lily

**Secret of the White Lily** — giver: Aethelmaer (North Shroud) `[COND: parallel → Skeletons in Her Closet]`
- show the lily button to: Miounne -> Bernadette -> Ceinguled -> Ursandel
- Next: Skeletons in Her Closet

**Skeletons in Her Closet** — giver: Ursandel (Old Gridania)
- [Haukke Manor] (stop Lady Amandine) -> Minfilia
- Next: Wrath of the Titan

**Wrath of the Titan** — giver: Minfilia (the Waking Sands)
- R'ashaht Rhiki (Maelstrom Command: the kobolds summoning Titan) -> Trachtoum (Grey Fleet mills, lower La Noscea: a former Company of Heroes member)
- Next: Tales from the Tidus Slayer
- Manifest tie: this opens the COMPANY OF HEROES / TITAN buildup (08.1 L5); Titan trial (The Navel) = CRYSTAL #4 EARTH, later in this cluster.

**Tales from the Tidus Slayer** — giver: Trachtoum (Lower La Noscea) `[COND: fetch]`
- destroy the rats' nest by the windmill -> report to Trachtoum
- Next: Hungry Hungry Goobbues

**Hungry Hungry Goobbues** — giver: Trachtoum (Lower La Noscea) `[COND: fetch]`
- slay goobbues W of the Grey Fleet -> report to Trachtoum
- Next: The Lominsan Way

**The Lominsan Way** — giver: Trachtoum (Lower La Noscea)
- The Miller (boulder-breaking contest) -> Wheiskaet (Costa del Sol: prove your worth before learning to defeat Titan)
- Next: Nix That

**Nix That** — giver: Wheiskaet (Eastern La Noscea) `[COND: fetch]`
- fattened herring to lure the nix -> lie in wait -> deliver the nix leg to Wheiskaet
- Next: A Modest Proposal

**A Modest Proposal** — giver: Wheiskaet (Eastern La Noscea)
- Landenel (Camp Tranquil, South Shroud: how to obtain a giant adamantoise egg)
- Next: Trial by Turtle

**The Penitent Man** — giver: Landenel (South Shroud) `[COND: fetch]`
- stingbrew -> slay agaric flies + collect a brownie brush -> present to Landenel
- Next: Changing of the Guard

**Changing of the Guard** — giver: Landenel (South Shroud) `[COND: parallel → Trial by Turtle]`
- inform Kikokutaia / Kikokutaib / Kikokutaic (proceed to the Lower Paths, agaric fly swarms)
- Next: Trial by Turtle

**Trial by Turtle** — giver: Landenel (South Shroud)
- obtain a Giant Adamantoise Egg from the nest -> U'odh Nunh (Forgotten Springs: convince him to aid)
- Next: The Perfect Prey

**The Drake Exception** — giver: U'odh Nunh (Southern Thanalan) `[COND: fetch]`
- slay sundrakes, collect blood (0/7) -> deliver to U'odh Nunh
- Next: The Perfect Prey   [U'odh Nunh sub-thread; converges at The Perfect Prey]

**The Perfect Prey** — giver: U'odh Nunh (Southern Thanalan)
- spear as bait -> lure & defeat the Amalj'aa veteran -> present the necklace to U'odh Nunh
- Next: When the Worm Turns

**When the Worm Turns** — giver: U'odh Nunh (Southern Thanalan)
- slay an angler & take its carcass -> place it in Wellwick worm territory -> slay the Wellwick worm -> return the meat + deliver an item to Wheiskaet
- Next: There and Back Again

**There and Back Again** — giver: U'odh Nunh (Southern Thanalan) `[COND: fetch]`
- deliver the onyx brandewine to Wheiskaet
- Next: The Things We Do for Cheese

**The Things We Do for Cheese** — giver: Wheiskaet (Costa del Sol, Eastern La Noscea)
- Ozun Nazun (directions to Raincatcher Gully) -> Brayflox Alltalks (clear [Brayflox's Longstop] of the flying beast) -> deliver the goblin cheese to Wheiskaet
- Next: What Do You Mean You Forgot the Wine?

---
> NOTE (Company of Heroes cluster): the Wheiskaet / Landenel / U'odh Nunh member-trials run as several short converging sub-threads (the recruitment of the veterans who once felled Titan); listed here in the wiki's sequence.
> Carryover backfills: The Scions of the Seventh Dawn (quest-page); The Company You Keep (steps).

## ARR — INSTALLMENT 4: Company-of-Heroes finish -> TITAN -> Waking Sands attacked -> Coerthas (VERIFIED, CGW)

**What Do You Mean You Forgot the Wine?** — giver: Wheiskaet (Eastern La Noscea) `[COND: fetch]`
- Shamani Lohmani (Wineport: hand over the Aperitif Order Slip)
- Next: An Offer You Can Refuse

**An Offer You Can Refuse** — giver: Shamani Lohmani (Eastern La Noscea) `[COND: relay]`
- Byrglaent (request wine for the banquet) -> Shamani Lohmani (deliver the refusal)
- Next: It Won't Work

**It Won't Work** — giver: Shamani Lohmani (Eastern La Noscea) `[COND: fetch]`
- 2 Vignerons (search for a bottle of Bacchus wine) -> Shamani Lohmani
- Next: Give a Man a Drink

**Give a Man a Drink** — giver: Shamani Lohmani (Eastern La Noscea) `[COND: relay]`
- Rhitskylt (where to find Drest) -> Drest (deliver Lohmani Rosso at the Severed String)
- Next: That Weight

**That Weight** — giver: Drest (Eastern La Noscea) `[COND: fetch]`
- slay dung midge swarms -> report to Drest
- Next: Battle Scars

**Not My War** — giver: Drest (Eastern La Noscea) `[COND: fetch]`
- defeat jungle coeurls, collect 4 skins -> Drest   [parallel Drest sub-thread; converges at Battle Scars]
- Next: Battle Scars

**Battle Scars** — giver: Drest (Eastern La Noscea) `[COND: fetch]`
- collect 3 coconuts of palm wine (Red Mantis Falls) -> Shamani Lohmani (Wineport)
- Next: It Was a Very Good Year

**It Was a Very Good Year** — giver: Shamani Lohmani (Eastern La Noscea)
- Drest (show the Bacchus leaf) -> defeat the Goobbue near the juggernaut -> Shamani Lohmani (Bacchus cutting) -> Wheiskaet (Bacchus wine)
- Next: In the Company of Heroes

**A Final Ignominy** — giver: Wheiskaet (Eastern La Noscea) `[COND: parallel → In the Company of Heroes]`
- Dyrstweitz (offer assistance) -> arrange the flowers -> arrange the wine bottles -> portion the feast (0/3) -> Wheiskaet   [parallel banquet-prep sub-thread; converges]
- Next: In the Company of Heroes

**In the Company of Heroes** — giver: Y'shtola (Eastern La Noscea)
- final tests by the veterans: Landenel (bravery) -> U'odh Nunh (skill) -> Shamani Lohmani (character) -> Brayflox Alltalks (planning) -> Wheiskaet (fortitude)
- Next: As You Wish

**As You Wish** — giver: Wheiskaet (Eastern La Noscea)
- Bronze Lake (whistle at 3 marked spots) -> Riol (how to face Titan)
- Next: Lord of Crags

**Lord of Crags** — giver: Riol (Upper La Noscea)
- Riol (the beastman aetheryte used by the Company of Heroes) -> Y'shtola (Zelma's Run: amplify the aetheryte) -> [The Navel — TITAN trial] -> Y'shtola (rendezvous at Camp Bronze Lake)
- Next: All Good Things
- Manifest tie: CRYSTAL #4 EARTH (Titan / The Navel), 08.1 L5.

**All Good Things** — giver: Y'shtola (Upper La Noscea)
- R'ashaht Rhiki (report Titan's defeat, Maelstrom Command) -> Noraxia (search for survivors at the Waking Sands) -> Father Iliud (shelter at the Church of Saint Adama Landama, eastern Thanalan)
- Next: You Can't Take It with You
- STORY: this is the aftermath of the GARLEAN RAID ON THE WAKING SANDS (the Scions' HQ attacked). Handle per the ARR manifest.

**You Can't Take It with You** — giver: Marques (Eastern Thanalan) `[COND: relay]`
- Traveling Goldsmith (buy tools) -> Marques (repair the horologe) -> Sister Eluned (give her the repaired horologe)
- Next: Bringing out the Dead

**With a Little Elbow Grease** — giver: Eaduuard (Eastern Thanalan) `[COND: relay]`
- Marques (show the broken alembic/oven) -> Marques (deliver a bronze ornamental hammer)   [Marques alchemy sub-thread]
- Next: A Tall Drink of Aqua del Sol

**A Tall Drink of Aqua del Sol** — giver: Ilcum (Eastern Thanalan) `[COND: fetch]`
- slay a sabotender del sol (brazo del sol) -> deliver the Aqua del Sol to Marques -> Marques   [converges at Bringing out the Dead]
- Next: Bringing out the Dead

**Bringing out the Dead** — giver: Sister Eluned (Eastern Thanalan)
- Merchant (outside the Waking Sands: bodies to transport) -> gather 8 corpses (4+4) to the chocobo carriage at the east gate -> Sister Eluned
- Next: Bury Me Not on the Lone Prairie

**The Warden Works in Mysterious Ways** — giver: Eluned (Eastern Thanalan) `[COND: fetch]`
- pilgrimage (Mark of the Warden: offer a prayer) -> Eluned   [parallel; converges]
- Next: Bury Me Not on the Lone Prairie

**Bury Me Not on the Lone Prairie** — giver: Eluned (Eastern Thanalan)
- return Noraxia's corpse to Little Solace -> the sylphs receive her remains -> Eluned
- Next: Eyes on Me

**Eyes on Me** — giver: Marques (Eastern Thanalan)
- search the lichyard (unseen observers) -> Marques (after being attacked) -> Father Iliud (show the sword)
- Next: He Who Waited Behind

**He Who Waited Behind** — giver: Father Iliud (Eastern Thanalan)
- Aethelmaer (Fallgourd Float: the Enterprise airship) -> Vortefaurt (Florentel's Spire: witnessed the Enterprise's final flight)
- Next: Cold Reception

**Cold Reception** — giver: Vortefaurt (North Shroud)
- Ludovoix (the Observatorium: information about the Enterprise)
- Next: The Unending War

**The Unending War** — giver: Ser Ludovoix (Coerthas Central Highlands) `[COND: relay]`
- search for the missing knight W of the Observatorium -> Ludovoix -> Edmelle -> Chief Astrologian Forlemort
- Next: Men of Honor

**Men of Honor** — giver: Jocea (Coerthas Central Highlands)
- search for the missing Astrologian (cliffs E of the Observatorium) -> Jocea -> Portelaine (formal introductions to the High Houses)
- Next: Three for Three

**Three for Three** — giver: Portelaine (Coerthas Central Highlands) `[COND: fetch]`
- recover 3 Stolen Wares (W of the Observatorium) -> Portelaine
- Next: The Rose and the Unicorn

**The Rose and the Unicorn** — giver: Ser Carrilaut (Coerthas Central Highlands)
- Francel (warn about the inquisitors; mention an edelweiss so he trusts you) -> Haurchefant (deliver Francel's letter of introduction)
- Next: The Talk of Coerthas
- STORY: HAURCHEFANT is introduced here (Coerthas), buildup toward the Stone Vigil.

---
> Carryover backfills: The Scions of the Seventh Dawn (quest-page); The Company You Keep (steps).

## BACKFILLS resolved (EXTRA — belong to INSTALLMENT 1 positions)

**The Scions of the Seventh Dawn** (the quest; page = ...(Quest)) — giver: Momodi (Ul'dah - Steps of Nald)
- Momodi (tells of the Scions -> directs you to the Waking Sands, Vesper Bay) -> Tataru (announces you to Minfilia) -> Scion guard (escort) -> Minfilia (explains the Scions' mission + the Echo, asks you to join, entrusts the password "wild rose")
- Next: A Wild Rose by Any Other Name
- Placement: this is the FORMAL Scions joining, AFTER Into a Copper Hell (the three dungeons), BEFORE A Wild Rose by Any Other Name. Manifest L2.

**The Company You Keep (Twin Adder)** (Maelstrom / Immortal Flames = mirror variants) — giver: Serpent Officer (the Waking Sands)
- Personnel Officer (Adders' Nest: formal induction) -> (airship mission) -> report -> Biggs & Wedge encountered; defeat the imperial soldiers
- Next: Wood's Will Be Done (Twin Adder) [Maelstrom -> Till Sea Swallows All; Immortal Flames -> For Coin and Country]

## ARR — INSTALLMENT 5: Coerthas (Haurchefant/Whitebrim) -> STONE VIGIL -> corrupted-crystal arc (VERIFIED, CGW)

**Feats of Strength** — giver: Haurchefant (Coerthas Central Highlands)
- Storied Knight/Veteran (train by fighting three young knights) -> Haurchefant
- Next: The Talk of Coerthas

**The Talk of Coerthas** — giver: Haurchefant (Coerthas Central Highlands) `[COND: parallel → Road to Redemption]`
- Ninne -> Cravellin -> Forlemort -> Haurchefant (report)
- Next: Road to Redemption

**Road to Redemption** — giver: Haurchefant (Coerthas Central Highlands)
- find Lord Francel -> aid Francel's three knights (0/3) -> aid Lord Francel -> Haurchefant (report)
- Next: Following the Evidence

**Following the Evidence** — giver: Haurchefant (Coerthas Central Highlands)
- Rickeman (how shipments are tampered) -> Porter (search shipments for evidence) -> show the draconian rosaries to the Porter -> Haurchefant
- Next: In the Eyes of Gods and Men

**In the Eyes of Gods and Men** — giver: Haurchefant (Coerthas Central Highlands)
- Brigie (relay request to postpone Francel's trial) -> Haurchefant (trial can't be stopped; new orders) -> Hourlinet (protect Francel at Witchdrop) -> Haurchefant (Camp Dragonhead, Francel's name cleared)
- Next: The Final Flight of the Enterprise

**The Final Flight of the Enterprise** — giver: Haurchefant (Coerthas Central Highlands) `[COND: relay]`
- Witness (about the Enterprise) -> Haurchefant (letter of introduction) -> Francel (request a letter) -> Brunadier (deliver both letters)
- Next: Ye of Little Faith

**Ye of Little Faith** — giver: Ser Brunadier (Coerthas Central Highlands) `[COND: relay]`
- Ser Alboise -> Head Chirurgeon Astidien -> Ser Goudernoux -> Lord Drillemont (present the letters)
- Next: Factual Folklore

**Opportunity Knocks** — giver: Ser Benedict (Coerthas Central Highlands) `[COND: fetch]`
- slay feral crocs (0/5) -> Ser Clotairion   [parallel Whitebrim side-thread; converges at The Best Inventions]
- Next: The Best Inventions

**Factual Folklore** — giver: Haustefort (Coerthas Central Highlands) `[COND: fetch]`
- slay a spotted mudpuppy (tail meat) -> offer mudpuppy steaks to 3 Hungry Soldiers -> Haustefort -> Cenota (steak to the chirurgeon)
- Next: The Best Inventions

**The Best Inventions** — giver: Cid (Coerthas Central Highlands) `[COND: fetch]`
- obtain 3 Ice Sprite Cores (slay ice sprites) -> deliver to Cid
- Next: Influencing Inquisitors

> [REMOVED in patch 5.3, excluded from current flow: **All by Ourselves** (Nivie / Drillemont letter).]

**Influencing Inquisitors** — giver: Cid (Coerthas Central Highlands)
- question 4 residents of Whitebrim Front (testimonials about Inquisitor Guillaime) -> Alphinaud (review findings)
- Next: By the Lights of Ishgard

**By the Lights of Ishgard** — giver: Alphinaud (Coerthas Central Highlands)
- Ser Joellaut (account of the night Guillaime arrived) -> Alphinaud (retrace the inquisitor's path) -> search outside Whitebrim Front -> inspect the corpse -> show the bloody encyclical to Alphinaud
- Next: Blood for Blood

**Blood for Blood** — giver: Alphinaud (Coerthas Central Highlands)
- Joellaut (show encyclical) -> Prunilla (show encyclical) -> confront Prunilla (/doubt) -> search SE of Whitebrim Front, open the suspicious box -> Drillemont (present findings)
- Next: The Heretic among Us

**The Heretic among Us** — giver: Drillemont (Coerthas Central Highlands) `[COND: relay]`
- Knight of House Durendaire (at Snowcloak) -> Alphinaud (Whitebrim Front)
- Next: In Pursuit of the Past

**In Pursuit of the Past** — giver: Alphinaud (Coerthas Central Highlands)
- Drillemont (permission to enter the Stone Vigil) -> Nathelain (confirm entry) -> [THE STONE VIGIL dungeon] -> Alphinaud (next steps)
- Next: Into the Eye of the Storm
- Manifest tie: CRYSTAL #5 ICE (Isgebind at the Stone Vigil), 08.1 L6.

**Into the Eye of the Storm** — giver: Cid (New Gridania) `[COND: relay]`
- Lamberteint (Camp Drybone: research on corrupted crystals)
- Next: Sealed with Science

**All Due Precautions** — giver: Lamberteint (Eastern Thanalan) `[COND: fetch]`
- Munificent Merchant (obtain a clay pot) -> Lamberteint (deliver the clay pot)   [parallel; converges at Sealed with Science]
- Next: Sealed with Science

**Sealed with Science** — giver: Lamberteint (Eastern Thanalan) `[COND: fetch]`
- Hahasako (deliver the warded pot at Highbridge)
- Next: With the Utmost Care

**With the Utmost Care** — giver: Hahasako (Eastern Thanalan) `[COND: fetch]`
- fracture a corrupted cluster with the quarrying maul, collect a corrupted crystal in the warded pot -> Lamberteint (examine)
- Next: A Promising Prospect

**A Promising Prospect** — giver: Lamberteint (Eastern Thanalan)
- Ceana (Aleport: the corrupted-crystals site on the Isles of Umbra)
- Next: It's Probably Not Pirates

**It's Probably Not Pirates** — giver: Ceana (Western La Noscea) `[COND: relay]`
- question the Yellowjackets of Aleport (travel restrictions to the Isles of Umbra) -> Ceana (undead infesting the Isles of Umbra)
- Next: Representing the Representative

**Representing the Representative** — giver: Ceana (Western La Noscea) `[COND: relay]`
- Skyfryn (permission to travel) -> Mimidoa (golden feather -> writ of passage; investigate undead at Pharos Sirius) -> Ceana (show the parchment)
- Next: The Reluctant Researcher

**The Reluctant Researcher** — giver: Ceana (Western La Noscea)
- Ferry Skipper (to the Isles of Umbra) -> Ceana (accompanies, then abandons you partway) -> Davyd (guard at the Pharos Sirius gates: show the warded pot, convince him)
- Next: Sweet Somethings

---
> Carryover backfills: NONE (both resolved above).

## ARR — INSTALLMENT 6: Isles of Umbra finish -> GARUDA (#6) -> Castrum Centri -> Operation Archon / Cape Westwind (VERIFIED, CGW)

**Sweet Somethings** — giver: Davyd (Western La Noscea) `[COND: relay]`
- adventurers at the eastern shore (cause of the undead influx) -> Davyd (the voice heard at the Ship Graveyard)
- Next: History Repeating

**History Repeating** — giver: Davyd (Western La Noscea)
- Mimidoa (follow to the Ship Graveyard) -> wait by the campfire -> Mimidoa (after defeating the siren's thralls) -> Davyd (siren no longer a threat) -> Ceana (show the corrupted crystal)
- Next: The Curious Case of Giggity

**The Curious Case of Giggity** — giver: Ceana (Western La Noscea)
- Hedyn (Gridania: location of the corrupted crystal + the true-heart lure) -> Giggity the Spriggan (lure & slay, take the corrupted crystal) -> Hedyn
- Next: Better Late than Never

**Of Sylphs and Spriggans** — giver: Komuxio (East Shroud)
- Komuxio (the wayward spriggan) -> Tiggy (save him from a tempered sylph) -> Komuxio -> Maerwynn (Sanctum of the Twelve: luring Giggity with rare ore)   [parallel Giggity sub-thread]
- Next: Crazy Enough to Work

**Crazy Enough to Work** — giver: Maerwynn (East Shroud) `[COND: relay]`
- Maerwynn (use a chert golem's soulstone as bait) -> Tiggy (Giggity's location, the Spriggan Dig) -> Hedyn (ice-aspected corrupted crystal)
- Next: Better Late than Never

**Better Late than Never** — giver: Hedyn (Old Gridania) `[COND: fetch]`
- Hedyn (returns the corrupted crystal) -> Cid (New Gridania airship landing: deliver the corrupted crystal)
- Next: Lady of the Vortex

**Lady of the Vortex** — giver: Cid (New Gridania)
- Alphinaud -> [The Howling Eye — GARUDA trial] -> Alphinaud
- Next: Reclamation
- Manifest tie: CRYSTAL #6 WIND -> BLESSING COMPLETE (Garuda / The Howling Eye), 08.1 L7.

**Reclamation** — giver: Alphinaud (Ul'dah - Steps of Nald)
- Alphinaud (the Waking Sands) -> Yda & Y'shtola present
- Next: Casing the Castrum

**Casing the Castrum** — giver: Y'shtola (the Waking Sands) `[COND: relay]`
- Portelaine (the Observatorium: intel on Castrum Centri, prisoners & escaped engineers)
- Next: Eyes on the Empire

**Eyes on the Empire** — giver: Portelaine (Coerthas Central Highlands) `[COND: relay]`
- Bricelt (show the letter of introduction) -> Pierremons
- Next: Footprints in the Snow

**Footprints in the Snow** — giver: Ser Pierremons (Coerthas Central Highlands)
- search for footprints of two escaped prisoners -> Wedge (found under the bridge) -> Monument Tower -> Cid arrives -> Abelie (welcomes you & Wedge)
- Next: Monumental Hopes

**Monumental Hopes** — giver: Wedge (Coerthas Central Highlands) `[COND: relay]`
- Abelie (info on Biggs) -> investigate Fury's Gaze (S of Monument Tower) -> Wedge
- Next: Notorious Biggs

**Notorious Biggs** — giver: Wedge (Coerthas Central Highlands)
- Ignace (info on Biggs) -> assist Yda & Y'shtola in rescuing Biggs from imperial troops at Daniffen Pass -> Wedge (Monument Tower)
- Next: Come-Into-My-Castrum

**Come-Into-My-Castrum** — giver: Cid (Coerthas Central Highlands) `[COND: relay]`
- Slafborn (Revenant's Toll: infiltrate Castrum Centri disguised as imperial troops) -> Glaumunt (aid & knowledge of Castrum Centri)
- Next: Getting Even with Garlemald

**Getting Even with Garlemald** — giver: Glaumunt (Mor Dhona) `[COND: relay]`
- investigate the drainage pipe at the Tangle (confirm the Scions' presence at Castrum Centri) -> Alphinaud (report) -> Cid (prepare the rescue)
- Next: Drowning Out the Voices

**Drowning Out the Voices** — giver: Cid (Mor Dhona) `[COND: fetch]`
- use the electromagnetic reader at prime spots near the corrupted crystals W of Revenant's Toll
- Next: Fool Me Twice

**Acting the Part** — giver: Glaumunt (Mor Dhona) `[COND: parallel → Fool Me Twice]`
- learn the imperial salute -> observe imperial soldiers at Castrum Centri -> Glaumunt (Revenant's Toll)   [parallel infiltration-prep; converges]
- Next: Dressed for Conquest

**Dressed for Conquest** — giver: Sark Malark (Mor Dhona) `[COND: fetch]`
- obtain 3 damaged imperial uniforms + 3 damaged helms -> Eginolf (Rowena's House of Splendors: repair) -> Sark Malark (inspection)
- Next: Fool Me Twice

**Fool Me Twice** — giver: Glaumunt (Mor Dhona) [CGW-verified; full step spine in the BACKFILL RESOLVED block below]
- Next: Every Little Thing She Does Is Magitek

**Every Little Thing She Does Is Magitek** — giver: Cid (Mor Dhona)
- Wedge (replace the magitek core with a mammet heart) -> Serendipity (mammet heart from the Goldsmiths' Guild) -> Wedge (pilot the magitek armor, test runs) -> Biggs (servomechanism; defend the armor) -> Cid
- Next: Escape from Castrum Centri

**Escape from Castrum Centri** — giver: Cid (Mor Dhona)
- /imperialsalute to 3 Imperial Soldiers (find where comrades are held) -> Imperial Centurion (obtain the imperial identification key) -> Biggs (give the key) -> Steel Door (enter the storage tower) -> Minfilia (after the rescue)
- Next: The Black Wolf's Ultimatum

**The Black Wolf's Ultimatum** — giver: Minfilia (Ul'dah - Steps of Nald)
- Bartholomew (Royal Promenade: admit you to the Fragrant Chamber to plead the Scions' case to the Alliance leaders) -> Minfilia (Waking Sands, after the leaders resolve to fight)
- Next: Operation Archon

**Operation Archon** — giver: Minfilia (the Waking Sands)
- Allied Communications Officer (orders for the first mission) -> Lieutenant Adalbert (staging point before the imperial outpost) -> [Cape Westwind: RHITAHTYN sas Arvina, solo duty]
- Next: A Hero in Need
- Manifest tie: Cape Westwind (Rhitahtyn) = now a SOLO instance (05 REVAMPED-DUTY LOCK); Cid & the Enterprise established; 08.1 L7 (AFTER Garuda).

**A Hero in Need** — giver: Allied Communications Officer (Western Thanalan) `[COND: relay]`
- Cracked Fist (Camp Bluefog: raise the garrison's morale)   [Camp Bluefog morale cluster -> converges at Hearts on Fire]
- Next: Hearts on Fire

**The Ladle in the Darkness** — giver: Sergeant Cracked Fist (Northern Thanalan) `[COND: parallel → Hearts on Fire]`
- basilisk stew to Zezeragi -> Adelena -> Betyn (morale boosted)   [parallel morale sub-thread]
- Next: All upon the Watchtowers

**All upon the Watchtowers** — giver: Sergeant Cracked Fist (Northern Thanalan) `[COND: relay]`
- Wymund (west watchtower) -> Hopeful Dawn (east watchtower) -> Edelstein (Ceruleum Processing Plant: report)
- Next: Hearts on Fire

---
> Fool Me Twice: RESOLVED — full step spine in the BACKFILL RESOLVED block below.

## ARR — INSTALLMENT 7: Camp Bluefog morale -> Castrum Meridianum -> The Praetorium -> The Porta Decumana / ULTIMA WEAPON (VERIFIED, CGW)

**Hearts on Fire** — giver: Cracked Fist (Northern Thanalan)
- Raubahn (rally the garrison at the Ceruleum Processing Plant, /psych up the green recruits) -> /psych up: Flame Private Third Class -> Second Class -> First Class -> Edelstein
- Next: Rock the Castrum

**Setting the Stage** — giver: Lieutenant Edelstein (Northern Thanalan)   [parallel staging quest; converges]
- defeat 3 imperial soldiers + 3 imperial vanguards at Raubahn's Push -> Raubahn (report before Castrum Meridianum)
- Next: Rock the Castrum

**Rock the Castrum** — giver: Edelstein (Northern Thanalan)
- Raubahn (briefing) -> Cid (enter Castrum Meridianum, create a diversion while he deactivates the magitek field generator) -> [Castrum Meridianum: LIVIA sas Junius] -> Raubahn
- Next: The Ultimate Weapon
- Manifest tie: Castrum Meridianum = 4-player duty (05 REVAMPED-DUTY LOCK); leads directly into the Praetorium chain.

**The Ultimate Weapon** — giver: Raubahn (accept) / first step Cid (Ceruleum Processing Plant)
- Cid (Ceruleum Processing Plant) -> [The Praetorium — dungeon duty] -> [The Porta Decumana — trial: ULTIMA WEAPON] -> GAIUS defeated during the Porta Decumana -> LAHABREA confronted & defeated on the Porta Decumana (solo duty) -> Minfilia
- Next: The Price of Principles   (= first patch-2.1 MSQ quest; GAMER-ESCAPE-VERIFIED direct link — there is NO separate 'Warrior of Light' MSQ quest between them; CGW's 'Warrior of Light' next-link resolves to the character page)
- Manifest tie: 2.0 FINALE. Praetorium + Porta Decumana = REVAMPED duties (05 LOCK). Lahabrea reveal-gate: this is the ARR unmask beat — respect 05 Ch.1 gate order. End of base A Realm Reborn.

---
## BACKFILL RESOLVED (from INSTALLMENT 6)

**Fool Me Twice** — giver: Glaumunt (Mor Dhona)   [use URL: Fool_Me_Twice_(Quest)]
- Imperial Centurion (/imperialsalute to alert them to enemy presence) -> Imperial Patrol (lure out with the imperial smoke signal) -> Cid (workshop, Revenant's Toll)
- Next: Every Little Thing She Does Is Magitek
- Placement: Castrum Centri infiltration-prep cluster (after Drowning Out the Voices / Dressed for Conquest; before Every Little Thing She Does Is Magitek). INSTALLMENT 6 pending = CLOSED.

---

## SEVENTH ASTRAL ERA — PATCH 2.1 'A REALM AWOKEN' (VERIFIED, CGW)

### Main spine
**The Price of Principles** — giver: Minfilia (the Waking Sands)
- Scions reunion round: Y'shtola -> Thancred -> Papalymo -> Yda -> Urianger -> Alphinaud
- Next: Moving On

**Moving On** — giver: Minfilia (the Waking Sands)
- Alphinaud (investigate rumors about F'lhaminn) -> Gegeruju (Costa del Sol) -> Wineport residents (info 0/2) -> Shamani Lohmani (track F'lhaminn by scent) -> F'lhaminn (Raincatcher Gully) -> Alphinaud (Wineport)
- Next: All Things in Time

**Flowers for One** — giver: Father Iliud (Eastern Thanalan)   [parallel to Moving On; same F'lhaminn hunt; converges at All Things in Time]
- Gegeruju (Costa del Sol) -> Wineport residents -> Shamani Lohmani -> The Perfumed Lady / F'lhaminn (Raincatcher Gully: defeat the goobbue, then speak) -> Alphinaud
- Next: All Things in Time

**All Things in Time** — giver: F'lhaminn (Eastern La Noscea)
- escort F'lhaminn to the Waking Sands (reunite with her daughter) -> Minfilia (witness the reunion)
- Next: Laying the Foundation

**The Resolute** — giver: Minfilia (the Waking Sands) `[COND: fetch]`   [parallel side-errand; converges at Laying the Foundation]
- F'lhaminn -> Memedesu (Goldsmiths' Guild: repair F'lhaminn's Aria) -> Odinel (Byregot's Strike: collect ores) -> Memedesu (deliver ores) -> F'lhaminn (deliver the repaired Aria) -> Minfilia
- Next: Laying the Foundation

**Laying the Foundation** — giver: Minfilia (the Waking Sands)
- Minfilia -> Slafborn (deliver the sealed documents, Revenant's Toll)
- Next: It's Possibly a Primal
- SEED: Crystal Tower ENTRY ANCHOR (see the CRYSTAL TOWER ARC block at end of Arc 1) - Slafborn / a Son of Saint Coinach notes the unearthed Tower + the NOAH expedition (Rammbroes, G'raha, Cid) at Saint Coinach's Find. INTEREST ONLY; Tower HARD-LOCKED; NO pull-forward.

### Revenant's Toll establishment cluster (Mor Dhona odd-jobs; several parallel unlocks converging at Welcome to Morbol Country, then feeding It's Possibly a Primal)
**Rock-solid Protection** — giver: Slafborn (Mor Dhona)
- Bibimu (outside the Sunken Temple of Qarn) -> [The Sunken Temple of Qarn — dungeon duty: obtain the wardstone] -> Slafborn (deliver the wardstone)
- Next: Welcome to Morbol Country

**Crate Go Kaboom** — giver: Sark Malark (Mor Dhona) `[COND: fetch]`   [parallel]
- destroy 3 Garlean crates in Castrum Centri with high-quality explosives -> Sark Malark (report)
- Next: Welcome to Morbol Country

**Better Late than Sever** — giver: Guolgeim (Mor Dhona) `[COND: fetch]`   [parallel]
- Wood Wailer (Fallgourd Float) -> Wood Wailer (supply carriage) -> rescue captured coachmen (0/2) -> recover looted supplies (0/3) -> Elezen coachman -> Guolgeim (Revenant's Toll)
- Next: Welcome to Morbol Country

**Welcome to Morbol Country** — giver: Slafborn (Mor Dhona) `[COND: fetch]`
- slay morbols in the Tangle -> Slafborn (report)
- Next: Answering the Call

**Answering the Call** — giver: Slafborn (Mor Dhona) `[COND: fetch]`
- slay hapalits in the Singing Shards -> Slafborn (report)
- Next: You're Gonna Carry That

**You're Gonna Carry That** — giver: Slafborn (Mor Dhona) `[COND: fetch]`
- Alphinaud (Waking Sands) -> gather 4 labeled packages -> Tataru (outside Waking Sands)
- Next: The Things We Do for Tea

**The Things We Do for Tea** — giver: Tataru (Western Thanalan) `[COND: fetch]`
- Medguistl (Camp Dragonhead: tea stores depleted) -> Emanuel (harvest highland tea leaves at Boulder Downs) -> harvest 4 tea leaves -> Tataru (Waking Sands)
- Next: It's Possibly a Primal

### Primal arc + close (Good King Moggle Mog XII)
**It's Possibly a Primal** — giver: Slafborn (Mor Dhona)   [convergence of the main spine + Revenant's Toll cluster]
- Tataru (Waking Sands) -> Minfilia (Waking Sands) -> Vorsaile Heuloix (Adders' Nest, Gridania)
- Next: Hail to the King, Kupo

**Hail to the King, Kupo** — giver: Vorsaile Heuloix (New Gridania)
- Kan-E-Senna (Lotus Stand: Good King Moggle Mog XII's return) -> Brother E-Sumi-Yan (how to breach the moogles' magical defenses)
- Next: You Have Selected Regicide

**You Have Selected Regicide** — giver: E-Sumi-Yan (Old Gridania)
- Kuplo Kopp (Westshore Pier) -> (Sweetbloom Pier) -> again -> escort to the warded entrance -> at the warded entrance -> attune to the Warded Entrance -> [Thornmarch (Hard): GOOD KING MOGGLE MOG XII] -> Pukni Pakk (Camp Tranquil)
- Next: On the Properties of Primals

**On the Properties of Primals** — giver: Raya-O-Senna (South Shroud)
- Kan-E-Senna (Lotus Stand: recount the victory) -> Minfilia (Waking Sands: report the Ascians' involvement)
- Next: The Gifted

**The Gifted** — giver: Minfilia (the Waking Sands)
- Urianger -> white-robed Ascian (search & follow, approach 0/4, speak) -> Minfilia
- Next: Build on the Stone

**Build on the Stone** — giver: Minfilia (the Waking Sands)
- Minfilia (give Warburton's Journal to Urianger) -> Urianger -> Tataru (Seventh Heaven, Revenant's Toll: gain entrance to the Rising Stones) -> Minfilia (in the Rising Stones)
- Next: **[CRYSTAL TOWER ARC - FIXED, MANDATORY - see the CRYSTAL TOWER ARC block at end of Arc 1; CID arrives at the Rising Stones with the crystal fangs]** -> on completion (**The Light of Hope**, Rammbroes @ Mor Dhona) -> **Still Waters** (= PATCH 2.2 opener)
- Manifest tie: Scions relocate to THE RISING STONES (Mor Dhona). End of patch 2.1.

---
> (No 'Warrior of Light' transition quest in the current chain — The Ultimate Weapon links DIRECTLY to The Price of Principles, Gamer-Escape-verified, v1.55.)

## SEVENTH ASTRAL ERA — PATCH 2.2 'THROUGH THE MAELSTROM' (Leviathan arc) (VERIFIED, CGW)

**Still Waters** — giver: Minfilia (the Rising Stones)
- Y'shtola (Horizon) -> Fufulupa (the thefts) -> Thancred (review findings)
- Next: A Final Temptation

**A Final Temptation** — giver: Thancred (Western Thanalan)
- Fufulupa (a possible Brass Blades traitor) -> Y'shtola (bait ambush, defeat the thieves) -> Y'shtola -> Fufulupa (Horizon, report)
- Next: The Mother of Exiles

**The Mother of Exiles** — giver: Thancred (Western Thanalan)
- Alphinaud (Doman visitors) -> Yugiri (Domans need asylum & provisions) -> Momodi (letters for suppliers) -> Fridurih (deliver letter) -> Katherine (deliver letter) -> Momodi -> Yugiri -> Raubahn (Royal Promenade: proceed to the audience with the sultana)
- Next: Promises to Keep

**Promises to Keep** — giver: Raubahn (Ul'dah - Steps of Thal) `[COND: relay]`
- Raubahn (Hall of Flames) -> Alphinaud
- Next: Yugiri's Game

**A Small-scale Operation** — giver: Alphinaud (Ul'dah - Steps of Nald) `[COND: fetch]`   [parallel; converges at Yugiri's Game]
- Hozan (Vesper Bay) -> retrieve a large wooden crate from the docks -> deliver -> collect 4 missing black scales -> deliver
- Next: Yugiri's Game

**Yugiri's Game** — giver: Alphinaud (Ul'dah - Steps of Nald) `[COND: parallel → Why We Adventure]`
- Hozan (Vesper Bay: rounding up children) -> Yozan -> find 3 hidden children Shiun/Koharu/Rokka (0/3) -> Hozan
- Next: Why We Adventure

**If Wishes Were Horsebirds** — giver: Hozan (Western Thanalan) `[COND: fetch]`   [parallel; converges at Why We Adventure]
- Folclind (chocobo-smell solution) -> Hyuran Coachman (perfume the chocobo) -> Hozan (give the perfumed scarf)
- Next: Why We Adventure

**Why We Adventure** — giver: Hozan (Western Thanalan)
- Hyuran coachman (begin the journey) -> survey the road to Ul'dah for beasts -> coachman (outside Horizon, road safe) -> Alphinaud (the Quicksand: safe arrival)
- Next: All Due Respect

**All Due Respect** — giver: Alphinaud (Ul'dah - Steps of Nald)
- Slafborn (Revenant's Toll: formally introduce Yugiri) -> Yugiri -> Minfilia (Rising Stones: introduce Yugiri) -> Minfilia (crystal thefts & the Leviathan threat)
- Next: The Sea Rises

**Full Belly, Happy Heart** — giver: Minfilia (the Rising Stones) `[COND: fetch]`   [parallel; feeds The Sea Rises via Writhing in the Dark]
- F'lhaminn -> Alys (Seventh Heaven: meal status) -> Adventurers' Guild Assistant (deliver meals & wine)
- Next: Writhing in the Dark

**Writhing in the Dark** — giver: Adventurers' Guild Assistant (Mor Dhona) `[COND: fetch]`
- lure & slay 6 rampant cobras with rancid eft meat -> report -> Minfilia (Rising Stones)
- Next: The Sea Rises

**The Sea Rises** — giver: Minfilia (the Rising Stones)
- Minfilia (final words) -> Admiral Merlwyb (Limsa command room: Maelstrom operation vs Leviathan & Sahagin) -> Commander Falkbryda (Camp Skull Valley: Sahagin intel)
- Next: Scouts in Distress

**Fireworks and Fish Don't Mix** — giver: Falkbryda (Western La Noscea) `[COND: fetch]`   [parallel; converges at Scouts in Distress]
- U'jughal (diversionary maneuvers) -> Maelstrom explosives: destroy Sahagin pavises at Halfstone & defeat Sahagin (0/5) -> Falkbryda (Camp Skull Valley)
- Next: Scouts in Distress

**Scouts in Distress** — giver: Falkbryda (Western La Noscea) `[COND: fetch]`
- Maelstrom restorative on the wounded Storm Private -> find the missing scouts in the Serpent's Tongue -> collect the soldiers' corpses (0/2) -> Falkbryda
- Next: The Gift of Eternity

**The Gift of Eternity** — giver: Falkbryda (Western La Noscea)
- Y'shtola (into the Sahagin lair, fight to the aetheryte) -> Thancred & Yugiri (lure Sahagin, rejoin the infiltration unit) -> Merlwyb (Sapsa Spawning Grounds, after the ritual)
- Next: Into the Heart of the Whorl

**Into the Heart of the Whorl** — giver: Merlwyb (Western La Noscea) `[COND: relay]`
- Merlwyb (Limsa command room) -> Yugiri -> Storm Private (Grey Fleet) -> Eynzahr (Moraby Drydocks: report)
- Next: Lord of the Whorl

**Lord of the Whorl** — giver: Eynzahr Slafyrsyn (Lower La Noscea, Moraby Drydocks)
- [The Whorleater (Hard): LEVIATHAN] -> Thancred & Y'shtola (3rd Levy diversion) -> Yugiri (5th Levy) -> Merlwyb (Limsa: victory report)
- Next: When Yugiri Met the Fraternity
- Manifest tie: LEVIATHAN (The Whorleater) primal beat, patch 2.2.

**When Yugiri Met the Fraternity** — giver: Zanthael (Limsa Lominsa Lower Decks) `[COND: relay]`
- Zanthael (Merlwyb's Letter of Introduction) -> The Inconspicuous Man (receive the letter; meet Yugiri)
- Next: Through the Maelstrom

**Through the Maelstrom** — giver: Yugiri (Limsa Lominsa Lower Decks)
- Yugiri (relay gratitude to Minfilia) -> Minfilia (her conclusions on the Echo & the Ascians)
- Next: The Great Divide   (= PATCH 2.3 opener)
- Manifest tie: End of patch 2.2. Echo/Ascian thread advances (respect 05 Ch.1 reveal-gate).

---

## SEVENTH ASTRAL ERA — PATCH 2.3 'DEFENDERS OF EORZEA' (Ramuh arc + Crystal Braves) (VERIFIED, CGW)

**The Great Divide** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- refugees in the Seventh Heaven -> search for Alphinaud in Ul'dah
- Next: Desperate Times

**Desperate Times** — giver: Alphinaud (Ul'dah - Steps of Nald) `[COND: relay]`
- Raubahn (Hall of Flames) -> Swift -> Brass Blades (Lost Hope) -> Zazawaka -> Terrified Refugee -> /soothe the Terrified Refugee
- Next: Shock and Awe

**Shock and Awe** — giver: Terrified Refugee (Central Thanalan) `[COND: fetch]`
- search the caves S of Lost Hope for the other refugees -> Desperate Refugee -> Terrified Refugee
- Next: Reap the Whirlwind

**Reap the Whirlwind** — giver: Terrified Refugee (Hall of Flames) `[COND: relay]`
- search Stonesthrow for the merchant -> the Ul'dah Dispatch Yard -> Stone Torch -> Swift (Hall of Flames)
- Next: Revolution   [CGW Next-field unscraped; resolved via scaffold + Swift giver of Revolution]

**Revolution** — giver: Swift (Ul'dah - Steps of Nald)
- Bartholomew (Royal Promenade)
- Next: Stories We Tell

**Stories We Tell** — giver: Alphinaud (Ul'dah - Steps of Thal)
- Minfilia (the Rising Stones)
- Next: Lord of Levin

**Lord of Levin** — giver: Minfilia (the Rising Stones)
- Vorsaile Heuloix (Adders' Nest) -> Kan-E-Senna (Lotus Stand) -> Serpent lieutenant (Little Solace)   [sets up the Ramuh arc]
- Next: Levin an Impression   (do the Sylphlands sub-chain first; all converge at Levin an Impression)

### Sylphlands infiltration sub-chain (parallel; converges at Levin an Impression)
**A Sylphlands Sting** — giver: Serpent Lieutenant (East Shroud)
- Komuxio (cleansing water on the soldiers) -> Hostile Sylph -> Maxio -> Maxio -> (invisible) stinging scalebomb on the Hostile Sylph -> Maxio -> Teary-eyed Private
- Next: Scattered Scions

**Scattered Scions** — giver: Teary-eyed Private (East Shroud)
- Papalymo (Goldleaf Dais) -> Maxio (trueform scalebombs) -> Yda & Papalymo impostors (scalebomb & defeat) -> Maxio -> Yda & Thancred impostors (reveal & defeat) -> Yda
- Next: True to Form

**True to Form** — giver: Yda (East Shroud)
- Maxio -> trueform scalebomb on the suspect Scions -> approach the touched sylph & defeat resistance -> confront the touched sylph -> Papalymo
- Next: Levin an Impression

**Levin an Impression** — giver: Serpent Lieutenant (Little Solace, East Shroud)
- Maxio -> Maxio -> search for the Scions -> investigate the beastman aetheryte in the Sylphlands -> [The Striking Tree (Hard): RAMUH] -> Serpent Lieutenant (Little Solace)
- Next: What Little Gods Are Made Of
- Manifest tie: RAMUH (The Striking Tree) primal beat, patch 2.3.

**What Little Gods Are Made Of** — giver: Serpent Lieutenant (East Shroud) `[COND: relay]`
- Kan-E-Senna (Lotus Stand) -> Papalymo (Nophica's Altar) -> Minfilia (the Rising Stones)
- Next: Guardian of Eorzea

### Tataru side cluster (parallel; converges at Guardian of Eorzea)
**A Hard Hapalit to Break** — giver: Minfilia Warde (the Rising Stones) `[COND: fetch]`
- Slafborn (Revenant's Toll) -> slay the hapalit threatening the struggling adventurer (Singing Shards) -> aid her -> /huh -> Slafborn
- Next: Picking Up the Sledge

**Picking Up the Sledge** — giver: Slafborn (Mor Dhona)
- Tataru (Rising Stones) -> Brithael (Blacksmiths' Guild) -> /doubt the Prickly Porter -> pick up the box for Tataru -> F'lhaminn (deliver) -> call out \"Tataru\" in Say -> defeat the morbol threatening Tataru -> Tataru -> Tataru (Rising Stones)
- Next: Guardian of Eorzea

**Guardian of Eorzea** — giver: Minfilia (the Rising Stones)   [convergence of main line + Tataru cluster]
- Yozan -> meet Hoary Boulder (E of Revenant's Toll) -> Alphinaud (the Rising Stones)
- Next: Recruiting the Realm

### Crystal Braves founding
**Recruiting the Realm** — giver: Alphinaud (the Rising Stones)
- Alphinaud (Bulwark Hall) -> scout the upper decks (recruit RIOL) -> Alphinaud (Limsa airship landing) -> Alphinaud (Nophica's Altar) -> scout Old Gridania (recruit LAURENTIUS & ALIANNE) -> Alphinaud (Gridania airship landing) -> Alphinaud (Royal Promenade) -> scout the Steps of Thal (recruit WILRED) -> Alphinaud (Royal Promenade) -> Alphinaud (Rising Stones)
- Next: Heretical Harassment

**Heretical Harassment** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- Slafborn (Revenant's Toll) -> Haurchefant (Camp Dragonhead)
- Next: When the Cold Sets In

**When the Cold Sets In** — giver: Haurchefant (Coerthas Central Highlands)
- Drillemont (Whitebrim Front) -> mistreated merchant -> search Snowcloak wilds & defeat heretics -> House Durendaire knight -> again -> Drillemont -> Haurchefant -> Slafborn (Revenant's Toll)
- Next: Brave New Companions

**Brave New Companions** — giver: Slafborn (Mor Dhona)
- Tataru (Rising Stones: uniform delivery) -> present ultramarine uniforms to the 8 recruits (Revenant's Toll) -> Alphinaud (Rising Stones: CRYSTAL BRAVES founding ceremony) -> Minfilia (concerns about Hydaelyn's silence)
- Next: Traitor in the Midst   (= PATCH 2.4 opener)
- Manifest tie: CRYSTAL BRAVES founded (Alphinaud's order). End of patch 2.3. Sets up the 2.55 betrayal thread — keep foreshadowing reveal-gated (05 Ch.1).

---

## SEVENTH ASTRAL ERA — PATCH 2.4 'DREAMS OF ICE' (Shiva arc / Iceheart) (VERIFIED, CGW)

**Traitor in the Midst** — giver: Minfilia (the Rising Stones)
- Alphinaud -> Ilberd -> Raubahn (Hall of Flames)
- Next: Back and Fourth

**Back and Fourth** — giver: Ilberd (Ul'dah - Steps of Nald)
- Alphinaud (Rising Stones) -> Alianne (the Tangle) -> find Rhesh Polaali (Castrum Centri) -> defeat imperial troops (0/3) -> Alianne (the Tangle) -> Alphinaud (Rising Stones)
- Next: Coming to Terms

**Coming to Terms** — giver: Alphinaud (the Rising Stones) `[COND: relay]`
- Minfilia -> Haurchefant (Camp Dragonhead) -> House Fortemps guard
- Next: The Intercession of Saints

**The Intercession of Saints** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Haurchefant -> House Fortemps knight (Boulder Downs) -> surviving squire (the Observatorium) -> Alphinaud
- Next: Strength in Unity

**Strength in Unity** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Drillemont (Whitebrim Front)
- Next: Dark Words, Dark Deeds

**Dark Words, Dark Deeds** — giver: Drillemont (Coerthas Central Highlands)
- observe the suspected heretic (Ser Jeantremont) -> follow through the SW gate -> surveil E along the road -> follow S toward Daniffen Pass -> observe the meeting with a robed heretic -> Drillemont
- Next: First Blood

**First Blood** — giver: Drillemont (Coerthas Central Highlands) `[COND: fetch]`
- rendezvous with the House Durendaire knights -> search the heretic's effects -> deliver the parchment to Drillemont
- Next: The Path of the Righteous

**The Path of the Righteous** — giver: Drillemont (Coerthas Central Highlands)
- Aymeric (Snowcloak) -> Alphinaud -> Stalwart Temple Knight -> [Snowcloak — dungeon duty] -> Alphinaud (report)
- Next: For the Greater Good
- Note: AYMERIC first appears here (Coerthas). Reveal-gate any Ishgard/Heavensward foreshadowing (05 Ch.1).

**For the Greater Good** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Yuyuhase -> pursue the heretics toward Daniffen Pass -> search S of Daniffen Pass -> follow the trail -> Yuyuhase -> search outside the Observatorium -> Alphinaud
- Next: Tendrils of Intrigue

**Tendrils of Intrigue** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Alphinaud -> Alphinaud (Old Gridania) -> silent conjurer -> Alphinaud -> Ilberd (New Gridania)
- Next: Chasing Ivy

**Chasing Ivy** — giver: Ilberd (New Gridania) `[COND: relay]`
- Ilberd -> Ilberd -> Ephemie (airship landing) -> Ilberd
- Next: In Flagrante Delicto

**In Flagrante Delicto** — giver: Ilberd (New Gridania)
- Ilberd (Sweetbloom Pier) -> Yugiri (near the Hawthorne Hut) -> Yugiri (the Bramble Patch) -> Yugiri -> Minfilia
- Next: A Simple Plan

**A Simple Plan** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- wait for the carriage outside Revenant's Toll -> Minfilia
- Next: The Instruments of Our Deliverance

**The Instruments of Our Deliverance** — giver: Minfilia (the Rising Stones)
- Alphinaud (Snowcloak) -> Alphinaud -> stalwart Temple Knight -> [Akh Afah Amphitheatre (Hard): SHIVA] -> Moenbryda
- Next: The Road Less Traveled
- Manifest tie: SHIVA (Akh Afah Amphitheatre) primal beat, patch 2.4 — tied to Ysayle / Iceheart. Reveal-gate her identity per 05 Ch.1.

**The Road Less Traveled** — giver: Moenbryda (Coerthas Central Highlands) `[COND: relay]`
- Alphinaud (Whitebrim Front) -> Haurchefant (Camp Dragonhead) -> House Fortemps guard
- Next: Eyes Unclouded

**Eyes Unclouded** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Minfilia (the Rising Stones)   [aftermath of Shiva / Ysayle-Iceheart]
- Next: The Reason Roaille

**The Reason Roaille** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- Alphinaud -> Ilberd (Camp Bluefog, N Thanalan) -> Ilberd (Ceruleum Processing Plant) -> Alphinaud
- Next: Let Us Cling Together

**Let Us Cling Together** — giver: Alphinaud (Northern Thanalan)
- Alphinaud (interrogation plans with Ilberd) -> Minfilia (Rising Stones: report) -> Moenbryda (white auracite & the blade of Light) -> Urianger (research on an aether blade) -> Raubahn (interrogate Roaille & associates)
- Next: Good Intentions   (= PATCH 2.5 opener)
- Manifest tie: End of patch 2.4. White auracite / aether-blade research set up (leads to Lahabrea's defeat in 2.5). Keep reveal-gated (05 Ch.1).

---

## SEVENTH ASTRAL ERA — PATCH 2.5 + 2.55 'BEFORE THE FALL' (Nabriales / Steps of Faith / Crystal Braves betrayal) (VERIFIED, CGW)

### Part 1 (patch 2.5)
**Good Intentions** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- Riol -> Ilberd (Highbridge)
- Next: Bait and Switch

**Bait and Switch** — giver: Ilberd (Eastern Thanalan) `[COND: relay]`
- Ilberd -> hired thug -> wait for Ilberd outside the tunnel entrance -> investigate the disturbance
- Next: Best-laid Schemes

**Best-laid Schemes** — giver: Ilberd (Eastern Thanalan - Wellwick Wood) `[COND: fetch]`
- collect the confiscated crate -> deliver it to Yuyuhase (Ul'dah - Steps of Thal) -> Riol (Sapphire Avenue Exchange) -> Tataru (the Rising Stones)
- Next: The Rising Chorus

**The Rising Chorus** — giver: Tataru (the Rising Stones)
- Minfilia -> Doman watch (Mor Dhona) -> enter the Keeper of the Lake -> Doman watch -> Alphinaud (Rising Stones) -> Alphinaud
- Next: Aether on Demand

**Aether on Demand** — giver: Alphinaud (the Rising Stones) `[COND: relay]`
- Moenbryda -> Moenbryda -> Alphinaud -> Wilred (Ceruleum Processing Plant) -> Edelstein
- Next: On the Counteroffensive

**On the Counteroffensive** — giver: Lieutenant Edelstein (Northern Thanalan)
- Alianne -> Yuyuhase -> defeat the imperial squad -> defeat the next imperial squad -> Yuyuhase -> Edelstein
- Next: An Uninvited Ascian

**An Uninvited Ascian** — giver: Edelstein (Northern Thanalan)
- Moenbryda (Dalamud's Talons) -> return to the Rising Stones -> [The Chrysalis: NABRIALES] -> MOENBRYDA sacrifices her life to defeat Nabriales (white auracite / aether blade) -> Minfilia
- Next: In Memory of Moenbryda
- Manifest tie: NABRIALES (The Chrysalis) trial, patch 2.5. Moenbryda's death. Major emotional beat — respect reveal-gate on Ascian lore (05 Ch.1).

**In Memory of Moenbryda** — giver: Minfilia (the Rising Stones)
- pay respects at the mark of the Scholar (Rathefrost) -> Minfilia
- Next: Mask of Grief

**Mask of Grief** — giver: Minfilia (the Rising Stones)
- Yda -> hand the flower payment to Rowena -> deliver the moon daisy to Yda (Rathefrost) -> Alphinaud (Rising Stones)
- Next: Defenders for Ishgard

**Defenders for Ishgard** — giver: Alphinaud (the Rising Stones) `[COND: parallel → An Allied Perspective]`
- Alphinaud (Camp Dragonhead) -> question the knights at the Gates of Judgement (0/4) -> Alphinaud
- Next: The Wyrm's Roar

**The Wyrm's Roar** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Haurchefant -> Aymeric (the intercessory) -> Alphinaud
- Next: Committed to the Cause

**Committed to the Cause** — giver: Alphinaud (Intercessory) `[COND: relay]`
- Minfilia (the Rising Stones)
- Next: Volunteer Dragonslayers

**Volunteer Dragonslayers** — giver: Minfilia (the Rising Stones) `[COND: parallel → An Allied Perspective]`
- Tataru -> Slafborn (Revenant's Toll) -> Tataru -> recruit 4 volunteers -> Tataru (report)
- Next: An Allied Perspective

**An Allied Perspective** — giver: Tataru (Mor Dhona)
- Alphinaud (Royal Promenade) -> Alphinaud -> Marcelain (Gates of Judgement) -> defeat Dravanian forces at Whitebrim -> at Providence Point -> Marcelain
- Next: The Steps of Faith

**The Steps of Faith** — giver: Marcelain
- Marcelain -> Alphinaud (Gates of Judgement) -> [The Steps of Faith — trial: VISHAP (defense of the Steps of Faith)] -> Minfilia (the Rising Stones)
- Next: Administrative Decision
- Manifest tie: VISHAP / The Steps of Faith trial (the great bridge before Ishgard). Foreshadows Heavensward — reveal-gate (05 Ch.1).

### Part 2 (patch 2.55) — the calm, then the fall
**Administrative Decision** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- look for Tataru at her desk -> F'lhaminn -> search for Tataru (Revenant's Toll) -> Minfilia
- Next: An Unexpected Ambition

**An Unexpected Ambition** — giver: Minfilia (the Rising Stones) `[COND: relay]`
- Tataru (Arcanists' Guild) -> Thubyrgeim -> observe Tataru's training S of the Zephyr Gate -> Tataru -> Thubyrgeim
- Next: Ancient Ways, Timeless Wants

**Ancient Ways, Timeless Wants** — giver: Tataru (Limsa Lominsa Lower Decks) `[COND: relay]`
- Tataru (Costa del Sol) -> Tataru -> stand guard as Tataru harvests pearls -> Tataru -> Minfilia (Rising Stones)
- Next: A Time to Every Purpose

**Where We Are Needed** — giver: Minfilia (the Rising Stones) `[COND: parallel → A Time to Every Purpose]`   [parallel Scion vignette; converges at A Time to Every Purpose]
- Hoary Boulder -> unsettled scholar (Camp Tranquil) -> escort to Issom-Har / Snakemolt / Rootslake (stand guard for measurements at each) -> unsettled scholar (Camp Tranquil)
- Next: The Least among Us

**The Least among Us** — giver: Unsettled Scholar (South Shroud) `[COND: fetch]`
- Unsettled Scholar (Urth's Fount) -> stand guard for measurements -> Minfilia (Rising Stones)
- Next: A Time to Every Purpose

**A Time to Every Purpose** — giver: Minfilia (the Rising Stones)   [convergence — last calm before the banquet]
- Minfilia -> Minfilia (Royal Promenade) -> Riol (as you leave the solar) -> rendezvous with Minfilia & the Scions (Royal Promenade)
- Next: Come, but Not Gone

**Come, but Not Gone** — giver: Minfilia (Ul'dah - Steps of Thal)
- Momodi (the Quicksand) -> rendezvous with Alianne (central Thanalan) -> keep waiting -> pick up the clouded vial -> show the clouded vial to Momodi
- Next: The Parting Glass

**The Parting Glass** — giver: Momodi (Ul'dah - Steps of Nald)
- lady-in-waiting (Royal Promenade) -> Pipin -> Haurchefant (Camp Dragonhead)
- Next: Before the Dawn

**Before the Dawn** — giver: House Fortemps Guard (the Intercessory, Ishgard)
- aftermath of the ULK'DAH BANQUET betrayal by the CRYSTAL BRAVES: Tataru & Yugiri (escape from the Crystal Braves in Limsa, Tataru rescued) -> Urianger (glamour hiding the refugees at the Waking Sands) -> ALPHINAUD (despair over the banquet betrayal & his role in founding the Braves) -> Lord Haurchefant & Tataru (encouragement to fight on) -> RAUBAHN imprisoned (cutscene) -> the Sultana (arrangements implied) -> ASCIANS discussing the northern lands & fate -> journey north to the gates of Ishgard
- Next: bridges to HEAVENSWARD (post-'Before the Dawn' opening -> 'Coming to Ishgard' begins 3.0)
- Manifest tie: ARR FINALE. Nald'thal banquet / regicide setup, Crystal Braves turn, Warrior of Light + Alphinaud flee to Ishgard under House Fortemps. HARD reveal-gate: identities & motives per 05 Ch.1.

---

> END 08.2 — ORDERED MSQ INDEX (ARR complete: openings + 2.0 + 2.1-2.55).

# 08.3 — ORDERED MSQ INDEX (AUTHORITATIVE DATA) — HEAVENSWARD (3.0 -> 3.56)

(convenzioni: vedi 08.0)

**SEAM FROM ARR:** ARR 2.55 (The Parting Glass / flight to Coerthas) -> **Coming to Ishgard** = first HW beat.

**SCOPE OF INSTALLMENT 1:** HW 3.0, arrival in Ishgard + the House Fortemps support chains (Artoirel + Emmanellain, run in parallel) -> Divine Intervention -> Disclosure. Levels ~50.

---

## MAIN — arrival in Ishgard

**Coming to Ishgard** — giver: Alphinaud (the Intercessory)
- Haurchefant -> Temple Knight gateguard (Gates of Judgement) -> House Fortemps manservant -> Haurchefant outside Fortemps Manor (the Pillars)
- Next: Taking in the Sights

**Taking in the Sights** — giver: Alphinaud (Fortemps Manor) `[COND: relay]`
- House Fortemps manservant -> manservant in the Hoplon -> Elaisse (the Jeweled Crozier) -> manservant in the aetheryte plaza
- Next: The Better Half

**The Better Half** — giver: Alphinaud (Ishgard - Foundation)
- Gibrillont (the Forgotten Knight tavern) -> observe the upper/lower-floor divide -> learn of the Dravanian attack's impact on the Brume -> Tataru stays behind to gather info -> return to Fortemps Manor -> Count Edmont de Fortemps -> accept the charge to aid House Fortemps and its two sons
- Next: the TWO support chains unlock IN PARALLEL — **Over the Wall** (Artoirel chain) + **Onwards and Upwards** (Emmanellain chain); both reconverge at Divine Intervention.

---

## SUPPORT CHAIN A — Lord Artoirel (Coerthas Western Highlands / Falcon's Nest)

**Over the Wall** — giver: Lord Artoirel de Fortemps (Foundation) `[COND: relay]`
- chocobokeep in Foundation -> journey to Falcon's Nest -> Artoirel -> Redwald
- Next: Work in Progress

**Work in Progress** — giver: Ser Redwald (Coerthas Western Highlands) `[COND: fetch]`
- Rothe -> search Falcon's Nest for icicle sprites -> report to Rothe
- Next: The First and Foremost

**The First and Foremost** — giver: Rothe (Coerthas Western Highlands) `[COND: fetch]`
- Thierremont (the Pike) -> slay deepeyes, obtain 3 dark bristles -> deliver to Thierremont
- Next: From on High

**From on High** — giver: Thierremont (Falcon's Nest) `[COND: fetch]`
- deliver the ice-crusted bundle to Ysaudore (the Anvil) -> report to Redwald
- Next: Reconnaissance Lost

**Reconnaissance Lost** — giver: Redwald (Coerthas Western Highlands)
- Artoirel (Falcon's Nest) -> follow Artoirel to the cliffs overlooking Camp Riversmeet -> to the cliffs east of the Black Iron Bridge -> search Camp Riversmeet for the missing knights -> aid the wounded knight
- Next: At the End of Our Hope

**At the End of Our Hope** — giver: Artoirel (Coerthas Western Highlands)
- search for the heretics' trail N of Camp Riversmeet -> examine the footprints -> [Solo Duty] defeat the basement enemies -> follow the fleeing heretic -> survey the hiding place -> Artoirel
- Next: Knights Be Not Proud

**Knights Be Not Proud** — giver: Artoirel (Coerthas Western Highlands) `[COND: relay]`
- Redwald -> Artoirel (Fortemps Manor)
- Next: Divine Intervention (converge)

---

## SUPPORT CHAIN B — Lord Emmanellain (the Sea of Clouds / Camp Cloudtop)

**Onwards and Upwards** — giver: Emmanellain de Fortemps (Foundation) `[COND: relay]`
- airship ticketer -> travel to the Sea of Clouds -> Emmanellain -> Laniaitte
- Next: An Indispensable Ally

**An Indispensable Ally** — giver: Laniaitte (the Sea of Clouds) `[COND: relay]`
- Emmanellain -> Honoroit -> Laniaitte
- Next: Meeting the Neighbors

**Meeting the Neighbors** — giver: Laniaitte (the Sea of Clouds) `[COND: fetch]`
- Marielle -> keep watch for Vanu -> report to Marielle
- Next: Sense of Urgency

**Sense of Urgency** — giver: Ser Marielle (the Sea of Clouds) `[COND: parallel → A Series of Unfortunate Events]`
- find sentries and psych them up (0/3) -> report to Marielle
- Next: Hope Springs Eternal

**Hope Springs Eternal** — giver: Ser Marielle (the Sea of Clouds) `[COND: fetch]`
- Laniaitte -> Emmanellain -> Emmanellain near Voor Sian Siran -> search for a spring crystal in Voor Sian Siran -> deliver it to Honoroit
- Next: A Series of Unfortunate Events

**A Series of Unfortunate Events** — giver: Honoroit (the Sea of Clouds)
- search for Emmanellain in Voor Sian Siran -> rendezvous with Honoroit -> Honoroit -> Cid
- Next: A Reward Long in Coming

**A Reward Long in Coming** — giver: Emmanellain (Fortemps Manor / the Sea of Clouds) `[COND: relay]`
- Laniaitte -> Haurchefant (Ishgard) -> Emmanellain (Fortemps Manor)
- Next: Divine Intervention (converge)

---

## MAIN — converge -> the tribunal

**Divine Intervention** — giver: House Fortemps Steward (Fortemps Manor)
- Edmont -> Aymeric (Foundation) -> Haurchefant (the Pillars) -> Haurchefant (at the tribunal) -> [Solo Duty] defeat Ser Grinnaux the Bull + Ser Paulecrain Coldfire -> Haurchefant after the trial
- Next: Disclosure

**Disclosure** — giver: Lord Haurchefant (Fortemps Manor) `[COND: relay]`
- Edmont (Fortemps Manor) -> the priest at the Vault -> Alphinaud (Fortemps Manor)
- Next: Flame General Affairs

---

**SCOPE:** the Raubahn gaol-break -> the search for Iceheart / the Convictors -> the Gnath "deity" arc -> RAVANA -> Sohm Al -> Beyond the Clouds (L51-53).

---

**Flame General Affairs** — giver: Alphinaud (the Rising Stones) `[COND: relay]`
- Storm Sergeant Zanthael (Bulwark Hall, Limsa) -> the Bridge, meet Admiral Merlwyb -> Higiri (Revenant's Toll kitchen)
- Next: In Search of Raubahn

**In Search of Raubahn** — giver: Higiri (Mor Dhona) `[COND: relay]`
- Doware (Highbridge) -> Hozan (Halatali entrance)
- Next: Keeping the Flame Alive

**Keeping the Flame Alive** — giver: Hozan (Eastern Thanalan)
- Hozan -> Hozan (again) -> Doware (in front of Halatali) -> Alphinaud -> enter the Waking Sands -> Alphinaud
- [Solo Duty] RESCUE RAUBAHN: defeat Crystal Braves for the key -> destroy the mist source -> free Raubahn -> defeat ILBERD of the Dull Blade + allies (Yuyuhase, Laurentius, 2 Crystal Braves)
- Next: To Siege or Not to Siege

**To Siege or Not to Siege** — giver: Alphinaud (the Waking Sands) `[COND: relay]`
- Tataru (outside Fortemps Manor) -> enter Fortemps Manor -> Alphinaud
- Next: Alphinaud's Way

**Alphinaud's Way** — giver: Alphinaud (the Pillars) `[COND: relay]`
- Alphinaud -> enter the Seat of the Lord Commander (Congregation of Our Knights Most Heavenly) -> Alphinaud
- Next: In Search of Iceheart

**In Search of Iceheart** — giver: Alphinaud (Coerthas Western Highlands)
- return to Fortemps Manor -> Estinien -> Redwald (Falcon's Nest) -> the expedition leader -> slay the beasts within Gorgagne Mills -> the expedition leader
- Next: From One Heretic to Another

**From One Heretic to Another** — giver: Expedition Leader (Coerthas Western Highlands) `[COND: fetch]`
- collect heretic epistles (0/3) -> hand them to the expedition leader
- Next: Sounding Out the Amphitheatre

**Sounding Out the Amphitheatre** — giver: Alphinaud (Akh Afah Amphitheatre)
- Tristechambel -> [Solo Duty] defeat the heretics -> Estinien -> Jantellot (the Convictors' camp)
- Next: Camp of the Convictors

**Camp of the Convictors** — giver: Alphinaud (Camp of the Convictors) `[COND: parallel → Where the Chocobos Roam]`
- question the Convictors (0/3) -> Pierriquet
- Next: Purple Flame, Purple Flame

**Purple Flame, Purple Flame** — giver: Estinien (Coerthas Western Highlands) `[COND: fetch]`
- obtain yak hides from woolly yaks (0/2) -> deliver to Estinien
- Next: Where the Chocobos Roam

**Where the Chocobos Roam** — giver: Ysayle (Coerthas Western Highlands)
- journey into the Dravanian forelands -> Ysayle -> Marcechamp
- Next: Worse than Dragons

**Worse than Dragons** — giver: Marcechamp (the Dravanian Forelands) `[COND: fetch]`
- Ysayle -> press on toward the Stained One, defeating foes en route
- Next: The Trine Towers

**The Trine Towers** — giver: Ysayle (the Dravanian Forelands) `[COND: fetch]`
- Ysayle -> defeat enemies on the path to Anyx Trine (x2) -> Ysayle
- Next: Gifts for the Outcasts

**Gifts for the Outcasts** — giver: Marcechamp (Tailfeather) `[COND: fetch]`
- Marcechamp -> obtain hunks of nanka flesh from clearwater nanka -> deliver to Alphinaud
- Next: The Nonmind

**The Nonmind** — giver: Alphinaud (the Gnath trading post / Loth ast Vath)
- the Vath fleetfoot -> the Vath storyteller
- Next: A Gnathic Deity

**A Gnathic Deity** — giver: Ysayle (Loth ast Vath) `[COND: parallel → Breaking into Hives]`
- gather information from the Vath (0/3) -> the voracious Vath -> obtain a hunk of nanka flesh (clearwater nanka) -> deliver to the voracious Vath -> Alphinaud
- Next: Breaking into Hives

**Breaking into Hives** — giver: Alphinaud (near Loth ast Gnath)
- provoke the Gnath drone + clear resistance -> Ysayle -> fight deeper into the hive -> wait for Ysayle deeper within (a staged capture by the Gnath)
- Next: Lord of the Hive

**Lord of the Hive** — giver: Ysayle (the Dravanian Forelands)
- surrender to the Gnath -> enter the inner chamber -> [TRIAL: Thok ast Thok (Hard) = RAVANA] confront Ravana -> Ysayle -> Alphinaud
- Next: Mourn in Passing
- Manifest tie: RAVANA (Thok ast Thok), 08.1 HW L10.

**Mourn in Passing** — giver: Alphinaud (the Dravanian Forelands)
- Vidofnir -> meet Vidofnir in the cavern of Mourn -> [DUNGEON: Sohm Al] -> Alphinaud
- Next: Beyond the Clouds
- Manifest tie: Sohm Al dungeon (08.1 HW L9 dungeon list).

**Beyond the Clouds** — giver: Alphinaud (the Churning Mists) `[COND: fetch]`
- Alphinaud -> search for the moogle at the marked spots -> Alphinaud
- Next: Mountaintop Diplomacy

---

**SCOPE:** Moghome + the moogle trials -> the Road to Zenith / Hraesvelgr -> the Ul'dah interlude -> THE AERY (Nidhogg's eyes) -> back to Ishgard (L54-56).

**EXTRACTION-ANOMALY NOTE (binding):** a few CGW quest pages exposed a `Next` that DISAGREES with the clean CGW ordered index (they surfaced an unlock/related link, not the MSQ next). Where they conflict, ORDER FOLLOWS THE INDEX and the page value is flagged for play-time check. One quest omitted by the index-page extraction — **Trials of Trustworthiness** — is confirmed as the `Next` of Mountaintop Diplomacy and is inserted here.

---

**Mountaintop Diplomacy** — giver: Alphinaud (Nophica's Altar, Old Gridania) `[COND: relay]`
- Alphinaud (Nophica's Altar) -> enter the Lotus Stand -> Alphinaud -> Estinien (Moghome) -> Moglin
- Next: Trials of Trustworthiness

**Trials of Trustworthiness** — giver: Moglin (Moghome) `[COND: relay]` [CGW-verified — the three challenges Moglin devised to measure your worth]
- Moghan (Moghome) -> Mogmug (Moghome) -> Mogwin (Moghome): meet the three wise moogles who will administer the trials
- Next: the three moogle trials (Moghan's / Mogmug's / Mogwin's Trial), then Moglin's Judgment

**Moghan's Trial** — giver: Moghan (moogle alchemist, Moghome) `[COND: fetch]`
- obtain sprigs of cloudsbreath (0/3, near Eil Tohm) -> deliver to Moghan

**Mogmug's Trial** — giver: Mogmug (Moghome) `[COND: fetch]`
- defeat archaeosaurs at Eil Tohm -> report to Mogmug

**Mogwin's Trial** — giver: Mogwin (Moghome) `[COND: fetch]`
- question Moghome inhabitants -> Mogwin -> obtain the moogle masterpiece -> deliver to Mogwin

**Moglin's Judgment** — giver: Chieftain Moglin (Moghome)
- Alphinaud -> Estinien -> Ysayle -> Kan-E-Senna -> Kuplo Kopp -> Moglin -> Moghan
- Next: Leaving Moghome

**Leaving Moghome** — giver: Moghan (Moghome) `[COND: relay]`
- Alphinaud -> Kan-E-Senna -> Moghan
- Next: The Road to Zenith

**The Road to Zenith** — giver: Moghan (the Churning Mists) `[COND: fetch]`
- defeat enemies on the path to Asah (x2) -> Moghan
- Next: Waiting for the Wind to Change

**Waiting for the Wind to Change** — giver: Moghan (the Churning Mists) `[COND: fetch]`
- Moghan -> defeat threatening monsters W of Alphinaud -> then E of Alphinaud -> Estinien
- Next: Heart of Ice

**Heart of Ice** — giver: Moghan (the Churning Mists)
- blow the horn on the top floor of Zenith -> Alphinaud [meeting with HRAESVELGR; the Dragonsong War truth]
- Next: The Wyrm's Lair

**The Wyrm's Lair** — giver: Alphinaud (eastern approach to the Aery) `[COND: fetch]`
- defeat enemies searching for the Aery (x3) -> Estinien [the wind barrier around the Aery -> need Cid/Garlond]
- Next: New Winds, Old Friends

**New Winds, Old Friends** — giver: Estinien (the Churning Mists) `[COND: relay]`
- Alphinaud (Saint Reinette's Forum) -> Emmanellain (Fortemps Manor) -> Cid (airship landing) -> Biggs (outside the Skysteel Manufactory)
- Next: A General Summons

**A General Summons** — giver: Tataru (Foundation) `[COND: relay]`
- enter the Waking Sands -> Yugiri -> question Silver Bazaar residents -> search for Meriel -> Alphinaud
- Next: Awakening in Ul'dah

**Awakening in Ul'dah** — giver: Alphinaud (Western Thanalan) `[COND: relay]`
- Bartholomew (Royal Promenade) -> Alphinaud
- Next: A Brave Resolution

**A Brave Resolution** — giver: Alphinaud (Ul'dah - Steps of Thal) `[COND: relay]`
- enter the Rising Stones -> Alphinaud
- Next: Ready to Fly

**Ready to Fly** — giver: Alphinaud (the Rising Stones) `[COND: relay]`
- Cid (Skysteel Manufactory) -> Estinien (Fortemps Manor) -> the Seat of the Lord Commander -> Estinien
- Next: Into the Aery

**Into the Aery** — giver: Estinien (Skysteel Manufactory)
- Cid -> [DUNGEON: The Aery] -> Estinien [ESTINIEN slays NIDHOGG and takes the two great eyes]
- Next: The Song Begins
- Manifest tie: The Aery / Nidhogg's eyes (08.1 HW L10).

**The Song Begins** — giver: Estinien (-> Zenith, the Churning Mists)
- Ysayle -> (continues)
- Next: Unrest in Ishgard

**Unrest in Ishgard** — giver: Estinien (the Churning Mists) `[COND: relay]`
- speak to Haurchefant (return to Ishgard) [CGW-verified: NO solo duty in this quest — 'Orthodox Mayhem' is NOT here; the earlier flag was wrong]
- Next: He Who Would Not Be Denied

**He Who Would Not Be Denied** — giver: Lord Haurchefant (Fortemps Manor) `[COND: relay]`
- return to Fortemps Manor -> Lucia
- Next: Ill-weather Friends

**Ill-weather Friends** — giver: Alphinaud (the Pillars) `[COND: parallel → Fire and Blood]`
- Tataru (the Forgotten Knight) -> question the Brume residents -> Alphinaud
- Next: The Spice of Life

---

**SCOPE:** the Brume/heretic thread -> THE VAULT (Haurchefant's death) -> the Dragonsong War truth -> the Vanu Vanu / BISMARCK arc -> Y'shtola retrieved from the Lifestream -> the approach to Sharlayan/Matoya (L56-57).

---

**The Spice of Life** — giver: Alphinaud (the Brume) `[COND: fetch]`
- Gibrillont -> the hunter at the Pillars -> deliver fresh herbs to Gibrillont
- Next: Noble Indiscretions

**Noble Indiscretions** — giver: Gibrillont (Foundation) `[COND: fetch]`
- deliver twice-mulled wine to Hierytha (the Pillars) -> report to Gibrillont
- Next: A Child Apart

**A Child Apart** — giver: Gibrillont (the Forgotten Knight) `[COND: fetch]`
- deliver twice-mulled wine to Gerraldieux -> report to Gibrillont
- Next: Bloodlines

**Bloodlines** — giver: Gibrillont (the Brume) `[COND: relay]`
- the Brume starveling -> Alphinaud (the Forgotten Knight)
- Next: Fire and Blood

**Fire and Blood** — giver: Alphinaud (the Brume)
- search for Tataru in the Brume (x2) -> Hilda -> Hilda (the Forgotten Knight) -> [Solo Duty] defeat Ser Charibert + soldiers
- Next: A Knight's Calling

**A Knight's Calling** — giver: Hilda (Foundation)
- Lucia -> the Temple Knight squire outside the Vault -> [DUNGEON: The Vault] -> the Temple Knight squire -> return to Fortemps Manor -> Alphinaud
- Next: The Sins of Antiquity
- Manifest tie: THE VAULT — HAURCHEFANT DIES (08.1 HW L10).

**The Sins of Antiquity** — giver: Alphinaud (the Pillars)
- Aymeric (Congregation of Our Knights Most Heavenly) -> the Seat of the Lord Commander -> [Echo flashback vision: THE DRAGONSONG WAR TRUTH] -> discuss the Heavens' Ward's primal powers with Aymeric -> agree to bring the Archbishop to justice
- Next: In Search of the Soleil
- Manifest tie: the Dragonsong War truth surfaces here (08.1 HW L10).

**In Search of the Soleil** — giver: Lucia (Foundation) `[COND: relay]`
- Cid (Skysteel Manufactory)
- Next: Into the Blue

**Into the Blue** — giver: Alphinaud (Foundation) `[COND: relay]`
- Cid (airship landing) -> Wedge (x2) -> Alphinaud [setup for the Sea of Clouds / Bismarck; NOT the trial itself]
- Next: Familiar Faces

**Familiar Faces** — giver: Alphinaud (the Sea of Clouds)
- /lookout at the isle's eastern edge -> /lookout farther north -> [Solo Duty] protect the unarmed Vanu Vanu from imperial troops -> the Lonu Vanu
- Next: Devourer of Worlds

**Devourer of Worlds** — giver: Lonu Vanu (the Sea of Clouds) `[COND: relay]`
- Alphinaud -> Lonu Vanu (x2)
- Next: Black and the White

**Black and the White** — giver: Alphinaud (the Sea of Clouds — Bismarck's Feeding Grounds) `[COND: relay]`
- Lonu Vanu -> greet Kunu Vali with /bow -> Alphinaud
- Next: Bolt, Chain, and Island

**Bolt, Chain, and Island** — giver: Alphinaud (the Sea of Clouds)
- Sonu Vanu -> Cid -> Wedge -> [TRIAL: The Limitless Blue (Hard) = BISMARCK] -> Alphinaud
- Next: A Difference of Opinion
- Manifest tie: BISMARCK (The Limitless Blue), won just before Azys Lla (08.1 HW L10). After Bismarck the crystals relight partially (reduced Blessing, §B23).

**A Difference of Opinion** — giver: Alphinaud (the Sea of Clouds) `[COND: relay]`
- Alphinaud -> Cid
- Next: One Good Turn

**One Good Turn** — giver: Cid (the Sea of Clouds) `[COND: relay]`
- Cid
- Next: An Engineering Enterprise

**An Engineering Enterprise** — giver: Alphinaud (the Forgotten Knight) `[COND: relay]`
- the Congregation guardsman (admittance to the Seat of the Lord Commander) -> Aymeric -> Tataru (the Forgotten Knight)
- Next: Aetherial Trail

**Aetherial Trail** — giver: Tataru (Foundation) `[COND: relay]`
- Pipin Tarupin (Hall of Flames) -> Urianger (the Sil'dih excavation site) -> Alphinaud (Nophica's Altar)
- Next: Lost in the Lifestream

**Lost in the Lifestream** — giver: Alphinaud (Gridania)
- the silent conjurer (Nophica's Altar) -> Kan-E-Senna (the Lotus Stand) -> Tataru -> Y'mhitra (Apkallu Falls) -> accompany Y'mhitra to Everschade; the elementals retrieve Y'SHTOLA from the Lifestream -> the Roost, speak with Tataru
- Next: Tataru's Surprise

**Tataru's Surprise** — giver: Tataru (the Carline Canopy, New Gridania) `[COND: fetch]`
- Geva (Leatherworkers' Guild) -> E-Sumi-Yan (Conjurers' Guild) -> deliver the items to Tataru
- Next: Onward to Sharlayan

**Onward to Sharlayan** — giver: Y'shtola (New Gridania) `[COND: relay]`
- Y'shtola on her former master Matoya (a hermit in the Dravanian hinterlands) -> return to Ishgard, rejoin at the Aetheryte Plaza -> Alphinaud (Ishgard Aetheryte Plaza) -> travel W through the Dravanian forelands to Tailfeather -> Y'shtola (Tailfeather)
- Next: A Great New Nation

---

**SCOPE:** Idyllshire -> Matoya -> THE GREAT GUBAL LIBRARY -> the Excelsior to AZYS LLA -> Fetters of Lament -> **Heavensward** (the 3.0 climax: Ascian Prime + King Thordan). L58-60. This CLOSES base Heavensward 3.0.

---

**A Great New Nation** — giver: Y'shtola (Tailfeather)
- journey into the Dravanian hinterlands -> find a Thaliak River crossing -> Slowfix (Idyllshire)
- Next: Golems Begone

**Golems Begone** — giver: Slowfix (Idyllshire) `[COND: fetch]`
- Y'shtola -> (in Say chat) enter "Noughts and Crosses" to unmake golems (0/2) -> Slowfix
- Next: An Illuminati Incident

**An Illuminati Incident** — giver: Slowfix (Idyllshire) `[COND: relay]`
- search the Makers' Quarter for Slowfix's friend -> Y'shtola -> Slowfix
- Next: Leaving Idyllshire

**Leaving Idyllshire** — giver: Slowfix (Idyllshire) `[COND: relay]`
- the gobwatch -> Y'shtola
- Next: Matoya's Cave

**Matoya's Cave** — giver: Y'shtola (outside Matoya's Cave, the Dravanian Hinterlands) [CGW-verified]
- follow the road south through the Answering Quarter -> ford the stream at the broken bridge -> rejoin your companions at the base of the bluff -> lay a hand on the wall (weapon ready) -> fend off the ferocious frogs -> Y'shtola -> enter the cave: MATOYA (reunion; Alphinaud explains the aetheric ram + entry to Azys Lla; Matoya agrees to help)
- Next: Forbidden Knowledge

**Forbidden Knowledge** — giver: Matoya (Matoya's Cave)
- Matoya -> the enchanted broom -> the enchanted broom at the Great Gubal Library -> [DUNGEON: The Great Gubal Library] -> deliver the tome to Matoya
- Next: An Eye for Aether
- Manifest tie: The Great Gubal Library (08.1 HW L11 dungeon list).

**An Eye for Aether** — giver: Matoya (Matoya's Cave) `[COND: relay]`
- Alphinaud -> Aymeric (Congregation of Our Knights Most Heavenly) -> Cid (Ishgard airship landing)
- Next: Hour of Departure

**Hour of Departure** — giver: Alphinaud (the Pillars)
- Aymeric -> Lucia (Congregation) -> Tataru (the Forgotten Knight) -> Hilda (the Brume) -> Edmont (Fortemps Manor) -> Alphinaud (Ishgard airship landing)
- Next: The First Flight of the Excelsior

**The First Flight of the Excelsior** — giver: Alphinaud (Ishgard airship landing)
- Y'shtola -> Alphinaud (journey to AZYS LLA) -> Cid
- Next: Systematic Exploration

**Systematic Exploration** — giver: Cid (Azys Lla - Base Camp) `[COND: parallel → Close Encounters of the VIth Kind]`
- search for a terminal (0/3) -> Cid -> search for Wedge -> Cid
- Next: In Node We Trust

**In Node We Trust** — giver: Alphinaud (Azys Lla) `[COND: relay]`
- Alphinaud -> guidance node (Matter Conduit II-III) -> Allagan teleporter to the Beta Quadrant -> guidance node (Matter Conduit III-II)
- Next: Chimerical Maintenance

**Chimerical Maintenance** — giver: Guidance Node (Matter Conduit IV-V) `[COND: fetch]`
- guidance node (IV-V) -> defeat 3 chimerical creatures (Recombination Labs) -> guidance node (IV-V) -> Allagan teleporter to the Gamma Quadrant
- Next: Close Encounters of the VIth Kind

**Close Encounters of the VIth Kind** — giver: Estinien (Azys Lla)
- Estinien -> guidance node (VI-VII) -> guidance node (VII-VI) -> [Solo Duty] defeat Regula van Hydrus
- Next: Fetters of Lament

**Fetters of Lament** — giver: Guidance Node (Azys Lla)
- seek out Midgardsormr's child [TIAMAT — the Allag/Meracydia history; relights the penultimate crystal]
- Next: Heavensward
- Manifest tie: TIAMAT dialogue relights the penultimate crystal (08.1 HW L11).

**Heavensward** — giver: Guidance Node (the Flagship)
- guidance node + defeat enemies -> guidance node -> [DUNGEON: The Aetherochemical Research Facility] -> [TRIAL: The Singularity Reactor] confront Thordan VII -> Alphinaud (Fortemps Manor)
- Next: (post-HW / Patch 3.1 — the Nidhogg-possession + Warriors of Darkness thread)
- Manifest tie (08.1 HW L11): ASCIAN PRIME (Igeyorhm + Lahabrea) in the Aetherochemical Research Facility — Igeyorhm destroyed, Thordan kills Lahabrea (LAHABREA'S FINAL END) -> LAST crystal relights -> BLESSING FULLY RESTORED (Midgardsormr breaks the seal); then KING THORDAN + the Knights of the Round at the Singularity Reactor. NOTE: both duties sit inside this ONE L60 quest (they are consecutive climax duties, NOT separate MSQ quests).

---

> **END OF BASE HEAVENSWARD 3.0** (quests 1-94, CGW-verified across installments 1-5).
> Next: the POST-HEAVENSWARD PATCH chain 3.1-3.5 (As Goes Light, So Goes Darkness -> ... -> The Far Edge of Fate / Baelsar's Wall / Shinryu), on the CGW post-HW list — INSTALLMENT 6+.

---

## PATCH 3.1 — As Goes Light, So Goes Darkness

**An Uncertain Future** — giver: Alphinaud (Fortemps Manor) `[COND: relay]`
- Aymeric (Congregation) -> Lucia -> Tataru -> Lucia
- Next: Breaking the Cycle

**Breaking the Cycle** — giver: Alphinaud (Foundation) `[COND: relay]`
- Falcon's Nest -> Tailfeather -> rendezvous with Lucia outside Tailfeather -> Vidofnir (Anyx Trine) -> Alphinaud
- Next: Another Time, Another Place

**Another Time, Another Place** — giver: Alphinaud (the Dravanian Forelands)
- rendezvous with Y'shtola (Idyllshire) -> wait with Alphinaud & Y'shtola -> Krile (outside Matoya's Cave)
- Next: In the Eye of the Beholder

**In the Eye of the Beholder** — giver: Krile (the Dravanian Hinterlands) `[COND: parallel → As Goes Light, So Goes Darkness]`
- enter Matoya's Cave -> Alphinaud (outside Tailfeather) -> show Alphinaud's sketch to Marcechamp / Loupard / Grimold -> Krile -> wait with Krile in the Smoldering Wastes
- Next: A Little Slow, a Little Late

**A Little Slow, a Little Late** — giver: Alphinaud (the Dravanian Forelands) `[COND: fetch]`
- the Vath storyteller -> Loth ast Gnath (defeat foes en route) -> wait for your comrades -> Thancred
- Next: Dreams of the Lost

**Dreams of the Lost** — giver: Alphinaud (the Dravanian Forelands) `[COND: relay]`
- Vidofnir (Anyx Trine) -> Alphinaud (Foundation) -> Lucia
- Next: Against the Dying of the Light

**Against the Dying of the Light** — giver: Lucia (Congregation, Foundation) `[COND: relay]`
- Emmanellain (the Jeweled Crozier) -> question the Ishgardians in the Hoplon (x3) -> rendezvous with Thancred -> Alphinaud (the Brume) -> Lucia
- Next: As Goes Light, So Goes Darkness

**As Goes Light, So Goes Darkness** — giver: Lucia (Foundation)
- rendezvous with Aymeric (the Pillars) -> Aymeric -> [Solo Duty] rescue the hostages (0/6) -> Alphinaud -> Alphinaud (Fortemps Manor)
- Next: As It Once Was
- Manifest tie (08.1 HW L12 3.1): the WARRIORS OF DARKNESS thread opens (strangers from another world) — gated origin (the First, ShB).

---

## PATCH 3.2 — The Gears of Change

**As It Once Was** — giver: Tataru (the Pillars) `[COND: parallel → The Word of the Mother]`
- rendezvous with F'lhaminn (Limsa Lominsa) -> F'lhaminn (Revenant's Toll) -> the Scions in the Rising Stones (0/5) -> Tataru
- Next: The Word of the Mother

**The Word of the Mother** — giver: Alphinaud (the Rising Stones)
- rendezvous with Krile (Idyllshire) -> Matoya -> [DUNGEON: The Antitower] -> Alphinaud
- Next: This War of Ours
- Manifest tie (08.1 HW L12 3.2): MINFILIA merged with Hydaelyn in the aetherial sea; THE COSMOLOGY IS REVEALED (Zodiark & Hydaelyn, the world split into THIRTEEN reflections, the Ascians' Rejoining); MINFILIA SACRIFICES herself (the Word of the Mother). Defer only the deepest truths (Venat=Hydaelyn ShB; Final Days/Meteion EW).

**This War of Ours** — giver: Alphinaud (Matoya's Cave) `[COND: relay]`
- Aymeric (Congregation) -> Lucia (Falcon's Nest)
- Next: Staunch Conviction

**Staunch Conviction** — giver: Lucia (Coerthas Western Highlands) `[COND: parallel → Choices]`
- the people of Falcon's Nest (0/3) -> Artoirel
- Next: Once More, a Favor

**Once More, a Favor** — giver: Emmanellain (Coerthas Western Highlands) `[COND: fetch]`
- stand watch for wolves outside Falcon's Nest (0/2) -> Emmanellain -> search for Thancred -> Emmanellain
- Next: For Those We Have Lost

**For Those We Have Lost** — giver: Emmanellain (Coerthas Western Highlands) `[COND: parallel → Choices]`
- Thancred -> the people of Falcon's Nest (0/3) -> Thancred
- Next: Consequences

**Consequences** — giver: Thancred (Coerthas Western Highlands) `[COND: relay]`
- Lucia -> search for Honoroit -> Thancred
- Next: Choices

**Choices** — giver: Thancred (Coerthas Western Highlands)
- Aymeric (Congregation) -> Thancred -> Lucia -> deliver the letter to Hilda -> search for Emmanellain (the Pillars) -> Aymeric (Congregation) -> Thancred
- Next: A Spectacle for the Ages

**A Spectacle for the Ages** — giver: Lucia (Foundation)
- Emmanellain (outside the Gates of Judgement) -> Emmanellain again (receive House Fortemps colors) -> [Solo Duty] the grand melee: defeat alliance forces + reach 100 Tactical Points -> defeat Raubahn one-on-one -> Emmanellain -> Raubahn -> Thancred
- Next: For Those We Can Yet Save

**For Those We Can Yet Save** — giver: Ser Aymeric (Coerthas Central Highlands) `[COND: relay]`
- Alphinaud -> Artoirel (Falcon's Nest) -> Alphinaud
- Next: Causes and Costs

**Causes and Costs** — giver: Alphinaud (Coerthas Western Highlands) `[COND: relay]`
- wait for Alphinaud in the intercessory (Camp Dragonhead) -> Alphinaud -> Alphinaud (outside Fortemps Manor)
- Next: The Man Within (3.3)
- Manifest tie (08.1 HW L12 3.2): around the 3.2->3.3 seam the Falcon's Nest peace conference is shattered when ESTINIEN, POSSESSED by NIDHOGG (via the two eyes), lances Vidofnir — the 'final chorus' begins. Confirm the exact beat placement at play.

---

---

## PATCH 3.3 — Revenge of the Horde

**The Man Within** — giver: House Fortemps Knight (the Pillars) `[COND: relay]`
- Alphinaud (Fortemps Manor) -> Krile (the Forgotten Knight) -> Alphinaud (Congregation)
- Next: An Ally for Ishgard

**An Ally for Ishgard** — giver: Alphinaud (Foundation) `[COND: relay]`
- Ser Aymeric -> Vidofnir (Anyx Trine)
- Next: Winning Over the Wyrm

**Winning Over the Wyrm** — giver: Alphinaud (the Dravanian Forelands)
- Aymeric (outside Moghome) -> blow the horn atop Zenith -> Aymeric -> the imperious wyvern -> [DUNGEON: Sohr Khai] -> Alphinaud
- Next: An End to the Song
- Manifest tie (08.1 HW L12 3.3): HRAESVELGR entrusts ONE of his own EYES to the party.

**An End to the Song** — giver: Aymeric (the Churning Mists)
- [TRIAL: The Final Steps of Faith = NIDHOGG] confront Nidhogg's shade -> Alphinaud
- Next: Heroes of the Hour
- Manifest tie (08.1 HW L12 3.3): the party defeats Nidhogg's shade; with Alphinaud (aided by the spirits of Haurchefant & Ysayle) they wrest Nidhogg's two eyes from Estinien's armour and cast them into the abyss; ESTINIEN IS FREED AND SURVIVES. [This trial is PATCH 3.3.]

**Heroes of the Hour** — giver: Alphinaud (Foundation) `[COND: relay]`
- Lucia -> enter Fortemps Manor -> inquire after Alphinaud (Congregation)
- Next: Litany of Peace

**Litany of Peace** — giver: Ser Aymeric (Ishgard - the Pillars)
- Aymeric -> Aymeric (infirmary) -> Alphinaud (Fortemps Manor)
- Next: Promises Kept (3.4)

---

## PATCH 3.4 — Soul Surrender

**Promises Kept** — giver: House Fortemps Knight (the Pillars) `[COND: relay]`
- the House Borel steward -> return to Fortemps Manor -> Alphinaud
- Next: Shadows of the First

**Shadows of the First** — giver: Alphinaud (Fortemps Manor)
- Alphinaud (Camp Dragonhead) -> the steadfast knight -> [DUNGEON: Xelphatol] -> Alphinaud
- Next: Two Sides of a Coin
- Manifest tie: Xelphatol (Ixal stronghold), patch 3.4.

**Two Sides of a Coin** — giver: Alphinaud (Coerthas Central Highlands) `[COND: relay]`
- Aymeric (Congregation) -> Alphinaud -> Urianger (the Waking Sands) -> Bloeidin (Camp Overlook, outer La Noscea)
- Next: Unlikely Allies

**Unlikely Allies** — giver: Commander Bloeidin (Camp Overlook, Outer La Noscea) `[COND: fetch]`
- Alphinaud -> search for the koboldling (Camp Overlook) -> pursue the koboldling (x3) -> Alphinaud
- Next: The Beast That Mourned at the Heart of the Mountain

**The Beast That Mourned at the Heart of the Mountain** — giver: Ga Bu (Outer La Noscea)
- Ga Bu -> secure the caches of crystals in U'Ghamaro (x3) -> give the crystals to Alphinaud -> follow Ga Bu & Alisaie -> Alphinaud -> [TRIAL: The Navel (Hard) = TITAN] -> Alphinaud (Camp Overlook)
- Next: Beneath a Star-filled Sky

**Beneath a Star-filled Sky** — giver: Alphinaud (Outer La Noscea) `[COND: relay]`
- Bloeidin -> Alphinaud -> search for Alisaie -> return to the Waking Sands -> Alphinaud -> Alisaie (Little Ala Mhigo)
- Next: When We Were Free

**When We Were Free** — giver: Alphinaud (Southern Thanalan) `[COND: parallel → One Life for One World]`
- question the residents of Little Ala Mhigo (0/3: Otelin, Sifrid, Talebot) -> Alphinaud -> Gundobald -> rendezvous with Alphinaud (the Sunken Temple of Qarn) -> Alphinaud
- Next: Honorable Heroes

**Honorable Heroes** — giver: Papalymo (Southern Thanalan) `[COND: fetch]`
- deliver the sack of gil to Talebot -> Alphinaud -> (in weathered tunic/slops) Alphinaud -> Alphinaud
- Next: One Life for One World

**One Life for One World** — giver: Alphinaud (Southern Thanalan)
- Alisaie -> Alphinaud (x2) -> [Solo Duty in the Bowl of Embers: defeat the WARRIORS OF DARKNESS] -> aether-channel the Blade of Light x3 to power Alisaie's blade -> post-duty cutscenes
- Next: An Ending to Mark a New Beginning
- Manifest tie (08.1 HW L12 3.1-3.4): the Warriors of Darkness thread — gated origin (they are from the First, ShB).

**An Ending to Mark a New Beginning** — giver: Alphinaud (the Rising Stones, Southern Thanalan) `[COND: relay]`
- Alisaie -> Papalymo -> Alphinaud (Rising Stones) -> Alphinaud
- Next: Tidings from Gyr Abania (3.5)

---

---

## PATCH 3.5 — The Far Edge of Fate (part 1)

**Tidings from Gyr Abania** — giver: Tataru (the Rising Stones) `[COND: relay]`
- Tataru (the Diamond Forge, Rowena's House of Splendors) -> wait for Tataru -> attend the meeting at the Rising Stones -> Lucia (Congregation)
- Next: An Envoy for Ishgard

**An Envoy for Ishgard** — giver: Lucia (Foundation) `[COND: relay]`
- wait at the Gates of Judgement -> Ser Aymeric (Camp Dragonhead) -> Ser Aymeric (New Gridania)
- Next: An Allied Decision

**An Allied Decision** — giver: Aymeric (New Gridania) `[COND: relay]`
- the silent conjurer (Nophica's Altar) -> Alphinaud -> Alisaie (Revenant's Toll)
- Next: Griffin, Griffin on the Wall

**Griffin, Griffin on the Wall** — giver: Alisaie (Mor Dhona)
- enter the Rising Stones -> Alphinaud -> Alphinaud (near the Hawthorne Hut) -> the serpent scout (Amarissaix's Spire) -> Alphinaud -> [DUNGEON: Baelsar's Wall] climb the wall -> Yda
- Next: Louisoix's Finest Student
- Manifest tie (08.1 HW L12 3.5): ILBERD, revealed as THE GRIFFIN, at Baelsar's Wall — the plot that leads to summoning SHINRYU with Nidhogg's eyes (climax lands at the 3.56/SB seam).

**Louisoix's Finest Student** — giver: Alphinaud (East Shroud) `[COND: relay]`
- Alisaie (the Rising Stones)
- Next: The Obvious Solution (3.56)

---

## PATCH 3.56 — The Far Edge of Fate (part 2) — bridge to Stormblood

**The Obvious Solution** — giver: Alisaie (the Rising Stones) `[COND: relay]`
- the silent conjurer (Nophica's Altar) -> Alphinaud
- Next: The Greater Obeisance

**The Greater Obeisance** — giver: Alphinaud (Nophica's Altar) `[COND: relay]`
- Cid (Gridania airship landing) -> Hida (Gridania airship landing) -> Cid (Mor Dhona) -> Nero (the Rising Stones)
- Next: Fly Free, My Pretty

**Fly Free, My Pretty** — giver: Yda (the Rising Stones)
- Cid (Mor Dhona) -> defeat Grynewaht -> defeat imperial forces -> defeat imperial soldiers with the Red Baron -> defeat Grynewaht -> Cid -> Cid (Omega Control) -> Cid (Gridania airship landing)
- Next: The Far Edge of Fate

**The Far Edge of Fate** — giver: Alphinaud (New Gridania)
- Kan-E-Senna (the Lotus Stand) -> Alphinaud -> Y'shtola (Amarissaix's Spire) -> Alisaie (the Rising Stones)
- Next: Beyond the Great Wall (STORMBLOOD 4.0 opening)
- Manifest tie (08.1 HW->SB seam): at the 3.5/3.56 climax ILBERD sacrifices his own Ala Mhigan followers and himself, using NIDHOGG'S EYES to summon the primal SHINRYU; PAPALYMO casts Louisoix's binding spell to SEAL Shinryu and DIES. The solo duty 'Five Minutes of Fate' sits INSIDE this quest — The Far Edge of Fate, patch 3.56 [GE-verified] — NOT early SB.

---

> **END OF HEAVENSWARD** (base 3.0 quests 1-94 + patches 3.1-3.56, CGW-verified across installments 1-8).

# 08.4 — ORDERED MSQ INDEX (AUTHORITATIVE DATA) — STORMBLOOD (4.0 -> 4.56)

(convenzioni: vedi 08.0)

**SCOPE:** the HW->SB seam + the Ala Mhigan Resistance at Rhalgr's Reach -> the first ZENOS duel (Reach attacked) -> regroup + sail East -> Kugane -> THE SIRENSONG SEA (L60-61).
**SEAM FROM HW:** 3.56 The Far Edge of Fate -> **Beyond the Great Wall** = first SB beat.

**EXTRACTION-ANOMALY NOTE (binding):** several CGW pages exposed a `Next` that DISAGREES with the clean CGW ordered index (surfacing a side/unlock link or a reversed pointer). Where they conflict, ORDER FOLLOWS THE INDEX; the page value is flagged for play-time check.

---

**Beyond the Great Wall** — giver: Alphinaud (the Rising Stones) `[COND: relay]`
- Alphinaud -> Alphinaud (Amarissaix's Spire) -> the serpent officer -> Raubahn
- Next: Lyse Takes the Lead

**Lyse Takes the Lead** — giver: Lyse (the Fringes)
- follow Lyse -> enter Rhalgr's Reach -> Conrad
- Next: The Promise of a New Beginning

**The Promise of a New Beginning** — giver: Conrad Kemp (Rhalgr's Reach) `[COND: relay]`
- Conrad
- Next: A Haven for the Bold

**A Haven for the Bold** — giver: Alphinaud (Rhalgr's Reach) `[COND: parallel → Best Served with Cold Steel]`
- Lyse (x5 — tour of the Reach)
- Next: A Bargain Struck

**A Bargain Struck** — giver: Alisaie (Rhalgr's Reach) `[COND: relay]`
- Conrad -> Alisaie
- Next: A Friend of a Friend in Need

**A Friend of a Friend in Need** — giver: M'naago (Rhalgr's Reach) `[COND: fetch]`
- M'naago -> M'naago (the Fringes) -> lie in wait for imperial soldiers -> M'naago
- Next: Signed, Sealed, to Be Delivered

**Signed, Sealed, to Be Delivered** — giver: M'naago (the Fringes) `[COND: relay]`
- follow M'naago -> Raubahn
- Next: Best Served with Cold Steel

**Best Served with Cold Steel** — giver: Raubahn (the Fringes)
- lie in wait for imperial soldiers -> rendezvous with Raubahn -> defeat the imperial forces -> M'naago
- Next: Let Fill Your Hearts with Pride

**Let Fill Your Hearts with Pride** — giver: M'naago (Rhalgr's Reach) `[COND: relay]`
- M'naago
- Next: Where Men Go as One

**Where Men Go as One** — giver: Conrad (Rhalgr's Reach) `[COND: relay]`
- M'naago
- Next: Future Rust, Future Dust

**Future Rust, Future Dust** — giver: Beves (Rhalgr's Reach) `[COND: parallel → In Crimson It Began]`
- question the people of Rhalgr's Reach -> return the well-worn log to Beves
- Next: A Dash of Green

**A Dash of Green** — giver: Ahelissa (Rhalgr's Reach) `[COND: fetch]`
- Tebbe -> gather 4 Fragrant Herbs -> deliver the Reach Green to Ahelissa
- Next: Ye Wayward Brothers [both A Dash of Green and Ye Wayward Brothers converge on Token of Faith; index order used]

**Ye Wayward Brothers** — giver: Ananta Battlemaid (Rhalgr's Reach) `[COND: parallel → In Crimson It Began]`
- find the 5 missing recruits -> the Ananta Battlemaid
- Next: Token of Faith

**Token of Faith** — giver: Swarthy Resistance Fighter (Rhalgr's Reach) `[COND: fetch]`
- find the fighter's ward -> deliver the ward
- Next: Crossing the Velodyna

**Crossing the Velodyna** — giver: Alphinaud (Rhalgr's Reach) `[COND: relay]`
- Y'shtola -> Alphinaud -> Raubahn (Castrum Oriens) -> Alisaie
- Next: In Crimson It Began

**In Crimson It Began** — giver: Pipin (the Fringes)
- Pipin -> aid the Resistance + find your comrades -> [Solo Duty] confront ZENOS yae Galvus -> Raubahn
- Next: The Fires Fade
- Manifest tie (08.1 SB L13): ZENOS storms Rhalgr's Reach and crushes the party in a one-sided duel, sparing them out of contempt — establishes him as the relentless hunter/Viceroy.

**The Fires Fade** — giver: Raubahn (Ala Mhigo area / the Reach)
- aid the wounded -> bring Meffrid's charm to Conrad
- Next: Bereft of Hearth and Home

**Bereft of Hearth and Home** — giver: Pipin (Rhalgr's Reach) `[COND: fetch]`
- Orella -> search the infirmary for medical supplies -> give them to the Flame Courier
- Next: Divide and Conquer

**Divide and Conquer** — giver: Raubahn (the Reach) `[COND: relay]`
- Raubahn -> Lyse (Castrum Oriens) -> Alphinaud
- Next: Lies, Damn Lies, and Pirates

**Lies, Damn Lies, and Pirates** — giver: Alisaie (the Fringes) `[COND: relay]`
- Alphinaud (Limsa Lominsa) -> Alphinaud
- Next: Tales from the Far East

**Tales from the Far East** — giver: Alphinaud (Limsa Lominsa Upper Decks) `[COND: relay]`
- Lyse (Revenant's Toll) -> the Domans (the Rising Stones) -> Lyse (Revenant's Toll)
- Next: Not without Incident

**Not without Incident** — giver: Lyse (Mor Dhona)
- Alphinaud (ferry docks, Limsa Lominsa) -> the Kraken's Arms deckhand -> Carvallain -> [DUNGEON: The Sirensong Sea] -> Carvallain
- Next: The Man from Ul'dah

**The Man from Ul'dah** — giver: Alphinaud (Kugane)
- Hancock -> follow Hancock
- Next: Where the Streets Are Paved with Koban

**Where the Streets Are Paved with Koban** — giver: Hancock (Kugane) `[COND: relay]`
- follow Hancock (x3)
- Next: By the Grace of Lord Lolorito

**By the Grace of Lord Lolorito** — giver: Hancock (Kugane) `[COND: relay]`
- follow Hancock -> Hancock -> Alphinaud
- Next: A Good Samurai Is Hard to Find

**A Good Samurai Is Hard to Find** — giver: Alphinaud (Ruby Bazaar Offices) `[COND: parallel → It's Probably a Trap]`
- Lyse -> view Alphinaud's sketch -> hand the sketch to Karaku -> to Kotokaze -> show it to the captains on the Short Pier -> Lyse
- Next: It's Probably a Trap

**It's Probably a Trap** — giver: Lyse (Kugane)
- Gyodo -> Alphinaud (the Ruby Bazaar) -> Alisaie -> [Solo Duty] wait on the Tasogare Bridge -> defeat the imperial soldiers -> follow the curious Kojin -> Lyse
- Next: Making the Catfish Sing

**Making the Catfish Sing** — giver: Lyse (Kugane) `[COND: relay]`
- Hancock -> follow Hancock to the Sekiseigumi Barracks -> wait outside (x2) -> Lyse
- Next: Once More, to the Ruby Sea

---

**SCOPE:** the RUBY SEA — alliance with the Confederates & the Blue Kojin -> recovering the Yasakani-no-Magatama -> the trial of SUSANO -> departure for Yanxia (L63-64 band).

**SIDEQUEST-POLLUTION NOTE (confirmed excluded):** the Sui-no-Sato "Little Mermaid" chain (*A Part of Your World, The Elixir of Life, The Two Princesses, The Seaweed Is Always Greener, Up Where They Trade*) and "The Kami" appear in Next fields but are NOT MSQ — excluded.

---

**Once More, to the Ruby Sea** — giver: Gosetsu (the Ruby Bazaar) · MSQ `[COND: relay]`
- return to the Ruby Bazaar -> rendezvous with Soroban at Pier #2 -> Soroban
- Next: Open Water

**Open Water** — giver: Soroban (the Ruby Sea) · MSQ `[COND: relay]`
- follow Lyse -> Soroban -> Tansui
- Next: Boys with Boats

**Boys with Boats** — giver: Tansui (Kugane) · MSQ `[COND: relay]`
- search for Tansui -> Gosetsu -> search for Soroban
- Next: To Bend with the Wind

**To Bend with the Wind** — giver: Soroban (the Ruby Sea) · MSQ
- the proud Confederate -> Soroban (x2) -> Alisaie -> follow Alisaie -> defeat the gyuki -> search for Lyse -> follow Lyse
- Next: Confederate Consternation

**Confederate Consternation** — giver: Alisaie (the Ruby Sea) · MSQ `[COND: parallel → Under the Sea]`
- look for a familiar face on Onokoro -> Rasho -> Lyse -> gather information around Onokoro -> Alisaie
- Next: The Solace of the Sea

**The Solace of the Sea** — giver: Afumi (the Ruby Sea) · MSQ `[COND: fetch]`
- Aokumo -> give the medicine to the seasick Doman recruit -> Afumi
- Next: Alisaie's Stones

**Alisaie's Stones** — giver: Hirase (the Ruby Sea) · MSQ `[COND: fetch]`
- take the rotting fish -> use it to lure out aggressive sharks & slay them -> search for the industrious pirate -> rescue him -> report to Alisaie -> Rasho
- Next: Under the Sea

**Under the Sea** — giver: Rasho (the Ruby Sea) · MSQ
- search for Lyse -> join Alisaie on the Isle of Bekko -> search for the Blue Kojin village -> Alisaie
- Next: Of Kojin and Kami

**Of Kojin and Kami** — giver: Soroban (the Ruby Sea) · MSQ `[COND: fetch]`
- Bunchin -> Soroban -> slay an unkiu for its carapace -> deliver the unkiu carapace to Soroban
- Next: In Soroban We Trust

**In Soroban We Trust** — giver: Soroban (the Ruby Sea) · MSQ `[COND: relay]`
- Alisaie -> Lyse
- Next: Forever and Ever Apart
- (excluded from chain: "The Kami" = sidequest; "In Soroban We Trust" prev = Of Kojin and Kami, confirmed)

**Forever and Ever Apart** — giver: Lyse (the Ruby Sea) · MSQ `[COND: relay]`
- search for Shiosai -> Alisaie
- Next: In Darkness the Magatama Dreams

**In Darkness the Magatama Dreams** — giver: Alisaie (the Ruby Sea) · MSQ `[COND: fetch]`
- Alisaie -> use the enchanted lamp to find a shimmering object -> obtain the Yasakani-no-Magatama -> show it to Alisaie
- Next: The Whims of the Divine

**The Whims of the Divine** — giver: Alisaie (the Ruby Sea) · MSQ `[COND: fetch]`
- deliver the Yasakani-no-Magatama to Bunchin -> Alisaie
- Next: Breaking and Delivering

**Breaking and Delivering** — giver: Alisaie (the Ruby Sea) · MSQ `[COND: fetch]`
- follow Alisaie to the Isle of Zekki -> seek out & slay Red Kojin near the Dive -> slay Red Kojin elsewhere on the Isle of Zekki -> search for Lyse -> rendezvous with Alisaie -> Alisaie
- Next: The Lord of the Revel

**The Lord of the Revel** — giver: Alisaie (the Ruby Sea) · MSQ
- unlock the vault door -> [TRIAL: The Pool of Tribute] confront SUSANO -> Lyse (x2)
- Next: Tide Goes in, Imperials Go Out
- Manifest tie (08.1 SB): SUSANO, Lord of the Revel — first primal of Stormblood.

**Tide Goes in, Imperials Go Out** — giver: Alisaie (the Ruby Sea) · MSQ `[COND: parallel → A Silence in Three Parts]`
- search for villagers in need of aid (0/2) -> one of the Confederates -> report to Alisaie
- Next: A Silence in Three Parts

**A Silence in Three Parts** — giver: Gosetsu (the Ruby Sea) · MSQ
- journey to Yanxia -> Gosetsu -> follow Gosetsu
- Next: Life after Doma

---

**SCOPE:** arrival in Yanxia (Namai under occupation) -> the Doman refugees / House of the Fierce -> a second ZENOS clash -> decision to seek Lord Hien on the Azim Steppe (L64-65 band).

**EXTRACTION-NOTE:** two pages returned a noisy prev/next (*The Will to Live*, *All the Little Angels*) — order fixed by neighbours; MSQ-progress counters increase monotonically (59->65/162).

---

**Life after Doma** — giver: Gosetsu (Yanxia) · MSQ
- survey Namai from a safe distance -> the Namai Youth -> follow Gosetsu (x2)
- Next: A Glimpse of Madness

**A Glimpse of Madness** — giver: Liberation Front Guard (Yanxia) · MSQ `[COND: relay]`
- Alisaie -> your friends -> Yugiri
- Next: The Stubborn Remainder

**The Stubborn Remainder** — giver: Yugiri (the House of the Fierce) · MSQ `[COND: parallel → The Time between the Seconds]`
- follow Yugiri to Namai Village -> gather information in Namai -> Yugiri
- Next: The Ones We Leave Behind

**The Ones We Leave Behind** — giver: Yugiri (Namai) · MSQ (progress 59/162) `[COND: fetch]`
- find people in distress -> rescue Azami -> obtain yellow flowers -> bring them to Azami -> Azami -> Yugiri
- Next: A New Ruby Tithe

**A New Ruby Tithe** — giver: Yugiri (Yanxia) · MSQ `[COND: fetch]`
- hide with Lyse & Yugiri -> Yugiri -> follow Yugiri -> use the blowgun to incapacitate the imperial soldier -> blowgun the imperial soldiers -> hit the imperials with darts -> rendezvous with Yugiri -> blowgun again -> darts -> Yugiri -> follow Yugiri
- Next: The Will to Live

**The Will to Live** — giver: Yugiri (Yanxia) · MSQ `[COND: fetch]` [page prev/next noisy — order fixed by neighbours]
- stand watch for imperial patrols -> Yugiri -> steal a uniform from a sleeping soldier -> Yugiri -> (in uniform) /imperialsalute to the guards (0/2) -> Yugiri -> free the Doman villagers
- Next: Daughter of the Deep

**Daughter of the Deep** — giver: Yugiri (Yanxia) · MSQ `[COND: fetch]`
- gather up the imperial decurion -> find a suitable place -> use Yugiri's medicine on him -> gather up the imperial soldier -> find a place -> use the medicine -> search for Yugiri -> return with Yugiri to the House of the Fierce
- Next: Path of No Return

**Path of No Return** — giver: Gosetsu (the House of the Fierce) · MSQ `[COND: relay]`
- search for Yugiri -> rendezvous with Yugiri at Yuzuka Manor
- Next: The Time between the Seconds

**The Time between the Seconds** — giver: Yugiri (Yanxia) · MSQ
- search for a place to lie in wait -> Yugiri -> [Solo Duty] defeat ZENOS yae Galvus -> Alisaie
- Next: All the Little Angels
- Manifest tie: a second contemptuous ZENOS clash (the hunter keeps testing the party).

**All the Little Angels** — giver: Isse (the House of the Fierce, Doma) · MSQ (progress 65/162) `[COND: parallel → Here There Be Xaela]` [page prev/next noisy — order fixed by neighbours]
- Isse -> speak with your comrades (0/4) -> Alphinaud
- Next: Here There Be Xaela

**Here There Be Xaela** — giver: Yugiri (Yanxia) · MSQ
- follow Yugiri to Isari -> journey to the Azim Steppe -> Yugiri (x2)
- Next: The Search for Lord Hien

---

**SCOPE:** seeking Lord Hien on the AZIM STEPPE -> proving worth among the Mol/Xaela -> BARDAM'S METTLE -> the tribes (Oronir/Dotharl) toward the Naadam (L64-66).

**EXTRACTION-NOTE:** *Stars in the Dark*'s own page returned a noisy prev/next; its position is fixed by both neighbours (An Impossible Dream -> Stars in the Dark -> A Warrior's Welcome). THE NAADAM itself comes LATER (next installment).

---

**The Search for Lord Hien** — giver: Yugiri (Reunion, the Azim Steppe) · MSQ (446/992) `[COND: parallel → An Impossible Dream]`
- gather information in Reunion -> the Goro horsemaster -> (Say chat, any phrase with "Mol") search for a Mol woman -> Cirina
- Next: A Season for War

**A Season for War** — giver: Cirina (Reunion) · MSQ (447/992) `[COND: fetch]`
- slay dholes & obtain whisperroot -> deliver the whisperroot to Cirina
- Next: An Impossible Dream

**An Impossible Dream** — giver: Cirina (the Azim Steppe) · MSQ
- search for Hien -> Hien
- Next: Stars in the Dark

**Stars in the Dark** — giver: Hien (Mol Iloh) · MSQ (449/992) `[COND: relay]` [own page prev/next noisy — position fixed by neighbours]
- Hien -> Temulun -> Cirina
- Next: A Warrior's Welcome

**A Warrior's Welcome** — giver: Cirina (the Azim Steppe) · MSQ `[COND: fetch]`
- Hien -> use the entrails to lure out & slay gulo gulo -> show the meat to Gosetsu -> deliver the sack of meat to Cirina
- Next: The Heart of Nations

**The Heart of Nations** — giver: Cirina (the Azim Steppe) · MSQ `[COND: fetch]`
- Dorbei -> Lyse -> gather dung -> deliver the dung to Lyse -> Cirina -> Hien
- Next: A Trial Before the Trial

**A Trial Before the Trial** — giver: Hien (the Azim Steppe) · MSQ `[COND: relay]`
- Lyse (x2) -> survey your surroundings -> Hien -> survey again -> Hien
- Next: In the Footsteps of Bardam the Brave

**In the Footsteps of Bardam the Brave** — giver: Hien (the Azim Steppe) · MSQ
- enter [DUNGEON: Bardam's Mettle] -> Lyse
- Next: The Children of Azim
- Manifest tie (08.1 SB L13): Bardam's Mettle — the rite that wins the right to lead the Naadam.

**The Children of Azim** — giver: Lyse (the Azim Steppe) · MSQ `[COND: relay]`
- Magnai
- Next: The Labors of Magnai

**The Labors of Magnai** — giver: Baatu (the Azim Steppe) · MSQ `[COND: fetch]`
- Baatu -> the Oroniri spearson -> obtain swordgrass -> deliver the swordgrass to Baatu -> Magnai
- Next: For Love of the Moon

**For Love of the Moon** — giver: Hien (the Azim Steppe) · MSQ `[COND: fetch]`
- Udutai -> find lost lambs -> Udutai -> Hien -> Magnai
- Next: Sworn Enemies of the Sun

**Sworn Enemies of the Sun** — giver: Magnai (the Azim Steppe) · MSQ `[COND: fetch]`
- Gosetsu -> /lookout at the Dusk Throne -> save the wounded hunter -> Gosetsu
- Next: The Undying Ones

---

**SCOPE:** the DOTHARL (Sadu, the undying) -> uniting the tribes -> THE NAADAM (full-party battle for the ovoo) -> the Mol crowned, alliance won for Doma (L66).

**EXTRACTION-NOTE:** CGW's *The Naadam* page renders ONLY lore (no infobox/steps) — giver/steps/duty taken from Gamer Escape (title "Naadam"); *As the Gods Will* zone corrected via GE (CGW mis-extracted "The Lochs"; true zone = Azim Steppe, Nhaama's Retreat). Order A Final Peace -> As the Gods Will -> Naadam -> Glory to the Khagan is GE-confirmed on both ends.

---

**The Undying Ones** — giver: Gosetsu (the Azim Steppe, Dotharl Khaa) · MSQ
- Sadu -> Gosetsu -> gather information at Dotharl Khaa -> Gosetsu
- Next: A Final Peace
- Manifest tie (08.1 SB): the Dotharl believe in reincarnation — they do not mourn the dead.

**A Final Peace** — giver: Gosetsu (the Azim Steppe) · MSQ `[COND: relay]`
- Sadu -> pay your respects to Geser -> Gosetsu
- Next: As the Gods Will

**As the Gods Will** — giver: Gosetsu (the Azim Steppe, Nhaama's Retreat) · MSQ `[COND: relay]` [zone GE-corrected]
- Magnai -> Hien -> Cirina
- Next: The Naadam

**The Naadam** — giver: Cirina (the Azim Steppe, Mol Iloh) · MSQ [giver/steps/duty from Gamer Escape]
- speak with the Mol warriors (0/4) -> Temulun -> Cirina -> race to the ovoo
- [DUTY: The Naadam — FULL-PARTY battle] defeat Magnai the Older & hold back the Oronir -> defeat Sadu Heavensflame & hold back the Dothari -> claim the ovoo for the Mol -> defeat the imperial forces (Grynewaht) -> defend the stellar chuluu -> Hien
- Next: Glory to the Khagan
- Manifest tie (08.1 SB L14): THE NAADAM — the grand melee of the Steppe; winning it makes the Mol Khagan and secures Hien's Xaela alliance. Grynewaht's imperial ambush is repelled by the united tribes.

**Glory to the Khagan** — giver: Hien (the Azim Steppe) · MSQ `[COND: relay]`
- Temulun -> the diligent Mol warrior -> strike a /victorypose at the mark of Mol Iloh -> Cirina
- Next: In Crimson They Walked

---

**SCOPE:** with the Xaela alliance won, the party returns to occupied YANXIA, rallies the Doman resistance and the Confederates, and storms DOMA CASTLE (L67).

**SIDEQUEST-POLLUTION NOTE:** *In Crimson They Walked* lists two Next entries — MSQ = **The Hour of Reckoning**; *Something Fishy This Way Comes* is a sidequest (excluded).

---

**In Crimson They Walked** — giver: Hien (the Azim Steppe) · MSQ `[COND: relay]`
- Magnai -> Sadu -> Cirina
- Next: The Hour of Reckoning

**The Hour of Reckoning** — giver: Hien (the Azim Steppe) · MSQ `[COND: relay]`
- Gosetsu -> Hien -> Alphinaud
- Next: The Room Where It Happened

**The Room Where It Happened** — giver: Alphinaud (Yanxia) · MSQ `[COND: relay]`
- Hien -> Alphinaud -> Tataru in Kugane
- Next: How Tataru Got Her Groove Back

**How Tataru Got Her Groove Back** — giver: Tataru (the Ruby Bazaar Offices, Kugane) · MSQ `[COND: fetch]`
- search Kugane for the overworked porter -> deliver Cid's parcel to Tataru -> deliver the magitek field generator manual to Alphinaud in Yanxia
- Next: Seeds of Despair

**Seeds of Despair** — giver: Alphinaud (Yanxia) · MSQ `[COND: fetch]`
- Alisaie -> search for imperial patrols south of Prism Lake -> search Prism Lake for patrols -> follow Alisaie -> search the Ribbons for suspicious villagers -> defeat the imperial impostors -> rendezvous with Alisaie -> Alisaie
- Next: The Limits of Our Endurance

**The Limits of Our Endurance** — giver: Alisaie (Yanxia) · MSQ `[COND: relay]`
- Lyse -> Isse -> Tsuranuki
- Next: Broken Steel, Broken Men

**Broken Steel, Broken Men** — giver: Tsuranuki (Yanxia) · MSQ `[COND: fetch]`
- use the makeshift bombs to demolish abandoned magitek -> gather up the armor plating -> (again) demolish magitek -> gather armor plating -> deliver the armor plating to Tsuranuki
- Next: The Doma Within

**The Doma Within** — giver: Lyse (Yanxia) · MSQ
- search the House of the Fierce for people in need -> Hien -> accompany Hien to Monzen -> follow Hien -> search the ruins for usable weapons -> present the katana to Hien
- Next: On the Eve of Destiny

**On the Eve of Destiny** — giver: Hien (Yanxia) · MSQ
- Alphinaud at the House of the Fierce -> your comrades -> Alphinaud
- Next: The Die Is Cast

**The Die Is Cast** — giver: Hien (Yanxia) · MSQ
- wait in Monzen for the operation to begin -> Hien -> the Blue skiff captain -> enter [DUNGEON: Doma Castle] -> Alphinaud
- Next: The World Turned Upside Down
- Manifest tie (08.1 SB L15): DOMA CASTLE — the assault that breaks the imperial garrison and frees the Doman capital; Hien reclaims his father's seat.

---

**SCOPE:** the Qalyana beast-tribe summons LAKSHMI -> the trial of Emanation -> the Ala Mhigan front pushes through THE FRINGES & THE PEAKS toward Specula Imperatoris (L64-68 band).

**SIDEQUEST-POLLUTION NOTE:** *Delicate as a Flower* (Garima flower-errand) appears in a Next field after The Lure of the Dream but is NOT in the MSQ list — sidequest, excluded. True MSQ = The Lady of Bliss.

---

**The Lady of Bliss** — giver: Vajra (the Fringes) · MSQ
- follow Vajra to Djanan Qhat -> attune to the aetheryte at Djanan Qhat -> observe Sri Lakshmi and the Qalyana broodmother -> (Alisaie reveals herself) -> [TRIAL: Emanation] defeat SRI LAKSHMI -> the Qalyana broodmother -> report to Lyse
- Next: The Silence of the Gods
- Manifest tie (08.1 SB): LAKSHMI, the Lady of Bliss — Qalyana primal; her thrall is broken in Emanation.

**The Silence of the Gods** — giver: Sarisha (the Peaks) · MSQ `[COND: relay]`
- Sarisha -> M'naago (x2) -> Alphinaud
- Next: The First of Many

**The First of Many** — giver: Alphinaud (the Fringes) · MSQ `[COND: relay]`
- the Alliance recruit -> M'naago -> follow M'naago to Ala Ghiri
- Next: Strong and Unified

**Strong and Unified** — giver: M'naago (Ala Ghiri, the Peaks) · MSQ `[COND: relay]`
- Raubahn -> Alisaie
- Next: Hells Open

**Hells Open** — giver: Alisaie (Ala Ghiri, the Peaks) · MSQ
- patrol Wightrock for imperial forces -> rendezvous with Alisaie
- Next: Heavens Weep
- (note: Castrum Abania's main cannon destroys Specula Imperatoris in cutscene here — the Castrum is NOT yet entered)

**Heavens Weep** — giver: Alisaie (the Peaks) · MSQ `[COND: fetch]`
- follow Alisaie -> Raubahn -> search for wounded soldiers -> keep searching -> Lyse -> Alphinaud
- Next: The Road Home

**The Road Home** — giver: Alphinaud (the Peaks) · MSQ `[COND: fetch]`
- Alisaie -> search for wounded soldiers -> Alphinaud
- Next: For the Living and the Dead

**For the Living and the Dead** — giver: Alphinaud (Ala Ghiri, the Peaks) · MSQ `[COND: relay]`
- Raubahn -> Lyse
- Next: Above the Churning Waters

**Above the Churning Waters** — giver: Lyse (the Peaks) · MSQ `[COND: relay]`
- wait for Lyse at Nyunkrepf's Hope -> Lyse
- Next: The Path Forward

**The Path Forward** — giver: Lyse (the Peaks) · MSQ `[COND: relay]`
- report to Raubahn -> Alphinaud
- Next: With Tired Hands We Toil

**With Tired Hands We Toil** — giver: Alphinaud (the Peaks) · MSQ `[COND: relay]`
- stay alert on the way to Specula Imperatoris -> enter Specula Imperatoris (stay alert) -> Alphinaud -> stay alert on the way to Radiata -> Lyse
- Next: Where Courage Endures

---

**SCOPE:** the liberation of ALA MHIGO — infiltrate CASTRUM ABANIA -> rally the Alliance at the Lochs -> the Fordola & Hakuro solo duties -> storm ALA MHIGO -> the Royal Menagerie: SHINRYU merged with ZENOS (L68-70, 4.0 climax).

---

**Where Courage Endures** — giver: Lyse (Radiata, the Peaks) · MSQ `[COND: relay]`
- search for your contact in Radiata -> meet the contact outside Radiata
- Next: The Price of Freedom

**The Price of Freedom** — giver: Alphinaud (the Peaks) · MSQ
- search for imperial patrols between Radiata and Castrum Abania (x2) -> Stark Woad -> lie in wait for imperial soldiers -> stand watch for remaining soldiers -> enter [DUNGEON: Castrum Abania] -> Lyse
- Next: Raubahn's Invitation
- Manifest tie (08.1 SB L16): CASTRUM ABANIA — the imperial fortress guarding the road to Ala Mhigo.

**Raubahn's Invitation** — giver: Raubahn (Gyr Abania) · MSQ `[COND: relay]`
- follow Raubahn to Coldhearth
- Next: Liberty or Death

**Liberty or Death** — giver: Raubahn (the Peaks) · MSQ `[COND: relay]`
- Raubahn -> Lyse -> follow Lyse -> look out for suspicious individuals on the way to Radiata -> rendezvous with Lyse -> M'naago
- Next: The Lady in Red

**The Lady in Red** — giver: Lyse (Rhalgr's Reach) · MSQ `[COND: relay]`
- Orella at Rhalgr's Reach -> wait for Lyse -> Lyse
- Next: Upon the Great Loch's Shore

**Upon the Great Loch's Shore** — giver: Lyse (Rhalgr's Reach) · MSQ `[COND: relay]`
- Alphinaud -> Pipin at Castrum Abania -> journey to the Lochs -> Alphinaud
- Next: The Key to Victory

**The Key to Victory** — giver: Alphinaud (the Lochs) · MSQ
- Lyse -> head for the Saltery -> search the Saltery for clues -> [SOLO DUTY] survive the imperial ambush -> head for Sali Monastery -> Lyse
- Next: The Resonant

**The Resonant** — giver: Lyse (the Lochs) · MSQ
- follow Lyse -> Lyse in Loch Seld -> follow Lyse -> Lyse -> open the gates of the Ala Mhigan Quarter -> head to the Resonatorium -> [SOLO DUTY] defeat FORDOLA rem Lupis (two-part battle) -> Alphinaud
- Next: The Legacy of Our Fathers
- Manifest tie (08.1 SB): Fordola, the Butcher — her Resonant sight; defeated at the Resonatorium (NOT the Ala Mhigo dungeon).

**The Legacy of Our Fathers** — giver: Alphinaud (the Lochs) · MSQ
- Arenvald -> Raubahn -> Alphinaud -> Kan-E-Senna -> Merlwyb -> Aymeric -> Raubahn
- Next: The Measure of His Reach
- (the Eorzean Alliance leaders gather for the final assault)

**The Measure of His Reach** — giver: Raubahn (the Lochs) · MSQ
- deliver Raubahn's package to Pipin -> follow Alphinaud -> [SOLO DUTY] defeat five wolfmen, then HAKURO Whitefang -> report to Pipin
- Next: Stormblood

**Stormblood** (4.0 FINALE quest) — giver: Pipin (the Lochs) · MSQ
- enter [DUNGEON: Ala Mhigo] -> [TRIAL: The Royal Menagerie] confront SHINRYU -> Lyse -> Alphinaud -> M'naago -> Raubahn -> Yugiri -> Lyse -> Lyse in Rhalgr's Reach
- FINAL BOSS: ZENOS yae Galvus, merged with SHINRYU in the Royal Menagerie.
- Manifest tie (08.1 SB L17): ALA MHIGO liberated; Zenos summons/binds Shinryu and is defeated; Lyse leads a free Ala Mhigo. End of 4.0.
- Next: (Patch 4.1) The Ala Mhigan homecoming arc — see INSTALLMENT 17.

---

**SCOPE:** 4.1 (The Legend Returns) — the settlement of liberated Ala Mhigo, Fordola's Echo, Nanamo's incognito visit; 4.2 (Rise of a New Sun) — the rebuilding of the Doman Enclave and the arrival of the imperial emissary Asahi.

**SIDEQUEST NOTE:** the optional trial series Byakko (The Jade Stoa, 4.2) is NOT MSQ — excluded.

---

## PATCH 4.1 — The Legend Returns

**Arenvald's Adventure** — giver: Arenvald (Rhalgr's Reach) · MSQ `[COND: relay]`
- Arenvald -> wait on the eastern side of Starfall
- Next: The Darkness Below

**The Darkness Below** — giver: Alphinaud (Rhalgr's Reach) · MSQ `[COND: parallel → The Mad King's Trove]`
- speak with residents of the Ala Mhigan Quarter (0/3) -> Ernold -> report to Arenvald
- Next: The Mad King's Trove

**The Mad King's Trove** — giver: Alphinaud (the Lochs) · MSQ
- Alphinaud on the southern shore of Loch Seld -> search the ruins on the loch floor -> investigate the passage -> enter [DUNGEON: The Drowned City of Skalla] -> Alphinaud in the Ala Mhigan Quarter
- Next: The Butcher's Blood
- Manifest tie (08.1 SB patch): THE DROWNED CITY OF SKALLA — King Manfred's sunken vault beneath Loch Seld.

**The Butcher's Blood** — giver: Arenvald (the Lochs) · MSQ `[COND: relay]`
- Lyse (x2) -> the prison guard
- Next: Echoes of an Echo

**Echoes of an Echo** — giver: Lyse (the Lochs) · MSQ
- the Resonatorium guard -> Raubahn -> gather information at the Resonatorium (0/2) -> report to Raubahn -> Lyse
- Next: A Sultana's Strings
- (Fordola's Echo awakens — parallels the Warrior of Light's gift)

**A Sultana's Strings** — giver: Alphinaud (the Lochs) · MSQ `[COND: relay]`
- Bartholomew in Ul'dah -> Nanamo outside the Quicksand -> Nanamo near Stonesthrow -> Nanamo at the Unholy Heir -> Nanamo in the Coliseum -> Nanamo
- Next: A Sultana's Duty

**A Sultana's Duty** — giver: Nanamo Ul Namo (Ul'dah - Steps of Thal) · MSQ `[COND: relay]`
- Nanamo at Arrzaneth Ossuary -> Nanamo at the airship landing -> Nanamo at the Gold Saucer -> Nanamo
- Next: A Sultana's Resolve

**A Sultana's Resolve** — giver: Nanamo Ul Namo (the Gold Saucer) · MSQ `[COND: relay]`
- Hancock in Kugane -> Nanamo in Ul'dah -> Nanamo at the Waking Sands -> Nanamo
- Next: Securing the Saltery

**Securing the Saltery** — giver: Nanamo Ul Namo (the Waking Sands) · MSQ `[COND: fetch]`
- discover the yabby's weak point (telescope) -> report to Watt -> Wiscar (observe a yabby) -> discover its weak point -> Wiscar -> observe a phoebad -> discover its weak point -> Wiscar -> report to Watt
- Next: A Blissful Arrival

**A Blissful Arrival** — giver: Alphinaud (the Lochs) · MSQ `[COND: relay]`
- wait inside the gate to the Ala Mhigan Quarter -> Raubahn -> Lyse
- Next: Return of the Bull

**Return of the Bull** — giver: Raubahn (the Lochs) · MSQ `[COND: relay]`
- join your fellow Scions in the Ala Mhigan Quarter -> the Resistance guard -> Arenvald -> Lyse -> Lyse in Rhalgr's Reach
- Next: Tidings from the East

---

## PATCH 4.2 — Rise of a New Sun

**Tidings from the East** — giver: Lyse (Rhalgr's Reach) · MSQ
- head to the Ruby Bazaar offices in Kugane -> Alisaie in Sanjo Hanamachi
- Next: The Sword in the Store

**The Sword in the Store** — giver: Alphinaud (Kugane) · MSQ `[COND: relay]`
- search for the master of Shofuku Shichiten on Kogane Dori -> Ume at the Umineko Teahouse
- Next: Hope on the Waves

**Hope on the Waves** — giver: Yugiri (Kugane) · MSQ `[COND: relay]`
- Soroban at Pier #2 -> Alphinaud (x2) -> join Alisaie -> Soroban near Isari
- Next: Elation and Trepidation

**Elation and Trepidation** — giver: Yugiri (the Ruby Sea) · MSQ `[COND: parallel → His Forgotten Home]`
- Yugiri near Namai -> ask soldiers about Jifuya (0/2) -> the Liberation Front sentry -> search for Jifuya in Yanxia -> Yugiri -> Hien
- Next: Storm on the Horizon

**Storm on the Horizon** — giver: Hien (Yanxia) · MSQ `[COND: relay]`
- Hien at Castrum Fluminis -> Hien -> Yugiri at the mercantile docks -> Hien at the Doman Enclave -> the guardsman -> Hien -> Alisaie
- Next: His Forgotten Home

**His Forgotten Home** — giver: Alisaie (the Doman Enclave) · MSQ
- Asahi -> defeat the Red Kojin
- Next: A Guilty Conscience
- (Asahi sas Brutus — the imperial emissary, Yotsuyu's adoptive brother — arrives under a flag of truce)

**A Guilty Conscience** — giver: Asahi (Yanxia) · MSQ `[COND: relay]`
- Yugiri -> Hien
- Next: Rise of a New Sun

**Rise of a New Sun** — giver: Hien (the Kienkan, Doman Enclave) · MSQ `[COND: relay]`
- Hien (x2) -> Hancock at the Ruby Bazaar in Kugane
- Next: Gosetsu and Tsuyu

---

**SCOPE:** 4.3 (Under the Moonlight) — the hunt for a memory-less Yotsuyu and the trial of TSUKUYOMI; 4.4 (Prelude in Violet) — the Empire's succession crisis, THE BURN, and Y'shtola's search on the Steppe.

---

## PATCH 4.3 — Under the Moonlight

**Gosetsu and Tsuyu** — giver: Alphinaud (the Ruby Bazaar Offices, Kugane) · MSQ `[COND: relay]`
- Hien at the Kienkan -> Alphinaud
- Next: Gone Like the Morning Dew

**Gone Like the Morning Dew** — giver: Hien (the Doman Enclave) · MSQ `[COND: fetch]`
- question the residents of Yuzuka Manor (0/2) -> search for signs of Yotsuyu (x3) -> inspect the bamboo hat
- Next: Fruits of Her Labor

**Fruits of Her Labor** — giver: Hien (Yanxia) · MSQ `[COND: relay]`
- Hien -> Hien at the Kienkan -> Hien
- Next: Conscripts and Contingencies

**Conscripts and Contingencies** — giver: Hien (the Kienkan) · MSQ `[COND: fetch]`
- Rasho on Onokoro -> inspect the hull (0/2) -> report to Ihanashi -> Hien at the Kienkan
- Next: The Primary Agreement

**The Primary Agreement** — giver: Hien (the Kienkan) · MSQ
- the Confederate skipper in the Glittering Basin -> [TRIAL: Castrum Fluminis] confront TSUKUYOMI -> Hien -> Hien at the Doman Enclave -> Hien in the Kienkan
- Next: Under the Moonlight
- Manifest tie (08.1 SB patch): TSUKUYOMI — Yotsuyu reborn as the Dusk Mother; the Confederates & Doma end the primal at Castrum Fluminis.

**Under the Moonlight** — giver: Alisaie (the Kienkan) · MSQ `[COND: relay]`
- Lyse in Rhalgr's Reach -> Lyse at Bloodhowe -> Alisaie at the Rising Stones
- Next: Emissary of the Dawn

**Emissary of the Dawn** — giver: Alisaie (the Rising Stones) · MSQ
- claim the nearby table -> Alisaie
- [SOLO DUTY: play as Alphinaud in The Burn — rescue a fallen soldier, defeat enemy soldiers, free a restrained ally from magitek airships]
- Next: Sisterly Act
- (the great recap/bridge quest — the imperial withdrawal and the road ahead)

---

## PATCH 4.4 — Prelude in Violet

**Sisterly Act** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- Thancred in the Ala Mhigan Quarter -> Alisaie -> Y'shtola in the Doman Enclave -> Hien at the Kienkan
- Next: Feel the Burn

**Feel the Burn** — giver: Hien (the Kienkan) · MSQ
- Hien near the House of the Fierce -> enter [DUNGEON: The Burn] -> Hien in the Doman Enclave
- Next: Shadows in the Empire
- Manifest tie (08.1 SB patch): THE BURN — the aetherially-scarred waste between Othard and Ilsabard.

**Shadows in the Empire** — giver: Hien (the Doman Enclave) · MSQ `[COND: relay]`
- enter the Kienkan -> Hien -> Lyse in the Doman Enclave -> Hien at the Kienkan
- Next: A Power in Slumber
- (Garlemald's succession turmoil after Zenos — Varis, the Populares)

**A Power in Slumber** — giver: Hien (the Kienkan) · MSQ `[COND: relay]`
- Hien in Kienkan -> travel to the Azim Steppe & meet Y'shtola at Reunion -> Y'shtola at her favorite spot -> travel to Mol Iloh -> Hien in Mol Iloh -> Cirina in Mol Iloh
- Next: The Will of the Moon

**The Will of the Moon** — giver: Y'shtola (the Azim Steppe) · MSQ `[COND: relay]`
- Y'shtola at the House of the Crooked Coin -> Cirina at Mol Iloh -> Sadu at Dotharl Khaa -> wait at the designated location -> report to Cirina at Mol Iloh
- Next: The Call

**The Call** — giver: Y'shtola (the Azim Steppe) · MSQ `[COND: relay]`
- Y'shtola at the House of the Crooked Coin -> Hien -> Alisaie at the Kienkan -> Thancred in the Ala Mhigan Quarter -> the Resistance guard -> Alisaie
- Next: Prelude in Violet

**Prelude in Violet** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- Alisaie at the Rising Stones -> Alisaie at Maelstrom Command -> Alisaie -> Alisaie at the Rising Stones
- Next: Soul Searching

---

**SCOPE:** the war with Garlemald comes to a head — THE GHIMLYT DARK — then the Scions vanish and the WARRIOR faces a returned ZENOS one last time before being called to THE FIRST. This is the direct bridge into SHADOWBRINGERS.

**SIDEQUEST NOTE:** the optional trial Seiryu (The Wreath of Snakes, 4.4) is NOT MSQ; the MSQ quest *Seiryu's Wall* below only references it — no trial inside.

---

## PATCH 4.5 — A Requiem for Heroes (Part 1)

**Soul Searching** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- Alisaie in front of Matoya's Cave -> Alisaie
- Next: A Defector's Tidings

**A Defector's Tidings** — giver: Alisaie (the Dravanian Hinterlands) · MSQ
- the Resistance guard in the Ala Mhigan Quarter -> Alisaie -> Hien
- Next: Seiryu's Wall
- (Maxima of the Populares defects with a proposal of peace)

**Seiryu's Wall** — giver: Hien (the Kienkan) · MSQ `[COND: relay]` [no trial inside — see sidequest note]
- Hien near the House of the Fierce -> Hien at the Kienkan
- Next: Parley on the Front Lines

**Parley on the Front Lines** — giver: Hien (the Kienkan) · MSQ `[COND: parallel → The Face of War]`
- the Resistance fighter in Porta Praetoria -> Lyse -> Alisaie -> speak with Alliance leaders (0/3) -> report to Alisaie -> Lyse
- Next: The Face of War

**The Face of War** — giver: Lyse (Eorzean Alliance Headquarters) · MSQ
- enter [DUNGEON: The Ghimlyt Dark] -> Raubahn -> Hoary Boulder at the Rising Stones
- Next: A Brief Reprieve
- Manifest tie (08.1 SB patch): THE GHIMLYT DARK — the contested gateway to Garlemald; the war stalls into deadlock.

---

## PATCH 4.56 — A Requiem for Heroes (Part 2)

**A Brief Reprieve** — giver: Hoary Boulder (the Rising Stones) · MSQ `[COND: relay]`
- Maxima in north Silvertear -> Cid
- Next: A Requiem for Heroes

**A Requiem for Heroes** (STORMBLOOD conclusion) — giver: Resistance Fighter (the Lochs) · MSQ
- [SOLO DUTY — two parts: Part 1 fight as Hien alongside Lyse & Yugiri; Part 2 fight as YOUR character against ZENOS yae Galvus (Ascian-possessed)] -> Raubahn -> return to the Rising Stones -> Tataru
- Manifest tie (08.1 SB patch): the final ZENOS duel — the Ascian (Elidibus in Zenos's body) is driven off; soon after, Alphinaud, Alisaie, Thancred, Urianger and Y'shtola fall comatose — their souls summoned to THE FIRST. The Warrior of Light answers the call.
- Next: (SHADOWBRINGERS 5.0) — see the ShB index. First quest: **Ⅰ. The Syrcus Trench** (the Crystal Exarch's summons).

---

# 08.5 — ORDERED MSQ INDEX (AUTHORITATIVE DATA) — SHADOWBRINGERS (5.0 -> 5.55)

(convenzioni: vedi 08.0)

---

**The Syrcus Trench** — giver: Tataru (the Rising Stones) · MSQ
- the Saint Coinach ferryman in north Silvertear -> Tataru -> head to the Crystarium -> the Crystal Exarch
- Next: City of the First

**City of the First** — giver: the Crystal Exarch (the Crystarium) · MSQ `[COND: parallel → Open Arms, Closed Gate]`
- attune to the aetheryte in the Crystarium -> Katliss in the Crystalline Mean -> Moren in the Cabinet of Curiosity -> Bragi at Musica Universalis -> find the Crystal Exarch near the Exedra
- Next: Travelers of Norvrandt

**Travelers of Norvrandt** — giver: the Crystal Exarch (the Crystarium, Lakeland) · MSQ `[COND: relay]`
- the Crystarium gatekeep -> Crystal Exarch (x3) -> the manager of suites in the Pendants -> Crystal Exarch in the Ocular
- Next: In Search of Alphinaud

**In Search of Alphinaud** — giver: the Crystal Exarch (the Ocular) · MSQ `[COND: relay]`
- present the letter of introduction to Szem Djenmai at Temenos Rookery -> the aspiring amaro tamer -> Szem Djenmai
- Next: A Still Tide

**A Still Tide** — giver: Szem Djenmai (Kholusia) · MSQ `[COND: fetch]`
- deliver the lake thyme to Eybor -> wait for Alphinaud -> search the field for vermin -> knock on the barred door (x3) -> Theva
- Next: Open Arms, Closed Gate

**Open Arms, Closed Gate** — giver: Alphinaud (Kholusia) · MSQ
- Alphinaud -> search for the source of the scream -> rescue the manic madame -> aid her -> survey the scene -> Alphinaud -> have a look around Gatetown (0/3) -> Alphinaud
- Next: A Fickle Existence

**A Fickle Existence** — giver: Alphinaud (Kholusia, Wright) · MSQ `[COND: relay]`
- Mosha-Moa -> search for the Mystel -> locate the blue-haired Mystel youth -> the blue-haired Mystel -> rescue the weakened wretch -> Alphinaud -> Tristol
- Next: City of Final Pleasures

**City of Final Pleasures** — giver: Alphinaud (the First) · MSQ
- wait at the designated location -> the red jongleur -> the immigration officer -> present registration papers -> scrub yourself in the Delousery showers -> apply the perfume -> Alphinaud -> Cornenne -> Dulia-Chai
- Next: Free to Sightsee
- (entry into EULMORE, the city of final pleasures under Vauthry)

**Free to Sightsee** — giver: Alphinaud (Eulmore) · MSQ `[COND: parallel → A Desert Crossing]`
- gather information in the Canopy -> search for the ardent attendant -> the amiable maiden
- Next: A Taste of Honey

**A Taste of Honey** — giver: the Amiable Maiden (Eulmore) · MSQ `[COND: fetch]`
- Tista-Bie -> win a game against Tista-Bie (x2) -> Atharn -> /dance on the mark on stage -> Atharn -> Dulia-Chai
- Next: A Blessed Instrument

**A Blessed Instrument** — giver: Alphinaud (the Crystarium) · MSQ `[COND: fetch]`
- gather information in the Understory -> deliver the list of the singer's symptoms and the chunk of meol to Thoarich in the Derelicts -> the weeping warbler -> report to Alphinaud
- Next: Emergent Splendor

**Emergent Splendor** — giver: Alphinaud (Kholusia) · MSQ `[COND: relay]`
- Chadden -> Alphinaud -> Alphinaud on Cracked Shell Beach -> Alphinaud in the Ocular
- Next: In Search of Alisaie

**In Search of Alisaie** — giver: the Crystal Exarch (the Ocular) · MSQ `[COND: relay]`
- deliver the sealed missive to Cassard at the Amaro Launch -> Cassard (x3) -> admire the view -> Cassard
- Next: City of the Mord

**City of the Mord** — giver: Cassard (Amh Araeng) · MSQ `[COND: parallel → A Desert Crossing]`
- Rhon Ron (browse the wares) -> browse Rhon Ron's wares (0/4) -> Ghen Gen
- Next: Working Off the Meal

**Working Off the Meal** — giver: Cassard (Amh Araeng) · MSQ `[COND: fetch]`
- use the market receipt to collect Cassard's purchases (0/3) -> deliver the Mord Souq merchandise to Cassard
- Next: A Desert Crossing

**A Desert Crossing** — giver: Tesleen (Amh Araeng) · MSQ
- Tesleen -> defeat any coyotes that threaten Tesleen -> Tesleen -> scout ahead and slay other coyotes -> Tesleen (x2)
- Next: Following in Her Footprints

**Following in Her Footprints** — giver: Tesleen (Amh Araeng) · MSQ `[COND: fetch]`
- look for signs of Alisaie near the Derrick -> investigate the small footprints -> follow them (x2) -> investigate -> Alisaie
- Next: Culling Their Ranks

**Culling Their Ranks** — giver: Alisaie (Amh Araeng) · MSQ `[COND: fetch]`
- scout the designated locations and defeat any sin eaters (0/3) -> Alisaie -> Tesleen
- Next: A Purchase of Fruit

**A Purchase of Fruit** — giver: Tesleen (Amh Araeng) · MSQ
- tend to Pawnil -> tend to Todden -> tend to Halric -> Tesleen -> Rhon Ron -> Alisaie (x2) -> give the nectarine to Tesleen
- Next: The Time Left to Us
- (the Inn at Journey's Head / Tesleen's care for the afflicted — sets up the coming tragedy)

---

**SCOPE:** Tesleen's fall -> the first Lightwarden slain at HOLMINSTER SWITCH (night returns to Lakeland) -> the Crystarium rallies -> IL MHEG, the faerie kingdom (Feo Ul, the pixies) and DOHN MHEG (L71-73).

---

**The Time Left to Us** — giver: Tesleen (Amh Araeng) · MSQ
- Tesleen -> search for Halric (x3) -> Alisaie -> the carers (0/2) -> Halric
- Next: Tears on the Sand
- Manifest tie (08.1 ShB): Tesleen is taken by the Light and transforms into a sin eater before the party — the plague made personal.

**Tears on the Sand** — giver: Alisaie (Amh Araeng) · MSQ
- Alisaie at the Red Serai -> Alisaie -> Alisaie in the Ocular
- Next: The Lightwardens

**The Lightwardens** — giver: the Crystal Exarch (the Crystarium) · MSQ
- the Exarch -> the Exarch at the crossroads beyond the Accensor Gate -> the Exarch at the Northern Staging Point -> enter [DUNGEON: Holminster Switch] -> the Exarch
- Next: Warrior of Darkness
- Manifest tie (08.1 ShB L18): HOLMINSTER SWITCH — the Warrior slays the Lightwarden Philia; true night returns to Lakeland for the first time in a century.

**Warrior of Darkness** — giver: the Crystal Exarch (the Crystarium) · MSQ `[COND: relay]`
- Alphinaud in the Crystarium -> Bragi -> Glynard -> the manager of the suites in the Pendants
- Next: An Unwelcome Guest
- (the Warrior is hailed as the Warrior of Darkness — achievement "Between Two Worlds" here, NOT a quest)

**An Unwelcome Guest** — giver: the Manager of Suites (the Crystarium) · MSQ `[COND: fetch]`
- head to the Ocular -> Moren at the Cabinet of Curiosity -> search the shelves -> deliver the book to Moren -> Alphinaud
- Next: The Crystarium's Resolve

**The Crystarium's Resolve** — giver: the Crystal Exarch (the Crystarium) · MSQ `[COND: relay]`
- Lyna -> Katliss -> Chessamile -> drink the vial of prince's kiss before Chessamile -> Szem Djenmai
- Next: Logistics of War

**Logistics of War** — giver: Szem Djenmai (the Crystarium) · MSQ `[COND: relay]`
- Szem Djenmai -> ride the amaro to the sentry at Radisca's Round -> ride to Szeli Vantheu -> Szeli Vantheu -> Lyna
- Next: The Oracle of Light

**The Oracle of Light** — giver: Lyna (Lakeland) · MSQ
- obtain treated fodder -> feed the treated fodder to the amaro (0/4) -> Lyna -> the Crystarium scout -> Thancred
- Next: Il Mheg, the Faerie Kingdom
- (Thancred and the amnesiac Minfilia — the Oracle of Light — in Il Mheg)

**Il Mheg, the Faerie Kingdom** — giver: Thancred (Il Mheg) · MSQ
- Thancred -> search for looking grass -> deliver the looking grass to Thancred
- Next: Sul Uin's Request

**Sul Uin's Request** — giver: Sul Uin (Il Mheg) · MSQ `[COND: fetch]`
- sow everbloom seeds around Lydha Lran (0/3) -> Sul Uin
- Next: Ys Iala's Errand

**Ys Iala's Errand** — giver: Ys Iala (Il Mheg) · MSQ `[COND: fetch]`
- obtain fruit from belltrees (0/2) -> deliver the bellfruits to Ys Iala
- Next: Oul Sigun's Plea

**Oul Sigun's Plea** — giver: Oul Sigun (Il Mheg) · MSQ `[COND: fetch]`
- draw water from Longmirror Lake -> give the water to the leafmen (0/2) -> Oul Sigun
- Next: Unto the Truth

**Unto the Truth** — giver: Thancred (Il Mheg) · MSQ
- summon Feo Ul (Say: "Feo Ul") -> ("Please, Feo Ul, I need you") -> ("O loveliest of branches, please grant me your succor!") -> Thancred -> Thancred at the Bookman's Shelves
- Next: Courting Cooperation
- (the Warrior becomes Feo Ul's "adorable sapling")

**Courting Cooperation** — giver: Urianger (Il Mheg) · MSQ `[COND: fetch]`
- use the Sharlayan box to capture a weakened hawker -> deliver the boxed hawker to Urianger -> Sul Uin
- Next: The Key to the Castle

**The Key to the Castle** — giver: Sul Uin (Il Mheg) · MSQ
- investigate the Untouchable Gate -> enter [DUNGEON: Dohn Mheg] -> search for Urianger
- Next: A Visit to the Nu Mou
- Manifest tie (08.1 ShB L19): DOHN MHEG — the pixies' waterlogged palace; Urianger is recovered.

**A Visit to the Nu Mou** — giver: Urianger (Il Mheg) · MSQ `[COND: relay]`
- Urianger (x3) -> head to the destination under the effect of fae cloak -> Thancred
- Next: A Fitting Payment

**A Fitting Payment** — giver: Wyd Aenc (Il Mheg) · MSQ `[COND: fetch]`
- Marn Ose -> slay moss fungi for their legs (0/2) -> deliver the moss fungus legs to Marn Ose
- Next: Spore Sweeper

**Spore Sweeper** — giver: Ys Gyuf (Il Mheg) · MSQ `[COND: fetch]`
- remove the flamespores (0/3) -> Ys Gyuf -> remove the flamespores -> the owner of the gaze -> Ys Gyuf
- Next: The Lawless Ones

**The Lawless Ones** — giver: Wyd Lad (Il Mheg) · MSQ `[COND: fetch]`
- Minfilia -> obtain vials of invisible ink (0/3) -> Minfilia -> deliver the vials of invisible ink to Wyd Lad
- Next: The Elder's Answer

**The Elder's Answer** — giver: Wyd Lad (Il Mheg) · MSQ `[COND: fetch]`
- Wyd Aenc -> the enormous amaro -> /pet Rispa -> /pet Eo An -> /pet Nimbus -> Urianger
- Next: A Resounding Roar

**A Resounding Roar** — giver: Urianger (the Crystarium) · MSQ
- Seto (x5, defeating any sin eaters that appear)
- Next: Memento of a Friend
- (Seto, the great amaro who mourns Ardbert — the Warriors of Light of the First)

---

**SCOPE:** the Lightwarden of Il Mheg — TITANIA — falls (The Dancing Plague); the party divides; the Warrior joins Y'shtola among the NIGHT'S BLESSED in the RAK'TIKA GREATWOOD, the Viis of Fanow, and the ruins of Ronka, ending in the pyramid escape from General RAN'JIT (L74-75).

---

**Memento of a Friend** — giver: Seto (Il Mheg) · MSQ `[COND: fetch]`
- search for Seto's medallion -> deliver the medallion to Seto
- Next: Acht-la Ormh Inn

**Acht-la Ormh Inn** — giver: Seto (Il Mheg) · MSQ
- investigate the castle gate -> [TRIAL: The Dancing Plague] confront TITANIA -> Urianger
- Next: The Wheel Turns
- Manifest tie (08.1 ShB L20): TITANIA, the Lightwarden of Il Mheg (a corrupted pixie king); slain in The Dancing Plague, restoring night to Il Mheg.

**The Wheel Turns** — giver: Thancred (Il Mheg) · MSQ `[COND: relay]`
- Alisaie in the Crystarium -> Alisaie -> the manager of suites in the Pendants
- Next: A Party Soon Divided

**A Party Soon Divided** — giver: the Crystal Exarch (the Crystarium) · MSQ `[COND: relay]`
- proceed to the Ocular -> the Crystal Exarch -> Urianger at Fort Jobb
- Next: A Little Faith

**A Little Faith** — giver: Urianger (Lakeland) · MSQ `[COND: fetch]`
- survey the area -> search for the timeworn tablet -> Urianger
- Next: Into the Dark

**Into the Dark** — giver: Urianger (Lakeland) · MSQ `[COND: relay]`
- Myrcant -> Urianger -> search for Y'shtola -> Y'shtola
- Next: A Day in the Neighborhood

**A Day in the Neighborhood** — giver: Y'shtola (Slitherbough, the Rak'tika Greatwood) · MSQ
- Runar (x2) -> /kneel before Runar -> (Say: "allin tuta" to greet the residents of Slitherbough, 0/3) -> Minfilia
- Next: A Helping Hand

**A Helping Hand** — giver: Runar (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Minfilia -> take the water jug to the garden -> Minfilia -> take the water to the garden -> Ersabel
- Next: Lost but Not Forgotten

**Lost but Not Forgotten** — giver: Runar (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- look around the destination -> defeat the sin eater -> Minfilia -> search for the jade heartstone -> show it to Minfilia -> deliver the jade heartstone to Runar
- Next: Saying Good-bye

**Saying Good-bye** — giver: Runar (the Rak'tika Greatwood) · MSQ
- Minfilia -> the placid elder -> place the candle at the destination -> wait at the destination -> Y'shtola
- Next: Stirring Up Trouble

**Stirring Up Trouble** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Y'shtola -> search for the Blessed watchman -> aid him -> retrieve supplies from the outpost crates -> use a smoke bomb on the beehive -> take bees with a burlap sack -> (repeat smoke + sack) -> give the buzzing burlap sacks to Y'shtola
- Next: A Beeautiful Plan

**A Beeautiful Plan** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: relay]`
- Y'shtola -> stand at the destination and examine the murals -> Y'shtola
- Next: An Unwanted Proposal

**An Unwanted Proposal** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: relay]`
- Runar -> wait by the fire -> Urianger
- Next: Put to the Proof

**Put to the Proof** — giver: Urianger (the Rak'tika Greatwood) · MSQ `[COND: parallel → Legend of the Not-so-hidden Temple]`
- Y'shtola -> locate the first statue in the ruins of Ronka -> find the second -> find the third -> find the seal -> deliver the seal to Y'shtola
- Next: Into the Wood

**Into the Wood** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: relay]`
- Y'shtola -> survey the area -> the bow-wielding sentinel
- Next: Top of the Tree

**Top of the Tree** — giver: Cymet (the Rak'tika Greatwood, Fanow) · MSQ `[COND: parallel → Legend of the Not-so-hidden Temple]`
- Almet -> speak with the residents of Fanow to gather information (0/4) -> Almet
- Next: Look to the Stars
- (the Viis of Fanow, guardians of the Ronkan legacy)

**Look to the Stars** — giver: Almet (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Almet -> Y'shtola -> use the clay tablets on the inscriptions (0/4) -> deliver the clay tablets to Y'shtola -> Y'shtola -> Almet
- Next: Mi Casa, Toupasa

**Mi Casa, Toupasa** — giver: Almet (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Almet -> search for the owl statuette -> carry the owl statuette to its proper altar -> Almet
- Next: Legend of the Not-so-hidden Temple

**Legend of the Not-so-hidden Temple** — giver: Almet (the Rak'tika Greatwood) · MSQ
- Y'shtola -> reach the bowels of the Great Pyramid of Ux'ner -> [SOLO DUTY] avoid the Ronkan executioners -> flee from the boulders -> take a leap of faith -> defeat General RAN'JIT and his officer -> activate the final switch (Heart of Toupasa)
- Next: The Aftermath
- Manifest tie (08.1 ShB): General Ran'jit, Eulmore's old enforcer, pursues the party through the Ronkan pyramid.

**The Aftermath** — giver: Almet (the Rak'tika Greatwood) · MSQ `[COND: fetch]` [list title "Aftermath" corrected]
- Urianger -> use the antidote to treat Runar's poison -> second dose -> third dose -> Urianger
- Next: In Good Faith

---

**SCOPE:** EMET-SELCH attaches himself to the party; the Rak'tika Lightwarden falls in THE QITANA RAVEL; then the long night of AMH ARAENG (Twine, the trolley line, the mines), Ran'jit again, Minfilia becomes RYNE, and MALIKAH'S WELL (L75-77).

---

**In Good Faith** — giver: Urianger (Yx'Maja, the Rak'tika Greatwood) · MSQ
- Emet-Selch -> use the aetherial lamp to find a location that resonates with the Lifestream -> call for Emet-Selch -> Emet-Selch -> Y'shtola
- Next: The Burden of Knowledge
- Manifest tie (08.1 ShB): EMET-SELCH (the Ascian Solus/Hades) openly joins the party "to help" — the great manipulator in plain sight.

**The Burden of Knowledge** — giver: Almet (the Rak'tika Greatwood) · MSQ
- search the destination -> enter [DUNGEON: The Qitana Ravel] -> Y'shtola
- Next: Bearing with It
- Manifest tie (08.1 ShB L21): THE QITANA RAVEL — the Ronkan sanctum; the Rak'tika Lightwarden is slain, restoring night to the Greatwood.

**Bearing with It** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: relay]`
- Almet -> Runar
- Next: Out of the Wood

**Out of the Wood** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: relay]`
- Y'shtola -> wait at the entrance to Slitherbough -> Y'shtola -> the manager of suites in the Pendants
- Next: When It Rains

**When It Rains** — giver: the Manager of Suites (the Crystarium) · MSQ
- Alphinaud -> Alisaie -> activate the first anchor -> activate the second anchor -> Alphinaud -> [SOLO DUTY] defeat the sin eaters in the wood -> make for the Ostall Imperative -> drive out the sin eaters -> Alisaie
- Next: Word from On High

**Word from On High** — giver: Alisaie (Lakeland) · MSQ `[COND: parallel → The Best Way Out]`
- aid the wounded (0/3) -> Lyna
- Next: Small Favors

**Small Favors** — giver: Lyna (Lakeland) · MSQ `[COND: fetch]`
- Thancred -> Minfilia -> get Minfilia's attention with a /poke -> obtain the medicinal herbs (0/2) -> deliver the herbs to Chessamile
- Next: The Best Way Out

**The Best Way Out** — giver: Thancred (the Crystarium) · MSQ
- the Crystal Exarch in the Ocular -> Minfilia -> wait for Minfilia at Tessellation -> Thancred -> Hardyss -> Minfilia
- Next: Free Trade

**Free Trade** — giver: Thancred (Amh Araeng) · MSQ `[COND: parallel → Full Steam Ahead]`
- seek out a talkative local -> question the Mord of Garik (0/3) -> Thancred
- Next: The Trolley Problem

**The Trolley Problem** — giver: Zhun Zun (Amh Araeng) · MSQ `[COND: parallel → Full Steam Ahead]`
- Thancred (x2) -> investigate the area (0/3) -> Urianger -> confront the suspicious man -> Thancred
- Next: Rust and Ruin

**Rust and Ruin** — giver: Thaffe (Amh Araeng) · MSQ `[COND: relay]` [zone GE-corrected; CGW mis-tagged "The Lochs"]
- Thaffe (x2) -> search for Thaffe -> Thaffe (x2) -> Magnus -> Minfilia
- Next: On Track

**On Track** — giver: Minfilia (Amh Araeng, the Central Hills of Amber / Twine) · MSQ `[COND: fetch]`
- seek out a talkative resident of Twine -> open the toolbox next to Jeryk (x2) -> remove nests and slay desert vultures (0/3) -> Jeryk (x2)
- Next: Down for Maintenance

**Down for Maintenance** — giver: Jeryk (Amh Araeng) · MSQ `[COND: fetch]`
- examine the defective Talos -> slay debitage for their fragments (0/3) -> deliver the debitage fragments to Urianger
- Next: The Truth Hurts

**The Truth Hurts** — giver: Jeryk (the Hills of Amber, Amh Araeng) · MSQ `[COND: relay]`
- Thaffe -> Urianger -> search for Thancred
- Next: A Convenient Distraction

**A Convenient Distraction** — giver: Thancred (Amh Araeng) · MSQ `[COND: fetch]`
- Thancred -> Guthjon -> Thancred -> search the shadows for a Voeburt gold piece -> present it to Thancred -> deliver the Voeburt gold piece to Guthjon
- Next: A Dirty Job

**A Dirty Job** — giver: Guthjon (Amh Araeng, the mine) · MSQ `[COND: fetch]` [zone corrected; CGW mis-tagged "The Tempest"]
- obtain the smoke bombs from the nearby shack -> place the smoke bombs at the designated locations inside the mine (0/3) -> inspect the rubble and slay knockers for glittering rocks (0/7) -> deliver the glittering rocks to Guthjon
- Next: Have a Heart

**Have a Heart** — giver: Guthjon (Amh Araeng) · MSQ `[COND: fetch]`
- Magnus -> deliver the chunk of leonine to Urianger -> Urianger
- Next: Full Steam Ahead

**Full Steam Ahead** — giver: Minfilia (Amh Araeng) · MSQ
- Minfilia -> Magnus -> [SOLO DUTY] defeat RAN'JIT (at Amh Malik) -> Minfilia
- Next: Crossing Paths

**Crossing Paths** (formerly listed "Crossroads") — giver: Minfilia (Amh Araeng) · MSQ
- survey the designated location -> search for Minfilia -> search for Thancred
- Next: A Fresh Start
- Manifest tie (08.1 ShB): Thancred gives Minfilia her own name — she becomes RYNE.

**A Fresh Start** — giver: Ryne (Amh Araeng) · MSQ
- survey the designated location -> enter [DUNGEON: Malikah's Well] -> Alisaie
- Next: More than a Hunch
- Manifest tie (08.1 ShB L22): MALIKAH'S WELL — the ancient Voeburtite waterworks; step toward the Amh Araeng Lightwarden.

---

**SCOPE:** the liberation of EULMORE (Vauthry flees); the dwarves of Kholusia raise a Talos to reach MT. GULG, where the last Lightwarden — INNOCENCE — is slain in The Crown of the Immaculate (L79).

---

**More than a Hunch** — giver: Y'shtola (the Crystarium) · MSQ `[COND: relay]`
- Y'shtola -> the manager of suites in the Pendants
- Next: Return to Eulmore

**Return to Eulmore** — giver: the Manager of Suites (the Crystarium) · MSQ `[COND: parallel → A Feast of Lies]`
- head to the Ocular -> Alphinaud in Wright -> speak with people en route to Gatetown (0/3) -> Thancred
- Next: A Feast of Lies

**A Feast of Lies** — giver: Alphinaud (Eulmore) · MSQ
- Alphinaud -> [SOLO DUTY] subdue the civilians -> subdue the soldiers -> defeat the jesters -> climb to the next level -> defeat RAN'JIT -> Thancred
- Next: Paradise Fallen
- Manifest tie (08.1 ShB): Eulmore is freed; Vauthry flees to Mt. Gulg; Ran'jit falls at last.

**Paradise Fallen** — giver: Thancred (the Crystarium) · MSQ `[COND: fetch]`
- search for enthralled civilians in the Derelicts -> administer dream powder to Thoarich -> search the Understory -> dream powder to the amiable maiden -> search the Canopy -> dream powder to the free citizen -> Ryne
- Next: The Ladder

**The Ladder** — giver: Urianger (Bottom Rung, Kholusia) · MSQ `[COND: fetch]`
- Urianger -> Irvithe -> take stock of lumber -> Irvithe -> Urianger
- Next: The View from Above

**The View from Above** — giver: Urianger (the Crystarium) · MSQ `[COND: parallel → A Gigantic Undertaking]`
- wait for the work to be completed -> Alphinaud -> Alisaie -> search the area for the mysterious person -> investigate the village (0/3) -> Alphinaud
- Next: In Mt. Gulg's Shadow

**In Mt. Gulg's Shadow** — giver: Alisaie (Kholusia) · MSQ `[COND: relay]`
- Alisaie -> survey the area (x2) -> Alisaie (x2)
- Next: A Gigantic Undertaking

**A Gigantic Undertaking** — giver: Alisaie (Kholusia) · MSQ
- Chai-Nuzz -> Dulia-Chai -> Tristol
- Next: Meet the Tholls
- (the plan: build a Talos to scale Mt. Gulg — the dungeon is not yet entered)

**Meet the Tholls** — giver: Tristol (the Crystarium) · MSQ `[COND: fetch]`
- the Crystal Exarch -> Xamott -> the dwarf observer (undertake the trial) -> the dwarf observer again (the true trial) -> Xamott
- Next: A-Digging We Will Go

**A-Digging We Will Go** — giver: Xamott (Kholusia) · MSQ `[COND: fetch]`
- Korutt -> escort Korutt -> defeat the sin eaters
- Next: The Duergar's Tewel

**The Duergar's Tewel** — giver: Korutt (Kholusia) · MSQ `[COND: fetch]`
- the Crystal Exarch -> while invisible, use dream powder on Gogg Family dwarves (0/3) -> the Crystal Exarch
- Next: Rich Veins of Hope

**Rich Veins of Hope** — giver: the Crystal Exarch (Amity, Kholusia) · MSQ `[COND: parallel → Extinguishing the Last Light]`
- Xamott -> Alisaie -> deliver pickaxes to Magnus -> to Rhon Ron -> to Kai-Shirr -> Alisaie
- Next: That None Shall Ever Again

**That None Shall Ever Again** — giver: Alphinaud (Kholusia) · MSQ `[COND: fetch]` [full title confirmed]
- Y'shtola (x2) -> imbue the heartstone with magick -> Chai-Nuzz
- Next: A Breath of Respite

**A Breath of Respite** — giver: Chai-Nuzz (Kholusia) · MSQ `[COND: relay]`
- Dulia-Chai -> search for the Crystal Exarch -> the Crystal Exarch
- Next: Extinguishing the Last Light

**Extinguishing the Last Light** — giver: Chai-Nuzz (Kholusia) · MSQ
- the Crystal Exarch -> Y'shtola -> enter [DUNGEON: Mt. Gulg] -> [TRIAL: The Crown of the Immaculate] confront INNOCENCE -> Ryne
- Next: Reassuring the Masses
- Manifest tie (08.1 ShB L23): MT. GULG + INNOCENCE (Vauthry's primal form), the last Lightwarden. Its death floods the Warrior with unspent Light — the near-transformation into a Lightwarden; the true crisis of ShB begins.

---

> End SHADOWBRINGERS INSTALLMENT 24 (Eulmore -> Mt. Gulg -> Innocence, CGW-verified, full step spines, coordless). Next installment (25 — 5.0 FINALE) resumes at **Reassuring the Masses** -> the Light-sickness -> **[DUNGEON: The Twinning]** -> THE TEMPEST -> **[DUNGEON: Akadaemia Anyder]** -> AMAUROT -> **[DUNGEON: Amaurot]** -> **[TRIAL: The Dying Gasp]** HADES (Emet-Selch).

**SCOPE:** the Light-sickness after Innocence; the truth of the Crystal Exarch; the descent into THE TEMPEST and the recreated city of AMAUROT; the confrontation with HADES (Emet-Selch) in The Dying Gasp — the 5.0 climax (L80).

**DUNGEON-SCOPE NOTE:** ShB's two remaining L79/L80 dungeons — **The Twinning** and **Akadaemia Anyder** — are OPTIONAL (unlocked by side quests), NOT MSQ, and are excluded from this index. The ShB MSQ dungeons are: Holminster Switch, Dohn Mheg, The Qitana Ravel, Malikah's Well, Mt. Gulg, Amaurot.
**TITLE FIX:** list title "The Storm-tossed Seas" -> correct **To Storm-tossed Seas**; its Next is **Waiting in the Depths** (the CGW "The Tempest" reading was spurious).

---

**Reassuring the Masses** — giver: the Manager of Suites (the Crystarium) · MSQ `[COND: relay]`
- Bragi -> Chessamile -> Moren -> Katliss
- Next: In His Garden
- (the Warrior hides the worsening Light-sickness)

**In His Garden** — giver: Katliss (the Crystarium) · MSQ `[COND: parallel → The Unbroken Thread]`
- take a moment to feel the wind upon your face -> gather information on the Crystal Exarch (0/3) -> Lyna at the Accensor Gate
- Next: The Unbroken Thread

**The Unbroken Thread** — giver: Lyna (the Crystarium) · MSQ
- head to the Ocular -> Lyna -> the aspiring amaro tamer -> Urianger
- Next: To Storm-tossed Seas
- Manifest tie (08.1 ShB): Urianger reveals the Exarch's true plan — to bear the Light himself and be cast into the rift.

**To Storm-tossed Seas** — giver: Urianger (Sullen, Lakeland) · MSQ `[COND: fetch]` [title corrected]
- Urianger -> investigate suspect rock formations beneath the water's surface (0/2) -> Urianger (x2)
- Next: Waiting in the Depths

**Waiting in the Depths** — giver: Thancred (the Tempest) · MSQ
- search for anything unusual on the Norvrandt Slope -> the Ondo youth -> Alphinaud -> defeat blue swimmers (0/3) -> Paushs Ooan
- Next: City of the Ancients
- (the party breathes underwater by amaurotine means and enters THE TEMPEST)

**City of the Ancients** — giver: Y'shtola (the Tempest) · MSQ `[COND: fetch]`
- Y'shtola -> inspect the Ondo Cups from the survey point -> use the mythril knife to collect scrapings from the remnant wall -> Y'shtola -> find a structure resembling those in the Qitana Ravel mural and inspect it -> Y'shtola
- Next: The Light of Inspiration

**The Light of Inspiration** — giver: Y'shtola (the Tempest) · MSQ `[COND: fetch]`
- Paushs Ooan -> search for Grenoldt -> approach Grenoldt and /psych him up -> complete any role quest line at the Wandering Stairs in the Crystarium -> present something inspiring to Grenoldt
- Next: The Illuminated Land

**The Illuminated Land** — giver: Grenoldt (the Tempest) · MSQ `[COND: relay]`
- deliver Grenoldt's lamp to Tolshs Aath -> the Ondo guide (x2) -> Urianger -> Alphinaud -> Alisaie (x2) -> proceed towards the end of the Caliban Gap -> Y'shtola
- Next: The End of a World

**The End of a World** — giver: Alisaie (the First — Amaurot, the Tempest) · MSQ
- investigate the imposing doors -> Alisaie -> gather information in Amaurot (0/3) -> Alphinaud
- Next: A Greater Purpose
- Manifest tie (08.1 ShB): AMAUROT — Emet-Selch's perfect recreation of the sunken capital of the ancients.

**A Greater Purpose** — giver: Alphinaud (the Tempest) · MSQ `[COND: fetch]`
- the administrative clerk -> wait at the designated location -> the administrative clerk -> submit the visitor's writ application to the secretariat clerk -> find an empty seat -> the secretariat clerk -> show the visitor's writ to Thancred
- Next: Shadowbringers

**Shadowbringers** (5.0 FINALE quest) — giver: the Crystal Exarch (the Crystarium) · MSQ
- Alphinaud -> Urianger -> Y'shtola -> Thancred -> Ryne -> the Capitol attendant -> enter [DUNGEON: Amaurot] -> [TRIAL: The Dying Gasp] confront HADES -> the Crystal Exarch -> Tataru in the Rising Stones
- FINAL BOSS: HADES — Emet-Selch's true unsundered Ascian form.
- Manifest tie (08.1 ShB L24): the Warrior nearly becomes a Lightwarden but is anchored by the Scions' aether and Ardbert's soul (the Azem crystal); Emet-Selch falls, mourning his lost people. The Crystal Exarch is revealed as G'raha Tia. End of 5.0.
- Next: (Patch 5.1) Vows of Virtue, Deeds of Cruelty — see INSTALLMENT 26.

---

**SCOPE:** 5.1 (Vows of Virtue, Deeds of Cruelty) — the aftermath on the First: healing sundered souls (Beq Lugg), rebuilding Eulmore (Chai-Nuzz); 5.2 (Echoes of a Fallen Star) — the new imperial threat stirs (Telophoroi), the Ronkan trial, and the deep sea (L80).

**DUTY PLACEMENTS (ShB 5.3, wiki-verified):** the dungeon The Heroes' Gauntlet is unlocked by **The Converging Light** (Y'shtola); the Elidibus solo duty (as Ardbert) is in **Faded Memories** (Thancred); the 'defeat the Warrior of Light' solo duty is in **Hope's Confluence** (Crystal Exarch); the trial The Seat of Sacrifice (Elidibus) is unlocked by **Hope's Confluence** and fought at the 5.3 climax (GE-verified — NOT inside 'Reflections in Crystal', which is the denouement). Title: **The Admiral's Resolve** (singular).

---

## PATCH 5.1 — Vows of Virtue, Deeds of Cruelty

**Shaken Resolve** — giver: Tataru (the Rising Stones) · MSQ `[COND: relay]`
- F'lhaminn at the House of Splendors -> Tataru -> the Crystal Exarch in the Ocular
- Next: A Grand Adventure

**A Grand Adventure** — giver: the Crystal Exarch (the Ocular) · MSQ
- the Crystal Exarch in Sullen -> enter [DUNGEON: The Grand Cosmos] -> Alphinaud
- Next: A Welcome Guest
- Manifest tie (08.1 ShB patch): THE GRAND COSMOS — the enchanted manor haunted by the White Lady of Lakeland.

**A Welcome Guest** — giver: Alphinaud (Lakeland) · MSQ `[COND: fetch]`
- return to the Ocular -> Beq Lugg -> Beq Lugg at the Inn at Journey's Head -> treat the patients with soul tonic (0/3) -> Beq Lugg
- Next: Good for the Soul
- (Beq Lugg, the Nu Mou loremaster, aids the sundered-soul afflicted)

**Good for the Soul** — giver: Beq Lugg (Amh Araeng) · MSQ `[COND: fetch]`
- Beq Lugg -> Magnus -> search Mount Biran Mines for lumps of pristine clay (0/3) -> deliver them to Beq Lugg -> Alisaie
- Next: Nowhere to Turn

**Nowhere to Turn** — giver: Kai-Shirr (Amh Araeng) · MSQ `[COND: relay]`
- Alphinaud in Eulmore -> search for Dulia-Chai
- Next: A Notable Absence

**A Notable Absence** — giver: Alphinaud (Eulmore) · MSQ `[COND: parallel → Moving Forward]`
- gather information about Master Chai's disappearance in the Canopy -> in the Buttress -> in the Derelicts -> Alphinaud at the Glory Gate
- Next: For the People

**For the People** — giver: Alphinaud (Eulmore) · MSQ `[COND: relay]`
- Hastelot -> Alphinaud -> search for Chai-Nuzz -> Tristol -> Wrenden -> Chai-Nuzz
- Next: Finding Good Help

**Finding Good Help** — giver: Chai-Nuzz (Kholusia) · MSQ `[COND: relay]`
- Chai-Nuzz -> guide Chai-Nuzz from the vantage point -> Chai-Nuzz -> Wrenden
- Next: Moving Forward

**Moving Forward** — giver: Chai-Nuzz (Eulmore) · MSQ
- Chadden -> Alphinaud -> Kai-Shirr
- Next: Vows of Virtue, Deeds of Cruelty
- (Chai-Nuzz becomes Eulmore's elected leader)

**Vows of Virtue, Deeds of Cruelty** (5.1 finale) — giver: Alphinaud (the Crystarium) · MSQ `[COND: relay]`
- the Crystal Exarch in the Ocular -> Tataru -> Tataru at the Rising Stones -> Tataru
- Next: Old Enemies, New Threats

---

## PATCH 5.2 — Echoes of a Fallen Star

**Old Enemies, New Threats** — giver: Krile (the Rising Stones) · MSQ `[COND: relay]`
- Maxima at the Ala Mhigan Quarter in the Lochs -> Krile
- Next: The Way Home
- (Source-side: the Telophoroi cult and a returned threat stir)

**The Way Home** — giver: Krile (the Lochs) · MSQ `[COND: relay]`
- the Crystal Exarch in the Ocular
- Next: Seeking Counsel

**Seeking Counsel** — giver: Alphinaud (the Ocular) · MSQ `[COND: relay]`
- Lyna -> Lyna at Fort Jobb in Lakeland -> the Crystarium Scout -> Lyna
- Next: Facing the Truth

**Facing the Truth** — giver: Lyna (the Crystarium) · MSQ `[COND: relay]`
- Alphinaud -> the people of the Crystarium -> Alphinaud
- Next: A Sleep Disturbed

**A Sleep Disturbed** — giver: the Crystal Exarch (the Ocular) · MSQ
- Almet at Fanow in Rak'tika -> Almet at Rak'tika Falls -> [SOLO DUTY: the Trial of Ronka — answer Huaca's riddles, match the cards to free your allies, then defeat Huaca] -> leave Trial's Threshold -> Almet
- Next: An Old Friend

**An Old Friend** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Runar in Slitherbough -> Asgeir (obtain a well-worn broom) -> take the broom to Y'shtola -> Thancred
- Next: Deep Designs

**Deep Designs** — giver: Y'shtola (the Rak'tika Greatwood) · MSQ `[COND: fetch]`
- Tolshs Aath in the Ondo Cups -> retrieve the mnyiri livers from the Flounders' Floor -> deliver them to Tolshs Aath
- Next: A Whale's Tale

**A Whale's Tale** — giver: Urianger (the Tempest) · MSQ `[COND: fetch]`
- Urianger in Sullen -> Urianger -> remove tenacious barnacles -> Urianger -> Thancred (x2)
- Next: Beneath the Surface

**Beneath the Surface** — giver: Urianger (Lakeland) · MSQ
- Urianger at the Split Hull -> enter [DUNGEON: Anamnesis Anyder] -> Y'shtola
- Next: Echoes of a Fallen Star
- Manifest tie (08.1 ShB patch): ANAMNESIS ANYDER — the sunken Ronkan facility mirrored beneath the Tempest.

**Echoes of a Fallen Star** (5.2 finale) — giver: Urianger (Kholusia) · MSQ `[COND: relay]` [title corrected]
- Alphinaud -> Theyler -> the Crystal Exarch -> the manager of suites in the Pendants
- Next: In the Name of the Light

---

**SCOPE:** 5.3 (Reflections in Crystal) — Elidibus's endgame on the First and the **return to the Source** (the Crystal Exarch farewell); 5.4 (Futures Rewritten) — a lighter Source interlude in La Noscea (pirates, Matoya, the great ship Vylbrand).

---

## PATCH 5.3 — Reflections in Crystal

**In the Name of the Light** — giver: the Manager of Suites (the Crystarium) · MSQ `[COND: fetch]`
- Moren -> Riqi-Tio -> Chessamile -> Gracine -> obtain bunches of undersized grapes (0/3) -> deliver them to Riqi-Tio -> Chessamile
- Next: Heroic Dreams

**Heroic Dreams** — giver: Eirwel (the Crystarium) · MSQ `[COND: fetch]`
- Alisaie at the Exarch gate -> use heat lures to draw out vampire bats and slay them for fangs (0/3) -> deliver bat fangs to Ryne -> the lookout in the Crystarium -> the Crystal Exarch
- Next: Fraying Threads

**Fraying Threads** — giver: Ryne (the Crystarium) · MSQ `[COND: relay]`
- Thancred -> Tataru at the Rising Stones -> enter Dawn's Respite -> Krile
- Next: Food for the Soul
- (brief Source-side check on the sleeping Scions; Dawn's Respite)

**Food for the Soul** — giver: Tataru (the Rising Stones) · MSQ `[COND: fetch]`
- Tataru -> deliver the Archon loaf to the Crystal Exarch in the Ocular -> Urianger
- Next: Faded Memories

**Faded Memories** — giver: Thancred (the Crystarium) · MSQ
- Y'shtola -> Venmont Yards (the shipwright) -> travel to Anamnesis Anyder by boat -> [SOLO DUTY: enter the aetherial stream — phantom Amaurot; defeat the recreations of past enemies; defeat **Elidibus in the guise of Ardbert**] -> Y'shtola
- Next: Etched in the Stars

**Etched in the Stars** — giver: the Peculiar Crystal (the Tempest) · MSQ `[COND: fetch]`
- examine the crystals -> search for crystals (repeat sweeps) -> examine the crystal -> Y'shtola
- Next: The Converging Light

**The Converging Light** — giver: Y'shtola (Kholusia) · MSQ
- Y'shtola in Eulmore -> Chai-Nuzz -> enter [DUNGEON: The Heroes' Gauntlet] -> the Crystal Exarch -> the nervous guard -> the Crystal Exarch
- Next: Hope's Confluence
- Manifest tie (08.1 ShB patch): THE HEROES' GAUNTLET — Eulmore's underbelly, warped by Elidibus's rallying of the star's "heroes."

**Hope's Confluence** — giver: the Crystal Exarch (the Crystarium) · MSQ
- [SOLO DUTY: defeat the Warrior of Light (Ardbert's manifested memory)] -> Ryne
- Next: Nothing Unsaid

**Nothing Unsaid** — giver: Y'shtola (the Crystarium) · MSQ `[COND: relay]`
- Alisaie -> Alisaie at the Inn at Journey's Head -> search for Halric -> Alisaie -> travel to Eulmore -> Alphinaud
- Next: The Journey Continues

**The Journey Continues** — giver: Alphinaud (Eulmore) · MSQ
- Urianger at the Bookman's Shelves -> deliver the faded Crystal of Light to Seto -> Urianger
- Next: Unto the Morrow
- (Seto, the aged Nu Mou guardian of Rak'tika, and Ardbert's crystal)

**Unto the Morrow** — giver: Urianger (Il Mheg) · MSQ
- Y'shtola in Slitherbough -> Y'shtola -> Magnus at Twine -> Ryne in the Crystarium -> Thancred
- Next: Reflections in Crystal
- (farewells across the First before the confrontation)

**Reflections in Crystal** (5.3 FINALE) — giver: Beq Lugg (the Ocular, the Crystarium) · MSQ
- Beq Lugg -> G'raha Tia -> [TRIAL: The Seat of Sacrifice] (**Elidibus**, wielding the Warriors of Light) -> aftermath cutscenes
- Reveal beats: **Elidibus defeated**; the WoL's soul returns to the Source body; the **Crystal Exarch = G'raha Tia** relinquishes the tower and comes to the Source to join the Scions.
- Next: Alisaie's Quest

---

## PATCH 5.4 — Futures Rewritten

**Alisaie's Quest** — giver: Krile (the Rising Stones) · MSQ `[COND: relay]`
- Alisaie -> Tataru in Mor Dhona -> Alisaie
- Next: The Wisdom of Allag

**The Wisdom of Allag** — giver: G'raha Tia (Azys Lla) · MSQ `[COND: fetch]`
- G'raha Tia -> G'raha Tia again -> find a point of stagnant lightning and defeat the lightning sprites -> examine it, obtain a concentrated lightning shard -> deliver it to G'raha Tia
- Next: Reviving the Legacy

**Reviving the Legacy** — giver: G'raha Tia (Azys Lla) · MSQ `[COND: relay]`
- G'raha Tia at the Rising Stones -> wait for Cid in Dawn's Respite -> Cid -> show the Ironworks promissory note to Fromelaut at the Skysteel Manufactory -> hand it to the Skysteel engineer
- Next: Forget Us Not

**Forget Us Not** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- Alisaie at Maelstrom Command -> Alphinaud
- Next: Like Master, Like Pupil

**Like Master, Like Pupil** — giver: Y'shtola (Limsa Lominsa Upper Decks) · MSQ
- Y'shtola in the Ruling Quarter -> Matoya -> Puro Roggo in the Makers' Quarter -> enter [DUNGEON: Matoya's Relict] -> Alphinaud
- Next: The Admiral's Resolve
- Manifest tie (08.1 ShB patch): MATOYA'S RELICT — Matoya's automated cave laboratory in the Dravanian Hinterlands, overrun.

**The Admiral's Resolve** — giver: Alphinaud (the Dravanian Hinterlands) · MSQ `[COND: parallel → Futures Rewritten]` [title corrected: singular]
- Zanthael on the lower decks of Limsa Lominsa -> Alphinaud -> the leaders of Limsa Lominsa's pirate powers (0/2) -> Alphinaud
- Next: The Search for Sicard

**The Search for Sicard** — giver: Alphinaud (Limsa Lominsa Lower Decks) · MSQ `[COND: relay]`
- Alphinaud at Oschon's Embrace -> Alphinaud
- Next: On Rough Seas

**On Rough Seas** — giver: Alphinaud (Lower La Noscea) · MSQ `[COND: relay]`
- Merlwyb in the command room -> Merlwyb
- Next: The Great Ship Vylbrand

**The Great Ship Vylbrand** — giver: Merlwyb (Command Room, Limsa Lominsa) · MSQ `[COND: relay]`
- Alisaie at Camp Overlook -> Merlwyb -> Merlwyb again
- Next: Futures Rewritten

**Futures Rewritten** (5.4 FINALE) — giver: Alphinaud (Outer La Noscea) · MSQ
- Lyse in the Ala Mhigan Quarter -> Lyse -> Krile at the Rising Stones
- Next: Unto the Breach

---

**SCOPE:** 5.5 (Death Unto Dawn, Part 1) — the Telophoroi endgame at Azys Lla and Ul'dah (**[DUNGEON: Paglth'an]**); 5.55 (Death Unto Dawn, Part 2) — the first tremor of the coming calamity and the launch preparations that seam directly into **ENDWALKER**.

**FIX vs skeleton list:** dungeon PAGLTH'AN is entered in **The Flames of War** (#5), not the 5.5 finale *When the Dust Settles* (which is the aftermath).

---

## PATCH 5.5 — Death Unto Dawn (Part 1)

**Unto the Breach** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- Urianger in the Ala Mhigan Quarter -> Arenvald
- Next: Here Be Dragons

**Here Be Dragons** — giver: Alphinaud (the Lochs) · MSQ `[COND: relay]`
- Alphinaud in Ishgard -> Lucia -> Alisaie at the airship landing -> Alphinaud in the Delta Quadrant (Azys Lla)
- Next: Righteous Indignation

**Righteous Indignation** — giver: Estinien (Azys Lla) · MSQ `[COND: fetch]`
- proceed to the designated location -> G'raha Tia -> Alphinaud at the Flagship -> search for the necessary Allagan node (0/3) -> Alphinaud -> use the field trial spirit vessel to access the clamorous node
- Next: For Vengeance

**For Vengeance** — giver: the Restrainment Node (Azys Lla) · MSQ `[COND: relay]`
- access the Flagship terminal -> Alisaie -> Alisaie again -> G'raha Tia
- Next: The Flames of War

**The Flames of War** — giver: G'raha Tia (Azys Lla) · MSQ
- Thancred at the Hall of Flames -> the Immortal Flames pilot at the airship landing in Ul'dah -> enter [DUNGEON: Paglth'an] -> Alphinaud
- Next: When the Dust Settles
- Manifest tie (08.1 ShB patch): PAGLTH'AN — the Amalj'aa holy ground seized by the Telophoroi; Lunar Bahamut / the summoned menace routed with the Immortal Flames. The star's aether roils — first omen of the coming days.

**When the Dust Settles** (5.5 FINALE) — giver: Alphinaud (Ul'dah - Steps of Nald) · MSQ `[COND: relay]`
- the Phrontistery chirurgeon -> Alphinaud -> Alisaie -> return to the Rising Stones -> Tataru
- Next: The Company We Keep
- (Arenvald recovers from wounds taken at Paglth'an; the Scions regroup)

---

## PATCH 5.55 — Death Unto Dawn (Part 2)

**The Company We Keep** — giver: Alisaie (the Rising Stones) · MSQ `[COND: relay]`
- the Resistance guard in the Ala Mhigan Quarter -> Alphinaud -> Alisaie -> Riol at Castrum Oriens
- Next: On Official Business

**On Official Business** — giver: Alphinaud (the Fringes) · MSQ `[COND: relay]`
- Alisaie in Gridania -> Frixio in Little Solace -> the silent conjurer at Nophica's Altar -> Kan-E-Senna -> Alisaie
- Next: Death Unto Dawn

**Death Unto Dawn** (5.55 FINALE — SHADOWBRINGERS END) — giver: Kan-E-Senna (the Lotus Stand, Gridania) · MSQ
- Alphinaud outside the Carline Canopy -> Alisaie -> Aymeric
- Reveal beats: strange aetheric disturbances and mass unrest across Eorzea — the **first thread of the Final Days**; the Scions prepare to sail for distant shores.
- **Next: The Next Ship to Sail** (ENDWALKER 6.0 opener) — EXPANSION SEAM

---

> **SHADOWBRINGERS COMPLETE** (5.0 base + patches 5.1-5.55). Installments 20-28 cover the full ShB main scenario, CGW-verified, full step spines, coordless. Seam confirmed: **Death Unto Dawn -> The Next Ship to Sail**.
>
> Next: **ENDWALKER 6.0** build begins — opener **The Next Ship to Sail** (giver at the Rising Stones), Old Sharlayan / Thavnair / Garlemald arc toward the Final Days. Then EW patches 6.1-6.5x.

# 08.6 — ORDERED MSQ INDEX (AUTHORITATIVE DATA) — ENDWALKER (6.0)

(convenzioni: vedi 08.0)

**SCOPE:** the opening of ENDWALKER — arrival in **Old Sharlayan** (Krile, the Forum), descent into **Labyrinthos**, and the voyage to **Thavnair / Radz-at-Han** (Matsya, Varshahn). No duties in this block; the first dungeon (Tower of Zot) follows shortly after.

---

**The Next Ship to Sail** — giver: Alphinaud (the Rising Stones) · MSQ `[COND: relay]`
- Tataru in Limsa Lominsa -> Krile
- Next: Old Sharlayan, New to You

**Old Sharlayan, New to You** — giver: Krile (Old Sharlayan) · MSQ
- G'raha Tia -> Krile (with G'raha Tia) -> guided tour of the city with G'raha Tia & Krile: the Last Stand -> the aetheryte plaza -> the Agora -> the Rostra -> Journey's End -> the Baldesion Annex -> Krile in the main hall
- Next: Hitting the Books

**Hitting the Books** — giver: Krile (the Main Hall, Baldesion Annex) · MSQ `[COND: fetch]`
- Krile outside Noumenon -> read books in Noumenon on the relevant subjects (0/3) -> wait at the designated location (x3) -> Krile
- Next: A Seat at the Last Stand

**A Seat at the Last Stand** — giver: Alisaie (Old Sharlayan) · MSQ `[COND: fetch]`
- Alisaie -> Last Stand customers with Alisaie (0/2) -> Dickon -> serve the correct dishes (tea set to the group by the water; omelette to Gisla; lobster to the Miqo'te gentleman) -> Alisaie (x2)
- Next: A Labyrinthine Descent

**A Labyrinthine Descent** — giver: Alisaie (Old Sharlayan) · MSQ `[COND: parallel → The Full Report, Warts and All]`
- Krile -> follow Alisaie's lead -> Krile -> gather information in upper Acrinthos (0/3) -> Krile
- Next: Glorified Ratcatcher
- (the party descends into Labyrinthos, the vast subterranean biosphere beneath Sharlayan)

**Glorified Ratcatcher** — giver: Krile (Labyrinthos) · MSQ `[COND: fetch]`
- Erenville -> track and capture the grizzled mouse (defeat enemies; use the rat sack) -> deliver the squirming rat sack to Erenville -> Alphinaud
- Next: Deeper into the Maze
- (Erenville, the Sharlayan hunter/guide, is introduced)

**Deeper into the Maze** — giver: Alphinaud (Labyrinthos) · MSQ `[COND: fetch]`
- the Archeion custodian -> Y'shtola -> people outside the Archeion (0/2) -> the pack-bearing gleaner -> sedate the target with the sleeping dart -> Alphinaud
- Next: The Medial Circuit

**The Medial Circuit** — giver: Alisaie (Labyrinthos) · MSQ `[COND: fetch]`
- survey the areas and defeat enemies -> Alphinaud -> survey at the designated location -> gather information at Meryall Agronomics (0/3) -> investigate the stacked boxes -> Y'shtola
- Next: The Full Report, Warts and All

**The Full Report, Warts and All** — giver: Alisaie (Labyrinthos) · MSQ
- Y'shtola -> (transfigured) Alphinaud -> head to the designated location transfigured with Alphinaud & Alisaie -> Alphinaud
- Next: A Guide of Sorts
- (the party is transfigured to blend into Labyrinthos)

**A Guide of Sorts** — giver: Alisaie (Labyrinthos) · MSQ `[COND: relay]`
- Y'shtola -> search for Krile -> Y'shtola
- Next: Estate Visitor

**Estate Visitor** — giver: Alisaie (Old Sharlayan) · MSQ
- Alphinaud -> Alisaie (with Alphinaud) -> Ameliance (the twins' mother) -> Alphinaud -> Krile in the main hall of the Baldesion Annex
- Next: For Thavnair Bound

**For Thavnair Bound** — giver: Thancred (the Main Hall, Old Sharlayan) · MSQ
- Kytte at the Confluence -> wait at the aetheryte plaza -> search for Estinien -> /deny to Estinien that the deal is fair -> deliver a bottle of special amra lassi to Urianger -> to Thancred
- Next: On Low Tide
- (Estinien rejoins; the party departs for Thavnair)

**On Low Tide** — giver: Thancred (Yedlihmad, Thavnair) · MSQ `[COND: parallel → A Boy's Errand]`
- gather information in Yedlihmad (0/4) -> Khalzahl -> Matsya
- Next: A Fisherman's Friend

**A Fisherman's Friend** — giver: Matsya (Yedlihmad) · MSQ `[COND: relay]`
- with Matsya: Mehrunnah -> Nashreen -> Bhazahma -> accompany Matsya to the pier -> Thancred
- Next: House of Divinities

**House of Divinities** — giver: Estinien (Thavnair) · MSQ `[COND: fetch]`
- search for Matsya (repeat) -> render aid to Matsya -> Matsya -> gather information in Akyaali (0/2) -> Matsya
- Next: The Great Work

**The Great Work** — giver: Matsya (Radz-at-Han) · MSQ `[COND: fetch]`
- Nidhana (x2) -> follow the drunken deepa across the city (repeat) -> obtain the drunken deepa -> deliver it to Nidhana
- Next: Shadowed Footsteps
- (arrival in Radz-at-Han, city of the Arkasodara)

**Shadowed Footsteps** — giver: Nidhana (Thavnair) · MSQ `[COND: fetch]`
- Nidhana (repeat) -> stand guard for Nidhana -> Nidhana
- Next: A Boy's Errand

**A Boy's Errand** — giver: Nidhana (Radz-at-Han) · MSQ
- Varshahn -> gather information at the tower outpost (0/3) -> Varshahn -> mount the Hamsa -> ride to the Giantsgall Grounds -> Zeynuha
- Next: Tipping the Scale
- (Varshahn, the satrap's young envoy, is introduced)

**Tipping the Scale** — giver: Zeynuha (Thavnair) · MSQ `[COND: fetch]`
- deliver the sack of giantsgall to Nidhana -> Nidhana -> the Radiant Host Soldier -> Thancred
- Next: The Satrap of Radz-at-Han

**The Satrap of Radz-at-Han** — giver: Thancred (Thavnair) · MSQ `[COND: relay]`
- Varshahn -> Thancred -> Thancred in the main hall
- Next: In the Dark of the Tower

---

**SCOPE:** the **[DUNGEON: The Tower of Zot]** on Thavnair, the Eorzean Alliance gathering warding scales, the frozen ruin of **Garlemald** (Jullus, the survivors of Tertium), the body-swap **[SOLO DUTY: In from the Cold]**, the **[DUNGEON: The Tower of Babil]**, and the ascent to **the Moon**.

**NOTE:** Tertium (in *The Last Bastion*) is a Garlemald settlement, NOT a dungeon. The Zodiark trial (The Dark Inside) is NOT in this block — it follows in the next installment.

---

**In the Dark of the Tower** — giver: Krile (the Main Hall, Old Sharlayan) · MSQ
- Nahbdeen at the Hamsa Hatchery -> stand by at the boat -> enter [DUNGEON: The Tower of Zot] -> Thancred
- Next: The Jewel of Thavnair
- Manifest tie (08.1 EW): THE TOWER OF ZOT — the Telophoroi tower on Thavnair; the Magus Sisters (Minduruva, Sanduruva, Cinduruva) and Barnabas.

**The Jewel of Thavnair** — giver: Thancred (Thavnair) · MSQ `[COND: relay]`
- the Radiant guardsman -> Estinien (accompany) -> the attentive / watchful / vigilant Radiant -> the Meghaduta attendant -> Alisaie
- Next: The Color of Joy

**The Color of Joy** — giver: Alphinaud (Radz-at-Han) · MSQ `[COND: relay]`
- Alisaie (repeat) -> Alphinaud -> Alisaie -> Krile at the Baldesion Annex -> Ojika Tsunjika
- Next: Sound the Bell, School's In

**Sound the Bell, School's In** — giver: Krile (Old Sharlayan) · MSQ `[COND: relay]`
- Alisaie -> Krile -> the excitable student -> Miss Aliapoh -> the level-headed student -> search for Montichaigne
- Next: A Capital Idea

**A Capital Idea** — giver: Krile (Old Sharlayan) · MSQ `[COND: relay]`
- G'raha Tia in the main hall of the Baldesion Annex -> the command room in Limsa Lominsa -> Raubahn in the Ala Mhigan Quarter
- Next: Best of the Best
- (the Eorzean Alliance convenes over the worldwide crisis)

**Best of the Best** — giver: Maxima (the Lochs) · MSQ `[COND: parallel → Tracks in the Snow]`
- enter the Royal Palace -> Y'shtola -> deliver warding scales to A-Ruhn-Senna, Sicard, Lyse, Lucia, Cirina -> a warding scale to Maxima -> Alphinaud
- Next: A Frosty Reception
- (Vrtra's warding scales protect the leaders from tempering)

**A Frosty Reception** — giver: Tataru (the Lochs) · MSQ `[COND: relay]`
- the Ironworks Pilot -> Alphinaud -> Y'shtola -> G'raha Tia -> Lucia -> Alisaie
- Next: Tracks in the Snow
- (the expedition sets out for frozen Garlemald)

**Tracks in the Snow** — giver: Emmanellain (Garlemald) · MSQ
- Emmanellain -> footprints in the snow (x2) -> Alisaie -> survey the designated location -> approach the girl in green -> the girl in green
- Next: How the Mighty Are Fallen

**How the Mighty Are Fallen** — giver: Licinia (Garlemald) · MSQ `[COND: parallel → A Way Forward]`
- Alphinaud -> deliver warming tinctures (sickly / emaciated / despondent refugee) -> to Licinia -> the burly tapper -> head for Tapper's Den -> Alisaie
- Next: At the End of the Trail

**At the End of the Trail** — giver: Jareck (Garlemald) · MSQ `[COND: fetch]`
- Alisaie -> search for Alphinaud -> Alisaie (x2) -> search for hints as to Licinia and her sister's whereabouts -> search for Licinia -> Alisaie
- Next: A Way Forward

**A Way Forward** — giver: Alphinaud (Garlemald) · MSQ
- Lucia (x2) -> Jullus -> accompany Jullus -> follow Alphinaud and Alisaie -> Jullus
- Next: The Last Bastion
- (Jullus, a sympathetic Garlean soldier, becomes the party's guide)

**The Last Bastion** — giver: Jullus (Garlemald) · MSQ
- defeat tempered soldiers alongside Jullus (repeat) -> catch up with Jullus -> enter Tertium (surviving settlement, not a dungeon) -> Alphinaud -> Jullus
- Next: Personae non Gratae

**Personae non Gratae** — giver: Jullus (Tertium) · MSQ `[COND: parallel → In from the Cold]`
- gather information in Tertium (0/5) -> Alphinaud -> assist Flavius -> Alphinaud -> Jullus
- Next: His Park Materials

**His Park Materials** — giver: Jullus (Garlemald) · MSQ `[COND: fetch]`
- Alisaie -> search for ceruleum in Forum Solius (0/4) -> Jullus -> search for ceruleum at the designated location -> deliver the temperature regulator ceruleum tank to Jullus
- Next: No Good Deed

**No Good Deed** — giver: Jullus (Garlemald) · MSQ `[COND: fetch]`
- Jullus -> use an incendiary #37 on the destroyed magitek armor to retrieve a ceruleum tank -> deliver the warmachina ceruleum tank to Jullus -> wait at the designated location -> Jullus
- Next: Alea Iacta Est

**Alea Iacta Est** — giver: Jullus (Tertium) · MSQ `[COND: relay]` [skeleton typo "Alea lacta Est"]
- Marcellinus -> Octavia -> Jullus -> wait at the specified location -> Lucia
- Next: Strange Bedfellows

**Strange Bedfellows** — giver: Lucia (Garlemald) · MSQ `[COND: fetch]`
- Alisaie -> Sabinianus -> Caeso -> Flavius -> Alphinaud -> survey the designated locations and deal with enemies (0/4) -> Thancred -> Lucia
- Next: In from the Cold

**In from the Cold** — giver: Lucia (Camp Broken Glass, Regio Urbanissima / Garlemald) · MSQ
- Y'shtola -> Alisaie -> [SOLO DUTY: In from the Cold] the WoL's body is hijacked; play the possessed Garlean — find and mount the Magitek Reaper, retrieve the ceruleum tank, defend the citizens, survive the QTE, and crawl to Camp Broken Glass
- Next: Gateway of the Gods
- Reveal beat: **Zenos** demonstrates soul-transference (body-swap); the hooded man's identity is felt but not yet spoken.

**Gateway of the Gods** — giver: Lucia (Garlemald) · MSQ
- Lyse -> Pipin -> wait inside the station -> enter [DUNGEON: The Tower of Babil] -> clear it -> Alphinaud
- Next: A Trip to the Moon
- Manifest tie (08.1 EW): THE TOWER OF BABIL — the great tower Fandaniel & Zenos use to reach the Moon; Anima at its summit. (Zodiark's release is the looming threat — the trial follows.)

**A Trip to the Moon** — giver: G'raha Tia (the Nethergate) · MSQ
- activate the teleportation device -> the ancient spirit (x2) -> survey the destination -> search the Watcher's Palace for the source of the voice
- Next: Sea of Sorrows
- (arrival on the Moon; the Loporrits and the Watcher's Palace)

---

**SCOPE:** the Moon (**Mare Lamentorum**) — the Watcher, Zodiark's prison, the **[TRIAL: The Dark Inside]** (Zodiark), and the Loporrits; the return to the Source as the **Final Days** strike Thavnair — **[DUNGEON: Vanaspati]** and the blasphemies.

---

**Sea of Sorrow** — giver: the Watcher (Mare Lamentorum) · MSQ `[COND: parallel → The Martyr]` [title corrected: singular]
- speak with the faded / dreaming / forlorn / somber spirit -> approach the lustrous dog and follow it -> the temperamental spirit (x2) -> follow the lustrous dog again -> the anguished spirit
- Next: The Martyr

**The Martyr** — giver: the Watcher (Mare Lamentorum) · MSQ
- ride the lustrous dog -> confront Zodiark in [TRIAL: The Dark Inside] -> the Watcher
- Next: In Shadow's Wake
- Manifest tie (08.1 EW): THE DARK INSIDE — **Zodiark** (bound primal-god of the ancients), roused within his lunar prison. Reveal beats: the Watcher = Hydaelyn's echo/guardian; the true nature of Zodiark & Hydaelyn opens here.

**In Shadow's Wake** — giver: the Watcher (the Moon) · MSQ `[COND: parallel → A Harey Situation]`
- search for your comrades at the Watcher's Palace -> inspect the dimly / faintly / warmly / brightly glowing crystals -> Y'shtola
- Next: Helping Hands

**Helping Hands** — giver: the Watcher (Mare Lamentorum) · MSQ `[COND: fetch]`
- the Watcher (x2) -> suffuse the lunar spongoi with aether -> the Watcher -> Y'shtola -> Thancred
- Next: A Harey Situation

**A Harey Situation** — giver: Thancred (Mare Lamentorum) · MSQ
- the chipper Loporrit -> the dozing Loporrit -> the snappy Loporrit (x2)
- Next: A Taste of the Moon
- (the Loporrits, the Moon's caretaker rabbits, are introduced)

**A Taste of the Moon** — giver: Livingway (Mare Lamentorum) · MSQ `[COND: fetch]`
- examine the storage crate -> show Cookingway the obscenely large carrot -> eat the obscenely large carrot -> Cookingway
- Next: Styled a Hero

**Styled a Hero** — giver: Livingway (Mare Lamentorum) · MSQ `[COND: fetch]`
- the restless Loporrit -> the jubilant Loporrit (in your new attire) -> Livingway -> the fidgeting Loporrit -> Growingway (x2)
- Next: All's Vale That Endsvale

**All's Vale That Endsvale** — giver: Growingway (Mare Lamentorum) · MSQ `[COND: parallel → Skies Aflame]`
- Growingway (x2) -> do a big stretch near Growingway -> accompany Growingway to five designated locations (speak at each) -> Y'shtola
- Next: Back to Old Tricks

**Back to Old Tricks** — giver: Thancred (Mare Lamentorum) · MSQ `[COND: relay]`
- search for Urianger (x2) -> follow Urianger -> Urianger
- Next: Setting Things Straight

**Setting Things Straight** — giver: Urianger (Mare Lamentorum — the Moon) · MSQ `[COND: fetch]` [CGW-zone "Ultima Thule" is an error]
- Urianger -> stand watch and defeat any enemies (x2 locations) -> Urianger -> Y'shtola -> search for Runningway -> Y'shtola
- Next: Heart of the Matter

**Heart of the Matter** — giver: Growingway (the Moon) · MSQ `[COND: fetch]`
- Growingway -> defeat the Loporrits -> Y'shtola -> Urianger
- Next: Returning Home

**Returning Home** — giver: Y'shtola (Mare Lamentorum) · MSQ `[COND: relay]`
- Thancred at the Nethergate -> Lucia at Camp Broken Glass -> Krile at the Baldesion Annex -> wait at the designated location -> Ojika Tsunjika
- Next: Skies Aflame
- (the party returns to the Source — the Final Days now scourge Eorzea and Thavnair)

**Skies Aflame** — giver: Tataru (Limsa Lominsa — the Scions' HQ) · MSQ
- head to the main hall -> journey to Thavnair -> Ahewann -> enter [DUNGEON: Vanaspati] -> Ahewann
- Next: The Blasphemy Unmasked
- Manifest tie (08.1 EW): VANASPATI — the Thavnairian garden district consumed by the Final Days; despair transmutes people into **blasphemies**.

**The Blasphemy Unmasked** — giver: Ahewann (Radz-at-Han) · MSQ `[COND: parallel → Warm Hearts, Rekindled Hopes]`
- with G'raha Tia: Nuhadeen -> gather information at Balshahn Bazaar (0/3) -> designated location -> gather information at Mehryde's Meyhane (0/2) -> Mihleel
- Next: Amidst the Apocalypse

**Amidst the Apocalypse** — giver: Mihleel (Radz-at-Han) · MSQ `[COND: parallel → Warm Hearts, Rekindled Hopes]`
- with G'raha Tia: Kama -> gather information in Kama (0/2) -> Djinabaha -> Kamala -> deliver the light / ordinary / weighty crates to Nahbrifhal / Mahnuha / Zeymeira -> Kamala -> Djinabaha
- Next: Beyond the Depths of Despair

**Beyond the Depths of Despair** — giver: G'raha Tia (Radz-at-Han) · MSQ `[COND: fetch]`
- Y'shtola -> Alphinaud -> survey and defeat enemies (x2) -> Alisaie -> save the villagers of Palaka's Stand (0/4) -> Alphinaud
- Next: That We Might Live

**That We Might Live** — giver: Alphinaud (Thavnair) · MSQ `[COND: fetch]`
- Matsya (x2) -> search for Qerasaf -> aid the wounded Qerasaf -> survey the area (x3) -> Matsya
- Next: When All Hope Seems Lost

**When All Hope Seems Lost** — giver: Matsya (Thavnair) · MSQ `[COND: fetch]`
- Yeruvvet -> Alisaie -> search for the villagers of Palaka's Stand -> aid the villager woman -> Matsya -> defeat the beasts at Purusa (0/3) -> Alphinaud
- Next: Warm Hearts, Rekindled Hopes

**Warm Hearts, Rekindled Hopes** — giver: Alisaie (Thavnair) · MSQ
- survey the designated location -> rescue Mehvan -> search for Mehvan's baby -> have Alphinaud tend to the baby -> Alphinaud
- Next: Simple Pleasures

**Simple Pleasures** — giver: Vrtra (Palaka's Stand, Thavnair) · MSQ `[COND: fetch]`
- Vrtra -> Nidhana -> deliver the hot chai to the villagers (0/3) -> Nidhana
- Next: Under His Wing

---

**SCOPE:** the close of the Thavnair Final Days (Vrtra shelters his people), the return to **the Crystarium** and the door to the past, and the long **ELPIS** arc in the ancient age of Amaurot — Hythlodaeus, Hermes, **Meteion**, the ancient Emet-Selch (Hades), and **Venat**. **No duty in this block** (both *Verdict and Execution* and *Travelers at the Crossroads* verified NOT to enter Ktisis Hyperboreia — that dungeon follows).

**REVEAL-GATE (handled by the procedure rules, listed here as data only):** in Elpis, Emet-Selch appears as a living ancient (not the Ascian); Hermes' link to future events and Venat's true identity are gated reveals — do not pre-empt them.

---

**Under His Wing** — giver: Matsya (Palaka's Stand) · MSQ `[COND: fetch]`
- Estinien -> Thancred in Radz-at-Han -> search for townspeople who missed the announcement (x2) -> wait at the designated location -> Alphinaud
- Next: At World's End
- (Vrtra opens Radz-at-Han as a refuge)

**At World's End** — giver: the Radiant Host Soldier (Radz-at-Han, Sundrop) · MSQ `[COND: relay]`
- the Radiant Host soldier (repeat) -> Mihleel -> Y'shtola -> Thancred
- Next: Return to the Crystarium

## ENDWALKER 6.0 — Level 86 (Crystarium -> Elpis)

**Return to the Crystarium** — giver: G'raha Tia (Radz-at-Han) · MSQ `[COND: relay]`
- Lyna -> wait for Lyna in front of the Cabinet of Curiosity -> Ryne
- Next: Hope Upon a Flower
- (the party travels to the First to seek a path into the distant past)

**Hope Upon a Flower** — giver: Ryne (the Crystarium) · MSQ
- the Crystarium gatekeep -> explore the facility (0/4) -> examine the door -> Hythlodaeus
- Next: Petalouda Hunt
- (Hythlodaeus manifests; the gateway to Elpis opens)

**Petalouda Hunt** — giver: Hythlodaeus (Elpis) · MSQ `[COND: fetch]`
- Hythlodaeus -> use the aetheric rope to capture weakened petaloudai (0/2) -> deliver them to Hythlodaeus
- Next: In Search of Hermes
- (arrival in Elpis, the ancients' garden of concepts)

**In Search of Hermes** — giver: Hythlodaeus (Elpis) · MSQ `[COND: fetch]`
- the Anagnorisis observer -> search for Hermes -> search for the adventurous ambystoma
- Next: Ponder, Warrant, Cherish, Welcome

**Ponder, Warrant, Cherish, Welcome** — giver: Hermes (Elpis) · MSQ
- Hermes -> Emet-Selch -> Meteion (accompany) -> Memnon -> search for idle creations -> Euanthe -> Hermes
- Next: Lives Apart
- (Meteion, Hermes' created messenger, is introduced; the ancient Emet-Selch)

**Lives Apart** — giver: Hermes (Elpis) · MSQ `[COND: fetch]`
- Hermes (x2) -> use the lightning converger to create ball lightning (0/2) -> Hermes (x2)
- Next: Their Greatest Contribution

**Their Greatest Contribution** — giver: Emet-Selch (Elpis) · MSQ `[COND: fetch]`
- Hermes (x2) -> Hythlodaeus -> (/say) "I have a favor to ask" then "Please, Emet-Selch" -> /wave to Emet-Selch from the edge of the isle -> Emet-Selch
- Next: Aether to Aether

**Aether to Aether** — giver: Hermes (Elpis) · MSQ `[COND: fetch]`
- search for Hermes -> Meteion (accompany) -> search for Doros -> Meteion
- Next: A Sentimental Gift

**A Sentimental Gift** — giver: Hermes (Elpis) · MSQ `[COND: fetch]`
- Meteion (accompany) -> examine flowers at the Twelve Wonders (0/2) -> look for flowers across Elpis (repeat) -> Meteion
- Next: Verdict and Execution

**Verdict and Execution** — giver: Hermes (Elpis) · MSQ
- Doros -> Hermes -> face down the lykaon and its fireballs (0/3) -> keep the lykaon's attention -> Emet-Selch
- Next: Travelers at the Crossroads

**Travelers at the Crossroads** — giver: Hythlodaeus (Elpis) · MSQ
- Hythlodaeus -> Venat -> search for the concept crystal -> deliver it to Venat
- Next: A Past, Not Yet Come to Pass
- (Venat, the traveling philosopher, is introduced)

**A Past, Not Yet Come to Pass** — giver: Venat (Elpis) · MSQ `[COND: relay]`
- Venat (repeat) -> Ismene -> Venat -> search for Timaios -> Venat
- Next: Witness to the Spectacle

**Witness to the Spectacle** — giver: Venat (Elpis) · MSQ `[COND: parallel → Caging the Messenger]`
- Venat -> the Peripeteia archivist (x2) -> the approachable archivist -> the unhurried observer -> Venat
- Next: Worthy of His Back

**Worthy of His Back** — giver: Venat (Elpis) · MSQ `[COND: relay]`
- survey the area from the vantage point -> Venat (repeat)
- Next: A Flower upon Your Return

**A Flower upon Your Return** — giver: Venat (Elpis) · MSQ `[COND: relay]`
- approach Argos -> Venat -> travel from northerly Zephyrneus to southerly Boreneus -> Venat (x2)
- Next: Hunger in the Garden

**Hunger in the Garden** — giver: Hythlodaeus (Elpis) · MSQ `[COND: fetch]`
- Hythlodaeus -> travel from easterly Boreneus to Euroneus -> search for Hermes in the Hungering Gardens -> Hythlodaeus
- Next: Words without Sound

**Words without Sound** — giver: Emet-Selch (Elpis) · MSQ `[COND: parallel → Caging the Messenger]`
- search the area for Meteion -> search beneath / north of / east of the Hungering Gardens -> Hermes
- Next: Follow, Wander, Stumble, Listen

**Follow, Wander, Stumble, Listen** — giver: Hythlodaeus (Elpis) · MSQ `[COND: fetch]`
- search for Meteion (with Emet-Selch, repeat) -> survey the areas -> Emet-Selch
- Next: Caging the Messenger

---

**SCOPE:** the **[DUNGEON: Ktisis Hyperboreia]** (Elpis), the return to the present, the **[DUNGEON: The Aitiascope] + [TRIAL: Hydaelyn]**, the launch of the Ragnarok to the edge of the universe, and the descent through **Ultima Thule** to **[DUNGEON: The Dead Ends] + [TRIAL: The Final Day] (Endsinger)** and the final duel with **Zenos**. **This completes base ENDWALKER 6.0.**

**GLITCH-TITLE NOTE:** In-game, the Ultima Thule quests #97-104 display with corrupted glyphs; the DECODED plain titles are used here (verified via CGW page-titles + Fandom decode). A few glyph-only pages (#100, #103, #104) would not render step lists to the extractor — their ORDER and titles are confirmed; step spines flagged for backfill at merge.

---

**Caging the Messenger** — giver: Hythlodaeus (Elpis) · MSQ
- Venat -> enter [DUNGEON: Ktisis Hyperboreia] -> Venat
- Next: Thou Must Live, Die, and Know
- Manifest tie (08.1 EW): KTISIS HYPERBOREIA — Elpis's high creation-magicks facility; the truth of Hermes & Meteion, and Venat's resolve.

**Thou Must Live, Die, and Know** — giver: Venat (Elpis) · MSQ
- Venat -> report to Krile in the main hall of the Baldesion Annex (return to the present)
- Next: As the Heavens Burn

**As the Heavens Burn** — giver: Krile (the Main Hall, Old Sharlayan) · MSQ
- Lucia at Camp Broken Glass -> [SOLO DUTY: fight as Alphinaud to protect the refugees; then as Alisaie coordinating with G'raha Tia; then as yourself with all comrades] -> Alisaie
- Next: Outside Help

**Outside Help** — giver: Lucia (Garlemald) · MSQ `[COND: relay]`
- Urianger -> return to the main hall of the Baldesion Annex -> the Rostra steward -> wait -> Alphinaud
- Next: Going Underground

**Going Underground** — giver: Fourchenault (Old Sharlayan) · MSQ
- Fourchenault outside the Archeion (x2) -> Alphinaud -> Hester -> Fourchenault -> Kokkol Dankkol -> Krile
- Next: No Job Too Small
- (Fourchenault, the twins' father, and the Forum are drawn in)

**No Job Too Small** — giver: Alphinaud (Sharlayan Hamlet) · MSQ `[COND: parallel → Her Children, One and All]`
- Alisaie -> gather information in Sharlayan Hamlet (0/3) -> search for the behatted rabbit
- Next: Wise Guides

**Wise Guides** — giver: Urianger (Labyrinthos) · MSQ `[COND: fetch]`
- Singingway -> survey the wotsit -> survey and defeat enemies -> Growingway -> Urianger -> Singingway
- Next: Agriculture Shock
- (the Loporrits help build the ark that could evacuate the star)

**Agriculture Shock** — giver: Cookingway (the Tempest) · MSQ `[COND: parallel → Her Children, One and All]`
- with Cookingway: Jebke -> accompany him to the vineyard / orange grove / pumpkin field / lemon grove -> Jebke -> Cookingway
- Next: Sage Council

**Sage Council** — giver: Urianger (Labyrinthos) · MSQ `[COND: parallel → Her Children, One and All]`
- Growingway -> the troubled researcher -> seek out troubled souls in Sharlayan Hamlet (0/8) -> Urianger -> wait -> Urianger
- Next: Hither and Yarns

**Hither and Yarns** — giver: Urianger (Labyrinthos) · MSQ `[COND: fetch]`
- search for Alisaie -> pick up the crate of samples -> deliver it to Alphinaud -> Theopauldin -> deliver the ream of documents to the reserved representative -> Theopauldin
- Next: Once Forged

**Once Forged** — giver: G'raha Tia (Labyrinthos) · MSQ `[COND: fetch]`
- G'raha Tia -> survey and defeat enemies -> survey again -> Kokkol Dankkol
- Next: Bonds of Adamant(ite)

**Bonds of Adamant(ite)** — giver: Kokkol Dankkol (Sharlayan Hamlet) · MSQ `[COND: relay]`
- wait -> Alphinaud -> Fourchenault at Aporia -> Clarilaine -> Fourchenault -> proceed to the entrance of Thaumazein -> Fourchenault
- Next: Her Children, One and All

**Her Children, One and All** — giver: Fourchenault (Labyrinthos) · MSQ
- Fourchenault -> enter [DUNGEON: The Aitiascope] -> clear it -> confront [TRIAL: Hydaelyn] at the Mothercrystal -> Fourchenault -> Ojika Tsunjika
- Next: A Bold Decision
- Manifest tie (08.1 EW): THE AITIASCOPE + HYDAELYN — the path to the Mothercrystal; **Hydaelyn** tests the WoL and entrusts her power. Reveal beat: Venat = Hydaelyn confirmed. (Trial subtitle: verify exact duty name at merge.)

**A Bold Decision** — giver: Krile (Old Sharlayan) · MSQ `[COND: relay]`
- Fourchenault -> Alphinaud -> Tataru -> wait -> Varsarudh
- Next: Friends Gathered
- (the resolve to chase Meteion to the edge of the universe aboard the Ragnarok)

**Friends Gathered** — giver: Tataru (Old Sharlayan) · MSQ
- Krile -> Thancred -> Y'shtola -> Alisaie -> Alphinaud -> Ojika Tsunjika
- Next: Unto the Heavens

**Unto the Heavens** — giver: Ojika Tsunjika (Old Sharlayan) · MSQ
- Fourchenault at Thaumazein -> Aeglyffe -> Livingway
- Next: A Strange New World
- (the Ragnarok launches beyond the edge of the star)

**A Strange New World** (#97) — giver: Alphinaud (Ultima Thule) · MSQ
- Alphinaud -> gather information at the vitrified fort (0/3) -> Alphinaud -> Estinien -> Alisaie
- Next: On Burdened Wings
- (arrival in Ultima Thule, the graveyard of dead civilisations at the universe's edge)

**On Burdened Wings** (#98) — giver: Urianger (Ultima Thule) · MSQ
- gather information in Reah Tahra (0/3) -> search for the source of the dragons' woes in Ahm Nohl -> investigate the dragon eggs (0/3, then continue) -> search for a dragonet near Ahm Nohl -> the bereaved dragon
- Next: A Test of Will
- (the dead dragon-race of Ultima Thule)

**A Test of Will** (#99) — giver: Estinien (Ultima Thule) · MSQ `[COND: relay]`
- Alphinaud -> Al End -> Alphinaud -> touch the wind confluence and await the others
- Next: Roads Paved with Sacrifice

**Roads Paved with Sacrifice** (#100) — giver: (Ultima Thule) · MSQ [glyph-title page; steps backfill at merge]
- narrative Ultima Thule beat ->
- Prev: A Test of Will · Next: Flesh Abandoned

**Flesh Abandoned** (#101) — giver: Coph-coodg (Ultima Thule) · MSQ
- Coph-coodg -> wait at the designated location (x2) -> Y'shtola
- Next: Where Knowledge Leads
- (the Ea, the extinct philosopher-race that willed itself to extinction)

**Where Knowledge Leads** (#102) — giver: Urianger (Ultima Thule) · MSQ `[COND: relay]`
- Urianger -> G'raha Tia -> Y'shtola
- Next: Victory, All is Lost

**Victory, All is Lost** (#103) — giver: (Ultima Thule) · MSQ [glyph-title page; steps backfill at merge]
- narrative Ultima Thule beat ->
- Prev: Where Knowledge Leads · Next: Truth Not Found

**Truth Not Found** (#104) — giver: (Ultima Thule) · MSQ [glyph-title page; steps backfill at merge]
- narrative Ultima Thule beat ->
- Prev: Victory, All is Lost · Next: Hello, World

**Hello, World** (#105) — giver: G'raha Tia (Base Omicron) · MSQ
- observe M-017 with G'raha Tia -> identify an anomaly in M-017 when it manifests
- Next: Forge Ahead
- (the Omicrons — the machine-race that chose to keep living)

**Forge Ahead** (#106) — giver: Alphinaud (Ultima Thule) · MSQ `[COND: relay]`
- Alphinaud -> accompany Alphinaud -> Alisaie (accompany) -> follow the crystalline path -> Alphinaud
- Next: You're Not Alone

**You're Not Alone** (#107) — giver: Alisaie (the Nekropolis) · MSQ
- explore the nekropolis (0/6) -> Alisaie -> Alphinaud -> make your way to Absolute Horizon -> Alisaie
- Next: Endwalker
- (Meteion at Absolute Horizon; the party lends the WoL their strength)

**Endwalker** (#108 — 6.0 FINALE) — giver: Alphinaud (Ultima Thule) · MSQ
- enter [DUNGEON: The Dead Ends] -> confront the Endsinger in [TRIAL: The Final Day] -> [SOLO DUEL: Zenos viator Galvus] -> speak with your comrades (0/8) -> Tataru
- Reveal beats: the **Endsinger** (the despair-song of Meteion's collective / the will of the dead star) is defeated on **The Final Day**; the Final Days are ended; **Zenos** returns for the final duel and dies as the WoL's "friend."
- **Next: Newfound Adventure** (ENDWALKER PATCH 6.1 opener)

---

> **ENDWALKER 6.0 COMPLETE** (108 quests, installments 29-33, CGW-verified, coordless). Seam confirmed: **Endwalker -> Newfound Adventure**.
> Next: **ENDWALKER PATCHES 6.1-6.55** (Newfound Adventure -> ... -> Growing Light), the last block before the full ARR->EW merge.
