# AUDIT REPORT — stato del progetto, FASE 0 (sola lettura)

> **Dev-only. NON si carica su Project/GEM**, come `CHANGELOG.md`.
> Misurato su HEAD `2f60679`. Nessun file del progetto è stato modificato per produrre questo report.

## Esito in una pagina

Il sistema è **in condizioni migliori di quanto l'inquadramento «audit» presupponesse**. Su cinque assi, due
producono lavoro vero, uno si cancella del tutto, e due danno una resa modesta ma con un reperto ciascuno che
vale da solo il passaggio.

| Asse | Resa | Verdetto |
|---|---|---|
| 1 · Densità delle regole | **~10 KB**, di cui 6,9 dal solo 00 | Ridimensionato: la prosa di 06 è quasi tutta portante |
| 2 · Chunking di 06 | **56 KB in 18 righe** | Confermato, è il lotto principale |
| 3 · Precedenza istruzioni↔06 | 2 reperti, uno ALTO | Ridimensionato nei byte, **cresciuto in gravità** |
| 4 · File dati 01-04 + 07 | **zero** | **Si cancella**, i controlli passano tutti |
| 5 · Memoria → Manutentore | 119 KB da ristrutturare | Confermato, indipendente dagli altri |

**Due stime del piano erano sbagliate e vanno corrette prima di procedere.** Sono segnate ⚠️ qui sotto.

---

## ASSE 1 — Densità delle regole

### 1.1 Le 65 failure shape di 06 — ⚠️ la resa è molto inferiore all'attesa

Estratte e classificate tutte e 65 (non 63: due righe ne contengono due ciascuna). Applicando il criterio
anti-bias di v4.78 — *un esempio guadagna il posto SOLO se disambigua un confine che l'affermazione astratta
non può fissare*:

| Esito | Numero | Byte |
|---|---|---|
| **RESTA** — fissa un confine reale | **53** | — |
| **VIA** — istanzia e basta | **8** | ~1,6 KB |
| **CONSOLIDA** — due esempi per lo stesso confine | 4 | ~0,6 KB |

**Il verdetto onesto: la prosa di 06 non è grasso.** Mi aspettavo di trovare una sedimentazione da potare e ho
trovato regole scritte da qualcuno che sapeva perché le stava scrivendo. Le 53 che restano non sono ripetizioni:
portano il *riparo* insieme al divieto (§A1 L42 «*la riparazione di default è la CANCELLAZIONE, non la
sostituzione*»), o distinguono un caso che l'astratto fonde (§A5 L75: il sesso della PERSONA contro il genere
grammaticale del sostantivo), o registrano una misura che nessuna regola potrebbe rimpiazzare (§B6 L1337: lo
stesso goobbue statato **tre volte in tre run** con tre GdS diversi).

**Le 8 da togliere**, tutte perché la regola sopra di loro è già completa e chiusa:

| # | Sezione | L | Cosa si toglie | Perché |
|---|---|---|---|---|
| 2 | §A1 | 33 | «*Sei tornato* → *Siete tornati*» | La regola «sempre plurale, MAI 'tu'» è autosufficiente — **e l'esempio è già in `cv` L.29 a recall 100%** |
| 7 | §A4 | 64 | «*Alveare Ventrerosso*» | «un'entità INVENTATA non prende link» è completa; ripetuta anche in `cv` L.55 |
| 9 | §A5 | 76 | «*un Elau dai capelli grigi*» | «la razza è sempre canonica, scritta giusta» è completa |
| 10 | §A5 | 78 | «*la Cospicua della Settima Alba*» | «MAI coniare un titolo» è completa |
| 15 | §A20 | 154 | «anello +1 CA marcato Non-comune a L4» | Pura istanza della scala di rarità già tabellata |
| 17 | §A23 | 220 | «il secondo scontro lasciato senza tema» | «OGNI scontro statato ha il SUO header 🎵» è output-forcing e completa |
| 23 | §B1 | 1254 | «*un lampo dell'Eco attraversa uno dei PG*» | «l'Eco è condivisa, mai divisa» è completa |
| 63 | §D4 | 1770 | «sottoclasse persa a L3» | Riafferma «non omettere nulla» senza aggiungere confine |

Le 4 da consolidare: §B2 L1280+L1283 dicono lo stesso confine con il caso sylph (due esempi, uno basta);
§B6 L1368 porta due failure shape aritmetiche nella stessa riga; §B10 L1404 è contata due volte.

**Ogni frase rimossa va archiviata in `CHANGELOG.md` con il motivo**, secondo la verifica 6 del piano.

### 1.2 I `Cross-references` di 05 — 2.282 B in 8 blocchi, ma non sono tutti uguali

Il piano li dava per «routing duplicato» in blocco. Sbagliato: **2 su 8 sono peggio di così.**

- **6 blocchi puri puntatori** (1.8, 7.8, 12.7, 13.8, 18.8, 19.7 — ~1,2 KB): rimandano a capitoli dello stesso
  file, che il modello non naviga. **VIA**.
- **2 blocchi che duplicano REGOLE**, non rimandi — ed è un difetto di categoria diversa:
  - **5.7** (726 B) ristampa i valori operativi di RAISE/ARAISE/Phoenix (livello, slot, frazione di PF,
    Aether Sickness) che vivono in **Ch.18**;
  - **9.10** (352 B) ristampa la regola Tempering/Eco che vive in **Ch.4.5/7.3**.
  Sono **seconde copie di regole numeriche**, cioè la cosa che diverge per prima quando una delle due viene
  ritoccata. **Vanno ridotti a puntatori**, con i numeri in un posto solo.

### 1.3 `00_Manual_Index.md` — confermato, si rimuove

Verificato blocco per blocco: **zero contenuto unico** (la mappa completa è nel piano). Nessun file caricato lo
cita. **−6,9 KB e il set scende a 8 file (01-08).** È da solo il 69% della resa dell'intero asse 1.

---

## ASSE 2 — Chunking di 06 (il lotto principale)

Confermato senza correzioni. **18 righe oltre 2000 caratteri, 56.026 B, il 18% del file.** Ogni altro file del
corpus resta sotto i ~1600. Le peggiori:

| Riga | Char | Sezione | Cosa contiene |
|---|---|---|---|
| L220 | **5.145** | §A23 | tema di battaglia contestuale + salienza + beat misto + titoli OST |
| L115 | **4.495** | §A14 | split delle due wiki + cache-first + scoping + fallback |
| L1666 | 3.647 | §B26 | ordine di scena del montaggio di viaggio |
| L1410 | 3.659 | §B11 | tier di scontro + carve-out offensivo |
| L1603 | 3.609 | §B20 | riga di chiusura di `/voci` + i tre livelli |
| L1295 | 3.256 | §B2 | riga viaggio + TRIP-PENDING |
| L1601 | 3.349 | §B20 | colore opzionale vs contenuto obbligatorio |
| L1644 | 2.882 | §B24 | gate anchor quote |
| L1280 | 2.978 | §B2 | **`COUNTING N`** |

L'ultima è la prova che il difetto non è teorico: `COUNTING N` è **esattamente** la regola che nei test non
veniva co-recuperata con l'avviso che la consuma.

**§A24 — misura per la tua decisione:** 42 KB e 990 righe su 1813, cioè il **55% delle righe** di 06. Non
raccomando di spostarla: l'argomento strutturale che l'ha portata lì regge e il tracker funziona su entrambe le
piattaforme. La registro perché il numero vada a verbale, non per riaprire la decisione.

---

## ASSE 3 — Precedenza istruzioni ↔ 06 ↔ 05

### ⚠️ 3.1 La stima del piano era sbagliata: le istruzioni NON duplicano 06

Il piano diceva «~8 KB di `cv28` riaffermano regole che vivono anche in 06». Misurato con sovrapposizione di
9-grammi sulle righe lunghe:

| File | Righe lunghe | Sovrapposte a 06 |
|---|---|---|
| `Instructions_Campaign.txt` | 25.411 B | **872 B — 3%** |
| `Instructions_OneShot.txt` | 14.887 B | **777 B — 5%** |
| `Instructions_Loremonger.txt` | 12.271 B | **1.506 B — 12%** |

E l'unico vero doppione in tutti e tre è **lo stesso**: l'esemplare di registro della prosa italiana, duplicato
**deliberatamente** perché deve avere recall 100%. I tre file rispettano la loro stessa riga di formato
(*«/comando → cosa produce → riga d'apertura → la cosa non ovvia → sezione 06»*): sono puntatori, non copie.
**Non c'è debito di sincronizzazione da byte.** Il rischio è tutto semantico — ed è lì che stanno i due reperti.

### 3.2 ALTA — 06 viola la propria regola del roster chiuso

§B1 stabilisce, con la failure shape osservata **due volte** in test dal vivo:

> *«questa regola è enunciata come ROSTER CHIUSO e mai come elenco di ciò che è stato rimosso: **nominare un
> comando ritirato lo rimette in circolo attraverso il recupero**.»*

E poi 06 nomina tre comandi ritirati, in forma negativa:

| Comando | Dove | Testo |
|---|---|---|
| `/carica` · `/load` | 06, §B17/§B24 | «*non esiste alcun comando `/carica` o `/load`*» (×2) |
| `/subquest` | 06 §B20 | «*NON esiste un comando `/subquest`*» |
| `/subquest` | **`cv` L.71** | «*There is NO /subquest command*» |

La negazione non protegge: il recupero non distingue «X non esiste» da «X». È il meccanismo che ha tenuto vivo
`/prepara` per un intero ciclo dopo la rimozione — il progetto ha già pagato per sapere che questo è vero.
**Riparazione:** cancellare le tre negazioni e lasciare che sia il roster chiuso a fare il lavoro. Dove la frase
serviva a spiegare *perché* il load non ha comando, si riscrive in positivo: «il blocco `=== SAVE ===` è esso
stesso l'innesco, e il load non ha comando».

### 3.3 MEDIA — `/riposo` è e non è un beat

| Fonte | Dice |
|---|---|
| `cv` L.6 e L.58 | «*A STORY BEAT IS PRODUCED ONLY BY /continua, /riassumi, /viaggio*» |
| `cv` L.62 | «*`/riposo` → **LONG REST beat**, transient*» |
| `cv` L.79 | elenca `/riposo` e `/viaggio` fra i «*transient **played beats***» |
| 06 §B28 | «*LONG REST (/riposo) — on-demand, **played**, transient*» |

Una riga chiusa ed enumerativa che esclude un comando che le altre tre righe descrivono come beat giocato. È la
stessa forma che aveva già causato problemi con `BEAT END`. **Riparazione:** separare i due concetti — `/continua`,
`/riassumi`, `/viaggio` avanzano il **cursore**; `/riposo` e `/viaggio` sono beat **giocati e transienti**. Il
predicato che serve alla riga L.6 è *«avanza il cursore»*, non *«è un beat»*.

### 3.4 Direzione 05 → 06: pulita
I capitoli con controparte in 06 delegano correttamente e lo dicono esplicitamente (Ch.19.2 «*non duplicato qui:
usa sempre quello*»). Le uniche due eccezioni sono i blocchi 5.7 e 9.10 del §1.2.

---

## ASSE 4 — File dati 01-04 + 07: **nessun reperto, il lotto si cancella**

Tutti i controlli passano:

- **13 classi di creature dichiarate in 04, 13 presenti** (Ashkin → Wavekin);
- **22 job dichiarati in 05 Ch.3.3, 22 intestazioni in 02**; le 8 razze giocabili di 05 Ch.3.2 corrispondono a 01;
- **schema uniforme**: `SCHEMA NOTES` in 00-06; 07 e 08 hanno il proprio blocco di convenzioni equivalente
  (`G0`, `08.0`);
- **la regola di strip XP ESISTE già** — §B6: «*NO XP EVER (binding, output-forcing): la riga GdS stampa il
  NUMERO NUDO e nient'altro*». Il sospetto del piano era infondato: il dato inglese `CR 3 (700 XP)` in 04 è
  correttamente separato dall'output.

I file dati sono la parte meglio tenuta del progetto. **Non spendere un lotto qui.**

---

## ASSE 5 — La memoria storica → il Manutentore

Confermato: **143 menzioni di comandi ritirati** (`/stop` ×68, `/load` ×44, `/confermo` ×12, `/prepara` ×7,
`/nota` ×4, `/gioca` ×3, `/subquest` ×2, `ESEGUO` ×3), in linguaggio imperativo. Caricarlo nei tre assistenti di
gioco è escluso — e il §3.2 qui sopra mostra che il progetto sta già pagando questo prezzo con **tre** menzioni,
figurarsi con 143.

Ripartizione del file: **92,9 KB di cronologia datata** (14 sezioni `UPDATE (data)`, la lezione centrale,
l'archivio, lo stato) contro **26,7 KB di architettura evergreen**. Il file si dichiara *«version-agnostic ON
PURPOSE»* in intestazione e non lo è.

---

## Piano dei lotti, rivisto sui reperti

| Lotto | Contenuto | Resa | Ricarica |
|---|---|---|---|
| **B1** | Rimozione di 00 · le 8 failure shape · le 4 consolidazioni · i 6 `Cross-references` puntatori · i 2 blocchi 05 che duplicano regole | **~10 KB** e un rischio di deriva chiuso | **05**; togliere **00** da Project e GEM |
| **B2** | Chunking delle 18 righe-mostro, poi triage delle 74 | il grosso | **06** |
| **B3** | Le tre negazioni di comandi ritirati · il predicato di `/riposo` | **la gravità più alta del report** | **06** + incollare **cv** |
| ~~B4~~ | ~~File dati~~ | **cancellato — zero reperti** | — |
| **B5** | `M1_Project_Memory.md` + `Instructions_Maintainer.txt` | il quarto Project | crearlo e caricarci M1 + CHANGELOG |

**Raccomandazione sull'ordine: B3 prima di B1 e B2.** Il piano lo metteva terzo per pura sequenza degli assi, ma
è l'unico lotto con un reperto ad alta gravità, è piccolo (quattro frasi), e non tocca le stesse righe degli
altri due. Farlo per primo mette al sicuro il risultato che conta di più prima di aprire il file grosso.

B1 e B2 restano in quest'ordine fra loro e restano commit distinti.
