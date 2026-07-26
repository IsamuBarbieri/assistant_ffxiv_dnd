# 09_TRACKER — CANONICAL COMBAT-TRACKER TEMPLATE
Version v1.2 | Source: FFXIV x D&D 5e Homebrew — the single approved build of the `/tracker` artifact

> SCHEMA / USAGE (binding): this file holds the ONE approved tracker. Behaviour rules (which encounters to
> include, roster fidelity, what to pre-fill, the text fallback) live in **06 §B9** — this file is the ARTEFACT.
> If in conflict with the Instructions (06/master), the Instructions win.

## 09.0 — EMISSION RULES (binding)

- **EMIT THE TEMPLATE VERBATIM.** The block in 09.1 is the tracker. Copy it as-is. Do NOT redesign it, do NOT
  "improve" it, do NOT reorder or rename anything, do NOT drop features to save space, do NOT add a light
  theme or a theme toggle. A tracker that looks different from the last one is a FAILURE even if it works:
  the GM runs this at the table and must find the same controls in the same places every session.
- **THE ONLY THINGS THAT CHANGE ARE THE DATA**, and they are exactly three:
  1. the `<p class="subtitle">` line — name the beat (campaign) or the module (one-shot);
  2. the `encountersData` array — one object per encounter;
  3. the `statblocks` array inside each encounter.
  Everything else — every CSS rule, every HTML element, every JS function — is fixed.
- **THE EXAMPLE DATA IS A SHAPE, NOT CONTENT (binding, output-forcing — the most likely way this file is
  misused).** The `encountersData` in 09.1 shows two invented encounters with placeholder names. NONE of that
  is ever emitted. "Verbatim" covers the CSS, the HTML and the JS functions; the data block between the `DATI`
  and `FINE DATI` comment banners is REPLACED IN FULL every time. If a tracker ever ships with a name like
  `NOME NEMICO A`, or with four PC rows at a table that has three players, the block was copied instead of
  filled.
- **HOW MANY ROWS (binding, both counts are DERIVED, never assumed):**
  - **PC ROWS = the real number of players at the table.** Take it from the save's `[B] Numero PG`, or from
    what the GM said ("tracker con N PG"). NEVER default to four because the example shows four. If the count
    is genuinely unavailable, use four AND say so in one line under the artifact, so the GM can correct it.
  - **MONSTER ROWS = exactly the enemies statted in THAT encounter**, with their real AC and HP, reused
    VERBATIM from the stat block already written in chat. Never one more, never one fewer, never imported from
    another encounter or another beat, never invented. Three identical guards are three ROWS (`Guardia 1/2/3`)
    but ONE CARD in the `statblocks` panel.
- **DATA CONTRACT (binding).** Every combatant carries the same keys; what differs is what you FILL.
  `{ id, name, isMonster, initBonus, init, ac, hp, maxHp, isDown, telegraph, notes }`
  - `id` = any unique integer. `initBonus` = the DEX modifier, kept so "Resetta Scontro" can re-roll
    initiative correctly.
  - **MONSTER:** `init` PRE-ROLLED (1d20 + DEX mod), real `ac`, `hp` and `maxHp` equal and real.
  - **PC:** `init` = `""` and `ac` = `""` — the GM fills both at the table, and you do not know a PC's AC.
    `hp`/`maxHp` stay `0`: they are never rendered for a PC, because hit points are the players' to track;
    what the GM needs is the AC to roll against and the A TERRA toggle. The keys stay present only so every
    row has the same shape.
  - `isDown` ALWAYS `false`, `telegraph` ALWAYS `null`, `notes` ALWAYS `""` on creation: all three are set by
    the GM during the fight, never pre-armed by you.
- **`notes` IS TRANSIENT STATE, NOT A STAT REMINDER (binding).** It holds what CHANGES during the fight —
  conditions, concentration, timed effects. It does NOT repeat AC, HP, CR or moves: those live in the
  `statblocks` panel below the table, and duplicating them costs tokens on every single tracker.
- **STRING SAFETY (binding, output-forcing).** Every data string uses **DOUBLE QUOTES**. Italian names are full
  of apostrophes (`Custode d'Anime`, `Lame d'Ottone`, `Spada d'Acciaio`) and a single apostrophe inside a
  single-quoted JS literal breaks the whole script — the tracker then renders as a blank page. Never write
  `'Spada d\'Acciaio'`; write `"Spada d'Acciaio"`. Check every string before emitting.
- **NUMBERS ARE NUMBERS**: `initBonus`, `init`, `ac`, `hp`, `maxHp` are bare integers, never quoted strings.
  The only exceptions are a PC's `init` and `ac`, which are the empty string `""`.
- **REUSE, NEVER RECALCULATE**: AC, HP and moves come VERBATIM from the stat blocks already written in chat for
  that encounter (06 §B9). The tracker never invents a combatant and never re-rolls a stat.

## 09.1 — THE TEMPLATE

```html
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FFXIV x D&D 5e - Tracker di Combattimento</title>
  <style>
    html, body {
      background-color: #1b1d21;
      color: #e8e6e3;
      margin: 0;
      padding: 0;
      min-height: 100vh;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .container {
      max-width: 1050px;
      margin: 0 auto;
      padding: 20px;
      background-color: #1b1d21;
      color: #e8e6e3;
    }
    header {
      border-bottom: 2px solid #374151;
      padding-bottom: 15px;
      margin-bottom: 20px;
    }
    h1 {
      margin: 0 0 5px 0;
      font-size: 1.6rem;
      color: #f3f4f6;
    }
    .subtitle {
      margin: 0;
      font-size: 0.9rem;
      color: #9ca3af;
    }
    .tabs {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      border-bottom: 1px solid #374151;
      padding-bottom: 8px;
      flex-wrap: wrap;
    }
    .tab-btn {
      background-color: #272a30;
      color: #9ca3af;
      border: 1px solid #374151;
      padding: 8px 16px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.15s ease;
    }
    .tab-btn:hover {
      background-color: #32363e;
      color: #f3f4f6;
    }
    .tab-btn.active {
      background-color: #2563eb;
      color: #ffffff;
      border-color: #3b82f6;
    }
    .controls-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #23262d;
      padding: 12px 16px;
      border-radius: 8px;
      margin-bottom: 15px;
      border: 1px solid #374151;
      flex-wrap: wrap;
      gap: 10px;
    }
    .round-display {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.1rem;
      font-weight: 600;
    }
    .btn-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    button {
      background-color: #3b82f6;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 500;
      font-size: 0.88rem;
      transition: all 0.15s ease;
    }
    button:hover {
      background-color: #2563eb;
    }
    button.btn-secondary {
      background-color: #4b5563;
    }
    button.btn-secondary:hover {
      background-color: #374151;
    }
    button.btn-danger {
      background-color: #dc2626;
    }
    button.btn-danger:hover {
      background-color: #b91c1c;
    }
    button.btn-success {
      background-color: #059669;
    }
    button.btn-success:hover {
      background-color: #047857;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      background-color: #23262d;
      color: #e8e6e3;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #374151;
    }
    th {
      background-color: #141619;
      color: #9ca3af;
      padding: 10px 12px;
      text-align: left;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 2px solid #374151;
    }
    td {
      padding: 8px 12px;
      border-bottom: 1px solid #2d3139;
      vertical-align: middle;
    }

    tr.monster-row {
      background-color: #2c1a1d;
      color: #e8e6e3;
    }
    tr.monster-row:hover {
      background-color: #361e21;
    }
    tr.pc-row {
      background-color: #1a222d;
      color: #e8e6e3;
    }
    tr.pc-row:hover {
      background-color: #1f2a38;
    }
    tr.active-turn {
      outline: 2px solid #f59e0b;
      outline-offset: -2px;
    }

    /* Style riga spenta per mostro a 0 PF o PG a terra */
    tr.down {
      opacity: 0.45;
      background-color: #17181c !important;
    }
    tr.down .name-input {
      text-decoration: line-through;
      color: #9ca3af;
    }

    /* Inputs di testo e numerici */
    input[type="text"] {
      background-color: #2a2d33;
      color: #e8e6e3;
      border: 1px solid #4b5563;
      border-radius: 4px;
      padding: 6px 8px;
      font-size: 0.9rem;
      box-sizing: border-box;
    }
    input.num-input {
      width: 55px;
      text-align: center;
    }
    input.name-input {
      width: 100%;
      font-weight: 600;
    }

    .badge {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
      margin-left: 6px;
      white-space: nowrap;
    }
    .badge-monster {
      background-color: #7f1d1d;
      color: #fca5a5;
    }
    .badge-pc {
      background-color: #1e3a8a;
      color: #93c5fd;
    }

    /* Controls per PF dei Mostri */
    .hp-cell-container {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .hp-controls {
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .hp-input {
      width: 48px;
      text-align: center;
      font-weight: 600;
    }
    .dmg-group {
      display: flex;
      align-items: center;
      gap: 2px;
      margin-left: 6px;
      background-color: #1a1c22;
      padding: 2px;
      border-radius: 4px;
      border: 1px solid #374151;
    }
    .btn-step {
      background-color: #374151;
      color: #e8e6e3;
      padding: 3px 8px;
      font-size: 0.85rem;
      font-weight: 700;
      border-radius: 3px;
      line-height: 1;
    }
    .btn-step:hover {
      background-color: #4b5563;
    }
    .dmg-input {
      width: 40px !important;
      padding: 3px 4px !important;
      text-align: center;
      font-size: 0.82rem !important;
      border-color: #4b5563 !important;
    }

    .hp-bar-bg {
      width: 100%;
      height: 5px;
      background-color: #374151;
      border-radius: 3px;
      overflow: hidden;
    }
    .hp-bar-fill {
      height: 100%;
      background-color: #10b981;
      transition: width 0.2s ease, background-color 0.2s ease;
    }
    .hp-bar-fill.warning {
      background-color: #f59e0b;
    }
    .hp-bar-fill.danger {
      background-color: #ef4444;
    }

    /* Interruttore "A terra" per PG */
    .btn-down-toggle {
      background-color: #272a30;
      color: #9ca3af;
      border: 1px solid #4b5563;
      padding: 6px 12px;
      border-radius: 4px;
      font-weight: 600;
      width: 100%;
      text-align: center;
      cursor: pointer;
    }
    .btn-down-toggle.is-down {
      background-color: #7f1d1d;
      color: #fca5a5;
      border-color: #ef4444;
    }

    /* Contatore Telegrafo per Mostri */
    .teleg-wrapper {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .btn-teleg {
      background-color: #272a30;
      color: #9ca3af;
      border: 1px solid #4b5563;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .btn-teleg.active {
      background-color: #b45309;
      color: #fef3c7;
      border-color: #f59e0b;
    }
    .btn-teleg.scatta {
      background-color: #d97706;
      color: #ffffff;
      border-color: #fbbf24;
      animation: pulse 1.2s infinite alternate;
    }
    @keyframes pulse {
      0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.4); }
      100% { transform: scale(1.05); box-shadow: 0 0 8px 2px rgba(245, 158, 11, 0.8); }
    }

    .notes-cell input {
      width: 100%;
    }
    .actions-cell {
      text-align: center;
      width: 50px;
    }
    .empty-state {
      text-align: center;
      padding: 30px;
      color: #9ca3af;
    }
    .statblocks {
      margin-top: 26px;
    }
    .statblocks h2 {
      font-size: 0.85rem;
      color: #9ca3af;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid #374151;
      padding-bottom: 8px;
      margin: 0 0 14px 0;
    }
    .sb-card {
      background-color: #23262d;
      color: #e8e6e3;
      border: 1px solid #374151;
      border-left: 3px solid #7f1d1d;
      border-radius: 6px;
      padding: 12px 14px;
      margin-bottom: 10px;
    }
    .sb-name {
      font-weight: 700;
      color: #f3f4f6;
      font-size: 1rem;
      margin-bottom: 4px;
    }
    .sb-line {
      color: #9ca3af;
      font-size: 0.84rem;
      margin-bottom: 9px;
    }
    .sb-move {
      color: #e8e6e3;
      font-size: 0.88rem;
      padding: 3px 0 3px 12px;
      border-left: 2px solid #374151;
      margin-bottom: 3px;
    }
    .sb-move strong {
      color: #fca5a5;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>FFXIV × D&D 5e — Combat Tracker</h1>
      <p class="subtitle">Gestore Iniziativa &amp; Punti Vita — <em>NOME DEL BEAT O DEL MODULO</em></p>
    </header>

    <div class="tabs" id="tabsHeader"></div>

    <div class="controls-bar">
      <div class="round-display">
        <span>Round: <span id="roundCounter" style="color: #f59e0b;">1</span></span>
        <button class="btn-secondary" onclick="nextTurn()">Avanza Turno &raquo;</button>
        <button class="btn-secondary" onclick="resetRound()">Resetta Round</button>
        <button class="btn-danger" onclick="resetEncounter()">Resetta Scontro</button>
      </div>
      <div class="btn-group">
        <button onclick="addCombatant('pc')">+ Aggiungi PG</button>
        <button onclick="addCombatant('monster')">+ Aggiungi Mostro</button>
      </div>
    </div>

    <table id="trackerTable">
      <thead>
        <tr>
          <th style="width: 65px;">Iniz.</th>
          <th>Combattente</th>
          <th style="width: 65px;">CA</th>
          <th style="width: 210px;">Stato Vita (PF)</th>
          <th>Condizioni &amp; Effetti</th>
          <th style="width: 45px;">Azione</th>
        </tr>
      </thead>
      <tbody id="trackerBody"></tbody>
    </table>

    <div class="statblocks" id="statblocksPanel"></div>
  </div>

  <script>
    // ============================================================================
    // DATI — QUESTO BLOCCO SI SOSTITUISCE PER INTERO. NON copiarlo come sta.
    // Quello che segue e' un ESEMPIO DI FORMA, non contenuto da emettere.
    //   RIGHE PG      = il numero REALE di giocatori al tavolo ([B] Numero PG del
    //                   save, o quello indicato dal GM). NON quattro per default.
    //                   I PG hanno init e CA VUOTE (le scrive il GM) e non hanno
    //                   PF: i punti ferita li tengono i giocatori.
    //   RIGHE MOSTRO  = esattamente i nemici statati in QUEL scontro, coi loro
    //                   CA/PF veri. Ne' uno in piu' ne' uno in meno, mai importati
    //                   da un altro scontro, mai inventati.
    //   isDown / telegraph / notes partono sempre false / null / "": li imposta
    //   il GM durante lo scontro, mai tu.
    // Tutto il resto del file (CSS, HTML, funzioni) si emette VERBATIM.
    // ============================================================================
    const encountersData = [
      {
        id: "enc1",
        title: "NOME DEL PRIMO SCONTRO",
        round: 1,
        activeTurnIndex: 0,
        combatants: [
          { id: 101, name: "NOME NEMICO GREGARIO 1", isMonster: true, initBonus: 2, init: 18, ac: 13, hp: 22, maxHp: 22, isDown: false, telegraph: null, notes: "" },
          { id: 102, name: "NOME NEMICO CAPO", isMonster: true, initBonus: 2, init: 15, ac: 15, hp: 68, maxHp: 68, isDown: false, telegraph: null, notes: "" },
          { id: 103, name: "NOME NEMICO GREGARIO 2", isMonster: true, initBonus: 2, init: 12, ac: 13, hp: 22, maxHp: 22, isDown: false, telegraph: null, notes: "" },
          { id: 1, name: "PG 1", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 2, name: "PG 2", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 3, name: "PG 3", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 4, name: "PG 4", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" }
        ],
        statblocks: [
          {
            name: "NOME NEMICO CAPO",
            line: "CA 15 · PF 68 · Vel 9 m · TS DES +4, COS +5 · Perc. passiva 13 · GdS 3",
            moves: [
              "Multiattacco — 2 attacchi con Arma pesante",
              "Arma pesante — +5, portata 3 m, 2d8+3 perforanti",
              "Mossa telegrafata (Ric. 5-6) — telegrafo 1 round; cono 4,5 m, TS DES CD 13, 4d6 danni, meta' se supera"
            ]
          },
          {
            name: "NOME NEMICO GREGARIO",
            line: "CA 13 · PF 22 · Vel 9 m · Perc. passiva 10 · GdS 1",
            moves: [
              "Arma leggera — +4, portata 1,5 m, 1d4+2 taglienti"
            ]
          }
        ]
      },
      {
        id: "enc2",
        title: "NOME DEL SECONDO SCONTRO",
        round: 1,
        activeTurnIndex: 0,
        combatants: [
          { id: 201, name: "NOME NEMICO SOLITARIO", isMonster: true, initBonus: 1, init: 14, ac: 14, hp: 45, maxHp: 45, isDown: false, telegraph: null, notes: "" },
          { id: 1, name: "PG 1", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 2, name: "PG 2", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 3, name: "PG 3", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" },
          { id: 4, name: "PG 4", isMonster: false, initBonus: 0, init: "", ac: "", hp: 0, maxHp: 0, isDown: false, telegraph: null, notes: "" }
        ],
        statblocks: [
          {
            name: "NOME NEMICO SOLITARIO",
            line: "CA 14 · PF 45 · Vel 9 m · TS COS +4 · Perc. passiva 12 · GdS 2",
            moves: [
              "Multiattacco — 2 attacchi con Artiglio",
              "Artiglio — +4, portata 1,5 m, 1d8+2 taglienti",
              "Fase (50% PF) — a meta' dei PF cambia postura: da qui usa la mossa telegrafata ogni round"
            ]
          }
        ]
      }
    ];
    // ============================ FINE DATI =====================================

    let currentEncounterIndex = 0;

    function isCombatantDown(c) {
      return c.isMonster ? (c.hp <= 0) : !!c.isDown;
    }

    function captureRoundTelegraphs() {
      const enc = encountersData[currentEncounterIndex];
      enc.combatants.forEach((c) => {
        if (c.isMonster) {
          c.roundStartTelegraph = c.telegraph;
        }
      });
    }

    function initTracker() {
      renderTabs();
      captureRoundTelegraphs();
      renderEncounter();
    }

    function switchTab(index) {
      currentEncounterIndex = index;
      renderTabs();
      captureRoundTelegraphs();
      renderEncounter();
    }

    function renderTabs() {
      const tabsContainer = document.getElementById("tabsHeader");
      tabsContainer.innerHTML = "";
      encountersData.forEach((enc, index) => {
        const btn = document.createElement("button");
        btn.className = "tab-btn " + (index === currentEncounterIndex ? "active" : "");
        btn.textContent = enc.title;
        btn.onclick = () => switchTab(index);
        tabsContainer.appendChild(btn);
      });
    }

    function renderEncounter() {
      const enc = encountersData[currentEncounterIndex];
      document.getElementById("roundCounter").textContent = enc.round;

      const tbody = document.getElementById("trackerBody");
      tbody.innerHTML = "";

      if (enc.combatants.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="empty-state">Nessun combattente in questo scontro. Aggiungi PG o mostri con i pulsanti in alto.</td></tr>';
        renderStatblocks();
        return;
      }

      enc.combatants.forEach((c, index) => {
        const tr = document.createElement("tr");

        const isDown = isCombatantDown(c);

        tr.className = (c.isMonster ? "monster-row" : "pc-row") +
                     (index === enc.activeTurnIndex ? " active-turn" : "") +
                     (isDown ? " down" : "");

        let hpCellHtml = "";
        if (c.isMonster) {
          const hpPercent = c.maxHp > 0 ? Math.max(0, Math.min(100, (c.hp / c.maxHp) * 100)) : 0;
          let hpBarClass = "";
          if (hpPercent < 25) hpBarClass = "danger";
          else if (hpPercent < 50) hpBarClass = "warning";

          hpCellHtml = `
            <div class="hp-cell-container">
              <div class="hp-controls">
                <input type="text" inputmode="numeric" class="hp-input" value="${c.hp}" onchange="updateCombatant(${c.id}, 'hp', this.value, false)" />
                <span style="color: #9ca3af;">/</span>
                <input type="text" inputmode="numeric" class="hp-input" value="${c.maxHp}" onchange="updateCombatant(${c.id}, 'maxHp', this.value, false)" />

                <div class="dmg-group">
                  <button class="btn-step" onclick="applyDmg(${c.id}, -1)" title="Sottrai danno / −1">&#8722;</button>
                  <input type="text" inputmode="numeric" id="dmg-input-${c.id}" class="dmg-input" placeholder="dmg" onkeydown="if(event.key==='Enter') applyDmg(${c.id}, -1)" />
                  <button class="btn-step" onclick="applyDmg(${c.id}, 1)" title="Aggiungi cura / +1">+</button>
                </div>
              </div>
              <div class="hp-bar-bg">
                <div class="hp-bar-fill ${hpBarClass}" style="width: ${hpPercent}%;"></div>
              </div>
            </div>
          `;
        } else {
          hpCellHtml = `
            <button class="btn-down-toggle ${c.isDown ? 'is-down' : ''}" onclick="togglePcDown(${c.id})">
              ${c.isDown ? '💀 A terra' : 'In piedi'}
            </button>
          `;
        }

        let telegBtnHtml = "";
        if (c.isMonster) {
          let telegText = "⚠";
          let telegClass = "";
          if (c.telegraph === 1) { telegText = "⚠ 1"; telegClass = "active"; }
          else if (c.telegraph === 2) { telegText = "⚠ 2"; telegClass = "active"; }
          else if (c.telegraph === 3) { telegText = "⚠ 3"; telegClass = "active"; }
          else if (c.telegraph === 0) { telegText = "⚠ SCATTA"; telegClass = "scatta"; }

          telegBtnHtml = `<button class="btn-teleg ${telegClass}" onclick="cycleTelegraph(${c.id})" title="Contatore Telegrafo (1-3 rds)">${telegText}</button>`;
        }

        tr.innerHTML = `
          <td>
            <input type="text" inputmode="numeric" class="num-input" value="${c.init !== null && c.init !== undefined ? c.init : ''}" placeholder="-" onchange="updateCombatant(${c.id}, 'init', this.value, true)" />
          </td>
          <td>
            <div style="display: flex; align-items: center;">
              <input type="text" class="name-input" value="${escapeHtml(c.name)}" oninput="updateCombatant(${c.id}, 'name', this.value, false)" />
              <span class="badge ${c.isMonster ? 'badge-monster' : 'badge-pc'}">${c.isMonster ? 'Mostro' : 'PG'}</span>
            </div>
          </td>
          <td>
            <input type="text" inputmode="numeric" class="num-input" value="${c.ac}" onchange="updateCombatant(${c.id}, 'ac', this.value, false)" />
          </td>
          <td>
            ${hpCellHtml}
          </td>
          <td class="notes-cell">
            <div class="teleg-wrapper">
              ${telegBtnHtml}
              <input type="text" value="${escapeHtml(c.notes)}" placeholder="Condizioni, concentrazione, durata..." oninput="updateCombatant(${c.id}, 'notes', this.value, false)" />
            </div>
          </td>
          <td class="actions-cell">
            <button class="btn-danger" style="padding: 4px 8px;" onclick="removeCombatant(${c.id})" title="Rimuovi">&times;</button>
          </td>
        `;
        tbody.appendChild(tr);
      });

      renderStatblocks();
    }

    function renderStatblocks() {
      const enc = encountersData[currentEncounterIndex];
      const wrap = document.getElementById("statblocksPanel");
      wrap.innerHTML = "";
      if (!enc.statblocks || enc.statblocks.length === 0) return;

      const title = document.createElement("h2");
      title.textContent = "Riferimento rapido — mosse nemiche";
      wrap.appendChild(title);

      enc.statblocks.forEach((sb) => {
        const card = document.createElement("div");
        card.className = "sb-card";
        let html = '<div class="sb-name">' + escapeHtml(sb.name) + "</div>";
        html += '<div class="sb-line">' + escapeHtml(sb.line) + "</div>";
        (sb.moves || []).forEach((m) => {
          const sep = m.indexOf(" — ");
          const inner = sep > -1
            ? "<strong>" + escapeHtml(m.slice(0, sep)) + "</strong>" + escapeHtml(m.slice(sep))
            : escapeHtml(m);
          html += '<div class="sb-move">' + inner + "</div>";
        });
        card.innerHTML = html;
        wrap.appendChild(card);
      });
    }

    function escapeHtml(str) {
      if (!str) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }

    function applyDmg(id, sign) {
      const enc = encountersData[currentEncounterIndex];
      const c = enc.combatants.find((item) => item.id === id);
      if (!c) return;

      const dmgInput = document.getElementById("dmg-input-" + id);
      let amount = 1;

      if (dmgInput && dmgInput.value.trim() !== "") {
        const parsed = parseInt(dmgInput.value, 10);
        if (!isNaN(parsed) && parsed > 0) {
          amount = parsed;
        }
        dmgInput.value = "";
      }

      if (sign < 0) {
        c.hp = Math.max(0, c.hp - amount);
      } else {
        c.hp = c.hp + amount;
      }

      renderEncounter();
    }

    function togglePcDown(id) {
      const enc = encountersData[currentEncounterIndex];
      const c = enc.combatants.find((item) => item.id === id);
      if (!c || c.isMonster) return;

      c.isDown = !c.isDown;
      renderEncounter();
    }

    function cycleTelegraph(id) {
      const enc = encountersData[currentEncounterIndex];
      const c = enc.combatants.find((item) => item.id === id);
      if (!c || !c.isMonster) return;

      if (c.telegraph === null || c.telegraph === undefined) {
        c.telegraph = 1;
      } else if (c.telegraph === 1) {
        c.telegraph = 2;
      } else if (c.telegraph === 2) {
        c.telegraph = 3;
      } else {
        c.telegraph = null;
      }

      renderEncounter();
    }

    function updateCombatant(id, field, value, triggerSort) {
      const enc = encountersData[currentEncounterIndex];
      const c = enc.combatants.find((item) => item.id === id);
      if (!c) return;

      if (field === "init") {
        c.init = value === "" ? null : (parseInt(value, 10) || 0);
        if (triggerSort) {
          sortInitiative();
          return;
        }
      } else if (field === "hp" || field === "maxHp" || field === "ac") {
        c[field] = value === "" ? "" : (parseInt(value, 10) || 0);
        renderEncounter();
      } else {
        c[field] = value;
      }
    }

    function sortInitiative() {
      const enc = encountersData[currentEncounterIndex];
      const activeCombatant = enc.combatants[enc.activeTurnIndex];

      enc.combatants.sort((a, b) => {
        const valA = a.init !== null && a.init !== "" ? parseInt(a.init, 10) : -999;
        const valB = b.init !== null && b.init !== "" ? parseInt(b.init, 10) : -999;
        return valB - valA;
      });

      if (activeCombatant) {
        enc.activeTurnIndex = enc.combatants.indexOf(activeCombatant);
        if (enc.activeTurnIndex < 0) enc.activeTurnIndex = 0;
      }

      renderEncounter();
    }

    function nextTurn() {
      const enc = encountersData[currentEncounterIndex];
      if (enc.combatants.length === 0) return;

      const anyAlive = enc.combatants.some((c) => !isCombatantDown(c));
      if (!anyAlive) {
        enc.activeTurnIndex = 0;
        renderEncounter();
        return;
      }

      let attempts = 0;
      const total = enc.combatants.length;
      let roundChanged = false;

      do {
        enc.activeTurnIndex++;
        if (enc.activeTurnIndex >= total) {
          enc.activeTurnIndex = 0;
          enc.round++;
          roundChanged = true;
        }
        attempts++;
      } while (isCombatantDown(enc.combatants[enc.activeTurnIndex]) && attempts <= total + 2);

      const currentActive = enc.combatants[enc.activeTurnIndex];
      if (currentActive && currentActive.isMonster && currentActive.telegraph !== null && currentActive.telegraph > 0) {
        currentActive.telegraph--;
      }

      // La fotografia va scattata DOPO la scalata, non prima: se il primo in
      // ordine e' un mostro che entra nel round col telegrafo a 1, scala subito
      // a 0 (SCATTA) ed e' QUELLO lo stato d'inizio round. Fotografando prima,
      // "Resetta Round" lo riportava a 1 e lo SCATTA andava perso.
      if (roundChanged) {
        captureRoundTelegraphs();
      }

      renderEncounter();
    }

    function resetRound() {
      const enc = encountersData[currentEncounterIndex];
      if (enc.combatants.length === 0) return;

      enc.combatants.forEach((c) => {
        if (c.isMonster && c.roundStartTelegraph !== undefined) {
          c.telegraph = c.roundStartTelegraph;
        }
      });

      enc.activeTurnIndex = 0;
      let attempts = 0;
      while (isCombatantDown(enc.combatants[enc.activeTurnIndex]) && attempts < enc.combatants.length) {
        enc.activeTurnIndex++;
        attempts++;
      }
      if (enc.activeTurnIndex >= enc.combatants.length) {
        enc.activeTurnIndex = 0;
      }

      renderEncounter();
    }

    function resetEncounter() {
      const enc = encountersData[currentEncounterIndex];
      enc.round = 1;

      enc.combatants.forEach((c) => {
        if (c.isMonster) {
          c.hp = c.maxHp;
          c.telegraph = null;
          c.roundStartTelegraph = null;
          c.isDown = false;
          const bonus = c.initBonus !== undefined ? c.initBonus : 0;
          c.init = Math.floor(Math.random() * 20) + 1 + bonus;
        } else {
          c.isDown = false;
        }
      });

      sortInitiative();

      enc.activeTurnIndex = 0;
      let attempts = 0;
      while (isCombatantDown(enc.combatants[enc.activeTurnIndex]) && attempts < enc.combatants.length) {
        enc.activeTurnIndex++;
        attempts++;
      }
      if (enc.activeTurnIndex >= enc.combatants.length) {
        enc.activeTurnIndex = 0;
      }

      captureRoundTelegraphs();
      renderEncounter();
    }

    function addCombatant(type) {
      const enc = encountersData[currentEncounterIndex];
      const isMonster = type === "monster";
      const newId = Date.now();
      enc.combatants.push({
        id: newId,
        name: isMonster ? "Nuovo Mostro" : "Nuovo PG",
        isMonster: isMonster,
        initBonus: 0,
        init: isMonster ? Math.floor(Math.random() * 20) + 1 : null,
        ac: isMonster ? 10 : "",
        hp: isMonster ? 10 : 0,
        maxHp: isMonster ? 10 : 0,
        isDown: false,
        telegraph: null,
        notes: ""
      });
      renderEncounter();
    }

    function removeCombatant(id) {
      const enc = encountersData[currentEncounterIndex];
      enc.combatants = enc.combatants.filter((c) => c.id !== id);
      if (enc.activeTurnIndex >= enc.combatants.length) {
        enc.activeTurnIndex = Math.max(0, enc.combatants.length - 1);
      }
      renderEncounter();
    }

    window.onload = initTracker;
  </script>
</body>
</html>
```

## 09.2 — THE `statblocks` PANEL (binding)

The panel under the table exists for ONE reason: the GM must resolve a turn WITHOUT scrolling back up the chat
to find the stat block. Write it accordingly.

- **TELEGRAPHIC, NEVER PROSE (binding).** No narration, no lore, no "Descrizione visiva", no flavour, no
  telegraph *imagery* — those belong in the chat stat block and in the beat. Here: only what resolves a turn.
- **`line`** = the defensive one-liner, in this order and separated by ` · `:
  `CA <n> · PF <n> · Vel <n> m` then, only if the encounter actually uses them, `TS <abbrev +n>`,
  `Immunità <…>`, `Resistenze <…>`, `Perc. passiva <n>`, and always `GdS <n>` last.
- **`moves`** = ONE STRING PER MOVE, each shaped `Nome — effetto`. The em-dash matters: the renderer bolds
  everything before it. Put in the effect ONLY the resolvable numbers — to-hit or save (`TS DES CD 13`), range
  or area, damage dice and type, recharge (`Ric. 5-6`), and the rider (`metà se supera`, `spinta 3 m`,
  `prono`). A move whose telegraph costs a round says `telegrafo 1 round` and nothing more about how it looks.
- **ONE CARD PER DISTINCT STAT BLOCK, not per combatant**: three identical guards are three ROWS in the table
  but share ONE card. Elites, bosses and any variant with different numbers each get their own.
- **Phase gates and legendary actions are moves too** — a boss that changes posture at 50% gets a line
  (`Fase (50% PF) — …`), because that is exactly what the GM forgets mid-fight.
- The `notes` column is NOT a smaller copy of this panel: it carries transient state the GM writes during the
  fight (a condition, a concentration, a timed effect). Everything static about a creature belongs here.

## 09.3 — WHAT THE CONTROLS DO (so they are not "improved" away)

- **`−` / `dmg` / `+` on a monster's HP.** Type the DAMAGE in the small box and press `−` (or just hit Enter,
  which subtracts): the HP drop by that much and the box clears itself, so a stray second click cannot
  subtract twice. Press `−` or `+` with the box EMPTY and it steps by 1. The HP field itself stays directly
  editable — to set an exact value, or restore the maximum, the GM types over it. HP never go below 0.
- **`In piedi` / `💀 A terra` on a PC.** The GM's only PC-side bookkeeping, because hit points are the
  players'. Toggled on, the row dims and the name is struck through.
- **Rows dim automatically at 0 HP** for monsters — the SAME `.down` styling as the PC toggle, so "out of the
  fight" always looks the same whoever it is.
- **The turn SKIPS whoever is down.** `Avanza Turno` walks past downed monsters and downed PCs; with everyone
  down it stops instead of looping.
- **`⚠` on a monster.** The telegraph counter, for the rounds-of-warning that §B10 requires every telegraphed
  move to declare. Click cycles `off → 1 → 2 → 3 → off`. It counts down when the turn pointer COMES BACK to
  that monster — a telegraph starts on its turn and resolves on its next one — and at zero pulses `⚠ SCATTA`
  in amber until the GM clicks it away.
- **`Resetta Round`** rewinds the turn order to the first standing combatant and restores every telegraph to
  the value it had when the round began — for when a round is replayed after a rules correction. The snapshot
  is taken AFTER the first combatant's own countdown, never before: a monster that opens the round already
  firing must come back as `⚠ SCATTA`, not as the value it held a step earlier.
- **`Resetta Scontro`** restores monster HP to maximum, clears telegraphs and down states, RE-ROLLS monster
  initiative (`1d20 + initBonus`, which is why `initBonus` is in the data) and re-sorts. For rerunning a fight
  after a wipe or a retcon.
- **All numeric fields are PLAIN TEXT** (`inputmode="numeric"`), deliberately: the native spinner arrows are
  too small to hit during a session. HP/AC/initiative commit on CHANGE, not on every keystroke, so editing
  never steals focus mid-typing.
