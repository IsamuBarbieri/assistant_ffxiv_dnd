# PM — PROJECT MEMORY (dev-only: how this project works and why)

Version mv2

> **THIS FILE IS NOT PLAY KNOWLEDGE AND IS NOT UPLOADED ANYWHERE.** It is dev-only, like `CHANGELOG.md`, and
> its reader is whoever picks the project up cold — a fresh assistant session in this repo, or the GM months
> from now. It must NEVER be uploaded to the Campaign, One-Shot or Loremonger assistants.
> *(An earlier plan made this the knowledge of a fourth "Maintainer" assistant with its own instructions file.
> The GM retired that idea: no fourth assistant exists, `Instructions_Maintainer.txt` was deleted, and this file
> serves the cold-start need directly.)*
>
> **QUARANTINE RULE (binding, read before anything else):** this file records the project's HISTORY, and that
> history contains commands, rules and file names that NO LONGER EXIST. Every one of them is tagged
> `RITIRATO`. A name appearing in this file is **archive material, never a capability of the system**. The live
> command roster is the one in `Instructions_Campaign.txt` / `_OneShot` / `_Loremonger` and nowhere else —
> if this file and an instruction file disagree about what exists, the instruction file is right and this file
> is describing the past.

---

# PART 1 — ARCHITECTURE (evergreen: what the system is and how it works)

## 1.1 What this project is
An FFXIV × D&D 5e homebrew campaign assistant. The GM is human; the assistant works behind the scenes and
never speaks to the players. Instructions and knowledge in ENGLISH, output in ITALIAN. Campaign arc =
A Realm Reborn → Endwalker (Dawntrail excluded from the CAMPAIGN only; DT names and player options exist).

**Three assistants, one knowledge set:**

| Assistant | Instructions file | Role |
|---|---|---|
| Campaign | `Instructions_Campaign.txt` (cvNN) | runs the MSQ campaign |
| One-Shot | `Instructions_OneShot.txt` (ovNN) | builds and runs self-contained modules in ACTS |
| Loremonger | `Instructions_Loremonger.txt` (lvNN) | read-only lore, stat blocks, utilities |

## 1.1b THE PROJECT IS HOST-AGNOSTIC (binding design constraint)
The system runs **equivalently on any host** that offers a custom-instructions box plus file-backed retrieval.
No knowledge file and no instruction file may name a vendor, a product or a UI. The assistants are generic.
This is not tidiness: a rule written against one host's behaviour becomes wrong the moment the same corpus is
run on another, and this project has already paid for that once (the media rules once carried "renders
clickable in <host>" as their justification).

**The two host differences that actually exist, and how each is handled:**
- **The tracker panel.** Some hosts render the emitted HTML into a side panel automatically; on others the GM
  selects it manually. **Not automatable from our side** — it is host UI, not output. The emission is identical
  either way, so 06 §A24 forbids compensating for it (no "open the panel" instruction line, no re-emission, and
  above all no pasting the roster as chat text as a fallback).
- **Media links.** Every image/map/OST reference is a plain SEARCH link the GM clicks — never an embedded or
  tool-fetched result. This was once a per-host override; it is now the unconditional rule in 06 §A4/§A23,
  which is why the three `PLATFORM OVERRIDE` blocks were deleted from the instruction files (they had become
  no-ops occupying always-on context).

## 1.1c THE THREE INSTRUCTION FILES ARE EDITED TOGETHER (binding, GM decision 2026-07-27)
A change that touches a rule the assistants SHARE is applied to **all three files in the same pass**, and where
the rule is the same **the text is identical word for word** — not merely equivalent. This is not tidiness:

- **Divergence is invisible and permanent.** The three files are never read side by side, so a rule updated in
  `cv` and left stale in `ov` produces a defect that only shows up in a One-Shot session weeks later, with no
  signal pointing at the cause. Every drift this project has recorded started as "I'll do the other two later".
- **Identical text makes the next change mechanical.** A shared rule that reads the same everywhere is a
  find-and-replace; three paraphrases of the same rule are three rewrites that drift a little further apart
  each time. The stat-block row proved it: it sat at 1,421 B in `ov` and `lv` — the exact pre-strip `cv`
  version — for as long as it took someone to look.
- **The exception is real and narrow:** what genuinely DIFFERS per assistant stays different, and should say so
  explicitly. `/tracker` scope is the model — one artifact, three scopes (campaign = last beat · one-shot =
  whole module · loremonger = last statted encounter), each stated in its own file next to the shared emission
  rule.
- **Verification is part of the edit, not a later pass:** after touching any shared rule, grep the changed
  string across all three files. Do it BY STRING, never by section (LESSON 2.11).

## 1.1d THE TEST MATRIX — which models run what, and what the FLOOR is
Recorded because every optimisation decision is relative to it: a rule is "good enough" only if it holds at the
floor **of the assistant it belongs to**. GM-observed ordering, weakest first:

| Model | Reasoning setting | Runs |
|---|---|---|
| Haiku 4.5 | Esteso | Loremonger |
| Gemini 3.5 Flash-lite | Esteso | Loremonger |
| **Gemini 3.6 Flash** | Esteso | **everything — this is the campaign's floor** |
| Sonnet 5 | Alto | everything |
| Opus 5 | Medio | everything |

**THE FLOOR IS NOT THE SAME FOR EVERY ASSISTANT, and this is the non-obvious part.** The Campaign's floor is
Gemini 3.6 Flash; **Loremonger's floor is two tiers lower.** So a Loremonger-specific rule has to survive a
weaker model than a campaign rule does — counterintuitive, since Loremonger looks like the simpler assistant,
but it follows from the workload: lookups and stat blocks tolerate a small model, a long narrative beat with a
manifest, an OST cadence and a footer does not. Gemini 3.5 Flash-lite was tried on a campaign dungeon and
**dropped Lahabrea and other pinned content** — a clean demonstration of the boundary, not a defect to patch
(LESSON 2.14(c)).

**The reasoning setting is part of the configuration, not incidental.** The ordering above compares models at
the settings actually used (Opus at Medio sits above Sonnet at Alto), so a comparison run at a different
setting is not comparable. Record the setting whenever a test result is recorded.

**MEASURED, 2026-07-27 — what the reasoning setting actually costs when it is OFF.** Same work (the Toto-Rak
encounter package) run on Gemini 3.6 Flash with and without extended reasoning:

| | Esteso | Non esteso |
|---|---|---|
| HP / damage arithmetic | **7 of 7 correct** | **2 errors of 8** — Coeurl 52 declared vs 59 computed, Acaro 9 vs 7 |
| Dice | all real | **`1d7`**, which does not exist in 5e |
| Map footprints | Titan 3×3 exact | wrong on 2 maps of 3 |
| Language | clean | «*repetir*» for «ripetere» |

**These are SILENT faults** — a boss at 52 HP instead of 59 is not noticed as a wrong number, it is noticed as
a fight that ended early. Honest limit: **one run per configuration**, so this is an indication, not a
measurement; the project's own discipline says a single observation is variance. It did NOT change the floor —
the GM's decision is that the floor is Gemini 3.6 Flash, and rules must hold there **without** leaning on
reasoning to rescue them. That is precisely why every check added in 06 v4.94 is a COUNT: a condition you can
count does not need reasoning to pass.

**Ordering caveat, stated honestly:** the sequence is the GM's own observation on THIS workload, and that is
the only ranking that matters here — published tier names would put a full small model above a "lite" variant,
which is not what was observed. Do not "correct" it from generic benchmarks.

## 1.2 The two layers — this is the single most important structural fact
- **CONTROL layer** = the host's custom-instructions box. **100% in context on EVERY turn.** This is the
  ONLY guaranteed-present surface, so anything that must fire on EVERY beat (command contract, prose register,
  high-frequency name bindings) lives HERE. Everything looked up only when relevant stays in the knowledge
  files.
- **DATA layer** = knowledge files 01-08, **RAG chunk-retrieved** — only a fraction is in context at a time.
  CONFIRMED from the host's own UI (a retrieval-mode indicator, active at ~20% capacity): the host runs
  retrieval here, not full context, and **there is no toggle to force full context**. The threshold appears to
  key on file COUNT rather than token size. Assume retrieval on any host; it is the pessimistic case and the
  one every rule is written against.

**Consequence, and the dominant risk class in this architecture:** the instruction files WIN over the knowledge
files wherever they differ. A rule changed in 06 but left stale in cv does not merely disagree — it is
overridden, silently, with an intermittent symptom (the model condenses sometimes and not others, depending on
what RAG pulled). Every change that touches behaviour must check cv/ov/lv, not only the `.md`.

**Consequence 2:** a rule that must fire every turn cannot live only in a knowledge file. This was proved by
the 07 naming failure (LESSON 2.4).

## 1.3 The command model
A **SINGLE COMMAND EXECUTOR**: the GM types ONE slash command per turn; the assistant runs exactly that one and
stops. No state of its own — the ONLY persistence is the plain-text `=== SAVE ===` block written on `/salva`.

- **The `/` is a CHANNEL SEPARATOR, not decoration.** It distinguishes an out-of-fiction instruction from
  narration ("il gruppo continua verso il fondo" vs `/continua`). This ambiguity exists regardless of model
  capability, which is why the slash survived the platform move.
- **ONE NAME PER ACTION, NO ALIASES.** One spelling per command. Nothing to recognise, no "which one did they
  type" branch.
- **THE ROSTER IS CLOSED**, and is stated as a closed list — **never** as a list of what was removed. See
  LESSON 2.9.
- **END OF SESSION IS TWO COMMANDS, and the split IS the safety mechanism:** `/fine sessione` (READ-ONLY recap
  + delta gate) then `/salva` (writes). The read command *cannot* write because the write command has not been
  typed yet — the invariant is enforced by vocabulary instead of by teeth.
- **LOAD HAS NO COMMAND.** A `=== SAVE ===` block in the GM's CURRENT message is itself the trigger: the marker
  cannot occur in narration, so it does exactly the job the `/` does for everything else.

## 1.4 Language convention (binding)
Instructions AND knowledge are ENGLISH; only OUTPUT and COMMAND WORDS are Italian. Literal Italian output
strings (`Ancora save:`, `Da leggere ai PG`, markers, one-line GM redirects) stay Italian because they ARE
output.

**Do NOT translate the corpus to improve the Italian.** Most of it is DATA (stat blocks, indexes, tables) whose
language does not affect narration, and the canonical FFXIV names must stay English or §A14's wiki verification
breaks. The lever for prose is EXEMPLARS, not language (LESSON 2.4).

## 1.5 Versioning and delivery
- **Independent versioning:** each file bumps on its own; the version lives in its own header. Knowledge =
  MAJOR.MINOR (06 v4.x / 07 v1.x / 08 v3.x); control layer = cvNN / ovNN / lvNN / mvNN.
- **`CHANGELOG.md` is dev-only and never uploaded.** Version history lives there, never in a file tail.
- **Git does NOT deploy.** A knowledge change ships the changed `.md` for MANUAL re-upload; a control change is
  pasted into the host's instructions box by hand.
- **VERIFY THE DEPLOYED VERSION BEFORE TRUSTING A TEST.** Two whole test cycles were misread this way
  (LESSON 2.5).

## 1.6 File map (8 knowledge files, 01-08)
| File | Role |
|---|---|
| `01_Races` | PC race build data (8 playable + Garlean + beast tribes) + Role Action Feats |
| `02_Classes` | the 22 Jobs: progression, subclasses, resources, artes |
| `03_Spells` | spell lists by Job + homebrew spells (metric) |
| `04_Bestiary` | monsters by creature class → genus → species + Primals |
| `05_Campaign` | campaign RULES only — Section A, Ch.1-20 (Echo, Blessing, Limit Break, combat, save spec) |
| `06_Procedures_and_Format` | the assistant's operational formats + shared rules (Parts A-E) — the how-it-behaves layer |
| `07_Glossary` | the SINGLE naming source: method + parenthesis test + element map + bindings |
| `08_MSQ_Flow` | the MSQ FLOW (PURE DATA): 08.1 roadmap + manifests + REVAMPED-DUTY LOCKs; 08.2-08.6 ordered index ARR→EW; 08.OST-* duty OST + 08.OST-SCENE-* mood OST |

`00_Manual_Index` — **RITIRATO** (audit lotto B1). It was routing, which does nothing in a RAG pipeline, plus
content that already existed elsewhere. Do not recreate it.

Dev-only, never uploaded to a PLAY project: `CHANGELOG.md`, `AUDIT_REPORT.md`, this file, `combat_tracker.html`
(the browser-openable copy of the §A24.1 template — **06 §A24.1 is authoritative; the direction is always
HTML → 06**, and the two must be diff-checked on every touch).

## 1.7 Structural model #1 — the MSQ flow lives in 08, 05 is RULES only
- **08.1** = Roadmap ARR→EW + the CANONICAL CUTSCENE & REVEAL MANIFESTS (5 arcs + the Crystal Tower 6th) + the
  ARR REVAMPED-DUTY LOCK. **08 is PURE DATA**: all flow BEHAVIOUR lives in 06 + the instructions; a flow tweak
  never edits 08.
- **08.2-08.6** = the ordered MSQ index (giver + step spine + [duty] + single resolved Next), authoritative over
  model memory for order and next-step. **What is actually cached, be precise:** for every quest, the ORDER,
  the NAME and the resolved Next; the GIVER and the STEP SPINE only on the minority of entries that show them.
  A live fetch is the NORMAL path for step spine + dialogue.
- **08.OST-*** = duty OST tables; **08.OST-SCENE-*** = city (day+night) / zone / scene-madri mood themes.
- **CRYSTAL TOWER = INLINE MANDATORY MSQ FLOW** (no side gate): seeded at 'Laying the Foundation' (2.1,
  hard-locked, no pull-forward), played as a fixed ~13-beat arc after 'Build on the Stone', exit to 2.2 'Still
  Waters'. Labyrinth alliance-gates = NON-COMBAT enigmas; no mid-arc exit. Sets up the ShB Exarch reveal
  (GATED).
- **CONDENSATION** (06 §B2): the 08 index pins `[COND]` markers on every condensable quest (542). They do NOT
  trigger anything — they DEFINE the extent of a connective run: start, stop, contents. `/continua` ALWAYS
  plays the next quest as a normal beat, marked or not; **`/riassumi` is the ONLY trigger of a bridge**.
  One vignette per condensed quest, counted. Guardrail: `/riassumi` never compresses a pillar, an instanced
  duty, or a manifest-pinned cutscene.

## 1.8 Structural model #2 — the LEAN save
- **[A] POSIZIONE MSQ** = current quest (EN) + last COMPLETED step (resume anchor; the NEXT step is DERIVED from
  the wiki, never stored). Mission = the owning QUEST, never a duty name, never the just-'apre' quest.
- **[B] PARTY** = N PG + livello (table-owned, copied VERBATIM, never derived or "corrected").
- **[C] SUBQUEST ATTIVA** = exactly ONE (or 'nessuna'), with its STATE (ATTIVA/SOSPESA).
- **Sessione: N** = a dedicated integer (table-owned, copied verbatim, +1 only when beats were played).
- Reveals, NPC reputations, world-state, Crystals/Blessing and Aetherytes are **NOT** save fields — all derived
  live from the MSQ position + the internal reveal gates (05 Ch.1). There is no [D]-[G].
- **PER-BEAT SCALING LINE** `⚔️ Rif. gruppo: N PG · Lv L` closes every beat: party size and level at the point of
  use, for §B11 scaling and per-PC loot. It carries NO save vocabulary so it can never read as a save.

## 1.9 Canon model — Echo vs Blessing vs Tempering (do NOT regress)
- **THE ECHO** = innate, NEVER-removed immunity to TEMPERING, in ANY arc.
- **THE BLESSING** (6 crystals) = permanently SHATTERS Ascians + wards against aetherial corruption. NOT
  tempering immunity, NOT absolute.
- Midgardsormr seals ONLY the Blessing (end of ARR). **There is no tempering-wipe mechanic** — never invent a
  check by which a PC becomes Tempered.
- **ARR REVAMPED-DUTY LOCK:** Toto-Rak = terminals, sole boss GRAFFIAS; Castrum = Black Eft → Magitek Vanguard
  F-1 → Livia; Praetorium = ride → Mark II Colossus → Nero → Gaius; Ultima Weapon = its own trial Porta
  Decumana; Cape Westwind & Steps of Faith = solo instances.

## 1.10 Encounter, economy and loot in one screen
- **TIERS:** BOSS = CR party level EXACTLY (difficulty from mechanics + phase longevity; offense in band).
  MID-BOSS = CR level −2. MSQ STORY MOB = lore-first GdS, easy, only outside duties. RETREATING VILLAIN = easy
  skirmish (may return later as a CR-party boss in its own duty).
- **DUNGEON:** no trash; statted encounters = exactly the wiki roster; a short playable interlude between EVERY
  pair of fights, ≥1 a tangible puzzle; FIRST-FIGHT-FIRST; roster pinned at entry; SPLIT-NEVER-SHRINK.
- **ECONOMY = 5e-2014 rarity ladder by party level**; each special = a real 5e item of that rarity or an
  on-theme reskin; price + FULL EFFECT printed per item.
- **LOOT RESOLVE-AND-PRINT:** the assistant ROLLS and prints the concrete result, never the dice formula.
  Loot is never omitted and never empty.

---

# PART 2 — LESSONS (the durable why, detached from its dates)

## 2.1 THE CORE LESSON — distinguish a problem you own from a property of a closed product
For ~40 versions an end-of-session command PLAYED A BEAT instead of running the save gate. Four theories were
chased; **the first three were all wrong** and are recorded so none is chased again:

1. **The PER-BEAT ANCHOR** (reprinting save vocabulary every beat). Failed.
2. **The command LEXEME** (neutral markers → retire the word → rename it → strict single word + guard). Failed
   identically: even an unambiguous HALT word, typed right after one beat, ran as the next beat.
3. **THE DIET THESIS — total always-on context load past a threshold. FALSIFIED BY DIRECT MEASUREMENT and
   RETIRED.** The measurement that killed it: the known-good build is **42,050 B** and the broken one is
   **41,885 B** — *the working version is bigger*. **Size was never the variable. Do NOT resurrect "cut bytes
   until commands work."**
4. **THE ACTUAL ANSWER: the host.** The final test on the host of the time — with the most instrumented
   instruction layer the project ever had — failed three commands out of five, and one emitted **raw tool-call
   JSON of search queries** into the output, twice, byte-identical. That is not prose gone wrong: it means the
   instruction layer was not being read at that point at all. **No prompt can reach that.** The same commands,
   on the same knowledge, worked FIRST TRY and repeatedly once the corpus was moved.

**THE GENERALISABLE LESSON:** prose quality is tractable (exemplars measurably moved it in one iteration); a
host that bypasses its own instruction layer is not. Ten fix attempts against an intractable problem is the real
cost recorded here.

**WHAT DID HELP, AND STILL DOES:**
- **(a) SEMANTIC ACCURACY IN COMMAND NAMES.** The worst offender was a generic halt word — "stop WHAT?" — and
  its genericness plausibly fed its own unreliability. Every command now names exactly what it does.
- **(b) THE READ/WRITE SPLIT.** `/fine sessione` cannot write because `/salva` has not been typed yet.
- **(c) RECONCILING CONTRADICTIONS.** §B17 and §B24 each simultaneously banned a trigger and gave a full
  procedure for it; a model retrieving either found "reject X" and "on X, do the full thing" at once.
  **Prefer these three over adding emphasis.**

## 2.2 Before acting on a defect report, ask WHICH LAYER produced the behaviour
Of one 18-item fix brief, 14 items were good and **three of the four rejected shared one root: they diagnosed as
MODEL failures things where the model had faithfully obeyed the DATA.** A name reported as "gated until later,
confirmed 100%" was in fact spoken in the quest dialogue and correctly pinned in 08.1 — applying the fix would
have deleted canon and corrupted a correct manifest. If the manifest ordered it, patching 06 or the instructions
leaves the defect in place; the fix belongs in 08.

**And: "wiki-verified" is a claim, not evidence.** Two documents in this corpus both claimed verification for
opposite facts, and one was wrong.

## 2.3 A pinned plot does not license its staging
Related to 2.2, and now a rule (06 §A6). A canonical plot being pinned does NOT authorise inventing the scene
around it: the Garlean plot to make the sylphs summon Ramuh IS canon, but "decine di sylph appesi in bozzoli"
and "undici sylph liberati" were invented — canon has the party find one sylph, alone and unharmed. The plot was
right; the scene was fabricated.

## 2.4 STYLE BY EXEMPLAR, NOT BY INSTRUCTION
The question was whether to translate the whole corpus into Italian to fix weak Italian prose. Answer: no
(see 1.4). The real lever is **exemplars**: the instructions were all META ("write vivid Italian") — instructions
ABOUT writing, never examples OF it. For STYLE, showing beats telling.

06 §A1 carries GM-approved samples plus **what makes them work**, distilled into generalisable rules: verbs
carry the image, never generic 'c'è'/'appare'; adjectives CONCRETE not evaluative; comparisons physical; one
main image per sentence; every 'Da leggere ai PG' ENDS ON THE OBSTACLE; NPCs have an idiolect.

**METHOD NOTE, generalises:** the prose fixes that work name a CONCRETE FAILURE SHAPE or show a CONCRETE SUCCESS
SHAPE. Vague quality asks have never moved the output. Keep feeding real flagged sentences, good and bad.

**The name-binding corollary:** exemplars fixed the register in one iteration, but the SAME run violated three
binding 07 renderings. **Mechanism:** `07_Glossary` is RAG-retrieved and is NOT retrieved on a narrative beat,
so the model never consults it and coins names ad hoc — pretty, wrong, and different every session. "If the name
has a binding in 07, use it verbatim" is unreachable if 07 is never opened. **Fix:** the high-frequency bindings
live in the ALWAYS-ON layer. Good prose and correct naming are independent failure modes.

**Two self-inflicted traps found here, both now rules in §A1:**
- The default repair for an invented idiom is **DELETION, not substitution** — the urge to close a farewell with
  SOMETHING is the bug.
- **CONCRETE ≠ PLAUSIBLE-SOUNDING.** The replacement line written INTO §A1 as the exemplar of the fix was itself
  meaningless against what the scene had staged. *Writing a failure shape while codifying the rule against it is
  a real hazard — verify exemplars against the fiction before committing them.*

## 2.5 Verify the deployed version before drawing ANY conclusion from a test
The deployed instructions were **cv2** while the working copy was at **cv7** — the upload had not been
saved. Name resolution, the euphony gate, the high-frequency bindings and the self-revision pass were ABSENT
from the tests that "failed" on naming. The model did not ignore those rules; it never had them.

## 2.6 A format rule must name its atoms
§B6 said "normal text with bold" but never specified WHERE the bold goes or that entries need separation — so
the model emitted a flat wall that satisfied every rule as written. Later, "separate short lines" did not say
WHICH categories may share a line, so three defensive categories were chained onto one. **A rule that names an
allowed device without specifying its placement is not a format rule.** The same principle is why a schema beats
prose in the instructions: a fixed field makes an OMISSION VISIBLE.

## 2.7 Before demoting an always-on rule to RAG, grep for it
When the always-on checklist was stripped (−36%), every item was first verified to have a home in the RAG. **One
did not** — "never invent a post-duty setpiece" existed ONLY in the instructions, although this very log claimed
it had been added to a knowledge file. **A handoff claim that a rule "was added" is not evidence it was added
there.**

**And the risk asymmetry, which is the reusable part:** stripped anti-slip rules fail **LOUDLY** (a command
visibly does the wrong thing). A stripped content CHECKLIST fails **SILENTLY** — if the model omits a pinned
cutscene, the beat still reads perfectly, and the only way to notice is auditing the transcript against 08.
So "the rerun looked fine" is NOT evidence a checklist was dead weight; it is the expected appearance of a
content-omission failure.

## 2.8 A rule removed to test a hypothesis, where the test failed, has no surviving justification
The per-beat party line was deleted as TEST 1 of the command-slip hunt. The test failed, the whole hypothesis
family was later falsified by measurement, and the platform cause no longer applies — but the line stayed
deleted by inertia for many versions. **Restore it explicitly rather than leaving it retired by inertia**, and
leave an inline history note so it is not re-litigated a third time.

## 2.9 Naming a retired command feeds it back through retrieval
Observed twice in live tests: a command retired in an earlier version was still executed in full, reconstructed
from training memory, after every roster had dropped it. **A retired command does not stop existing for the model
just because the files stopped listing it.** Hence the roster is stated as CLOSED and never as a list of what was
removed — *including in the negative* ("there is no /X command"), because retrieval does not distinguish
"X does not exist" from "X". Three such negations survived in 06 and cv until the audit found them (lotto B3).

## 2.10 Never put a per-name verdict in the always-on layer
A naming gate carried two worked examples and BOTH said keep-the-English, so the only concrete naming behaviour
modelled in the always-on layer was "keep it" — and three transparent names went untranslated. **A verdict that
specific belongs in the RAG.** Translate everything that plausibly renders: the '(English)' parenthesis is the
safety net that makes an imperfect Italian name cheap and an untranslated one a silent loss. (Note: the
HIGH-FREQUENCY BINDINGS list is *not* what this targets — it is a lookup table for names recurring every beat,
a proven fix, not a per-name exception encoded as an example.)

## 2.11 A thing removed where it is DEFINED survives where it is merely REFERENCED
**Sweep by string, never by section — and the sweep must cover `cv/ov/lv`, not only the `.md` files.**
Three recorded instances, which is what makes this a rule rather than an anecdote: an alias killed in the
section that defined a command survived in the sections that referenced it; three retired commands survived as
NEGATIONS ("there is no /X") long after the roster dropped them; and `00 → index` survived in **all three**
instruction files after `00` was deleted — in a batch whose own written verification said to check `cv/ov/lv`,
where only the `.md` files were actually checked.
The pattern is always the same: the deletion is done where the thing LIVES, and the mind moves on before
reaching the places that merely POINT at it.

## 2.12 When reported symptoms do not match the artefact you were handed, check the artefact first
A test transcript was once pasted OVER the control-layer file, destroying it on disk. It was caught because five
of eight flagged defects had no counterpart in the file the GM pointed at. The morning's commit made it
recoverable. **Check whether you are looking at the right artefact before theorising about the symptoms.**

## 2.13 The marker/rule co-location principle
A rule must be retrievable together with what it governs. When two consumers can be retrieved separately,
duplicating a compact statement is justified. Corollary — **one rule per retrievable unit**: a long paragraph
holding five binding rules gets split, because a chunk boundary can cut a rule from its trigger. Audit lotto B2
found 18 lines in 06 that were *larger than a chunk* (max 5145 chars) and split them; the file grew 0.4% and the
partial-retrieval exposure went to zero.

**IT APPLIES TO DATA ROWS JUST AS MUCH AS TO RULES — three instances found in one pass, all in 08:**
- a DUTY's OST row gave one unlabelled track (the ambient) while battle/mid-boss/final sat in a separate
  preamble line, so a dungeon played its ambient over the boss;
- a ZONE's row gave only the ambient while the region's battle theme was named nowhere in the data at all, so
  an open-world fight came out silent;
- **172 pinned cutscenes named no track**, while the mood themes that govern them sat 660 lines away — which is
  why the first named Ascian of the campaign played over dungeon ambience.

**A FOURTH instance, found the same day and different in kind — a rule that GATHERS data for a rule that never
reads it.** §B10's TRIAL LORE-FIDELITY CHECKLIST obliges you to establish from the wiki «the arena — its real
look AND its real instant-death / hazard». §B8 draws the arena and never referenced that item, so three
collaudo maps came out with **zero hazard cells** despite the hazard being mandatory to look up. The other
three instances were a row missing its own label; this one is **a producer and a consumer in different
sections, neither naming the other**. Check for it whenever a new rule CONSUMES something an existing rule
already establishes: the fix is a reciprocal pointer, one line on each side, so the link survives partial
retrieval from either direction.

**The generalisation worth keeping: a data row must carry everything its consumer needs to act on it, because
the consumer will use only what the row happens to say.** A default living in a preamble is not a default; it
is a second retrieval that may not happen. When a set is too big to inline everywhere, put the mapping in the
nearest enclosing HEADER (the manifest fix used six insertions instead of 111 inline tags).

## 2.14 Three failure categories — do not spend rules on the third
- **(a)** Absent or ambiguous rule → fix the rule.
- **(b)** Right rule in the wrong FORM → fix with a template + a testable self-check, never by repeating the ban.
- **(c)** Capability limit at the floor model → do not spend rules. The GM tests deliberately on the weakest
  model available, as a floor; a failure there that the strong model does not reproduce is category (c).
  **Check the matrix first (§1.1d): the floor differs per assistant**, so a Loremonger failure may be category
  (c) at a tier where the same behaviour would be a real defect in the Campaign.

**And a falsification worth keeping:** a prose defect was once attributed to a weak model and declared a
"model gap". Wrong — the narrative beats had run on the *strongest* model. **Prose defects here are
PROMPT-layer, not model-capability; do not reach for a model upgrade as the fix.**

## 2.15 Optimising for the FLOOR model — what actually moved, and what did not
The GM tests on the weakest available model deliberately, because what holds there holds everywhere. A pass
built on published guidance for that model family produced a clear split, and the split is the lesson.

**WHAT WORKED:**
- **One structural form for one kind of object.** 06 was using SIX line shapes for the same thing — a binding
  rule that already had a name. Normalising 181 lines to a single shape is free (verified: zero words added,
  zero lost) and gives an unambiguous instruction/data boundary. It also makes an OMISSION visible, which is
  the same reason §B6's layout rule only started working once it named its atoms (LESSON 2.6).
- **Shrinking the always-on layer, MEASURED not assumed.** Every candidate row was grep-verified to exist in 06
  BEFORE removal. cv 27.2 → 21.7 KB, ov −10%, lv −5.5%. The table checklist came through the strip intact,
  including the two items a previous strip had lost.

**WHAT REFUTED ITS OWN PREMISE — and this is now the more useful half:**
- The guidance says open-ended negatives ("do not guess") make the model over-index and fail basic logic. 06
  has 73 of them, which looked like a large finding. Read one by one, **the large majority were already
  sourcing rules** — "the creature's TYPE comes from its wiki entry, NEVER inferred from its name" — with the
  positive form one clause away. Rewriting them wholesale would have spent risk on a problem the corpus did
  not have.
- The same shape had already appeared: 65 failure-shape exemplars looked like fat, and 53 were load-bearing;
  the instruction files looked duplicated, and measured 3-5% textual overlap.

**THE METHOD NOTE THAT GENERALISES: measure the FORM, do not count the OCCURRENCES.** Three audit axes in a
row were sized by a keyword count and all three shrank by an order of magnitude once the matches were actually
read. A count tells you where to look; it never tells you what is there.

**AND THE ONE PLACE THE TWO GOALS CONFLICT:** stripping the always-on layer is a COST lever that can cost YIELD
on a weak model, because a guaranteed-present rule is worth MORE to a weak model, not less. So a strip is
tested alone, before other changes, and is the first thing rolled back if a checklist item disappears.

## 2.17 Designing a feature AROUND a known model weakness, instead of hoping
The tactical map (§B8) is the worked example, and the method generalises to any feature added from here on.
The floor model's documented weakness is **spatial reasoning**; a scale grid is the worst possible task for it.
The feature shipped anyway, because every design choice was made to REMOVE a spatial decision rather than to
add a warning:

- **A closed set of labels instead of a free number.** Seven named presets (`CUNICOLO` … `ARENA`) turn "how big
  is this room" — an estimate — into "what kind of place is this" — a classification, which the model already
  performs in prose. **This is the transferable move:** when a step needs a quantity the model is bad at,
  see whether the quantity can be reached by naming instead of measuring.
- **Read, don't derive.** The room's shape is already written in the 08 arena pins and the beat's own
  read-aloud; a creature's footprint is a table lookup from the Taglia in the stat block just written. Neither
  is computed.
- **Do the arithmetic ONCE, where it can be checked.** The `In caselle:` line converts metres to cells a single
  time, in a visible place, instead of leaving the GM (or the model) to redo it every round.
- **Aesthetics chosen for robustness.** Solid-block walls beat box-drawing characters not because they look
  better but because every wall cell is the SAME character — box-drawing needs the right junction per position,
  which is topology. No emoji, because double-width glyphs break the alignment that is the map's whole point.
- **A declared fallback that is the old behaviour.** If the self-check fails, emit the key line without the
  grid. A wrong map is worse than no map, because the GM copies it onto the mat without re-reading it.

**And the part that was NOT mine:** five of the design's best decisions came from the GM — sizing by real
shape, the scale being wrong by excess, dropping the axis labels, not drawing the PCs, and "the map is the
starting state and nothing else", which replaced a weaker rule of mine and removed a symbol. **The person who
will use the artefact at the table sees things the person writing the rule does not** — the same lesson the
combat tracker taught (ARCHIVE, cv23-cv28).

## 2.18 REPLACING A PROSE FIELD WITH A STRUCTURED ONE SILENTLY DROPS ITS GUARANTEE
The tactical map replaced the `Terreno:` prose field. `Terreno:` had one property nobody had written down:
**it could not be empty.** A field whose whole content is a description of the terrain forces the terrain to be
described. The grid that replaced it made the terrain OPTIONAL — no line of §B8 required a single feature on it
— and the collaudo returned three maps holding only `█ · _ B`: walled boxes with a monster inside.

**Why it survived every check: a bare grid is trivially consistent.** The self-check verified that every symbol
on the grid appears in the key and vice versa, which an empty grid satisfies perfectly. **A consistency check
cannot detect an absence.** Where the old field's guarantee was structural, the new one needed a COUNT — at
least one overlay, two openings, N cells per creature — and counts are what got added in v4.94.

**The move to make when replacing any field:** before shipping the new form, ask what the OLD form made
impossible, and check the new form still makes it impossible. Here the answer was "an encounter with no terrain
described", and the answer should have been found before the collaudo, not by it.

**A second contributor, and it was a wording of mine.** The verbatim rule for the round presets read «reproduce
it exactly **and then place the actors into its cells**» — it names only N/B/O/X, so it reads as permission to
add nothing else, and the model complied to the letter. **A rule that enumerates what to add also defines what
not to add.** When a template is a STARTING POINT, say so in the rule itself; "verbatim" otherwise propagates
from the shape to the contents.

## 2.19 WHEN TWO BINDING RULES COLLIDE, THE OUTPUT-FORCING ONE WINS AND THE OTHER VANISHES SILENTLY
Toto-Rak, on the floor model: the 08.1 manifest pinned '[BEFORE the boss] LAHABREA appears and NAMES HIMSELF …
then unleashes the banemite' — wiki-verified, and the **first named Ascian of the campaign**. §B1 requires
reproducing EVERY pinned cutscene. It was dropped anyway, and the AFTER-the-boss Echo vision in the same beat
was not.

**Why:** §B1's ENCOUNTER PACKAGE rule says Difficoltà and Innesco sit above the read-aloud «and NOTHING ELSE».
Taken literally that FORBIDS a pinned scene in the only place it could go. Two binding rules, and the one that
is **output-forcing and positional** beat the one that is a general obligation. The model then invented a
trigger ('the first PC to cross the threshold') to replace the canonical one the pin had supplied.

**The transferable diagnosis: a rule that dictates the SHAPE of the output outranks a rule that dictates its
CONTENT, whatever both of them say about being binding.** When adding a positional/format rule, ask what
content could legitimately need that position — and scope the exclusion explicitly. «Nothing else here» must
say *nothing else FROM THIS PACKAGE*, or it silently deletes everything else in the beat.

**Two multipliers worth remembering.** (1) **A part boundary is where content dies:** the duty was split and
part 2 opened directly on the encounter package, so the scene sat exactly on the seam. (2) **The measurement
that stopped the wrong fix:** the GM's instinct was «it isn't pinned, pin it, and probably pin others too».
Counting first showed **113 pins, only 3 with a position relative to a fight** — the pin existed and said
exactly where to go. More pinning would have changed nothing. **Count before you conclude what is missing.**

## 2.20 A SIZE THAT INCLUDES ITS OWN FRAME CAN GO NEGATIVE — check the smallest member of a scale
`CUNICOLO` was specified as '2 wide' with a rule that the `█` perimeter **counts in the stated size**. Two
cells minus two walls is **zero floor**: the preset could not be drawn. It shipped and survived two collaudi
untouched, precisely because nothing ever selected it — and `CORRIDOIO` (4 wide → 2 playable) was delivering
what `CUNICOLO` had promised, so the scale had two labels for one thing.

**The check that would have caught it takes one line: apply the frame rule to the SMALLEST entry in the scale
and see whether anything is left.** Any table where a dimension includes an overhead has this failure mode at
its bottom end, and only at its bottom end — which is exactly where it is least likely to be tested.

**The structural fix, not the arithmetic one:** the table now has **two separate columns, GRID (walls in) and
FLOOR (playable)**, so the two quantities can no longer be confused. A derived number that readers must compute
in their heads will eventually be computed wrong; print both.

## 2.21 A PROCEDURE BEATS A CHECK — and whichever one is a procedure becomes the real source
Two rules governed the tactical map's contents. «The map draws what the prose already says» was written as a
CHECK («every feature named HAS its cells»). «Pick a REGION from the table» was written as a PROCEDURE. The
model followed the procedure and ignored the check — so the region table, meant to be a *drawing vocabulary*,
silently became **the menu the contents were chosen from**, and the read-aloud three lines above stopped being
the source of anything.

**The evidence was unusually clean:** the model wrote «antiche celle in pietra … radici contorte … ragnatele
spesse come cavi d'acciaio … emerge dal fango», then drew a strip of `▒` against one wall. Another read-aloud
put «un antico pedestal gelmorriano AL CENTRO della stanza»; the map showed nothing there. **The map and the
text read to the players described two different rooms.** Nothing was missing from the model's output — the
LINK was missing.

**The transferable rule: when you want X to be the source, write X as the step that comes first, not as the
thing verified afterwards.** A check runs (at best) at the end, on output already committed; a procedure runs
during generation. If a check and a procedure disagree about where content comes from, the procedure wins every
time, and the check silently reports success on the wrong thing.

**Corollary — an EXAMPLE in a table is a rule in practice. THREE confirmed instances now, so treat it as the
default expectation, not a curiosity:** (1) the region table's only cover example read `LATO` = «colonnade,
cover down one side», and cover came out wall-adjacent **8 times out of 8**; (2) the round-silhouette rule said
«reproduce it exactly and then place THE ACTORS», and the model added actors and nothing else; (3) the
distances line's example opened with «dalla porta al boss 6», and the output dutifully measured distances
between two things both already drawn instead of converting the AoE shapes that appear nowhere on the grid.
**The prose of a rule is read; the example is copied.** Audit examples for bias the same way
you audit the rule text — and make sure the example demonstrates the case you most want, not the easiest one to
write.

## 2.22 IMPORT AN ALGORITHM'S ACCEPTANCE CRITERION, NEVER ITS PROCEDURE
The GM asked whether a known D&D map-generation algorithm could improve the maps. Two useful findings.

**(a) The famous ones solve the wrong problem.** BSP, cellular automata, drunkard's walk and Wave Function
Collapse generate FLOOR PLANS — rooms and corridors — not the furnishing of a single combat room. Name-matching
a well-known algorithm to a superficially similar task is a trap.

**(b) The right one is unrunnable, and that does not matter.** Poisson-disc (blue noise) sampling is the correct
tool for scattering features evenly without clumps, and a floor model cannot execute it. But its defining
property is a single thing — **minimum distance between features** — and that reduces to two conditions anyone
can eyeball: *no two overlays touch* and *they are not all against the same wall*.

**The generalisation: take the property the algorithm GUARANTEES and state it as a testable condition; leave the
algorithm behind.** This is the same move as everywhere else in this project — a condition you can look at or
count survives on the floor model, a computation does not.

## 2.23 AN UNCONSTRAINED DEGREE OF FREEDOM BECOMES AN ARBITRARY CONSTANT, NOT VARIETY
The map spec required two openings — «one the party comes in by, one the dungeon continues through» — and never
said WHICH ONE IS WHICH on the grid. The intuition would be that the model then varies; it does not. **Every
map of every collaudo came out entered from the top.** Left free, the model picks one option and picks it
forever, so the effect of the omission was not randomness but a silent convention nobody had chosen — and this
one put the enemies between the party and the door they had just walked through.

**The check worth running on any spec that names roles without positions:** if a rule distinguishes two things
by FUNCTION (entrance / exit, near / far, first / second), does anything say which is which in the OUTPUT? If
not, you do not have flexibility — you have an undeclared default that you will discover only by measuring.

**Related, same day:** «PCs are never drawn» had been written as a pure omission. It only became actionable when
it acquired its consequence — *keep the two rows nearest the entrance clear, because that is where the GM puts
them*. **A rule that removes something must say what fills the space**, or the space gets used by whatever else
is being placed; here it was the boss, two cells from the door.

## 2.24 WORKING NOTES LEAK INTO THE OUTPUT — and a VERBATIM template is the worst place to leave them
The round-preset silhouettes shipped with headers reading `SALA TONDA (12 × 12) — ENCLOSED, walls included,
floor 10 across`. The GM asked, correctly, whether that was for them or for the checks. It was for the checks —
and it reached them **because it sat inside a block whose entire contract is 'reproduce this exactly'.**

**The trap, stated generally: anything written inside a verbatim template is not documentation, it is output.**
A comment addressed to the model has no way to distinguish itself once the rule says to copy the block
character for character. Guidance about a template goes in the RULE AROUND IT, never in the template.

**The test to apply to every figure printed at the table:** does the reader need it, or did I need it to check
myself? Three cases came up together and they resolved differently, which is why the test is worth stating —
*a size the drawn walls already show* (cut), *'Enorme, 3×3 = 9 caselle', the same fact three times* (trimmed to
one, because the total is what §B6 means by 'the GM needs the board footprint' AND is the check's anchor), and
*a distance between two things both already on the grid* (cut: the GM counts four squares with a finger faster
than they read the sentence). **Redundancy that helps the writer verify is still clutter for the reader.**

## 2.25 A SECOND, WORSE-DEFINED VERSION OF A FEATURE IS HOW A PROJECT SHIPS TWO OF THEM
Loremonger carried `/schema <luogo>` → §D6 «textual map or map-generation prompt». §D6 was a **two-line stub
with no spec at all**, written long before the tactical map existed and never revisited. So the project had two
map features: one fully specified in §B8 and used by two assistants, one undefined and used by the third.

**Nobody would design that on purpose; it arrives by accretion, and only a full read finds it.** The fix was
not to specify §D6 — it was to DELETE the second entrance and point it at the first. The number stays as an
empty placeholder (like §A2 and §B9) because renumbering breaks cross-references.

**Search for this shape whenever a feature grows: an older, vaguer rule covering the same ground, that nobody
updated because nobody was looking at it.** The give-away is a section that is much SHORTER than its neighbours
while claiming the same scope.

**And the corollary that made it worth doing properly: when the third file joined the shared spec, the
comparison immediately exposed a drift I had introduced** — 06 had moved to `Grande, 4 caselle` while cv and ov
still said `Grande 2×2 = 4 caselle`. **Aligning a third consumer is itself a diff test on the other two.**

## 2.26 A RULE STATED FIVE TIMES AND STILL BROKEN DOES NOT NEED A SIXTH STATEMENT — IT NEEDS A SHAPE
'A puzzle is solved by the players, not by the dice' was written in FIVE binding places: §E1 principle 1,
§E1 `PUZZLE != CHECK BLOCK`, §A18's notes, §B12 `TANGIBLE-PUZZLE SALIENCE`, and §B12 `SOLUTION LINE` —
which even described the correct arrangement. The output violated all five, every time.

**All five were principles or prohibitions. The only thing in the corpus with a concrete TEMPLATE was
§A18's check block — so §A18's check block is what got emitted**, complete with slot labels that are a
ladder of RESULTS (`CD Facile (10): [base result / what it gets]`). Applied to a puzzle, 'what it gets'
*is* 'the die solves it'. **A template does not have to be the right one to win; it only has to be the
only one.**

**The rule to carry forward: repetition count is evidence about the WRONG THING.** Finding a rule
already stated five times should stop you from writing a sixth statement and send you looking for the
shape that is beating it. The fix here was a six-block output form with two countable conditions, not
another 'never'.

**Two supporting findings worth keeping.**
- **A prohibition with no alternative leaves the model on the template it can see.** §A18 said rolls do
  not solve puzzles and did not say what to use instead; adding *where the other shape lives* is the
  same co-location fix used for the encounter package's 'NOTHING ELSE'.
- **A rule can contradict itself and lose to its own concrete half.** `SOLUTION LINE` demanded a
  read-aloud of '1-3 sentences' AND that the solution be deducible from it. The size cap is concrete,
  the deducibility is not, so the cap won and the puzzle became unsolvable. **When one half of a rule is
  measurable and the other is a quality, the measurable half is the one that gets obeyed** — check every
  rule that pairs a limit with an aspiration.

## 2.27 AUDIT DONE (2026-07-27, 06 v5.02) — what it found, and what it correctly refused to do
Outcome first: **one root fix, three retirements, six pointers, two findings killed by measurement.**

**The root, and it is the reusable lesson: 'a roll gives INFORMATION, never the outcome' had been derived
INDEPENDENTLY three times** — §B20 for hooks, §E5 for mysteries, §B12/§E1 for puzzles — **and was absent
from §A18, the shared block all three route through**, whose template is a ladder of RESULTS. So every new
consumer re-invented it, and the puzzle one re-invented it wrongly for months while §B20 already had it
right. The previous day's puzzle fix was **a patch on one caller mistaken for a root fix**. §A18 now asks
the question once — *is there an outcome the players must reach themselves?* — with a one-sentence test and
the three specialisations NAMED so a fourth consumer does not re-derive them.
**Generalise: when the same principle appears in N sections, the bug is usually in the N+1th place that all
of them call.** Look for what they share before fixing any of them.

**TWO FINDINGS WERE CANCELLED BY MEASUREMENT, and that is a result, not a failure to act.**
- The six duplication clusters **do not diverge** (`boss = party level`, `mid-boss = level -2`, tiers
  10/15/20, `1,5 m` — consistent everywhere). Consolidating would have meant refactoring the cursor/save
  machinery, the most delicate part of the corpus, for a problem that does not exist.
- The fifteen 1400+ char lines are **each essentially ONE rule** carrying its rationale and failure shape
  inline; splitting would separate a rule from its reason.
**Redundancy that is CONSISTENT is not debt. Only redundancy that can drift is** — and the drift observed
that day was across FILES (06 vs cv/ov), which the verification script already catches.

**Metrics deliberately not chased** (both previously debunked): '198 prohibitions without an example' —
the trap audit F3 already dismantled, since most were already sourcing rules — and negative command naming,
cleaned up in earlier passes.

**The detector worth reusing, because it is mechanical:** orphan sections (nothing in the corpus OR the
instruction files references them → retrievable only by accident), dangling `§X` references, and phantom
sets (a rule promising 'the 12 structures' that are listed nowhere). It found 10 orphans, 1 dead reference
and 1 phantom set in a corpus that had passed several prose-reading audits. **Corto ≠ stub, though:** §C8
gives a complete format in 53 characters. The criterion is *nobody cites it*, never *it is short*.

## 2.31 "THE MODEL GOT DUMBER" IS ALMOST ALWAYS TWO RULES DRIFTING APART
Reported symptom: `/continua` re-printed the load block instead of playing, sometimes twice. Measured across
the archive: **runs 2, 3 and 4 clean; runs 5 and 6 both broken.** A regression with a date, not model decay.

**Cause: three statements of the same rule in `cv`, disagreeing on SCOPE.** The one at the top said 'when the
GM's message contains a `=== SAVE ===` block' — **no NEWEST** — so with the conversation in context it also
matched the save from two turns earlier. Two later lines said it correctly, and one of them is the EXECUTION
CONTRACT that declares it wins over everything. **The wrong one won anyway: it is first, bold, labelled
'most frequent violation', and it carries a self-check.** Position + emphasis + enforcement beat two correct
statements further down.

**Why it started firing now, and this is the part worth keeping:** the ambiguity was always there, latent.
The file grew ~2.5 KB that week and the correct statement drifted further from the ambiguous one. **What
degrades is not the model — it is the distance between two rules that were never reconciled.** Every
addition to a file lengthens the gap between rules that contradict each other, so latent ambiguities surface
as apparent 'model decay'. When a user reports things getting worse, diff the file's growth before doubting
the model.

**Second lesson, cheap and reusable: a one-directional self-check only catches the failure you imagined.**
The load gate checked 'a reply to a save must not contain a beat' and never 'a reply to a command must not
contain a load' — so it policed the direction that was working. **Write both directions when a rule separates
two modes**; the one you did not think of is the one that fails.

## 2.35 A KEY THAT NAMES AN EFFECT AND NOT A THING BREAKS THE CHAIN THE MAP EXISTS FOR
`▒ mezza copertura (+2)` is complete as mechanics and useless at the table: the GM cannot tell the players
what they are hiding behind. The map is drawn FROM the read-aloud, so the key must carry the read-aloud's
NOUN back out — `▒ detriti di pietra crollati (mezza copertura, +2)`. **Object first, effect in brackets.**

The inversion also makes two other defects visible for free: a symbol whose object you cannot name is a
symbol that should not be on the grid (the observed key listing a `▒` the grid never drew), and two rooms
of one dungeon stop coming out as the same picture, because their nouns differ even when their shapes do not.

**General form: when a rule's output loses the concrete noun that produced it, the chain from fiction to
table breaks at that point — carry the noun through, do not summarise it into its effect.**

## 2.36 A FIRST-MATCH LOOKUP FINDS THE CROSS-REFERENCE, NOT THE RULE
Twice now an automated check of mine matched the wrong line by taking the first occurrence of a key that
also appears in cross-references: once reporting a pinned scene missing because "Graffias" appeared in an
earlier `[Info GM]`, and once splicing a section where `{NOTHINGLEFT}` matched CHUNKING's pointer
"(NOTHING IS LEFT BEHIND, below)" instead of the clause — leaving the file with two CHUNKING rules and the
real rule deleted.

**A rule and its pointers share their name; that is the whole point of a pointer.** Match on the line's
SHAPE, not its content: a rule starts `- **NAME`, a pointer does not. And verify by COUNT (`exactly one
occurrence of the clause, in each file`), never by "are the copies I found identical" — that passes
trivially when a file has no copy at all, which is exactly how this survived my check.

## 2.33 THE FLOOR MODEL'S OWN DOCUMENTATION IS A MEASUREMENT WE NEVER TOOK
Seven runs of trial and error produced rules that Google's Gemini 3 guide states outright. Four of our
hard-won lessons are in it: constraints placed early get DROPPED under complexity (which is why the
`/continua` fix only held on the command row, after four correct statements at the top were ignored);
blanket negatives make the model **"fail to perform basic logic or arithmetic"** (we print `6d10+18` as 45
while carrying 1,270 negations); the model is **less verbose by default** and must be told to expand (our
"fixed output budget", 2.30); and verbose prompt engineering makes it **over-analyze**.

**The lesson is procedural: read the floor model's own docs BEFORE the next audit, not after seven
playtests.** Empirical measurement stays the arbiter — but it should be testing a hypothesis the vendor
already handed us, not rediscovering it.

## 2.34 A RULE IS LONG BECAUSE IT SAYS MUCH — MEASURE BEFORE PROMISING A CUT
I sized a 55% reduction from the average rule length (516 B) plus the observation that rules carry
rationale, and inferred that most of the bulk was argument. **I had already measured the argument: 4% of
the file.** Both numbers were mine; I let the one that suggested a big win set the target.

The rewrite landed at −27%, −22%, −13%, −10%, −9% by section, and the pattern in the low ones is the
proof: §B8 is preset tables, two verbatim silhouettes, a closed symbol set and two counted self-checks —
**all of it irreducible by construction.** Compression cannot beat content.

**Rule for the next estimate: derive the target from what is REMOVABLE (measured), never from total size
minus a hoped-for ratio.** And when the gap appears mid-job, say it then — the user can still choose a
different path while the credits are unspent.

## 2.32 TO STOP A SILENT CUT, MAKE THE LEFTOVER COUNTABLE — a debt declared is a debt paid
The fixed budget (2.30) kept eating content, and `SPLIT, NEVER SHRINK` was already binding and stated five
ways. It lost anyway, because **another rule pulled the other way: CHUNKING asked for 'the FEWEST complete
chunks'.** Between 'never condense' and 'few messages' the model found the exit that violates neither
LITERALLY — write everything, thinner. Two rules in opposite tension do not average out; the model finds the
seam between them.

**Fix in three moves, no new prohibition.** (1) **Remove the counter-pressure:** 'fewest' demoted to a
TIEBREAK among arrangements that all render at full richness. (2) **Give the shape** (2.26): OWE the beat's
items before writing · stop only AFTER a complete item, never inside one · **DECLARE what is left as a
`Restano:` line** · the next play command resumes THAT first. (3) **Make it a count** in the pre-send scan:
unwritten owed items = 0, or the residue line is present.

**The move that matters is the third.** Scaffolding survives because self-checks count it; fiction dies
because nothing does. `Restano:` is the first mechanism that makes the CUT itself countable — it does not
buy more budget, it converts an invisible loss into a visible debt the next turn must pay. **When a cap you
cannot raise is dropping content, stop legislating the content and start counting what fell off.**

## 2.30 A BEAT'S OUTPUT VOLUME IS A FIXED BUDGET — every mandatory rule you add is spent from it
Measured across six saved runs of the same dungeon: **total output is effectively constant, ~16,500
characters, whatever the rules say.** Inside that ceiling, one week of fixes grew the tactical map from 462
to 832 characters (+80%) and the enigma blocks from 2,015 to 2,988 (+48%). In the same step the narrative
prose fell by 967 — almost exactly the amount added — and a manifest-pinned Echo vision went with it. The
next run shows the same mechanism in reverse: the prose recovers and the enigma collapses instead, losing
`Soluzione` and `Indizi`.

**The model balances a fixed budget by dropping whatever is least enforced. Scaffolding has self-checks;
fiction does not. So the fiction goes, silently, every time.**

**The cost of a rule is never visible in the rule.** It shows up as something unrelated disappearing two
sections away. Before adding mandatory output, ask what it will displace — and if the answer is 'narrative
content', that content needs a count too, or a way out.

**And the correction that completes it: a check with no remedy is only an alarm.** The same morning I had
added the pin COUNT to §A9 and stopped there — a beat that counts its pins and finds them missing still has
nowhere to put them. `SPLIT, NEVER SHRINK` now lists pinned scenes as protected and names the remedy:
**if they do not fit, SPLIT the beat.** Pair every new count with the action to take when it fails.

**Method note, and it is why this was findable at all: keep the raw test outputs.** The premise under
investigation ('it worked before the cleanup') was half wrong — the pre-boss scene had NEVER appeared in six
runs, and the earlier fix had simply never been re-tested on a complete beat. Six archived extracts settled
in one query what memory would have argued about indefinitely.

## 2.29 A RULE WITH A SHAPE STILL NEEDS A COUNT — the shape survives ONE instance, the count survives all of them
The cleanest evidence this project has produced, because both halves are in the SAME output. The five-block
enigma shape shipped the day before. In the next test the **first** interlude was perfect — five blocks,
three distinct actions, all seven objects of the solution present in the player-facing text — and the
**second** had no `Soluzione (GM)` and no `Indizi` at all, with `CD Facile` reading 'cut through the knots',
i.e. the tier WAS the solution. Same spec, same turn, opposite results.

**The tactical map, given the same kind of scrutiny in the same beat, held on every point** — entrance at
the bottom, enemy deep, two doors, cover present, boss footprint correct. **The only structural difference
between them: the map has a countable self-check and the enigma had none.**

**So the ladder has three rungs, not two.** A rule needs (1) a SHAPE, or the nearest template wins
(LESSON 2.26); and (2) a COUNT, or the shape holds for the first instance and decays for the rest.
Writing the shape and stopping is a half-fix that looks complete because the first example comes out right.

**Where to put the count: §A9 already exists** as the pre-output scan, one line per failure mode pointing at
its home section. Extending it beat re-inventing a mechanism — check for the existing checklist before
adding a new one.

**And a rule requested as an absolute usually is not one — but the FIRST correction can still be too clever.**
The ask was 'mid-boss and boss are always Grande or larger'. I replaced it with a beast/humanoid split:
monsters Grande+, humanoids keep their canonical Medium. **The GM rejected that too, and was right** — FFXIV
is full of humanoid-shaped bosses that are anything but Medium (Susano, Ravana, Zodiark, an Ascian Prime),
so the taxonomy would have become a list of exceptions the moment it met real content.

**What survived is the invariant with no categories in it at all:** the Taglia is READ from the creature's
real body, exactly like its look is (§A5, §B10), and the ONE binding constraint is **internal coherence —
the Taglia and the 'Descrizione visiva' in the same block must describe the same creature.** 'Colossale
bulbo vegetale' + Media is self-refuting on its face, needs no taxonomy to detect, and is correct for cases
nobody has thought of yet.

**The reusable move: when a proposed absolute has exceptions, do not codify the exceptions — look for the
self-checking invariant underneath.** A rule that requires a category system is a rule that will need
maintenance; a coherence rule maintains itself.

## 2.28 A TOMBSTONE IS DOCUMENTATION FILED IN THE WRONG PLACE
Retired sections were kept as `§X — RITIRATA (…)` headings so their numbers stayed reserved. Measured after
five of them accumulated: **§B7, §C3, §D2 and §D6 had ZERO incoming references, and §B9's only two came
from the other tombstones.** They cited each other and nothing else cited them.

**The stated justification was a false premise.** 'Keep the number so cross-references do not break' answers
a proposal nobody made — deleting a section simply leaves a gap in the numbering, which `§A2` had already
demonstrated for months without incident. **Check that a rule's rationale answers a real alternative before
accepting it**; this one had been repeated into three separate tombstones unexamined.

**The cost was real and the benefit was already paid elsewhere:** every tombstone is a retrievable RAG chunk
that describes a REMOVED behaviour — LESSON 2.9's shape — while the history it preserves already lives in
`CHANGELOG.md`, which is dev-only and never uploaded. **History belongs in the file that is not in the
context window.** 06 went from 77 to 72 sections; the verification invariant changed with it.

**Side effect worth the note:** deleting §D6's tombstone orphaned §D8, because that tombstone was the only
thing naming it. **Removing dead weight can cut a live thing's only lifeline** — re-run the orphan check
after any deletion, not just after an addition.

## 2.27b ORIGINAL AUDIT BRIEF (kept for the shapes it names)
The GM's call after three of these surfaced in one day: **the project is probably full of binding rules that
are never obeyed**, left over from the era before the work moved into VS Code. Sweep 06 and all three
instruction files for the three shapes, which are now well characterised:

- **(a) Collision** — a rule that dictates the FORM of the output and, read literally, excludes mandatory
  content. The encounter package's 'NOTHING ELSE' deleted a manifest-pinned scene (LESSON 2.19).
- **(b) No shape** — a principle repeated in many places with nothing showing how it is done, losing to
  whatever nearby template IS concrete. The puzzle rule existed FIVE times and lost to §A18's check block
  (LESSON 2.26). **A high repetition count is the symptom, never the remedy.**
- **(c) Negative naming** — a retired command or a forbidden label named in the negative, which retrieval
  feeds back as if valid (`/carica`, `/subquest`, and once a label of my own — LESSON 2.9).

**The method that actually found them, and the reason a text-first audit missed them for months: start from
a REAL OUTPUT, measure what is missing, and only then go looking for the rule** — which turns out to exist.
Reading the rules first tells you the corpus is fine.

## 2.16 REJECTED DECISIONS — do not re-propose
- **RERANKING for RAG optimisation: NO** in this deployment. Reranking lives BETWEEN retrieval and generation
  and needs pipeline control; on a hosted assistant of this kind the host does retrieval end-to-end and
  there is no insertion point. Even granting one, it would not help: it improves PRECISION over an already
  retrieved candidate set, and the failures observed were rules that **never arrived**, not rules ranked badly.
  The queries are `/continua`, `/riassumi` — words with almost no semantic content.
- **SPLITTING 08 PER EXPANSION: NO** (GM decision). It would remove ~173 KB of never-usefully-retrievable mass
  in ARR, but costs a manual file swap at the table at every arc transition.
- **DEFERRED DEBT in condensation: NO.** The ARR MSQ is causal, so a hole spreads (no Titan aether for Ultima,
  no Blessing without all six Crystals).
- **NAMING AN AUTHOR as a style pointer: NO.** An author name is a lossy, caricatured pointer to a style; the
  GM's own approved samples ARE the style, at higher fidelity.
- **CONSOLIDATING THE FILES to drop below the RAG threshold: NO.** It might work, but full context ≈ 300K tokens
  PER MESSAGE would burn the plan in a few sessions. RAG is the right mode; its weaknesses are handled by
  layering.

---

# PART 3 — EDITING PRACTICE

**COLD-START DIRECTIVE:** every change ties to an OBSERVED failure; CLASSIFY it (compliance slip → salience at
≥2 observations, since a single slip is variance; mechanism/capability gap → root-cause fix at the FIRST);
apply it as a surgical, anchored, RAG-aware edit; RECONCILE, do not accumulate; log it in `CHANGELOG.md`.

1. **GENERAL PRINCIPLE + TEETH + ONE EXAMPLE** — never a closed enumeration (a list reads as exhaustive, so
   anything unlisted becomes inventable).
2. **POSITIVE FRAMING** (do X) over walls of prohibitions.
3. **SURGICAL, ANCHORED EDITS** — a rule lives in ONE home + at most a terse echo elsewhere.
4. **TWO FAILURE KINDS**, per the cold-start directive above.
5. **MECHANISM OVER EXHORTATION** — if a failure is data-availability, re-emit the datum NEAR the point of use.
6. **RECONCILE, DO NOT ACCUMULATE** — when a behaviour slips, find the rule pulling the other way and fix THAT.
7. **TEETH PLACEMENT** — beat-scoped FORMAT rules land fine from 06 (RAG) alone; keep instruction-layer teeth
   ONLY for cross-cutting always-on behaviours (save, flow pointers, markers, dispatch). Escalate a 06 rule into
   the instructions only if it keeps failing after a mechanism fix.
8. **RAG-AWARE FORMATTING** — chunkers split on blank lines and headers, so co-dependent rules and their
   exceptions stay adjacent, and no single line exceeds a chunk (LESSON 2.13).
9. **ASSERTED EDITS** — unique-anchor asserts; for a DATA-file dedup, verify with a fact-extractor diff (0 facts
   lost). For a form-only refactor, verify at SENTENCE level, not by n-grams: broken joins destroy shingles and
   make a textual diff meaningless.
10. **SALIENCE BUDGET & CONSOLIDATION** — observed-Nx notes are CHANGELOG, not rule. Consolidate every ~8-10
    bumps. If everything is salient, nothing is.
11. **THE FLOOR MODEL IS A FLOOR, NOT A BASELINE** — see LESSON 2.14(c).
12. **TEST PROTOCOL** — short sessions (2-4 beats; a dungeon counts double) with a save checkpoint before big
    setpieces. Tail-test the save cheaply: load → 1 beat → `/fine sessione` → `/salva`.
13. **AUDIT ALL REFERENCES ON A STRUCTURAL CHANGE** — when a shared datum changes shape, grep EVERY consumer.
14. **EVERY BEHAVIOUR CHANGE CHECKS cv/ov/lv, NOT ONLY THE `.md`** — see 1.2.

**RETIRED PRACTICES (do not reinstate):** the "context diet" budget rules (BP #15/#16 in the old numbering),
which prescribed keeping the built instruction file under a byte ceiling. **Falsified by measurement** — see
LESSON 2.1(3). Byte cost is still real; a byte *threshold for command reliability* is not.

---

# PART 4 — QUARANTINE: retired names, listed once

**Everything in this section is `RITIRATO`. None of it exists in the live system.** It is recorded here, in one
place, so the archive below can be read without ambiguity — and deliberately NOT scattered through the text.

| Retired | Replaced by |
|---|---|
| `/stop`, `/confermo` | `/fine sessione` (read-only) then `/salva` (writes) |
| `/load`, `/carica` | no command — a `=== SAVE ===` block in the CURRENT message is the trigger |
| `/gioca` | nothing: playing is the default; `/riassumi` condenses |
| `/prepara` and the campaign STUDY mode | nothing: the only persistence is the save, so a trial chat achieves the same |
| `/nota` | merged into `/esito` (scope widened to any GM-to-system fact) |
| `/subquest` | `/accettiamo` opens the slot, `/riprendi MSQ` suspends, `/riprendi SQ` resumes |
| `/riaggancio` | a MODE of `/continua` (06 §B3), not a command |
| `/torniamo alla MSQ` | `/riprendi MSQ` |
| `▶ ESEGUO <cmd>` echo line | nothing: the box executes the newest command directly |
| `09_Tracker.md` | 06 §A24 |
| `00_Manual_Index.md` | nothing: content already lived elsewhere |
| `GEM_master.json`, `GEM_Builder.html`, tplC/tplL/tplO | the three (now four) instruction files, edited directly |
| Canvas / Immersive | a self-contained HTML ARTIFACT |

**FALSE POSITIVE, do NOT "fix":** `02_Classes` contains **World Canvas**, an 18th-level class ability. It is not
a Canvas reference.

---

# PART 5 — ARCHIVE (closed cycles, oldest → newest)

## 5.1 The first host (abandoned 2026-07-21)
- **v153-v169** — chunk-contiguity refactor; CONDENSE-FIRST; no tuning labels; tier reveal-gate;
  FIRST-FIGHT-FIRST; HP hygiene; banned sidebar labels; LOAD ANCHOR ECHO; GATE ANCHOR QUOTE; SOLUTION LINE;
  HP FORMULA LOCK; LIVE DEFAULT = GIOCATO. (v169 = the known-good baseline used for every later A/B.)
- **v170-v188** — MISSION-IN-INDEX; GATE OUTPUT DISCIPLINE; Italian attack lines; NO COINED OST TITLES; SESSIONE
  FIELD; Crystal Tower inlined; [A] = QUEST-NOT-DUTY; combat cadence is MSQ-sourced.
- **v189-v202 — DISPROVEN root cause "per-beat anchor".** The command slip was fought with more teeth, then by
  repurposing the anchor. The ENGINEERING (loot, footer, save gate, scaling line) is all valid and kept; the
  ROOT-CAUSE CLAIM was wrong.
- **v203-v208 — DISPROVEN command-WORD arc.** Neutral markers → retire the word → rename it → strict single word
  + guard. It still played a beat under load. **The lexeme is not the lever.**
- **v209-v217 — the "diet" cure.** Instruction consolidation 49.5k → 42.1k, test passed — and this was read as
  confirmation of the diet thesis. It was later **falsified by direct measurement** (LESSON 2.1); what actually
  changed was that the disproven command-word arc got reverted to terse, i.e. the CONTRADICTIONS went away.
- **v218-v238 — the SLASH-COMMAND EXECUTOR.** The `/` channel introduced (v218), English-only instruction
  examples (v219), simplified to a single executor (v220); then AUTO-LOAD-ON-BARE-BLOCK and the ECHO SELF-COPY
  found by A/B against v169 and fixed; the box rewritten as a minimal router. **The final v238 test failed three
  of five commands and leaked raw tool-call JSON twice.** That ended the platform.

## 5.2 The current host
- **cv1-cv7 — pilot and prose.** All commands passed first try, repeatedly. §A1 REGISTER EXEMPLARS introduced
  and measurably worked in one iteration (LESSON 2.4). The 07 name-binding failure diagnosed and the
  high-frequency bindings hoisted into the always-on layer. Two claims of mine falsified in this window (the
  "model gap" attribution and the exemplar line that was itself meaningless) — both recorded in 2.4/2.14.
- **cv8-cv11 — the command model rebuilt.** NO ALIASES at all; end of session split into two commands; LOAD has
  no command. Two live self-contradictions found and reconciled (§B17 and §B24 each banning a trigger while
  giving its full procedure). Full host audit: 64 host-branded references removed, Canvas → Artifact, aliases
  killed, terminology cleaned across all files. Stat-block layout fixed twice (LESSON 2.6). XP printing, missing
  loot, merged Coeurl encounters and untranslated names all fixed with rules that name their atoms.
- **cv12 — the always-on layer stripped 22,987 → 14,652 B (−36%), as a deliberate calculated risk.** Verdict:
  it held, at a cost of exactly two lines (the in-beat milestone flag and a missing `[Info GM]` on a dungeon
  part), restored for ~250 bytes instead of the 4,625-byte checklist. See LESSON 2.7 for the risk asymmetry that
  makes this result readable.
- **cv13-cv22 — content and fidelity batches.** The 18-item fix brief and its audit (LESSON 2.2); the
  `[VISIONE DELL'ECO]` tag; encounter-package order; TRIAL PINS for all ~24 MSQ trials, wiki-verified; Titan
  corrected to EARTH over a chasm; revival rebalance; LB no friendly fire; §A1 prose-rule pruning.
- **cv23-cv28 — condensation and the tracker.** Deterministic MSQ condensation with 542 pinned `[COND]` markers;
  then condensation INVERTED to GM-triggered (`/continua` plays, `/riassumi` condenses) with the connective-run
  notice — the GM's design, adopted over mine, because it needs no persisted mode. Command-set cleanup
  (`/prepara`, `/nota`, `/riaggancio` retired). The `/tracker` artifact canonised as a verbatim template, first
  as file 09, then reabsorbed into 06 §A24 as a SHARED rule with three per-assistant scopes.
- **cv29 / 06 v4.86 — THE FULL-PROJECT AUDIT** (`AUDIT_REPORT.md`). Five axes measured. Results, including the
  two that refuted the audit's own premises: the instruction files do **not** duplicate 06 (3%/5%/12% textual
  overlap — they are pointers, well factored); and of 65 failure shapes in 06 only **8** failed the anti-bias
  criterion, i.e. **the prose was not fat**. Delivered: three retired-command negations removed (LESSON 2.9);
  the `/riposo` predicate fixed; `00` retired; 05's eight `Cross-references` blocks removed, two of which were
  second copies of NUMBERS; and the 18 oversized rule-lines in 06 split (LESSON 2.13). The data files 01-04 and
  07 passed every check and were left untouched.
- **cv32 / ov12 / lv11 · 06 v4.90 / 07 v1.35 / 08 v3.40 — THE FLOOR-MODEL PASS (2026-07-27).** Built on published
  guidance for the weakest model in use, and split cleanly between what worked and what refuted itself
  (LESSON 2.15). **Delivered:** the always-on layer back on a diet in all three files — cv 27.2 → 21.7 KB, ov
  −10%, lv −5.5%, every removed row grep-verified in 06 first; 06 normalised to ONE line form for a named
  binding rule (181 lines, zero words changed); and shared rules now written IDENTICALLY across the three
  instruction files (§1.1c). **Not done, deliberately:** the mass rewrite of open-ended negations — read one by
  one, they were already sourcing rules.
  **Three OST defects, all the same shape (LESSON 2.13):** a duty's row named only its ambient, so dungeons
  played the ambient over the boss; a zone's row named only its ambient and the region battle themes were
  nowhere in the data, so open-world fights came out silent; and 172 pinned cutscenes named no track at all,
  660 lines from the mood table that governs them. Fixed by completing the rows (44 duty, 29 zone) and putting
  the mood mapping in all six manifest headers. Leve/FATE themes pinned after the GM authorised Fandom for that
  one lookup — **four of the nine proposed titles were rejected**, two because they were already assigned
  elsewhere and would have leaked a Stormblood dungeon track, or a primal lead-in, into subquest fights.
  **New rule from an observed defect:** a beat ENDS at its statted encounter and never narrates past it — the
  bridge was writing "you got the cutting, the banquet is ready" after the Bottino line, handing the GM a fight
  whose result was already decided.
  **Verified on the floor model:** the strip cost nothing on the table checklist, including the two items an
  earlier strip had lost; the dungeon OST cadence came out correct after the fix.
