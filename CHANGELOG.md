# CHANGELOG — FFXIV x D&D 5e assistant (knowledge files)

## 2026-09-03h — Rifattorizzazione Sistema di Viaggio, Meteo Dinamico e Banner Meccanico (06 v6.82, Instructions cv144, 05 v2.29)

Risoluzione definitiva della sovrapposizione tra `/continua` e `/viaggio`, formalizzazione dell'architettura Eterite + Ultimo Miglio, estrazione casuale del meteo dai roster canonici e introduzione del banner di allerta meteo severo a vista del DM:
- **06_PROCEDURES_AND_FORMAT.MD (v6.82):**
  - **§A3 (Meteo Dinamico e Banner Meccanico):**
    - Sancita la fine del "sempre sereno": all'ingresso in una nuova zona (tramite `/continua` compresso o `/viaggio`), il meteo viene **estratto casualmente dalla tabella canonica della regione di destinazione** (Gamer Escape / ConsoleGamesWiki; durata reimpostata a `da 0 ore`).
    - Introdotto il **Banner di Allerta Meccanica in Testa al Beat**: quando il meteo è SEVERO (§A3: Pioggia battente, Temporale, Nebbia fitta, Tempesta di sabbia, Ondata di calore, Tormenta/Bufera, Burrasca), viene emessa su riga singola l'allerta `⚠️ Condizione Ambientale: <Meteo> <emoji> — <Effetti Meccanici 5e>` subito sotto l'header/estimate del beat prima della narrazione, garantendo al GM visibilità immediata su CD, terreno difficile e penalità prima di iniziare a leggere o giocare la scena.
    - Convalidato il *Lead-in Narrativo Ambientale*: le prime 1-2 frasi della nuova scena descrivono diegeticamente l'impatto sensoriale del cielo, della luce e del clima.
  - **§B1 (Struttura Beat e Footer Command-Neutral):**
    - Codificata la posizione del banner `⚠️ Condizione Ambientale:` tra header/estimate e narrazione.
    - Ribadita la natura rigorosamente **command-neutral** della bussola `🧭 Viaggio:` e dei marcatori (nessun nome di comando con slash `/`), prevenendo al 100% il rischio di *continue-momentum* e priming di comandi concorrenti su LLM veloci.
  - **§B2 (Arrivo Compresso sotto `/continua`):**
    - Chiarito che sotto `/continua`, in presenza di viaggio pendente, il party arriva compresso all'obiettivo: teletrasporto via Eterite all'hub con 1 sola clausola diegetica di rematerializzazione, zero montaggi di marcia a piedi, zero tiri d20, apertura diretta della scena MSQ. Se prima volta in una terra vergine (Eterite non ancora visitata), la marcia è narrata in modo compresso a tappe forzate, calcolando le ore effettive sull'Orario e sintonizzando il cristallo all'arrivo.
  - **§B26 (Varianti di `/viaggio` e Meccaniche di Transito):**
    - Codificate le 4 opzioni di viaggio giocato: `/viaggio` (default: Eterite all'hub + montaggio giocato dell'Ultimo Miglio a piedi, +1h Orario, tiro evento 1d20), `/viaggio chocobo` (Eterite all'hub + Ultimo Miglio a dorso di chocobo, +1h Orario, vantaggio fuga), `/viaggio strada` (overland completo a piedi senza Eterite, +1h per zona attraversata, 1d20) e `/viaggio strada chocobo` (overland completo su chocobo, +1h ogni 2 zone, 1d20). Chiusura sempre con marcatore neutro `— Arrivo a <destinazione> —`.
- **INSTRUCTIONS_CAMPAIGN.TXT (cv144):**
  - Aggiornato il blocco `<commands>`: `/continua` documentato con arrivo compresso, sincronizzazione meteo/orario e apertura diretta della quest; `/viaggio` espanso con la sintassi `[chocobo | strada | strada chocobo]`.
  - Aggiornato il blocco `<beat>`: incorporata la regola del banner `⚠️ Condizione Ambientale:` in testa al beat per meteo severo e il roll casuale del meteo di zona con lead-in narrativo sensoriale.
- **05_CAMPAIGN.MD (v2.29):**
  - Capitolo 8 (§8.2): Esplicitata la distinzione tra Macro-tratta verso gli hub regionali (Eterite) e Ultimo Miglio selvaggio. Formalizzata la regola della prima esplorazione: un'Eterite non può essere raggiunta se mai visitata prima; il party viaggia overland dall'hub più vicino e sintonizza il cristallo all'arrivo.
- **PROJECT_MEMORY.MD:**
  - Registrata la documentazione tecnica sulla separazione `/continua` vs `/viaggio`, la gestione del meteo casuale, il banner in testa al beat e la protezione contro il continue-momentum.

Rifattorizzazione globale della spina dorsale MSQ contro i colli di bottiglia e il padding da MMO (Ordeals of Valor e rimozione dei ping-pong fetch), preservando al 100% i titoli canonici inglesi, i giver, le coordinate e la compatibilità con salvataggi e wiki search:
- **08_MSQ_FLOW.MD (v3.60):**
  - **Company of Heroes (ARR L30-L34):** Tagliate le 12 quest di commissioni e viaggi a vuoto intercontinentali per il banchetto (`Tales from the Tidus Slayer` -> `There and Back Again`, e `What Do You Mean...` -> `It Was a Very Good Year`) con tag `[CUT: Company of Heroes MMO ping-pong filler — bypassed in D&D flow]`. Il flusso collega direttamente: *Wrath of the Titan* (Minfilia manda a Costa del Sol dal capitano Wheiskaet) -> *The Things We Do for Cheese* ([DUNGEON: Brayflox's Longstop], prova tattica e recupero del sintonizzatore per l'eterite) -> *In the Company of Heroes* (Wheiskaet onora il party e introduce lo scout Riol) -> *As You Wish* -> *Lord of Crags* ([TRIAL: Titan / The Navel]). Da 15 quest a 3 quest ad alta tensione.
  - **I Cristalli Corrotti di Garuda (ARR L40-L44):** Tagliate le 8 quest del finto giro del mondo tra Camp Drybone (cristallo di fuoco) e Isles of Umbra / Sirena (cristallo d'acqua) con tag `[CUT: Corrupted Crystal MMO wild-goose-chase filler — bypassed in D&D flow]`. Cid identifica subito l'anomalia di vento nel Bosco Centrale: *Into the Eye of the Storm* -> *The Curious Case of Giggity* (recupero del cristallo dal nido dello spriggan Giggity) -> *Better Late than Never* (montaggio del rostro d'etere sull'Enterprise) -> *Lady of the Vortex* ([TRIAL: Garuda / The Howling Eye]). Da 12 quest a 3 quest dense.
  - **I Rifugiati di Doma (Post-ARR Patch 2.2):** Tagliata la quest del nascondino con i bambini a Vesper Bay (*Yugiri's Game*) con tag `[CUT: Doman hide-and-seek MMO filler — bypassed in D&D flow]`. Il flusso collega il rifiuto d'asilo dei Monetaristi ad Ul'dah (*Promises to Keep*) direttamente alla scorta armata del convoglio fuori dal Thanalan (*Why We Adventure*) e all'accoglienza a Mor Dhona (*All Due Respect*).
  - **Il Carrello di Amh Araeng (Shadowbringers L76-L77):** Tagliate le 4 quest di commissioni di pulizia cassette attrezzi, ricerca monete e piazzamento fumogeni (*On Track*, *Down for Maintenance*, *A Convenient Distraction*, *A Dirty Job*) con tag `[CUT: Amh Araeng trolley-chores MMO filler — bypassed in D&D flow]`. Il dolore e il lutto di Magnus a Twine (*The Truth Hurts*) conducono direttamente alla pericolosa spedizione nelle miniere di Biran per riesumare la Pietra Senza Tempo (*Have a Heart*), risvegliando il Talos e lanciando la corsa del carrello verso il duello con Ran'jit (*Full Steam Ahead*).
  - **I Loporrit e l'Arca di Labyrinthos (Endwalker L88-L89):** Tagliate le 4 quest di commissioni agricole con Cookingway, interviste a 8 studiosi e trasporto casse/documenti durante i Giorni Finali (*Wise Guides*, *Agriculture Shock*, *Sage Council*, *Hither and Yarns*) con tag `[CUT: Endwalker Labyrinthos ark-logistics MMO filler — bypassed in D&D flow]`. *No Job Too Small* si collega direttamente alla difesa degli estrattori lunari con G'raha Tia (*Once Forged*), alla grande convergenza planetaria dell'adamantite (*Bonds of Adamantite*) e alla discesa verso la Madre Cristallo (*Her Children, One and All* -> [DUNGEON: The Aitiascope] + [TRIAL: Hydaelyn]).
  - **Header Installment 1 (riga 1258):** Rimossa la dicitura obsoleta "Grand Company", sostituita con *Remembrance Speeches & Nine Ivies*.
  - **Riallineamento Linguistico Completo (08.0, 08.1, Subquest):** Tradotte e riallineate al 100% in lingua inglese le convenzioni globali (`08.0`), la legenda dei marcatori, i sommari dei trial/subquest di Hildibrand e i requisiti di sblocco dei dungeon opzionali, garantendo uniformità stilistica e massima compatibilità cross-file con Gamer Escape e ConsoleGamesWiki.
- **05_CAMPAIGN.MD (v2.28):**
  - Allineata la Table of Contents: Capitolo 17 corretto in `The Grand Companies & Regional Allies`.
  - Chiarito al capitolo 12 (§12.7) che i voli diplomatici e gli spostamenti su aeronave legati alla MSQ tra le capitali alleate sono coperti dal lasciapassare diplomatico dei Scion (*Airship Pass*, 0 Gil); le tariffe commerciali si applicano esclusivamente a rotte private, charter o viaggi personali fuori servizio.
- **README.MD:**
  - Aggiornato il flusso di test standard rimuovendo il comando ritirato `/chiusura` e allineando al protocollo unico di `/salva`.
  - Integrata la descrizione operativa di `combat_tracker.html` come app web standalone da aprire nel browser e alimentare incollando i blocchi incontro generati dall'assistente.

08 v3.60 · 05 v2.28 · README.md aggiornato.

## 2026-09-03f — Revisione ed Espansione Glossario e Adattamento Nomi (07_Glossary.md v1.41)

Revisione completa di `07_Glossary.md`:
- **REGOLE DI ADATTAMENTO AUTOMATICO (G1 & G3):**
  - Espansa la regola sui cognomi trasparenti dotati di lore in G1: tradotti per senso/composto fuso (*Pietragrigia* per bastardi di Coerthas, *Sanguedidrago*, *Diecidita*, *Cuordiferro*, *Spinanera*), preservando invariati i cognomi culturali/metrici francesi (*de Fortemps*, *de Borel*), roegadyn antichi (*Bloefhiswyn*, *Wilfsunwyn*) e lalafell (*Nanarito*, *Taru*).
  - Aggiunte a G3 radici geografiche e infrastrutturali frequenti (`-grotto` -> Grotta; `-rest` -> Riposo; `-hollow` -> Antro/Cavità; `-crag` -> Dirupo/Falesia; `-scar` -> Sfregio; `-dell` -> Valletta; `Shrine/Sanctum` -> Santuario; `Barrow/Cairn` -> Tumulo; `Airship` -> Aeronave; `Skiff/Barge` -> Battello/Chiatta; `Caravan` -> Carovana; applicazione snella di `Station` e `Float`).
- **TERMINI DI MONDO E LORE (G5, G6, G7):**
  - Inseriti `Magitek` (invariato), `ceruleo (ceruleum)`, `sintonizzazione (attunement)`, `Aeronave (Airship)`, `Erba Gysahl / Erbe Gysahl (Gysahl Greens)`, `Tomopietra Allagana (Allagan Tomestone)`, `la Calamità (The Calamity)`, `Settima Era Ombrosa (Seventh Umbral Era)` e `Settima Era Astrale (Seventh Astral Era)`.
- **HUB E FAZIONI ARR (G9 & G10):**
  - Toponimi snelli e integrati: *Campo Orizzonte*, *Campo Tranquillo*, *Zuccacaduta*, *Boscomulino*, *Stazione Sterpenero*, *Postarapida*, *Piane di Carteneau*, *Lago Lacrimargento*, *Grotta del Canto Marino*, *Albero della Sultana*, *Presidio del Bannock*, *Rovine di Sil'dih*.
  - Fazioni: *Le Spade della Sultana (The Sultansworn)*, *Studenti di Baldesion (Students of Baldesion)*, *i Monetaristi e i Realisti*, *Quattordicesima Legione (XIVth Legion)*, *Impero Garleano (The Garlean Empire)*.
- **ROSTER NPC BLINDATO (G11):**
  - Nomi e cognomi canonici locked (Scion, leader cittadini, nobili ishgardiani, generali imperiali, Ascian e Antichi).
- **DUNGEON E TRIAL MANCANTI (G12, G13, G14):**
  - Integrati *Valdorata (The Aurum Vale)*, *La Crisalide (The Chrysalis - Nabriales)*, *I Gradini della Fede (The Steps of Faith - Vishap)*, *Il Muro di Baelsar (Baelsar's Wall)* e *L'Oscuro Ghimlyt (The Ghimlyt Dark)*.
- **IMPRECAZIONI ED ESCLAMAZIONI REGIONALI (G27.2):**
  - Espansione massiccia delle invocazioni dei Dodici e del colorito parlato eorzeano (*Per i seni di Nophica!*, *Per il conio di Nald!*, *Per la lancia di Halone!*, *Per la tempesta di Llymlaen!*, *Per il martello di Byregot!*, *Per la Custode!*, *Per lo Studioso!*, *Per il Viandante!*, *Per l'Amante!*, *Per la Tessitrice!*, *Ratti di mare!*, *Che tu vada al Settimo Inferno!*, *Dèi del cielo!*, *Rovina e putredine!*).

- **ALLINEAMENTO RIFERIMENTI 06 (06_Procedures_and_Format.md v6.81):**
  - Corretto a §B6 riga 413 il riferimento incrociato alla regola anti-doppione del test delle parentesi, puntando al corretto `07 G2` anziché `07 G10`.

07 v1.41 · 06 v6.81.

## 2026-09-03e — Eliminazione Arruolamento Grand Company e Status Sovranazionale dei Scion

Rimozione della scelta e arruolamento militare dei giocatori in una singola Grand Company, preservando le tre compagnie come fazioni geopolitiche del mondo e alleate dei Scion (05 v2.27, 06 v6.80, 08 v3.59):
- **RUOLO DEL PARTY (05 Ch. 17 & Ch. 1.7):**
  - I PG appartengono ai *Scions of the Seventh Dawn*, una coalizione neutrale e sovranazionale. Eliminato l'arruolamento obbligatorio o facoltativo in una singola armata cittadina, evitando di dividere il party o forzare la scelta di una fazione militare.
  - A seguito della vittoria su Ifrit e dei discorsi di Carteneau, tutte e tre le Grand Company riconoscono il gruppo come campioni dell'Alleanza e inviati speciali dei Scion, garantendo pari stima e accoglienza a Limsa Lominsa, Gridania e Ul'dah.
- **RIFATTORIZZAZIONE QUEST MSQ (08_MSQ_Flow.md):**
  - In *A Hero in the Making*, i discorsi commemorativi di Merlwyb, Kan-E-Senna e Raubahn cementano l'appello congiunto ai Scion per unire il reame contro i garleani.
  - In *The Company You Keep*, eliminato il triplo bivio di reclutamento. La missione si focalizza sull'azione sul campo: la ricognizione urgente dell'aeronave abbattuta da pattuglie garleane a Nine Ivies, lo scontro e il salvataggio degli ingegneri Biggs e Wedge che si uniscono ai Scion.
  - Tagliate le varianti delle cerimonie di giuramento militare (*Wood's Will Be Done* / *Till Sea Swallows All* / *For Coin and Country*) con `[CUT: MMO military swearing-in ceremony]`, connettendo direttamente l'arco a *Sylph-management*.
- **REGOLE PROCEDURALI (06 §B2):**
  - Riformulata la regola di §B2 da "Light Enrollment Beats" a "Transnational Scion Status", eliminando il beat di scelta dell'arruolamento militare dal flusso operativo.
- **INDICE DEI TERMINI (05 Ch. 20):**
  - Aggiornata la voce *GRAND COMPANY*: fazioni nazionali e alleati regionali dell'Alleanza; i PG operano come inviati e campioni dei Scion.

05 v2.27 · 06 v6.80 · 08 v3.59.

## 2026-09-03d — Allineamento Canonico MSQ e Bonifica Lore (05_Campaign.md v2.26)

Audit completo di coerenza tra `05_Campaign.md` e `08_MSQ_Flow.md` / lore ufficiale FFXIV:
- **CONVERGENZA AMBASCIATA E SCIONS (Ch. 1.7 & Ch. 5.3):**
  - Chiarita la sequenza delle tre città: l'ambasciata converge in `Call of the Sea` ➔ primi 3 dungeon (Sastasha, Tam-Tara, Copperbell) ➔ invito a Vesper Bay per unirsi ai Scion (`The Scions of the Seventh Dawn`).
  - Separata nettamente la scelta della Grand Company (`The Company You Keep`), che avviene dopo Ifrit (L4) e i discorsi commemorativi (`A Hero in the Making`), eliminando la conflazione precedente in Ch. 1.7.
- **RIALLINEAMENTO MILESTONE PROGRESSION 1-20 (Ch. 5.3):**
  - *ARR:* Inseriti i dungeon mancanti di L5 che preparano Titano (*Haukke Manor* e *Brayflox's Longstop*); corretto il posizionamento di Cape Westwind (*Rhitahtyn sas Arvina* solo duty) a L7 durante l'Operazione Archon (dopo Garuda e prima di Castrum Meridianum), rimuovendolo da L6; esplicitato il trial *The Porta Decumana* (revamp 6.1) per lo scontro con Ultima Weapon e Lahabrea.
  - *Heavensward (L9-L12):* Inseriti i checkpoint narrativi di *The Aery* (Nidhogg), *The Vault* (sacrificio di Haurchefant), e la risoluzione della Dragonsong War a *The Final Steps of Faith*.
  - *Stormblood (L13-L15):* Corretto il timing della liberazione (Doma a L13, Ala Mhigo a L14 con Shinryu/Zenos); precisato l'arco 4.x con Tsukuyomi (4.3) e The Ghimlyt Dark / il richiamo dei Scion (4.5).
  - *Shadowbringers (L16-L19):* Risolto il grave disallineamento su Hades: *Amaurot* e *The Dying Gasp (HADES)* costituiscono il climax di 5.0 (L18); L19 governa l'arco 5.1-5.3 che culmina in *The Seat of Sacrifice (ELIDIBUS)* come Guerriero della Luce primordiale.
  - *Endwalker (L20):* Strutturata la sequenza canonica a cap (Zot, Babil, Zodiark, Vanaspati, Elpis/Ktisis, Aitiascope/Hydaelyn, Ultima Thule/Endsinger).
- **CONTRADDIZIONE PRIMA VOCE HYDAELYN (Ch. 7.4):**
  - Corretta la descrizione del Cristallo dell'Acqua (#1): non è la "prima voce" di Hydaelyn (che parla già all'arrivo e nella visione della grotta/albero dove chiede i cristalli per nome), ma il primo cristallo fisico reclamato in risposta al Suo incarico.
  - Aggiornati i riferimenti al dovere in solitaria distrettuale per la visione di Hydaelyn (`Lurkers in the Grotto` / `Chasing Shadows` / `Underneath the Sultantree`) a seguito del taglio dei gear check.
- **TERM INDEX (Ch. 20):**
  - Rimossa la menzione obsoleta della tabella d20 in `GOSSIP / RUMORS`, allineandola al testo attuale di Ch. 15.

05 v2.26 · 06 v6.79 · 08 v3.58.

## 2026-09-03c — Bonifica Meccaniche MMO e Sfoltimento Flow (08_MSQ_Flow.md v3.58)

Rimozione e rifattorizzazione di tutte le quest e i passaggi contenenti meccaniche prettamente da videogioco MMO, restituendo fluidità e coerenza al gioco di ruolo:
- **TUTORIAL DI EQUIPAGGIAMENTO LIVELLO 5 (TAGLIATI):**
  - Limsa Lominsa: Tagliata `Dressed to Call` (`[CUT: MMO gear-check tutorial]`). `On to Summerford` conduce direttamente alla Solo Duty di `Lurkers in the Grotto` a Seasong Grotto dopo il briefing di Staelwyrn.
  - Gridania: Tagliata `Passing Muster` (`[CUT: MMO gear-check tutorial]`). `To the Bannock` conduce direttamente alla Solo Duty di `Chasing Shadows` nel bosco dopo il briefing di Galfrid.
  - I PG possiedono già l'equipaggiamento iniziale appropriato da Sessione 0.
- **SINTONIZZAZIONE ETERITI (IN-CHARACTER ADVICE):**
  - Mantenuto l'invito a sintonizzarsi con l'Eterite principale nelle quest #2 delle tre città (`Close to Home`), riformulato come consiglio diegetico dato dalla Gilda dei rispettivi avventurieri (senza forzature da checklist o sblocchi fittizi di magie videoludiche come "Return").
- **SBLOCCHI DI SISTEMA VIDEOLUDICI RIMOSSI:**
  - Espunti i riferimenti a "unlocks Inn Rooms & Guildleves" al termine delle tre quest di scontro con l'Ascian harbinger (`Just Deserts`, `Spirithold Broken`, `Way Down in the Hole`).
- **TUTORIAL DI RUOLO "HALL OF THE NOVICE" (BYPASSATO):**
  - In `It's Probably Pirates` prima di Sastasha, bypassata la tappa d'addestramento ruoli MMO dell'avventuriero veterano; i PG passano direttamente dall'imbarco di V'mellpa al briefing delle Yellowjacket all'ingresso delle caverne di Sastasha.
- **RIFATTORIZZAZIONE EMOTE E COMANDI SLASH IN CHAT (ROLEPLAY & PROVE):**
  - Riformulati in pure interazioni narrative o prove di abilità (Insight, Intimidation, Persuasion, Performance) tutti i comandi slash videoludici del flow:
    - Limsa #9 (`Plowshares to Swords`): incoraggiamento dei braccianti ai frutteti senza spam di `/cheer` o `/soothe`.
    - East Shroud (`First Contact` & `Dance Dance Diplomacy`): Komuxio accoglie la squadra con la danza cerimoniale dei silfi in *First Contact*; tagliata `Dance Dance Diplomacy` (`[CUT: MMO emote fetch cut]`) che richiedeva di ballare per 3 silfi generici.
    - Coerthas (`Blood for Blood`): interrogatorio e intuizione per smascherare l'eretica Prunilla anziché l'emote `/doubt`.
    - Thanalan (`Desperate Times`): conforto al rifugiato terrorizzato con Persuasione/Medicina anziché `/soothe`.
    - Heavensward (`Black and the White`): saluto di rispetto cerimoniale all'anziano Kunu Vali anziché `/bow`.
    - Stormblood (`The Will to Live`): infiltrazione in divisa militare garleana con saluto marziale anziché `/imperialsalute`.
    - Shadowbringers (`A Taste of Honey` & `A Day in the Neighborhood`): esibizione di corte a Eulmore anziché ballo sul marcatore arcade, e scambio del saluto rituale dei Blessed of the Night (*allin tuta*) a Slitherbough anziché digitazione in chat e inginocchiamento forzato.

05 v2.25 · 06 v6.79 · 08 v3.58.

## 2026-09-03b — De-duplicazione Architetturale e Pulizia 05 (Campaign)

De-duplicazione e bonifica di `05_Campaign.md` (v2.25) a seguito del Full Audit 05 vs 06, eliminando dati contrastanti, tabelle obsolete e testo di prompt engineering:
- **TARIFFE DI TRASPORTO (Ch. 8):** Riscritto Ch. 8.4 ed eliminata integralmente la sezione ridondante 8.5 che conteneva tariffe obsolete e confliggenti (1–10 Gil). Tutti i prezzi canonici di traghetti, Chocobo, navi, aeronavi e cavalcature risiedono unicamente e autorevolmente nel capitolo economico (`05 Ch. 12.7`).
- **EVENTI DI VIAGGIO & ACCAMPAMENTO (Ch. 14.6):** Rimossa la verbosità procedurale per LLM (pre-generazione di entrambi i rami, gestione dei token e chiamate interne), preservando la sola regola di gioco per il GM: le 3 classi di pericolo (*Tranquillo, Rischioso, Ostile*), le soglie d20 e il bilanciamento proporzionato degli incontri.
- **METEO & PERICOLI AMBIENTALI (Ch. 14.7):** Mantenute le tabelle regionali e le meccaniche 5e dei pericoli estremi (caldo, freddo, nebbia, burrasca), espungendo le istruzioni di formattazione della stringa footer (che appartengono a `06 §B1`).
- **VOCI & TAVERNE (Ch. 15.2):** Rimossa la vecchia tabella d20 con voci vere/false e disclaimers operativi; Ch. 15 si concentra sul roleplay nelle taverne storiche della Gilda, lasciando il motore operativo di `/voci` a `06 §B20`.
- **CUTSCENE & DRAMATIC IRONY (Ch. 16.6):** Trasformata la sezione in guida pura di narrazione per il GM (cutscene su binari in-scena vs scene di ironia drammatica off-scene), eliminando le formule imperative di sintassi e metatesto.

05 v2.25 · 06 v6.79 · 08 v3.57.

## 2026-09-03a — Linearizzazione Quest Multiple: Moguri (1A), Fringes (2B) e Fortemps

Evoluzione della catena MSQ in `08_MSQ_Flow.md` (v3.57) per garantire un avanzamento sequenziale univoco:
- **I MOGURI DI MOGHOME — OPZIONE 1A (HEAVENSWARD 3.0):**
  - Risolto il nodo a 3 quest parallele di Chieftain Moglin a Moghome: scartati i micro-fetch superflui di raccolta erbe (*Moghan's Trial*) e ricerca del manufatto perduto (*Mogwin's Trial*).
  - La sequenza lineare mantiene la sola prova marziale eroica di caccia e difesa contro gli archeosauri ad Eil Tohm (*Mogmug's Trial*), che conduce direttamente a *Moglin's Judgment* e all'incontro con Hraesvelgr.
- **LE FRINGES / RESISTENZA DI ALA MHIGO — OPZIONE 2B (STORMBLOOD 4.0):**
  - Sequenzializzate le due catene precedentemente parallele: completata l'intera catena di M'naago con Raubahn nelle Fringes (4 quest), il cui finale conduce naturalmente al fronte dei rifugiati di Meffrid ad Ala Gannha.
  - Snellita la catena di Meffrid eliminando 4 micro-fetch di cava/Qiqirn superflue (*Hard Country*, *Death by a Thousand Rocks*, *A Life More Ordinary*, *The Color of Angry Qiqirn*), preservando il soccorso dell'Ananta (*The Prodigal Daughter*), la Solo Duty canonica di protezione dei giovani ribelli (*The Black Wolf's Pups*) e il rientro con Meffrid (*Homeward Bound* ➔ *Where Men Go as One*).
- **LINEARIZZAZIONE DEI FRATELLI FORTEMPS (HEAVENSWARD 3.0):**
  - Collegata in serie contigua la Support Chain A (Lord Artoirel a Falcon's Nest, 7 quest con Solo Duty eretici) con la Support Chain B (Lord Emmanellain al Sea of Clouds, 6 quest con Vanu Vanu), da cui si approda a *Divine Intervention* con entrambi i fronti completati senza salti logici.

06 v6.79 · 08 v3.57.

Aggiornamento approfondito del Knowledge Layer (`08_MSQ_Flow.md` v3.56):
- **VERIFICA & CHIARIMENTO LEGENDA DEI MARCATORI (`08.0` & `08.1`):**
  - Rettificata la legenda a riga 30 e nelle convenzioni globali di `08.0`, separando nettamente i contenuti tagliati (`[CUT]`) dai contenuti opzionali supportati (`[REC]`).
  - Formalizzate le categorie autoritative: `[GATE]` (checkpoint obbligatorio MSQ), `[REC]` (subquest raccomandata canonica giocabile tramite `/voci`), `[OPT]` (raid parallelo opzionale), `[CUT]` (quest/feature non implementate nel regolamento o fetch-errand fuori mano e saltate a piè pari), `[COND: …]` (marcatori di condensazione per `/riassumi`).
- **RIPRISTINO INTEGRALE DELLA SAGA DI HILDIBRAND MANDERVILLE (ARR → EW):**
  - Reintegrato l'arco di Heavensward (*Further Hildibrand Adventures* a Ishgard con Cyr, Gigi il mammet, i suplex di Godbert a Dravania e la minion Gigi), precedentemente omesso.
  - Arricchito l'arco di ARR con i 3 Trial canonici (*Battle on the Big Bridge*, *The Dragon's Neck*, *Battle in the Big Keep*) contro Gilgamesh (Greg) ed Enkidu.
  - Espanso l'arco di Stormblood a Kugane con Shigure, Akebono, il trial canonico *Kugane Ohashi* (Yojimbo / Greg & Daigoro) e il cliffhanger della Fenditura Interdimensionale.
  - Formalizzato l'interludio dimensionale in Shadowbringers con il cameo spettrale nel dungeon MSQ *The Heroes' Gauntlet* (5.3).
  - Integrato l'arco di Endwalker a Radz-at-Han con il salvataggio di Hildibrand da Norvrandt, l'alieno PuPu, Delion, Brandihild, le Armi Manderville forgiate da Godbert e il trial canonico *The Gilded Araya* (Asura).
  - Inserite in `08.OST` e `08.OST-SCENE` tutte le tracce dedicate di Soken (`Agent of Inquiry`, `Battle on the Big Bridge`, `Decisive Battle`, `Battle on the Big Bridge (Stormblood Version)`, `Final Fantasy IV: Battle 2 (Endwalker)`).
- **RIMOZIONE DEFINITIVA DEI LIVELLI VIDEOLUDICI MMO:**
  - Tutti i dungeon e contenuti opzionali sono ora ancorati unicamente alle quest MSQ di sblocco (senza livelli numerici estranei al sistema di avanzamento a milestone 1-20 del gioco).

08 v3.56.


Evoluzione coordinata tra Knowledge Layer (`06` v6.78, `05` v2.24) e Control Layer (`cv143`):
- **TRACCIAMENTO CONTINUO DELLA DURATA METEO (`da N ore`):**
  - Nel blocco `=== SAVE ===` sotto `[B] PARTY`, il campo `Meteo` traccia ora esplicitamente la durata in ore dall'inizio della condizione attiva: `- Meteo: {Condizione} (da N ore)` (es. `Meteo: Sereno (da 2 ore)` o singolare `da 1 ora`).
  - Nel footer di ogni beat giocato (`⏱️ / 🌙 Orario & Meteo`), la durata attiva viene mostrata dinamicamente di fianco alla condizione atmosferica ed emoji (`Meteo: Sereno ☀️ (da 2 ore)`), avanzando di pari passo con l'Orario (`+delta`).
- **DINAMICHE DI TRANSIZIONE & SOGLIE ATMOSFERICHE:**
  - Il meteo evolve plausibilmente quando persiste continuativamente per 3-4 ore o al varcare delle soglie orarie principali della giornata (Alba 0, Mattino 1, Pomeriggio 5, Tardo Pomeriggio 9, Sera 13, Notte 16).
  - Al variare del meteo (o su `/viaggio` verso una nuova zona), il contatore si riallinea alla durata del tragitto o riparte da `(da 1 ora)`.
  - Sul riposo lungo (`/riposo`) e sul comando manuale `/meteo [condizione]`, il contatore si azzera a `(da 0 ore)`.
- **PROSA DIEGETICA DEL CAMBIO AMBIENTALE A INIZIO BEAT:**
  - Quando il meteo cambia O l'Orario varca una soglia di periodo (Alba 0, Mattino 1, Pomeriggio 5, Tardo Pomeriggio 9, Sera 13, Notte 16), le prime 1-2 frasi di prosa del beat descrivono esplicitamente il mutare del cielo, della luce, delle ombre o dell'atmosfera (es. sole calante, torce accese, nubi o pioggia), immergendo i giocatori nell'ambiente prima di dialoghi o azioni.
- **RETROCOMPATIBILITÀ SAVE:**
  - I salvataggi precedenti privi di parentesi (es. `Meteo: Sereno`) vengono letti e interpretati silenziosamente come `(da 1 ora)`, senza pause né errori di caricamento.

05 v2.24 · 06 v6.78 · cv143 · ov78 · lv59 · mv18.

## 2026-09-02c — Disposizione Scenografica Arena, Elementi Illimitati AI e Posizionamento Intelligente Mostri

Evoluzione coordinata tra Table Tool (`combat_tracker.html`), Knowledge Layer (`06` v6.77) e Control Layer (`cv142`, `ov78`, `lv59`):
- **DISPOSIZIONE SCENOGRAFICA IN `#### 🏟️ Arena` (§B8):**
  - Aggiunto il campo opzionale `**Disposizione:**` (o `**Scenografia:**`) subito dopo `Forma:` in `#### 🏟️ Arena`, dedicato a una sintesi in 1-2 frasi della scenografia e della collocazione di nemici/ostacoli.
  - Supportate note descrittive inline su ciascun elemento (`- Elemento — note di dettaglio`).
  - L'AI nel Combat Tracker riceve `Disposizione` e le note di ciascun elemento per arredare la mappa con estrema fedeltà visiva e tattica. Il fallback procedurale ignora il campo e pulisce le note inline senza errori.
- **RIMOZIONE LIMITI QUANTITATIVI ELEMENTI NELL'AI:**
  - L'AI non ha più limiti artificiali (es. "2-4 elementi"): può posizionare quante istanze ritiene opportune per rendere la scena suggestiva, realistica e credibile in base alle dimensioni dell'arena (es. vaste zone o banchi multipli di fango, formazioni di rocce, barriere di radici), preservando lo spazio di manovra e combattimento.
- **POSIZIONAMENTO TATTICO DEI MOSTRI CON AI:**
  - Nel prompt dell'AI vengono passati tutti i mostri dello scontro con relativo ingombro (in caselle).
  - L'AI posiziona i nemici in posizioni coerenti con la narrazione (es. sul retro della caverna, in copertura o in avanscoperta).
  - Regole rigide: l'ingombro deve poggiare interamente su pavimento libero, mai sopra coperture solide o trappole, con rotta di movimento aperta e non intrappolata.
- **FALLBACK PROCEDURALE DEI MOSTRI RISCRITTO (`findEmptySpot`):**
  - Rimosso il limite che forzava i mostri nella sola metà superiore o in una porzione ridotta al 25% dell'arena.
  - Ricerca estesa a tutta la mappa calcolando punteggio di distanza dall'ingresso dei PG, spazio libero circostante e controllo di raggiungibilità BFS verso la porta d'accesso per prevenire nemici bloccati o intrappolati da rocce/muri.
- **PROTEZIONE CORRIDOI INGRESSO & SELEZIONE MODELLO AI:**
  - `isSafeZone` e prompt aggiornati per proteggere porte e interi corridoi/strettoie d'ingresso ($\le 3$ caselle) da coperture solide, impedendo che altari o massi blocchino l'accesso dei PG.
  - Aggiunto selettore modello (`Gemini 2.0 Flash` vs `Gemini 1.5 Pro`) nel modale `🔑 API Key`.
  - `🔄 Rigenera Mappa` ora interroga l'AI per generare un nuovo layout tattico alternativo su richiesta quando l'API key è attiva.

06 v6.77 · cv142 · ov78 · lv59 · mv17.

## 2026-09-02b — Integrazione Fanfara, Gestione API Key, Mappa Tattica AI e Tab Dinamico nel Combat Tracker

Aggiornamento del Table Tool (`combat_tracker.html`), Knowledge Layer (`06` v6.76) e Control Layer (`cv141`, `ov77`, `lv58`):
- **FANFARA DI VITTORIA NEL TRACKER:**
  - Aggiunto pulsante `🎵 Fanfara Vittoria` nell'header in alto a destra del tracker che apre il tema canonico FFXIV su YouTube in una nuova scheda.
  - Rimosso l'obbligo di emissione del link YouTube dall'output dell'assistente in §A23, §B1, §B8 e negli `<output_contract>` dei tre assistenti (il pacchetto incontri si chiude direttamente dopo `#### 💰 Bottino`).
- **GESTIONE DEDICATA API KEY GEMINI:**
  - Aggiunto pulsante `🔑 API Key` nell'header in alto a destra con modal dedicato (`apiKeyModal`) per inserimento, salvataggio in `localStorage`, rimozione e test rapido di connessione e quota (endpoint gratuito Google Gemini `models?key=...`).
  - L'indicatore nell'header segnala graficamente se la chiave è presente e attiva.
- **MENU "GENERA INCONTRO AI" CON DIAGNOSTICA QUOTA:**
  - Rimosso il campo password per l'API key dall'interno della modal Genera.
  - Banner informativo che rileva istantaneamente se la chiave è configurata o se la quota è esaurita (errore 429), bloccando/abilitando coerentemente il pulsante di generazione.
  - Aggiornato l'endpoint a `gemini-2.0-flash` (con fallback automatico a `gemini-1.5-flash`), eliminando il precedente `gemini-3.5-flash` inesistente.
- **POSIZIONAMENTO TATTICO MAPPE AI ALL'IMPORTAZIONE:**
  - Quando si importa un pacchetto incontro tramite `📥 Importa`: se l'API key è memorizzata e valida, il tracker interpella l'AI per posizionare gli elementi d'arredo/ostacoli sul pavimento in modo intelligente e tattico, rispettando ingressi/uscite e note tattiche.
  - In assenza di chiave o in caso di errore di quota/rete, il tracker effettua un fallback fluido e immediato sull'algoritmo procedurale nativo.
- **VISIBILITÀ DINAMICA TAB TATTICA & BOTTINO:**
  - Il tab `🎯 Tattica & Bottino` resta nascosto al lancio iniziale del tracker con scontro vuoto.
  - Compare dinamicamente non appena viene importato o generato uno scontro, o in presenza di nemici/tattiche/bottino caricati.

06 v6.76 · cv141 · ov77 · lv58 · mv16.

## 2026-09-02 — Comando /help agnostico e dinamico nel Control Layer (cv140, ov76, lv57)

Aggiunto il comando `/help` a tutti gli assistenti (`Campaign`, `One-Shot`, `Loremonger`):
- **INTROSPEZIONE DINAMICA DEL ROSTER:** Il comando legge la sezione `<commands>` del proprio file di istruzioni ed elenca tutti i comandi disponibili con sintassi e una breve descrizione su una riga. Non richiede liste hardcodate ed è auto-aggiornante nel tempo.
- **ZERO IMPATTO SUL KNOWLEDGE:** Implementato interamente nel Control Layer (`Instructions_*.txt`), rispettando il principio per cui il RAG non nomina mai i comandi slash.
- **PARITÀ PERFETTA:** Regola identica al carattere su `cv140`, `ov76`, `lv57`.

cv140 · ov76 · lv57 · mv15.

## 2026-09-01f — Riorganizzazione Pacchetto Incontro (1-click code block, Victory Fanfare, tab Tattica & Bottino nel Tracker)

Riorganizzazione coordinata tra Control Layer (`cv139`, `ov75`, `lv56`), Knowledge Layer (`06` v6.75) e Table Tool (`combat_tracker.html`):
- **NUOVA SEQUENZA PACCHETTO INCONTRO (§B1, §B8):**
  1. `### 🗡️ Pacchetto Incontro: <nome>`
  2. `**Difficoltà:**` e `**Innesco:**` (se presente)
  3. `**📖 Da leggere ai PG:**` (prosa narrativa leggibile dal GM, fuori dai code block)
  4. Blocco meccanico per il tracker in UN unico code block copiabile 1-click (```` ``` ````): `**Nemici:**` (roster ×N) $\rightarrow$ `#### 🏟️ Arena` $\rightarrow$ `**Tattica:**` $\rightarrow$ stat blocks completi $\rightarrow$ `#### 💰 Bottino` (con quota Gil per PG e drop) $\rightarrow$ chiusura ```` ``` ````.
  5. Subito sotto il code block: `[🎵 Vittoria: Victory Fanfare](https://www.youtube.com/watch?v=nMNRPmX5Eng)` (§A23).
- **TAB TATTICA & BOTTINO NEL COMBAT TRACKER (`combat_tracker.html`):**
  - Aggiunto tab `🎯 Tattica & Bottino` nel pannello stat block con vista dedicata e modalità di modifica ("✏️ Modifica", salvataggio e annullamento).
  - Parser `processImport()` aggiornato: estrae automaticamente `Tattica` e `Bottino`, separa i testi nelle proprietà dell'incontro (`enc.tactics`, `enc.loot`), evita che la sezione `Bottino` finisca nelle mosse dell'ultimo mostro e genera un titolo di fallback intelligente se l'utente incolla solo il blocco di codice a partire da `Nemici:`.
  - Persistenza garantita nell'export/apertura JSON del tracker.
- **PARITÀ CONTROL LAYER:** `<output_contract>` aggiornato in perfetta parità letterale su `Instructions_Campaign.txt`, `Instructions_OneShot.txt` e `Instructions_Loremonger.txt`.

06 v6.75 · cv139 · ov75 · lv56 · mv14.

## 2026-09-01e — Formattazione pulita blocco Bottino (eliminata ripetizione etichetta inline)

Rifinita la formattazione dell'output della sezione Bottino in `06_Procedures_and_Format.md` (§A21):
- **ELIMINATA LA RIDONDANZA DELL'ETICHETTA INLINE:** Sotto l'intestazione di blocco `#### 💰 Bottino` (o `💰 Bottino`), la riga di contenuto stampa direttamente il bottino risolto (`<quota> Gil a persona (totale: <totale> Gil)[; drop]`) senza ripetere inutilmente il prefisso `💰 Bottino:` all'inizio della riga.
- **PARITÀ CON REGOLE DI FORMATTAZIONE (§A1/§A9):** Le etichette di blocco con emoji identificano la sezione; i campi interni non duplicano il titolo del blocco.
- **COMPATIBILITÀ TABLE & TRACKER:** Piena compatibilità con `combat_tracker.html`, che aggancia il titolo di sezione `Bottino` nello stat block e ne mostra ora l'entrata pulita senza testo duplicato.

06 v6.74 · mv13.

## 2026-09-01d — Snellimento Control Layer (cv138, lv55) e fix orientamento /carica con template tratto connettivo

Audit completo delle istruzioni e snellimento del Control Layer per ridurre il carico cognitivo dei prompt e garantire l'emissione del tratto connettivo al caricamento:

**FIX ORIENTAMENTO AL CARICAMENTO (`/carica` in Instructions_Campaign.txt).**
- Risolto il punto cieco per cui `⏭️ Tratto connettivo` veniva omesso al `/carica`: la specifica telegrafica precedente (`pending 🧭 and ⏭️ lines if present`) non forniva al modello né la condizione attiva ($N \ge 2$) né il template della riga, e poiché `/carica` non è un beat narrativo il modello non leggeva la sezione `<beat>`.
- Inserita direttamente nella specifica di `/carica` la clausola attiva e il template completo: `if 08 chain ahead has 2+ [COND] quests: ⏭️ Tratto connettivo: da {q1} a {q2} — {N} quest condensabili, poi si gioca {STOP} (~X min giocate / ~Y riassunte)`.

**SNELLIMENTO & DEFATICAMENTO ISTRUZIONI (`Instructions_Campaign.txt` cv138).**
- *Asciugatura aritmetica Orario*: rimosse le formule matematiche duplicate su `/continua`, `/svolta`, `/riassumi` e `/viaggio`, lasciando solo i delta essenziali ed evitando distrazioni cognitive.
- *Compattazione specifica footer (riga 46)*: ridotto il blocco da 840 a ~460 caratteri asciutti ed esatti, eliminando formulazioni prolisse e delegando le casistiche estese a `06 §B2` e `05 Ch.14.6`.
- *Riduzione dimensione file*: ridotto il peso di `Instructions_Campaign.txt` di circa 800 byte (da 12.463 B a 11.670 B).

**ALLINEAMENTO ISTRUZIONI CONDIVISE (`Instructions_Loremonger.txt` lv55).**
- Aggiornato `/negozio` in Loremonger per supportare `[tipo]` includendo la categoria `cavalcature` aggiunta di recente nel manuale.
- `Instructions_OneShot.txt` verificato: già sincronizzato al 100% nei blocchi comuni.

05 v2.23 · 06 v6.73 · cv138 · lv55 · mv12.

## 2026-09-01c — Integrazione Sistema Meteo (condizioni canoniche, pericoli ambientali 5e e salvataggio pulito)

Introdotto il sistema completo del meteo (`Meteo`) per la Campagna, integrando le condizioni atmosferiche canoniche di FFXIV (da Gamer Escape e ConsoleGamesWiki) sia come abbellimento narrativo per le condizioni standard, sia con regole meccaniche D&D 5e per il tempo avverso, con salvataggio persistente e aggiornamento dinamico:

**DATI CANONICI REGIONALI (05 Ch. 14.7 & 06 §A3).** Roster meteorologici specifici per regione e zona:
- *La Noscea*: Clear Skies (Sereno ☀️), Fair Skies (Soleggiato 🌤️), Clouds (Nuvoloso ☁️), Fog (Foschia 🌫️), Rain (Pioggia 🌧️), Wind (Vento 💨), Gales (Burrasca 💨).
- *The Black Shroud*: Clear Skies (Sereno ☀️), Fair Skies (Soleggiato 🌤️), Clouds (Nuvoloso ☁️), Fog (Nebbia fitta 🌫️), Rain (Pioggia 🌧️), Thunder (Tuoni 🌩️), Thunderstorms (Temporale ⛈️), Tension (Tensione / Odin ⚡).
- *Thanalan*: Clear Skies (Sereno ☀️), Fair Skies (Soleggiato 🌤️), Clouds (Nuvoloso ☁️), Fog (Foschia 🌫️), Dust Storms (Tempesta di sabbia 🌪️), Heat Waves (Ondata di calore 🏜️).
- *Coerthas*: Snow (Neve ❄️), Blizzards (Tormenta / Bufera 🌨️), Fog (Nebbia gelata 🌫️), Clouds (Coperto ☁️), Clear Skies (Sereno gelido ☀️), Fair Skies (Soleggiato 🌤️).
- *Mor Dhona*: Clouds (Nuvoloso ☁️), Fog (Nebbia 🌫️), Gloom (Foschia eterea / Gloom 🌌).
- Espansioni successive (HW, SB, ShB, EW): attingono ai fenomeni eterei canonici dalle wiki (es. Umbral Static, Everlasting Light, Apocalypse).

**EFFETTI MECCANICI DEL TEMPO AVVERSO (5e).**
- *Pioggia battente / Nubifragio (🌧️)*: area leggermente oscurata (svantaggio a Percezione basata su vista o udito), fiamme libere non magiche estinte, svantaggio agli attacchi con armi a distanza oltre la gittata normale, sentieri sterrati diventano terreno difficile (fango).
- *Temporale (⛈️)*: effetti della pioggia battente + tuoni costanti (svantaggio automatico a prove di udito) e pericolo fulmini all'aperto.
- *Nebbia fitta / Foschia / Gloom (🌫️)*: area pesantemente oscurata oltre 6 yalm (9m); svantaggio a Sopravvivenza per orientarsi fuori sentiero.
- *Tempesta di sabbia (🌪️)*: pesantemente oscurata; TS Costituzione CD 10 ogni ora senza protezioni a occhi e volto o svantaggio a Percezione e tiri per colpire; dune come terreno difficile.
- *Ondata di calore (🏜️)*: Caldo estremo (DMG 5e), TS Costituzione CD 10 ogni ora con armature medie/pesanti o senza razione doppia d'acqua o 1 livello di sfinimento.
- *Tormenta / Bufera (🌨️)*: Freddo estremo (DMG 5e), TS Costituzione CD 10 ogni ora senza abiti invernali pesanti o 1 livello di sfinimento; pesantemente oscurata oltre 6 yalm; cumuli di neve come terreno difficile; svantaggio ad attacchi a distanza.
- *Burrasca (💨)*: vento forte, velocità di volo dimezzata/arrestata (prova di Forza CD 13 per avanzare); svantaggio ad attacchi a distanza.

**DINAMICHE TEMPORALI & RIPOSO LUNGO.**
- *Avanzamento diurno*: il meteo evolve naturalmente al passaggio delle fasce orarie o dopo 2-3 beat identici.
- *Transizione di zona (`/viaggio`)*: adotta una condizione canonica della zona di arrivo.
- *Riposo lungo (`/riposo`)*: azzera l'Orario a 0 e RIGENERA SEMPRE il meteo per la nuova alba (Alba 7:00 🌅), pescando tra quelli canonici della zona.
- *Comando GM (`/meteo [condizione]`)*: comando di servizio per consultare o impostare il meteo al tavolo.

**FORMATO OUTPUT & IGIENE SAVE (NO EMOJI NEL SAVE).**
- *Blocco Save [B]*: solo testo pulito senza emoji: `- Meteo: Sereno`. Salvataggi precedenti senza Meteo propongono `Meteo: Sereno` in modo trasparente e non bloccante.
- *Footer dei Beat*: integrato simmetricamente sulla stessa riga di Orario con emoji posizionata DOPO il meteo:
  `⏱️ Orario: 5 → 6 (+1) — Pomeriggio (13:00) 🌤️ · Meteo: Pioggia battente 🌧️ [Visibilità ridotta]`
  `⏱️ Orario: N → 0 (riposo) — Alba (7:00) 🌅 · Meteo: Sereno ☀️`

**RISOLUZIONE DEL CURSORE AL CONFINE DI QUEST AL `/carica` (06 §B1 & §B2).** Esplicitata la regola procedurale per cui, se l'`Ultimo step completato` del save chiude la missione [A], il cursore attivo è posizionato alla soglia della prima quest da giocare sull'indice 08: il controllo dei segnali pendenti (`🧭 Viaggio` e `⏭️ Tratto connettivo` per N ≥ 2) viene valutato obbligatoriamente su tale quest entrante, evitando che il modello ometta il tratto connettivo basandosi sul nome della quest precedente ormai chiusa.

**VERSIONI & FILE AGGIORNATI.**
- `Instructions_Campaign.txt`: `cv137`.
- `06_Procedures_and_Format.md`: `v6.73`.
- `05_Campaign.md`: `v2.23`.
- `Project_Memory.md`: `mv12`.
- `CHANGELOG.md`: aggiunto record `2026-09-01c`.

05 v2.23 · 06 v6.73 · cv137 · mv12.

## 2026-09-01b — Stat block Chocobo, equipaggiamento cavalcature, negozio CAVALCATURE e tariffe trasporti

Integrati gli stat block completi dei 3 tipi di Chocobo cavalcabili, le regole e la tabella dell'equipaggiamento per cavalcature, il nuovo tipo di negozio `CAVALCATURE` e la tabella ufficiale delle tariffe trasporti di Eorzea:

**STAT BLOCK CHOCOBO (01_Manual.md).** Codificati i 3 esemplari per i PG:
- **Chocobo da Soma (Draft Chocobo)**: Bestia Grande, GS 1/4, CA 10, PF 19, Vel 8 yalm (12m). Forza 18, capacità di traino e carico raddoppiata (fino a 245 kg carico, 1.225 kg traino). Docile e pauroso, fugge se attaccato.
- **Chocobo da Sella (Riding Chocobo)**: Bestia Grande, GS 1/4, CA 11, PF 19, Vel 12 yalm (18m / 60 ft). Cavalcatura timorosa: in combattimento disarciona e fugge a meno di superare una prova di Saggezza (Addestrare Animali) CD 13 come reazione.
- **Chocobo da Battaglia (Battle Chocobo)**: Bestia Grande, GS 1/2, CA 12 (naturale), PF 34, Vel 12 yalm (18m). Addestrato alla guerra (agisce in iniziativa a fianco del padrone, vantaggio contro spaventato). Multiattacco (Becco + Calcio con TS Forza CD 13 per non cadere proni) e reazione bonus *Choco Drop* su proni. *Legame con l'Erba Gysahl*: nutrito con 1 fascio (5 Gil), ottiene 10 PF temporanei e +1 al tiro per colpire per 1 ora.

**EQUIPAGGIAMENTO CAVALCATURE & BARDATURE.** Aggiunta tabella completa con prezzi, pesi ed effetti: Selle (viaggio 25–40 Gil; militare 60 Gil con vantaggio a non cadere), Sacche da sella (15 Gil, +50 kg), Bardature (leggera in cuoio 75 Gil [+1 CA]; pesante in acciaio 200–350 Gil [+3 CA, svantaggio Furtività]), Stallaggio in locanda/scuderia (1–2 Gil/notte) ed Erba Gysahl (5 Gil a fascio).

**NUOVO NEGOZIO `CAVALCATURE` (06 §A22).** Aggiunto tra i tipi di negozio invocabili (`ARMI / ARMATURE / ACCESSORI / CAVALCATURE / CONSUMABILI / GENERALE`). Vende cavalcature permanenti, selle, bardature, sacche, Erba Gysahl e stallaggio. Regola di separazione: il noleggio temporaneo NON si acquista al banco, ma è gestito in automatico da `/viaggio chocobo`.

**TARIFFE TRASPORTI DI EORZEA & REGOLA 2+ ZONE.**
- Traghetti locali e costieri: 5–15 Gil (chiatte interne: 10–20 Gil).
- Navi d'alto mare: 30–50 Gil (200–500 Gil rotte pericolose/lunghe es. Kugane).
- Aeronavi di linea Highwind Skyways: 75–100 Gil (Pass d'Aeronave MSQ Lv 15; charter privato: 500–1.500 Gil).
- Noleggio Chocobo: 1 zona (tratta breve tra avamposti) = 10–15 Gil a persona | 2+ zone o intera giornata = 20–25 Gil/giorno forfettario a persona (con 50 Gil cauzione restituita al rientro). Con cavalcatura propria = 0 Gil di nolo.

**IGIENE E PARITÀ.** Aggiornato `01_Manual.md`, §A22 e §B2 in `06_Procedures_and_Format.md` (v6.72), Ch. 12.7 in `05_Campaign.md` (v2.22), §1.8 in `Project_Memory.md` (mv11). `Instructions_Campaign.txt` resta asciutto a cv136.

05 v2.22 · 06 v6.72 · cv136 · mv11.

## 2026-09-01 — Bottino in Gil a persona (diviso per Numero PG)

Introdotta la formattazione obbligatoria del bottino monetario espressa a persona dividendo per il numero di giocatori (`N PG` da save [B] / riga `⚔️ Rif. gruppo`), garantendo che la somma delle quote individuali corrisponda esattamente al totale dichiarato:

**FORMATO OUTPUT BOTTINO IN GIL.** La riga `💰 Bottino:` stampa la quota individuale seguita dal totale:
- Esempio: `💰 Bottino: 25 Gil a persona (totale: 100 Gil); oggetto: 1 Pozione di Cura` (o `35 Gil a persona (totale: 140 Gil)`).
- Si applica esclusivamente al denaro (solo Gil); consumabili, parti di mostro ed equipaggiamento mantengono la loro assegnazione discreta.

**INVARIANTE DELLA SOMMA ESATTA (`quota × N = Totale`).**
- Quando il tiro dei dadi dal band CR non è esattamente divisibile per N PG, il totale viene arrotondato al multiplo più vicino di N PG per garantire quote intere e pulite al tavolo senza decimali.
- Se una ricompensa fissa di quest è intrinsecamente non divisibile, il resto viene assegnato alla cassa comune del party (es. `33 Gil a persona (+1 Gil fondo cassa, totale: 100 Gil)`).

**IGIENE E PARITÀ.** Aggiornato §A21 in `06_Procedures_and_Format.md` (v6.71), Ch. 12.2 in `05_Campaign.md` (v2.21), §1.8 in `Project_Memory.md` (mv10). `Instructions_Campaign.txt` resta inalterato a cv136 per rispetto del principio di igiene (formati derivati dal RAG).

05 v2.21 · 06 v6.71 · cv136 · mv10.

## 2026-08-31c — Riprogettazione comando `/svolta` (ex `/esito`) con generazione immediata del beat

Riprogettato il meccanismo delle deviazioni diegetiche e delle scelte impreviste dei giocatori: ritirato il vecchio comando passivo `/esito` e introdotto **`/svolta`**, che genera immediatamente un beat narrativo giocabile basato sull'input del GM:

**GENERAZIONE IMMEDIATA DEL BEAT NARRATIVO.** `/svolta` entra nel novero dei comandi che producono prosa narrativa e tag di beat (`ONLY /continua, /riassumi, /viaggio, /riposo, /svolta`):
- Il comando risponde **immediatamente** generando la scena `[MSQ — Svolta: {situazione}]` (o `[SUBQUEST — Svolta: {situazione}]` se una SQ è ATTIVA).
- Non richiede più un successivo `/continua`: la reazione del mondo e le conseguenze dell'azione dei PG si giocano nel turno stesso.

**DUE LIVELLI DI LIBERTÀ DIEGETICA (MSQ vs SUBQUEST).**
- **Nella MSQ (Massima Flessibilità di Approccio, Invarianza dei Pilastri)**: I giocatori hanno piena libertà di approccio ai singoli ostacoli (fuga, diplomazia, corruzione, inganni, rifiuti temporanei). Nessun retcon, nessun rimprovero meta; il mondo reagisce realisticamente e la pressione narrativa riconduce organicamente ai nodi obbligati dell'MSQ (pilastri, duty instanziate, rivelazioni/cristalli 08.1).
- **Nelle Subquest (Libertà Totale e Sovvertimento)**: Le missioni secondarie possono essere stravolte, deviate, fallite, tradite o risolte in modi alieni. Il beat gestisce il fallout locale, aggiorna lo stato della Subquest in [C] (anche portandola a conclusione anticipata/fallita) e libera il campo per il rientro in MSQ.

**CURSORE E ORARIO.**
- Il cursore narrativo si riallinea allo step coerente con la nuova situazione.
- L'orario di campagna avanza in base all'attività del beat (+1 narrativo / +2 con combattimento o inseguimento/fuga concitata).

**CONTINUITÀ NARRATIVA E PASSAGGIO DI CONSEGNE SCENICO.** Aggiunta in §B1 la regola output-forcing `SCENE HANDOVER & NPCS IN MOTION`: quando un beat si conclude aprendo lo step successivo, la chiusura narrativa (dopo dialoghi, prove o bottino) deve descrivere la transizione e mettere in moto i PNG (es. il PNG che si avvia in anticipo verso la grotta/scogliera o le tracce che si allontanano), eliminando i salti di teletrasporto dei PNG tra turni consecutivi.

**PREFISSO EXPORT SAVE CODE BLOCK (`/carica`).** Allineato il template di esportazione del blocco save su `/salva`: il blocco di codice markdown emesso contiene `/carica` sulla prima riga (invece di `/continua`), in modo che incollando il blocco in una nuova chat venga immediatamente e correttamente eseguito il comando `/carica` per l'inizializzazione e l'orientamento.

**IGIENE E PARITÀ.** Aggiornato `Instructions_Campaign.txt` (cv136), §B1, §B3, §B17 e §B24 in `06_Procedures_and_Format.md` (v6.70), `05_Campaign.md` (v2.20), §1.8 e tabella quarantena in `Project_Memory.md` (mv9).

05 v2.20 · 06 v6.70 · cv136 · mv9.

## 2026-08-31b — Ricalibrazione economica 5e trasporti e semplificazione comando `/viaggio`

Ricalibrate le tariffe dei trasporti per allinearle all'economia standard di D&D 5e (`1 Gil = 1 gp`) e semplificata la gestione del comando `/viaggio`:

**SEMPLIFICAZIONE COMANDO `/viaggio` E COSTI IN TESTA AL BEAT.** L'unica scelta manuale per il party via terra è tra viaggio a piedi e con Chocobo:
- `/viaggio` (senza argomenti): default automatico a piedi.
- `/viaggio chocobo`: viaggio rapido a dorso di Chocobo per le tratte terrestri.
- Tratte marittime, fluviali e aeree (barche, navi d'alto mare, aeronavi): fisse e obbligate dalla rotta/geografia, integrate e risolte automaticamente nel montaggio narrativo del viaggio senza richiedere parametri manuali.
- Viaggi multitratta con Chocobo: il costo del noleggio Chocobo (2 Gil a persona) viene addebitato per ciascuna tratta terrestre distinta (es. Chocobo + Nave + Chocobo = 2 Gil + 5 Gil + 2 Gil = 9 Gil a persona).
- **Riepilogo spese in testa al beat**: se la tratta comporta costi (> 0 Gil), viene stampata subito sotto l'intestazione la riga `💰 Spesa: N Gil a persona (dettaglio: ...)`; se il viaggio è a piedi a costo zero (0 Gil), la riga viene omessa.

**RICALIBRAZIONE ECONOMICA 5e DEI TRASPORTI.** Prezzi convertiti dai valori MMO a cifre calibrate e sostenibili per l'economia 5e:
- Barca comune / traghetto locale: 1 Gil a persona.
- Noleggio Chocobo (Chocobokeep / nolo per singola tratta tra avamposti): 2 Gil a persona / tratta.
- Nave oceanica di linea (es. Limsa ↔ Vesper Bay): 5 Gil a persona.
- Volo aeronave di linea Highwind Skyways: 10 Gil a persona (sblocco MSQ Lv 15).
- Acquisto Chocobo permanente da sella: 150 Gil (finimenti inclusi; o licenza Grand Company MSQ Lv 20).

**IGIENE E PARITÀ.** Aggiornato `Instructions_Campaign.txt` (cv135), Ch. 8.5 in `05_Campaign.md` (v2.19), §A22 e §B26 in `06_Procedures_and_Format.md` (v6.68), e §1.8 in `Project_Memory.md` (mv8).

05 v2.19 · 06 v6.68 · cv135 · mv8.

## 2026-08-31 — Calcolo tempo di viaggio diegetico, costi trasporti e save code block con `/continua`

Aggiornato il calcolo del tempo trascorso durante i viaggi convenzionali (`/viaggio`) e introdotto il listino trasporti di Eorzea:

**AVANZAMENTO ORARIO PER DISTANZA E MEZZO DI TRASPORTO.** Il viaggio diegetico consuma tempo in base alla tratta percorsa:
- Viaggio a piedi: +1 ora per ogni zona attraversata.
- A dorso di Chocobo / carrozza: +1 ora ogni 2 zone attraversate (minimo 1 ora). Passo rapido su strada; permette disingaggio/fuga rapida su agguati terrestri senza spendere risorse o Vantaggio all'Iniziativa.
- Volo in aeronave interregionale (Highwind Skyways): +2 ore.
- Nave d'alto mare / traghetto oceanico (es. Limsa ↔ Vesper Bay): +2 ore.
- Barca comune / traghetto fluviale o costiero locale: +1 ora.
- Viaggi multitratta (misti): montaggio unico e fluido, durata pari alla somma delle singole tratte, riepilogo costi in Gil e un unico Travel Check (1d20) ambientato sulla tratta più esposta.
- Parametro opzionale comando: `/viaggio [chocobo | aeronave | nave | a piedi]`.

**LISTINO SERVIZI DI TRASPORTO (Gil a persona / tratta).** Codificate le tariffe canoniche dei trasporti: barca locale 5–10 Gil; noleggio Chocobo (Chocobokeep) 15–25 Gil; nave oceanica di linea 30–50 Gil; volo aeronave di linea 100–120 Gil; Chocobo permanente 300–500 Gil (o licenza Grand Company MSQ Lv 20).

**FORMATO EXPORT DEL SAVE IN CODE BLOCK CON `/continua`.** Sul comando `/salva`, il blocco di salvataggio viene emesso all'interno di un unico blocco di codice markdown (fenced code block) preceduto da `/continua` sulla prima riga (`/continua` + `=== SAVE === ... === FINE SAVE ===`), consentendo al GM di copiare l'intero blocco con il pulsante "Copia" e incollarlo direttamente in una nuova chat per riprendere subito a giocare.

**IGIENE E PARITÀ.** Aggiornato il comando `/viaggio` e `/salva` in `Instructions_Campaign.txt` (cv133), §A22, §B17, §B24 e §B26 in `06_Procedures_and_Format.md` (v6.66), Ch. 8.5, Ch. 14.6 e Ch. 19.3 in `05_Campaign.md` (v2.17), e §1.8 in `Project_Memory.md` (mv7).

05 v2.17 · 06 v6.66 · cv133 · mv7.

## 2026-08-30 — Evoluzione tracking orario: coerenza in prosa, salti MSQ, /riposo breve e /attesa

Aggiornato il sistema dell'orario di campagna (`[B] Orario: 0-24`) per renderlo diegeticamente attivo e flessibile:

**COERENZA DELL'ATMOSFERA COL MOMENTO DELLA GIORNATA.** Il momento della giornata (Alba 🌅 0, Mattino ☀️ 1-4, Pomeriggio 🌤️ 5-8, Tardo Pomeriggio 🌇 9-12, Sera 🌆 13-15, Notte 🌙 ≥16) non è più solo una riga nel footer: si integra naturalmente nella descrizione ambientale, nella luce, nelle ombre e nel fermento della scena all'interno della prosa, quando serve.

**SALTO TEMPORALE GUIDATO DA MSQ / SQ (QUEST-FORCED TIME JUMP).** Quando uno step di missione richiede o racconta un momento specifico (es. attendere la sera per un banchetto, la notte per un'infiltrazione, l'alba per un incontro), l'orologio non incrementa con il normale conteggio del beat ma salta all'inizio della fascia oraria target (Alba 0, Mattino 1, Pomeriggio 5, Tardo Pomeriggio 9, Sera 13, Notte 16), segnalando il salto nel footer (`attesa MSQ: {periodo}`).

**RIPOSO BREVE (`/riposo breve`).** Introdotto il comando dedicato per il riposo breve (1 ora): risposta secca di una sola riga, gestione meccanica di Dadi Vita e slot a carico del tavolo come da 5e base, `Orario +1`, nessun beat narrativo. Distinto da `/riposo` che gestisce il riposo lungo prosato con alloggio/bivacco e reset a 0.

**COMANDO ATTESA GENERICA (`/attesa [N ore | periodo]`).** Introdotto il comando di avanzamento orario libero per gestire le attese del gruppo: risposta di una sola riga, avanza l'orologio di N ore o fino alla fascia richiesta.

**ABILITÀ TELEGRAFATE: COLPISCONO SEMPRE (NO TIRO PER COLPIRE, NO TS).** Le azioni nemiche dotate di `Telegrafo:` non usano mai un tiro per colpire (+N al tiro) né concedono Tiri Salvezza: avendo fornito preavviso e finestra di reazione, colpiscono automaticamente chiunque resti nell'area o non attui contromisure/mitigazioni. La contromossa è puramente posizionale e tattica. Gli attacchi base non telegrafati mantengono i normali tiri per colpire.

**IGIENE E PARITÀ.** Rimossa riga duplicata in `Instructions_Campaign.txt` L.43; aggiornati i binding di ruolo (`the short-rest command`, `the wait command`) in cv e 06; allineati §A3, §B1, §B10 e §B28 in 06, Ch. 9.3, 9.6, 14.5/14.6 in 05, e §1.8/§1.10 in PM.

05 v2.14 · 06 v6.63 · cv131 · mv4.

## 2026-08-17b — Revisione delle modifiche; l'ultima invocazione scritta per esteso

**REVISIONE.** Riletto tutto quello che avevamo toccato oggi contro le regole del progetto. Quattro
punti erano scritti male, tutti nostri:
- **adiacenza.** La parola 'act' era rimasta accanto al marcatore di parte in DUE punti; ne avevamo
  ripristinato uno solo, e l'output aveva prodotto '— Fine atto 1 —'. Ora zero occorrenze di
  act/atto entro 90 caratteri dal marcatore.
- **G29 spiegava invece di prescrivere** ('that is what tells the players…', 'so a qualifier always
  exists…'). La giustificazione sta in chat e qui, mai nel knowledge. La voce perde un terzo.
- **la riga del volume** aveva prosa nella colonna che ovunque contiene un'unita': ora `*none*`.
- **l'ancora del fulm era ristretta ai corpi** ('a body height') mentre la riga copre tutte le
  altezze: misurato, funzionava sulle persone e falliva su soffitti e creature. Ora 'EVERY height'.

**L'ULTIMA INVOCAZIONE SCRITTA PER ESTESO.** 06 chiamava 'mappa MSQ' per nome, 5 volte, mentre ogni
altro comando e' chiamato per ruolo (the play command ×46, the travel command ×19, the bridge
command ×18). Diventa **the flow-map command**, e la mappa e' dichiarata in cv E in lv — senza il
binding la regola sarebbe invisibile, che e' il modo esatto in cui avevamo perso 67 regole. La forma
estesa del comando ('+' / 'prossimo') resta documentata come argomento, non come nome.

Nella stessa frase c'era anche l'ultima negazione che disegna il nome dell'artefatto ('NO reveal
box'): rimossa, la forma positiva era gia' nella riga.

06 v6.60 · 07 v1.40 · cv125 · lv54.

## 2026-08-17 — Merci per origine; il numero della parte; il fulm senza ancora

Tre difetti misurati su run consecutive della stessa one-shot, tre cause diverse.

**IL RUM GIAMAICANO ERA UN VUOTO, NON UNO SBAGLIO.** 07 aveva i demonimi e i luoghi ma nessuna
regola che li collegasse alle merci: servendo un aggettivo per il rum, il modello pescava dalla
Terra. Nuova **G29**: le merci si nominano per origine, e il qualificatore si prende da G8/G9 —
forma generativa, non una lista da mantenere, con la clausola di scarico che una merce senza
origine e' comunque una merce. Misurato alla run successiva: 'rum di Vylbrand', e la forma si e'
estesa da sola a 'Rum Pregiato di Portobirra'.

**'— Fine parte 1 —' ALLA FINE DELL'ATTO 2.** L'unico esempio funzionante del marcatore in tutto
il corpus stava nella regola sullo split dei dungeon, con l'uno scritto dentro. Il modello copiava
il letterale invece di calcolare N. Riscritto senza cifra: il numero e' sempre quello del pezzo che
chiude. Corretto alla run successiva.

**L'ULTIMO ATTO NON CHIUDEVA SUL MARCATORE.** Contraddizione fra i livelli: ov dice 'LAST, ALWAYS',
06 restringeva a 'dungeon-split / unfinished beat / finale only' — tre situazioni scritte nel
vocabolario della Campagna, nessuna delle quali e' l'ultimo atto di una one-shot. Un ambito
enumerato batte un 'sempre' generico. Aggiunto il caso mancante.

**IL FULM NON AVEVA UN'ANCORA.** Uscivano '4 fulm (4m)' e '5 fulm (5m)' per la stessa creatura: il
fattore in §A2 era giusto ma il modello non aveva da dove partire, quindi immaginava un'altezza in
metri e ci appiccicava l'unita'. Lo yalm non sbaglia mai perche' ha il quadretto. Data al fulm la
stessa cosa: un Hyur adulto e' alto ~6 fulm, e le stature scalano su una persona.

**ETICHETTE DEL PITCH.** Tre run, tre set di emoji diversi, perche' il template di §C4 elencava
i blocchi in maiuscolo senza icona. Ora le porta scritte: `🎬 Sinossi` · `🪝 Aggancio` ·
`🎭 Dramatis Personae` · `📑 Indice degli Atti`. 🎬 e non 📜 perche' 📜 e' gia' Lore a Strati:
un'icona, una cosa. Dichiarate SOLO in 06, mai nelle istruzioni.

**DIMENSIONI: SI LASCIA COSI'.** Il campo oscilla fra '14 × 14' e '14 × 14 yalm' perche' il template
dice 'written BARE' e la tabella di §A2 lo elenca fra i campi in yalm. Decisione del GM: vanno bene
entrambe, il tracker le accetta entrambe, e riconciliare le due regole rischia piu' di quanto renda.

06 v6.55 · 07 v1.39.

## 2026-08-16 — Le scatole disegnate spariscono dal corpus; il pacchetto incontro si dichiara chiuso

Nei test continuavano a comparire diagrammi ASCII: uno schema dell'enigma e una mappa, infilati fra un
blocco e l'altro del pacchetto incontro. La caccia al divieto mancante ha trovato invece il contrario.

**LA FONTE ERA UN USO, NON UN DIVIETO.** 05 e 08 contenevano tre scatole VERE —
`>>> SPOILER (GM ONLY - ...) <<<` — piu' la riga che ne documentava la convenzione. Il corpus non
proibiva quella forma: la usava. I due divieti in 06 la ridisegnavano per vietarla, aggiungendo due
occorrenze in piu'. Tutte convertite in etichetta in grassetto: stessa semantica, nessun disegno.

**LA FORMA DEL PACCHETTO ERA APERTA.** L'ordine dei blocchi dichiarava l'esaustivita' solo in
posizione («nient'altro SOPRA il read-aloud»), mai globalmente: elencava cosa mettere senza mai dire
che l'elenco fosse completo. E' negli spazi fra i blocchi che finivano i disegni. Ora la regola dice
che quei blocchi SONO il pacchetto, che nulla si inserisce fra loro e nulla segue l'ultimo.

**NEGAZIONI RIMOSSE.** `no table or pipes`, `no grid is drawn`, `never pipes/table/columns`,
`NEVER a pipe table`: nominavano l'artefatto che vietavano, e la forma positiva sta gia' in §A1
(frasi, etichette in grassetto, link). Tolta anche la razionalizzazione «printing them PRIMES the
model»: la knowledge non spiega perche'.

05 v2.12 · 06 v6.52 · 08 v3.54.

## 2026-08-13i — Tracker: gli sgherri evocati si mettono sul tabellone con un clic

Un boss che evoca creature descrive le loro statistiche DENTRO l'abilita', in una capsula come
`(Imp del Vuoto: Piccola creatura del Vuoto; CA 12; PF 7 (2d6); Vel 6 yalm, volare 6 yalm; Artigli +4
…)`. Prima andavano ricreate a mano in mezzo allo scontro.

**RILEVAMENTO.** Una mossa che contiene sia `CA <n>` sia `PF <n>` sta descrivendo una CREATURA, non un
effetto: e' la firma. Su quella riga compare il pulsante, all'inizio.

**COSA SI ESTRAE, E COSA NO.** Solo le quattro cose che servono al tabellone — nome (fra la parentesi e
i due punti), CA, PF, quanti (la parola prima del nome, in cifre o in lettere). **Il resto resta testo
opaco**: strutturare l'abilita' sarebbe una scommessa persa, visto che la forma cambia a ogni
generazione. La descrizione finisce nella scheda dello sgherro, una riga per segmento, per VEDERE cosa
fa — non per essere interpretata.

**NUMERAZIONE PROGRESSIVA.** Nascono sempre numerati e si riprende dal piu' alto gia' presente: la
seconda evocazione continua con 3 e 4 invece di creare due omonimi. Senza, sarebbero indistinguibili in
iniziativa e sulla mappa, e col medesimo colore (che si assegna per nome base).

**NIENTE LOOP.** Una scheda generata porta un contrassegno e non mostra mai il pulsante: la sua stessa
descrizione contiene CA e PF, quindi ogni sgherro sarebbe stato un generatore di sgherri.

**PULIZIA DELLA DESCRIZIONE.** Via l'involucro `(Nome: …)`, una riga per segmento, e la punteggiatura
di giunzione tolta a fine riga — anche perche' un punto finale faceva leggere il segmento come 'titolo
di mossa' e lo stampava in rosa. Due protezioni: si taglia su `, ; .` **solo se non segue una cifra**
(cosi' `1,5m` e `4 (1d4+2)` restano interi, e gli attacchi non si spezzano a meta'), e la parentesi
chiusa si rimuove **solo se ce n'e' una in piu' delle aperte** (cosi' `PF 7 (2d6)` sopravvive).

**DUE GUASTI DI SCRITTURA INTERCETTATI PRIMA DEL RILASCIO.** Quattro `` delle regex diventati
caratteri di backspace reali, e una classe di caratteri chiusa male (`[\]\]`) che lasciava aperto un
letterale regex — quest'ultima vista da VS Code. Riparate rimuovendo la RegExp costruita da stringa,
che era la sola parte a richiedere quell'escaping: il conteggio ora usa una ricerca semplice.


## 2026-08-13h — Audit del rumore su tutti i file, flag Eterite 💎, bottino 💰

**AUDIT DEL RUMORE (05, 06, 07, 08, 01).** Il primo conto diceva 7,7% di cronaca in 06. Era sbagliato:
sommava le frasi INTERE che contengono un marcatore, ma in quelle frasi il marcatore introduce
l'esempio dell'output sbagliato, e **l'esempio e' la regola** — test della fonte di [2.39], e [2.26] ha
misurato che una forma batte un divieto. Il rumore vero era lo **0,07%**.

Tolto: **25 annotazioni di provenienza** — `(observed)`, `(observed, Toto-Rak)`, `(measured)` — in due
modi diversi: via del tutto quando erano etichette secche, ridotte alla sola parola quando la parentesi
conteneva l'esempio (`(observed: 'Coeurl a Nove Code — Media'…)` → `('Coeurl a Nove Code — Media'…)`).
Nessun esempio toccato. Piu' l'unica cronaca del corpus, in 08: *«the older loosely-worded envoy
sub-steps previously here are removed»*. **−551 caratteri.**

NON toccati, e la ragione: le 37 failure shape (errori che il modello rifa' da solo) e i sei blocchi
`RATIONALE`, di cui **due non sono motivazioni ma regole** — uno dice dove va la spiegazione di una
mossa, l'altro regge l'esistenza della sezione Arena. **01_Manual: zero rumore**, i tre riscontri erano
`used to` nel senso di «impiegato per».

**FLAG ETERITE, riattivato e vincolato.** §B23 lo aveva gia' ma era irraggiungibile: sta in una sezione
sul SAVE, e chi scrive un beat pesca §A3/§B1. Ora §A3 (descrizione del luogo) lo richiama, e la regola
dice **💎 accanto al NOME DELL'ETERITE**, che porta il nome del suo insediamento ed e' quello che i
giocatori si annotano — mai una locanda o un quartiere interno. Failure shape misurata: 💎 finito su
'Il Baldacchino di Carline' invece che su 'Nuova Gridania'. Copre arrivo, transito e zona vicina.

**BOTTINO 💰.** La moneta precede sempre l'etichetta, intestazione o riga in linea, dichiarata dove le
etichette si definiscono (§A1) e propagata ai dieci punti che la mostrano. **Il tracker riconosceva
`Bottino` con regex ANCORATE**: rese opzionali alla moneta in tutte e tre, cosi' i pacchetti gia'
salvati continuano a importarsi.

**🎵** query rimessa nell'ordine giusto: `FFXIV OST <traccia>`.

06 v6.45 · cv121 / lv50 / ov70.


## 2026-08-13g — 50 regole di 06 erano scritte per un comando senza nome; tracker; 🎵 su ricerca Google

**LA RICOSTRUZIONE DELLE PERIFRASI (la scoperta grossa).** `/viaggio` non compariva mai. Causa: il
commit `c18670e` del 10 agosto, che tolse i nomi dei comandi da 06 per curare Flash, aveva convertito
**50 occorrenze** in un segnaposto generico, `the relevant command`, che non nomina nulla. Regole intere
erano diventate tautologie — *«the relevant command lo salta, the relevant command lo gioca»* per le due
opzioni del viaggio; *«una subquest ATTIVA BLOCCA the relevant command ... the relevant command avanza la
subquest»* per tre comandi diversi. Ricostruite dal file PRECEDENTE alla sostituzione, non a indovinare:
34 erano `continua`, 10 `riassumi`, 4 `viaggio`, piu' due lette dal contesto e tre doppi articoli.
Riscritte con le perifrasi di ruolo (1.4: la knowledge non nomina i comandi), tutte gia' legate in cv.
**Misurato dal GM: `/viaggio` compare e funziona**, in un test da 12 quest con due viaggi, un riposo e
un ponte narrativo.

**§B1/§B8 allineate a 06.** cv elencava la condizione per `Prossimo beat:`, 🧭 e ⏭️ ma non per il
marcatore `— Fine parte N —`, che 06 vuole solo a beat incompiuto: ora concordano. E il read-aloud del
pacchetto era l'UNICA parte nominata descrittivamente invece che con la sua etichetta — ora e'
`**Da leggere ai PG:**` come tutte le altre.

**🎵 → ricerca Google**, stessa forma di 🖼️ e 🗺️: `google.com/search?q=<track>+ffxiv+ost`. Il
blocco §A23 passa da quattro paragrafi a tre righe (−1.457 caratteri): cosa e' il link, quale nome ci
va, come si scrive l'etichetta.

**TRACKER (sei modifiche).** Rosso ai gruppi DUPLICATI invece che al primo tipo incontrato — i sosia sono
quelli da distinguere a colpo d'occhio; clic sul badge cicla il colore di TUTTO il tipo, salvato
nell'incontro. Le righe media non finiscono piu' nelle Azioni del mostro precedente. L'import azzera gli
indici e ridisegna come farebbe un cambio di scheda, e il turno riparte dalla cima dell'iniziativa
invece di seguire il primo PG. Un combattente aggiunto prende subito il suo posto in iniziativa, e il
cursore di turno segue l'ENTITA' per id, non il numero di slot. La copia con Shift non anima piu' il
ritorno dell'originale.

06 v6.40 · cv120 / lv49 / ov69.


## 2026-08-13f — Ripristinato l'URL originale della musica: l'host non era il problema

**Ritrattazione della voce precedente.** Il 🎵 usciva nudo per via delle PARENTESI nell'etichetta
(v6.26), non per l'host. La prova e' nella segnalazione del GM: *«se premo il link»* — il link c'era ed
era cliccabile con host `music.youtube.com`, quindi quel dominio su Gem funziona.

Peggio: mettendo `youtube music` dentro la query per compensare, il modello ha letto quelle parole come
destinazione e **ha ricostruito l'host da esse**, restituendo
`music.youtube.com/search?q=youtube+music+FFXIV+OST+To+the+Sun` — host vecchio e query ridondante che
sporca la ricerca una volta arrivati.

Ripristinato `https://music.youtube.com/search?q=FFXIV+OST+<track>` nei quattro punti. §A23 ora dice
esplicitamente che **la query non nomina mai il servizio**: nominarlo fa costruire l'host da quelle
parole invece che copiarlo. PM 2.46.

06 v6.31 · cv111 / lv40 / ov60.


## 2026-08-13e — Il link musica passa da music.youtube.com a una ricerca Google che punta a YouTube Music

Su Gemini il 🎵 continuava a uscire come testo nudo mentre 🖼️ e 🗺️ erano link corretti. La
differenza misurabile era **una sola**: le due che reggono sono `google.com/search`, quella che cadeva
era `music.youtube.com`. L'host e' l'unica variabile, e l'ipotesi e' che il renderer del Gem linkifichi
solo certi domini.

**Riparato cambiando SOLO la cosa che era diversa**: stesso host e stessa forma delle altre due, con la
destinazione spostata dentro la query — `google.com/search?q=youtube+music+FFXIV+OST+<track>`. Su Claude
il link diretto funzionava; questa forma funziona su entrambi, che e' il criterio host-agnostic del
progetto.

Nota su una parola: il GM aveva proposto `Google Music`, ma quel servizio (Google Play Music) e' chiuso
dal 2020 e come testo di ricerca spinge verso pagine morte. La chiave che porta davvero su YouTube
Music e' **`youtube music`**.

Ripuliti anche tre riferimenti a `music.youtube.com` rimasti dentro le spiegazioni di §A23, che dopo il
cambio dicevano il falso.

06 v6.30 · cv110 / lv39 / ov59.


## 2026-08-13d — Tracker: elementi con impronta vera, selezione e animazione a posto

Rifinitura in piu' passaggi, tutta provata al tavolo dal GM.

**I sei carri, causa vera.** Non bastava il profilo: esiste una TERZA passata, la *decor pass*, che dopo
il giro tattico semina copie lungo i bordi pescando **a caso** da `sparsi`, senza guardare ne' il
numero grammaticale ne' il profilo. Ora lavora su un `decorPool` che esclude gli elementi singolari.

**Sovrapposizioni.** `put()` marcava UNA cella anche per un elemento 2×2, quindi il generatore posava
altro sotto il carro. Ora prenota l'intera impronta, e il nuovo `freeFootprint()` verifica tutte le
celle PRIMA di scegliere il punto — sia nel giro tattico sia nella decor pass.

**Impronta nativa ovunque:** trascinamento singolo, trascinamento di gruppo, copia con Ctrl e aggiunta
dalla legenda ragionano tutti su N×N. Lo scambio di posto per trascinamento avviene solo fra elementi
di taglia UGUALE (con taglie diverse lascerebbe impronte sovrapposte).

**Selezione.** Clic semplice seleziona (e azzera il resto), ri-clic deseleziona, Shift+clic somma. Dopo
un trascinamento la selezione si azzera **solo se il trascinato non era selezionato**: se stavi
muovendo cio' che avevi scelto, resta selezionato.

**Animazione.** Partiva dalla posizione d'origine, quindi dopo lo snap l'icona rifaceva tutto il
tragitto gia' percorso col mouse. Ora parte dalla cella di **rilascio**: l'animazione e' solo la
correzione dello snap. Vale per elemento singolo, gruppo e pedine (queste ultime tenendo conto
dell'offset di presa).

**Ridimensionamento (↑/↓), anche in multi-selezione.** Rimpicciolire e' sempre lecito; ingrandire cerca
un ancoraggio libero che contenga la posizione attuale, e se sono tutti bloccati ritenta inglobando i
confinanti **solo se dello stesso tipo**. In gruppo: ordine dai piu' piccoli quando si rimpicciolisce e
dai piu' grandi quando si ingrandisce, cosi' chi cresce trova lo spazio liberato da chi si e' ristretto;
e i fratelli selezionati non si inglobano a vicenda.

**Accostamento.** Rimpicciolendo, l'ancora fissa in alto a sinistra allontanava di una cella due
elementi che erano attaccati. Ora si sceglie, dentro la vecchia impronta, la posizione piu' vicina al
riferimento — e il riferimento sono **PRIMA i compagni di selezione**, poi (se l'elemento e' solo) cio'
che ha intorno.

**Memoria della posizione.** Un elemento da solo che torna alla taglia di partenza torna anche al punto
di partenza, se quel posto e' ancora libero. La memoria e' legata alla selezione e si azzera cambiandola.


## 2026-08-13c — Tracker: il ridimensionamento occupa celle vere

Il passo precedente cambiava solo il DISEGNO dell'icona: un carro 2×2 si vedeva grande ma il motore
ragionava sulla sola cella d'ancoraggio, e un altro elemento poteva finirgli sotto. Ora l'occupazione
e' reale.

**Tre funzioni nuove.** `featureCells(f)` restituisce le N×N celle coperte; `cellIsFloor(data,x,y)`
dice se una cella e' dentro la mappa e calpestabile (le mappe salvate senza griglia contano come tutto
pavimento, cosi' i vecchi incontri continuano a funzionare); `resizeFeature(data,obj,target)` fa il
lavoro.

**Come sceglie dove crescere.** Rimpicciolire non ha vincoli. Per ingrandire genera tutti gli
ancoraggi che CONTENGONO la posizione attuale, li ordina per quanto poco spostano l'oggetto e prende
il primo interamente libero: e' il «scala dove c'e' posto». Se ogni ancoraggio e' bloccato, **ritenta
una seconda passata in cui puo' INGLOBARE gli elementi confinanti, ma solo se sono dello STESSO tipo**
— quelli inglobati vengono rimossi dalla mappa e dalla selezione. Se non entra nemmeno cosi', non
scala: la freccia non fa nulla e la mappa non viene ridisegnata.

Restano ancorati alla sola cella d'origine il trascinamento e la selezione multipla: li' l'occupazione
estesa non e' stata toccata.


## 2026-08-13b — Il save non registra piu' un incarico solo annunciato; tracker: carro singolo e icone scalabili

**IL BUCO NEL SAVE (il piu' grave: perdeva trama).** Il beat chiudeva su Warin che dice *«ho un vero
incarico per voi»* — annunciato, non dato — e `/salva` ha scritto *«ottenuto l'incarico per fermare i
coblyn»*. Al ricaricamento quella scena non si gioca piu'. Il guardrail esisteva gia' ma solo per la
quest (*[A] = mai una che l'[Info GM] indicava*), non per lo step.

§B24 LAST-PLAYED ECHO ora dice che l'evento e' uno che il testo ha **risolto**, che un incarico
OFFERTO o PROMESSO non e' un evento compiuto, e che **se l'ultima cosa del beat e' un annuncio lo step
e' l'evento risolto precedente**. Con la regola di pareggio che il GM ha chiesto: **a parita' si prende
sempre il piu' arretrato**, perche' i due errori non sono simmetrici — uno step corto costa una
rilettura, uno step lungo cancella una scena per sempre.

**TRACKER — i sei carri.** `Carro` stava nella riga dei cluster con `groups:[3,7]`: da tre a sette carri
per una scena che ne stagiona uno. Ora: profilo proprio a gruppo unico, **`Carovana` aggiunta** al
catalogo, entrambi **Grande (2×2) di default**.

**NUMERO GRAMMATICALE.** Il catalogo porta le due forme (Carro/Carri, Roccia/Rocce, Cassa/Casse,
Albero/Alberi, Carovana/Carovane...), il parser legge quale ha scritto il Gem, e **il singolare piazza
esattamente UN elemento** mentre il plurale usa l'algoritmo di sparpagliamento. In 06 la specifica
`Elementi:` ora chiede di accordare il numero alla prosa.

**ICONE SCALABILI.** Gli elementi hanno un campo `size` e le classi CSS `.map-overlay.size-2/3/4`,
speculari a quelle che i token dei mostri avevano gia'. Con **una sola** icona selezionata, ↑ e ↓ la
scalano fra Media e Mastodontica; se crescendo esce dalla mappa rientra spostandosi.

**DUE LACUNE DI GIOCABILITA', trovate confrontando i beat con la forma dei moduli pubblicati:**
- §A21 RESOLVE-AND-PRINT copriva il bottino dei mostri ma non le ricompense: il test stampava *«vi
  consegna la ricompensa pattuita in Gil»*, senza numero, e il GM non ha nulla da dare. Ora copre
  **ogni pagamento che la finzione consegna**.
- §A18 era 'check ON DEMAND': nessuna regola chiedeva prove dentro una scena giocata, e infatti il giro
  di Ul'dah aveva tre luoghi, tre PNG e **zero tiri**. §A10 ora chiede almeno una prova per ogni scena
  non di combattimento con un'intestazione propria.

06 v6.29.


## 2026-08-13 — 06 v6.25: la riga musica usciva senza link perche' il corpus la chiamava 'header'

**Pro e Flash passano, terza run solida.** Unico difetto rimasto: il 🎵 usciva come testo semplice,
mentre 🖼️ e 🗺️ erano link corretti.

**Correlazione misurata:** `Musica header` compariva 3 volte in 06 (5 occorrenze di *header* accanto a
🎵). `Immagine header` e `Mappa header`: **zero, mai**. L'unica delle tre righe che il corpus chiamava
'header' era l'unica a uscire senza link — e un header, in markdown, e' `###`, non un collegamento.
Stessa forma dei `piedi` accanto agli `yalm` e di `/chiusura` accanto a `closing scene`: la parola usata
per descrivere la cosa vince sulla regola che la descrive.

Tutte e cinque le occorrenze dicono ora `Musica link`, e la definizione si allinea alle altre due:
*«like the 🖼️ and 🗺️ lines, the OST is a MARKDOWN LINK typed out as text»*.


## 2026-08-12v — FLASH 2/2. Pro 0/2 su `/salva`: assembla il turno dai due vicini di lista

**Flash e' a posto: 2/2 sulla sequenza intera** (`/pippo` → `/carica`+save → `/continua` → `/salva`).
Restano le riparazioni di oggi: regola media senza nomi di strumenti, load gate senza pretesa di trigger,
perifrasi legate ai comandi. Lo teniamo comunque sotto osservazione.

**Pro fallisce 0/2, e le due uscite hanno la STESSA firma:**
- `[Info GM] chiude l'apertura (Beat 0); apre Coming to Gridania; prossimo step wiki: ...`
- `[Info GM] prosegue Coming to Gridania; prossimo step wiki: ...`

Non sono «gioca un beat» e «rifa' il load»: **`[Info GM]` e' un pezzo del FOOTER del beat, `prossimo step
wiki:` e' un pezzo della riga `/carica`.** Pro non trova una forma propria per il turno e la **assembla
dai due vicini di lista**. E' [2.26] un'altra volta, sul comando accanto.

**Errore mio, ammesso:** in cv108 avevo tolto *«A delta, never an orientation: no `Prossimo step
wiki:`»* giudicandola duplicato di 06. **Non lo era: `Prossimo step wiki` non compare in 06 nemmeno una
volta.** Era l'unica difesa esistente, e l'ho cancellata. La lezione della potatura vale, ma la verifica
«sta gia' in 06?» va fatta con un grep, non a occhio.

**Riparato in 06 (§B24 SAVE OUTPUT-SHAPE), estendendo la lista di MUST NOT che gia' esisteva** invece di
rimettere la clausola in cv: il turno non contiene beat tag, **ne' una riga `[Info GM]`, ne' una
`Prossimo step wiki:`, ne' altri pezzi di footer del beat o di orientamento di load**. Casa sua, e cv
resta magro.

**Da verificare:** le run di Pro sono state fatte su cv108, che per `/salva` non aveva NESSUNA forma —
l'avevo stripped io. cv109 ha ripristinato la riga `ENTIRE REPLY`. Va riprovato prima di concludere.

06 v6.23 · cv109.


## 2026-08-12u — 06 v6.21: era 06 a contraddire cv sul trigger del load

`/continua` ristampa il caricamento, sul turno dopo `/carica`. Flash 1/2, Pro fallisce. Sopravvissuto a
ogni modifica di cv, **cv96 compreso** — e questo era il dato che lo diceva: il colpevole non era cv.

**§B24 diceva l'opposto di cv.** cv: *«the block alone, with no command, is inert... never a trigger»*.
06: *«the block IS the trigger... the load fires when the block is read in»* e *«FILLED-BLOCK = ALWAYS
A LOAD ... load it immediately»*. Per PM 2.37 nel canale RAG vince il RAG, quindi finche' il blocco
restava in conversazione ogni turno era un nuovo load.

**La difesa esisteva e mancava il bersaglio:** *«NON-DELIMITED IS NOT A SAVE»* copriva l'eco
`Save caricato:` e i frammenti — casi che non capitano — mentre il blocco che il GM incolla ha i
delimitatori. Proteggeva da tutto tranne che dal caso reale.

**Riparato togliendo, −129 caratteri.** Via il trigger e il 'load it immediately'; la clausola riscritta
sul caso vero: *«A SAVE IS LOADED ONCE, ON THE TURN THE GM ASKS FOR IT.** Everything still sitting in the
conversation afterwards — the delimited block itself, the echo, a recap line — is SPENT DATA.»*

Nota: §B24 si apre con *«THIS SECTION IS FORM, NEVER TIMING»*, frase che 06 ripete **sette volte**. Il
guasto stava dentro la sezione che la dichiara. PM 2.45.


## 2026-08-12t — cv108: la riga delle perifrasi aveva gia' reso inutile il template del pre-save

Domanda del GM: *«sei sicuro che il template del pre-save serva in cv? non e' scritto in 06?»* No, non
serviva — e la cosa notevole e' **quando** ha smesso di servire. Le cinque righe della forma e la riga
che lega le perifrasi le ho aggiunte **nello stesso commit**, senza accorgermi che la seconda cancellava
la prima: finche' `'the end-session command'` non era legato a un comando, la forma in 06 era
irraggiungibile e duplicarla sembrava necessario; nel momento in cui e' legata, il duplicato e' morto.

Verificato prima di cancellare: 06 ha `Ancora save` ×4, `[GIOCATO]` ×2, `[DA VERIFICARE]`,
`Ultimo evento giocato` ×3, piu' due regole che cv non aveva nemmeno (`MUST NOT contain a beat tag`,
`do NOT write`). Duplicato puro.

In cv resta solo cio' che e' semantica di comando e non forma: `/salva` e' READ-ONLY e non scrive, e
chiude sulla riga verbatim che nomina `/confermo` (stesso schema di `/voci` → `/accettiamo`). −349
caratteri. Corretta anche la riga del cursore, che diceva ancora `/salva` persists it.

**cv 8.483 → 8.966: +483 (+5,7%)**, contro il +17% di stamattina. Il grosso di oggi e' uscito da cv, non
entrato.


## 2026-08-12s — cv107: potatura. Tolto tutto cio' che era allineamento e non riparazione

cv era cresciuto **da 8.483 a 9.927 caratteri in una sessione, +17%**, e buona parte non riparava
niente: era la passata di allineamento fra i tre assistenti, fatta **in mezzo a un debug**, contro la
regola di cambiare una cosa per volta.

**Tolto (−612 caratteri):**
- la riga di verifica wiki — **06 §A14 la copre gia', output-forcing, per tutti e tre**: era un duplicato,
  non un allineamento. Ed era nel contenitore sbagliato (lv e ov la tengono in `<scope>`, cv non ne ha uno).
- `/prova`, `/negozio`, `/cercano` riportati alla riga compatta di cv96: nessun guasto li' era mai stato osservato.
- `on its own turn`, e le code esplicative della riga delle perifrasi e della forma di `/salva`.

**Rimasto, e perche' ciascuno se lo merita:** la regola media riscritta (unica riparazione MISURATA:
`/continua` pulito su Pro) · la riga che lega le perifrasi (sblocca 67 regole a ~450 caratteri) ·
`/salva`+`/confermo` (sostituiscono `/fine`, crescita quasi nulla) · le misure eorzee (la funzione
richiesta) · `HOW A THING IS MADE` (35 caratteri per l'enunciato dei due strati).

**Bilancio: +832 sul cv96 di partenza (+9,8%)**, non +17%.


## 2026-08-12r — 67 regole della knowledge erano irraggiungibili; `/salva` mostra, `/confermo` scrive

06 non puo' nominare i comandi (1.4), quindi li chiama per ruolo: **13 perifrasi, 67 occorrenze**
(`'the rumours command'` 14, `'the write command'` 13, `'the end-session command'` 9, `'the travel
command'` 8, `'the bridge command'` 8...). **cv non ne dichiarava nessuna.** Regole su forma
dell'output, ancore verbatim e perfino un `MUST NOT contain a beat tag` erano scritte per comandi
senza nome: invisibili.

**Riparato con una riga in `<knowledge>`** che lega ogni perifrasi al suo comando. ~570 caratteri per
sbloccarne 67. Righe equivalenti in lv (check, image) e ov (act, check, wipe).

**Gate del save a due passi, che §B24 descriveva gia':** *«a 'the end-session command' turn: do NOT
write ... the write happens only on the 'the write command' turn»*. Ora **`/salva` stampa il recap di
sola lettura e non scrive**; **`/confermo` scrive**, valido solo nel turno subito dopo — stesso schema
di `/voci` → `/accettiamo`, con riga di chiusura verbatim. `/fine` (ex `/chiusura`) sparisce: non serve
piu' un nome che significhi 'recap'.

`[DA CONFERMARE]` → **`[DA VERIFICARE]`** in cv e 06: e' il termine che entrambe le glosse usavano gia',
ed evita che `/confermo` si sieda accanto al bucket.

Scartato `/stop`, misurato: `stop` compare **21 volte in 06** come `QUEST-STOP`, cioe' la quest che il
ponte **GIOCA PER INTERO**. Sarebbe stato lo stesso bug con una parola nuova.

cv106 · lv38 · ov58 · 06 v6.20. PM 2.44.


## 2026-08-12q — `/chiusura` diventa `/fine`: il comando collideva col proprio significato

`/chiusura` giocava un nuovo beat su Gemini 3.1 Pro. Il divieto era scritto **cinque volte** (roster
chiuso, 'no beat', 'writes nothing', contract 1, contract 4) e perdeva sempre. Per [2.26] una regola
scritta cinque volte non ne vuole una sesta: vuole che si trovi la forma che la batte.

**La forma era la parola stessa.** `/chiusura` e' l'italiano di *closing*, e nel corpus `closing scene`
/ `closing beat` / `closing narrative` compaiono ~15 volte come **cosa dovuta da un beat** — una perfino
in cv, nella riga NOTHING IS LEFT BEHIND: *«name what this beat OWES (... the closing scene)»*. Per un
modello che legge a senso, `/chiusura` non e' un comando: e' l'ordine di scrivere la scena di chiusura.
Il git conferma che il comando si chiamava `/fine sessione` e che la collisione l'ha creata una rinomina.

**Rinominato `/fine`** (scelta del GM). Nessun sesto divieto aggiunto; anzi ne e' stato tolto uno.

**Due guasti strutturali trovati per strada:**
- **05 riga 1218 nominava i comandi** (`'/chiusura', '/salva'`), che 1.4 vieta ai file di knowledge — e
  rimandava a *«06 §B17 ... the full '/CHIUSURA — SEQUENCE OVERVIEW'»*, **una sezione che in 06 non
  esiste**. Chi cercava la procedura di fine sessione seguiva un puntatore morto e ripiegava su cio' che
  vedeva. Rimando riscritto per perifrasi.
- **06 riga 206** diceva *«needs NO 'Chiusura' label»*, nominando il token in contesto di chiusura beat.

**Reso indirizzabile.** La knowledge chiama quel turno *'the end-session command'* sei volte, senza mai
dire quale sia; cv non conteneva la stringa `end-session` nemmeno una volta. Ora la riga lo dichiara, e
le sei regole di 06 (ancora verbatim, due bucket, `MUST NOT contain a beat tag`) diventano raggiungibili
per nome. Il template inline separato da barre e' diventato **cinque righe distese**.

**RISCHIO NOTO su `/fine`:** in cv esistono gia' `=== FINE SAVE ===` (righe di `/carica` e `/salva`) e
`— Fine parte N —` (footer del beat). Se il guasto si ripresenta in forma nuova — blocco save stampato,
o marcatore di fine parte — il primo posto da guardare e' questo, e il ripiego e' `/fine sessione`, che
non urta nulla e coincide con la perifrasi della knowledge.

cv105 · 06 v6.19 · 05 v2.10.


## 2026-08-12p — cv101 / lv36 / ov56: allineate le regole condivise fra i tre assistenti

Cross-check dei tre file di istruzioni. L'`<output_contract>` era gia' identico parola per parola in
tutti e tre; le lacune stavano altrove, ed erano regole presenti in un file e assenti in un altro che
ne aveva lo stesso bisogno.

**Allineato al file che l'aveva scritta meglio:**
- `HOW A THING IS MADE` (l'enunciato dei due strati) — mancava in **cv**, proprio dove il confine e' piu' delicato.
- Regola wiki, versione lv con `Cite only those two` e `say so` — mancava del tutto in **cv**, monca in **ov**.
- Taglia con `colossal is never Media` + **ricalcolo dei PF** (versione cv) — dimezzata in **lv**, assente in **ov**, che pero' scrive statblock.
- `match the LONGEST entry` — esisteva solo in **cv**.
- `on its own turn` (mancava in cv) e `answering one twice is the failure` (mancava in lv): la versione completa era quella di **ov**.
- `/riposo`: `SAFE` → `SICURO` in lv, per parita' con cv e con 1.4.
- `/prova`, `/negozio`, `/cercano`: cv li liquidava in cinque parole, ora hanno l'argomento e i gradini CD degli altri due.

**ORDINE DEI COMANDI: deciso di NON riordinare** (PM 2.42). Il dispatch di cv e' un baseline misurato e
l'adiacenza aumenta la confondibilita'. Unico spostamento: `/sessione 0` dalla coda dei cambi di stato
alla testa del ciclo di vita, prima di `/carica`. Il principio d'ordine e' scritto in PM, non nei file.

**Il frutto vero dell'analisi sull'ordine:** in lv `/pg` e' PREFISSO di `/png`, unica collisione reale
nei tre roster — e lv era il file senza la regola del match piu' lungo. Ora nominata esplicitamente.

**NON allineato, deliberatamente:** `ANSWER ONLY WHAT WAS ASKED` resta solo in lv. cv e ov sono coperti
da 06 §A1, e lv ce l'aveva gia' mentre prosava la 'Regola di conversione': propagare una regola che
abbiamo misurato non mordere e' costo senza beneficio.

cv 8.642 → 9.140 caratteri (+5,8%) · lv 7.027 → 7.367 · ov 7.968 → 8.360.


## 2026-08-12o — cv100: `/sessione 0` torna nel dispatch

Costo reale **+105 caratteri (+1,23%)**, da 8.537 a 8.642. Cosi' poco perche' 05 Cap. 2 contiene gia'
tutta la Sessione 0 (PURPOSE, ground rules 2.1, background 2.2, end checklist, piu' l'avvertimento di
1.7 che l'apertura non si narra mai durante la Sessione 0): a cv mancava solo il QUANDO. E la riga
sempre attiva «ONLY /continua, /riassumi, /viaggio, /riposo produce narrative prose — the roster is
closed» garantisce gia' che non giochi una scena, quindi non serviva spendere caratteri per dirlo.

Aggiunto anche alla lista multi-parola dello STEP 1 (15 caratteri), senza i quali il match sulla voce
piu' lunga non lo vede.


## 2026-08-12n — Parentesi `(10,5m)` a forma fissa, e potatura della prosa nelle regole sulle unita'

Uscita osservata: `7 yalm (pari a 10,5 metri)`. La regola diceva «metri, non piedi» ma non fissava la
FORMA, e il modello ha glossato in prosa. Ora la parentesi ha una forma sola: **`<numero>m` attaccato,
niente parole** — `7 yalm (10,5m)` · `3 malm (4,8km)` · `10 ponze (4,5kg)`.

**Potatura.** Il blocco §A2 sulle misure era cresciuto a 3.674 caratteri di spiegazioni: perche' l'1:1
col piede e' comodo, perche' la parentesi aiuta, dove conviene usarla. La conversione e' matematica e
non ha bisogno di motivazioni. Riscritto come **tabella** (registro → unita' → fattore dalla fonte 5e →
equivalente metrico) piu' cinque righe secche: **1.554 caratteri, -58%**. Stessa potatura su G28, sulle
tre righe del control layer e sulle quattro schema note del manuale.

**Cosa e' sopravvissuto alla potatura, e perche':** i fattori di conversione, la forma della parentesi,
i numeri PHB (Forza × 15 ponze, 24 malm/giorno) e la riga «la fonte 5e e' l'unica origine di un
numero, non i valori dell'MMO». Quest'ultima passa il test della fonte di [2.39]: l'errore verrebbe
dal prior FFXIV del modello anche senza quella frase. Le giustificazioni no: quelle stanno qui e in
PM 2.41.

06 v6.17 · 01_Manual m2.04 · 07 v1.38 · cv99 / lv35 / ov55.


## 2026-08-12m — La parentesi va in METRI: il piede diventa dato sorgente, non un divieto

Prima run dopo il cambio di unita': `Gittata: 30 yalm (150 piedi)`. La regola diceva letteralmente
*«NEVER print 'ft' or 'piedi' next to a number»* e non e' bastata, perche' la riga sotto conteneva la
scala `5 ft = 1 yalm · 10 = 2 · 15 = 3...` e il manuale altre tre righe `Key: 5 ft=1 yalm`. Il piede
era accostato allo yalm decine di volte: vietato da una frase, reso partner naturale da tutte le altre.

**Non ho rafforzato il divieto.** Tre mosse: (1) la parentesi ha ora un contenuto LEGITTIMO — i
**metri**, `30 yalm (45 m)`, cioe' yalm × 1,5 — perche' l'impulso a glossare il numero era la causa e
andava soddisfatto, non represso; (2) il piede cambia stato, da «vietato» a «lato sorgente della
conversione, come un budget XP: si usa per calcolare, non si stampa»; (3) ogni definizione e' ancorata
al metrico (1 yalm = 1,5 m · 1 fulm = 0,3 m · 1 ilm = 2,5 cm · 1 malm = 1,6 km · 1 ponze = 0,45 kg),
con l'1:1 col piede degradato a nota di calcolo.

La parentesi resta **facoltativa**: si usa dove la scala reale aiuta (una gittata lunga, una stanza, un
salto nel vuoto) e si omette sui numeri corti da griglia, dove `portata 1 yalm` non ha bisogno di
glossa. In parentesi vanno solo metri, km e kg — mai piedi, miglia, libbre.

06 v6.16 · 01_Manual m2.03 (quattro schema note + le due note OCR che citavano i piedi) · 07 v1.37
(G28 estesa alla forma con parentesi) · cv98 / lv34 / ov54. PM 2.41 ha il seguito misurato: e' [2.9]
applicato alle unita'.


## 2026-08-12l — UNITA' EORZEE: yalm / fulm / ilm / malm / ponze sostituiscono metri e kg ovunque

Le tre scale ora coincidono: **1 quadretto = 1 yalm = 1,5 m = 5 ft**. La sovrapposizione esisteva gia'
a meta' (il tracker ragiona in caselle da 1,5 m), mancava solo il nome dell'ambientazione.

**Le unita', verificate su CGW (pagina `Measurements`):** ilm=pollice · fulm=piede · yalm=3 fulm=iarda
· malm=1760 yalm=miglio · onze=oncia · ponze=16 onze=libbra · tonze=2000 ponze. Quindi **fulm, ilm,
malm e ponze sono 1:1 con la fonte 5e** e passano senza aritmetica, tabella dei viaggi (24 malm/giorno)
e capacita' di carico (Forza × 15 ponze) comprese. Lo **yalm e' l'unica forzatura**: canone 0,9 m,
qui allungato a 1,5 m per farlo coincidere col quadretto. Il rapporto fulm↔yalm non e' enunciato in
nessun file — fulm serve alle altezze, yalm alla griglia, non si incontrano mai.

**Due correzioni alla proposta iniziale.** (1) malm = 1 miglio ≈ 1,6 km, non 1,5 km, e ritmo 24
malm/giorno, non 36: cosi' la tabella dei viaggi del manuale passa invariata. (2) L'esempio della cura
AoE «raggio 15 yalm» e' stato scartato: importava un numero del videogioco. Vedi PM 2.41.

**Modifiche.** 06 v6.15: §A2 riga 49 riscritta (`MEASUREMENTS IN OUTPUT ARE EORZEAN`), con la scala
ft÷5, l'assegnazione per registro (griglia→yalm, altezze→fulm, viaggi→malm, pesi→ponze), la failure
shape dell'origine e quella di superficie (`m`/`kg` accanto a un numero = regola saltata). 01_Manual
m2.02: **1.356 figure convertite**, quattro schema note riscritte, le 15 righe `- Size:` portate a mano
in fulm. 05 v2.09: le Limit Break diventano raggi 4/8/12 yalm, linea 4/8/12 × 1/2/3 yalm, cerchio
2/4/6 yalm. 07 v1.36: nuova **G28** — unita' mai tradotte, minuscole, invariabili al plurale.
cv97/lv33/ov53. Tracker: `Dimensioni: 12 × 8 yalm` ora passa senza avviso, `m`/`metri` no.

**Deliberatamente NON fatto: nessun undicesimo controllo contabile in §A9.** La regola metrica reggeva
da sempre senza un controllo dedicato; quella eorzea e' dello stesso tipo. Al suo posto, la failure
shape di superficie dentro §A2. (PM 2.40.)


## 2026-08-12i — 08 v3.53: verificate su CGW TUTTE le 37 candidate. La marcatura e' completa.

Chiuso il secondo fronte: le 29 candidate rimaste sono state aperte **una per una** sulla wiki, con la
stessa domanda (duty? cutscene con un PNG di trama? reveal?). Nessun campione, nessuna stima.

**BILANCIO FINALE: 37 candidate verificate, 8 marcabili, 29 no.** Precisione della sagoma da
commissione: **22%** — quasi quattro su cinque delle quest che SEMBRANO commissioni portano invece
trama. La marcatura sul fronte fetch **e' sostanzialmente completa**: non c'e' quasi piu' niente da
prendere, e l'euristica di forma non e' un buon predittore. Se un giorno servisse riaprire il tema, il
dato da ricordare e' questo: si verifica, non si stima.

**MARCATE in questo giro (3):** `Presence of the Enemy` (fetch) · `The Curious Case of Giggity` (fetch)
· `Picking Up the Sledge` (fetch — la wiki nota che fu rimossa in 5.3 «as part of the pruning of the
ARR main story», cioe' contenuto che SE stesso il gioco ha giudicato superfluo).

**QUATTRO SPINE INCOMPLETE trovate fra le scartate — e sono la parte che conta**, perche' il tag duty
e' cio' che protegge una quest dalle marcature future. Aggiunte:
- **`Escape from Castrum Centri`** — DUE solo duty, e dentro c'e' la scoperta che **THANCRED E' POSSEDUTO
  DA LAHABREA** piu' la prima apparizione dell'ULTIMA WEAPON. Nel nostro spine non c'era nulla di tutto
  questo.
- **`The Oracle of Light`** — solo duty con boss: **GENERALE RAN'JIT**.
- **`Road to Redemption`** — una duty contro un servo dravaniano.
- **`The Gifted`** — non una duty ma un pin: e' la scena 2.1 in cui **ELIDIBUS si presenta ai Waking
  Sands**, vista attraverso una VISIONE DELL'ECO.

**Altri reveal grossi incontrati fra le scartate**, a conferma che erano giustamente non marcate:
`Hope Upon a Flower` (**Fandaniel era Hermes**) · `A Strange New World` (**il sacrificio di Thancred**)
· `Lost in the Lifestream` (Y'shtola recuperata) · `Moving On` (F'lhaminn viva) · `The Legacy of Our
Fathers` (il Risonante di Fordola).

**Andamento utile per il futuro:** le commissioni vere si concentrano in **ARR 2.0-2.3**. Da Heavensward
in poi, delle candidate esaminate NESSUNA era una commissione — la MSQ smette proprio di produrne.

## 2026-08-12h — 08 v3.52: caccia ai marcatori MANCANTI, cinque aggiunti su otto verificati

Seconda direzione dell'audit `[COND]`: le quest che DOVREBBERO essere marcate e non lo sono. Imbuto,
dalle 812 voci: **318 non marcate** -> tolte quelle che devono restare tali (duty nello spine, rimando
di manifest, ULTIMA quest di sezione) = **209** -> tolte quelle nominate nella roadmap 08.1 o in un pin
= **37 candidate con sagoma da commissione**. Di queste ne sono state verificate **otto** su CGW.

**MARCATE (5), tutte con la wiki che le chiama «pure errand»:** `Trial by Turtle` (fetch) ·
`When the Worm Turns` (fetch) · `Bringing out the Dead` (fetch) · `First Impressions` (fetch) ·
`A Modest Proposal` (relay).

**NON MARCATE (3) — sono la parte utile del risultato:**
- **`Road to Redemption`** — sembra una commissione («aiuta i tre cavalieri 0/3») ma **contiene una
  duty** e il filo di Francel, con il testimone dell'ultimo volo dell'*Enterprise*.
- **`Believe in Your Sylph`** — Papalymo e Yda in scena, e soprattutto **FRIXIO CONSEGNA IL CRISTALLO
  qui**: e' il Cristallo #3 FULMINE del manifest ARR L4. Annotato nella voce, perche' e' un pin.
- **`Mask of Grief`** — consegna di un fiore, ma con la cutscene doppiata dell'omaggio a Moenbryda e i
  draghi che compaiono: e' la cerniera verso Ishgard.

**IL DATO CHE SERVE PER DECIDERE IL RESTO: 5 su 8.** Circa **un terzo** dei candidati con sagoma da
commissione porta invece contenuto. Marcare le 32 rimanenti a occhio produrrebbe una decina di errori
del tipo appena corretto — quindi restano NON marcate, deliberatamente: per la regola d'oro un tag
mancante costa tempo al tavolo, un tag di troppo cancella una scena. Si verificano a lotti su richiesta.

**Confermato completo il controllo del giro precedente:** censite tutte le notazioni di duty presenti
nel file (`[DUNGEON:`, `[TRIAL:`, `[SOLO DUTY:`, `[RAID:`, ma anche le forme in prosa tipo
`[The Sunken Temple of Qarn - dungeon duty: ...]`) e ricontrollate contro i tag: **zero** violazioni
`[COND]`+duty residue. I due soli riscontri erano note che ESCLUDONO una duty.

## 2026-08-12g — 08 v3.51: UNDICI finali di patch erano marcati condensabili

Audit dei marcatori `[COND]` richiesto dal GM. Su 812 quest ne erano marcate 549. **Le commissioni
ordinarie sono marcate bene** (verificate a campione: `Forest Friend` = uccidi tre mostri e raccogli
tre spazzole; `All upon the Watchtowers` = riferisci a tre PNG). Il guasto e' concentrato in un punto
solo, ed e' sistematico.

**LA CAUSA A MONTE.** La passata di marcatura ha giudicato dallo STEP SPINE. Ma lo spine di una quest
finale di patch e' indistinguibile da un relay — *«parla con Alisaie -> parla con Alisaie -> parla con
Alisaie»* — perche' il contenuto sta nelle CUTSCENE, che lo spine non elenca. **I finali sono stati
marcati proprio perche' sembrano commissioni.** E' la stessa trappola gia' documentata in 08.2 («NEVER
from the title, which is the method proven unsafe»), un livello piu' sotto.

**UNDICI VIOLAZIONI, tutte verificate su CGW una per una e tutte smarcate.** Con `/riassumi` su quel
tratto sarebbero sparite in una frase:
- **`For Those We Can Yet Save` (3.2)** — la conferenza di Falcon's Nest: **ESTINIEN posseduto da
  NIDHOGG trafigge Vidofnir** e dichiara guerra. Il reveal piu' grosso della patch.
- **`Return of the Bull` (4.1)** — contiene una **SOLO DUTY contro LAKSHMI** (piu' il riscatto di
  Fordola e il congedo di Raubahn). Duty istanziata dentro una quest marcata: violazione netta della
  regola d'oro. Lo spine non la nominava nemmeno: **aggiunta**.
- **`Vows of Virtue, Deeds of Cruelty` (5.1)** — due solo duty (fuga dal palazzo NEI PANNI DI ESTINIEN,
  Arch Ultima).
- `An Ending to Mark a New Beginning` (3.4) — il Griffin riceve gli Occhi di Nidhogg da Elidibus.
- `Louisoix's Finest Student` (3.5) — **la morte di Papalymo** e Ilberd smascherato come il Griffin.
- `Rise of a New Sun` (4.2) — una **VISIONE DELL'ECO** (la vera natura di Asahi) + il corpo di Zenos
  vivo, che il manifest pinna come ALTROVE con reveal protetto.
- `Under the Moonlight` (4.3) — la tomba di Zenos aperta e VUOTA.
- `Prelude in Violet` (4.4) — Y'shtola e Urianger colpiti dalla voce; **Solus zos Galvus si palesa e
  Varis gli spara**, che e' l'ALTROVE pinnato.
- `Seiryu's Wall` (4.5) — **GAIUS VAN BAELSAR rivelato VIVO** e l'identificazione di Elidibus.
- `Echoes of a Fallen Star` (5.2) — Elidibus nella pioggia di stelle; l'Eco e' innata, non un dono.
- `When the Dust Settles` (5.5) — Hydaelyn tace da tempo; **Estinien entra stabilmente negli Scions**.

**DOPPIONE MIO, CORRETTO.** `Vows of Virtue, Deeds of Cruelty` era finita nel file DUE volte: la voce
che avevo inserito il 2026-08-12 e una che c'era gia'. Il grep con cui avevo controllato cercava
`^\*\*Vows of Virtue\*\*` e non poteva matchare il titolo completo con la virgola. Le due voci fuse in
una, con i dati CGW (giver a Eulmore, le due solo duty nello spine).

**RIMANDO DI MANIFEST FUORI POSTO** — ed e' il motivo per cui il tag su `For Those We Can Yet Save` era
sopravvissuto: il `Manifest tie` della conferenza era attaccato a `Causes and Costs`, che e' l'INDOMANI
(CGW: «the peace conference is **not** depicted in this quest»). Spostato sulla quest che contiene
davvero la scena; `Causes and Costs` resta marcata e ora dice cosa e'.

**CONVENZIONE AGGIUNTA in 08.0**, perche' la prossima passata non ripeta l'errore: non si marca dallo
step spine, come non si marca dal titolo — si aprono le CUTSCENE. E la regola pratica che avrebbe
trovato dieci di queste undici da sola: **l'ultima quest di una patch o di un installment non si marca
quasi mai.**

## 2026-08-12f — 06 v6.14: tre regole one-shot che esistevano senza una FORMA, piu' il premio ribaltato

Due one-shot collaudate dal GM (Flash 3.6 e Pro 3.1, stesso soggetto: Hildibrand a Portobirra). Sono
giocabili entrambe, ma a nessuna delle due usciva quello che un modulo pubblicato ha in testa. **Il
motivo non era il modello: le regole c'erano gia' e nessuna aveva un template che le stampasse** —
§C2 chiede «max 3-5 PNG con un tratto distintivo», §C10 da' le quote 20/55/25, §C11 impone lo STRONG
OPENING. Tutte e tre invisibili in output. E' la classe «regola binding senza forma».

**Dato un template in §C4**, che ora elenca i blocchi del pitch nell'ordine:
- **AGGANCIO** — chi convoca il gruppo, cosa promette, perche' proprio loro; due righe nel pitch e
  **giocato** nella scena d'apertura dell'Atto 1. Nei due test nessuno spiegava perche' i PG fossero a
  Portobirra: Flash lo dichiarava in sinossi senza metterlo in scena, Pro non lo diceva affatto.
- **DRAMATIS PERSONAE** — subito dopo la sinossi, una riga per PNG: `**{Nome}** — {chi e'}, {tratto} ·
  Atto {N}`. E' il lookup del GM mentre i giocatori aspettano. Una creatura che combatte e basta NON
  ci va: sta nel suo statblock.
- **TEMPO PER OGNI VOCE DELL'INDICE**, ricavato dal totale con le quote di §C10. Un totale da solo non
  dice al GM se sta andando lungo, che e' l'unica cosa per cui serve una stima.

**NON aggiunta la scalatura per 3/5 giocatori: decisione del GM, la fa a mano al tavolo.**

**§C9 RIBALTATO — «il premio che conta e' quello speso PRIMA della fine».** Osservazione del GM:
*«alla fine e' un'avventura che finisce, cosa te ne fai di soldi o equip?»* Corretto, e cambia il
disegno: l'oggetto utile va messo A META' MODULO, nelle mani del gruppo, dove possono decidere se e
quando spenderlo per vincere — cioe' **coincide con il setup di PLANT AND PAY**. Il miglior bottino di
una one-shot e' una cosa che ha cambiato l'ultimo combattimento. Il premio di chiusura e' colore: una
riga, e il pagamento vero e' cosa fa il mondo adesso. I due test lo dimostrano: le Bombe Traccianti di
Nashu (Flash, Atto 1, usate nel boss) valgono piu' della Fiaschetta di Pro, data dopo l'ultimo colpo.

**IL CONTROLLO CONTABILE (7) NON E' STATO TOCCATO** — e ci ero andato vicino. Avevo scritto una deroga
one-shot («il conteggio si sposta indietro, 0 pezzi sul boss finale e' corretto»); il GM ha chiesto se
fosse la cosa giusta e non lo era. **Ripristinato prima del commit.** Due errori: (a) avevo chiamato
contraddizione una ridondanza — §C9 dice DOVE mettere l'oggetto che conta, (7) dice COSA stampa il
boss, e si possono fare entrambe; (b) un ramo per modalita' dentro un controllo contabile distrugge la
proprieta' che li rende efficaci (nessun ragionamento, solo un conteggio), e si romperebbe anche in
campagna. Costo del comportamento «sbagliato»: una riga di bottino che il GM non legge. Lezione in
PM 2.40. §C9 ora dice esplicitamente che il bottino di chiusura si stampa normalmente e che (7) vale
come ovunque: cambia solo DOVE va lo sforzo di design.

Nessuna modifica alle istruzioni `ov`: la forma del modulo e' formato, e il formato vive in 06.

## 2026-08-12e — 08 v3.50: le scene SOCIALI avevano musica solo per caso + una traccia usata nel ruolo sbagliato

Domanda del GM: che ritmo musicale c'e' fra una scena e l'altra, soprattutto nei momenti social e non
dungeon. Le tabelle coprivano citta', zone, duty e scene-madri; **le tre transienti piu' frequenti no**
(viaggio, riposo, negozio, per genere di scena — mai per nome di comando, il knowledge non li nomina).

**ERRORE TROVATO STRADA FACENDO — `Where the Heart Is` e' il tema dei QUARTIERI RESIDENZIALI**
(`Locales I|023`, venduto dai mercanti di alloggi), non un tema di lutto. Era usato come mood di
morte/addio in **13 punti**: le 6 copie della riga SCENE-KIND, la mood list master e 5 scene-madri —
Moenbryda, il Banchetto di Sangue, l'addio di G'raha, il sacrificio di Minfilia, Yda/Lyse. Con quel
mapping il sacrificio di Minfilia prendeva la musica dei quartieri residenziali.
**Sostituito con `Sacred Bonds`**, l'unica traccia che la wiki etichetta `Sadness Theme` (`Quests|053`).
`Where the Heart Is` non e' stato cancellato ma **rimesso al suo posto**: mood HOMELY / domestico, una
scena quieta in un luogo vissuto — che nei momenti social serve davvero.
*(Caveat: `Sacred Bonds` e' di rilascio EW. Le mood si riusano fra archi per dichiarazione dello stesso
file, ma se il GM preferisce una traccia ARR per le morti ARR, va scelta e sostituita qui.)*

**Nuovo blocco `SOCIAL / INTERIOR / TRANSIENT`**, tutto verificato:
- **`Another Round`** ('Tavern Theme') — la sala comune della gilda: Drowning Wench, Quicksand, Carline
  Canopy. E' il fondale del beat social piu' frequente della campagna e non c'era.
- **`Behind Closed Doors`** ('Inn Room Theme') per il riposo al coperto · per il campo all'aperto NON
  esiste una traccia dedicata: si usa l'ambient della zona, variante notturna dove c'e'.
- Viaggio: l'ambient della zona **attraversata**, non della destinazione; l'arrivo prende quella della
  destinazione. Negozio: il tema della citta'.
- `Shelter` ('Sanctuary Theme' HW) · `Thicker than a Knife's Blade` (The Forgotten Knight) ·
  i tre QG di Grand Company `Into the Adder's Den` / `Maelstrom Command` / `The Hall of Flames`
  (briefing e commissioni) · `Safety in Numbers` (villaggi delle tribu') · `Coming Home` (Vanu Vanu) ·
  `Cradle` (Dawn Throne/Onokoro) · `The Mushroomery` (grotta di Matoya).

Categorie escluse dopo verifica: `Ambient` sono effetti sonori (pioggia, falo', grilli), `Others` e'
contenuto laterale (Eureka, PvP, Firmament). Traghetto, mercato e taverna-generica non esistono come
temi separati: la taverna e' `Another Round`, gli altri due ricadono sul tema della citta'.

## 2026-08-12d — 08 v3.49 / 06: il blocco OST di HEAVENSWARD era riempito per pattern, non verificato

Controllo richiesto dal GM sulle OST generiche di cutscene/reveal. La mood list si e' rivelata sana; il
guasto stava accanto, nella tabella duty di HW — **tutte e 10 le righe dicevano
`(mid-boss) Ominous Prognisticks · (final) Ominous Prognisticks`**, cioe' la regola generica copiata su
ogni riga invece dei dati della duty. Tutte e 10 riverificate su CGW una per una:

- **Il mid-boss HW non e' Ominous Prognisticks: e' `To the Fore`** (8 duty su 10; eccezioni: Antitower
  = `A Fine Death`, Sohr Khai 1° boss = `The Seven Jesters`).
- **META' DEI FINAL HA UNA TRACCIA PROPRIA**, che andava persa: Aery/NIDHOGG = `Primogenitor` ·
  Vault/Charibert = `The Heavens' Ward` · Sohr Khai/HRAESVELGR = `Primogenitor` · Xelphatol =
  `Revenge Twofold` · Antitower = `Dancing Calcabrina -> Ominous Prognisticks` · **Aetherochemical
  Research Facility / ASCIAN PRIME = `Thunderer -> The Maker's Ruin`**. Quest'ultimo e' il climax di
  3.0: prendeva il tema generico dei corridoi.
- **Un ambient SBAGLIATO:** Antitower era `Upon the Rocks`, e' `Down the Up Staircase`.
- **Un ambient INCOMPLETO:** The Vault ha TRE tracce d'area (`Hallowed Halls` · `Toll of the Bells` ·
  `Stigma`); ne era cachata una, contro la regola «MULTIPLE THEMES — LIST THEM ALL» di §A23 scritta
  nello stesso file.

**06 — decimo controllo contabile in §A9.** Il controllo (8) conta la musica sugli SCONTRI e si ferma
li': una cutscene pinnata non emetteva alcun 🎵 e niente se ne accorgeva. Aggiunto **(10) EVERY PINNED
SCENE HAS ITS OWN 🎵** — si contano i pin scritti nel beat e le 🎵 attaccate, e i due numeri devono
combaciare. Questo chiude il difetto «musica» che il GM aveva gia' osservato al tavolo, che era una
regola scritta e non contata.

**MOOD LIST COMPLETATA (2a passata, su insistenza del GM: «non puoi cercare con calma?»).** La prima
ricerca aveva fallito per METODO, non per mancanza di fonte. La pagina `Orchestrion_Roll` di CGW e'
troppo grande da leggere in blocco e l'API MediaWiki non e' esposta, ma **le pagine dei singoli rulli
dichiarano il tema in un template** `{{orchestrioninfo|Categoria|NNN|descrizione}}`, e la ricerca del
wiki **indicizza il wikitext**. Interrogando `Special:Search` sul nome del template si enumera l'intera
categoria «Quests» con, per ogni traccia, **cosa suona e quando** — che era esattamente il dato
mancante. Metodo da riusare.

Aggiunte al blocco master `RECURRING MOOD THEMES`, tutte con la descrizione presa dalla wiki:
- **Tema di cutscene per ESPANSIONE**, che era il buco vero: HW **`Stone and Steel`** ('Heavensward MSQ
  Theme') · SB **`Victory or Death`** e `Far East of Eorzea` ('Stormblood Cutscene Theme') · ShB
  **`A Better Tomorrow`** ('Shadowbringers Cutscene Theme') e `Dangerous Words` ('Story Theme 2') · EW
  il set generico `Tranquility · Fracture · Damnation · Kiss of Chaos · Return of the Hero · Meteor`
  (tutti 'Miscellaneous Cutscene Theme') + `Home Beyond the Horizon` per Garlemald.
- **`From Fear to Fortitude`** ('Solo Instanced Battle Theme') — buco che non avevo nemmeno cercato: la
  campagna pinna piu' solo duty (Cape Westwind, Steps of Faith, Fordola a Castellum Velodyna,
  l'evasione di Estinien in 5.1) e nessuna aveva una traccia.
- `Sacred Bonds` ('Sadness Theme'), piu' stretto di Where the Heart Is che e' addio/lutto · `Bliss`
  (scena leggera) · e i TEMI PERSONAGGIO per le scene che appartengono a qualcuno: Canticle (i gemelli)
  · **`Bedlam's Brink` (Solus zos Galvus / Emet-Selch)** · Dreams Aloft (Cid) · The Sands' Secrets
  (Raubahn) · Ripples in the Sea (Merlwyb) · Dewdrops & Moonbeams (Kan-E-Senna).

La riga SCENE-KIND co-locata coi pin (6 copie) prende solo le due voci che valgono ovunque — solo duty
e tema di cutscene d'arco — e rimanda al blocco master per il resto.

## 2026-08-12c — 08 v3.47: la regola OST-scena non puo' usare «L1» come sinonimo di «visione d'apertura»

La regola diceva *«an ECHO vision -> The Echo **at L1 ONLY**»*, in 6 copie identiche. Funzionava
finche' sotto `L1` c'era UNA visione sola. Aggiungendo il pin della visione in cui Hydaelyn si nomina
(2026-08-12) le visioni sotto L1 sono diventate **due**, e la regola ha iniziato a mandare `The Echo`
anche sulla seconda — mentre la tabella scena diceva `Prelude - Rebirth` e vietava esplicitamente di
riusare `The Echo` sui beat Hydaelyn/cristallo. Contraddizione fra due punti del file, causata
dall'aggiunta del pin.

**Corretto in tutte e 6 le copie:** `The Echo for the OPENING vision (ENTRY 0) ONLY`. E la riga della
tabella scena passa da `BOUND TO L1 ONLY` a `BOUND TO ENTRY 0 ONLY`. **Il vincolo e' la SCENA, non
l'etichetta di livello:** un'etichetta di livello e' un contenitore e i contenitori si riempiono.

## 2026-08-12b — 08 v3.46: tolti i FOSSILI DI CORREZIONE (nuova lezione PM 2.39)

Domanda del GM su una riga scritta poche ore prima: *«perche' quando correggi qualcosa metti sempre la
negazione di quello che hai corretto? Non bastava pinnare Primal Judgment e basta? In teoria se una cosa
non e' pinnata non puo' uscire, ma qua e' pinnata come sbagliata, non e' una contraddizione?»* **Si'.**

La riga era `IFRIT — Primal Judgment [CGW-verified: … 'Fallen Angel' is GARUDA's theme, never Ifrit's]`.
Un pin e' un contratto su cosa DEVE comparire: scriverci dentro cosa NON deve comparire lo trasforma in
un elenco di due candidati, e mette il titolo sbagliato nello **stesso chunk recuperabile** di quello
giusto. E' la lezione sul priming che avevamo gia' (PM 2.9, misurata sui comandi ritirati) applicata
al contrario da me, lo stesso giorno.

**Censite 651 costruzioni negative nella knowledge, classificate in quattro famiglie.** Solo UNA non ha
diritto di esistere — quella dove l'errore esiste solo perche' il nostro file l'ha detto una volta.
Tolte tutte e sei le occorrenze:
- `IFRIT` -> ora solo `Primal Judgment [CGW-verified]` (il discriminante positivo c'era gia': la riga di
  Garuda, due righe sotto, dice Fallen Angel)
- `**Crossing Paths** (formerly listed "Crossroads")` -> il titolo falso non si stampa piu'
- Crystal Tower `(no longer a side gate)` -> resta solo l'affermazione positiva
- quattro `[title corrected]` / `[title corrected: singular]` -> metadati di changelog dentro un chunk
  di RAG; non nominavano niente, ma occupavano spazio recuperabile per parlare di noi

**RESTANO, e se lo guadagnano** (il discriminante e' il TEST DELLA FONTE, PM 2.39): le negazioni che
parano un errore proveniente dalla **wiki che diciamo noi al modello di leggere** (*«There is NO
'Magitek Colossus Rubricatus'»* — Gamer Escape lo elenca davvero) o **dal nome stesso / dai pesi**
(`Coeurl O' Nine Tails` e' un Ochu; Frixio e' un silfo; Titan e' TERRA dentro un vulcano). E le
`FAILURE SHAPES` di 06, che nominano una FORMA sbagliata e non un FATTO rivale: non creano un candidato
concorrente.

**La regola sta in `Project_Memory` 2.39 e nel README (punto 5 di sei), NON nel knowledge** — riguarda
come scriviamo noi i file, non cosa fa il modello a runtime. Scriverla dentro il knowledge sarebbe
esattamente l'errore che descrive.

## 2026-08-12 — 08 v3.45 / 05 v2.08: AUDIT COMPLETO DI 08 (mai fatto prima)

Richiesto dal GM: i pin erano stati costruiti a pezzi con una webchat, quindi sospetti. 4.752 righe,
331 KB, incrociate con `05`. **Metodo:** lettura integrale dei 6 manifest + verifiche MECCANICHE sulla
catena `Next:` (800 voci) + verifica su CGW dei punti dubbi. Le verifiche meccaniche hanno trovato
quello che l'occhio non trova.

### GUASTO PRINCIPALE — SETTE quest MSQ consecutive assenti (Stormblood 4.0)
`The Die Is Cast` (Doma Castle) dichiarava `Next: The World Turned Upside Down`, un nome **che non
compare da nessun'altra parte nel file**; la voce successiva era `The Lady of Bliss`. Catena reale
ricostruita su CGW e **inserita per intero**: *The World Turned Upside Down · A Swift and Secret
Departure · While You Were Away · Rhalgr's Beacon · The Fortunes of War · Rising Fortunes, Rising
Spirits · The Lure of the Dream*. Il buco cade **esattamente su una giuntura di installment**, che e'
dove una costruzione a pezzi lascia i vuoti. Dentro c'era anche la **prima sconfitta di FORDOLA**
(solo duty a Castellum Velodyna) — il personaggio che a L14 porta l'Eco artificiale contro Lakshmi.

### OTTAVA quest assente — `Vows of Virtue, Deeds of Cruelty` (ShB 5.1)
MSQ vera (giver Alphinaud a Eulmore, con la solo duty **come Estinien** + Arch Ultima). Sparita perche'
il suo titolo era stato usato come **intestazione della sezione** `## PATCH 5.1` e la voce non e' mai
stata scritta. `Moving Forward` la puntava nel vuoto. Inserita al suo posto nella catena.

### `Next: Sea of Sorrows` -> `Sea of Sorrow`
La voce porta la nota *[title corrected: singular]* — il titolo era stato corretto **ma non il
puntatore che lo cita**. E' la lezione 2.11 in purezza (corretto dove DEFINITO, sopravvissuto dove
RIFERITO), e stavolta l'ha presa il file che la lezione l'ha prodotta. CGW conferma: singolare.

### SETTE rimandi ai manifest che puntano a livelli inesistenti
L'indice citava `Manifest tie (08.1 ShB L20..L24)` e `(08.1 SB L16/L17)`, ma il manifest ShB arriva a
**L19** e quello SB a **L15**. Sette rimandi ciechi. Rimappati sul contenuto: SB L16/L17 -> **L14**
(Castrum Abania e Ala Mhigo stanno nel climax L14); ShB L20/L21 -> **L16**, L22/L23 -> **L17**,
L24 -> **L19**.

### La fine della campagna puntava oltre la fine della campagna
Tre punti dicevano al walker di proseguire su 6.1: la chiusura di 08.5, la chiusura di 08.6
(*"Next: ENDWALKER PATCHES 6.1-6.55"*) e il `Next:` della quest **Endwalker** stessa. Ma 08.1 dice
*"THE CAMPAIGN CLOSES ON THE ENDSINGER. No 6.x patches"* e manda il marker a `[CAMPAGNA CONCLUSA]`.
Erano segnaposto di costruzione rimasti accesi **sul beat piu' importante di tutta la campagna**.
Ora la quest terminale dice `Next: NONE — TERMINAL BEAT` e `Newfound Adventure` resta registrata solo
perche' la giuntura non sembri un buco.

### Musiche
- **NOVE duty ShB senza riga OST**, di cui due MSQ del 5.0 base (**The Twinning**, **Akadaemia
  Anyder**) piu' i cinque delle patch (Grand Cosmos, Heroes' Gauntlet, Anamnesis Anyder, Matoya's
  Relict, Paglth'an). La tabella E' il lookup di riferimento: una duty assente rimanda il modello a
  indovinare, che §A23 vieta. Aggiunta una riga esplicita che applica la regola generica ai boss e
  manda l'ambient a SEARCH-FIRST — **senza coniare titoli**, che il file stesso proibisce.
- **Ifrit:** la riga si contraddiceva (*"CGW-listed Primal Judgment; the iconic Ifrit track is often
  'Fallen Angel'"*) mentre due righe sotto assegnava *Fallen Angel* a GARUDA. CGW verificato: la
  pagina del Bowl of Embers elenca **solo Primal Judgment**. Nota ambigua rimossa.

### Cross-check con 05
- `05 Ch.1.6` non diceva **quando si apprende il NOME Hydaelyn**: la lista partiva dalla cosmologia
  (HW 3.2), lasciando intendere che anche il nome fosse gated. Aggiunta la riga: nome ad ARR molto
  presto, **natura** gated. Senza, i due file divergevano sul nuovo pin.
- `05 Ch.5.4` elencava i 6 Cristalli senza dire **da dove nasce l'incarico**. Aggiunta l'origine.
- Verificati e CONFORMI: ordine dei 6 cristalli (05 Ch.5.4 vs 08.1), stati della Benedizione
  (05 Ch.5.5/5.6 vs manifest HW), Tiamat = penultimo cristallo, la nota HW 3.2 che dichiara
  aggiornato Ch.1.6 A (lo e' davvero).

### Stato di salute (per sapere di cosa fidarsi)
La qualita' di fondo e' **buona**: i manifest ARR/HW/SB/ShB/EW sono dettagliati, i pin pesanti ci sono
tutti (Lahabrea nominato a Toto-Rak, Haurchefant, Ysayle, Minfilia, la cosmologia 3.2, Yda=Lyse, Azem,
G'raha, Elidibus cuore di Zodiark, Venat=Hydaelyn), e su **792 anelli della catena il 94% combacia**;
il resto sono cluster paralleli documentati. I difetti erano quasi tutti **di giuntura**: fine
installment, fine espansione, titolo usato come intestazione. Falsi allarmi verificati e scartati: le
note `SCOPE:` sono per-installment e non stantie; `Coming to <Citta>` e' catalogata sidequest su CGW ma
resta come sta (vedi 2026-08-11e).

### Aperto, non risolto
- **HW 3.4 (Soul Surrender)** e' l'unico blocco di manifest liquidato come *"a quieter bridge patch"*,
  senza `REVEAL` ne' `GATED` — ma li' i Guerrieri delle Tenebre rivelano di venire dalla Prima e si
  chiude la trama di Urianger. Il reveal e' pinnato piu' avanti (ShB L17), quindi non si perde nulla:
  resta una riga magra, non un buco.
- **ShB manifest: 5.4 non ha un blocco** (ci sono 5.1, 5.2, 5.3, 5.5). E' un interludio leggero, ma in
  un manifest anti-drop l'assenza di un numero di patch andrebbe dichiarata.
- **La fine di FANDANIEL non e' pinnata** nel manifest EW: viene introdotto con un `⚠️ reveal protetto`
  in Fase 2 e la sua uscita di scena non e' scritta da nessuna parte. Non verificabile su CGW (la
  pagina non riporta la morte); serve una fonte.

## 2026-08-11f — 08 v3.44 / 05 v2.07: ENTRY 0 riscritta sulle tre trascrizioni canoniche

Il GM ha recuperato le tre cutscene d'apertura (`Loremonger:Introduction (<Citta>)`, GE non e'
fetchabile: testo incollato a mano). Sono lo **stesso copione tre volte**, e questo ha smontato
l'assunto su cui poggiavano le tre voci ENTRY 0.

**ERRORE CORRETTO — «Of the three openings this is the ONLY one carrying a pinned fight».** Falso.
Ogni citta' ha il suo incidente armato: pirati che aprono il fuoco (Limsa), scaramuccia Wood Wailer
contro **Ixal** (Gridania), **Brass Blades** che estorcono l'ambulante finche' non arriva l'incursione
**Amalj'aa** (Ul'dah). Le due frasi `NO pinned fight here` + `NOT to be upgraded into one to 'match'
Limsa` erano il divieto esplicito di quello che ora facciamo: **ribaltate**, non lasciate a marcire
(precedente: la riga in §B2 contro §B1, undici tentativi).

**Lo schema vero non era «niente combattimento»: era che i PG vengono TOLTI dalla scena** — *'Get
below!'* · *'Try to break clear!'* · *'Now go, all of you!'*. Quindi l'homebrew e' **una regola sola,
non tre invenzioni**: *il gruppo non viene messo al riparo, resta dentro e combatte.* I nemici sono
canonici e nominati nella cutscene stessa. Gridania non richiede nemmeno quello: *'We shall hold them
here! Try to break clear!'* e' gia' un invito a passare combattendo.

**VISIONE SPOSTATA DOPO IL COMBATTIMENTO** (decisione del GM). Risolve un problema che avevamo gia':
05 pretende che la visione sia *il legame* che fa di estranei un gruppo, ma in canon arriva **nel
sonno**, e da addormentati non possono vedersi riceverla — il legame era **dichiarato, non mostrato**.
Ora il mondo si ferma a scontro concluso, solo i PG sono svegli dentro, e alla ripresa restano a
guardarsi. Due rifiniture: **(a)** il mal d'etere resta ma si svuota — i PG si svegliano nauseati
SENZA sogno e l'ambulante da' la spiegazione sbagliata, che diventa un presagio invece di sparire;
**(b)** il tempo si ferma a combattimento **finito**, altrimenti i nemici che si ritirano sono un
salvataggio gratuito e lo scontro non conta piu'. Scritto esplicito che **il tempo fermo e' narrazione,
non una meccanica** (niente tiri, niente azioni, non si ripete a richiesta) — senza quella riga al
terzo utilizzo i giocatori se lo aspettano come risorsa. **Il pin non si rompe:** `VISIONE DELL'ECO`
resta dentro ENTRY 0 e continua a cadere prima dell'arrivo in citta'.

**VISIONE RIPULITA.** 05 diceva *«a star-shower falling from a burning SKY»* e **tre righe dopo**
*«NO burning dragon — that imagery belongs to the CALAMITY cinematic»*: le due frasi si mordevano, ed
era stato tolto il drago lasciando il cielo. Le trascrizioni contengono **solo** `Hear... / Feel... /
Think...`, e il breadcrumb di Limsa e' `The Aetherial Sea`. Ora: luce eterica, niente cielo e niente
suolo, e il divieto copre **sky + star-shower + dragon**.

**AGGIUNTO, tutto canonico e tutto assente prima:**
- **L'AMBULANTE**, perno dell'intera apertura e mai censito: **Brennan** (Limsa) · **Bremondt**
  (Gridania) · **Brendt** (Ul'dah). Spiega il malessere come mal d'etere, chiede a OGNI PG *perche' sei
  diventato un avventuriero* (giro di tavolo gratis al primo beat), espone la politica locale, manda
  alla Gilda, si congeda con un regalo.
- **I MOOGLE di Gridania** — *'Normal folks can't see or hear us, kupo!'*: **primo segno esterno
  dell'Eco**, prima della visione, su TUTTO il gruppo. E pianta il filo del bosco inquieto.
- **Le tre benedizioni di congedo**, una per divinita' cittadina: Llymlaen *'Till sea swallows all'* ·
  Nophica *'serenity, purity, and sanctity'* · Nald'thal *'For by fire are we reborn'*. Chiusura
  naturale del beat 0.
- La corruzione dei Brass Blades a Ul'dah, da giocare PRIMA dello scontro: e' il ritratto della citta'
  in una scena, e Brendt lo dice in chiaro (*'Like common bandits, they are, only less honest'*).

**Confermato dalle trascrizioni, invariato:** Ryssfloh / Bertennant / Wymond come accoglienza, gli
approdi (Lower Decks, Blue Badger Gate, Gate of Nald), la sequenza verso `Coming to <Citta>`.
**Divergenza consapevole registrata:** il testo canonico dice *'comes a **lone** adventurer'* — il
gruppo plurale resta scelta nostra, gia' motivata in Ch.1.7, ma ora si sa che il canon dice il
contrario.

## 2026-08-11e — 08 v3.43 / 05 v2.06: ENTRY 0 ha un nome canonico, `Introduction (<Citta>)`

**Scoperta del GM:** esiste una sequenza MSQ prima della prima missione, `Introduction (Limsa Lominsa)`,
e analoghe per le altre due citta'. Check fatto sulle due wiki fissate.

**Verificato su ConsoleGamesWiki** (Gamer Escape continua a dare 403 a ogni fetch — limite noto):
- `Introduction (Limsa Lominsa)` → **404**, e la pagina `Introduction` non esiste.
- `Coming to <Citta>` → giver **Ryssfloh** (Limsa) · **Bertennant** (Gridania) · **Wymond** (Ul'dah),
  tutti e tre `Previous Quest: None listed`. Combaciano ESATTAMENTE con i giver di #1 gia' in 08.2 e
  con gli NPC d'accoglienza gia' in 05 Ch.1.7.
- `Close to Home (Limsa Lominsa)` → MSQ, giver Baderon, `Previous Quest: Coming to Limsa Lominsa`.

**I link del GM stanno nel namespace `Loremonger:` di Gamer Escape — l'archivio dei DIALOGHI delle
cutscene, non quello delle quest** (quelle stanno a titolo nudo). Quindi `Introduction (<Citta>)` e' il
nome interno della CUTSCENE d'apertura, una per citta'.

**Conseguenza: la riga di 08 NON era sbagliata, e non si tocca.** «*NOT a quest, no giver, no wiki
step, absent from every wiki chain listing*» regge — CGW da' 404 sulla quest e la catena parte da
`Coming to`. Era stata anticipata una smentita che non c'e'. Quello che la scoperta aggiunge e' un
**nome** e una **fonte per i dialoghi**, non una correzione: nessun beat da aggiungere, ordine di gioco
invariato, ENTRY 0 era gia' al posto giusto e col contenuto giusto.

**Scritto:** il nome canonico nelle tre voci ENTRY 0 di 08.2, nel paragrafo Scope di 08.2 (dove
rafforza la motivazione invece di sostituirla: *archiviata SOLO come cutscene, nel namespace
`Loremonger:`*) e nel BINDING FRAME di 05 Ch.1.7. Tre citta' insieme, mai una sola: una parte nominata
e due no e' l'asimmetria che poi si dimentica.

**NON scritto, di proposito — `Coming to <Citta>` e' un SIDEQUEST su CGW**, non MSQ (categorie
«Lominsan/Gridanian/Ul'dahn Sidequests»); la prima MSQ vera e' `Close to Home`. I nostri file la
numerano `1.` in testa alla catena. Al tavolo non cambia NULLA — si gioca in quell'ordine comunque — e
scriverlo introdurrebbe un rischio reale: un file che dice «#1 tecnicamente e' un sidequest» invita a
saltarlo. Resta qui come discrepanza nota.

## 2026-08-11d — cv96: `/cambio Classe` rientra nel roster, `/riprendi SQ` prende una riga sua

**Guasto trovato dal GM al tavolo:** `/sessione 0` risponde "non esiste". Ricerca in cronologia: la
riscrittura XML da zero (cv da 31.9 KB a 6.2 KB) ha lasciato cadere **due** righe di roster, non una —
`/sessione 0` e `/cambio Classe` — e nessuna delle due aveva una nota qui. Collaterali del "ridotte
all'osso", non decisioni prese. **Le procedure non erano perse:** stanno intere in `05` (Cap. 2 +
checklist, Cap. 1.7 per il primo save, Cap. 3.4 per il cambio Job). Mancava solo il dispatch.

**RIMESSO — `/cambio Classe`.** E' materia di CAMPAGNA, non di wiki: il cancello e' la posizione MSQ
("solo se la subquest e' raggiungibile da dove sta il gruppo ORA"), quindi ha bisogno del cursore e in
Loremonger non ci puo' stare. Riga scritta senza rimando a `05 Ch.3.4`: la vecchia riga lo aveva, ed e'
esattamente l'enumerazione che avevamo tolto (una lista di cosa consultare e' un ordine di recuperare,
eseguito a ogni turno). Il cancello sta nella riga, il resto si recupera da solo.

**NON rimesso — `/sessione 0`, per ora.** Non e' un comando: e' una conversazione. In `lv` un messaggio
senza `/` e' gia' una domanda a cui rispondere, e "sessione 0" pesca il Cap. 2 in condizioni di
recupero ideali (capitolo intitolato SESSION 0 SETUP, query ricca di vocabolario, forma gia' presente
nella checklist finale). **Metterlo in `lv` come comando costerebbe caro:** la Sessione 0 finisce
scrivendo save-0 (Ch.1.7, "Session 0 ENDS with this save"), e `lv` dichiara READ-ONLY in tre punti
(role, chiusura di `<commands>`, contract §3). Sarebbe una contraddizione interna nel file che gira sul
modello piu' debole — la classe di guasto del fossile in §B2, otto tentativi falliti su `/stop`.

**`/riprendi SQ` non era caduto:** c'era, ma sepolto a meta' riga dopo un `·`, condiviso con
`/riprendi MSQ`. Era illeggibile abbastanza da sembrare assente al GM. Ora ha una riga sua.
Il tetto di 8.000 caratteri di OpenAI Projects non vincola piu' (il GM usa solo Gemini e Claude
Projects), quindi la riga condivisa non aveva piu' ragione di esistere. **cv da 7.959 a 8.483 caratteri.**

**DUE modifiche su un baseline con UNA sola run 5/5** — se il collaudo regredisce, lo split di
`/riprendi` e' il pezzo piu' economico da revertire per primo.

## 2026-08-11c — 01_Manual diventa la SORGENTE: 01-04 e lo script cancellati, cinque file e basta

Decisione del GM dopo il collaudo riuscito col file unito. `01_Manual` era un DUPLICATO di 01-04,
tenuto allineato solo dalla disciplina di lanciare `build_manual.py` — e la disciplina, in questo
progetto, ha gia' fallito tre volte (§B2 contro §B1, i bucket di `/chiusura`, il FOOTER ORDER: tutte
copie divergenti scoperte giorni dopo). **Ora la sorgente e' una sola.**

**Cancellati:** `01_Races` · `02_Classes` · `03_Spells` · `04_Bestiary` · `build_manual.py`.
**Restano cinque file di conoscenza:** `01_Manual` · `05` · `06` · `07` · `08` — un solo setup, valido
sia sui Gemini sia su OpenAI Projects.

**Il buco di numerazione (02, 03, 04) e' voluto** e non fa danni: i rimandi negli altri file usano il
NUMERO, che ora identifica una PARTE dentro `01_Manual`. Precedente noto: §A2 fu cancellata per intero
e il buco non ha mai causato nulla. Il contenuto e' stabile — regole di manuale gia' corrette e
validate — e le aggiunte future vanno dentro la parte che le riguarda.

**RIFERIMENTI RIPULITI PRIMA DI CANCELLARE, non dopo:**
- `05` citava i quattro **per nome file** in 10 punti (`see 01_Races`, `(02_Classes)`): portati alla
  forma `01 Races` / `02 Classes`, senza parentesi annidate dove erano gia' dentro una parentesi.
- `01_Manual` aveva due **autoreferenze** rimaste dai file originali (`section (04_Bestiary)`,
  `see 03_Spells`): ora puntano alla parte.
- `06 v6.13`: la convenzione FILE REFERENCES non descrive piu' la configurazione a due opzioni
  ("o quattro file o un manuale") che non esiste piu'.
- `README` e `Project_Memory`: mappa dei file e sezione "come si allega" riscritte.
- Intestazione di `01_Manual` riscritta: **e' la sorgente, non un derivato**. La riga "GENERATO da
  build_manual.py, non modificare a mano" sarebbe diventata una bugia attiva — avrebbe detto a chi
  legge di non toccare l'unico file dove ora si scrive.


## 2026-08-11b — combat_tracker: l'intestazione dello statblock puo' stare su due righe

**SINTOMO (GM):** tre pacchetti incontro su tre, la MAPPA si importava e il MOSTRO no.

**CAUSA.** `SB_HEADER` pretende nome + trattino + taglia + CA + PF **sulla stessa riga fisica**. Il
modello ha scritto il nome su una riga e `Grande · CA 13 · PF 45 (6d10+12) · Vel 6 m` su quella dopo,
senza trattino: zero header trovati, zero statblock. La mappa funzionava perche' `parseArenaSection`
e' indipendente e legge una lista etichettata, che e' una forma molto piu' robusta.

**CORRETTO IL TRACKER, NON IL CORPUS.** Da una parte c'e' codice deterministico, dall'altra un
generatore probabilistico che tre settimane di test hanno dimostrato difficile da inchiodare a una
stringa esatta — e l'intestazione su riga unica e' la forma piu' fragile dell'intero contratto
(nome + trattino + taglia + CA + PF, tutto insieme). L'output era **semanticamente completo**:
cambiava un a capo. Tolleranza in input, rigore in output.

`joinSplitStatblockHeaders()` ricuce nome e riga-statistiche prima dell'analisi, con due guardie
(`SB_STATS_LINE`, `SB_NOT_A_NAME`) perche' non agganci Arena, Bottino, Tattica o prosa qualunque.
Il contratto nelle istruzioni resta invariato: la riga unica e' ancora la forma richiesta, il tracker
ora accetta anche quella spezzata. **Otto casi di prova, 8/8** (quattro che deve trovare, compresa la
run reale, e quattro che non deve).

**NOTA DI METODO:** la prima applicazione della patch ha corrotto le regex — `` diventato un
backspace, `
` un a capo vero, doppio livello di escape. Il file e' rimasto rotto finche' non l'ho
riletto **byte per byte** invece che a occhio. Su un file di codice, dopo una patch scritta da script,
il controllo non e' opzionale.


## 2026-08-11 — IL CONTRATTO D'OUTPUT SALE NELLE ISTRUZIONI; 06b CANCELLATO

**PRIMO TEST SU GPT (OpenAI Projects, 5 file, 01_Manual).** Dispatch **4/4 al primo colpo** —
`/carica`, `/continua`, `/chiusura`, `/salva`, con save che incrementa 6->7 e il diff. Pin di 08.1
tutti al posto giusto (Lahabrea prima del boss, Eco dopo, Frixio, Cristallo #3), boss loot per ruolo.
**Mancavano tutte le immagini e le mappe, e lo stat block era in formato pipe.**

**LA DIAGNOSI, e non era quella che pensavo.** Un test diagnostico («come si scrive uno stat block?»)
ha mostrato che **06 viene letto benissimo**: GPT ha recitato Taglia<->dado, «niente griglia», «niente
usa-le-statistiche-di-X», il Telegrafo. Ma ha poi stampato il layout **di 04**, con le pipe, e l'ha
chiamato «un esempio reale del formato presente nel materiale». **Aveva ragione.** Misurato in
04_Bestiary: **230 righe con pipe, 112 volte `(… XP)`, 125 `AC `, 143 `HP `, 122 `STR `.**

E' la stessa malattia di queste settimane **un piano piu' sotto**: in 06 avevamo COMPORTAMENTO che
competeva con le istruzioni; in 04 abbiamo un LAYOUT che compete con §B6 — ed e' concreto, completo e
ripetuto oltre cento volte. **Una regola astratta non batte cento esempi.** Spiega retroattivamente
difetti visti su Gemini e attribuiti ad altro (stat block senza CA/PF/Vel, `Sensi` monco).

**DUE INTERVENTI, entrambi host-agnostici.**
- **04 dichiara di essere un archivio** (in inglese, §1.4): le sue righe sono DATI compressi, mai la
  forma dell'output; da li' si prendono NUMERI e PROFILO, mai la disposizione della pagina.
- **`<output_contract>`, IDENTICO nei tre file** (verificato per stringa): la riga d'apertura dello
  stat block, l'`### ` del pacchetto, `**Nemici:** ×N`, `#### Arena` con Tipo/Dimensioni/Elementi, e i
  tre template di link. Con la giustificazione in testa: **queste forme sono un'INTERFACCIA, non uno
  stile** — un programma esterno le legge, quindi devono stare dove sono garantite presenti, non dove
  si spera che il recupero peschi la sezione giusta.
  **cv 7.959 · ov 7.790 · lv 6.849 caratteri**, tutti sotto il limite OpenAI di 8k. cv era finito a
  8.019: stretto il blocco condiviso invece di far divergere un file. In lv il blocco duplicava due
  righe gia' in `<output>`: rimosse.

**COLLAUDO SU GEMINI (cv95 + 01_Manual): 5/5.** L'aumento da 6,3 a 8,0 KB **non ha rotto il dispatch**.
E hanno funzionato le regole dei giorni scorsi: 🖼️/🗺️ presenti, 🎵 diversa a ogni scontro con
**Nemesis** sul boss (controllo #8), boss loot con tre pezzi ed effetti (controllo #7), entrambi i
Coeurl con stat block completo, e **un ENIGMA e una PROVA di tipo diverso** — la regola di ieri, al
primo test. Aritmetica dei PF corretta in tutti e tre i blocchi.

**NOMI DELLE SOTTO-AREE (06 v6.11 -> v6.12): la regola si sabotava da sola.** §A6 vieta di nominare
`Camera dell'Abacinazione` & co. nella prosa player-facing — ed e' violata da sempre. Causa: la stessa
regola AUTORIZZAVA il nome nei sotto-titoli GM, e il modello scriveva
`Enigma: Il Terminale del Confessionale` **tre righe sopra** il read-aloud. E' il pozzo gravitazionale
semantico: la menzione stessa attiva il termine. Ora **anche il sotto-titolo sopra un read-aloud resta
descrittivo**, e il nome canonico vive lontano dalla prosa, in `[Info GM]` e nel pin. Piu' il
controllo contato **#9** (nomi di sotto-area dentro `Da leggere ai PG`: 0).

**06b CANCELLATO (110 KB).** Misurato: **l'87% era testo identico a 06**, e le 18 regole "uniche"
sono tutte coperte in `cv` in forma compressa (il `/carica` copre i cinque LOAD-*, il roster chiuso
copre NO ALIASES, `<cursor>` copre LIVE STEP e NO PENDING TASK...). Non e' lo spazio il problema: **e'
una fabbrica di fossili** — fra due mesi qualcuno legge 06b, vede una regola che «manca» e la rimette
in 06. **E' esattamente cosi' che e' nato il fossile di §B2.** LEZIONE 2.28: la storia va nel CHANGELOG
e in Project_Memory, non in un file di lapidi. Cancellato anche 06b_SMISTAMENTO (lista di lavoro
esaurita) e i file di prova.

**UN PATTERN CHE VALE DA SOLO:** tre difetti di fila — bottino del boss, musica, nomi delle stanze —
erano **regole gia' scritte e disattese**, non regole mancanti. Su questo progetto il rimedio che
funziona non e' aggiungere una regola: e' renderla CONTABILE. §A9 e' passata da sei a nove controlli.
**E serve un criterio di ritiro**, che il progetto non ha: una regola resa contabile che fallisce due
volte non si riscrive una terza — o e' un limite di capacita' (2.14c) o e' nello strato sbagliato, e
in entrambi i casi esce da 06 e resta come limite noto in Project_Memory.


## 2026-08-10 — QUATTRO INTERVENTI: enigma/prova, i tre file allineati all'XML, il manuale unito

### 06 v6.09 — l'interludio si sdoppia, il 'tre' torna un minimo (dal collaudo del GM)
Quattro difetti, tutti di FORMATO, quindi riparati in 06 senza toccare cv.
- **INTERLUDIO != ENIGMA.** 06 li aveva fusi (`interlude/enigma`) e definiva UNA sola forma d'output:
  qualunque cosa stesse fra due scontri usciva enigma a cinque blocchi. Il GM ricordava due oggetti
  distinti e aveva ragione — la distinzione non era stata persa, **non era mai stata scritta**. Ora
  sono due tipi e il dungeon li ALTERNA: **ENIGMA** (c'e' uno stato da cambiare; i PG deducono e
  mettono in atto; cinque blocchi) e **PROVA** (una situazione da attraversare; niente da dedurre;
  QUATTRO blocchi, **senza `Soluzione (GM)`**, con fallimento fino a una scaramuccia di 1-2 round a
  mini-stat inline). Le tracce del concetto c'erano gia' (`INTERLUDE IS NEVER A FIGHT`,
  `BACKGROUND MOB`) ma senza una forma propria, quindi non potevano produrre nulla.
- **IL 'TRE' ERA DIVENTATO UNA PIANTA DELLA STANZA.** §E1 dice `min 3 solutions` = minimo di MODI DI
  AGIRE; il modello costruiva tre vasche, tre condotti, tre anelli in tre beat di fila. Ora e' un
  FLOOR sulle azioni, mai un conteggio di oggetti: un solo meccanismo puo' offrirne tre. Allineati
  anche §E1 principio 4 e §D5, che diceva `3 solutions` secco.
- **`Innesco:` CONDIZIONALE.** Si stampa solo se lo scontro ha un innesco vero; se la rissa parte
  perche' il gruppo e' entrato, la riga si omette — il read-aloud lo dice gia', e parafrasarlo costa
  al GM una riga da saltare.
- **VISIBILITA' ESTESA ALLA PROVA + VERBOSITA' DELL'ENIGMA.** Una Prova puo' nominare solo oggetti che
  il suo read-aloud ha mostrato (osservato: un CD 10 per trovare una leva mai descritta). E cio' che e'
  in piena vista non costa un tiro: il gradino piu' basso degli `Indizi` deve aggiungere qualcosa di
  NUOVO, altrimenti la prova non compra niente.
**§A9 PASSA DA SEI A OTTO CONTROLLI CONTATI**, perche' §A21 e §A23 c'erano gia' e venivano disattese:
(7) il boss finale stampa i suoi equip drop, non la riga da mid-boss (Graffias aveva avuto bottino da
mid-boss); (8) una 🎵 per ogni scontro dalla tabella duty, mai l'ambient riusato sul boss (per Toto-Rak:
ambient *A Thousand Screams*, mid-boss *A Fine Death*, finale **Nemesis**). Tolto anche l'ultimo token
di comando rimasto in 06, il trigger di `/musica` in §A23.

### ov50 / lv30 / cv93 — i tre file di istruzioni allineati all'XML
Stesso scheletro e stesse regole ricavate dai test: `role / knowledge / scope / commands /
beat|act|output / contract`. **cv 6,4 KB · ov 6,2 KB · lv 5,6 KB** (erano 31,9 / 22,7 / 19,8).
Applicato a ov e lv cio' che era stato misurato solo su cv: zero §-codici e zero elenchi di cose da
consultare (e' l'enumerazione a essere un ordine di recuperare, eseguito a ogni turno); ogni riga di
comando dice COSA LEGGE e COSA CAMBIA; «ogni comando piu' in alto e' gia' stato risposto»; contratto
in fondo con la coda del proprio output dichiarata inerte.
**Differenze volute:** ov ha `<act>` e l'INDICE DEGLI ATTI come piano che `/atto` rende una voce per
volta; **lv ha il default ROVESCIATO** — un messaggio senza slash e' una DOMANDA da rispondere, non
chat, ed e' il suo turno piu' frequente — ed e' il file piu' piccolo perche' il suo pavimento e' due
gradini sotto (Haiku 4.5 / Flash-lite). **cv93:** rientrato e corretto un segnaposto in parentesi
angolari, che dentro un file XML e' un tag non chiuso; stesso difetto gia' corretto giorni fa, **da
ricontrollare a ogni riscrittura del blocco comandi**.

### 01_Manual.md + 06 v6.10 — un file per gli host con pochi slot
OpenAI Projects (tier free) accetta max 5 file e istruzioni entro 8k caratteri. Le tre istruzioni ci
stanno gia'; restava il vincolo sui file, 8 -> 5. **Il rischio vero non era la dimensione ma le
INTESTAZIONI DOPPIE:** 13 titoli comparivano in due manuali (`SCHEMA NOTES` in tutti e quattro;
`BLACK MAGE`, `SCHOLAR`, `SUMMONER`, `BARD`, `PALADIN`, `SAGE`... in 02 come Job e in 03 come lista di
incantesimi). Unendo alla cieca il file avrebbe avuto due sezioni omonime, indistinguibili in fase di
recupero — la stessa classe di guasto delle regole duplicate, applicata ai dati. 28 titoli
disambiguati con un suffisso di parte, zero collisioni residue, contenuto invariato (+803 B di sole
intestazioni). **06 v6.10: UNA riga cambiata invece di 26** — i riferimenti a 01-04 sparsi in 06 sono
NUMERI, e dentro il file unito quelle cifre nominano le PARTI, quindi risolvono in entrambe le
configurazioni. Nessuna versione di 06 da mantenere in doppio (§1.1b).

### build_manual.py — il manuale unito e' DERIVATO, non un secondo originale
`01_Manual.md` era una COPIA di 01-04, cioe' l'esatto guasto che questo progetto ha pagato tre volte
(§B2 contro §B1, i bucket di `/chiusura`, il FOOTER ORDER: tutte copie divergenti, tutte scoperte
giorni dopo da un output sbagliato). Ora la sorgente sono 01/02/03/04 e il manuale si rigenera con
`python build_manual.py`. Lo script disambigua i titoli da solo e **asserisce** che non restino
collisioni: se la fusione smettesse di essere sicura si ferma, invece di produrre un file ambiguo.
La deriva diventa impossibile per costruzione, non per disciplina.


## 2026-08-09b — 06 v6.07: LA FORMA RIENTRA, IL COMPORTAMENTO NO. E NON ERA IL VOLUME

Smistate a mano le 145 regole finite in `06b`: **118 sono FORMA, 27 sono COMPORTAMENTO.** Non avevamo
buttato un file di comportamenti con un po' di formato: avevamo buttato un file di FORMATO con dentro
27 regole velenose.

**RICOSTRUITE in 06 con lo STESSO numero e nome** (tutti i §-rimandi restano validi), ognuna aperta da
`THIS SECTION IS FORM, NEVER TIMING`: §B1 (forma del beat: header, BEAT ESTIMATE, tag, cutscene pinnate,
[Info GM] SLIM, footer, pacchetto ORDER/LAYOUT) · §B2 (grana, one-scene rule, continuity handoff) ·
§B12 (dungeon: mid-boss + interludio, niente trash, split-never-shrink) · §B17 (template del save,
[A] TITLE OWNERSHIP, QUEST NOT DUTY, CARRY-FORWARD, LEVEL IS NEVER DERIVED) · §B3 · §B19 · §B22 · §B24 · §B25.
**Resta stub solo §B21** (registro e cursore), che e' comportamento puro.

**06: 177 -> 266 KB. IL DISPATCH HA RETTO.** E' il dato che mancava: **non era il volume, era il
contenuto.** 89 KB di formato in piu' non disturbano; 27 regole di comportamento si'.

**QUATTRO RESIDUI PREESISTENTI trovati mentre ricostruivo**, mai introdotti da noi: i trigger di `/voci`
in §B20, il trigger del viaggio in §B26, e un token di comando nel dossier di §B22. 06 e' ora a **zero**
token di comando e **zero** segnali di comportamento.

**COLLAUDO (cv90 + tutti e 8):** tag con stima · scontro-enigma-scontro · stat block completi ·
`[Info GM]` di una riga · footer nell'ordine giusto col marcatore nudo in fondo · **i pin di 08.1
(Lahabrea, Graffias, Frixio, Cristallo) dovuti nel `Prossimo beat:`** · `/salva` fa Sessione 6->7 e
copia l'ultimo step con la riga di diff.

**INTERMITTENZA, dato nuovo e utile:** il primo `/carica` ha sbagliato, e **il pulsante Ripeti lo ha
risolto**. Il guasto e' a livello di CAMPIONAMENTO, non deterministico: al tavolo costa un click, non
una regola. Smettere di inseguirlo con il prompt.

**RESIDUI MINORI:** due parole sporche in output ('violently', 'specidie') · `Sensi` con la sola
Percezione passiva · un messaggio di troppo dopo `/salva`.


## 2026-08-09 — cv90 / 06 v6.01: IL DISPATCH FUNZIONA, RIPETUTO. 06 non e' conoscenza, e' un secondo prompt

**PRIMO RISULTATO RIPETIBILE:** cv90 + tutti e 8 i file, due run indipendenti, 4/4 su entrambe —
compreso `/chiusura` dopo un beat di dungeon, il guasto da cui e' partita l'indagine.

**COSA ERA, in tre frasi.** 06 conteneva 265 menzioni di comandi e 5 sezioni di COMPORTAMENTO
(quando agire, cosa interrompe, cosa avanza il cursore). Recuperate a pezzi dal RAG, competevano col
control layer e vincevano: piu' lunghe, piu' dettagliate, piu' imperative della riga di dispatch.
Undici fix precedenti non avevano spostato niente perche' riscrivevano lo strato che perde.

**ISOLAMENTO — 11 test a variabile singola, Gem di prova con 15 righe di dispatch e risposte letterali:**

| istruzioni | knowledge | esito |
|---|---|---|
| 0,8 KB | niente | PASS |
| 0,8 KB | tutti e 8 | FAIL |
| 0,8 KB | tutto tranne 06 | **PASS** (1,4 MB non disturbano) |
| 0,8 KB | solo 06 | FAIL |
| 0,8 KB | 06 senza token di comando | parziale |
| 0,8 KB | 06 meno B1/B2/B12/B17/B21 | PASS |
| 26 KB (cv81) | niente | PASS |
| 26 KB | tutti e 8 | FAIL |
| 6,0 KB senza §-codici | tutti e 8 | PASS |
| 6,4 KB **con** §-codici | tutti e 8 | FAIL |
| **6,2 KB + /carica** | **tutti e 8** | **PASS x2** |

**LE QUATTRO REGOLE RICAVATE (valgono su qualunque modello):**
1. **Le istruzioni non enumerano mai cosa consultare.** Ne' `§B6` ne' «la sezione dello stat block»:
   e' la lista in se' a essere un ordine di recuperare, e il modello lo esegue a ogni turno, anche su
   `/pippo`. Il formato si recupera da solo mentre scrivi, perche' li' la query e' ricca.
2. **Il knowledge non contiene comportamento.** Solo «com'e' fatta una cosa», mai «quando farla».
3. **Il knowledge non nomina i comandi.** Il token e' un amo che pesca i chunk sbagliati.
4. **Ogni turno ha un token da matchare.** Il save incollato nudo era l'unico turno senza comando del
   sistema, ed era quello che falliva piu' spesso: ora e' `/carica` + blocco. Il blocco da solo e' inerte.

**INTERVENTI.** 06: 284 -> 177 KB, zero token di comando, 10 sezioni di comportamento spostate in
`06b_Workflow.md` (114 KB, NON allegare). 05 §19.5: rimossi 5 bullet che definivano i trigger di
LOAD/RECAP/SAVE/RE-HOOK mentre 23 righe sopra lo stesso capitolo dichiara di non essere la fonte dei
trigger. cv: 26,7 -> 6,2 KB, `/fine sessione` -> `/stop` -> **`/chiusura`** (il token `stop` compariva
10 volte come parola comune e 4 come comando, nel suo stesso file), `Restano:` -> `Prossimo beat:`
spostato in cima al footer, `— Fine parte N —` senza «(in corso)» e in ultima posizione.

**FOSSILE TROVATO, ed e' la causa di otto tentativi falliti:** 06 §B2 imponeva «the end-of-step marker
names the next sub-beat and **stays 'continua'**» — sopravvissuto al divieto di §B1, e in contraddizione
con §B12 che documenta *quel marcatore* come causa del continue-momentum. Una regola annullata da un
fossile in un'altra sezione.

**ALTRI DIFETTI REALI CHIUSI:** §A1 misure metriche (non erano in nessun file di conoscenza) · §A4
contraddizione media tool + densita' per beat · §B1 FOOTER ORDER senza la riga connettiva · §B17 i
bucket di `/chiusura` erano «three» con due definiti, e cv puntava a `[A][B][C]`, che e' la struttura
di `/recap` · un rimando morto `§A-COMMAND CHANNEL`.

**DEBITO APERTO, dichiarato:** spostando le 5 sezioni ho portato via anche il FORMATO che ci viveva
dentro (BEAT HEADER, TAG CHOICE, ENCOUNTER PACKAGE ORDER/LAYOUT, PARTY-REFERENCE LINE). Si vede nei
collaudi: titolo di quest tradotto, stat block senza CA/PF/Vel, Taglia Media su un corpo «colossale»,
`9 (2d8+2)` che fa 11. **145 regole in `06b` da rileggere una per una e smistare: forma o momento?**
La forma torna in 06, il momento resta fuori. Da fare con la ripetizione tripla, non alla cieca.

**METODO, la lezione piu' cara:** per dieci giorni ho letto singole run come misure. Con un guasto
intermittente non lo sono: cv87 ha fatto 4/4 e alla ripetizione e' caduto. Da qui in avanti, ogni
candidato si prova almeno due volte in chat nuove prima di dire che funziona.

ov/lv non toccati per decisione del GM: si riscrivono quando cv e' stabile.


## 2026-08-05 (5) — TRE VOCI RINOMINATE NEL TRACKER, TRE RIGHE MORTE NEL FORMATO (06 v5.27)

Altro giro di modifiche al tracker dal GM: *Albero Grosso* → **Albero**, *Mobilio/Tavoli* → **Mobili/Tavoli**,
*Acqua Profonda* → **Acqua**. Rinomine cosmetiche nel tool, rotture totali nel formato: i nomi si risolvono
CARATTERE PER CARATTERE, quindi `- Acqua Profonda` non trovava più niente e l'elemento veniva scartato con un
avviso. Il pacchetto restava formalmente corretto secondo 06 e la pozza non arrivava sulla mappa — esattamente
il tipo di guasto silenzioso che il catalogo chiuso serve a rendere impossibile.

**QUATTRO OCCORRENZE, non una:** l'elenco chiuso (§B8 `Elementi:`), la mappatura nome-comune→voce (*una pozza,
un guado* → *Acqua*, con l'aggiunta di *l'acqua alle ginocchia* perché la vecchia etichetta portava dentro il
«profonda» che ora va detto in prosa), la lista delle MASSE che si compattano al centro, e la riga del patto
prosa/mappa (§B8 «*Acqua* si dice 'l'acqua', 'una pozza', 'la fossa allagata'»).

**UN EFFETTO COLLATERALE DELLE RINOMINE, corretto nella stessa passata.** «Non scrivere mai un nome del
catalogo nel 'Da leggere ai PG'» era una regola sana finché le voci si chiamavano *Acqua Profonda* e *Albero
Grosso*: erano etichette, e leggerle ad alta voce suonava come leggere l'inventario. Ora che quattro voci SONO
la parola comune (*Acqua*, *Albero*, *Rocce*, *Macerie*), la regola letta alla lettera vietava di dire «acqua»
in una stanza allagata. Riscritta su cosa vietava davvero: le BARRE e i qualificatori — *Mobili/Tavoli*,
*Portale/Teletrasporto*, *Acido/Tossina* — non i nomi italiani nudi.

## 2026-08-05 (4) — IL TRACKER HA TRENTUNO VOCI, NOI NE DICHIARAVAMO VENTOTTO (06 v5.26 / cv67 / ov44 / lv38)

Revamp del tracker fatto dal GM, non da qui: il catalogo è cambiato sotto i piedi al formato. Nessuna regola
riscritta, solo il catalogo riallineato — la mappa nasce da nomi che devono combaciare CARATTERE PER CARATTERE,
e un nome fuori elenco viene scartato con un avviso, cioè la stanza che volevi non c'è.

**QUATTRO VOCI NUOVE, dichiarabili.** *Oscurità Magica* 🌌 (`type-obscuring`, e il tracker ora le dà una
famiglia sua, «Visibilità», staccata dalle coperture: acceca ANCHE la scurovisione, dove *Nebbia/Fumo* no —
due voci perché sono due ruling diversi); *Portale/Teletrasporto* 🌀, *Cerchio Runico* 🔯, *Cristallo
Instabile* 🔮 (`type-interactive`). Le tre interattive coprono il buco vero di un'arena FFXIV: il varco che
sputa nemici, il sigillo a terra, lo shard d'aether che ronza — prima esisteva solo *Meccanismo*, cioè la leva.
Ognuna ha la sua riga di mappatura dal nome comune in prosa (§B8), come tutte le altre.

**VORAGINE/VUOTO PASSA A MANUAL-ONLY, ed è il cambio che rompeva qualcosa.** Nel tracker è diventata una voce
da tavolozza, da posare a mano. Ha senso: un baratro funziona SOLO dove la meccanica lo vuole — il bordo su cui
il boss ti spinge, la crepa che spacca la piattaforma — e un vuoto sparso a caso è o decorazione o un TPK. Ma
§B10 IMPONEVA di dichiararla («la voce esiste esattamente per questo punto della checklist»), quindi il
pacchetto obbediva a 06 e il tracker la scartava con un avviso: il pericolo ricercato sul wiki non arrivava
sulla mappa in nessuno dei due modi. Ora §B10 dice il contrario per il solo vuoto — vive nella prosa e in
**Tattica:** (dove avviene la spinta e quanto costa), e le caselle le posa il GM. Le altre voci fetchate
(*Fuoco/Lava*, *Acido/Tossina*, *Portale/Teletrasporto*) restano dichiarate come prima.

**TRE CORREZIONI DI COERENZA che senza il riallineamento restavano bugie silenziose.** I MANUAL-ONLY sono
TRE, non due (e la regola ora dice cosa costa sbagliare: la riga viene SCARTATA, non piazzata a caso). La
lista delle MASSE che si compattano al centro non contiene più la voragine. Il conteggio in chiusura di lista
dice trentuno, perché quel numero è l'unico modo per accorgersi di aver aggiunto una voce inventata.

**NON TOCCATO:** parsing, `Tipo:`/`Dimensioni:`/`Forma:`, le nove etichette dei preset, il divieto di zone,
il test dell'indomani, il test della permanenza. Il revamp non li ha cambiati e non li abbiamo riaperti.

## 2026-08-05 (3) — VIA IL PIN DELLE POSIZIONI: MASSE AL CENTRO, IL RESTO SPARSO (06 v5.25 / cv66 / ov43 / lv37)

Il GM rigenera la stessa arena e la trova ancora sbagliata: l'acqua spezzata in TRE pozze staccate, le radici
in quattro grumi separati. «Così è tutto a caso. Togliamo il pin delle posizioni, più semplice, più elegante,
anche se meno preciso: masse compattate al centro, il resto sparpagliato in maniera radiale, con spazi fra uno
e l'altro. Guarda come fanno gli algoritmi migliori, stile roguelike.»

**LE ZONE SPARISCONO DAL FORMATO.** `Elementi:` ora è un elenco di NOMI NUDI: `- Rocce`, senza posizione. Chi
scrive ancora «Rocce — nord» non riceve errori: la zona si legge e si scarta in silenzio, così i pacchetti
già scritti continuano a importare. Le zone erano una precisione apparente: «nord» è un terzo di una stanza
di cui l'assistente non vede la forma, mentre il tracker sa dove sono finiti muri, porte e altri elementi.

**IL NUOVO PIAZZAMENTO, in due fasi.**
1. **MASSE AL CENTRO, COMPATTE.** Acqua, fango, sabbia, acido, lava, ghiaccio, neve, voragine: prendono le
   caselle libere più vicine al baricentro del pavimento (non al centro geometrico: in una caverna cadrebbe
   dentro un muro), quindi crescono come un disco. Tetto di 12 caselle perché una pozza dev'essere leggibile,
   non mangiarsi la stanza. Più masse insieme si dispongono a corona invece di impastarsi.
2. **IL RESTO SPARSO, con POISSON-DISK (Bridson 2007) + FARTHEST-POINT SAMPLING.** È l'algoritmo che i
   roguelike usano per spargere oggetti senza reticolo e senza grumi. Ogni casella non può toccare — nemmeno
   in diagonale — un gruppo diverso dal proprio: i vuoti fra un elemento e l'altro sono parte del risultato.

**TRE DIFETTI TROVATI MISURANDO, non previsti.**
- **Poisson interrotto presto copre metà stanza.** Fermarsi al numero di semi voluto tiene solo quelli nati
  vicino al primo punto. Bridson copre tutto solo se lo si lascia saturare, e si sceglie DOPO.
- **L'ordinamento per distanza dal centro separava gli elementi in metà opposte.** Su una galleria le due
  caselle simmetriche (y=7 e y=10) distano uguale, finiscono consecutive, e la rotazione ne manda
  sistematicamente una a nord e una a sud: misurato, radici y=10..16 e macerie y=1..5. Sostituito con
  farthest-point PER ELEMENTO — a turno ognuno prende il seme più lontano da quelli che ha già.
- **Un elemento dichiarato poteva non comparire.** Svuotando prima tutti i semi del primo elemento, il tetto
  di ingombro si esauriva a metà strada. Ripristinata la regola «varietà prima di quantità» (si gira per rango
  di seme) e aggiunto un recupero finale: un elemento scritto nel pacchetto compare sempre, punto.

**Misurato sul pacchetto reale del GM**, 40 mappe: acqua sempre UNA pozza sola a 1.3 caselle dal centro;
radici in 4 chiazze medie che coprono l'80% dell'altezza (10° percentile oltre il 40%, contro il 17% del
difetto segnalato); zero adiacenze fra elementi diversi. Otto esecuzioni consecutive delle cinque suite,
85/85 ogni volta.

**Suite ritirate**: t4, t5, t8, t9 verificavano il contratto delle zone, che non esiste più. Sostituite da
t10, che verifica il nuovo. harness e t6 mantenute, con le asserzioni sulle zone riscritte.

## 2026-08-05 (2) — 'OVUNQUE' NON GARANTIVA DI TOCCARE TUTTA LA MAPPA (06 v5.24 / cv65 / ov42 / lv36)

Confronto diretto fra due mappe dallo stesso pacchetto: in una le Radici ("ovunque", Galleria 12×18) sono tutte fra y=13 e y=15, meta' nord della stanza completamente vuota. L'altra le aveva sparse su tutta l'altezza. Il GM: «si puo' pensare diversamente il sistema — le zone cardinali impediscono al tracker di fare un buon lavoro; la pozza resti compatta, il resto si sparga in modo radiale e omogeneo».

**LA DIAGNOSI, non l'architettura.** Le zone non erano il problema — Macerie/nord+est e Acqua/ovest nello stesso pacchetto erano esattamente cio' che il GM voleva (roba pinnata dove la prosa la mette). Il difetto era nel `minSep`: impedisce a due gruppi di toccarsi, ma non impedisce che finiscano per puro caso tutti nella stessa meta' della stanza — la separazione minima non distribuisce, si limita a non far toccare.

**LA CURA — una griglia, non una ricerca cieca.** Per un elemento diffuso la zona (l'intero pavimento per 'ovunque', o la fascia dichiarata) si divide ora in tante celle quanti sono i gruppi previsti, il piu' vicino possibile a un quadrato, ordine mescolato: un gruppo a cella, non tutti a cercare posto nello stesso rettangolo. E **'ovunque' sull'intero pavimento impone ora ALMENO 4 gruppi**, uno per quadrante — con meno gruppi la stanza non puo' toccare tutti e quattro i quadranti per pura conta, indipendentemente da quanto bene si distribuisce la griglia sotto. Misurato sul pacchetto vero del GM, 30 prove: le Radici toccano SEMPRE tutti e quattro i quadranti (minimo 4/4, media 4.0). L'acqua (pozza, zona 'ovest') resta raccolta, mai piu' di 2 quadranti — nessuna regressione sulla distinzione pozza/diffuso della sessione precedente. La stessa griglia vale anche dentro una zona nominata piu' piccola, non solo su 'ovunque'.

## 2026-08-05 — DUE SPANDONO A CASO, UNA STANZA CIRCOLARE DIVENTA UNA CAVERNA (06 v5.23 / cv64 / ov41 / lv35)

Il GM confronta due mappe dallo STESSO pacchetto (Acqua Profonda/centro, Muffa/ovest, Macerie/est, Radici/nord su una Caverna Irregolare 14×12) e ottiene due risultati opposti: in uno le radici sono un piccolo blocco in un angolo, nell'altro sono spanse. In piu’: il read-aloud dice esplicitamente «un vasto atrio **circolare**», ma il pacchetto dichiara `Tipo: Caverna Irregolare`.

**1. IL TERRENO IN UNA ZONA NOMINATA NON SI SPANDEVA MAI, SOLO 'OVUNQUE' LO FACEVA.** Il moltiplicatore che fa crescere piu' gruppi piu' piccoli (introdotto per 'ovunque' come MEZZO) scattava SOLO quando la zona era l'intero pavimento. Una zona nominata come 'nord' restava un singolo blob la cui unica o doppia chiazza finiva dove capitava — a volte spanta per fortuna, a volte tutta in un angolo. **LA STESSA dichiarazione non deve dare esiti opposti da un'importazione all'altra.**

**LA CURA — POZZA CONTRO DIFFUSO, non 'ovunque contro il resto'.** La vera distinzione non era la zona, era la NATURA dell'elemento. **Le pozze** (Acqua Profonda, Fuoco/Lava, Acido/Tossina, Voragine/Vuoto) si raccolgono per gravita' o gravitano attorno a un varco preciso: restano compatte in qualunque zona nominata, per lo stesso motivo per cui "una pozza larga mezza sala" non e' piu' una pozza — **tranne quando la zona e' l'intero pavimento**, il caso in cui 'ovunque' e' il MEZZO (l'acqua alle ginocchia, non due pozzanghere). **Tutto il resto del terreno diffuso** (Fango, Muffa, Radici, Erba Alta, Ragnatele, Rovi/Spine, Ghiaccio, Neve, Sabbia, Nebbia/Fumo) si spande di default in QUALUNQUE zona, nominata o no — radici, muffa e ragnatele coprono un'area per natura, mai un punto solo. Misurato sul pacchetto vero del GM, ripetuto 12 volte: copertura di 'nord' mai sotto un decimo (il tetto di leggibilita' §B8/CHANGELOG-7 condiviso fra quattro elementi su un'arena piccola), in media oltre il 60%.

**Un bug vero scoperto scrivendo il fix**: la prima versione applicava lo spandimento a QUALSIASI modo non 'single', inclusi i grappoli d'arredo (Casse, Macerie, Rocce...) — alzando anche il loro `minSep` da 0 a 1 e facendo sconfinare piu' spesso le zone gia' strette e affollate (i test di saturazione). Ristretto al solo modo `blob` (il terreno): l'arredo resta esattamente come prima.

**2. IL TIPO NON AVEVA UNA MAPPATURA DIRETTA DALLA PROSA.** §B8 elencava le nove etichette ma non diceva MAI esplicitamente «se il read-aloud dice 'circolare', il Tipo e' Struttura Circolare» — Struttura Circolare compariva solo come esempio di un'arena da trial (Amaurot), mai come corrispondenza diretta. Il crollo del soffitto e le radici hanno probabilmente attirato la scelta verso 'caverna' per assonanza tematica, scavalcando l'unica parola che dichiara davvero la forma. Aggiunta la mappatura diretta parola→Tipo (stessa disciplina gia' usata per gli Elementi), con la regola esplicita: **crollo, macerie e radici sono ARREDO (Elementi: Macerie, Radici), mai una parola di forma** — un atrio circolare il cui soffitto e' crollato resta una Struttura Circolare, piena di macerie. Self-check (4) ora conta anche questo.

**Suite di test**: due (harness, t8) erano gia' fragili PRIMA di questa sessione per lo stesso motivo strutturale (contenimento a tolleranza zero su una zona che puo' allargarsi di un passo quando satura); sistemate con la stessa tolleranza "non lontano" (2 caselle) gia' in uso altrove. Verificate stabili su run ripetuti.

## 2026-08-04 (11) — CASELLE DALL'INIZIO, MAI PIU' METRI DA CONVERTIRE (06 v5.22 / cv63 / ov40 / lv34)

Il GM segnala l'avviso «Dimensioni e' in CASELLE, non in metri» e chiede la cosa giusta: al tavolo, per
disegnare, gli servono caselle e basta, mai un numero da ricalcolare.

L'avviso funzionava gia' — il tracker prendeva i numeri, li interpretava come caselle e correggeva la
conversione se trovava un'unita' scritta dopo. Il difetto stava nella REGOLA che l'assistente legge: §B8 diceva
letteralmente «si immagina la stanza in metri, poi si divide per 1,5» — un invito diretto a pensare in metri
e convertire, cioè la causa dell'errore che l'avviso poi doveva scoprire.

Riscritta perche' non ci sia conversione da fare: si ancora la stima **direttamente** in caselle, come farebbe
un GM che dispone le miniature — un combattente a piedi e' 1 casella; un duello in un corridoio stretto e'
8 × 18; un'arena normale 14-18 per lato; la piattaforma di un primal o un'arena da raid 20 × 20 o più. I metri
restano la regola per tutto il resto dell'output (§A1: portate, raggi, Vel) — solo le Dimensioni dell'arena si
pensano in caselle dal primo momento.

## 2026-08-04 (10) — SABBIA E NEVE (06 v5.21 / cv62 / ov39 / lv33)

Su richiesta del GM, due voci in più al catalogo dei terreni: **Sabbia** 🟡 e **Neve** ❄️, entrambe terreno
difficile. Catalogo dichiarabile a 28.

**NEVE E GHIACCIO SONO DUE VOCI, NON UNA.** La neve alta RALLENTA (costo movimento doppio), il ghiaccio fa
SCIVOLARE (rischio caduta proni): sono due decisioni diverse al tavolo, e tenerle in una voce sola avrebbe
lasciato al GM il compito di indovinare quale applicare guardando un'icona. Così la mappa lo dice.

**Sabbia** entra nella famiglia dei dischi colorati — acido 🟢, acqua 🔵, fango 🟤, sabbia 🟡 — che sulla
mappa si leggono a colpo d'occhio come varianti della stessa domanda: su cosa stai camminando.

## 2026-08-04 (9) — RADICI SÌ, VITICCI NO (06 v5.20 / cv61 / ov38 / lv32)

Il GM importa un pacchetto e il tracker rifiuta «Radici/Viticci». Passato il read-aloud al TEST DELL'INDOMANI,
il nome conteneva due cose opposte: le **radici** che invadono il pavimento della galleria RESTANO a scontro
finito e sono la stanza; i **nove viticci spinosi** che frustano l'aria se ne vanno con la pianta e sono il
mostro. Un buco vero e un errore, dentro la stessa riga.

**+ Radici** 🪢 (terreno difficile), 26ª voce. Si chiama *Radici* e basta: un nome «Radici/Viticci»
cucirebbe dentro al catalogo proprio la confusione che il test serve a togliere. §B8 lo dice nella mappatura,
accanto all'esempio.

**AVVISO CHE SUGGERISCE.** Un nome inventato di solito CONTIENE quello giusto: l'avviso ora lo indica —
«Elemento "Radici/Viticci" non è nel catalogo: ignorato. Forse intendevi "Radici"?» — invece di lasciare il
GM a confrontare la sua riga con un elenco di ventisei voci. Se nessuna voce condivide una parola, nessun
suggerimento: meglio niente che un'indicazione inventata.

**DIFETTO SILENZIOSO TROVATO NELLO STESSO PACCHETTO.** Diceva «Dimensioni: 12 × 18 **m**», ma le Dimensioni
sono in CASELLE: 12 × 18 m sono 8 × 12 caselle, quindi la galleria usciva metà più grande del dovuto e
nessuno se ne sarebbe accorto. Ora §B8 impone i numeri NUDI («un'unità vuol dire che stavi pensando in
metri») e il tracker avvisa dicendo anche la conversione giusta.

## 2026-08-04 (8) — DUE DOMANDE AL POSTO DI DUE ELENCHI (06 v5.19 / cv60 / ov37 / lv31)

Rilievo del GM sulle regole appena scritte: **troppe negazioni cucite sul caso di prova**. Audit fatto — il
blocco Arena era 19% racconto di difetti osservati e 6% citazioni testuali di Toto-Rak. Ma il numero non era
il problema: il problema era **dove stava l'istruzione operativa**. In tre regole l'operativo era un ELENCO DI
FRASI, e il principio generale stava in coda o non c'era.

**«Il corpo del mostro non è un elemento»** era un'enumerazione — coda velenosa, spruzzo acido, viticci
spinosi — destinata ad allungarsi di una voce a ogni caso nuovo. Sostituita dal **TEST DELL'INDOMANI**: *ci
sarebbe ancora, a scontro finito e cadaveri freddi?* Se sì è la stanza e si dichiara; se no è la creatura e sta
nello stat block. Copre code, spruzzi, aure, spore, un muro di ghiaccio evocato al secondo round, e non chiede
se il nemico sia pianta, bestia o macchina — per questo è una domanda e non una lista di parti anatomiche.

**«Dichiara il mezzo»** apriva con cinque frasi italiane e teneva il test in fondo, cioè nell'ordine in cui si
impara a riconoscere le frasi invece del criterio. Ribaltato nel **TEST DELLA POSIZIONE**: *un PG può starne
fuori senza muoversi?* Se sì la cosa ha un posto, e la zona è quel posto; se no la cosa NON ha un posto perché
**è** il posto, e la zona è *ovunque*. Nessun vocabolario da memorizzare: la formulazione varia, il test no.

**«Un muro non è un elemento»** era per l'80% racconto del difetto. Ora apre sul principio — *quello che
'Tipo' già disegna non si dichiara* — e i due nomi manuali sono una consultazione di due voci, non
un'euristica.

Le failure shape restano (sono house style e sono prove), ma ridotte a una clausola e chiaramente subordinate
al test. Misurato dopo: citazioni dal 6% all'**1%**, racconto dei difetti dal 19% al **9%**, blocco da 11.282
a 10.773 caratteri. Zero residui verbatim del caso di prova. I due test sono nominati e richiamati da §B8, dal
self-check e dai tre file di istruzioni, così una regola sola vale in tutti i punti che la usano.

**TRACKER:** l'asserzione sul ripiego di zona chiedeva il 100% dentro la fascia, mentre il codice promette
«non lontano». Test allineato a quel che il codice garantisce davvero: ≥90% dentro, e nessuna casella oltre
due passi dalla fascia dichiarata.

## 2026-08-04 (7) — IL MEZZO DENTRO CUI SI COMBATTE (06 v5.18 / cv59 / ov36 / lv30)

**IL DIFETTO, visto su due scontri di fila.** Read-aloud: «il **fango sotto i vostri piedi** inizia a
tremare» → dichiarato *Fango — centro*, e il gruppo guadava una sala asciutta con una pozzanghera. Read-aloud:
«scendete nei **corridoi allagati** … **l'acqua vi arriva alle ginocchia** e una **densa nebbia** verdastra
ristagna sulla superficie» → dichiarati né l'acqua né la nebbia, e al loro posto *Acido/Tossina — centro*, una
sostanza nominata **solo in Innesco e Tattica**, che la mappa non legge per regola. L'acqua e la nebbia ERANO
lo scontro. Nel primo caso, in più, *Rovi/Spine* erano i **viticci della pianta**, cioè il mostro.

**LA REGOLA NUOVA, e ha un test di una domanda sola.** Prima di elencare l'arredo si dichiara **il MEZZO**:
cos'è il pavimento adesso e cosa c'è nell'aria — acqua, fango, ghiaccio, ragnatele, erba alta, nebbia, fumo.
È normalmente la prima riga di **Elementi** ed è normalmente *ovunque*, perché una prosa che mette il gruppo
DENTRO qualcosa ne ha già dichiarato l'estensione. **IL TEST: un PG può restarne fuori senza muoversi? Se no,
è *ovunque*.** Il mezzo conta più dell'arredo perché cambia MOVIMENTO e VISTA a ogni turno di ogni
combattente, mentre una cassa cambia una casella: una cassa mancante non costa nulla, un pavimento allagato
mancante costa tutto lo scontro.

**CATALOGO RIVISTO** (25 voci dichiarabili, invariato nel numero):
- **Fango** 🟤 e **Muffa** 🦠 separati — erano una voce sola e non lo sono.
- **Acqua Profonda** ora 🔵: acido 🟢, acqua 🔵 e fango 🟤 sono lo STESSO disco in tre colori, così sulla
  mappa si leggono come tre versioni della stessa cosa — il terreno su cui stai.
- **Erba Alta** (via *Solchi*), **Siepe** (via *Filare*).
- Via **Cristallo Etereo** e **Tronco Colossale**.
- **+ Nebbia/Fumo** 🌫️, con un tipo suo (`type-obscuring`) perché in 5e la nebbia fitta **non è copertura**:
  è area PESANTEMENTE OSCURATA, non dà CA e toglie la vista. Per questo è anche esente dal vincolo dei
  pilastri: una nube lambisce le pareti, un pilastro no.

**DUE DIFETTI DEL GENERATORE, trovati misurando.**
1. **La zona satura sparava l'elemento dall'altra parte della sala.** Se il terzo dichiarato era pieno, il
   ripiego saltava sull'INTERO pavimento: macerie dichiarate «fascia ovest» finivano a est, che è peggio che
   non piazzarle — la mappa smetteva di combaciare con la prosa proprio dove doveva. Ora il rettangolo si
   **allarga di un passo alla volta**. Misurato: 215 elementi su 4 voci stipate in un angolo, zero finiti
   lontano.
2. **Il mezzo riceveva la stessa fetta di budget di una cassa.** Il budget si divideva in parti uguali, e
   «acqua ovunque» usciva come due chiazzette. Ora la quota è **proporzionale al peso** e un elemento diffuso
   pesa doppio: il fango passa dal 49% al **64%** della larghezza calpestabile.

**BUG DELL'IMPORT.** Con DUE pacchetti incollati insieme, la sezione Arena del primo arrivava fino
all'intestazione del secondo e ne masticava le righe come elementi («Pacchetto Incontro non è nel
catalogo»). '**Pacchetto Incontro**' è ora una parola di stop come le altre.

## 2026-08-04 (6) — GLI ELEMENTI SI LEGGONO DAL READ-ALOUD, NON SI SCELGONO (06 v5.17 / cv58 / ov35 / lv29)

Secondo collaudo, e la sezione Arena non combaciava con la prosa che le stava sopra. Il read-aloud diceva
«una rotonda di pietra Gelmorrana **invasa da ragnatele e sostanze vischiose**», e gli Elementi dichiaravano
*Acido/Tossina* al centro (che erano le **zanne e la coda del mostro**), *Rocce* a est e ovest (che **nessuna
frase descriveva** — «pietra Gelmorrana» è di cosa sono fatti i MURI) e *Ragnatele* confinate in una fascia.
Una riga su tre corrispondeva alla stanza, e le due cose su cui la prosa insisteva mancavano o erano fuori posto.

**1. VIA IL NUMERO DI ELEMENTI.** §B8 suggeriva «three to six entries in a normal fight»: un bersaglio da
centrare, che si centra riempiendo. Ora la regola è una PROCEDURA: **si scrive prima il read-aloud, poi si
rilegge la propria prosa e si scrive una riga per ogni cosa che dice essere nella stanza.** Il conteggio si
decide da sé — una rotonda spoglia ne ha due, un'officina crollata sette, e nessuna delle due sbaglia. Niente
riempitivi e niente elementi che i giocatori non sentiranno mai nominare.

**2. ANCHE LA ZONA SI LEGGE DALLA PROSA.** La stessa frase che nomina la cosa di solito dice DOVE sta: «lungo
la parete est» è *fascia est*, «al centro della sala» è *centro*. E **quando la prosa dice tutta la stanza,
la zona è *ovunque*** — «invasa da», «il pavimento è coperto di», «dappertutto». Il self-check ora confronta
anche l'ESTENSIONE, non solo il nome.

**3. IL TRACKER RENDE *ovunque* COME DIFFUSO.** Prima «ovunque» voleva dire «una chiazza grande in un punto a
caso», che è il contrario di «invasa». Ora un elemento dichiarato sull'intero pavimento riceve più GRUPPI più
piccoli, tenuti staccati fra loro, a parità di budget; un elemento con una zona precisa resta concentrato,
che è il suo senso. Misurato su 50 mappe da 18×18: 4,6 chiazze contro 1,4, estensione 22,3 contro 10,1.

**4. DUE VOCI NUOVE, entrambe per un buco reale.** *Voragine/Vuoto* — §B10 impone di stabilire il pericolo
mortale dell'arena di un trial (la spinta nel baratro, la piattaforma sospesa) e poi di dichiararlo, ma nel
catalogo **non c'era modo di dirlo**. *Cristallo Etereo* — firma di metà delle arene di FFXIV, che finiva
schiacciata su «Meccanismo». Il catalogo dichiarabile sale a 25.

**5. LA PAROLA DELLA PROSA SCEGLIE LA VOCE.** Aggiunta a §B8 la mappatura che mancava, nel verso giusto:
*sostanze vischiose, melma, resina* → *Fango/Muffa*; *un crepaccio, il vuoto oltre il bordo* → *Voragine/Vuoto*.
Il catalogo è lo strato MECCANICO: un suo nome non entra mai nel read-aloud.

## 2026-08-04 (5) — UN MURO NON E' UN ELEMENTO, E UN PILASTRO STA DA SOLO (06 v5.16 / cv57 / ov34 / lv28)

Osservazione del GM: **«Muro di Pietra» finiva in quasi ogni arena**. Due difetti sotto una sola segnalazione.

**1. IL MURO NON SI DICHIARA.** Il perimetro della stanza lo disegnano già `Tipo` e `Forma`; dichiarare un muro
non lo traccia, **semina pezzi di muratura sul pavimento dove il gruppo combatte**. Il nome però legge come la
cosa più ovvia da nominare in una stanza di pietra, e l'assistente lo sceglieva per questo. Ora «Muro di
Pietra» e «Grata/Cancello» sono **fuori dal catalogo dichiarabile** — restano nella tavolozza del tracker,
per ritoccare a mano una mappa già fatta, ed è esattamente il mestiere per cui esistono. Il catalogo di §B8
scende a 23 nomi. Chi li dichiara riceve un avviso che dice cosa usare al loro posto.

**2. LA COPERTURA TOTALE IN CAMPO APERTO È UN PILASTRO, E STA DA SOLO.** Un pilastro appoggiato alla parete non
offre riparo che il muro non desse già, e due pilastri accostati sono un muro corto: in entrambi i casi la
copertura non vale niente. Il generatore ora lo sa — un elemento `type-cover-total` **non viene mai piazzato
adiacente a un muro né accanto a un altro pezzo di copertura totale**, e per questi la distanza minima NON si
allenta quando lo spazio scarseggia: meglio un pilastro in meno che un pilastro inutile. Su un corridoio
stretto, di conseguenza, i pilastri semplicemente non entrano. Misurato su 60 mappe: 252 pilastri, zero
attaccati a un muro, zero adiacenti fra loro; il vincolo non tocca rocce, acqua e fango, che continuano a
lambire le pareti come prima.

## 2026-08-04 (4) — QUATTRO CORREZIONI DAL PRIMO COLLAUDO DELLA SEZIONE ARENA (06 v5.15 / cv56 / ov33 / lv27)

Primo pacchetto vero passato nel tracker con la sezione Arena, e quattro cose non tornavano.

**1. GLI ELEMENTI SENZA TRATTINO VENIVANO RIFIUTATI IN BLOCCO.** Il parser pretendeva `- ` davanti a ogni
elemento, ma **incollando il pacchetto come testo semplice i punti elenco del markdown spariscono**: un'arena
scritta a regola d'arte dava «Nessun elemento riconosciuto». Ora dopo `Elementi:` ogni riga non vuota è un
elemento, il trattino è consentito e non preteso, e si accetta anche l'elenco `·`-separato sulla stessa riga.

**2. VIA LA DESCRIZIONE DELL'AMBIENTE ETICHETTATA.** Un blocco «Descrizione visiva (Ambiente):» sopra il
pacchetto descriveva in tre frasi la stessa stanza che il «Da leggere ai PG» descrive subito dopo, meglio e al
posto giusto. Non era in §A4 — era un'invenzione dell'output. Ora §A4 dice che **la descrizione di un luogo è
prosa giocata e non porta etichetta**: '**Descrizione visiva:**' è una riga di stat block e appartiene a una
CREATURA o a un PNG (§B6), un luogo non ne ha mai una.

**3. VIA IL CAMPO DELL'ESITO.** Un paragrafo che prevede cosa succede se il gruppo perde o lascia il nemico in
piedi è una supposizione che il GM deve poi smentire, stampata sopra lo stat block dove compete con quello che
serve davvero a metà combattimento. L'esito si decide al tavolo, e quando conta per la storia lo porta già la
riga '[Info GM]' (§B1). Il pacchetto **imposta** lo scontro, non lo risolve.

**4. UN MOSTRO CON TUTTI GLI ATTACCHI TELEGRAFATI NON PUÒ ATTACCARE.** Osservato: un mini-boss le cui uniche
due azioni erano entrambe telegrafate, e un Multiattacco che combinava esattamente quelle due — una creatura
che al proprio primo turno non tira nulla. §B10 ora impone che **ogni stat block abbia almeno un attacco SENZA
'**Telegrafo:**'**, con il conteggio prima dell'invio: il danno di base sta sugli attacchi normali, il
telegrafo si spende su ciò che merita il preavviso (l'area, la fase, la meccanica da leggere e schivare).
Nessuna sezione «Azioni Speciali» separata: la riga '**Telegrafo:**' sotto la voce è già ciò che la marca,
sulla pagina e nel tracker.

**TRACKER, in più:** tutto quello che sta fra il TS e la prima sezione (Resistenze, Immunità, Vulnerabilità)
non è più reso come una mossa ma entra nel riquadro dei dati difensivi, etichetta in grassetto e valore
normale. Vale anche per i tracker già salvati, senza toccarne il formato.

## 2026-08-04 (3) — L'AMBIENTE SI DICHIARA, NON SI INDOVINA (06 v5.14 / cv55 / ov32 / lv26)

Segnalazione del GM sul pacchetto «Il Terrore delle Fauci»: **la mappa non ha senso con la descrizione, e in
prosa non si capisce cosa è ambiente e cosa è roba del mostro**. Il difetto non era tarabile, era strutturale.

**LA CAUSA.** La mappa nasceva da regex sulla prosa del «Da leggere ai PG». Ma un read-aloud descrive il
MOSTRO almeno quanto la stanza, e nessuna scansione sa distinguerli. Sul Graffias, quattro elementi su quattro
erano il boss: «la **pozza** d'acido» → Acqua Profonda, «spruzzo di **melma** verdastra» → Fango/Muffa, «coda
**velenosa**» e «linfa **corrosiva**» → Acido/Tossina, «sulla **pietra**» → Rocce. Nessuno di questi era
sul pavimento. In più le posizioni erano casuali: il testo diceva «pozza **al centro** della stanza» e l'acido
finiva in cima alla mappa.

**LA CURA — SEZIONE `#### Arena`, OBBLIGATORIA IN OGNI PACCHETTO (06 §B1/§B8).** L'ambiente si DICHIARA:
`**Tipo:**` fra nove etichette chiuse, `**Dimensioni:**` in caselle, `**Forma:**` opzionale, e `**Elementi:**`
con una riga `- <Nome> — <zona>` per elemento, nomi dal catalogo chiuso e zone da un vocabolario chiuso
(nord/sud/est/ovest/centro/angoli/ingresso/fondo/ovunque). Il tracker semina E fa crescere l'elemento dentro
quel terzo di pavimento, quindi «Acido/Tossina — centro» mette davvero la pozza in mezzo.
**NIENTE RIPIEGO:** il motore a regex sulla prosa è stato CANCELLATO (lessico delle forme, `classifyShape`, le
25 regex del catalogo). Un pacchetto senza sezione Arena non produce una stanza a caso: carica nemici e
statistiche e lo dice.

**LA REGOLA DI SINCRONIA.** Ogni voce di **Elementi** è nominata nel read-aloud col suo sostantivo ordinario, e
nel read-aloud non si descrive nessun ambiente che non sia in **Elementi**. Il corpo del mostro è l'eccezione e
la ragione della regola: si descrive liberamente e non si dichiara mai. Il self-check di §B8 passa da quattro a
sei condizioni contabili, due delle quali sono un confronto fra due numeri.

**BUG COLLATERALE CHIUSO.** «🔄 Rigenera Mappa» ri-scandiva `narrativeText` INTERO mentre l'import usava solo il
read-aloud: i due percorsi davano mappe diverse, ed è da lì che nascevano le 🕸️ Ragnatele viste dal GM
(«bozzoli», in **Conseguenze**). Ora si rigenera dalla sezione Arena salvata sullo scontro.

Riconciliato anche il vecchio elenco campi di §B1, che citava ancora un campo `terreno` mai emesso, e l'esempio
di failure shape che stampava la stringa `Terreno:` in una regola.

## 2026-08-04 (2) — UN NOME FRA PARENTESI FACEVA SPARIRE IL MOSTRO (06 v5.13 / cv54 / ov31 / lv25)

Collaudo del GM sul pacchetto «Il Guardiano delle Radici»: **il mostro non compare nel tracker e la mappa non
c'entra niente con la descrizione** — un «cunicolo cupo» dove «il passaggio si stringe» era diventato uno
Spazio Aperto 23×20 con sedici caselle di fuoco. Tre difetti, e i primi due si tenevano per mano.

**1. L'INTESTAZIONE DELLO STAT BLOCK NON REGGEVA UN NOME NORMALE.** La regex pretendeva che il nome fosse fatto
di soli `[A-Za-z0-9 '‑]`. L'intestazione vera era
`Coeurl a Nove Code (Coeurl O' Nine Tails) — Grande · CA 13 · PF 45…`: le **parentesi** del nome inglese
spezzavano il match, quindi zero stat block, zero nemici. Non è un caso limite — §A5 chiede il nome canonico e
il nome inglese fra parentesi è la forma normale di metà del bestiario.
Ora **si riconosce la RIGA dai suoi campi obbligatori, non il nome**: una riga con un separatore — poi taglia,
`CA n` e `PF n` (esattamente il formato che §B6 impone) è un'intestazione, e il nome è tutto ciò che sta prima
del trattone, qualunque carattere contenga. Un eventuale `(nome inglese)` finale viene tolto dal nome, così
combacia con la riga `Nemici:`. CA, PF e DES si leggono dal BLOCCO e non dall'intestazione: se un campo manca,
il mostro entra lo stesso invece di sparire.

**2. LA MAPPA LEGGEVA ANCHE LO STAT BLOCK.** Conseguenza diretta del punto 1: fallito il riconoscimento, il
testo-mappa era l'INTERO pacchetto. «Vulnerabilità: **fuoco**» diventava un incendio sul pavimento. Ora la
mappa si costruisce **solo sul blocco «Da leggere ai PG»**, ritagliato fino all'etichetta successiva — che è
quel che §B8 già dichiarava, ma il codice prendeva «tutto quello che sta prima del primo stat block», cioè
anche Innesco, Tattica e Conseguenze. È anche una rete di sicurezza: se domani un'intestazione sfugge di
nuovo, lo stat block resta comunque fuori dalla mappa. «Rigenera Mappa» usa la stessa sorgente, altrimenti
darebbe una mappa diversa da quella appena importata.

**3. LA FORMA SI DECIDEVA COL PRIMO TERMINE CHE COMBACIAVA.** Difetto di progetto, non un termine sbagliato:
due catene `if/else` in cui la seconda sovrascriveva sempre la prima. «cunicolo» e «il passaggio si stringe»
fissavano *Passaggio Stretto*; poi «l'acqua della **palude** filtra dal soffitto» e «sbarrano la **strada**»
— due parole incidentali — lo ribaltavano in *Spazio Aperto*, che per giunta è l'unica forma **senza muri**:
il cunicolo perdeva le pareti, che erano il punto tattico della scena.
Sostituito con un **classificatore a punteggio pesato** (piccolo modello bag-of-words, la cosa standard per
questo mestiere): ogni famiglia somma i pesi di TUTTI i suoi termini presenti e vince il totale piu´ alto,
sopra una soglia. I pesi dicono quanto un termine è davvero una forma — `cunicolo` 3, `si stringe` 2.5,
`palude` 1.5, `strada` 0.5 — e lo Spazio Aperto ha dei **termini NEGATIVI** (`soffitto`, `sotterraneo`,
`pareti`, `cripta`, `corridoio`…): se il testo dice che si sta al chiuso, non gli si tolgono i muri.
Sul pacchetto reale: *stretto* 7.0, *arena* 1.0, *aperto* −0.5.

**Due parole sono state DEGRADATE, ed è un cambio di contratto che §B8 registra:** `grande` ed `enorme` da sole
non nominano piu´ una forma. In pratica descrivono il MOSTRO («un **enorme** bulbo vegetale») e la vecchia
catena le trattava come parole-stanza: è così che un corridoio diventava un'arena. Anche `naturale` è sparito
dalla famiglia caverna per lo stesso motivo. In cambio sono entrati i sinonimi che mancavano — strettoia,
budello, angusto, tunnel, andito, passerella, salone, aula, anfratto, ruderi, anfiteatro, piazzale, spianata,
rotonda — e §B8 e le tre istruzioni li elencano, perché quelle liste e il tool sono le due metà dello stesso
contratto.

**Semplificazione ricavata:** le misure delle nove forme stavano in due posti (le catene `if/else` e
`MapPresets`, aggiunta ieri per il menu «Genera Mappa»). Ora c'è solo `MapPresets`, e il classificatore ne
restituisce la chiave. Le due catene sono sparite.

**NON aggiunto, e vale la pena dirlo:** «spesse radici sotterranee» e i «viticci» del bulbo non ammobiliano
niente. Una voce `radic|lian|viticc` nel catalogo sembrava ovvia, ma nell'altro pacchetto di collaudo le
mandragore «brandiscono le loro **radici** come clave»: sarebbe stato lo stesso identico difetto di «clave»
→ lava, cioè un pezzo del MOSTRO scambiato per arredo. Se servono le radici come terreno difficile, il
vocabolario di §B8 va esteso con un termine che non sia anche un'arma naturale.

**4. SU UNA MAPPA PICCOLA VINCEVA IL PRIMO ARRIVATO.** Segnalato dal GM sul cunicolo generato dopo le
correzioni sopra: 5×15, cinque elementi riconosciuti dal testo, e sulla mappa **solo grata e sassi** — cinque
caselle di Rocce, e Macerie, Acqua e Fango assenti del tutto. Il ciclo esauriva un elemento alla volta: il
primo prendeva tutti i gruppi che il suo profilo prevedeva, il tetto d'ingombro (26% del pavimento, qui 10
caselle su 39) finiva sul secondo, e gli ultimi tre non venivano mai raggiunti. Su una radura da 484 caselle
non si notava; su un cunicolo si.
**Decisione del GM: su una mappa piccola la VARIETÀ vale piu' della quantità.** Il piazzamento ora fa due
passate: la prima garantisce **un gruppo per OGNI elemento nominato dal testo**, con una quota di caselle pari
a `budget / numero di elementi`; la seconda distribuisce **a giro** i gruppi in piu' previsti dai profili,
finche' resta budget. Nessun elemento puo' piu' mangiarsi la quota degli altri, e un blocco 2x2 viene posato
solo se ci sta dentro la quota. Anche la distanza minima fra semi si allenta quando serve (2 → 1 → 0): in un
corridoio largo tre caselle pretendere due caselle di stacco significava non piazzare niente.

**5. GRATE E CANCELLI: RICONOSCIUTI, MAI PIAZZATI DA SOLI.** Nel cunicolo il tool metteva una grata in mezzo
al corridoio. Ma una grata o un cancello sono quasi sempre l'INGRESSO della stanza — la prosa li nomina di
continuo («i resti di una cancellata in ferro battuto») e sono una porta, non un ostacolo a metà campo.
La voce resta nel catalogo, trascinabile a mano dove il GM la vuole, ma porta un flag `manualOnly` e il
generatore la salta. È un meccanismo generale, non un caso speciale nel ciclo di piazzamento. Di conseguenza
«grate» e «cancelli» escono dal vocabolario dei sostantivi in §B8 e nelle istruzioni: nominarli non ammobilia
piu' niente, e lasciarli in lista sarebbe esattamente il difetto invisibile che quell'accoppiamento deve
evitare.

**INTESTAZIONE DELLA MAPPA SU UNA RIGA SOLA.** «Passaggio Stretto (7 × 18)» e i due comandi non vanno piu' a
capo: titolo con `white-space: nowrap`, header `flex-wrap: nowrap`, e la `min-width` del pannello — gia'
calcolata sulla larghezza della griglia — ora è il MASSIMO fra griglia e riga di intestazione. Sotto quella
misura è il pannello intero ad andare a capo sotto il tracker, che era gia' il comportamento voluto.

**VERIFICA:** le regex nuove sono state riprodotte in Python ed eseguite sui **due pacchetti reali** presi dai
JSON salvati dal GM.
— *Guardiano delle Radici*: stat block riconosciuto (`Coeurl a Nove Code`, line1 `Grande · CA 13 · PF 45…`),
read-aloud isolato (nessuna traccia di «Vulnerabilità» o «Tattica»), forma *stretto*, elementi
Grata/Cancello · Rocce · Macerie · Acqua · Fango — **nessun fuoco**.
— *Disinfestazione dei Solchi* (non-regressione): forma *aperto* e gli stessi cinque elementi di prima.
Anche il piazzamento e' stato riportato in Python: sul cunicolo 5×15, su tre semi diversi, **tutti e cinque
gli elementi presenti** ogni volta (8-9 caselle su un tetto di 10, quota 2 a testa); sulla radura 22×22
14-22% di ingombro e i cinque elementi presenti, come prima. Nessun file di conoscenza toccato da questa
quarta correzione: è politica di piazzamento del tool, non contratto d'ingresso.
Struttura del blocco `<script>` verificata. **Nessun runtime JS in ambiente: il rendering nel browser lo
collauda il GM.**

## 2026-08-04 — cv54 / 06 v5.13: LE ISTRUZIONI CAMPAGNA RISCRITTE DA ZERO IN XML, A PUNTATORI (**DA COLLAUDARE**)

Richiesta del GM: ripartire da zero, istruzioni ridotte all'osso che puntano al knowledge, niente hardcoding.
E' il **terzo tentativo** su questa strada (cv50 XML e i due giri di cv50-MIN sono stati rigettati, LEZIONE
2.35), quindi e' scritto contro le misure che quei tentativi hanno prodotto invece che contro l'intuizione.

**cv53 → cv54: 31.897 → 19.528 B (−39%).** Il taglio non e' uniforme, ed e' il punto: e' guidato da
**LEZIONE 2.34 (il formato si recupera dal RAG, lo stato no)** e da **2.33 (il test di visibilita')**.

- **USCITO, perche' il RAG lo recupera dimostrabilmente** — il registro italiano e i suoi esemplari, la
  tabella dei binding ad alta frequenza (~1,4 KB: nel test MIN `Bosco del Sud` e `Piccolo Rifugio` sono
  arrivati da 07 senza aiuto), i template dei link media, l'ordine e il layout del pacchetto incontro, la
  forma dello stat block, i cinque blocchi dell'enigma, le due opzioni canoniche della riga 🧭, il template
  della riga ⏭️, la conversione metrica. Restano **un puntatore con il codice §, mai una parafrasi**.
- **RIMASTO INTERO, perche' e' STATO e non formato** — il blocco `<cursor>` (cosa avanza il cursore, cosa e'
  transiente, gli interrupt cursor-safe) e ogni riga di comando riscritta per dire **COSA LEGGE e COSA
  CAMBIA**, non solo cosa emette. E' esattamente il guasto di MIN: `/continua` rigioco' il primo beat della
  campagna con `[A]` corretto nel save, perche' la query `/continua` non assomiglia a niente e la regola non
  arrivava mai. Il `<commands>` e' ~8 KB dei 19,5 e resta il blocco piu' grosso del file: e' corretto che lo sia.
- **RIMASTO INTERO, perche' il guasto e' INVISIBILE** — le due righe condizionali del footer (una 🧭 non
  stampata cancella `/viaggio` in silenzio), NOTHING IS LEFT BEHIND con i suoi quattro passi e il puntatore
  **08.1 letterale**, la milestone dentro il beat, WRITE LONG, il VOI plurale.
- **Zero priming (LEZIONE 2.32):** nessuna stringa sbagliata stampata nel file. L'unica coppia
  giusto/sbagliato sopravvissuta e' il `voi` contro il singolare, dove la coppia *e'* la regola.
- **`<checks>` a condizioni contabili** e `<contract>` in coda a 5 clausole, per la regola «le restrizioni
  critiche vanno in ultima riga».
- **I segnaposto passano da `<nome>` a `{nome}`:** in un file XML una parentesi angolare e' un tag, e un
  segnaposto in parentesi angolari e' ambiguo per il parser del modello. Nessuno dei tentativi precedenti
  aveva chiuso questo dettaglio.

**QUATTRO BUCHI VERI TROVATI NEL KNOWLEDGE durante il controllo, e chiusi li' (06 v5.13).** Un puntatore vale
solo se la sezione puntata contiene davvero la regola: prima di togliere qualsiasi cosa dalle istruzioni ho
verificato per stringa che vivesse in 05/06/07/08. Quattro non c'erano.
- **§A1 — LE MISURE IN OUTPUT SONO METRICHE:** la regola viveva SOLO nelle istruzioni. Ora e' una riga
  output-forcing con la scala completa (1 ft = 0,3 m), la virgola decimale e l'elenco dei posti dove un
  numero raggiunge il GM (`Vel`, gittate, raggi, portata, distanze nel read-aloud).
- **§A4 — LA CONTRADDIZIONE DEL MEDIA TOOL:** il primo punto vietava ogni chiamata a tool, poi
  `HOW TO DO IT` diceva «rephrase to trigger the integrated search» e `HIERARCHY` metteva l'inline al primo
  posto. Due strati in disaccordo dentro la stessa sezione, ed e' la sezione a cui ora punta `<media>`.
  Riscritta a link-only, senza inline, con `&tbm=isch` dichiarato parte dell'URL.
- **§A4 — LA DENSITA' PER BEAT:** diceva «at least at the FIRST occurrence per entity in each answer/act»,
  che non dice che **il conteggio riparte a ogni beat**. Le istruzioni lo dicevano, il file no. Ora e'
  esplicito, con il boss e il PNG gia' linkati in un beat precedente nominati come il caso che fallisce.
- **§B1 — FOOTER ORDER SENZA LA RIGA ⏭️:** l'elenco ordinato del footer aveva quattro voci e la riga
  connettiva non era una di quelle (viveva 10 righe piu' su, descritta come «accanto alla 🧭»). Ora e' la
  voce (4), con il marcatore e il suo `Restano:` come (5), e la clausola «decidi ENTRAMBE prima di emettere
  il footer» accanto all'ordine invece che solo nelle istruzioni.

**CONTROLLO RAG SULLE MODIFICHE A 06 (domanda del GM, e ha trovato roba).** Le lunghezze erano a posto —
963 / 282 / 477 B per le tre righe nuove, contro un tetto di 2.000 e un massimo di file a 1.879 — ma
**LEZIONE 2.13 non parla di lunghezza, parla di UNA REGOLA PER UNITA' RECUPERABILE**, e su quel criterio due
punti erano sbagliati. **(1)** La riga `ENCOUNTER-SCALING SOURCE` di §B1 era arrivata a **1.297 B** e teneva
tre regole distinte: da dove si leggono PG e livello, il FOOTER ORDER, e la clausola «decidi le due righe
condizionali prima di emettere il footer». La regola sul footer stava sotto un innesco che parla di
*scaling degli scontri*. Spezzata in tre bullet — 609 / 448 / 750 B — ognuno con il proprio innesco.
**(2)** In §A4 le mie due righe nuove hanno lasciato `WIKI-REAL SUBJECTS ONLY` e `URL-ENCODING` appese come
righe di continuazione indentate sotto un altro bullet (debito preesistente: erano indentate sotto la voce
`2. CLICKABLE LINK` della HIERARCHY che ho rimosso). Promosse a bullet propri, **zero parole spostate**.
Nessuna riga di 06 supera i 2.000 caratteri, prima e dopo.

**VERIFICATO MECCANICAMENTE:** roster comandi invariato (14 righe, `/cambio Classe` promosso a riga propria) ·
zero rimandi § persi (§A5 e §A6 recuperati in un secondo giro) · zero letterali italiani di output persi tra
quelli che restano nel control layer · zero tag XML non chiusi · zero segnaposto in parentesi angolari.

**DA COLLAUDARE, e il metro e' quello di §1.1d:** il pacchetto Toto-Rak su Gemini 3.6 Flash Esteso, contro
cv49/cv51. **Due avvertenze dichiarate in anticipo, non scoperte dopo.** (1) Questa e' una riscrittura
integrale contro un baseline misurato, cioe' esattamente cio' che LEZIONE 2.35 sconsiglia: se il collaudo
fallisce, la diagnosi non e' «l'XML non funziona» ma «quale singola cosa e' stata tolta», e la risposta va
cercata riga per riga contro cv53. (2) **La parita' §1.1c e' ROTTA:** `ov` e `lv` sono ancora in forma
markdown (ov29 / lv23), quindi ogni blocco condiviso ora diverge. O si allineano dopo un collaudo positivo,
o cv54 resta un candidato.

## 2026-08-04 — IL TOOL DIVENTA UN'APPLICAZIONE (solo `combat_tracker.html`, nessun file di conoscenza toccato)

Sei richieste del GM dopo il secondo collaudo. Nessuna regola di §B8 cambia: il contratto d'ingresso
(riga titolo h3, riga `**Nemici:**`, read-aloud che nomina forma e cose) resta identico.

**SALVA è il salvataggio della SESSIONE, non dello scontro.** «Esporta» salvava solo lo scontro aperto, cioè la
metà sbagliata: un tab su cinque. Ora il payload è
`{ app, version: 2, savedAt, currentEncounterIndex, encounters: […] }` — tutti gli scontri, con nemici,
statistiche, mappe, posizioni delle pedine e pf attuali.

**APRI, accanto a Salva.** Un `<input type=file>` nascosto: si sceglie il JSON e il tracker torna com'era.
Un solo formato accettato, quello nuovo: nessun supporto ai salvataggi vecchi. **Le regex del
`FeatureCatalog` non sopravvivono a `JSON.stringify`** — diventano `{}` — quindi in caricamento ogni elemento
piazzato viene riagganciato PER NOME alla voce viva del catalogo: senza quel passaggio la legenda di una mappa
ricaricata sarebbe muta.

**IMPORTA è solo testo.** Il ramo che riconosceva un JSON incollato è stato tolto: quel mestiere ora è di Apri.
Il modale lo dice, e il placeholder mostra la forma vera del pacchetto (`### Pacchetto Incontro:`, `**Nemici:**`).

**IL COLORE DELLA SCHEDA SEGUE LA PEDINA.** I tab delle statistiche erano tutti blu; la riga nel tracker e la
pedina sulla mappa usavano già `getEnemyColorRGB`. Ora anche il tab: pallino colorato sempre, bordo superiore
e testo del tab attivo nello stesso RGB. Tre canali, un colore per nemico.

**LEGENDA A SINISTRA DELLA MAPPA quando c'è spazio, e NIENTE BARRE ORIZZONTALI.** Primo tentativo con
`container-type: inline-size` + `@container`: sbagliato, e in modo istruttivo. `container-type` implica
`contain: inline-size`, che rende la larghezza dell'elemento indipendente dal contenuto — quindi il
`min-width: min-content` messo sullo stesso pannello per farlo andare a capo valeva **zero**, e stringendo il
resizer la griglia usciva dal pannello e si sovrapponeva al tracker. Anche `min-content` senza containment
si è rivelato instabile: in modalità riga il min-content del pannello CRESCE (mappa + legenda), il pannello si
allarga, e la scelta del layout si morde la coda. Assetto finale, senza anelli di retroazione:
`.map-panel` è `flex: 1 1 0` con una `min-width` IN PIXEL scritta da `renderVisualMap` sulla larghezza reale
della griglia — la larghezza del pannello non dipende mai da come sta messa la roba dentro. Sotto quella
soglia il pannello va a capo sotto il tracker invece di comprimersi. La disposizione interna la decide un
`ResizeObserver`: legenda SOTTO la mappa di default, a fianco (`row-reverse`) solo se il pannello ha spazio
per entrambe. Quindi quando il blocco mappa condivide la riga col tracker la legenda sta sotto, e quando la
mappa ha una riga tutta sua va a fianco. La legenda è `width: min-content`, cioè esattamente la riga dei
filtri — l'unico suo contenuto che non va a capo: né troppo larga né con la barra orizzontale.
Il catalogo NON è più un `<details>`: chiuso, un `<details>` toglie i figli dal flusso, la riga dei filtri
smetteva di contare e la legenda si restringeva. Ora è un div con un bottone di apertura; da chiuso nav e
lista restano nel layout (`visibility: hidden; height: 0`), quindi **la legenda è larga uguale aperta o
chiusa**. Il **Catalogo Completo** ha barra di navigazione propria
(Tutti / Coperture / Terreno / Pericoli / Interattivi, filtro derivato dal `cssType`, nessun dato nuovo) e
scorrimento proprio (`max-height: 300px` + `overscroll-behavior: contain`): sfogliarlo non trascina più tutta
la legenda.

**MAPPA A MANO, DA MODELLO.** «Rigenera Layout» → «Rigenera Mappa», e accanto un menu **Genera Mappa** con le
nove forme che il generatore sa fare (Spazio Aperto · Grande Arena · Sala Ampia · Rovine Complesse · Caverna
Irregolare · Struttura Circolare · Galleria · Passaggio Stretto · Stanza Base). Sceglierne una crea una mappa
VUOTA di quella forma, misure tirate a caso a ogni scelta: la stessa voce due volte dà due caverne diverse.
Non è un secondo generatore — `generateDynamicMap` prende un secondo argomento opzionale e, quando c'è, non
legge nessun testo (quindi nessuna forma dedotta e nessun elemento piazzato). Le forme stanno in una tabella
`MapPresets` che riempie anche il menu, così l'elenco non può sfasarsi.

**SELEZIONE MULTIPLA SULLA MAPPA.** Trascinando un riquadro sul vuoto si selezionano tutti gli elementi che
ci finiscono dentro (Shift somma alla selezione, Shift+clic su un elemento lo aggiunge o lo toglie). Poi:
trascinare uno dei selezionati **sposta tutto il gruppo** dello stesso delta, **Ctrl o Shift + trascina lo
copia** (vale l'uno o l'altro, e la copia funziona anche sul singolo elemento), e
**Canc** lo cancella. Lo spostamento è tutto-o-niente: se anche una sola casella di destinazione è muro o
occupata da un elemento non selezionato, il gruppo non si muove. Il riquadro parte solo dal vuoto, così il
drag&drop nativo del singolo elemento e delle pedine resta intatto. La selezione è tenuta per `uid`, quindi
cambiando scontro o cancellando un elemento decade da sola. Il tasto Canc è ignorato quando il fuoco è in un
campo di testo. Sopra la legenda una riga spiega il gesto e, quando c'è una selezione, dice quanti sono.
L'anteprima di trascinamento nativa mostra solo l'elemento afferrato: per un gruppo se ne costruisce una
apposta con `setDragImage` (tutte le icone del gruppo, fuori schermo perché l'elemento deve stare nel
documento) e nel frattempo si sbiadisce l'intero gruppo, non solo la casella cliccata.

**Titolo della mappa vuoto all'avvio:** niente più «Mappa Tattica» e «Nessuna mappa generata» — l'intestazione
resta vuota finché una mappa non c'è davvero.

**IL PIAZZAMENTO A GRUPPI (la modifica vera).** Il difetto segnalato dal GM su
`disinfestazione_dei_solchi.json`: contenuto giusto, disposizione senza senso — icone singole sparpagliate a
caso, e «una pozza d'acqua larga 1,5 m». Il vecchio algoritmo era uno scatter uniforme con distanza minima:
per costruzione non poteva produrre un raggruppamento. Sostituito con un piazzamento **a semina e crescita**,
la tecnica standard dei generatori di mappe (seme con separazione minima tra gruppi, poi crescita del gruppo),
con un profilo d'ingombro EURISTICO per elemento (`featureProfile`):

| profilo | come cresce | chi |
|---|---|---|
| `blob` | chiazza contigua, cresciuta da una casella già posata (non da un cammino che vaga: così resta attaccata) | acqua, fango, ghiaccio, solchi/erba alta, ragnatele, fuoco, acido, rovi |
| `line` | fila dritta, direzione estratta | siepi/filari, barricate, muri |
| `cluster` | grappolo vicino ma non compatto, entro 2 caselle dal seme | casse, anfore, mobilio, macerie, rocce, cespugli, carri |
| `single` | pezzo isolato, ben distanziato | alberi, tronchi, pilastri, statue, trappole, meccanismi |

**Nessuna icona grande.** Un primo tentativo con pezzi 2x2 veri è stato scartato dal GM: non c'è modo di
piazzarli a mano e il generatore li usava come scorciatoia al posto del raggruppamento. Resta una sola taglia,
1x1, e quando serve una massa più grossa si posa un **blocco 2x2 di quattro caselle 1x1** (`clump`, 30-35% su
masse naturali, casse, macerie, rocce, cespugli, carri; zero su alberi, pilastri, siepi, trappole). Effetto
identico a schermo, e ogni casella resta trascinabile e cancellabile da sola.

**Il tetto d'ingombro è esplicito:** `cellCap = 26% delle caselle di pavimento`. Numero e gruppi scalano con
l'area (`scale`), non con un `rand(1,3)` fisso. La fascia in basso (le 3 righe di schieramento PG) resta
sgombra come prima.

**RIPULITURA (passata ponytail su tutto il file).** Un difetto vero: in `findEmptySpot` l'occupazione delle
pedine si leggeva con `Object.values(entityPositions)` e poi `getCombatantSizeById(ep.id)` — ma l'id sta nella
CHIAVE, non nel valore `{x,y}`, quindi la taglia usciva sempre 1 e una pedina Grande o Enorme non riservava
le sue caselle. Passato a `Object.entries`. Poi solo tagli: campo `enemyColors` (scritto in quattro punti,
letto in nessuno — i colori li calcola `getEnemyColorRGB`), classe CSS `.sb-skills-hl` mai usata, il calcolo
delle radici uniche duplicato dentro `updateCombatant` (ora chiama `getEnemyColorRGB`), la regex acrobatica di
`getCombatantTokenLabel` (ora riusa `getBaseName`), lo statblock vuoto scritto per esteso in tre punti (ora
`emptyStatblock()`), la catena a quattro rami del testo Telegrafo, e `getBaseName("Nuovo Nemico")` su una
costante senza numeri. Nessun cambio di comportamento a parte il difetto sopra.

**VERIFICA:** l'algoritmo è stato riportato in Python ed eseguito su una mappa 22×22 con i cinque elementi
davvero riconosciuti dal testo della Disinfestazione — 18% e 19% di ingombro su due semi diversi, 7 blocchi
2x2 per seme, pozze contigue, filari in riga, casse a grappoli, alberi staccati, fascia PG libera. Struttura
del blocco `<script>` verificata (parentesi e stringhe bilanciate, 1116 righe). **Nessun runtime JS in
ambiente: il rendering nel browser lo collauda il GM** — in particolare Apri/Salva e la `@container`.

## 2026-08-03 (2) — IL PRIMO COLLAUDO DEL TOOL: TRE DIFETTI VERI (06 v5.12 / cv53 / ov30 / lv24)

Primo scontro davvero importato (`Test.txt` → `disinfestazione_dei_solchi.json`, la Disinfestazione dei Solchi).
Tre difetti, tutti trovati leggendo l'export JSON e non l'output a schermo.

**1. LA RIGA TITOLO NON SI VEDEVA.** Funzionava, ma era una riga di testo semplice in mezzo alla prosa: in un
beat con due scontri il GM non trova dove comincia il secondo. Ora è un'INTESTAZIONE h3 — `### Pacchetto
Incontro: <nome>` — allo stesso livello di 'Lore a Strati' e dei nomi degli stat block (§B6). Il parser la
leggeva già anche con i cancelletti davanti, quindi è un cambio di sola resa.

**2. IL SISTEMA MAPPE NON SAPEVA COSA FOSSE UNO SPAZIO APERTO.** Un frutteto radurato — senza un muro in vista
— è stato disegnato come «Sala Ampia» 17×16, muri perimetrali su tutti e quattro i lati e due porte. Le sette
famiglie di forma erano tutte al chiuso: la sola che generava una mappa senza muri (`shape: "open"`) si
attivava su *arena/enorme/immenso*, cioè su un'ARENA, non su un campo. Aggiunta l'ottava famiglia, SPAZIO
APERTO (*all'aperto, a cielo aperto, radura, frutteto, campi, prato, pascolo, bosco, foresta, collina,
pianura, spiaggia, duna, deserto, palude, giardino, piazza, cortile, accampamento, sentiero, strada*): nessun
muro, nessuna porta, e misura da mat da esterno reale, 20-24 caselle di lato (≈ 30-36 m), che è la taglia
standard con cui un DM apparecchia uno scontro campale. Vince sulle altre forme: «ampio frutteto» è un campo,
non una sala grande.

**3. TRE FUOCHI IN UN FRUTTETO.** Nessuno li aveva nominati. La regex del pericolo da fuoco conteneva lo stem
`lav` (per «lava») e la prosa diceva «brandendo le loro radici come **clave**». È il difetto tipico di questo
parser — stem corto senza confine di parola — e non era l'unico: `bott` prendeva «bottino», `mobil`
«immobile», `spin` «spinta», `grat` «grattare». Tutti e cinque ancorati (`\blav[ae]\b`, `\bbott[ei]\b`,
`mobili[oa]\b`, `\bspin[ae]\b`, `\bgrat[ae]\b`).

**4. L'AREA ERA GRANDE E MEZZA VUOTA** (osservazione del GM, non un bug singolo). La quota di oggetti per tipo
era `rand(1,3)` fissa, indipendente dalla superficie: la stessa densità in uno stanzino 10×14 e in un campo
22×22. Ora segue l'area — `featBudget = area/70`, tra 2 e 9, e la distanza minima tra oggetti scende da 2 a 1
casella sopra le 300 caselle. Aggiunte anche quattro voci al `FeatureCatalog` per l'esterno, che prima non
esisteva come ambiente: **Siepe/Filare**, **Carro**, **Solchi/Erba Alta** e i sinonimi mancanti.

**RISULTATO SULLO STESSO TESTO:** prima 3 fuochi inventati + albero + casse + 2 acque in una sala murata;
adesso spazio aperto senza muri, e alberi · casse · siepi/filari · pozze d'acqua · solchi — tutte e cinque
nominate davvero dal «Da leggere ai PG», nessuna inventata.

**§B8 AGGIORNATA DI CONSEGUENZA** (è la metà prosa del contratto, e va sempre mossa insieme al parser): l'ottava
famiglia di forma con la sua nota — *outdoor non è sinonimo di grande, è l'unica forma senza muri* — il
vocabolario esterno nella lista dei sostantivi, la riga titolo come h3 e le condizione (1) e (3) del
self-check riscritte. Regola condivisa identica parola per parola nei tre file istruzioni (§1.1c), verificata
per lunghezza.

**VERIFICA:** le regex sono state estratte dall'HTML e rieseguite in Python sul «Da leggere ai PG» reale di
`Test.txt` — 25 voci di catalogo, 5 riconosciute, zero fuochi, famiglia OPEN riconosciuta. Il rendering nel
browser lo collauda il GM.

## 2026-08-03 — IL TRACKER ESCE DAL SISTEMA (06 v5.11 / 05 v2.05 / cv52 / ov29 / lv23)

**DECISIONE DEL GM, cambio di architettura.** Il tracker di combattimento non è più qualcosa che l'assistente
GENERA: è `combat_tracker.html`, uno **strumento esterno** che il GM apre nel browser e a cui dà in pasto il
testo del pacchetto incontro. Il tool ne ricava da solo la tabella iniziativa, il roster nemici, le schede e
**la mappa tattica**. Di conseguenza tutto ciò che nel sistema serviva a produrre quelle due cose è diventato
peso morto e va via.

**RIMOSSO (in blocco, non deprecato):**
- `09_Assets.md` — **file cancellato**. Conteneva solo §Z1, il template HTML da emettere verbatim.
- `06 §A24` (COMBAT TRACKER) con §A24.1 / §A24.2 / §A24.3 — 48 righe: scope per assistente, contratto dati a
  due forme di riga, pannello `statblocks`, cosa fanno i controlli, invarianti anti-recupero-parziale.
- `06 §B8` MAPPA TATTICA — 95 righe: i nove preset con le loro misure, le due silhouette tonde verbatim, la
  tabella delle sette regioni, il set chiuso di simboli, la regola del bottom-to-top, la riga chiave, la riga
  distanze e i due self-check contati. §B8 resta come sezione ma cambia mestiere (sotto).
- Il comando `/tracker` in tutti e tre gli assistenti, e ogni sua traccia: roster comandi §B1, elenco degli
  interrupt cursor-safe, side-output read-only, self-scan §A9.
- 05: Ch. 2.5 e Ch. 9.2 riscritti sul tool esterno; il conteggio PG del save non alimenta più un tracker.

**AGGIUNTO — §B8 non descrive più un disegno, descrive un CONTRATTO D'INGRESSO.** Il pacchetto incontro adesso
ha tre campi che il tool legge, e ognuno fallisce in SILENZIO se manca:
1. **La riga titolo** `Pacchetto Incontro: <nome dello scontro>`, prima riga del pacchetto. Prima non veniva
   mai emessa: il parser la cercava già (`combat_tracker.html`, `importFromText`) e non la trovava mai, quindi
   **ogni scontro importato si chiamava "Nuovo Scontro"**. Difetto trovato leggendo il tool, non le istruzioni.
2. **La riga roster** `**Nemici:** <nome> ×N · <nome> ×N`, subito sotto `**Innesco:**`, con i nomi identici
   carattere per carattere alle intestazioni `### ` degli stat block. **È la richiesta esplicita del GM** ed è
   la correzione di un canale fragile: il numero di nemici veniva DEDOTTO dalla prosa cercando un numerale
   entro tre parole dal nome (`\btre\b\s+(?:\w+\s+){0,3}<stem>`), che sbaglia su un plurale lontano dal nome,
   su «un drappello di» e su qualunque nome multi-parola. Ora è una lettura, non un indovinello — e la prosa
   torna libera di dire «un drappello» senza costare al GM un roster sbagliato.
3. **Il "Da leggere ai PG" fa doppio lavoro:** è la scena E la sorgente della mappa. Deve NOMINARE LA FORMA
   della stanza con una parola ordinaria (le sette famiglie che il tool classifica: stretto/cunicolo/passaggio
   · corridoio/ponte/galleria · sala/grande/ampio/vasto/spazioso · arena/enorme/immenso ·
   grotta/caverna/antro/cavità · rovine/labirinto · tondo/circolare/ad anello) e NOMINARE LE COSE FISICHE col
   loro sostantivo comune (rocce, macerie, pilastri, casse, barili, ragnatele, acqua, fango, ghiaccio, fiamme,
   acido, rovi, trappole, meccanismi… — il vocabolario che il `FeatureCatalog` del tool riconosce).
   **NON è una regola nuova sulla prosa:** §A1 chiedeva già sostantivi concreti e un blocco che CHIUDE
   SULL'OSTACOLO. È la stessa richiesta con un costo finalmente visibile: «il disordine della sala» non
   ammobilia niente, «casse rovesciate e barili spaccati» ammobilia correttamente. Il self-check di §B8 è
   sceso da due blocchi contati a quattro condizioni.

**MODIFICHE AL TOOL** (`combat_tracker.html`, ora unica versione e autorevole su sé stessa):
- `importFromText` legge la riga `Nemici:` e la usa come **fonte autorevole** del conteggio; la vecchia
  deduzione dalla prosa resta come fallback per un pacchetto scritto prima di oggi. Il match sul nome è esatto,
  con ripiego sulla coda (l'estrazione del nome dallo stat block può trascinarsi un prefisso).
- La riga roster e la riga titolo sono **escluse dal testo che genera la mappa**: un nemico chiamato «Golem di
  Pietra» non deve piazzare rocce sul pavimento.
- La riga titolo accetta anche la forma in grassetto.
- `FeatureCatalog`: la regex del fuoco copre anche `braci|bracier|tizzon|rogo` («braci» non faceva match su
  `brace`, e è la parola che la prosa usa davvero).

**COSA RESTA ACCOPPIATO, ed è l'unica cosa da ricordare:** §B8 e il parser di `combat_tracker.html` sono due
metà dello stesso contratto. Toccare le liste di vocabolario in §B8 senza toccare `FeatureCatalog` (o viceversa)
produce esattamente il difetto di questa architettura: una prosa perfetta che ammobilia una mappa vuota, senza
niente che sembri sbagliato.

**VERIFICA:** le due nuove regex sono state riprodotte in Python ed eseguite su un pacchetto d'esempio — titolo
estratto, roster `{sentinella del bosco: 3, capitano delle sentinelle: 1, mastino: 1}` (nome in grassetto e
voce senza ×N incluse), riga `Nemici:` assente dal testo-mappa, forma e feature riconosciute. Nessun runtime JS
in ambiente: il rendering nel browser lo collauda il GM.

## 09 — Tracker (FILE RITIRATO: il tracker è ora 06 §A24)

> Il file 09 è vissuto un solo commit (e09b0e9) ed è stato riassorbito in 06 §A24. Le voci qui sotto restano
> come storia del template; **la spec autorevole è 06 §A24**, e `09_Tracker.md` non va più caricato.



- **NOTA DI PROCESSO — `combat_tracker.html` è tracciato ma NON caricato.** È la copia apribile in browser, quella che il GM modifica nel GEM e riconsegna. **06 §A24.1 è l'autorevole**; la direzione è sempre HTML → 06 §A24.1, mai il contrario. Le due copie sono già divergite una volta nello stesso turno (il fix v1.2 era finito solo in 09), quindi il controllo di allineamento — diff del codice ignorando il blocco dati — va rifatto a ogni tocco. L'unica differenza legittima è il sottotitolo, che in 09 è un segnaposto.

- v1.2: **FIX — `Resetta Round` perdeva lo SCATTA del primo in ordine** (segnalato dal GM dopo l'uso). In `nextTurn()` la fotografia dei telegrafi (`captureRoundTelegraphs`) veniva scattata PRIMA che il combattente entrante scalasse il proprio contatore. Colpiva SOLO il primo in ordine, perché è l'unico per cui le due cose avvengono nello stesso istante: un mostro che entra nel round col telegrafo a `1` scala subito a `0` (SCATTA), ma l'istantanea salvata era `1` — e `Resetta Round` lo riportava a `⚠ 1`, buttando via lo stato che il GM stava guardando. Corretto invertendo l'ordine: **prima la scalata, poi la fotografia**, perché lo stato d'inizio round è quello DOPO il countdown del primo. Riprodotto e verificato in simulazione, con controprova che un mostro NON primo in ordine si comporta identico a prima (nessuna regressione). Nessun'altra modifica al template.

- v1.1: **ERGONOMIA AL TAVOLO — build del GM, canonizzata** (companion 06 v4.80 / cv27). PERCORSO, registrato perché la lezione è generale: avevo implementato queste modifiche partendo dal template v1.0 e il GM ha fatto **revert** — «non era corretto, troppo diverso dalla versione base». Ha poi sistemato il tracker **direttamente nel GEM**, dove lo usa, e ha consegnato `combat_tracker.html` già funzionante. Quello è ciò che è stato canonizzato. **La lezione: per un artefatto che il GM usa al tavolo, la build giusta la produce chi lo usa, non chi scrive le regole** — il mio compito era dichiarare il confine struttura/dati, non ridisegnare l'oggetto. Verificato per diff: **744 righe di codice contro 744, con l'unica differenza nel sottotitolo**, che è uno dei tre slot dati dichiarati.
  **UNICA MODIFICA APPLICATA AL FILE DEL GM: i dati d'esempio.** Il suo file portava contenuto reale (i Sahagin di una subquest della campagna). Sostituito con segnaposto neutri nella stessa forma e registro, per la ragione già accettata nella potatura esemplari di 06 v4.78: un esempio concreto fa **sovra-adattare al caso**, e qui il rischio è che il modello copi quei nemici in un beat che non c'entra. La struttura didattica è conservata (due gregari identici = due RIGHE ma una sola CARD nel pannello).
  **COSA IL FILE DEL GM AGGIUNGE rispetto alla mia versione scartata** — tre cose che non avevo e che valgono più delle mie: **(a) il turno SALTA i caduti**, con guardia `anyAlive` e limite `attempts` che impediscono il giro infinito quando sono tutti a terra; **(b) `Resetta Round`** ripristina i telegrafi al valore d'inizio round (`roundStartTelegraph`, catturato a ogni cambio round), per rigiocare un round dopo una correzione di regole; **(c) `Resetta Scontro`** riporta i PF al massimo, azzera telegrafi e stati, **ri-tira le iniziative** (`1d20 + initBonus` — ecco perché `initBonus` sta nei dati) e riordina. In più: il campiello danno accetta **Invio**, e PF/CA/iniziativa committano su `change` invece che su `input`, quindi la tabella non si ridisegna a ogni tasto.
  **CONTRATTO DATI: le due righe non hanno la stessa forma.** MOSTRO = `init` pre-tirato, `ac`/`hp`/`maxHp` reali, contatore telegrafo. PG = `init` e `ac` **vuoti** (li scrive il GM: l'assistente non conosce la CA dei PG) e **nessun PF** — i punti ferita li tengono i giocatori, al GM servono la CA per tirarci contro e l'interruttore A TERRA. `isDown` `false`, `telegraph` `null`, `notes` `""` alla creazione.
  **VERIFICA, col suo limite dichiarato:** nessun runtime JS in ambiente, quindi la logica di stato del file del GM è stata **portata in Python ed eseguita** su 22 casi — danno col campiello e a vuoto, floor a 0, salto dei caduti, tutti-a-terra senza loop, avanzamento round saltando i morti, decremento e ripristino del telegrafo, reset scontro con ri-tiro nel range corretto: tutti passano. Prova l'ALGORITMO, non il rendering; quello il GM lo ha già validato su GEM e Project.

- v1.0: **THE `/tracker` ARTIFACT IS NOW A CANONICAL TEMPLATE, NOT A DESCRIPTION** (companion 06 v4.79 / 00 v1.23 / cv26). PROBLEM: §B9 described the build IN PROSE — 5.3 KB of requirements including literal CSS fragments (`html, body { background:#1b1d21… }`, `input { background:#2a2d33… }`) and three observed failure shapes (names rendered white-on-white, a bright frame surviving around the dark panel). That is the worst of both worlds: it paid a template's token cost without giving a template's determinism, and every run re-derived layout, CSS and JS from scratch, so the GM never got the same panel twice. BASE: the GM supplied a GEM-produced tracker that works and that they like (`tracker_di_combattimento_atto_3.html`, 14.6 KB / 472 lines) — canonising something already proven at the table beats designing a new one. It already had the right shape: everything is invariant except `encountersData` (31 of 472 lines) and the subtitle, so the rule reduces to declaring that boundary. **MECHANISM: emit the template VERBATIM; the only things written are the subtitle, `encountersData`, and each encounter's `statblocks`.**
  **CHANGES MADE TO THE GM'S FILE BEFORE CANONISING IT** (deliberately minimal, verified by diff): (a) example data replaced with neutral placeholders — the original named a specific one-shot's acts and NPCs, which would have become bias exactly as the pruned exemplars did in 06 v4.78; (b) **all data strings moved to DOUBLE QUOTES** — the original used `'Spada d\'Acciaio'`, an escaped apostrophe inside a single-quoted literal, which works but is precisely what §B9 warns against: Italian is full of apostrophes and one missed escape blanks the entire artifact; (c) NEW `statblocks` panel (see below); (d) `escapeHtml` hardened with `String(str)`; (e) **a real bug fixed in `sortInitiative`** — it tested `init !== null`, but PCs carry `init: ""`, which JS coerces to 0, so un-rolled PCs sorted at initiative 0 instead of at the bottom; now `""` is treated as unset.
  **NEW — ENEMY QUICK-REFERENCE PANEL (09.2), GM request:** a card per DISTINCT stat block under the table, so a turn can be resolved without scrolling back up the chat. `line` = one defensive line (CA · PF · Vel · TS · Perc. · GdS); `moves` = ONE LINE PER MOVE shaped `Nome — effetto`, carrying only resolvable numbers (to-hit or save + CD, range/area, dice and type, recharge, rider). Binding: **no prose, no lore, no visual description** — those stay in the chat stat block. Phase gates and legendary actions count as moves, because they are what gets forgotten mid-fight.
  **WHY A SEPARATE FILE rather than inside §B9:** 14.6 KB would have quintupled that section inside an already 267 KB file; a single-topic file matches a LEXICALLY RICH query (`/tracker` appears both in the GM's message and in the file), unlike `/continua` which resembles nothing; and the Gemini 10-file cap is not actually contested — we upload 9, and a future per-expansion split of 08 would still upload one 08 at a time. HONEST RESIDUAL RISK: a 14 KB block can be retrieved PARTIALLY, so §B9 keeps the invariants that matter most (exact palette, column set, combatant object shape) in compact form, and a partial retrieval lands close rather than nowhere.



## Project Memory (NUOVO, LOTTO B5 dell'audit) + Handoff RITIRATO

- **mv1: nasce il QUARTO assistente, il MANUTENTORE, e la memoria storica diventa la SUA knowledge.** Richiesta del GM: trasformare l'Handoff in un file di conoscenza, «tutta la conoscenza del progetto come memoria storica di come funziona, cosa fa e come».
  **PERCHÉ NON NEI TRE ASSISTENTI DI GIOCO — misurato, non supposto.** L'Handoff nominava **143 volte comandi ritirati** (`/stop` ×68, `/load` ×44, `/confermo` ×12, `/prepara` ×7, `/nota` ×4, `/gioca` ×3, `/subquest` ×2, `ESEGUO` ×3) e li nominava in **linguaggio imperativo**, non da cronaca: «*LOAD IS COMMAND-ONLY — a load happens ONLY on the explicit /load*». La ragione per cui è inaccettabile era scritta **dentro l'Handoff stesso** — «*il roster è CHIUSO: i comandi rimossi non vanno nominati nella knowledge caricata, perché nominarli li rimette in circolo attraverso il recupero*» — e il lotto B3 aveva appena mostrato che il progetto stava già pagando quel prezzo con TRE menzioni. Con 143 sarebbe stato il guasto peggiore mai introdotto. Secondo danno, più subdolo: l'Handoff **parla di** §B17, §B24, delle procedure di save, quindi è lessicalmente vicinissimo a 06 e nel recupero **competerebbe con lui**, restituendo la *descrizione* di una regola al posto della regola.
  **LA FORMA SCELTA:** un quarto assistente il cui mestiere è sviluppare il sistema, mai giocarlo. Lì la storia completa è un patrimonio e i comandi morti non contaminano niente. **Questo lotto non tocca un byte di ciò che gira al tavolo.**
  **LA RISTRUTTURAZIONE, che è il valore vero.** L'Handoff era 364 righe in 14 sezioni `UPDATE (data)` in ordine cronologico: **92,9 KB di cronologia contro 26,7 KB di architettura evergreen**, e si dichiarava *«version-agnostic ON PURPOSE»* in intestazione senza esserlo. Era anche profondamente **stale**: `CURRENT STATE` diceva 06 v4.33 (siamo a v4.87), le procedure di save descrivevano `stop`/`confermo`, la mappa file elencava 00 e il builder JSON. `PM` lo sostituisce in cinque strati: **1 ARCHITETTURA** (i due strati, il modello a comando singolo, il save lean, il modello canonico Eco/Benedizione/Tempra, tutto corretto allo stato attuale); **2 LEZIONI** — 15 lezioni staccate dalla loro data, incluse le tre teorie sbagliate da non riprovare e le decisioni RIGETTATE; **3 PRATICA DI EDITING**; **4 QUARANTENA**, dove ogni nome ritirato compare **una volta sola, in tabella, taggato**, invece di essere sparso nel testo; **5 ARCHIVIO** compresso.
  **NOME:** `FFXIV_GEM_Project_MASTER_Handoff.md` → **`Project_Memory.md`**. Il vecchio nome portava «GEM» (host che il progetto ha lasciato) e «Handoff» descriveva un passaggio di consegne, non una memoria. Il prefisso **`M`** lo tiene fuori dallo spazio dei nomi `01-08`, così un caricamento nel Project sbagliato è visibile a occhio.
  **`CHANGELOG.md` sale come seconda knowledge del Manutentore** — è già il registro delle decisioni, comprese quelle rigettate, cioè esattamente ciò che serve per non ri-proporre una strada chiusa. Non cambia, cambia solo dove viene caricato.
  **`Instructions_Maintainer.txt` (mv1)** porta tre vincoli che lo rendono sicuro: il **DIVIETO ASSOLUTO** di emettere contenuto di gioco (beat, stat block, save, tracker, tag) — perché generarlo qui compete in silenzio con gli assistenti veri e non insegna niente; la **QUARANTENA**, cioè l'obbligo di verificare nel file di istruzioni CORRENTE prima di dichiarare che una capacità esiste; e l'obbligo di **citare la fonte** di ogni affermazione, perché una tesi non tracciabile è un'ipotesi e va etichettata come tale. A differenza degli assistenti di gioco, qui un messaggio senza `/` è conversazione normale: il Manutentore non è un esecutore a comando singolo.

## 00 — Manual Index (FILE RITIRATO, LOTTO B1 dell'audit)

> **`00_Manual_Index.md` è stato RIMOSSO dal set caricato.** I file di knowledge sono ora **8: 01-08**.

- **Motivo: non faceva niente.** Metà del file era ROUTING («Razze → 01», «Incantesimi → 03») — ma in una pipeline RAG il modello **non legge un indice per decidere cosa recuperare**: il recupero è per similarità, in un colpo solo, senza un secondo giro di lookup. Quella tabella poteva solo occupare spazio nel corpus e competere nel chunking. L'altra metà era già scritta altrove.
- **Verificato blocco per blocco, ZERO contenuto unico:** precedenza dei file e forma di citazione → `cv` L.14-15 e 06 §A1 · split delle due wiki → 06 §A14 e `cv` L.23 · metrico, naming a due livelli, nomi mostri, Dawntrail → 07 G1/G24/G25/G26, `cv` L.30-32/38, 04 SCHEMA NOTES · vocabolario controllato Asservito/Temprato → esisteva **già in tre copie** (05, 06, 07) · coerenza e spoiler policy → 06 §A8 e 05 Ch.1 · 22 job, 8 razze, niente duplicati → 05 Ch.3.2/3.3, dove la regola dei duplicati ricorre **sette volte** · ruoli dei job → 05 Ch.6.7, che mappa ruolo→job nominali ed è quindi più informativo dei conteggi di 00.
- **Nessun file lo citava.** L'unico riferimento in tutto il repo era nell'Handoff, dev-only. La lista `FILE REFERENCES` di 06 partiva già da 01. Nessun riferimento orfano dopo la rimozione, verificato.
- **Effetto:** −6,9 KB dal corpus recuperabile; set caricato da 9 a **8 file**; una casella in meno da ricaricare a ogni modifica.



Dev-only revision history moved out of the RAG knowledge files (they self-identify their
version in the header). **Not uploaded to the Project.** Newest entries first, per file.
Includes REJECTED / do-not-re-apply decisions — the reason they live here and not in-file.

## 06 — Procedures & Format
- **ov28 / lv22 — TRE DIFETTI PREESISTENTI CHIUSI, UNO PER VOLTA.** Trovati durante l'audit rigettato e riportati a galla dopo il ritorno a cv49; nessuno era una mia regressione, vivevano nei file da tempo. **(1) RIDONDANZA:** il paragrafo sulle heading `###`/`####` dello stat block compariva **due volte nella stessa riga** in ov e lv — la seconda copia rimossa, la prima resta al suo posto naturale dentro la forma del blocco. **(2) REGOLA NEL BLOCCO SBAGLIATO:** la riga dell'enigma chiudeva su `▒` mezza copertura (+2) / `▓` tre quarti (+5), che e' una regola di MAPPA, in tutti e tre i file; spostata dentro la riga della legenda accanto all'esempio che gia' c'era («mai un `▒ mezza copertura` nudo»), dove il modello la legge mentre disegna. In lv era gia' presente li', quindi in lv e' solo una rimozione del doppione. **(3) PUNTATORE CHE NON PUNTAVA:** l'OWE di ov diceva «the **08.1** pins», ma un one-shot ha scope libero e **nessun manifest MSQ** — era copia da cv, quindi il passo (1) di NOTHING IS LEFT BEHIND non aveva alcuna fonte da cui enumerare. Sostituito con la fonte reale di quell'assistente: **rileggi la voce di questo atto nell'INDICE DEGLI ATTI stampato da `/genera` (§C2/§C4)** e nomina gli oggetti dovuti uno per uno, incluso il setup da pagare al climax (§E2). E' la stessa classe di guasto che aveva fatto sparire Lahabrea in campagna — un rimando reso generico e' un rimando cancellato (LEZIONE 2.34). **ov 21.866 → 21.919 B · lv 18.945 → 18.548 B.** Numeri di versione: si saltano ov27/lv21, bruciati dall'audit XML rigettato, come cv ha saltato cv50.
- **cv51 — RITORNO A cv49 PIU' UNA RIGA SOLA: IL FOOTER CONDIZIONALE. Decisione del GM dopo tre collaudi.** cv49 e' **l'unica versione con una buona corsa misurata** su Toto-Rak (v5.10: `Restano:` a quattro voci, Lahabrea prima del boss con l'Innesco dal pin, Eco, cinque blocchi su entrambi gli enigmi, aritmetica verificata). Le tre riscritture successive — cv50 in forma XML, poi due giri di cv50-MIN a puntatori — hanno introdotto **una regressione ciascuna**, tutte mie: il puntatore `08.1` reso generico nell'OWE (Lahabrea e l'Eco spariti, e nemmeno in `Restano:`), il grassetto tolto a `EMIT §Z1` (`/tracker` a due tentativi), la semantica del cursore persa in MIN (`/continua` ha rigiocato il primo beat della campagna a Lv 1 con `[A]` = Into the Beast's Maw nel save), la riga letterale di `/voci` persa in MIN (un Aggancio partito come subquest invece di essere offerto). **Controllo riga per riga di cv49: tutti e quattro quei guasti erano cose che le riscritture avevano TOLTO, non cose che a cv49 mancano** — cv49 ha gia' la riga di chiusura di `/voci`, gia' «resume the LIVE cursor», gia' il grassetto sul tracker. Il delta reale era **una voce sola**.
  **L'UNICA AGGIUNTA, e il difetto vero che l'ha motivata:** le due righe condizionali del footer, `🧭 Viaggio` e `⏭️ Tratto connettivo`, **non sono mai state in cv in nessuna versione** — vivevano solo in 06 §B1 BEAT END, cioe' dietro al RAG, e il RAG non le pescava. Il costo e' asimmetrico e invisibile: **un `🧭` non stampato cancella in silenzio `/viaggio`, un `⏭️` non stampato cancella in silenzio `/riassumi`**, e il GM non puo' scegliere un'opzione che non e' stata offerta. Aggiunta UNA riga in §KNOWLEDGE, nello stile di cv49 (imperativa, razionale inline): FOOTER ORDER completo, definizione di tratta NON BANALE (05 Ch.8.4), le due opzioni canoniche del viaggio, la forma esatta della riga connettiva e le sue tre condizioni (N ≥ 2 · beat che avanza il cursore · [C] non ATTIVA). **cv49 31.087 B → cv51 33.062 B. Diff: una riga aggiunta piu' il bump di versione, nient'altro.**
  **ov e lv riportati a ov26 / lv20**, per il vincolo §1.1c: con cv tornato allo stile cv49 le riscritture XML degli altri due avrebbero fatto divergere ogni blocco condiviso. Le tre versioni XML restano su disco come candidati (`Instructions_*_XML.txt`) e la variante a puntatori come `Instructions_Campaign_MIN.txt`; nessun lavoro e' perso, ma **nessuno dei tre e' la versione di produzione.**
  **LA DISCIPLINA CHE MANCAVA, ed e' la vera lezione del ciclo:** quattro riscritture consecutive contro una baseline buona, ognuna con decine di modifiche simultanee, ognuna con almeno una regressione silenziosa. **Contro una baseline che funziona si cambia UNA cosa per volta e si collauda.** Il valore delle riscritture non e' perso — e' tutto in PART 2 (lezioni 2.32, 2.33, 2.34) e li' resta, come misura, senza costare byte al tavolo.
- **cv50 / ov27 / lv21 — [ESITO: RIGETTATO, sostituito da cv51. Tenuto agli atti per le misure che ha prodotto.] LE TRE ISTRUZIONI RIFATTE IN FORMA XML, TARATE SU GEMINI 3.6 FLASH (06 non toccato).** Secondo passaggio sul control layer dopo l'audit cv48, questa volta con la ricerca fatta sul modello uscito il 2026-07-21 e non solo sulla documentazione della famiglia Gemini 3. **COSA DICE LA RICERCA, e cosa ci riguarda.** (a) Gemini 3 «responds best to direct, clear instructions» e **sovra-analizza** il prompt engineering verboso pensato per i modelli vecchi: il razionale inline (`RATIONALE, measured:`, `OBSERVED FAILURE (one real beat)`) non viene letto, viene ragionato. (b) I vincoli negativi aperti fanno **over-index** fino a far cadere la logica di base. (c) **Priming failure** (arXiv 2601.08070, *Semantic Gravity Wells*): nell'87,5% delle violazioni e' la menzione stessa del termine proibito ad attivarlo — e noi stampavamo `'Ammorsalice'`, `'Cantore dei Boschi'`, `'Boscoscuro'`, `'Piana Meridionale'`, `"Sei tornato"`, `450 PE`, `1d7`. Li stavamo insegnando. (d) Le restrizioni critiche vanno in ultima riga. (e) Non mischiare i formati; l'XML da' confini non ambigui fra istruzione, dato ed esempio. (f) 3.6 Flash: 1M di contesto, 91,8% a 128k — **il collo di bottiglia non e' piu' la distanza, e' l'ambiguita'**.
  **QUATTRO INTERVENTI.** **(1) FORMA XML**, uguale nei tre file: `<role> <knowledge> <scope> <output_style> <formats> <media> <commands> <checks> <contract>`, piu' `<workflow>` solo in ov. Scelta host-agnostica (§1.1b): nessun tag nomina un vendor, e' il formato raccomandato dalla guida Gemini 3 ed e' anche quello nativo per Claude Projects. Vantaggio strutturale che vale ovunque: **separa la sintassi dell'istruzione da quella dell'output**, che prima coincidevano (`**grassetto**` era insieme enfasi della regola e formato dello stat block). Lingua invariata, §1.4: tag e regole in inglese, italiano solo dove E' output. **(2) NIENTE PIU' STRINGHE SBAGLIATE STAMPATE.** Un divieto si esprime con la forma corretta. I quattro nomi inventati escono dalla tabella dei binding, che gia' fa il lavoro in positivo; `450 PE`, `1d7`, `"Sei tornato"` spariscono. Grep di regressione pulito su tutti e tre. Unica coppia giusto/sbagliato sopravvissuta: `voi` contro il singolare, perche' li' la coppia E' la regola. **(3) BLOCCO `<checks>` NUOVO, in coda prima del contratto:** ogni failure shape diventa una **condizione contabile** (`enemies inside the two rows nearest the bottom edge: 0`, `the printed PF total equals its dice expression`), che e' la disciplina che il progetto si e' gia' dato in 06 v4.94. E' l'unico contenuto aggiunto, ed e' anche il motivo per cui ov e lv non calano di byte. **(4) IL CONTRATTO FINALE SI CARICA:** da 2 clausole a 5 in cv (mancava del tutto quella d'ambito, che ov e lv avevano gia'), 4 in ov e lv. Ci vivono le invarianti che devono sparare a ogni turno — messaggio piu' recente, un comando per turno, load non e' play, cursore e save, scrivi lungo e in italiano.
  **COLLAUDO IMMEDIATO DEL GM — UN PERSO, E IL PIU' ISTRUTTIVO DI TUTTI.** Fine Toto-Rak: **nessuna opzione di viaggio nel footer**. Diagnosi: le due righe condizionali del footer — `🧭 Viaggio:` (tratta non banale in arrivo) e `⏭️ Tratto connettivo:` (run `[COND]` davanti) — **non sono mai state in cv**, in nessuna versione. Vivevano solo in 06 §B1 BEAT END, cioe' **dietro al RAG**, e il RAG non le ha pescate. Il costo e' asimmetrico e non si vede: un `🧭` omesso **cancella in silenzio `/viaggio`**, un `⏭️` omesso **cancella in silenzio `/riassumi`** — il GM non puo' scegliere un'opzione che non e' stata stampata. **FIX: `<beat_end>` diventa il FOOTER ORDER completo in quattro righe** (`⚔️ Rif. gruppo` → `[Info GM]` → `🧭` → `⏭️`), con dentro la definizione di tratta NON BANALE (05 Ch.8.4), le due opzioni canoniche del viaggio, la forma esatta della riga connettiva e le sue tre condizioni (N ≥ 2 · beat che avanza il cursore · [C] non ATTIVA). Piu' due nuovi `<checks>` contati. **Questa e' la prova diretta del §1.2**: cio' che deve sparare a OGNI beat non puo' vivere solo in un file di conoscenza — precedente identico a cv49, dove 06 perse per intero `NOTHING IS LEFT BEHIND` e il collaudo passo' lo stesso perche' la clausola era in cv. cv risale a **29.691 B**: il footer costa 2,5 KB ed e' la cosa giusta da pagare.
  **SECONDO COLLAUDO — DUE PERSI, ED ERANO DUE REGRESSIONI MIE, NON DIFETTI VECCHI.** **(1) LAHABREA E L'ECO SPARITI, E NEMMENO IN `Restano:`.** Il `Restano:` di fine parte 1 elencava solo «Boss finale Graffias; Salvataggio dell'Anziano Frixio»: i due pin non erano stati tagliati, **non erano mai stati dovuti**. Causa esatta: nella riscrittura di `NOTHING IS LEFT BEHIND` il passo (1) OWE e' passato da «the **08.1** pins» a «the **manifest** pins». Ho tolto il puntatore al file, e senza `08.1` il modello non apre niente: elenca cio' che ha gia' sotto gli occhi, cioe' il boss e l'uscita. **Non si puo' rinviare cio' che non si e' mai dovuto.** Ripristinato e irrobustito: OWE ora dice APRI IL MANIFEST 08.1 di questa duty e nomina i pin uno per uno, in ordine canonico, PRIMA degli scontri; piu' un `<checks>` contato («pin del manifest assenti sia dal testo sia dalla riga `Restano:`: 0»). **LEZIONE: un rimando reso generico e' un rimando cancellato** — «the manifest pins» e «the 08.1 pins» si leggono uguali a un umano e non lo sono affatto per il modello. **(2) `/tracker` non partiva se non forzato due volte.** Nel giro di pulizia dei marcatori avevo tolto il grassetto a `**EMIT 09 (Assets) §Z1 VERBATIM**`, che era l'unico segnale output-forcing della riga. Riscritta piu' forte in **tutti e tre i file, Loremonger e One-Shot inclusi**: «THIS COMMAND'S ENTIRE REPLY IS THE ARTIFACT, EMITTED ON THIS TURN» — niente preambolo, niente annuncio di cio' che si sta per costruire, niente roster incollato come testo, mai un secondo turno per produrlo davvero. Gli SCOPE per assistente restano i tre di sempre (ultimo beat · modulo intero, un tab per atto · ultimo scontro statato nella conversazione).
  **CONTROLLO SISTEMATICO DEI RIMANDI CONCRETI, fatto dopo aver capito la causa.** Diff vecchio-contro-nuovo su tutti i puntatori eseguibili dei tre file (`08.1`, `08.OST`, `05 Ch.x`, `07 Gn`, `0n_Nome`, `§Xn`): **un solo altro caso**, `08.1` sparito da ov — ma li' e' corretto che sparisca, perche' un one-shot ha scope libero e nessun manifest MSQ. Il vero difetto era che l'OWE di ov puntava a `08.1` **per copia da cv** e quindi non puntava a niente di reale. Sostituito con la fonte giusta per quell'assistente: **rileggi la voce di questo atto nell'indice degli Atti stampato da `/genera` (§C2/§C4)** e nomina gli oggetti dovuti uno per uno, il setup da pagare al climax (§E2) incluso; piu' il `<checks>` contato corrispondente. cv e lv: zero puntatori persi.
  **QUATTRO DERIVE TROVATE E CHIUSE.** (a) La regola dell'enigma chiudeva sulla **copertura `▒`/`▓`**, che e' una regola di MAPPA, in tutti e tre i file; spostata nella checklist mappa (in lv c'era gia' due volte). (b) `BUILD TO THE TARGET GdS` (Via A / Via B / riuso identico) esisteva in ov e lv e **mancava in cv**: allineato. (c) Le tabelle `HIGH-FREQUENCY BINDINGS` avevano membri diversi nei tre file senza ragione dichiarata (lv senza `Cristallo Madre`/`i Dodici`, ov senza `Guerriero della Luce`): ora un nucleo unico identico, con una riga di ambito per file. (d) In ov e lv il paragrafo sulle heading `###`/`####` dello stat block compariva **due volte nella stessa riga**.
  **SFOLTIMENTO, PASSATA FINALE — IL CRITERIO E' LA VISIBILITA' DEL GUASTO, NON LA LUNGHEZZA DELLA REGOLA.** Richiesta del GM: togliere tutto il togliibile «in maniera che i comandi funzionino sempre e prendano il resto dal RAG». La riga di taglio, applicata a ogni blocco: **se la regola manca, il GM se ne accorge?** Se SI', va in 06 e l'istruzione punta (il disegno della mappa, il layout dello stat block, il dettaglio di procedura di `/negozio`, `/cercano`, `/riprendi MSQ`, `/salva`, `/esito` — tutti guasti che si vedono a occhio, e infatti li hai gia' beccati tu nei collaudi). Se NO, resta nel control layer, quanto costa costa. **`<map>` scende da 2.510 a ~1.500 B** tenendo solo i tre guasti ciechi (bottom-to-top e la striscia d'ingresso, caselle = Taglia contate sulla griglia, copertura col suo numero e simbolo nominato dall'oggetto); presets, silhouette, vocabolario delle regioni e set simboli restano in §B8. **`<stat_block>` da 1.543 a ~850 B**: fuori il layout, dentro i tre guasti aritmetici, che sono silenti per misura (§1.1d: un boss a 52 PF invece di 59 non si legge come numero sbagliato, si legge come combattimento finito presto). Righe comando accorciate dove la procedura e' recuperabile con query lessicalmente ricche (`/negozio` compare sia nel messaggio del GM sia in §A22 — il caso in cui il RAG funziona), **intatte** dove la query non assomiglia a niente (`/continua`, LOAD, `/riassumi`, `/tracker`).
  **NUMERO PROMESSO E NUMERO OTTENUTO — la seconda volta che succede, e vale registrarlo.** Il piano puntava a **−50%** (71.9 KB → ~35 KB). Ottenuto, a valle di tutte le correzioni: **cv 31.087 → 29.127 B (−6%) · ov 21.866 → 22.166 B (+1%) · lv 18.945 → 20.081 B (+6%) · totale 71.898 → 71.374 B, cioe' PIATTO.** Il numero grezzo pero' mente in un verso preciso, e va detto: **questo audit ha AGGIUNTO tre cose che prima non c'erano** — il blocco `<checks>` in tutti e tre (~1,1 KB l'uno), il FOOTER completo in cv (~2,5 KB) e `NOTHING IS LEFT BEHIND` nel Loremonger, che non l'aveva mai avuto (~900 B). Sono ~6,7 KB di funzionalita' nuova. Il testo PREESISTENTE, riscritto, si e' quindi compresso di circa il **10%** complessivo e del **20%** su cv. **Onesto in chiaro: come operazione di riduzione questo audit e' fallito. Come operazione di ristrutturazione e di copertura, no.** La ragione per cui non si arriva a −50% resta quella misurata a cv48: **la prosa di giustificazione non era il grosso del file, le regole sono lunghe perche' dicono molto.** Il guadagno vero non e' il byte: e' la forma XML, lo zero priming, le condizioni contabili e il footer che finalmente esiste.
  **VERIFICATO MECCANICAMENTE, prima del collaudo:** zero rimandi `§` persi nei tre file (ov ne guadagna uno, §A6) · zero stringhe letterali italiane perse · zero template di link persi · roster comandi invariato · **34 blocchi condivisi byte-identici nei tre file** (§1.1c, verifica per stringa) · zero tag XML non chiusi · grep priming pulito. **DA COLLAUDARE** su Gemini 3.6 Flash Esteso (metro: il pacchetto Toto-Rak, §1.1d) e su Gemini 3.5 Flash-lite per il solo Loremonger.
- **v5.10 / cv49 / ov26 / lv20 — COLLAUDO TOTO-RAK (9 pagine): TRE VINTI NUOVI, E LA LEGENDA CAMBIA FORMA.** **VINTI.** La riga **`Restano:`** e' comparsa alla prima prova — «— Fine parte 1 (dungeon in corso) — Restano: Scena con Lahabrea, Scontro con Graffias (Boss Finale), Visione dell'Eco e Salvataggio di Frixio» — e il `/continua` successivo ha giocato ESATTAMENTE quei quattro elementi, in ordine. **L'aritmetica dei dadi e' tornata giusta:** Coeurl `PF 45 (6d10+12)` e Graffias `PF 60 (8d10+16)` verificano entrambi, dado vita coerente con la Taglia Grande; GdS 2 per il mid-boss e 4 per il boss su party Lv4, esattamente livello e livello-2. **ONE ROSTER INSTANCE = ONE ENCOUNTER ha tenuto:** i due Coeurl sono due scontri separati con l'interludio in mezzo, non un `(×2)`. Piu' i gia' acquisiti: `/continua` che apre col tag, Lahabrea prima del boss con l'Innesco preso dal pin, Eco, cinque blocchi per entrambi gli enigmi, gimmick canonico dei terminali (Confessione -> Riposo dello Stolto -> Camera dell'Abacinazione) con meccanismi gelmorriani idraulici e nessun magitek. **PERSI, e tutti e cinque sono stati corretti.** **(1) LA LEGENDA — richiesta del GM:** ogni simbolo ora si chiama con **l'oggetto che la prosa ha messo li'**, e l'effetto di gioco va fra parentesi — `▒ detriti di pietra crollati (mezza copertura, +2) · ≈ vasca d'acqua allagata (terreno difficile)`. Un `▒ mezza copertura (+2)` nudo e' la forma sbagliata: il GM non puo' descrivere ai giocatori una cosa che non ha nome. Aggiunto anche il verso opposto — **la legenda si scrive rileggendo la griglia**, perche' la mappa di Graffias elencava `▒` senza averne uno disegnato. **(2) LA FORMA VIENE DALLA PROSA:** un read-aloud che apriva su «una sala circolare allagata» e' stato disegnato `STANZA 12 × 10`, rettangolare. Il passo (1) del disegno ora comincia leggendo la parola di forma nella propria prosa, e due stanze dello stesso dungeon non sono lo stesso disegno (le due mappe dei Coeurl erano identiche a simboli scambiati). **(3) LA RIGA DELLE DISTANZE** stampava `dall'ingresso al primo raggio d'attacco = 4` — cioe' proprio il controesempio scritto nella regola. Riscritta con una lista chiusa di cosa la riga CONTIENE (aree telegrafate, portate non disegnate, salti) invece che di cosa non deve contenere. **(4) I NOMI DEL PIN SI USANO COME SCRITTI:** il pin dice 'unleashes the BANEMITE' e l'output ha scritto «colossale **diremite**» — errore di canone, verificato su ConsoleGamesWiki (Graffias e' un Banemite). Aggiunta a §B1 la stessa disciplina di §B2 sui nomi propri della spina. **(5) IL MARCATORE DI PARTE** era sopra il footer invece che sotto: chiarito nella clausola condivisa. **RESIDUO NON CORRETTO:** `Chele Affilate 8 (1d8+3)` fa 7 — una formula su sei, la regola c'e' ed e' contata in §A9.
  **BUG MIO, TROVATO E RIPARATO.** Nel refactor di §B12 il segnaposto `{NOTHINGLEFT}` cercava la PRIMA riga contenente 'NOTHING IS LEFT BEHIND' e ha pescato il RIMANDO dentro CHUNKING invece della regola: 06 e' rimasto con **due CHUNKING e zero NOTHING IS LEFT BEHIND**. Il collaudo ha funzionato lo stesso perche' la clausola vive anche in `cv`, che e' sempre in contesto — il RAG non e' servito. Ripristinata da cv, identica nei tre file. **E' la seconda volta che un mio controllo automatico pesca la prima occorrenza sbagliata** (la prima fu il falso negativo su Lahabrea, che cercava 'Graffias' e trovava l'`[Info GM]` di parte 1): il difetto e' il `first match` su una chiave che compare anche nei rimandi.
- **v5.09 / cv48 / ov25 / lv19 / 09 a1.00 — AUDIT SU MISURA DI GEMINI 3.6 FLASH.** Partito dalla documentazione ufficiale Google, che descrive due nostri difetti e ne spiega uno: «may **over-analyze verbose or overly complex prompt engineering** techniques used for older models» (06 era 354 KB con la regola media a 516 B e la piu' lunga a 1.899); «may **drop negative constraints** if they appear **too early** in the prompt» (Lahabrea pinnato e saltato, lo split ignorato); i blanket negatives che portano a «**fail to perform basic logic or arithmetic**» (06 aveva 1.270 negazioni — e noi un `6d10+18` stampato 45); «by default **less verbose**» (il tetto di ~16.500 caratteri, LEZIONE 2.30); «place your specific instructions **at the end**» (il fix di `/continua` ha funzionato solo sulla riga del comando). **Cinque interventi.** **(F1)** I 29,9 KB di HTML del tracker escono da §A24.1 e diventano **09_Assets.md §Z1**, byte-identici (sha verificato): un asset si copia, una regola si applica, e 30 KB di HTML non competono piu' con le regole a ogni recupero RAG. **(F3)** I marcatori `(binding)` passano da **412 a 6** in 06 — restano solo dove c'e' un self-check contato dietro — e sono azzerati anche in 05/07/08 e nelle tre istruzioni; il contenuto esplicativo dentro le parentesi e' conservato. **(F4)** La `ABSOLUTE RULE` in cima a 06 vietava le code fence «per qualunque contenuto» con la sola eccezione del tracker, mentre §B8 ne IMPONE una per la mappa tattica: riscritta in positivo, nomina entrambe le eccezioni. E poiche' Gemini 3 e' conciso di default, lo **steer di verbosita'** («WRITE LONG: THIS IS AN EXPANSIVE ASSISTANT… length is the product, concision is a failure mode») sale in cima a 06 ed entra identico nelle tre istruzioni. **(F2)** Riscritte da tesi a istruzione le cinque sezioni maggiori: **§B2** −27% · **§B1** −22% · **§B12** −13% · **§B8** −10% · **§B6** −9%. Esce l'argomentazione (RATIONALE, FAILURE SHAPE observed, le misure su N run, l'archeologia delle decisioni), che e' gia' qui e in Project_Memory; resta intero il contenuto normativo. **(F5)** Le tre istruzioni: clausola stat-block unificata e identica, mappa del Loremonger compattata, marcatori allineati. **DERIVA TROVATA:** cv/ov/lv dicevano «emit these SIX BLOCKS» elencandone CINQUE, e 06 §B12 diceva «the six blocks above» elencandone cinque, mentre il self-check di §A9 ne conta CINQUE — quattro file in disaccordo con se stessi dentro la stessa frase, sull'enigma che nei test collassava. Ora sono cinque ovunque. **06: 347.608 -> 299.265 B (-13,9%)**, 72 sezioni, zero rimandi morti, silhouette delle mappe e sei self-check contati diff-identici. **DA COLLAUDARE.**
  **NUMERO PROMESSO E NUMERO OTTENUTO, perche' resti agli atti:** il piano puntava al -55%, dedotto dalla lunghezza media delle regole assumendo che fossero lunghe PERCHE' argomentate. Misurata sul campo, la prosa di giustificazione era il **4%** del file: le regole sono lunghe soprattutto perche' dicono molto. §B8 rende il -10% con tabelle, silhouette, set chiuso dei simboli e self-check tutti conservati — e' la sezione, non un limite del lavoro. Arrivare a 160 KB avrebbe richiesto di **cancellare** ~110 KB di regole, non di comprimerle: il GM ha scelto di fermarsi alla riscrittura. Il guadagno vero di questo audit non e' comunque il byte, sono i **412 -> 6** e la verbosita' dichiarata.
- **v5.08 / cv47 / ov24 — NIENTE RESTA INDIETRO: il taglio invisibile diventa un debito dichiarato.** Il GM ha scelto esplicitamente la precisione sul numero di messaggi («se devo fare un paio di /continua in più ma avere più precisione non mi turba»). Il tetto di output (LEZIONE 2.30) restava un editor silenzioso: `SPLIT, NEVER SHRINK` diceva di spezzare, ma **CHUNKING diceva «il minor numero di parti possibile»** — due regole in tiro opposto, e il modello risolveva assottigliando, che non viola letteralmente nessuna delle due (LEZIONE 2.31). **Tre modifiche, nessuna nuova proibizione.** (1) **CHUNKING declassato a spareggio:** «il minor numero» decide SOLO fra disposizioni che rendono tutto a piena ricchezza, e nel momento in cui una parte andrebbe assottigliata la disposizione giusta è una parte IN PIÙ. (2) **§B12 `NOTHING IS LEFT BEHIND` — la FORMA in quattro passi** (LEZIONE 2.26: non un sesto «mai», una forma): **OWE** — prima di scrivere, nominare gli oggetti dovuti dal beat (pin 08.1, ogni scontro, ogni interludio/enigma, la scena di chiusura); **WRITE WHOLE** — si interrompe SOLO dopo un oggetto completo, mai dentro, e un oggetto che verrebbe solo sottile è un oggetto della PROSSIMA parte; **DECLARE** — se resta qualcosa, la risposta chiude col marcatore e la riga `Restano: <oggetti non scritti>`; **RESUME FIRST** — il comando di gioco successivo apre sul primo elemento di `Restano`, che batte l'avanzamento del cursore. (3) **§A9 diventa SEI controlli contati:** il residuo è zero, oppure è dichiarato. Clausola **identica parola per parola** in 06/cv/ov (§1.1c), 1.374 B; agganciata alle righe di comando dove si esegue — `/continua` in cv, `/atto` in ov (co-locazione marcatore/regola, LEZIONE 2.13). **Perché funziona dove cinque «non condensare» hanno fallito:** l'impalcatura è imposta da self-check e la finzione no, quindi quando il budget stringe cede sempre la finzione — `Restano:` è la prima cosa che rende il taglio CONTABILE. **DA COLLAUDARE.**

- **v5.07 / cv46 / ov23 / lv18 — IL COLLAUDO VINCE TRE, PERDE DUE.** Primo test dopo il blocco di fix.
  **VINTI, e due erano aperti da giorni.** **Lahabrea compare PRIMA del boss per la prima volta in sette run** — si nomina («*Io sono Lahabrea, servitore dell'unico vero dio*»), risveglia la creatura e **l'`Innesco:` viene dal pin invece che inventato**, come impone la regola. **La visione dell'Eco è tornata.** **Entrambi gli enigmi hanno i cinque blocchi** (era 1 su 2): l'auto-controllo aggiunto a §B12 ha tenuto dove la sola forma aveva ceduto. E **il Coeurl è Grande**, coerente col suo «colossale bulbo vegetale».
  **NOTA DI METODO: il mio check automatico ha dato un FALSO NEGATIVO su Lahabrea** — cercava la prima occorrenza di «Graffias», che compare nell'`[Info GM]` di parte 1 molto prima del boss. Il difetto era nella misura, non nell'output. **Un controllo automatico va verificato sull'output vero prima di credergli.**
  **PERSO 1 — `/continua` risponde ancora con l'orientamento.** Ma non è una ricarica letterale: è una **PARAFRASI** del blocco di load, stessi fatti parole diverse. Quindi il modello non sta ri-agganciando il blocco `=== SAVE ===`, sta **ri-orientando** perché nulla lo obbliga ad aprire il beat. `cv` conteneva già QUATTRO enunciati corretti (righe 7, 60, 65, 83), uno dei quali dice testualmente «*The ONLY turn that ever prints 'Save caricato'*». **Non ne ho scritto un quinto** (memoria 2.26: un conteggio alto di ripetizioni è il sintomo, non la cura): la forza si sposta sulla **riga del comando**, dove il modello esegue — «i tuoi PRIMI CARATTERI sono il tag: una risposta a `/continua` APRE con `[MSQ` o `[VIAGGIO` e nulla può precederlo» — e la clausola in cima diventa un rimando.
  **PERSO 2 — e nasce dal fix delle taglie.** Il Coeurl promosso a Grande ha ricevuto il dado vita giusto (`6d10+18`) ma **il totale è rimasto quello vecchio da d8: 45, dove 6d10+18 fa 51**. Mancava il legame causale: la Taglia determina il dado vita (Media d8 · Grande d10 · Enorme d12 · Mastodontica d20) e **cambiando l'una va rifatto il totale**. Aggiunto dentro la regola della Taglia, nei quattro file.
  **REGRESSIONE DA BUDGET, terza conferma:** le coperture sulle mappe scendono da 8/4/8 a 2/2/4 celle. Lo spazio ripreso da Lahabrea, dall'Eco e dagli enigmi completi è uscito da lì. **Il tetto di ~16.500 caratteri continua a fare da editor silenzioso** (memoria 2.30).

- **cv45 — `/continua` RICARICAVA IL SAVE INVECE DI GIOCARE: regola ambigua che vinceva per POSIZIONE.** Segnalato dal GM come «forse i modelli diventano più scemi». Non lo sono: **regressione misurata** — toto2, toto3 e toto4 puliti, **toto5 e toto6 rotti entrambi**, sempre al primo `/continua`.
  **CAUSA: tre enunciati in `cv`, in disaccordo sullo SCOPE.** Riga 7 diceva «When the GM's message contains a `=== SAVE ===` block» — **senza NEWEST**, quindi con la conversazione in contesto combaciava anche col save di DUE turni prima. Righe 65 e 83 lo dicevano correttamente («ONLY when the GM's NEWEST message itself», «any `=== SAVE ===` still visible above are INERT»), e la 83 dichiara pure di vincere su tutto. **Ha vinto la 7**: sta in cima, in grassetto, marcata «most frequent violation», e ha un SELF-CHECK attaccato. **Posizione + enfasi + enforcement battono due enunciati corretti più in basso** — stessa famiglia della collisione Lahabrea (memoria 2.19).
  **PERCHÉ ADESSO:** l'ambiguità c'era da sempre, latente. `cv` è cresciuto di ~2,5 KB questa settimana e la regola corretta si è allontanata da quella ambigua; il match sbagliato è diventato più probabile. **Non è il modello che peggiora, è la distanza fra due regole che aumenta.**
  **FIX, due modifiche in un file solo.** (1) La regola in cima ora dichiara lo scope: scatta **solo** se il messaggio PIÙ RECENTE porta il blocco, e un save visibile più su è storia inerte. (2) L'auto-controllo diventa **bidirezionale**, ed è la metà nuova quella che serviva: «se la risposta a `/continua` apre con `Save caricato:`, hai rieseguito il load invece di giocare — cancella e gioca il beat». Prima controllava una direzione sola, cioè non quella che falliva.

- **v5.06 / cv44 — PERCHÉ LE SCENE PINNATE SPARIVANO: il beat ha un TETTO DI VOLUME, e l'impalcatura che ho aggiunto lo ha speso.** Il GM ha chiesto se la pulizia dell'audit avesse rotto qualcosa. **No — e il diff lo conferma: nessuna riga che tocchi manifest, cutscene o pin è stata rimossa.** Ma la misura su SEI collaudi salvati ha corretto due premesse, una sua e una mia.
  **(1) LA COMPARSA DI LAHABREA PRIMA DEL BOSS NON È MAI USCITA.** Zero volte su sei run, prima e dopo ogni fix. Il rimedio scritto due giorni fa **non è mai stato validato su un beat completo** — l'unico test successivo copriva solo la parte 1. «Prima funzionava» era vero per la VISIONE DELL'ECO, non per la comparsa.
  **(2) LA REGRESSIONE DELL'ECO È REALE, ED È CAUSATA DAL MIO LAVORO — ma non dalla pulizia.** Misurato: **il volume totale di un beat è di fatto COSTANTE, ~16.500 caratteri in tutti i test.** Dentro quel tetto, in una settimana la mappa è cresciuta da 462 a 832 caratteri (**+80%**) e i blocchi enigma da 2.015 a 2.988 (**+48%**). Nello stesso passaggio la **prosa narrativa cala di 967 caratteri** — quasi esattamente quanto è cresciuto il resto — e con lei se ne va la visione dell'Eco pinnata. Il collaudo successivo mostra lo stesso meccanismo al contrario: la prosa si riprende e a cedere è l'enigma, che perde `Soluzione` e `Indizi`. **Il modello bilancia un budget fisso lasciando cadere ciò che è meno controllato: l'impalcatura ha auto-controlli, la finzione no.**
  **IL RIMEDIO, e corregge un difetto del lavoro di stamattina.** §A9 aveva guadagnato il CONTEGGIO dei pin, ma **senza una via d'uscita un controllo che fallisce è solo un allarme**. Ora `SPLIT, NEVER SHRINK` (§B12) mette le **scene pinnate nella lista protetta** e dichiara il rimedio: se i pin non stanno insieme a mappe, stat block e interludi, **si SPEZZA il beat — non si lascia fuori un pin in silenzio**, e il pin viaggia nella parte successiva alla sua posizione canonica. Con la motivazione misurata scritta dentro la regola, così non venga ristretta di nuovo. Clausola gemella in `cv`, dove lo strato sempre in contesto la fa scattare.
  **LEZIONE GENERALE (Project_Memory 2.30): ogni regola che aggiunge impalcatura OBBLIGATORIA spende un tetto condiviso.** Il costo non si vede nella regola che si scrive, si vede in ciò che sparisce altrove — e sparisce sempre la stessa cosa: il contenuto che nessun conteggio protegge.

- **v5.05 / cv43 / ov22 / lv17 — CORREZIONE ALLA VOCE SOTTO, SULLE TAGLIE: via la tassonomia, resta la coerenza.** La regola bestia/umanoide che avevo scritto era **sbagliata**: FFXIV è pieno di boss di forma umanoide tutt'altro che Medi (Susano, Ravana, Zodiark, un Prime Ascian), quindi quella categoria sarebbe diventata una lista di eccezioni al primo contatto col contenuto reale. Su indicazione del GM la tassonomia è **rimossa**: la Taglia si LEGGE dal corpo reale della creatura come già si fa per il suo aspetto (§A5, §B10), e l'unico vincolo binding è la **coerenza interna** — Taglia e `Descrizione visiva` nello stesso blocco devono descrivere la stessa creatura. «Colossale bulbo vegetale» + Media si smentisce da solo, non richiede nessuna categoria per essere visto, ed è corretto anche per i casi a cui nessuno ha ancora pensato. **Una regola che ha bisogno di un sistema di categorie va manutenuta; una regola di coerenza si mantiene da sola.**

- **v5.04 / cv42 / ov21 / lv16 — CINQUE DIFETTI, UNA CAUSA SOLA: le regole c'erano, mancava il CONTEGGIO che le verifica.** Collaudo Toto-Rak. **YAGNI non si applicava** (nessun difetto era speculativo: tutti osservati), ma il principio di causa-radice sì — cinque difetti non volevano cinque regole.
  **LA RADICE.** Lahabrea assente (**seconda volta**, e stavolta con lui è sparita anche la visione dell'Eco), il secondo enigma tornato alla forma vietata, la taglia dei mid-boss, il preset della mappa in contrasto con la prosa, un errore aritmetico: **quattro su cinque avevano già la loro regola**, scritta e binding. Ciò che mancava era l'**enforcement**. La prova sta dentro lo stesso beat: **l'enigma 1 è perfetto** — cinque blocchi, tre azioni distinte, tutti e sette gli oggetti della soluzione presenti nel testo letto ai PG — **e l'enigma 2 non ha né `Soluzione (GM)` né `Indizi`**, con la `CD Facile` che compie l'obiettivo. Stessa spec, stesso turno, esiti opposti. **La differenza fra la mappa e l'enigma era una sola: la mappa ha un auto-controllo contabile, l'enigma no** — ed è per questo che i fix della mappa hanno tenuto tutti (ingresso in basso, nemico in profondità, due porte, coperture 8/4/8 celle, Graffias 4 caselle).
  **IL RIMEDIO, in un punto solo: §A9 era già il «fast pre-output scan»** e viene esteso invece di inventare un meccanismo nuovo. Cinque voci **contabili** — una lista da spuntare o una somma da rifare, mai un'impressione: (1) i pin del manifest 08.1 spuntati uno per uno; (2) i cinque blocchi di ogni enigma e nessuna soglia che conclude; (3) Taglia contro corpo descritto; (4) preset della mappa contro la prosa; (5) ogni `n (XdY+Z)` ricalcolato.
  **TAGLIE — e la regola richiesta andava corretta prima di scriverla.** «Boss sempre ≥ Grande» sarebbe **falso**: Lahabrea, Thordan, un ufficiale garleano sono umanoidi Medi nel canone, e gonfiarli sarebbe un difetto nuovo. La regola vera è duplice: **un mid-boss/boss BESTIA-MOSTRO è Grande o più** (Media è per la truppa, e un boss Medio sulla mappa è **UNA casella**, il che rende inutile il sistema di ingombro), **un boss UMANOIDE tiene la sua taglia canonica**, e **in ogni caso la Taglia non può contraddire la propria `Descrizione visiva`**. Failure shape osservato: «Coeurl a Nove Code — **Media**» la cui riga visiva diceva «un **colossale** bulbo vegetale».
  **DIFETTO NUOVO, non segnalato:** il read-aloud del boss diceva «la grande sala **circolare**» e la mappa era `SALA (16 × 12)`, **rettangolare** — la regola «la forma si legge, non si indovina» violata. Condizione aggiunta all'auto-controllo della griglia.
  **ARITMETICA:** `7 (1d8+2)` vale **6**. Tutto il resto tornava (PF 45 = 6d8+18, PF 95 = 10d10+40, coni e TS corretti, nessun dado inesistente).
  **LORE: nessun difetto.** Il gimmick dei terminali segue il lock di 08 (Confessione → Riposo dello Stolto → Abacinazione) e il Coeurl come **pianta** è giusto — il pin dice «an OCHU/plant despite the name».
  **ISTRUZIONI: solo la clausola taglia**, identica parola per parola nei tre file, messa dove la Taglia si scrive davvero (la riga dello stat block). Le altre quattro voci restano in §A9: sono controlli di fine beat, non regole di composizione.

- **v5.03 / 08 v3.41 — VIA LE LAPIDI, e la convenzione di lingua rimessa a posto.** Due domande del GM, entrambe fondate.
  **(1) LE SEZIONI «RITIRATA» ERANO PESO MORTO AUTO-REFERENZIALE.** Misurato: §B7, §C3, §D2 e §D6 avevano **zero citazioni**; §B9 ne aveva due, ed **entrambe venivano dalle altre lapidi**. Si citavano fra loro e nessun altro le citava. La giustificazione originale («conservare il numero per non rompere i riferimenti») era una **premessa falsa**: nessuno aveva proposto di rinumerare, e cancellare una sezione lascia semplicemente un buco nella numerazione — `§A2` lo dimostrava già da tempo, cancellata per intero e senza conseguenze. **Il costo era reale**: ogni lapide è un chunk RAG recuperabile, che descrive un comportamento rimosso — la forma della LEZIONE 2.9. Il beneficio, cioè la storia, lo dà già `CHANGELOG.md`, **che è dev-only e non viene caricato**. Cinque sezioni cancellate: 06 passa da **77 a 72 sezioni §**. **Effetto collaterale intercettato dalla verifica:** cancellare la lapide di §D6 ha orfanato **§D8**, che quella lapide era l'unica a nominare — puntatore aggiunto da §A4, dove nasce la confusione fra «cerca un'immagine che esiste» e «genera un'immagine che non esiste».
  **(2) LA LINGUA: la convenzione c'era già, ero io a derivare.** §1.4 impone che istruzioni e knowledge siano in INGLESE e che solo OUTPUT e parole di comando restino in italiano — e le lapidi le avevo scritte in italiano. Ma la stessa §1.4 avverte di **NON tradurre il corpus**, e la misura le dà ragione: la deriva era minuscola — **05 zero righe, 07 una, 06 quattro, 08 tre**. Delle otto, cinque sono **legittime** (gli esemplari di prosa di §A1 SONO output e devono restare italiani; i nomi di luogo citati dentro regole inglesi; la binding anti-doppione di 07). I veri sconfinamenti erano **tre righe di prosa di regola in 08** (`MARCATORI DI CONDENSAZIONE`, `MARCATORE [CUT]`, `TAGLIATA`), ora in inglese con marcatori ed etichette invariati. **Zero violazioni residue.**
  **VERIFICA:** 72 sezioni §, **zero orfane**, zero rimandi a sezioni inesistenti, nessuna lapide residua, nessuna riga > 2000 char. **L'invariante di verifica cambia da 77 a 72** — chi riesegue lo script dopo questa passata deve usare il numero nuovo.

- **v5.02 — AUDIT «REGOLE SENZA FORMA»: una radice, tre ritiri, sei orfane richiamate — e DUE findings su cinque cancellati dalla misura.** Passata su 05-08 (01-04 esclusi: dati puri). **Misurato prima di progettare**, e la misura ha subito ristretto il campo: righe sopra i 1400 char 1 in 05, **15 in 06**, 0 in 07 e 08; orfane e rimandi morti solo in 06. **06 ERA l'audit**, e dirlo subito ha evitato di spendere metà del lavoro dove non c'era.
  **LA RADICE (il finding che vale l'intera passata): la regola «il tiro dà INFORMAZIONE, mai l'esito» era stata derivata TRE volte in modo indipendente** — §B20 per i ganci («un tiro migliore = lore più ricca, MAI l'Aggancio»), §E5 per i misteri, §B12/§E1 per gli enigmi — **e mancava in §A18, il blocco da cui passano tutte e tre.** Il template di §A18 è una scala di RISULTATI (`[base result / what it gets]`), ed è quello che il modello copia. **Il fix di ieri sull'enigma era una patch su un chiamante, non sulla radice.** Ora §A18 pone la domanda una volta sola — *c'è un esito che i giocatori devono raggiungere da sé?* — con il test in una frase («rileggi il gradino più alto: questo conclude la cosa?») e con le tre specializzazioni NOMINATE perché non vengano reinventate una quarta volta. **Nota su §B20: aveva la forma giusta dall'inizio** — l'Aggancio in un blocco proprio fuori dalla scala — cioè esattamente ciò che `Enigma per i PG` ha reinventato ieri.
  **DIECI SEZIONI ORFANE (nessuno le citava, quindi il RAG le pescava solo per caso).** Tre RITIRATE, numero conservato come §B9: **§B7** (anteprima incontro, superata dal pacchetto §B1 e dal tracker §A24), **§C3** (copia parziale di §A5/§A6/§A14+07 — una copia parziale di una regola generale è un posto in più da cui può divergere), **§D2** («genera direttamente», non conteneva una regola). Sei RICHIAMATE con un puntatore dal punto in cui la regola morde davvero: §A11 da §B6 (dove il conflitto homebrew/RAW conta), §A15 da §A14, §B16 da §B8 (uno scontro è l'unico momento in cui il Limit Break serve), §B18 da §B2, §C8 e §C9 da §C4. **Criterio dichiarato: corto ≠ stub** — §C8 dà un formato completo in 53 caratteri ed è ottimo così; il criterio è l'orfananza.
  **DUE CORREZIONI PUNTUALI:** `§A2` era citato da due lapidi ma **non esiste** (rimando morto, tolto); §C5 prometteva **«12 common structures» che non erano elencate da nessuna parte** — insieme fantasma, sostituito da ciò che è davvero azionabile.
  **DUE FINDINGS CANCELLATI DALLA MISURA, ed è il risultato più utile dopo la radice.** (1) I sei **cluster di duplicazione NON divergono**: `boss = party level` e `mid-boss = level -2` concordano ovunque, le soglie sono 10/15/20 in tutti i punti, la casella è `1,5 m` in tutti e tre. Consolidarli avrebbe significato rifattorizzare il macchinario di cursore e salvataggi — la parte più delicata — per un problema inesistente. (2) Le **quindici righe sopra i 1400 char sono quasi tutte UNA regola** con motivazione e failure shape inline: spezzarle separerebbe la regola dal suo perché. **Le metriche scartate a monte** (198 «divieti senza esempio», comandi in negativo) erano le stesse trappole già smontate dall'audit F3 e dalle passate precedenti.
  **VERIFICA (ripetibile — è lo stesso script che ha prodotto il piano):** 77 sezioni §, **zero orfane** salvo le quattro lapidi, **zero rimandi a sezioni inesistenti**, nessuna riga > 2000 char, clausole condivise ancora identiche fra cv/ov/lv. **Criterio al tavolo, controintuitivo e voluto: un beat deve uscire IDENTICO a prima.** Questa passata toglie peso e ambiguità; se cambia un output visibile, si è rotto qualcosa.

- **v5.01 / cv41 / ov20 / lv15 — via la riga `Obiettivo:`, e le due coperture smettono di scambiarsi.** Due rilievi del GM sul collaudo v5.00. **(1) `Obiettivo:` diceva l'ovvio** («attivare il terminale per sbloccare la porta») — se `Enigma per i PG` ha fatto il suo lavoro, cosa si sta cercando di fare è già evidente, e una riga che lo ripete è testo che il GM legge per niente. La catena passa da SEI blocchi a **CINQUE**; §E1 principio 6 (obiettivo trasparente) resta soddisfatto dalla descrizione invece che da un'etichetta. **(2) `▓` usato per la mezza copertura**, che vale `▒`, e in una mappa la chiave non diceva affatto che copertura fosse. Lo scambio **raddoppia il bonus in silenzio** (+5 invece di +2). Tre rimedi, tutti strutturali: `▒` è dichiarato **la copertura predefinita** e `▓` l'eccezione che richiede una ragione; **la chiave porta SEMPRE il numero** (`mezza copertura (+2)`), mai un generico «copertura», perché è il numero che il GM applica ed è anche ciò che rende visibile lo scambio — «+2» accanto a `▓` si vede che è sbagliato, un blocco senza etichetta no; e l'auto-controllo verifica che **simbolo e bonus corrispondano**. Clausola identica parola per parola nei tre file (1.165 B).

- **v5.00 / cv40 / ov19 / lv14 — L'ENIGMA TORNA RISOLVIBILE DAI GIOCATORI: il blocco `Enigma per i PG`.** Il GM ha enunciato il principio giusto: un enigma si risolve ragionando sulla descrizione, **senza tirare**; le prove danno indizi, e al più la CD Difficile può dare quasi tutta la soluzione.
  **TRE DIFETTI MISURATI SULL'OUTPUT.** (1) **La soluzione usava un oggetto che i giocatori non avevano mai visto:** `Soluzione:` diceva «versando la linfa reattiva **delle radici vicine**», mentre il read-aloud nominava solo un portale, un pilastro con canali disseccati e un cristallo spento. **Le radici non c'erano.** L'enigma non era difficile da dedurre: era *impossibile*. (2) **Soglie invertite:** `CD Facile (10)` dava «il canale principale e il metodo per far scorrere l'etere», cioè la soluzione al gradino più basso, mentre `CD Difficile (20)` dava colore sulle condotte successive. (3) **«Minimo 3 soluzioni» degradato in «3 abilità con cui tirare»:** Arcana, Natura e Indagare sono tre modi di tirare per l'unica soluzione esistente.
  **LA DIAGNOSI, ed è il risultato più utile della passata: la regola giusta era già scritta in CINQUE punti binding** — §E1 principio 1, §E1 `PUZZLE != CHECK BLOCK`, le note di §A18, §B12 `TANGIBLE-PUZZLE SALIENCE`, e §B12 `SOLUTION LINE` che descriveva perfino la forma corretta. **Cinque enunciati, e l'output li violava tutti.** Quando una regola è ripetuta cinque volte e continua a perdere, **il problema non è che manchi: è che nessuno dà una FORMA al comportamento giusto.** Tutti e cinque erano principi o divieti; l'unica cosa con un template concreto era §A18, e infatti usciva il template di §A18 — comprese le sue etichette di slot, che sono una scala di RISULTATI (`CD Facile (10): [base result / what it gets]`). Applicata a un enigma, «what it gets» **è** «il dado risolve». Terza conferma della lezione 2.21.
  **E UNA CONTRADDIZIONE INTERNA che spiega perché la soluzione è DIVIDERE e non allungare:** §B12 `SOLUTION LINE` imponeva che il read-aloud fosse di **«1-3 frasi»** e insieme che presentasse l'ostacolo «COME LO VEDONO I GIOCATORI», da cui dedurre la soluzione. Richieste incompatibili, e vinceva il tetto di lunghezza perché era quello concreto.
  **LA FORMA NUOVA, sei blocchi:** `Da leggere ai PG:` (l'arrivo, 1-3 frasi) → **`Enigma per i PG:`** (letto ad alta voce, **senza tetto di lunghezza**, cosa vedono fisicamente) → `Obiettivo:` (una riga, §E1 principio 6) → `Soluzione (GM):` + **tre AZIONI diverse** → `Indizi:` → `Fallimento:`. Nome del blocco scelto dal GM.
  **DUE CONDIZIONI CONTABILI la reggono.** (a) **Ogni oggetto fisico nominato in `Soluzione (GM)` compare anche in `Enigma per i PG`** — è la stessa disciplina della mappa vista dall'altro lato: là la mappa disegna ciò che la prosa nomina, qui la prosa nomina ciò che la soluzione userà. (b) **Nessuna soglia può compiere l'obiettivo** — si rilegge ogni gradino e ci si chiede «qui la porta si apre?»; l'ostacolo cede quando i giocatori METTONO IN ATTO la soluzione, mai perché un dado è uscito alto.
  **§A18 INDICA ORA DOVE STA L'ALTRA FORMA.** Le sue note dicevano solo che i tiri non risolvono un enigma: **un divieto senza alternativa lascia il modello sul template che ha sotto gli occhi.** Ora nomina i sei blocchi di §B12. Stesso rimedio di co-locazione già usato per il «NOTHING ELSE» del pacchetto incontro. §E1 e §D5 collegati alla stessa forma; §E1 chiarisce che **l'indizio gratuito È `Enigma per i PG` stesso**.
  **ISTRUZIONI: clausola CORTA (1.040 B) e identica parola per parola nei tre file.** Non l'intera spec come per la mappa: là il difetto era una selva di dettagli, qui è **uno e strutturale**, quindi bastano i due blocchi e le due condizioni.
  **VERIFICA:** 77 sezioni §, nessuna riga sopra i 2000 char, nessun residuo del tetto «1-3 frasi» sull'enigma, clausola identica nei tre file. **Numeri da battere:** oggetti della `Soluzione` assenti dal testo letto ai PG **1 su 1 → 0**; soglie che compiono l'obiettivo **CD 10 → nessuna**; vie realmente distinte **1 → ≥3**; blocco `Enigma per i PG` **assente → presente in ogni interludio**.

- **v4.99 / cv39 / ov18 / lv13 — SANITY CHECK PRIMA DEL COMMIT, `/schema` RITIRATO, E IL LOREMONGER ENTRA NELLA STESSA SPEC.** Passata di controllo su §B8 letta per intero contro le best practice per il pavimento. **Quattro difetti reali, più una deriva che avevo introdotto io.**
  **(1) L'AUTO-CONTROLLO ERA A 1959 CARATTERI SU 2000, con 16 condizioni in una riga sola** — la riga che fa rispettare tutto il resto, a 41 caratteri dal rompersi, e con un taglio di chunk che ne avrebbe fatte sparire metà (LEZIONE 2.13). **Diviso in due unità recuperabili** che ripetono ciascuna il proprio innesco: `SELF-CHECK 1 of 2 — THE GRID ITSELF` (971 B: geometria, cornice, aperture, orientamento) e `SELF-CHECK 2 of 2 — WHAT IS ON THE GRID` (1285 B: prosa, overlay, spaziatura, nemici, ingombri). **§B8 non ha più nessuna riga sopra i 1400 caratteri** — margine di crescita recuperato.
  **(2) CO-LOCAZIONE: «il nemico sta nella metà lontana» usava il concetto di INGRESSO, definito quindici regole più in basso.** Recuperata da sola quella regola non sapeva dove fosse l'ingresso, quindi «metà lontana» non significava niente. L'orientamento è ora ripetuto **dentro** la regola che lo usa, con la ragione dichiarata.
  **(3) ORDINE: la tabella delle regioni compariva PRIMA della regola che dice che la sorgente è la prosa** — cioè, strutturalmente, la stessa inversione appena corretta nel testo: chi legge (e chi recupera un chunk) incontrava il menù prima di sapere che non è un menù. Aggiunto il puntatore in testa alla regola OVERLAY: risponde solo al DOVE, il COSA viene dal read-aloud.
  **(4) AMBIGUITÀ: «le due righe vicine all'ingresso restano libere» — libere da cosa?** Nel collaudo una fascia di `≈` a tutta larghezza copriva proprio l'ingresso. Disambiguato: **nessun nemico e non interamente coperte da un pericolo**, perché quella striscia è dove il GM appoggia i PG che la mappa non disegna.
  **(5) DERIVA MIA, trovata dal confronto fra i file:** 06 era passata a `Grande, 4 caselle` (una cifra sola) mentre cv e ov dicevano ancora `Grande 2×2 = 4 caselle`. Allineate.
  **`/schema` RIMOSSO E §D6 RITIRATA.** Il Loremonger aveva `/schema <luogo>` → §D6, che era **uno stub di due righe senza specifica** («schema testuale o prompt per generarla»). Avere un secondo formato di mappa, definito peggio e in un altro punto, era esattamente il modo di far uscire due mappe diverse dallo stesso progetto. §D6 resta un numero vuoto con il puntatore a §B8 — **come §A2 e §B9**, perché rinumerare §D7-§D8 romperebbe i riferimenti.
  **IL LOREMONGER USA ORA LA STESSA SPEC (decisione del GM: anche lui costruisce scontri in chat).** Nuova riga `A FIGHT COMES WITH ITS MAP` (2.912 B), con **le clausole condivise verbatim** rispetto a cv/ov (§1.1c) e le sole differenze imposte dal mestiere: «la prosa che hai appena scritto» invece del blocco 'Da leggere ai PG', «il luogo prosegue» invece di «il beat», e **un `/blocco` isolato senza scontro attorno NON prende la mappa**. `lv` passa da 12.883 a 16.017 B: +24% sul file più snello, che gira sul pavimento più basso del progetto (Haiku 4.5 / Gemini 3.5 Flash-lite) — costo accettato perché su quei modelli lo strato sempre in contesto conta PIÙ del recupero, non meno.
  **VERIFICA:** 77 sezioni §, nessuna riga sopra i 2000 char in 06, ogni regola di §B8 nella forma canonica, cv e ov identiche parola per parola, otto clausole condivise verbatim in tutti e tre i file, `/schema` assente ovunque.

- **v4.98 — GLI APPUNTI DI LAVORO USCIVANO INSIEME ALLA MAPPA.** Il GM ha chiesto se tre cose stampate al tavolo servissero a lui o a me: l'intestazione `— ENCLOSED, walls included, floor 10 across`, la forma `Grande, 2×2 = 4 caselle`, e la riga `In caselle: dall'ingresso al boss 4 · dal boss al terminale 3`. Domanda giusta, e le tre si risolvono in modo diverso — ed è il motivo per cui vale la pena scriverlo.
  **(1) INTESTAZIONE — difetto strutturale mio, tagliata.** Avevo messo metadati di verifica **dentro un blocco verbatim**, cioè dentro un blocco il cui unico contratto è «riproducilo esattamente»: **tutto ciò che ci scrivo è output, non documentazione**. Un commento rivolto al modello non ha modo di distinguersi una volta che la regola dice di copiare carattere per carattere. Le informazioni ENCLOSED/OPEN si sono spostate nella regola ATTORNO al fence, dove informano senza spedire, e nell'intestazione resta solo nome e misura — che è tutto ciò contro cui l'auto-controllo deve contare.
  **(2) INGOMBRO — non tagliato, ridotto da tre affermazioni a una.** `Enorme, 3×3 = 9 caselle` dice la stessa cosa tre volte; resta `Enorme, 9 caselle`. Il totale supera la soglia per due motivi indipendenti: è ciò che §B6 intende quando rende la Taglia obbligatoria perché «al GM serve l'ingombro sul tabellone» mentre ricopia, ed è l'ancora del conteggio che ha corretto il bug dell'ingombro in v4.94.
  **(3) RIGA DELLE DISTANZE — difesa, ma stava misurando la cosa sbagliata, e la colpa è del MIO esempio.** Non è impalcatura: esiste perché il GM abbia in caselle ciò che sulla griglia **non c'è**, cioè le aree telegrafate del boss. Ma l'esempio che la regola portava apriva con «dalla porta al boss 6», e l'output ha imparato da lì a misurare distanze fra due cose entrambe già disegnate — un numero che il GM ottiene contando quattro quadretti col dito. Regola riscritta come **converti ciò che non è disegnato, mai misurare ciò che lo è**, esempio ripulito.
  **LA REGOLA GENERALE, ora scritta in §B8:** una cifra si stampa se serve a chi legge, non se è servita a me per verificarmi. **La ridondanza che aiuta chi scrive resta disordine per chi legge.**
  **TERZA CONFERMA che un ESEMPIO è una regola di fatto** (memoria 2.21): `LATO` = «riparo lungo una parete» → copertura a muro 8 volte su 8; «riproducila e poi collocaci GLI ATTORI» → attori e nient'altro; «dalla porta al boss 6» → distanze già visibili. Da adesso è l'aspettativa predefinita, non una curiosità: **la prosa di una regola si legge, l'esempio si copia.**

- **v4.97 / cv38 / ov17 — LA MAPPA HA UN VERSO, E IL NEMICO NON STA SULLA PORTA.** Due osservazioni del GM sul collaudo v4.96 (Flash liscio, primo pezzo soltanto per risparmiare token). Entrambe confermate dalla misura, e la seconda era più marcata di quanto sembrasse: `STANZA` boss a **3 righe** dalla porta in alto, `CORRIDOIO` boss a **2 righe** su quattordici disponibili.
  **L'ORIENTAMENTO NON ERA DEFINITO DA NESSUNA PARTE — ed è il punto interessante.** La regola delle due aperture diceva già «una da cui il gruppo entra, una da cui il dungeon prosegue», ma **non diceva quale delle due fosse quale sulla griglia**. Con la scelta libera il modello ha imboccato sempre la stessa: entrata in alto, in tutte le mappe di tutti i collaudi. Un grado di libertà non vincolato non produce varietà, produce **una costante arbitraria** — e questa metteva i nemici fra il gruppo e la porta da cui era appena passato. Ora: **si entra dal BASSO e si avanza verso l'ALTO**, anche sui preset aperti senza porte. Motivazione scritta nella regola perché regga: il GM appoggia la mappa rivolta ai giocatori, quindi «avanti» è lontano da lui e in su nella pagina, e più si scende nella griglia più si è in profondità nel dungeon.
  **IL NEMICO STA IN PROFONDITÀ, e la regola rende finalmente azionabile una che c'era già.** Tre motivi, e il primo è quello che conta: **la mappa non disegna i PG di proposito**, quindi un boss piazzato sulla porta lascia il GM senza un posto dove metterli — la clausola «i PG non si disegnano» era finora una semplice omissione, adesso porta con sé le **due righe di pavimento più vicine all'ingresso tenute libere** come zona di schieramento. Secondo: §A1 impone che il read-aloud **finisca sull'ostacolo**, quindi il nemico sbarra la via in AVANTI e appartiene fra il gruppo e l'uscita, non alle sue spalle. Terzo: uno scontro che parte sulla soglia è uno scontro in una strettoia che il gruppo non ha scelto — nessuno si schiera, i tiratori non trovano un angolo, e l'intera griglia appena disegnata resta inutilizzata. I nemici vanno nella **metà lontana** del pavimento, o al **CENTRO** in un'arena tonda.
  **VERIFICA:** 06 a 77 §, nessuna riga sopra i 2000 char, blocco MAPPA **identico parola per parola in cv e ov**. Le due condizioni entrano anche nell'auto-controllo in forma contabile (via d'ingresso in basso · due righe libere · nemici nella metà lontana). **Progressi confermati dal collaudo:** `*` non più a muro (0 su 4), overlay distinti e non adiacenti, ingombro del boss corretto, due porte per stanza.

- **v4.96 / cv37 / ov16 — LA MAPPA E IL TESTO LETTO AI GIOCATORI DESCRIVEVANO DUE STANZE DIVERSE.** Il GM ha notato che le coperture stanno sempre attaccate ai muri. Misurato su `Toto-Rak.pdf`: copertura wall-adjacent **8 volte su 8 (100%)**, sempre la stessa forma — una striscia verticale contro la parete destra — e **zero ostacoli alla linea di vista** in tre mappe.
  **LA PROVA CHE HA SPOSTATO LA DIAGNOSI: il modello scrive già la prosa giusta e poi disegna altro.** Il read-aloud diceva «antiche celle in pietra … radici contorte … ragnatele spesse come cavi d'acciaio … emerge dal fango»; la griglia tre righe sotto mostrava una striscia di `▒` sul muro e un 2×2 di `≈`. Un altro nominava «un antico **pedestal** gelmorriano **al centro** della stanza»: sulla mappa, niente. Non mancava il contenuto — **mancava il collegamento**.
  **CAUSA, ed è un difetto della v2 che ho introdotto io.** La regola «la mappa disegna ciò che la prosa dice» esisteva già, ma scritta come **verifica a posteriori** («ogni feature nominata HA le sue caselle»), mentre l'overlay era scritto come **procedura** («scegli una REGIONE dalla tabella»). **Fra una verifica e una procedura vince la procedura**, e la tabella delle regioni è diventata un **menù di contenuti** invece del vocabolario con cui disegnare ciò che il testo aveva già detto. Ci si è aggiunto un bias mio: 3 regioni su 7 sono a muro, e l'unico esempio di copertura in tabella era `LATO` = «colonnato, riparo lungo una parete». Il modello ha copiato l'esempio.
  **IL FIX CENTRALE: la regola diventa una PROCEDURA IN TRE PASSI, e la tabella viene declassata.** «Rileggi il read-aloud che hai appena scritto → elenca gli elementi fisici che nomina → disegna QUELLI»; solo dopo la tabella interviene, e **solo per dire COME si dipinge ciascuno in caselle**. Aggiunta la riga che nomina l'inversione per quello che è: la tabella è **un vocabolario di disegno, mai un menù di contenuti** — scegliere prima la regione e poi inventarsi una feature per riempirla produce terreno generico che non appartiene a nessuna scena, mentre la cosa specifica che la finzione ha nominato resta non disegnata. Corretta anche la riga delle tre passate, che diceva ancora di dipingere «dalla tabella».
  **`█` VALE ANCHE DENTRO LA STANZA (modifica abilitante, non prescrittiva).** Nessuna riga diceva che il blocco pieno può stare fuori dal perimetro: «un pedestal al centro» o «celle in pietra» **non erano disegnabili nemmeno volendo**, ed è il motivo per cui nessuna mappa ha mai avuto un ostacolo alla linea di vista — `█` è l'unico simbolo che la interrompe, tutto il resto si vede e si colpisce attraverso. `CENTRO` nominava già «colonna centrale» senza mai dire con quale glifo.
  **SPAZIATURA: si importa il CRITERIO, non l'algoritmo.** I generatori classici (BSP, automi cellulari, Wave Function Collapse) producono planimetrie, non l'arredamento di una stanza: strumento sbagliato. Quello giusto è il campionamento a **disco di Poisson**, la cui proprietà utile è una sola — **distanza minima**. Non la si fa calcolare: la si riduce a due cose che si guardano, «due overlay non si toccano e non stanno tutti sullo stesso muro». **Di un algoritmo si importa il criterio di accettazione, mai il procedimento** — è l'unica forma che regge sul pavimento.
  **BIFORCAZIONE STANZA / ARENA (concordata col GM).** Un'arena da trial in FFXIV è **canonicamente spoglia**: un disco piatto dove il terreno È la meccanica (il bordo che brucia, le mattonelle che cadono), non scenografia. Riempirla di pilastri obbedirebbe alla lettera del design D&D e tradirebbe la fonte. Quindi: **stanze di dungeon** → almeno un overlay, al massimo tre, presi dalla lista ricavata dalla prosa; **`CUNICOLO`/`CORRIDOIO`** → niente di obbligatorio; **`ARENA`/`ARENA TONDA`** → **spoglia è la risposta GIUSTA**, solo pericoli e buchi.
  **DELIBERATAMENTE NON FATTO** (decisione del GM, «non dobbiamo strafare»): nessuna banda di densità 2-4, nessun obbligo di copertura a N caselle dal muro, nessuna percentuale di superficie da calcolare, nessun obbligo di pilastro, e **nessuna griglia a 9 zone / regola dei terzi** — vocabolario nuovo per un risultato già ottenuto altrimenti.
  **VERIFICA:** 06 a 77 §, nessuna riga sopra i 2000 char, tabella regioni unica, nessun residuo di «cover down one side», blocco MAPPA **identico parola per parola in cv e ov** (2.328 B). **Numeri da battere al prossimo collaudo (Flash liscio, consegna in PDF):** copertura a muro **100% → non tutte**; elementi del read-aloud resi in caselle **~0 su ~5 → la maggior parte**; ostacoli alla vista **0 → quelli che la prosa nomina**. Caso di controllo: la prima `STANZA` di Toto-Rak deve mostrare celle di pietra, radici e ragnatele, non una striscia generica.

- **v4.95 / cv36 — LA SCALA DELLE MAPPE ERA SBAGLIATA (e un preset era IMPOSSIBILE), e la prima comparsa di Lahabrea è caduta in una collisione fra due regole.** Due segnalazioni del GM sullo stesso collaudo, entrambe fondate, e la prima ha fatto emergere un difetto oggettivo mio.
  **IL `CUNICOLO` NON ERA DISEGNABILE.** Era dichiarato «2 wide», mentre la regola del muro perimetrale stabilisce che la cornice `█` **conta nella misura dichiarata**: 2 caselle meno 2 muri = **zero pavimento**. Conseguenza a catena: il `CORRIDOIO` da 4 lasciava 2 caselle giocabili, cioè esattamente ciò che il `CUNICOLO` prometteva — **i due preset erano collassati nello stesso oggetto**, ed è il motivo per cui il Coeurl Grande veniva rimpicciolito invece di tappare il passaggio. Rimedio strutturale: la tabella ha ora **due colonne separate, GRIGLIA (muri inclusi) e PAVIMENTO (calpestabile)**, perché confondere le due è precisamente il modo in cui si genera un preset impossibile.
  **SCALA RICALIBRATA (crescita moderata, scelta del GM) su tre fatti aritmetici, scritti in 06 come motivazione vincolante perché non vengano ristretti di nuovo.** (1) **Un PG percorre 9 m = 6 caselle a turno**, e la vecchia `STANZA` aveva 7×6 caselle giocabili: chiunque raggiungeva chiunque al turno 1, e il posizionamento smetteva di essere una decisione. (2) **Un'AoE da 6 m di raggio è larga 8 caselle** — copriva la stanza intera. Questo conta qui più che nel 5e generico, perché il nostro design dei boss (05 Ch.9, §B10) è costruito sulle **aree telegrafate con contromossa**: in una stanza più piccola dell'AoE non c'è dove schivare, e la mappa stava cancellando in silenzio la contromossa. (3) Oltre ~12 caselle di distanza lo scontro si affloscia, quindi i preset **si fermano lì** e non crescono oltre. Nuovi valori di pavimento: `CUNICOLO` 2×10 · `CORRIDOIO` 4×12 · `CELLA` 6×6 · `STANZA` 10×8 · `SALA` 14×10 · `ARENA` 16×16 · `APERTO` 20×14 · `SALA TONDA` 10 di diametro · `ARENA TONDA` 16. Entrambe le silhouette tonde **ridisegnate e verificate dai byte**: simmetriche sui due assi, `SALA TONDA` con anello di roccia chiuso (zero pavimento sul bordo) e due porte adiacenti al pavimento.
  **LAHABREA: il pin c'era, la regola c'era, ed è caduto lo stesso — è una COLLISIONE, non un buco di dati.** Il GM ha segnalato la mancanza della comparsa di Lahabrea prima del boss, supponendo che andasse pinnata. **Era già pinnata**: 08 riga 102, `[Toto-Rak, BEFORE the boss]`, WIKI-VERIFIED, con la battuta e con l'informazione che è **lui a scatenare il banemite**. E §B1 impone già di riprodurre OGNI cutscene pinnata. Misura del contorno: su **113 pin, solo 3 dichiarano dove vanno rispetto a uno scontro**, e due sono questo stesso beat — quindi ri-pinnare non avrebbe risolto nulla. **La causa vera:** §B1 ENCOUNTER PACKAGE impone che sopra il read-aloud stiano `Difficoltà:` e `Innesco:` **«and NOTHING ELSE»**, il che esclude letteralmente una cutscene che deve precedere lo scontro. Fra due regole binding il modello ha seguito quella **output-forcing** e ha lasciato cadere l'altra — perdendo **il primo Ascian nominato della campagna** — mentre la visione dell'Eco DOPO il boss è sopravvissuta perché nessuno le contendeva lo slot.
  **TRE RIMEDI, e nessuno è «ripetere il divieto».** (a) La clausola «nothing else» è ora **esplicitamente limitata ai blocchi del pacchetto**: una scena pinnata si scrive per intero PRIMA che il pacchetto si apra. (b) **Quando il pin fornisce l'innesco, l'innesco non si inventa** — se la scena finisce con qualcuno che scatena il nemico, quello è l'`Innesco:`; il modello aveva scritto «il primo PG che varca la soglia», sostituendo il canone con un arredo. (c) **Una divisione in parti non può cadere fra una scena pinnata e lo scontro che introduce** (§B12): qui la parte 2 si apriva dritta su `Boss del duty: Graffias` e la scena stava esattamente sulla cucitura, che è la posizione in cui un contenuto ha più probabilità di sparire.
  **`cv` PORTA LA REGOLA, `ov` NO — ed è l'eccezione prevista da §1.1c che funziona:** il One-Shot non usa il manifest MSQ, quindi la clausola sarebbe testo morto. Il blocco MAPPA resta invece **identico parola per parola** nei due file.
  **VERIFICA:** 06 a 77 §, nessuna riga sopra i 2000 char, silhouette lette dai byte, zero residui delle misure vecchie (`2 wide × 12`, `SALA 12 × 10`, `SALA TONDA 10 × 10`). **Progressi confermati dal collaudo precedente:** `≈` 3 e `*` 6 dove erano zero, due porte per stanza, boss a 4 caselle in tutte e tre le mappe. **Resta a zero la COPERTURA (`▓ ▒`)** — è il numero da guardare al prossimo giro.

- **v4.94 / cv35 / ov15 — MAPPA TATTICA v2: il preset diventa una TELA, e i controlli diventano CONTABILI.** Il collaudo su Gemini 3.6 Flash (`Toto-Rak.pdf`, letto dal PDF perché il paste `.txt` perde i glifi) ha dato tre mappe con **`▓ ▒ ≈ *` = zero occorrenze**: scatole murate con dentro un mostro. **CAUSA, e vale come lezione generale: sostituire un campo in prosa con uno strutturato fa perdere la garanzia che il campo portava.** `Terreno:` OBBLIGAVA a descrivere il terreno; la mappa lo ha reso facoltativo, perché nessuna riga di §B8 imponeva di metterci una sola caratteristica e **una griglia nuda è banalmente coerente** — supera ogni controllo di coerenza proprio perché non contiene nulla da controllare. Ci ha contribuito una mia formulazione: «riproducila esattamente **e poi collocaci gli attori**» nomina solo N/B/O/X e legge come un permesso a non aggiungere altro. Il modello ha obbedito alla lettera.
  **ARCHITETTURA: tre passate, ognuna una classificazione — PRESET → OVERLAY → ATTORI.** La passata nuova è la seconda. Un overlay è una coppia `(REGIONE, SIMBOLO)` da due insiemi chiusi: **sette regioni** (`BORDO` · `CENTRO` · `META` · `ANGOLI` · `LATO` · `CHIAZZA` · `SPINA`), ognuna con la sua ricetta in caselle, per i simboli che già esistevano. Il modello NOMINA dove e NOMINA cosa; nessuna coordinata, nessuna misura. Il bordo che brucia di Thordan è `BORDO` × `*`. Gli attori vanno per ultimi, su caselle libere, così nulla parte dentro il proprio pericolo — e dichiarare l'ordine toglie una decisione invece di aggiungerne una.
  **DIPINGERE COL VUOTO È RIMODELLARE — ed è il motivo per cui i preset NON si allargano.** `SPINA` × vuoto = un crepaccio che taglia l'arena · `META` × vuoto = mezza piattaforma sparita · `ANGOLI` × `█` = una sala tonda ricavata da una quadrata. Un solo vocabolario aggiunge e toglie, quindi una forma irregolare non richiede mai un preset nuovo.
  **CO-LOCAZIONE (quarto caso della sessione, LEZIONE 2.13): §B10 raccoglieva il dato e §B8 non lo leggeva.** Il TRIAL LORE-FIDELITY CHECKLIST obbliga già a stabilire dalla wiki, punto (2), «l'arena — il suo aspetto reale **E il suo vero pericolo / instant-death**». Quel dato non arrivava mai alla regola che disegna. Aggiunta una riga binding autonoma in §B10 (estratta a parte per non sfondare i 2000 char sulla riga del checklist) più il rimando in §B8, così è raggiungibile da entrambi i lati.
  **`SALA TONDA` MURATA — difetto del template, mio.** La silhouette era identica per aspetto a `ARENA TONDA`, cioè senza muri: una camera rituale dentro un dungeon veniva emessa come un disco di pavimento sospeso nel nulla, e il modello la copiava **correttamente**. Nuova sagoma verificata dai byte: 10×10, profilo di pavimento `0·4·6·8·8·8·8·6·4·0` simmetrico, anello di `█` chiuso (zero celle di pavimento sul bordo esterno), due `_` entrambe adiacenti al pavimento. **ROUND ≠ APERTO**: una CAMERA tonda è scavata nella roccia, una PIATTAFORMA tonda pende sul vuoto. Corretta di conseguenza la regola del muro perimetrale, che elencava «entrambi i preset tondi» fra gli aperti.
  **DUE APERTURE, contabile.** La `STANZA` del primo boss usciva con una porta sola e nessuna via oltre, nello stesso run in cui il `CORRIDOIO` ne portava correttamente una per capo. Un preset chiuso porta ora due aperture — una d'ingresso, una di prosecuzione — salvo vicolo cieco dichiarato dal beat.
  **INGOMBRO CONTABILE, e il pattern del guasto va nominato.** Il Coeurl Grande usciva da **1 casella** nella `STANZA` e **2** nel `CORRIDOIO`, con la chiave che scriveva «(2×2)» accanto: la regola era nota e semplicemente non applicata al disegno. Ma Graffias, nella `SALA TONDA` aperta, usciva **giusto (4)** — cioè **il modello rimpicciolisce la creatura solo quando lo spazio è stretto**, esattamente il caso in cui l'ingombro è l'informazione che serve. Rimedio nella forma che qui funziona: la chiave dichiara il **TOTALE in caselle** (`Grande, 2×2 = 4 caselle`) e l'auto-controllo **conta le lettere sulla griglia** e le confronta.
  **`cv`/`ov` TOCCATE, contro la previsione del piano.** Il piano le dava invariate; la verifica ha mostrato il contrario, per due motivi. (1) La riga descriveva la **forma** della mappa e mai il suo **contenuto** — cioè taceva proprio sulla regola che ha ceduto, e quel layer è sempre in contesto e vince sui knowledge file. (2) Diceva che i preset aperti sono «arena, aperto, **round**», affermazione resa FALSA dalla `SALA TONDA` murata: una modifica a 06 aveva silenziosamente invalidato una riga delle istruzioni. Il blocco resta **identico parola per parola in cv e ov** (§1.1c), 1.359 → 1.705 B. `lv` non tocca pacchetti incontro e resta invariata.
  **VERIFICA:** 06 resta a **77 §**, nessuna riga sopra i 2000 char, le sette regioni in una tabella sola, silhouette letta dai byte (non dal paste), nessun residuo di «then place the actors into its cells» né di «arena, aperto, round». **I numeri da battere al prossimo collaudo, che è su Flash liscio perché quello è il pavimento:** `▓ ▒ ≈ *` = 0 → almeno 1 overlay per mappa; porte nella `STANZA` = 1 → 2; caselle del Coeurl = 1 → 4.
  **NOTA A VERBALE, non una modifica:** confronto fra le due configurazioni di Flash sullo stesso lavoro — **con** reasoning esteso 7 conti su 7 corretti, **senza** 2 errori su 8 (PF Coeurl 52 dichiarati contro 59 calcolati, PF Acaro 9 contro 7) più un **`1d7`**, che in 5e non esiste, e un «*repetir*» al posto di «ripetere». Sono guasti **silenziosi**: un boss con 52 PF invece di 59 non si nota, si nota che lo scontro finisce prima. È **una run per configurazione**, quindi vale come indizio e non come misura — non cambia il pavimento, ma va rifatto il conto la prossima volta.

- **ov12 / lv11 / cv32 (LOTTO F1b): la dieta arriva anche a One-Shot e Loremonger, e un riferimento MORTO era in tutti e tre.** Il GM ha notato che l'ottimizzazione per il modello pavimento era stata fatta solo sulla campagna. **Precisazione utile: F2, F3 e F4 NON erano rimasti indietro** — vivono in 06/07/08, che sono condivisi, quindi One-Shot e Loremonger avevano già ereditato la forma unica delle regole, la regola del beat che finisce allo scontro e tutti i fix OST. Restava indietro solo F1, che è per definizione per-assistente.
  **DIFETTO PIÙ GRAVE DELLO STRIP, trovato strada facendo: tutti e tre i file citavano ancora `00 → index`**, un file RITIRATO nel lotto B1. La verifica di B1 diceva testualmente di controllare anche cv/ov/lv e io ho controllato solo i `.md`: è la terza occorrenza registrata della stessa classe («un alias rimosso dove il comando è DEFINITO sopravvive dove è solo CITATO — spazza per stringa, non per sezione»). Ora zero in tutti e tre. Rimosso anche l'ultimo `§A4 as overridden`, sopravvissuto in ov e lv dopo il lotto B5.
  **STRIP: ov 15.493 → 13.996 B (−1.497, −10%) · lv 13.395 → 12.659 B (−736, −5,5%).** Le righe tagliate sono le stesse di cv e per lo stesso motivo: lo stat block era **1.421 B identici in entrambi** — cioè la versione pre-F1 di cv — più il pacchetto incontro, lo SCOPE di ov (che ripeteva per intero la procedura `/wipe` già presente nella sua riga di comando), il WORKFLOW, e le righe `/tracker` e `/riposo`.
  **SCELTA DI METODO: dove la regola è la STESSA, ora il testo è IDENTICO nei tre file** (stat block e pacchetto incontro sono copiati da cv parola per parola, con la sola coda `Via A / Via B` che ov e lv hanno in più perché generano creature da zero). Non è estetica: rende la prossima modifica una sostituzione meccanica invece di tre riscritture che divergono. **Sempre intatte** le leve con supporto osservazionale: esemplare di registro, binding dei nomi, blocco MEDIA, self-revision.
  **Totale strato sempre in contesto: 50.576 → 48.330 B.** Sommato a F1 su cv, la dieta complessiva dal picco è ~7,7 KB per turno.

- **08 v3.40 (companion 06 v4.90): i temi leve/FATE sono pinnati — ma 4 delle 9 tracce proposte sono state SCARTATE.** Il GM ha autorizzato Fandom per questo caso specifico (le due wiki ammesse restano irraggiungibili: GE 403 anche sulla `Category:FATE Playing Battle Theme`, CGW 404 sulle pagine dei brani) e ha portato una lista di 9 titoli da Google. **Non è stata presa per buona.** Confronto con i dati già in 08:
  - **`To the Fore` — SCARTATA. 9 occorrenze in 08: è il tema di battaglia e mid-boss dei dungeon di STORMBLOOD.** Pinnarla anche come tema FATE avrebbe fatto colare una traccia di dungeon SB dentro gli scontri di subquest di tutta la campagna.
  - **`Torn from the Heavens` — SCARTATA. È già il lead-in dei PRIMAL overworld** (Ifrit/Titan/Garuda). Riusarla per un «FATE boss maggiore» avrebbe fatto suonare uno scontro di subquest come l'arrivo di un primal: fuorviante al tavolo, che è peggio del silenzio.
  - **`Battle Theme 1.x` — SCARTATA:** non è un titolo, è una descrizione.
  - **`Occult Crescent` — SCARTATA:** è Dawntrail, fuori dall'arco della campagna (e il segnale trovato indicava comunque 'FFV Battle 1' come traccia effettiva).
  **Pinnate le 5 pulite**, mappate per TIPO di scontro invece che elencate: `Tug of Fate` (subquest ordinaria, il default) · `Tenacity` (lavoro su commissione, tema delle Battlecraft leve) · `Hard to Miss` (boss di subquest) · `The Thunderer` (minaccia di scala world-boss) · `The Corpse Hall` (Odin, che 06 §B20 usa già come esempio di 'seme' non agganciabile). Il blocco dichiara anche esplicitamente le due tracce NON usabili e perché — così il prossimo audit non le ri-propone.
  **INCIAMPO REGISTRATO:** durante la ricerca avevo quasi preso `A Realm Remembered` per una traccia. È il nome dell'**album** dell'OST di ARR. È esattamente il tipo di errore che, se non intercettato, resta congelato nei dati per sempre.

- **08 v3.39: LE 172 CUTSCENE PINNATE NON DICEVANO CHE MUSICA PARTE — ipotesi del GM, confermata.** Il GM ha sospettato che i pin dei manifest avessero «lo stesso problema di forma» delle righe duty e zona. **Misurato: 172 voci di manifest (IN-SCENA / ALTROVE / VISIONE DELL'ECO / REVEAL / GATED), ZERO che nominano una traccia.** I temi d'umore ricorrenti esistono e sono corretti (`ASCIAN → Without Shadow`), ma vivono in `08.OST-SCENE` a **660 righe** dal pin di Lahabrea a Toto-Rak: chunk garantitamente diversi. Perché la scena di Lahabrea, che è il primo Ascian nominato dell'intera campagna, esce con la musica d'ambiente del dungeon.
  **111 delle 172 pin hanno un tema d'umore mappabile** (47 Ascian · 22 primal · 21 lutto · 17 garleano · 2 Eco · 2 cristallo). Taggarle una a una sarebbe stato 111 modifiche a rischio per ~3 KB; la co-locazione si ottiene meglio **mettendo la mappatura nell'intestazione di OGNI manifest** — 6 inserzioni, una per arco più la Torre di Cristallo — così viaggia a poche righe dalle sue voci invece che a centinaia. Le 61 pin senza mappatura ovvia restano correttamente sul tema del duty o della zona.
  **NON RIUSCITO — i temi leve/FATE.** Il GM ha chiesto di prenderli dalla wiki. Non è stato possibile con le fonti che §A14 ammette: Gamer Escape risponde **403** a ogni fetch, ConsoleGamesWiki dà **404** sulle pagine dei brani e la sua pagina FATE non nomina alcuna traccia. L'unica fonte reperibile resta Fandom, vietata. La regola corretta in 06 v4.89 regge comunque il caso — senza un titolo reale si ripiega sul `(battle)` della zona — quindi il difetto è chiuso; manca solo la varietà, che torna disponibile appena i titoli arrivano da una fonte ammessa o dal GM.

- **v4.91 (companion cv33 / ov13 / lv12): NUOVA FEATURE — la MAPPA TATTICA sostituisce il campo `Terreno:`.** Il campo descriveva a parole il campo di battaglia e il GM doveva tradurlo in una mappa vera con la penna. Ora §B8 emette una **griglia in scala dentro un code fence, 1 casella = 1,5 m**, il quadretto standard del tabellone, seguita da una riga-chiave e una riga di distanze.
  **IL RISCHIO, dichiarato in progetto e non scoperto dopo:** il pavimento è Gemini 3.6 Flash e la debolezza documentata di quel tier è **proprio il ragionamento spaziale**. Una griglia in scala è il compito peggiore possibile per quel modello, quindi **ogni scelta di design esiste per togliergli una decisione spaziale**: la taglia si sceglie fra SETTE preset con un nome (`CUNICOLO` 2×12 … `ARENA` 14×14), che è una CLASSIFICAZIONE e non una stima; la forma non si indovina perché è già scritta nei pin arena di 08 e nel read-aloud; l'ingombro di una creatura è una TABELLA letta dalla Taglia dello stat block; e la conversione metri→caselle la fa l'assistente **una volta**, nella riga `In caselle:`, invece del GM a ogni round. **Ripiego dichiarato:** se l'auto-controllo fallisce si emette la sola riga-chiave senza griglia — una mappa sbagliata al tavolo è peggio di nessuna mappa, perché il GM la copia senza rileggerla.
  **ESTETICA = ROBUSTEZZA, non decorazione.** Il peso visivo del glifo **È** il livello di copertura (`█` totale → `▓` tre quarti → `▒` mezza → `·` libero): più la cella è scura, più blocca, e la mappa si legge senza tornare sulla legenda. **Niente box-drawing** (`┌┐└┘`) per quanto belli: obbligano a scegliere il giunto giusto per ogni posizione, cioè topologia — col blocco pieno ogni cella di muro è lo stesso identico carattere, zero decisioni. **Niente emoji**: in monospazio occupano due colonne e spaccano l'allineamento, l'unica cosa che una mappa in scala non può permettersi. **Niente colori**: gli ANSI stamperebbero spazzatura, l'evidenziazione del fence colora per token e non per significato — e il problema che il colore risolverebbe è già risolto dalla scala di grigi, che per giunta sopravvive alla fotocopia.
  **CINQUE SCELTE DEL GM CHE HANNO MIGLIORATO IL DESIGN, registrate perché sono la parte che conta:** (a) la taglia segue la forma reale invece di essere fissa — corretto in preset chiusi, così resta una classificazione; (b) la prima scala sbagliava **per eccesso** (un «corridoio» da 9 m è una sala), quindi da quattro preset a sette, fino al cunicolo da **due quadretti**; (c) **niente assi A-L/1-10**, che avevo proposto: sul tabellone fisico non ci sono, sarebbero solo roba da ricopiare; (d) **i PG non si segnano**, si posizionano da soli — la mappa esiste per dire dove stanno i NEMICI, l'unica cosa che il GM non sa già; (e) **la mappa è lo STATO INIZIALE e basta**, che sostituisce una mia regola più debole («ciò che ha posizione stabile»): fuori gli addizionali di metà scontro e i bersagli attaccati al corpo del boss, e via il simbolo `A` che avevo proposto. Un simbolo in meno vale anche per il modello.
  **CHIUDE UN CERCHIO:** §B6 rende `Taglia` obbligatoria con la motivazione testuale che «*al GM serve l'ingombro sul tabellone*». Finora era un dato da convertire a mano; ora **la mappa lo disegna** — Titano è Enorme, quindi un blocco 3×3.
  **DUE FIX DI LEGGIBILITÀ nello stesso lotto.** (1) `Terreno:` usciva **attaccato** a `Tattica:`: la regola «ogni campo sulla propria riga» esisteva già, quindi era una slip di forma — rimediata **strutturalmente** (con la mappa in mezzo non possono più toccarsi) più il requisito esplicito di **riga vuota** fra i campi. (2) **Intestazioni a due livelli** nello stat block: nome della creatura `###`, sezioni `#### Tratti` / `#### Azioni` / `#### Azioni Leggendarie` / `#### Bottino`, con i nomi delle voci che restano in grassetto. **Nota storica inline in §B6 perché non venga re-litigata una quarta volta:** il layout era già stato corretto due volte (v4.47 il muro di testo, v4.50 le tre categorie incatenate); il difetto rimasto era che nome e titoli avevano lo stesso peso visivo del corpo che il GM sta scorrendo.
  **`lv` NON riceve il pacchetto incontro** — il Loremonger non ne costruisce — **ma riceve le intestazioni**, perché gli stat block li genera. È la prima applicazione della regola «i tre file si modificano insieme» (PM §1.1c) **con la sua eccezione**: si propaga ciò che è condiviso, non ciò che non lo è.

- **v4.92 (companion cv34 / ov14): la mappa dopo il PRIMO collaudo — tre difetti erano MIEI di specifica.** Test su Sonnet 5 (un beat ad Alto, uno a Medio). Ha retto la parte che temevo: **Titano è uscito 3×3**, quindi la regola Taglia→ingombro funziona, e il tema di battaglia della zona era corretto (`The Land Breathes` per La Noscea, il fix di co-locazione del giorno prima). Ma la griglia è uscita storta su entrambi i beat, e per il criterio fissato nel piano — *se sbaglia su Sonnet è la regola a essere scritta male* — la colpa era della spec.
  **(1) ORIENTAMENTO NON DICHIARATO.** `CUNICOLO 2×12` non diceva quale numero fosse la larghezza: il modello l'ha **trasposto**, disegnando 12 colonne × 2 righe. Ora ogni preset dice **`larghezza × altezza`** a parole, e l'auto-controllo lo verifica in quell'ordine.
  **(2) LA CORNICE ERA SEMPRE OBBLIGATORIA, ed è FALSO per i preset aperti** — segnalato dal GM. Avevo scritto che il muro perimetrale fa parte del preset, ma **l'arena di Titano è una piattaforma sospesa: non ha muri, ha il vuoto**. Avevo criticato come difetto un output che era corretto. Ora la regola è condizionata: `CUNICOLO`/`CORRIDOIO`/`CELLA`/`STANZA`/`SALA` hanno la cornice `█` e la contano nella taglia; `ARENA`/`APERTO`/le tonde no, il pavimento semplicemente finisce. (Il cunicolo, che i muri li vuole, non li aveva: quel difetto resta ed è coperto dalla stessa regola.)
  **(3) SPAZIATURA NON VINCOLANTE.** Le due mappe sono uscite una con le celle spaziate e una attaccate (`··········`), e attaccate non si contano — che è l'intero scopo di una mappa in scala. Ora: un carattere per cella, **uno spazio fra le celle, sempre**.
  **LE ARENE CIRCOLARI — che sono circa metà di quelle FFXIV — si COPIANO, non si disegnano.** Una circonferenza su griglia richiede un rientro calcolato riga per riga, cioè esattamente il calcolo che il pavimento sbaglia. Quindi due preset nuovi, `SALA TONDA` (10×10) e `ARENA TONDA` (14×14), con la **sagoma pre-disegnata nella spec ed emessa VERBATIM** — stesso meccanismo del template del tracker §A24.1, che esiste per la stessa ragione. Il modello non la calcola: la copia e ci mette dentro gli attori. Nove preset in tutto.
  **UN TRIAL NON È AUTOMATICAMENTE TONDO** (precisazione del GM, e i dati gli danno ragione): i pin arena di 08 dichiarano la forma e si contraddicono apposta — Amaurot è «*una piattaforma CIRCOLARE*», ma la Passerella della Fede è «*il PONTE*» (`CORRIDOIO`), il Whorleater è «*il PONTE DI COPERTA della nave*» (`SALA`) e Zodiark ha «*una piattaforma con un solo lato aperto*». Scegliere il tondo perché è un trial è un'ipotesi; leggere il pin no.
  **NUOVA REGOLA — IL CORPO PIÙ GRANDE DEL PAVIMENTO SI DISEGNA TRONCATO** (caso sollevato dal GM: la Nube dell'Oscurità, la Cantrice Finale). Alcuni boss sono così vasti che solo PARTE di loro sta sull'area calpestabile. Si disegnano **solo le caselle occupate DENTRO la griglia**, e la chiave dice che il corpo prosegue oltre il bordo. Non si disegna fuori dal pavimento giocabile e non si rimpicciolisce la creatura per farcela stare: la griglia risponde a «quali caselle sono bloccate e da dove lo raggiungo», la taglia vera resta nello stat block. Una fascia di `B` lungo un bordo è l'immagine giusta — dice che quella cosa si avvicina da un lato solo e non si aggira.
  **NOTA DI METODO:** due difetti che avevo diagnosticato non esistevano. Leggevo `Test.txt` con l'encoding sbagliato e ogni glifo Unicode arrivava corrotto: ho creduto che il pavimento fosse `█` invece di `·`, e che il terreno difficile fosse un simbolo inventato invece di `≈`. **Un `.txt` incollato è una fonte LOSSY: i glifi non si diagnosticano da lì**, si leggono dai byte o si chiedono al GM.

- **v4.93: RITIRATA la regola «un beat finisce al suo scontro» (v4.88) — era SBAGLIATA, non solo superflua.** Segnalata dal GM: «*/esito può essere dato a qualsiasi cosa, non solo a uno scontro, quella regola forza una cosa che non è naturale — finisce lo scontro, c'è l'epilogo dello scontro*». Ha ragione, e verificando è emerso un argomento più grave del suo: **la regola avrebbe CAUSATO un difetto.**
  **(a) Combatte il design esistente.** Il corpus dice testualmente che `/esito` è «*l'UNICO canale con cui la realtà al tavolo contraddice la presunzione LIVE DEFAULT = GIOCATO*»: il sistema è costruito perché l'assistente PRESUMA l'esito canonico e il GM corregga. Una regola che ferma il beat allo scontro annulla quella presunzione proprio dove si applica di più.
  **(b) Confligge con le cutscene pinnate — ed è il motivo decisivo.** §B1 obbliga a riprodurre ogni cutscene pinnata AL SUO BEAT. Il Cristallo di Terra e la voce di Hydaelyn dopo Titano sono pinnati in 08.1: con la regola attiva quel beat si sarebbe fermato allo stat block e la cutscene non sarebbe mai uscita. Avrei introdotto un guasto per prevenirne un altro.
  **(c) Il difetto originale era una VIOLAZIONE DI UNA REGOLA ESISTENTE.** Il beat del gubbue non narrava «l'epilogo dello scontro»: proseguiva per tre-quattro STEP DI QUEST (torna da Shamani, consegna a Wheiskaet, il banchetto è concluso). Quella è la `ONE-SCENE-RULE` / lo step atomico, che il corpus ha già. **Ho scambiato la violazione di una regola esistente per l'assenza di una nuova** — esattamente la lezione «prima di agire su un difetto, chiedi QUALE STRATO l'ha prodotto», applicata contro di me.
  **Nessun sostituto.** Se il caso si ripresenta è coperto dalla regola dello step atomico, che è dove va diagnosticato.

- **v4.89 (companion 08 v3.38): I TEMI DI BATTAGLIA DELLE ZONE ERANO IRRAGGIUNGIBILI — segnalato dal GM.** §A23 diceva già «*uno scontro OPEN-WORLD usa il tema di battaglia di quella ZONA/regione*» e ne citava la famiglia ARR (`The Land Breathes/Bleeds/Breaks/Burns/Bends`), ma **quei titoli avevano ZERO occorrenze in 08** e la riga zona in `08.OST-SCENE` portava solo l'ambiente (`La Noscea — On Westerly Winds`). Il modello aveva quindi i nomi di famiglia e nessuna mappatura: nella run osservata lo scontro col goobbue in La Noscea è uscito **senza musica**, e in una run precedente con un titolo **indovinato**. È lo stesso difetto di co-locazione dei duty, un piano più sopra.
  **Tutte e 29 le righe zona, in ogni espansione, portano ora `(ambient) … · (battle) …`.** Per ARR la mappatura per regione è nuova e **confermata dal GM** (Bosco Nero → The Land Bends · Thanalan → The Land Burns · La Noscea → The Land Breathes · Coerthas → The Land Breaks · Mor Dhona → The Land Bleeds): non l'ho scritta da fonte propria perché Gamer Escape risponde 403 e ConsoleGamesWiki non ha le pagine dei brani, e l'unica fonte reperibile era Fandom, che §A14 vieta. HW/SB/ShB/EW **avevano già** il proprio tema open-world (`Melt` · `Looping in the Deepest Fringes` · `Rencounter` · `Unbowed`) — ma nel preambolo dei DUTY, cioè in un chunk diverso da quello che una query sulla zona pesca. Ora è accanto a ogni zona.
  **REGOLA CORRETTA NELLA FORMA, non solo nei dati:** §A23 diceva che uno scontro di SUBQUEST usa «*un tema leve/FATE a scelta dell'assistente per varietà*». Nessun titolo leve/FATE è pinnato da nessuna parte, quindi quella riga chiedeva al modello di **scegliere liberamente da una categoria vuota** — la forma esatta che produce i titoli inventati che `NO COINED TITLES` vieta due righe dopo. Ora: si usa un tema leve/FATE **solo se se ne conosce uno reale e cachato**, altrimenti si ripiega sul `(battle)` della zona, che ora esiste sempre. Mai un titolo inventato, mai il silenzio. **Resta aperto:** se il GM fornisce i titoli leve/FATE reali si pinnano in 08 e la varietà torna disponibile per davvero.

- **v4.88 (LOTTI F2+F4 — companion 07 v1.35 / 08 v3.36): UNA FORMA SOLA PER LE REGOLE, e i due difetti che il test su Flash ha davvero prodotto.**
  **F2 — 181 righe portate alla forma canonica `- **NOME (binding):** testo`.** 06 usava SEI forme diverse per lo stesso oggetto — una regola binding *che ha già un nome* — proprio dove le regole sono più dense: 171 col trattino e il grassetto, 125 nude con `(binding):`, 56 nude con i soli due punti. La guida di prompting di Gemini 3 è esplicita («*scegli UNA convenzione, non mescolarle*»): serve un confine non ambiguo fra istruzione e dato. Dopo: **331 nella forma canonica, 38 righe nude rimaste** — e quelle 38 sono INTESTAZIONI DI BLOCCO (`HEAVENSWARD:`, `INPUT MODULE (render verbatim):`) che introducono righe successive, non regole su una riga: convertirle sarebbe stato sbagliato. **VERIFICA: zero parole aggiunte, zero perse** (confronto per multiinsieme di parole contro HEAD, ignorando la punteggiatura di formattazione). Il beneficio è doppio: il confine che il modello chiede, e la visibilità di un'OMISSIONE — la ragione per cui la regola di layout di §B6 iniziò a funzionare solo quando nominò i suoi atomi.
  **F4a — NUOVA REGOLA: un beat FINISCE al suo scontro, mai oltre.** Osservata due volte sullo stesso ponte: dopo la riga `Bottino:` del goobbue il beat proseguiva — *«Ottenuta la talea… riportate la botte a Wheiskaet… i preparativi sono conclusi»* — cioè **l'esito di un combattimento che il tavolo non aveva ancora giocato**. Verificato che NESSUNA regola lo vietasse: `ENDS ON THE OBSTACLE` esiste in §A1 ma è limitata al blocco `Da leggere ai PG`, non al beat. Il danno è concreto: consegna al GM uno scontro col finale già scritto, e il gruppo potrebbe perdere, fuggire o risolverlo altrimenti — infatti il GM ha dovuto correggere con `/esito i PG scappano dal Gubbue`. La regola sta in §B2 perché il punto in cui si rompe è il beat STOP di un ponte, ma vale per OGNI beat. Le vignette PRIMA dello scontro non sono toccate: quelle sono quest che il GM ha scelto di condensare, lo STOP è quello che si gioca.
  **F4b — la cadenza OST era un difetto di CO-LOCAZIONE in 08, non di regola** (08 v3.37). Flash ha usato `A Thousand Screams` per tutto Toto-Rak, boss compreso — ma quello è l'AMBIENTE, e riusarlo su un boss viola §A23 `AMBIENT != BATTLE`. Causa vera: la riga del duty dava **un solo titolo senza etichetta**, mentre i temi di battaglia/mid-boss/finale stavano in una riga di preambolo separata; basta un confine di chunk fra le due e resta solo l'ambiente. **Tutte e 44 le righe DUNGEON, in ogni espansione, portano ora il set completo inline** — `(ambient) … · (battle) … · (mid-boss) … · (final) …` — con le eccezioni già presenti conservate. È il principio di co-locazione applicato ai dati invece che alle regole.
  **DUE CORREZIONI SEGNALATE DAL GM, entrambe mie:** (a) avevo scritto le etichette in ITALIANO (`AMBIENTE:`, `battaglia:`) dentro un file di DATI, violando la convenzione «istruzioni e conoscenza in inglese, italiano solo nell'output» — e per giunta lo stile giusto esisteva già dodici righe più sotto, nelle voci della Torre di Cristallo (`(ambient)` / `(battle)` / `(final, Phlegethon)`), che non avevo guardato; (b) avevo completato **solo ARR**, lasciando HW/SB/ShB/EW con esattamente il difetto di co-locazione che avevo appena diagnosticato — una correzione a metà è peggio di nessuna, perché fa sembrare la tabella uniforme quando non lo è. Le 25 righe TRIAL restano a traccia singola o a progressione di fase: un trial è UN solo scontro e non ha un tema d'ambiente, quindi lì la forma corta è quella giusta.
  **F4c — `Goobbue` aggiunto a 07 G25** (v1.35): non aveva binding, e due sessioni l'hanno reso «Gobbue» e «Gubbue». È la classe di guasto per cui G25 esiste.
  **CORREZIONE A UNA MIA DIAGNOSI:** avevo scritto che Flash si era *inventato* il tag del riaggancio. **Falso — §B3 lo specifica** (`[MSQ — Riaggancio: <situazione deviata> → <ancoraggio canonico>]`), era presente in v4.87 durante il test, e l'output lo rispettava. Nessuna modifica dovuta.
  **F3 RIDIMENSIONATO, e va messo a verbale come il precedente sulle failure shape.** Il piano prevedeva di convertire 73 «negazioni aperte» in regole di provenienza, sul reperto che le negazioni aperte fanno sovra-indicizzare Flash. Rilette una per una: **la grande maggioranza è GIÀ scritta come regola di provenienza** — «*il TIPO di una creatura viene dalla sua voce wiki (§A5), MAI dedotto dal nome*», «*se la wiki non dà il dato, non inventarlo*», «*CONTA LE VOCI NELL'INDICE… mai dedurlo dalla prosa*». Il divieto sta già a una virgola dalla sua forma positiva, e la guida parla di **direttive isolate** («do not guess» come istruzione a sé), non di questo. Riscriverle in massa avrebbe speso rischio su un problema che il corpus non ha. **Seconda volta in due audit che un asse smentisce la propria premessa** — vale come metodo: misurare la forma, non contare le occorrenze.

- **cv31 (LOTTO F1 — passata sul modello pavimento Gemini 3.6 Flash): lo strato SEMPRE IN CONTESTO torna a dieta, 27.202 → 21.702 B (−5.500, −20%).** È l'unico posto dove i byte si pagano **a ogni turno di ogni sessione**, e da cv12 era cresciuto del +90% (14,6 → 27,7 KB), con un salto singolo di +5 KB quando entrò la condensazione. 06 non è stato toccato: questo lotto è **solo** cv.
  **PERCHÉ ADESSO — la guida di prompting di Gemini 3 su tre punti verificabili:** «*favours directness over persuasion and logic over verbosity*», il modello è poco verboso per default e risponde meglio a istruzioni brevi; *prompt = protocollo*, cioè istruzioni **corte, testabili, verificabili**; e per i contesti lunghi serve **igiene del contesto, non più contesto**. Le righe-comando erano cresciute ben oltre lo schema che il file stesso dichiara (`/comando → cosa produce → riga d'apertura → la cosa non ovvia → §rif`): `/continua` 1.925 B, `/tracker` 1.569, `/riassumi` 1.532, stat block 1.364. Sono tornate a essere righe di schema; la profondità sta in 06.
  **IL METODO, NON NEGOZIABILE** (lezione «prima di degradare una regola always-on al RAG, fai il grep»): per **ognuna** delle otto righe pesanti è stato verificato che il contenuto esistesse davvero in 06 **prima** di toglierlo. Il controllo ha prodotto un falso allarme istruttivo: `AN ACTIVE SUBQUEST BLOCKS 'riassumi'` sembrava mancare in 06 e invece c'era, con un'altra formulazione — motivo per cui la verifica va fatta per **concetto** e non per stringa.
  **NON TOCCATO, ed è deliberato:** l'esemplare di registro §A1 (unico intervento con effetto MISURATO sulla prosa), i binding dei nomi ad alta frequenza (esistono *perché* 07 non viene recuperato durante un beat), il blocco MEDIA (la sua rimozione causò una regressione osservata: le immagini sparivano dopo il primo beat) e i self-check testabili. **Mi sono fermato a 21,7 KB invece dei 18-20 KB previsti dal piano**: l'ultimo 1,3 KB si poteva prendere solo comprimendo le tre righe di politica dei nomi, che esistono per riparare un guasto osservato — non valeva il rischio, e il numero tondo non è un obiettivo.
  **RISCHIO DICHIARATO, perché su questo lotto i due obiettivi tirano in direzioni opposte:** la garanzia di presenza vale **di più** per un modello debole, non di meno. Lo strip è una leva di COSTO che può costare RESA proprio sul pavimento — su modelli forti è quasi certamente indolore perché recuperano 06 senza fatica. Per questo F1 **si collauda da solo, prima degli altri lotti**, ed è il **primo candidato al rollback** se un elemento della checklist sparisce. Precedente diretto: a cv12 uno strip del −36% resse e costò due righe, rimesse per ~250 B.
  Rimosso anche l'ultimo residuo di comando ritirato («*There is NO /nota command*» sulla riga `/esito`), sfuggito al lotto B3, e la dicitura stale «*§A4 as overridden*» nell'intestazione MEDIA.

- v4.87 (LOTTO B5 dell'audit — companion 05 v2.04 / cv30 / ov11 / lv10 / **PM**): **IL PROGETTO TORNA HOST-AGNOSTICO, PER DECISIONE DEL GM.** Il sistema gira in modo equivalente su qualunque host che offra una casella di istruzioni custom più il recupero su file: gli assistenti sono generici e **nessun file di conoscenza o di istruzioni può nominare un fornitore, un prodotto o una UI**. Non è pulizia formale — una regola scritta contro il comportamento di un host diventa sbagliata nel momento in cui lo stesso corpus gira altrove, e questo progetto l'ha già pagata una volta (tre regole media avevano come giustificazione «resta cliccabile su <host>»).
  **Le due differenze di host che esistono DAVVERO, e come sono gestite.** (1) **Il pannello del tracker:** alcuni host renderizzano l'HTML in un pannello laterale da soli, su altri il GM lo seleziona a mano. **Non è automatizzabile dal nostro lato** — è UI dell'host, non output. Nuova regola in §A24: l'emissione è identica e **è vietato compensare** — niente riga «apri il pannello», niente ri-emissione se non compare, e soprattutto **niente roster incollato come testo di chat**, che era la scorciatoia pericolosa (raddoppia i token e crea due fonti di verità sullo scontro in corso). (2) **I link media:** ogni immagine/mappa/OST è un link di RICERCA che il GM clicca, mai un risultato incorporato o recuperato da un tool.
  **CONSEGUENZA CHE VALE BYTE VERI: i tre blocchi `PLATFORM OVERRIDE` sono stati CANCELLATI da cv/ov/lv.** Erano nati per imporre link-only contro un 06 che descriveva un comportamento inline; ora che §A4 dice link-only **incondizionatamente** («il link È tutto l'output media — non esiste una variante inline su nessun host»), quelle righe erano no-op che occupavano contesto **sempre presente**, cioè l'unico posto dove i byte si pagano a ogni turno. −1.058 B complessivi dallo strato always-on.
  Ripulite anche: l'intestazione di §A4 che marcava il wording inline come «LEGACY (Gemini-era) superseded by a platform override»; la nota OST che verificava il prefisso di ricerca «su ENTRAMBI» gli host per nome; e la nota storica di §B1 sulla riga `⚔️ Rif. gruppo`, dove «la causa era la piattaforma Gemini» diventa «era l'host dell'epoca, che il progetto ha poi lasciato» — la lezione regge identica senza il nome del fornitore. Le intestazioni `Version` perdono «(Claude-native)» e diventano **(host-agnostic)**.
  **NON toccati, sono falsi positivi:** `Meteor Project` (il progetto garleano, 05 Ch.2.6), `Artifacts are OUT` (grado di rarità D&D, §A20), `Nominated Observers of Artifacts Historical` (il backronimo NOAH, 08), `World Canvas` (abilità di 18° livello, 02) e `Project Image` (incantesimo, 03).

- v4.86 (LOTTO B2 dell'audit — il lotto principale): **LE 18 RIGHE PIÙ GRANDI DI UN CHUNK SONO STATE SPEZZATE.** L'audit ha misurato che 06 portava **18 righe oltre i 2000 caratteri, per 56 KB — il 18% del file**, con un massimo di **5145 caratteri su una riga sola**, mentre nessun altro file del corpus supera i ~1600. La convenzione «una regola per unità recuperabile» si era **rovesciata al vertice**: quelle righe *erano* più grandi dell'unità che dovevano essere, quindi un confine di chunking poteva tagliarle a metà e separare una regola dal suo innesco. Non è teorico — `COUNTING N` (2978 char) è **esattamente** la regola che nei test non veniva co-recuperata con l'avviso che la consuma.
  **Criterio applicato, tre condizioni insieme:** (1) ogni unità **si nomina da sola**, cioè ripete il proprio token d'innesco (`'/voci'`, `🎵 Musica`, `'/viaggio'`, `[COND]`, `save gate`) così che una query la peschi senza il contesto delle righe vicine; (2) sta **sotto ~1200 caratteri**; (3) **non ha il soggetto nella riga precedente**. È il motivo per cui 12 etichette risultano «cambiate»: `OUTPUT IN ITALIAN` → `STAT BLOCK OUTPUT IN ITALIAN`, `BANNED LABELS` → `BANNED DIALOGUE LABELS`, `EXPAND TO THE MAX` → `'/voci' EXPANDS TO THE MAX WHEN TRIGGERED`. Non sono rinomine estetiche: un'etichetta che non nomina il proprio oggetto non è recuperabile da sola.
  **RISULTATO: righe >2000 da 18 a ZERO; massimo da 5145 a 1893; righe >1200 da 40 a 24.** Il file CRESCE di 1.244 B (+0,4%) perché ripetere gli inneschi costa — ed è un costo che si paga volentieri: la dimensione del corpus non è il problema, il recupero parziale sì.
  **VERIFICA DI NON-PERDITA, il controllo che conta:** diff semantico a livello di FRASE contro HEAD (non testuale: le giunzioni spezzate falsano qualsiasi confronto per n-grammi). Su **1.936 frasi da ≥10 parole, 28 risultavano assenti** — ricontrollate una per una: **27 sono riscritture imposte dal criterio 1** (`CGW`→`ConsoleGamesWiki`, `it fires`→`the notice fires`, `render this line`→`render the 🧭 line`), **1 è una deduplicazione voluta** (la conseguenza «/salva scrive una [A] sbagliata» era scritta due volte a due righe di distanza) e **1 è la rimozione di `tplC r.6`**, riferimento morto al nome che il file istruzioni aveva nell'era Gemini. **Zero clausole binding perse.**

- v4.85 (LOTTO B1 dell'audit — companion 05 v2.03, e **00 ritirato**): **POTATURA DELLE FAILURE SHAPE — 8 su 65, molte meno del previsto.** L'audit ha estratto e classificato TUTTE le failure shape del file applicando il criterio anti-bias di v4.78 (*un esempio guadagna il posto SOLO se disambigua un confine che l'astratto non può fissare*). **Esito: 53 RESTANO, 4 si consolidano, 8 escono.** Va messo a verbale perché contraddice l'ipotesi di partenza: mi aspettavo sedimentazione da potare e ho trovato regole che portano il RIPARO insieme al divieto (§A1 «*la riparazione di default è la CANCELLAZIONE, non la sostituzione*»), o distinguono un caso che l'astratto fonde (§A5: il sesso della PERSONA contro il genere grammaticale del sostantivo), o registrano una misura irripetibile (§B6: lo stesso goobbue statato **tre volte in tre run** con tre GdS diversi). **La prosa di 06 non era grasso.**
  **Le 8 tolte, tutte perché la regola sopra è già completa e chiusa:** §A1 «*Sei tornato → Siete tornati*» (ed è già in `cv` L.29 a recall 100%, quindi in 06 era la seconda copia); §A4 «*Alveare Ventrerosso*»; §A5 «*un Elau dai capelli grigi*»; §A5 «*la Cospicua della Settima Alba*»; §A20 «anello +1 CA marcato Non-comune a L4»; §A23 «il secondo scontro lasciato senza tema»; §B1 «*un lampo dell'Eco attraversa uno dei PG*»; §D4 «sottoclasse persa a L3». **Archiviate qui apposta:** se uno di questi guasti torna al tavolo, la riga da rimettere è in questa voce, testuale.

- v4.84 (LOTTO B3 dell'audit — companion cv29): **06 VIOLAVA UNA REGOLA CHE ENUNCIA LUI STESSO.** §B1 stabilisce, con la failure shape osservata **due volte** in test dal vivo, che il roster va enunciato come CHIUSO *«e mai come elenco di ciò che è stato rimosso: nominare un comando ritirato lo rimette in circolo attraverso il recupero»*. E poi il file nominava tre comandi ritirati in forma negativa: `/carica` e `/load` in §B17 (*«non esiste alcun comando /carica o /load»*), `/carica` di nuovo in §B24, `/subquest` in §B20 (*«NON esiste un comando /subquest»*) — più `/subquest` in `cv` L.71. **La negazione non protegge: il recupero non distingue «X non esiste» da «X».** È il meccanismo che ha tenuto vivo `/prepara` per un ciclo intero dopo la rimozione, quindi il progetto aveva già pagato per sapere che è vero.
  **Riparazione: tutte in POSITIVO, zero nomi ritirati.** Dove la frase serviva a spiegare perché il load non ha comando → *«il blocco È l'innesco, e il caricamento è l'unica azione senza una propria parola-comando»*. Dove elencava cosa non esiste per la subquest → *«lo slot singolo è guidato da esattamente tre comandi e nessun altro: /accettiamo lo apre, /riprendi MSQ lo sospende, /riprendi SQ lo riprende»*. Il contenuto informativo è identico, il fianco scoperto no.
  **Perché è stato trovato solo adesso:** l'audit ha confrontato il roster dei comandi nominati in 06 con quello dei tre file di istruzioni. Nessuna rilettura di 06 lo avrebbe prodotto — la frase è corretta e sensata riga per riga; è sbagliata solo rispetto a una regola che sta 400 righe più su.
  **SECONDO REPERTO DELLO STESSO LOTTO, solo cv29: `/riposo` era e non era un beat.** `cv` L.6 e L.58 dicevano *«A STORY BEAT IS PRODUCED ONLY BY /continua, /riassumi, /viaggio»* — enumerazione chiusa — mentre L.62 descrive `/riposo` come *«LONG REST beat»*, L.79 lo elenca fra i *«transient played beats»* e 06 §B28 lo definisce *«on-demand, PLAYED, transient»*. Un comando descritto come beat giocato da tre righe ed escluso dalla quarta, che è quella che si presenta come la definizione.
  **La causa era un predicato sbagliato, non un elenco incompleto:** «produce un beat» stava facendo il lavoro di due proprietà diverse. Separate: **quattro** comandi PLAY A BEAT (`/continua`, `/riassumi`, `/viaggio`, `/riposo`); di questi **due** avanzano il CURSORE e vanno salvati (`/continua`, `/riassumi`), gli altri due sono TRANSIENTI; e il tag `[MSQ`/`[VIAGGIO` appartiene a **tre** di loro — `/riposo` apre su una propria intestazione e non porta tag. Aggiungere `/riposo` all'elenco vecchio avrebbe rotto la parte sul tag, che era corretta: è la ragione per cui la riparazione ridefinisce il predicato invece di allungare la lista.

- v4.83: **UN TELEGRAFO SCATTATO ORA SI SPEGNE DA SOLO** quando il turno passa (domanda del GM: «quando è in stato SCATTA e vado avanti col turno si auto-rimuove, ha senso?»). **Prima verificato che il codice NON lo faceva:** il decremento in `nextTurn()` è protetto da `telegraph > 0`, quindi a zero non veniva toccato e lo SCATTA persisteva all'infinito, round dopo round — l'unico modo per toglierlo era cliccarlo o `Resetta Scontro`. La domanda però centrava un difetto reale nella direzione OPPOSTA: **uno SCATTA rimasto acceso è visivamente identico a uno appena armato**, quindi al giro successivo il GM lo rivede lampeggiare sul mostro e fa partire la stessa mossa una seconda volta.
  **Semantica adottata:** il telegrafo parte nel turno del mostro, quindi è SPESO quando quel turno finisce — si spegne all'`Avanza Turno` che lascia quel combattente, non prima. Un telegrafo RIARMATO nello stesso turno (1/2/3) non viene toccato, verificato con controprova. `Resetta Round` continua a riportarlo allo stato d'inizio round, quindi un turno avanzato per sbaglio si recupera.

- v4.82: **FIX — `Resetta Scontro` non ripristinava il ROSTER** (segnalato dal GM dopo l'uso). `resetEncounter()` rimetteva a posto lo STATO dei combattenti presenti in lista, ma la lista no: **un nemico o un PG rimosso durante lo scontro restava rimosso, e uno aggiunto restava**. Causa: da nessuna parte esisteva una memoria di com'era il roster all'inizio — il reset lavorava su `enc.combatants`, cioè sullo stato già modificato. Aggiunta `captureBaseRosters()`, che fotografa la formazione di partenza di OGNI scontro **una sola volta al caricamento** e mai su `switchTab`: rifotografare dopo le modifiche del GM le renderebbe la nuova base, che è esattamente il bug che stiamo togliendo. `resetEncounter()` ora ricostruisce la lista dall'istantanea — chi era stato tolto rientra, chi era stato aggiunto sparisce — e solo dopo azzera PF, `isDown`, telegrafi e note e ri-tira le iniziative dei mostri.
  **SCELTA DI DESIGN, non ovvia: le correzioni del GM sopravvivono al reset.** Per un combattente ancora in lista si conservano `name`, `ac` e `maxHp` — il nome scritto sopra "PG 1", la CA di un personaggio, un massimo di PF corretto perché la scheda era sbagliata. Sono fatti di sessione, non stato di combattimento: azzerarli renderebbe il bottone ostile da usare, e il GM dovrebbe riscrivere il party a ogni rerun. Si azzera solo ciò che appartiene allo scontro, iniziativa dei PG compresa (un rerun si ri-tira). Verificato in simulazione su 12 casi, incluso il doppio reset di fila (idempotente).
  **FORMATTAZIONE, trovata mentre correggevo:** §A24.2 e §A24.3 erano arrivate da 09 con la prosa **a capo forzato** a ~110 caratteri, mentre tutto il resto di 06 tiene una riga lunga per regola. Non è estetica: un bullet spezzato su tre righe può essere diviso a metà regola da un confine di chunk, che è esattamente ciò contro cui esiste quella convenzione. 25 righe di continuazione riunite ai loro bullet.

- v4.81: **THE TRACKER COMES BACK INTO 06 AS §A24, A SHARED RULE — and 09 is retired** (companion 00 v1.24 / cv28 / ov / lv). GM's call: «il tracker è una procedura e un formato, ha più senso averlo lì insieme al resto». **He is right, and for a reason I had missed when I argued for a separate file: `PART A — SHARED RULES (all assistants)` already existed for exactly this.** My earlier recommendation leaned on a retrieval argument that was weaker than the structural one.
  **THE RESEARCH FOUND A REAL DEFECT, BIGGER THAN THE REQUEST.** The tracker spec lived in `PART B — CAMPAIGN FORMATS` (§B9), yet **all three assistants have `/tracker`** — One-Shot and Loremonger were pointing at it from outside their own part. Worse, **ov and lv each still carried ~700 chars of the pre-template prose spec**, literal CSS fragments included, i.e. exactly what the canonical template replaced; and the ov row read *«for the most-recent statted encounter(s)»*, which is **the opposite** of the whole-module rule the GM wants and that §B9 already stated. Since the instructions beat the knowledge files, that row was silently winning.
  **STRUCTURE:** everything moves to **§A24 — COMBAT TRACKER (shared artifact, all assistants)** at the end of Part A: the artefact (§A24.1), the statblock panel spec (§A24.2), the controls documentation (§A24.3), and — the key choice — **all three SCOPES together in the same section**. A scope clause parked in §C4 or §D1 would never be retrieved by a `/tracker` query; keeping artefact + rules + scopes in one place means the single chunk that query must hit contains everything. Same co-location principle as the `[COND]` markers.
  **THE THREE SCOPES, which genuinely differ:** CAMPAIGN = the last beat only, one live tracker that replaces the previous; **ONE-SHOT = the WHOLE MODULE, one tab per act**, acts already played included (explicit GM requirement — a one-shot is prepared ahead and run in one sitting); LOREMONGER = the last encounter statted in that conversation, and only on an explicit request.
  **§B9 IS KEPT AS A TOMBSTONE, not deleted.** Every reference was updated (06 ×2 internal, 00 ×3, Handoff ×6, cv/ov/lv ×1 each → zero orphans), so nothing points there any more — but this system has already shown it reconstructs removed things from training memory (`/prepara` kept executing after every roster dropped it), so an explicit redirect is cheap insurance against a stale pointer. **CONSEQUENCE ON A STANDING CHECK: 06 goes 76 → 77 §-sections** (§A24 added, §B9 retained as the tombstone). The number was a damage detector, not a sacred invariant; the redirect is worth more than the round figure. The §B9 gap is NOT renumbered — §B10-§B28 keep their numbers, exactly as §A2 is an intentional gap, because renumbering would break dozens of cross-references.
  **DEDUPLICATION DURING THE MERGE.** The first assembly came out at 43.6 KB because §B9's rules and 09.0's rules had grown from the same source and now said the same things twice — `STRING SAFETY` was literally duplicated, and five more rules (emit verbatim, row counts, data contract, reuse-never-recalculate, example-is-a-shape) were saying one thing in two voices. Rewritten as ONE rule each: **§A24 lands at 40.3 KB**, and 06 at 302 KB.
  **HONEST CORRECTION TO THE PLAN'S OWN FORECAST.** I had predicted the ov/lv rewrite would SAVE ~1.4 KB on the always-in-context instructions. The first pass actually ADDED 685 bytes, because my replacement rows carried more content than the prose they replaced. Trimmed on a clean argument: **if the model is emitting the template it has necessarily retrieved §A24.1, and §A24.0's rules sit right beside it** — so the instructions only need what matters when §A24 is NOT retrieved. Final: ov −232, lv −128, cv −67. A modest saving, not the claimed one. Added while trimming, and genuinely new: *if §A24.1 cannot be retrieved, use the TEXT fallback rather than inventing a panel.*

- v4.80: **§B9 — THE '+/-' BAN IS REVERSED, and the row shapes diverge** (companion 09 v1.1 / cv27). The section said *«every field is a PLAIN editable input, never +/- buttons»*; the GM's own rebuilt tracker has exactly those buttons. **Recorded as a deliberate reversal, not worked around** — leaving the ban standing while the canonical template contradicts it is the silent-divergence class that already cost a batch on the instructions side. WHY IT DOES NOT REOPEN WHAT THE BAN PROTECTED: the old rule targeted +/- controls as a SUBSTITUTE for typing a value; here the HP field stays fully typeable (that is how the GM resets it) and the buttons are an ADDITION — type the damage, press a sign, or hit Enter. Added with it: all numeric fields are PLAIN TEXT with `inputmode="numeric"`, because the native spinner arrows are too small to hit in a dim room, and they commit on CHANGE so editing never steals focus.
  **§B9 RESTRUCTURED FOR RETRIEVAL, and pruned.** The section had grown two mega-paragraphs (`BEHAVIOR` at 1.785 chars and `FORMAT` at 2.713) holding five or six binding rules each — the same shape the §B2 pass already fixed, where a chunk boundary can split a rule from its consumer. Both are now one-rule-per-line bullets: 21 units, none over 800 chars. Two real redundancies removed while doing it: "the look comes from the template" was stated twice (opening clause and again in FORMAT), and step 5 restated MULTI-ENCOUNTER TABS almost verbatim — its only unique content was the no-statted-fight case, which survives. Net **−310 chars despite adding back two details the restructure had dropped** (the "never ask which fight" instruction and "self-contained HTML, inline CSS+JS", both re-homed where they belong).
  **PC AND MONSTER ROWS ARE NO LONGER THE SAME SHAPE** — stated explicitly so a partial retrieval of 09 still lands right. A PC ships `init` and `ac` EMPTY (the GM fills both; the assistant does not know a PC's AC) and `hp`/`maxHp` at 0, never rendered — players track their own hit points, while the GM needs the AC to roll against and an A TERRA toggle. A monster ships a pre-rolled `init`, real numbers, `initBonus` (the DEX mod, used by *Resetta Scontro* to re-roll) and a telegraph counter. `isDown`/`telegraph`/`notes` always ship `false`/`null`/`""`. New step 3c: `notes` ships EMPTY and is TRANSIENT STATE, not a compressed stat reminder — the statblock panel took that job in v1.0, and pre-filling it duplicates the panel on every tracker. Column headers follow the GM's build: `Stato Vita (PF)` and `Condizioni & Effetti`.

- v4.79: **§B9 SPLIT — the artifact moves to 09, the BEHAVIOUR stays here** (companion 09 v1.0 / 00 v1.23 / cv26). The section no longer describes how the tracker LOOKS: the CSS-in-prose is replaced by a pointer to 09 plus the invariants that must survive a partial retrieval of it (always dark with `html, body { background:#1b1d21; color:#e8e6e3 }` and `min-height:100vh` so no white gutter frames it; plain editable inputs, never +/- buttons; descending sort ONLY on initiative commit; monster vs PC told apart by background TINT, never by text colour; the six columns; the combatant object shape). Section went 5.3 → 5.9 KB — it did NOT shrink as planned, because the space freed by the CSS prose was taken by the two new rules below.
  **SCOPE IS NOW DIFFERENT PER MODE — the conflation was the bug.** §B9 said "the most recent beat/act" and treated BEAT and ACT as one unit. GM-observed consequence: in CAMPAIGN the tracker accumulated fights from earlier beats — already resolved, wasted tokens, and clutter in the one panel being read mid-fight. Now explicit: **CAMPAIGN = the LAST BEAT ONLY** (several statted fights inside that one beat still all belong — a dungeon's mid-boss + boss are the same beat); **ONE-SHOT = the WHOLE MODULE, one tab per act**, which is the behaviour the GM wants and which must not regress. Added with it: **ONE LIVE TRACKER AT A TIME in campaign** — a new `/tracker` REPLACES the previous panel instead of adding a second (stated as intent, since whether the platform updates the artifact in place or emits a new one is outside our control).
  **STRING SAFETY sharpened** from "embed names safely" to the concrete rule: every data string uses DOUBLE QUOTES, no escaped apostrophes at all — because the failure mode is not a garbled name, it is a BLANK ARTIFACT.

- v4.78: **SECOND LIVE TEST OF THE INVERTED CONDENSATION** (companion cv25). **PASSED and now considered stable:** vignette separation (the 7-quest bridge kept `That Weight` and `Not My War` in their own sentences, the regression v4.77 fix (2) targeted), the whole-span `[Info GM]` (all seven listed with the played STOP last), and — the big one — the **RE-HOOK**: `/esito` emitted the ACK plus its new pre-warning line, and the following `/continua` anchored on `Lord of Crags` ITSELF rather than the downstream `All Good Things` that presupposes Titan's defeat, with no retcon (the party's departure stands; the kobolds finish the ritual, Titan rises, the aether drains, Y'shtola holds the portal, tremors reach Ul'dah). Also correct: no notice on the isolated `Sylphic Studies` (N=1).
  **(1) THE NOTICE MISCOUNTS WHILE THE BRIDGE DOES NOT — fixed by changing WHAT the line must say.** Observed again: the notice printed '6 quest condensabili' where the run holds SEVEN, yet `/riassumi` from the same cursor produced `(Ponte narrativo 7 tappe)` and listed all seven correctly. The asymmetry is the diagnosis: **a bridge must ENUMERATE the quests in order to write them; a bare count need not**, so v4.77's instruction to 'count, do not estimate' had nothing forcing it. The notice now names BOTH ENDPOINTS — `da <PRIMA> a <ULTIMA> — N quest condensabili, poi si gioca <STOP>` — because the endpoints cannot be named without looking them up, and once both are located N is just the entries between. Output-forcing by construction instead of by exhortation.
  **(2) AN ACTIVE SUBQUEST DID NOT BLOCK `/riassumi`.** GM-found: with `[C]` ATTIVA the command bridged SEVEN MSQ quests and advanced the MSQ cursor, while the MSQ was PARKED and `/continua` would have advanced the subquest (§B22). v4.76 had suppressed the NOTICE for an active subquest but never said what the COMMAND does there — the announcement was covered, the action was not. Now: `/riassumi` takes no game action while [C] is ATTIVA, one line pointing at `/riprendi MSQ`. Consequence had it shipped: content the table never reached consumed while they were elsewhere, and a later `/salva` writing it as played.
  **(3) `/prepara` STILL RAN, and the GM's call is to stop fighting it.** The generic unrecognised-command rule was live in cv24 (always in context) and did not stop it — the model reconstructs the command from its own training, not from our files. GM decision: remove every remaining MENTION so nothing feeds it back through retrieval, and accept that nothing explicitly refuses it (they simply will not use it). Rosters are now stated as **COMPLETE and CLOSED** without naming any removed command, in 06 §B1/§B21, cv25 and the Handoff. HONEST LIMIT, recorded so it is not re-litigated: this reduces retrieval noise but is NOT expected to stop the behaviour, and it slightly weakens the refusal path — the trade was accepted deliberately.
  **(4) THREE OUTPUT SLIPS, each fixed by a GENERIC rule rather than a patch.** **(4a) QUEST TITLES STAY ENGLISH, ALWAYS** — observed `[MSQ — Studi sulle Silfidi (Sylphic Studies)]` in one beat while others in the same session kept the English title. A quest name is an INDEX KEY, not prose: G1's translate-by-default governs places, factions and things, never quest titles, and a translated title cannot be matched back to 08, which makes the cursor unverifiable. **(4b) IMAGES ONLY FOR WHAT IS ON SCREEN** — observed `🖼️ Immagine: Riol` in a beat where Riol had only SENT a courier and never appeared; a portrait tells the GM someone is present. Someone merely named or mentioned gets no image. **(4c) THE SPINE'S CONCRETE NOUNS SURVIVE COMPRESSION** — the cached spine reads 'defeat the Goobbue near the JUGGERNAUT' (an Allagan war machine) and the bridge rewrote it as 'il relitto di un mercantile incagliato', a shipwreck; the same passage wrote 'Gobbue' thirteen times for 'Goobbue' (all 8 source occurrences spell it correctly). Compressed prose is exactly where this drifts, because summarising invites re-wording — so a vignette may SHORTEN a quest but never RENAME its things. Checked and NOT an error: `Musica: A New Hope` for Ul'dah is a valid track per the 08 OST table, and 08 says nothing about Byrglaent's role, so 'sommelier' vs 'nobiluomo' is an internal inconsistency across runs, not a canon breach.
  **(5) A PASTED SAVE AUTO-PLAYED A FULL TRIAL — fixed by changing the FORM of the rule, not its content.** Confirmed by the GM: no command was typed; the save block alone produced a complete Titan trial (stat block, loot, milestone) with no `Save caricato:` line and no orientation. LOAD-ONCE and POST-LOAD NEUTRAL already forbade exactly this and were ignored, so restating the ban would have achieved nothing. What was missing is that both were written as DESCRIPTIVE PROSE buried in long lines. Replaced with the two devices a weak model actually follows: a LITERAL OUTPUT TEMPLATE for the load turn (anchor echo · 1-2 orientation lines · `Prossimo step wiki` · the notice if it applies · STOP) placed at the TOP of the instructions in the ROLE block, and a TESTABLE SELF-CHECK — 'if your reply to a save block contains a `[MSQ`/`[VIAGGIO` tag, a stat block, read-aloud prose, an image/music line or an `[Info GM]` line, you have already broken this: delete it'. A detectable condition beats an abstract prohibition.
  **(6) PRE-COMMIT EXEMPLAR PRUNE — anti-bias pass on this batch's own additions.** GM's concern, and the same one that forced the §A1 exemplar cull: a concrete example can make a model over-fit to the CASE instead of applying the RULE. Criterion applied: an example earns its place ONLY when it disambiguates a boundary the abstract statement cannot fix; if the rule already reads unambiguously, the example adds no information and only narrows it. The batch had added **12** failure shapes — cut to **5**. REMOVED as pure over-fitting risk (rule left intact, reason kept): the image example (an absent NPC named by a courier), the quest-title example (two specific titles), the spine-nouns example (a specific landmark and a misspelt creature), the active-subquest example (an INVENTED test subquest, worse than useless as a pattern), and one of the TWO N-counting examples — the same event had been narrated in both §B1 and §B2, and duplicating an EXAMPLE is worse than duplicating a rule. GENERALISED instead of deleted where the failure was genuinely non-obvious: 'two same-flavoured errands joined by an and read as one errand' (was: two named quests), and 'a notice stating only a COUNT undershot the run at every quest boundary while a BRIDGE from the same cursor got it right' (was: named quests + counts) — that asymmetry is the whole rationale for naming the endpoints, so it survives without names. KEPT DELIBERATELY: the Titan→Ultima causality note, because it is a RATIONALE RECORD for the never-skip policy and sits beside a set-based definition of 'fundamental' that an example cannot narrow; and the anchor example, because 'an anchor that PRESUPPOSES the bypassed content' is close to inapplicable in the abstract. Untouched: exemplars already shipped in v4.75 (they carry measured exposure figures and were GM-validated). VERIFIED SEPARATELY: every fix in this batch is GENERIC — any active subquest, any run, any quest title, any off-screen NPC, any retired command — with no per-quest patching anywhere.
  **TESTING METHODOLOGY, recorded because it explains the fix above.** The GM tests on **Gemini 3.6 Flash deliberately, as the FLOOR** — the weakest model the system might realistically run on — so anything that survives there is safe everywhere. This makes it worth SORTING failures rather than chasing them all: (a) ABSENT OR AMBIGUOUS RULES, where the weak model merely exposed a real hole sooner (the subquest block, the N miscount, the anchor selection) — fix the rule; (b) RULES PRESENT BUT IN THE WRONG FORM, where the content is right and only the shape fails under a weak model (the load auto-play) — fix by TEMPLATE + SELF-CHECK, never by repeating the ban; (c) CAPABILITY LIMITS, where the model reconstructs behaviour from its own training regardless of the files (a retired command still executing) — do not spend rules on these, the fight is unwinnable at the floor and the cost is file bloat.

- v4.77: **FIVE FIXES FROM THE FIRST LIVE TEST OF v4.76** (companion cv24). What PASSED and needs no further work: the pillar guardrail (`/riassumi` before `Lord of Crags` printed one line and played nothing), the ATTIVA-subquest suppression of the notice, the notice appearing at load and at beat end, and mid-run `/riassumi` bridging the remainder with the correct STOP played in full.
  **(1) COUNTING N WAS WRONG AT A QUEST BOUNDARY — and it did not stay contained.** With the cursor on `The Things We Do for Cheese` the notice read '6 quest condensabili' where the run holds SEVEN; the not-yet-started next quest had been excluded because the old wording ("including the current one if unfinished") does not describe a quest that has not begun. Worse, it was UNSTABLE — the same cursor reloaded later counted correctly. Reworded to count **from and including THE NEXT ONE THE CURSOR WILL PLAY**, which is unambiguous at both a boundary and mid-quest, plus an explicit instruction to COUNT INDEX ENTRIES rather than infer the number from prose.
  **(2) A VIGNETTE WAS LOST — direct consequence of (1).** The undercount set the vignette budget, and the 6-quest bridge emitted 5 passages, fusing `That Weight` (the midge cull) and `Not My War` (the jungle-coeurl hunt) into one clause. This re-opened the exact failure v4.75 fix #4 exists to prevent. Added: TWO QUESTS NEVER SHARE A SENTENCE, and when the vignette count and the quest count disagree **the quest count wins — lengthen, never trim**.
  **(3) `[Info GM]` DECLARED ONLY THE STOP.** A bridge over six quests closed with 'chiude It Was a Very Good Year' alone, leaving the whole bridged span undeclared — v4.75 fix #5 regressed, and it is the one that corrupts `/salva`. Added the explicit shape: the STOP is the LAST ITEM of the list, never the whole list.
  **(4) A REMOVED COMMAND STILL RAN — the real defect was a missing rule, not a missing deletion.** `/prepara` had been purged from every roster, yet it produced a full study beat, because **nothing anywhere said what to do with an unrecognised slash command**, so the assistant reconstructed the old behaviour from training memory. Deleting a command is not sufficient on its own. Added to §B1 and to the cv COMMANDS block: an unlisted `/word` is NEVER executed and NEVER improvised — one line naming the closest real command, no game action, no beat, no tag. This closes the whole class (removed commands, typos, invented ones), not just `/prepara`.
  **(5) `/riaggancio` RE-HOOKED INTO A CONTRADICTION, and the policy behind it was wrong.** After an `/esito` declaring the party had refused Titan and left for Ul'dah, `/riaggancio` anchored on `All Good Things` — whose FIRST step is *'report Titan's defeat to R'ashaht Rhiki'*. Two separate defects. **(5a) Anchor validity:** 'nearest reachable anchor' was never defined, so the model took the next chain entry. Now: the anchor is the EARLIEST NOT-YET-DONE FUNDAMENTAL point the sequel requires — `Lord of Crags` ITSELF here — and never one that PRESUPPOSES the bypassed content. **(5b) Policy — REJECTED DESIGN, do not re-propose:** I had recommended DEFERRING skipped fundamental content as a tracked 'debt' with a new save field. The GM rejected it on decisive grounds: the ARR MSQ is tightly CAUSAL, so a hole does not sit still — if Titan is never re-summoned and defeated, the Ultima Weapon has no Titan aether to absorb, and without every Crystal there is no Blessing to survive Ultima. The deferrable set is therefore nearly EMPTY, and the design was machinery (plus save bloat, which the GM had removed once before) for an empty set. Replaced by: **fundamental content is NEVER skipped** — the same list the `/riassumi` guardrail protects (pillar · instanced duty · manifest-pinned cutscene), ONE LIST TWO CONSUMERS, never a runtime judgement. `/riaggancio` brings the party BACK, honouring the refusal as a DETOUR and dramatising the world's pressure until returning is their own move; it never retcons and never scolds. **No save field was added.**
  **(5c) 'NOT FUNDAMENTAL' IS NOT 'DISPOSABLE'** — caught by the GM against my own first formulation: anchoring on 'the first fundamental point' would silently drop the minor quests in between, which still carry NPCs, information and setup. So the bypassed span is **BRIDGED, not skipped**, with the same countable one-vignette-per-quest floor as §B2. Two clarifications this needs: the `[COND]` markers DO NOT APPLY here (the span is bridged in full, marked or not, and the bridge does NOT stop at the first unmarked entry — that stop rule belongs to `/riassumi`), and the content must be **RE-ROUTED to where the party actually is** (a report, a messenger, an encounter on the way back) rather than replayed as though they had been present. Whatever genuinely cannot travel is declared lost in `[Info GM]`.
  **(6) `/riaggancio` REMOVED — the re-hook is a MODE of `continua`, not a command** (GM's idea, and it exposed a hole in (5)). The GM asked: if `/esito` must always be followed by `/riaggancio`, what does a plain `/continua` do in between? Answer: it was **UNDEFINED** — the cursor still pointed at the cached next quest, the party was somewhere else, and §B2 only said 'follow what actually happened', which is an aspiration and not an instruction. So the model would improvise, which is precisely what `/riaggancio` had been introduced to prevent. Fixed by defining it: when the register records a divergence the chain cannot absorb, **the next beat `continua` plays IS the re-hook** (§B3). That is not a new meaning — `continua` has always meant 'play the next beat from the ACTUAL play state', and a diverged state makes the re-hook that beat. With `continua` doing it, a separate command performs the SAME action under a second name, i.e. the alias ONE NAME PER ACTION forbids and the same ground on which `/gioca`, `/prepara` and `/nota` were removed in v4.76 — so it goes. §B3 SURVIVES as the procedure, retitled from a command to a mode. REJECTED ALTERNATIVE (do not re-propose): having `/esito` itself play the re-hook — it would break the note-vs-beat separation and, worse, would misfire on the majority of reports (a PC down, potions spent, a failed check) that need no re-hook at all; a note command that sometimes hands back a beat is a trap. GUARD AGAINST SURPRISE: since the re-hook is a large beat that moves the party, the `/esito` ACK now gains ONE line when it registers a canon divergence — `Deviazione registrata. Il prossimo /continua riaggancia a <ancoraggio> (<motivo>).` — GM-facing state, the same device as the connective-run notice.
  **(7) PRE-TEST AUDIT of the uncommitted batch — four defects caught before they ever ran.** **(7a) A rule of mine turned a harmless gap into a live bug:** the new 'unrecognised slash command is never executed' was written as 'not in THIS roster', but 06 is SHARED and the Loremonger has dozens of commands of its own (`/mostrami`, `/musica`, `/lore`, `/pg`…), none in §B1's campaign roster — the rule would have made the Loremonger refuse its own command set. Now explicitly SCOPED to the ACTIVE assistant's roster. (Checked and fine: `/carica`, `/load` and `/subquest` appear only as explicit negations, so the rule agrees with them.) **(7b) A contradiction between the instructions and 06, on the side that WINS:** the cv row still carried the command-era line 'if the story has NOT diverged it takes no game action and says so in one line' — true of the old `/riaggancio`, FALSE now that the re-hook is a mode of `continua`, where an undiverged story simply gets an ordinary beat. A model following the instructions would have made `/continua` do nothing on a normal turn. **(7c) Structural:** the RE-HOOK had been left as a row with no command inside a table whose stated schema is one row per command; folded into the `/continua` row as its single branch, and the duplicated `[Info GM]` sentence in the `/riassumi` row merged. **(7d) Broken cross-reference:** §B3 pointed at '§B21 DIVERGENCE ACK' but the ACK lives in §B1.
  **RAG PASS on the same batch.** The notice FORMAT STRING existed only in 06 §B1 — the instructions said a notice was due but never showed its shape, so a turn that failed to retrieve §B1 would know an obligation it could not satisfy; the literal line now sits in the always-in-context instructions. COUNTING N was reachable only from §B2 while its main consumer (the BEAT END notice) lives in §B1, the exact split-retrieval risk the marker co-location principle exists to prevent — the rule is now stated compactly in BOTH places, with the failure shape kept in §B2 only. And the two mega-bullets that had grown past 4.5K and 4.0K characters were split so COUNTING N and the `/riassumi` GUARDRAIL are independently retrievable units rather than tails of a long paragraph.
  **TEST-FIXTURE ERROR (mine, recorded so the scale-(ii) test is not believed to have passed):** the save I built to exercise scale (ii) used `A Final Ignominy`, assuming index order equals chain order. It does not — `It Was a Very Good Year`'s cached Next points straight at `In the Company of Heroes`, routing around it, so the model was RIGHT to skip it and **scale (ii) was never actually tested**. Correct fixture: `Sylphic Studies` (isolated `[COND: parallel]`, previous `We Come in Peace` and next `First Impressions` both unmarked, and genuinely on the Next chain) — which is also the canonical example the rules cite.

- v4.76: **CONDENSATION INVERTED TO GM-TRIGGERED + COMMAND-SET CLEANUP** (companion 08 v3.35 / cv23). Two strands in one batch because they touch the same regions (§B1 roster + BEAT END, §B2, §B21) and reopening those twice risks the fused-bullet damage already seen in §A1.
  **(A) THE INVERSION — `/continua` PLAYS, `/riassumi` CONDENSES.** GM's design, adopted over mine. I had proposed keeping condense-by-default and adding a notice plus a restored `/gioca`; the GM proposed inverting the default and keeping only `/riassumi`. **The GM's version is better and this is why:** my objection ("boredom arrives too late") only held against a version WITHOUT the notice — with the notice the choice happens BEFORE the time is spent in both directions, which was my own decisive argument. And it wins on three counts: one fewer command (`/gioca` never returns, in either direction — the v4.59 removal is now moot rather than reversed); `/riassumi` becomes MONO-SEMANTIC (always "condense from here to the end of the connective stretch", identical at the run's start and mid-run); and **there is NO MODE STATE** — my design armed a mode with `/gioca` that `/riassumi` disarmed, which would have needed persisting in the save or a mid-run reload would lose the choice. Here the run is re-derivable from the cursor + static index at any moment, so §B17 gains no field. **The 542 `[COND]` markers were NOT touched** — they stopped triggering and now only DEFINE a run's extent (start, stop, contents). ACCEPTED COST, recorded so it is not re-litigated: a reflexive `/continua` without reading the notice plays the connective quest in full — but it is PLAYED, not skipped, and the next `/riassumi` compresses the rest.
  **THE TWO SCALES SEPARATE (this is what makes the inversion clean):** scale (i) INTER-QUEST (a run of 2+ → one bridge) becomes GM-triggered; scale (ii) INTRA-QUEST (a `[COND: parallel]` cluster delivered as one passage) stays AUTOMATIC AND SILENT under `/continua`, because it is a GRANULARITY rule, not a skip — it is what SUB-BEAT GRANULARITY already wanted. The PRECEDENCE clause is kept but RESCOPED to `/riassumi`, where the `Free Trade` failure shape (22 of 114 runs begin with a `parallel` marker) is still a live risk; under `/continua`, playing Free Trade as its own beat is now CORRECT and the old failure text was rewritten to say so.
  **CONNECTIVE-RUN NOTICE (new):** `⏭️ Tratto connettivo: N quest condensabili fino a <STOP> (~X min giocate / ~Y riassunte)`, at BEAT END after `[Info GM]` and again at the END OF THE LOAD ORIENTATION. GM decision: **state only, no command words** — that is exactly why it does not fall under the dropped end-of-beat menu, whose ban "covers COMMAND WORDS in the footer, not GM-facing state" (same standing as `[Info GM]` and the 🧭 line). The load variant answers a case the GM raised: *saving mid-connective-stretch because we chose to play it — how do I know at reload?* It costs no save field. CONDITIONS, deliberately few so it stays reproducible: fires at N ≥ 2, ONLY on a cursor-advancing beat (never the transient `/viaggio` or `/riposo`), and NEVER while `[C]` is ATTIVA — there `/continua` advances the SUBQUEST (§B22), so an MSQ notice would point the GM at something the command will not touch. The minute figures are ESTIMATES like every other beat estimate; 08 carries no per-quest minutes.
  **COUNTING N (binding, closes a known ambiguity):** N = the `[COND]` quests still to traverse to the first unmarked one, INCLUDING THE CURRENT ONE IF UNFINISHED — so it is defined identically whether the cursor sits at a quest boundary or mid-quest, for the notice, the vignette floor and the span alike.
  **GUARDRAIL ON FREE-FORM `/riassumi` (new, and the most important consequence of the inversion):** the command went from RARE override to PRIMARY trigger, so it will be pressed often — and pressed one beat late it would silently compress a pillar or a dungeon. It now NEVER compresses a pillar, a quest naming an instanced duty, or a manifest-pinned cutscene (08.1); it stops BEFORE it, and if the very next quest is already one of those it takes NO game action and prints one line. Doing nothing beats asking: §B1 makes this a single-command executor.
  **PARTIAL BRIDGE = PARTIAL SPAN:** a mid-run `/riassumi` declares in `[Info GM]` only the quests THAT bridge consumed — re-declaring already-played ones inflates the span and can make `/salva` write a wrong `[A]`. **`[CUT]` IS INVISIBLE to a run:** the chain skips it, so it neither breaks contiguity nor counts toward N.
  **(B) COMMAND-SET CLEANUP.** **`/prepara` and the campaign STUDY mode REMOVED.** Decisive reason: the instructions already state the ONLY persistence is the save block written on `/salva`, so "prepare without dirtying the save" is obtained by opening a throwaway chat, using `/continua`, and never saving — the command defended against a risk the architecture had already eliminated, and its content was not even lighter (the rules required the same density as `/continua`). Two reasons that bite now: generation is NOT deterministic (one goobbue encounter yielded three different stat blocks across three runs), so a prepared beat is not the beat `/continua` will produce at the table; and the new design decides play-or-condense AT THE TABLE, so a pre-generated stretch is waste if the table picks the bridge. Removed with it: the STUDY PREPARATION CURSOR (a second cursor independent of the play cursor), the `[PREPARATO NON GIOCATO]` register state, the `prossimo da preparare:` end-marker, and ~20 STUDY branches. §B21 retitled `CAMPAIGN PLAY & ACTUAL-PLAY CAPTURE` (the plural "MODES" and "The MODE IS SET BY THE COMMAND" no longer meant anything with one mode). **One-Shots are untouched** — they are prep-only but run on `/genera` + `/atto X` with ACTS, and the preparation cursor was explicitly "Campaign only"; the register's "(a) the prepared act / between acts" clause was KEPT and re-scoped to §C rather than deleted with the rest.
  **`/nota` MERGED INTO `/esito`.** Found in audit: all five occurrences in 06 treated them as a pair with IDENTICAL behaviour (register, 1-line ACK, never a beat), cv22 listed them on ONE line with ONE description, and **no line in any file said what one did that the other did not** — a pure alias, which §B1's own "ONE NAME PER ACTION — NO ALIASES … no 'which one did they type' branch" forbids. The FUNCTION is load-bearing and untouched: it is the only channel by which reality at the table contradicts `LIVE DEFAULT = GIOCATO`, without which a wipe or a retreat would vanish silently. `/esito` survives with scope explicitly broadened to ANY fact for the save, not just fight outcomes.
  **`/riaggancio` ADDED + §B3 rewritten.** §B3 was titled `RE-HOOK TO THE MSQ` but was a two-line stub with **no trigger at all** — no command invoked it. And `/riprendi MSQ` is NOT that function (it suspends an active subquest, §B22): when `/torniamo alla MSQ` was renamed, the name survived and the meaning did not. It matters because only a slash command produces a beat, so there was literally no way to ask for a story that had diverged to be brought back on canon. §B3 is now a procedure reusing the bridge machinery: read the divergence from the register → pick the nearest canonical anchor still reachable AHEAD → play one connective beat that reaches it. Hard rule: **NEVER retcon** what the players did (an unavailable canonical NPC's role passes to another canonical NPC or their organisation, §A5). Declares chosen anchor + skipped span in `[Info GM]`. Not diverged = no game action, one line.
  **HOUSEKEEPING:** the in-file `Version` headers had fallen behind CHANGELOG and the commits (06 said v4.70, 08 v3.33, 05 v1.99) — realigned to v4.76 / v3.35 / v2.02. `/gioca` also purged from the Handoff's two command rosters, where it had lingered since v4.59.

- (08 v3.35) **MARKERS UNTOUCHED, SEMANTICS RESTATED.** All 542 `[COND]` + 1 `[CUT]` are byte-identical to v3.34 — the inversion moved the TRIGGER, not the data, which is the whole reason the exhaustive marking pass did not have to be redone. The 08.0 legend now states that condensation is GM-triggered via `/riassumi` and that the markers DEFINE a bridge's extent (start · stop at the first unmarked quest, played in full · contents); `REGOLA D'ORO: NON marcato = SI GIOCA` is unchanged verbatim. Also fixed, found only by auditing the plan against the file: **L.604 carried the command** (`stops offering 'continua'/'prepara' past 6.0`) — the first draft of the plan had claimed 08 needed only the legend edit. Left deliberately intact: `launch preparations` (08 L.4165) and `preparation only` (05 L.185) are English nouns, not the removed command — a blind grep-replace on "prepara" would have corrupted both.

- (cv23) **INSTRUCTIONS REWRITTEN — the file that actually changes behaviour.** Recorded because it was the near-miss of this batch: the first draft of the plan listed only the `.md` knowledge files, but `Instructions_Campaign.txt` L.66 hard-coded the OLD rule (`auto-condense of low-agency runs is AUTOMATIC on /continua`), and the custom instructions sit at the TOP of context and always present while 06 arrives via RAG — 08 itself states that in a conflict the Instructions WIN. Editing 06 alone would have left the feature dead, with a confusing intermittent symptom depending on what the RAG retrieved. Changed: the STORY-BEAT roster (`/continua, /riassumi, /viaggio, /riaggancio` — `/riassumi` had never been listed despite emitting an `[MSQ` tag), `/continua` (always plays + closes with the notice), `/riassumi` (sole condensation trigger, mid-run remainder, guardrail), LOAD (notice when the save lands inside a run), `/esito` (broadened, `/nota` gone), new `/riaggancio`; `/prepara` row deleted. `Instructions_Loremonger.txt` and `Instructions_OneShot.txt` verified to contain nothing about condensation — untouched, no lv/ov bump.

- v4.75: SEVEN FIXES FROM TWO ROUNDS OF LIVE TESTING of the `[COND]` condensation (saves built to land the cursor immediately before a marked run: ShB 'The Best Way Out' → a 9-quest run, ARR 'The Things We Do for Cheese' → a 7-quest run). Each carries its OBSERVED failure shape so it is not re-litigated. **(1) PRECEDENCE — SCALE (i) ALWAYS WINS:** a `[COND: parallel]` entry that BEGINS or sits INSIDE a run of 2+ is bridged WITH the run; the intra-quest scale (ii) applies ONLY to an ISOLATED marked entry, and the marker TYPE never decides whether the run fires. ROOT CAUSE of the first failed test — `/continua` played `Free Trade` as a full social beat (merely condensing its internal Mord-questioning cluster) instead of opening the 9-quest bridge it starts; the `parallel` type had been read as 'play this quest, compress inside it'. Measured exposure: **22 of 114 runs** begin with a `parallel` marker and would all have failed the same way. Retested: the bridge fired. **(2) THE BRIDGE TAG IS GM-FACING AND PERMITTED** (GM decision, reversing a first attempt to ban it): the GM WANTS the montage announced so they can frame the reading for their players, so the bridge names itself in its beat TAG — never read aloud, exactly like every other tag — while meta INSIDE the player-facing prose (headings such as 'Il Ponte Narrativo:', 'Riassunto', or any explanation of why it was condensed) stays banned. **(3) THE ARROW POINTS AT THE STOP** and the estimate states the vignette COUNT plus the stop's own type: observed a bridge tagged '… → Battle Scars' (the last CONDENSED quest) typed only '(Ponte narrativo · ~15-20 min)' while the beat went on to play 'It Was a Very Good Year' in full, goobbue encounter included — the GM got no warning a fight was coming. Correct shape: `[MSQ — Ponte narrativo: <prima condensata> → <STOP giocata in pieno>]` + `(Ponte narrativo N tappe + <tipo dello STOP> · ~N min)`. **(4) ONE VIGNETTE PER CONDENSED QUEST — COUNTABLE**, replacing the length-conditional 'LONG RUNS DO NOT COMPRESS HARDER' which bit at 9 quests but not at 7: N bridged quests owe N recognisable vignettes, counted BEFORE emitting, a longer run making the bridge longer and never denser. Fixed the twice-dropped `Not My War` (the jungle-coeurl hunt for Drest); the retest returned 7/7. **(5) [Info GM] DECLARES THE WHOLE CONSUMED SPAN** — save integrity: a 9-quest bridge closed with only 'chiude Free Trade; chiude Full Steam Ahead', leaving 8 intermediate quests undeclared, so a '/salva' could write an [A] step not reflecting the real span and the next LOAD could resume INSIDE the already-bridged stretch and replay it. Retested: all 8 quests named. **(6) TRAVEL LINE MEASURED FROM THE POST-BRIDGE POSITION**, and omitted when the next beat happens where the party already stands — observed a bridge that walked the party Mord Souq → Twine → the mines → Amh Malik and fought there, then still offered '🧭 Viaggio … verso Amh Malik'. Retested: correctly omitted. **(7) §B6 TARGET GdS IS DERIVED, NEVER CHOSEN** — it follows from PARTY LEVEL + the encounter's CONTEXT DIFFICULTY TIER (§B11/§B13/05 Ch.10.2), both deterministic, so the same encounter at the same beat yields the same GdS on every run (§B2 STORY-FLOW FIDELITY), and every number then obeys that band. Observed across THREE runs of ONE fixed beat (the goobbue guarding the Bacchus vine, 4 PG Lv5): 'GdS 3 · CA 13 · PF 85' (dice math also wrong — 10d10+40 = 95), then 'GdS 5 · CA 15 · PF 115', then 'GdS 3 · CA 13 · PF 114' — three tiers for one encounter, the last carrying nearly double its declared band's HP. TEST VERDICT: the mechanism itself is proven on three runs (7, 9 and 7 quests) with the correct STOP every time; what remains is prose quality, which surfaces better in play than in simulation. 06 stays 76 §.
- v4.74: DETERMINISTIC MSQ CONDENSATION via pinned `[COND]` markers + wiki-truth fixes (companion 08 v3.34). GM doubts: (1) auto-condensing fetch/light-social quests, (2) MSQ-flow precision. THREE FINDINGS. (A) §B2's auto-condense is mature but its classifier is UNFED — the 08 index annotates ~12% of entries, so most quests are classified from the TITLE, and the rule's own safe default ('when unsure, PLAY it') biases it to UNDER-condense (the recorded sylph failure). (B) DECISIVE, verified on live ConsoleGamesWiki pages: THE WIKI CANNOT DISCRIMINATE IMPORTANCE — `On to Summerford` (connective) and `Call of the Sea` (opens the Scions arc) have the SAME Steps shape ('Speak with X at Y'). TWO candidate designs were built and BOTH REJECTED on this evidence — do NOT re-propose them: (i) structural stop-to-stop condensation (stops are ~1 per 4 quests, so blind runs would swallow unpinned decisions/first-meetings), (ii) an evidence-based classifier reading the fetched step list (would have condensed Call of the Sea). What the wiki DOES expose reliably is DUTY presence (`It's Probably Pirates` names Sastasha in Steps + Rewards + dialogue). (C) §A14 factually wrong: it claimed CGW gives 'a single unambiguous Next Quest' — live pages list SEVERAL incl. unlocked sidequests (On to Summerford 2, Call of the Sea 5); the 08 cached Next is authoritative and the cache WINS. RESOLUTION (GM call): classify ONCE as pinned DATA instead of inferring per turn. SAFETY PROPERTY that makes an exhaustive pass acceptable: mark ONLY condensable quests — **UNMARKED = PLAYED, ALWAYS** — so any gap/oversight/uncertainty costs table time, never content (the cost asymmetry: over-condensing destroys content irreversibly, under-condensing only spends minutes). §B2 now: markers DECIDE (lookup, never re-classified at runtime, never added at runtime), at TWO SCALES — (i) inter-quest, a run of 2+ consecutive `[COND]` becomes one bridge; (ii) intra-quest, a `[COND: parallel]` quest condenses its internal micro-objective cluster EVEN ALONE (found during the pilot: the three sylph lessons live INSIDE one quest, so the 2+ run would never have fired — without this the documented failure repeats). The semantic classifier is DEMOTED to a fallback for unmarked content (One-Shot / Loremonger / unmarked expansions), conservative behaviour unchanged. Also fixed: §A14 Next-Quest caveat + an honest statement of WHAT IS CACHED (order+name+resolved Next for every quest; giver/step spine only where visibly shown), and §B2 QUEST-CLOSE=SPINE-EXHAUSTED reformulated — it told the model to 'COUNT the 08-index steps', data absent for most quests, so it now counts cached steps WHERE PRESENT and the fetched list otherwise, and never closes a quest whose step list could not be established. 06 stays 76 §.
- (08 v3.34) **MARKING PASS COMPLETE — ALL FIVE EXPANSIONS (544 markers + 1 CUT).** HW→EW added on top of ARR, classified from the CACHED step spines (unlike the ARR city openings, HW/SB/ShB/EW carry giver + steps on every entry, so no per-quest wiki fetch was needed). Per expansion — quests / marked / played / condensed-in-bridges: **ARR 257/117/140/93 in 29** · **HW 139/93/46/85 in 24** · **SB 145/107/38/100 in 21** · **ShB 157/113/44/104 in 24** · **EW 108/72/36/64 in 14**. Totals: **806 quests → 304 played in full, 446 condensed into 112 bridges**. The later expansions condense more heavily than ARR because their MSQ is structurally denser in connective relay chains between set-pieces. Longest runs: the Wineport banquet (7, ARR), the Amh Araeng mine chain and Rak'tika/Fanow stretch (8 each, ShB), the Ruby Sea magatama chain (7, SB), the Brume and moogle-trial chains (7 and 6, HW). PROTECTED EVERYWHERE (never marked): every dungeon, trial and solo duty; every manifest-pinned cutscene/reveal; first appearances of arc-anchor NPCs (Estinien, Hilda, Matoya, Ysayle, Hien, Lyse, Gosetsu, Tesleen, Runar, Emet-Selch, Venat, Hythlodaeus, Meteion, Jullus, Varshahn, Erenville…); the great emotional beats (Haurchefant's death at the Vault, Moenbryda's funeral, Tesleen's transformation, Seto/Ardbert's crystal, the Night's Blessed funeral rite, the Ultima Thule dead-civilisation stories, the pre-finale comrade rounds); the Dragonsong War truth; the Warriors of Darkness; the body-swap (In from the Cold); and every expansion finale. Safety re-verified across the WHOLE index at the end: zero `[COND]` on any entry whose steps name a duty, trial, solo duty/duel or manifest tie (the single grep hit is a false positive — 'Unrest in Ishgard' contains the string inside a note asserting there is NO solo duty there).
- (08 v3.34) **CITY OPENINGS MARKED — all three, per-quest wiki-resolved (42 new markers; total now 159).** GM correction that drove this: the campaign has NOT started (the starting city is still undecided) and the system must be REPEATABLE, so every origin needs equivalent treatment — my earlier inference that the openings were already behind the cursor was wrong, drawn from the Titan/Thordan TESTS rather than from play. Method: each of the 66 body quests resolved individually on ConsoleGamesWiki (steps + any fight / instanced-solo duty / named story NPC) — never from the title. THE PASS PAID FOR ITSELF: many titles read like errands but are not — `Lurkers in the Grotto` (solo duty + Y'shtola's FIRST appearance), `Chasing Shadows` (solo duty + Yda/Papalymo + a Hydaelyn vision), `Underneath the Sultantree` (solo duty vs voidsent + Thancred + Hydaelyn), the three masked-mage/Ascian encounters (`Just Deserts` · `Spirithold Broken` · `Way Down in the Hole`), the two-instance city climaxes (`Feint and Strike` · `To Guard a Guardian` · `Duty, Honor, Country`), and the three Carteneau ECHO-VISION banquets (`A Mizzenmast Repast` · `Renewing the Covenant` · `A Royal Reception`) — every one of them PLAYED. Per city: **Limsa 12 markers → 8 condensed in 2 bridges (15 played)**; **Gridania 15 → 13 in 3 bridges (10 played)**; **Ul'dah 15 → 13 in 3 bridges (10 played)**. The Limsa asymmetry is CONTENT-DRIVEN, not an inconsistency: that chain genuinely carries more early combat quests (Double Dealing, Plowshares to Swords, Just Deserts, Victory in Peril, Feint and Strike). ALSO CORRECTED: the older 08.2 line calling these bodies "overworld only, no duties" is wrong — the wiki shows solo duties throughout, which is precisely why per-quest resolution was required; the coverage note now records this. The previous "deliberately unmarked" note is superseded.
- (08 v3.34) AUDIT OF THE MARKING PASS + coverage gap closed. **1 REAL ERROR FOUND AND FIXED:** `Defenders for Ishgard` carried `[COND: parallel → The Wyrm's Roar]`, but The Wyrm's Roar is ITSELF marked — a converge target must be the first UNMARKED entry (the actual stop), so it was corrected to `An Allied Perspective`; all 15 `parallel →` targets were then re-checked and the other 14 are valid. INTEGRITY VERIFIED: no `[COND]` on any quest referencing a duty/trial/solo duty/manifest tie (whole index); duplicate quest entries (backfill blocks) carry consistent marking; no quest line escapes the `**Name** — giver:` format; the "single isolated low-agency quest plays normally" clause, the STOP GUARANTEE and the `riassumi` controls are all intact. **VERIFIED COUNTS (correcting an earlier overstatement of mine — I had said "710 ARR entries", which wrongly counted OST table rows and trial pins): ARR = 326 quests** (254 shared chain + 72 city-opening entries), matching the index header's "~330". Per playthrough (one starting city, 277 quests): **183 played in full (66%) · 93 condensed into 29 bridges (34%) · 1 cut** — top-level beats drop 277 → 212 (−23%), and more at the table since a played quest can span several sub-beats while a bridge is one. Longest run 7 (the Wineport banquet chain). Of the 117 markers, 24 sit ISOLATED between substantive beats and therefore PLAY (5 of those still condense their internal cluster via scale ii); the other 19 are inert until an adjacent entry is loosened — by design, not a defect. **COVERAGE GAP CLOSED (structurally, deliberately):** the three 23-quest city openings stay UNMARKED and 08.2 now says so explicitly as a binding note — the index holds only NAMES there (no giver, no steps), so marking would mean guessing from titles, the method already proven unsafe; unmarked = played keeps it safe, the §B2 FALLBACK classifier applies, and that is safe in this stretch specifically because the file itself certifies these bodies contain NO duties. Also noted: a live campaign past the openings (the current one is at installment 4) is unaffected either way. Any future pass over them must resolve each quest's steps on CGW first, never from the title.
- (08 v3.34) **ARR COMPLETE — 08.2 fully marked: 117 `[COND]` + 1 `[CUT]`** (53 fetch · 51 relay · 16 parallel). Patch content 2.1-2.55 added on top of the 7 base installments. MARQUES RULING APPLIED (GM: "condensa da dopo l'incontro, e comunque light social"): the first Marques scene (A Proper Burial, where he is introduced) stays PLAYED, while the three later errands (You Can't Take It with You / With a Little Elbow Grease / A Tall Drink of Aqua del Sol) are now marked — they form a run of 3 stopping at Bringing out the Dead. Notable patch runs: the Revenant's Toll establishment cluster = **6 consecutive** (Crate Go Kaboom → Better Late than Sever → Welcome to Morbol Country → Answering the Call → You're Gonna Carry That → The Things We Do for Tea, stop: It's Possibly a Primal); the Doman-refugee chain = 4 (Promises to Keep → A Small-scale Operation → Yugiri's Game → If Wishes Were Horsebirds, stop: Why We Adventure); the 2.55 pre-banquet calm = 5 (Administrative Decision → An Unexpected Ambition → Ancient Ways Timeless Wants → Where We Are Needed → The Least among Us, stop: A Time to Every Purpose, "the last calm before the banquet"). PROTECTED throughout (unmarked): every trial/dungeon beat (Moggle Mog, Leviathan, Ramuh, Shiva, Nabriales, Vishap, Snowcloak, Keeper of the Lake, Sunken Temple), Moenbryda's death and both mourning beats (In Memory of Moenbryda, Mask of Grief), the F'lhaminn/Minfilia reunion, the Scions reunion round, the Crystal Braves recruitment AND founding ceremony (load-bearing for the 2.55 betrayal), the Ilberd/traitor thread, the doppelganger fights in the Sylphlands, Aymeric's first appearance, the clouded-vial setup (Come, but Not Gone) and the ARR finale. Safety re-verified across the whole index: no `[COND]` quest references any duty, trial, solo duty or manifest tie. NEXT: HW (08.3) → SB → ShB → EW.
- (08 v3.34) INSTALLMENTS 5 + 6 + 7 MARKED (13 + 14 + 0) — **base ARR (2.0) now fully marked: 66 `[COND]` + 1 `[CUT]` across all 7 installments**. Inst.7 legitimately took ZERO markers (Hearts on Fire, Setting the Stage, Rock the Castrum, The Ultimate Weapon = a morale-rally convergence, a 6-enemy fight, Castrum Meridianum and the Praetorium/Porta Decumana finale) — a useful signal that the criterion does not over-mark. Biggest runs: inst.5 **run of 5** (The Final Flight of the Enterprise → Ye of Little Faith → Opportunity Knocks → Factual Folklore → The Best Inventions, stop: Influencing Inquisitors) and **run of 4** (the corrupted-crystal research chain Into the Eye of the Storm → All Due Precautions → Sealed with Science → With the Utmost Care, stop: A Promising Prospect); inst.6 **run of 5** (the Castrum Centri infiltration prep Come-Into-My-Castrum → Getting Even with Garlemald → Drowning Out the Voices → Acting the Part → Dressed for Conquest, stop: Fool Me Twice) and a **run of 3** for the Camp Bluefog morale cluster stopping exactly at Hearts on Fire — which is where the index's OWN pre-existing annotation said the cluster converges, an independent confirmation that the marking agrees with the file's earlier hand analysis. Kept unmarked on principle: the Francel heresy-trial investigation, the Guillaime inquisitor arc, the Giggity/Tiggy spriggan sub-thread (named target + tempered-sylph fight), the Biggs/Wedge rescues, Escape from Castrum Centri, The Black Wolf's Ultimatum, and every duty/manifest beat. STILL UNMARKED (next chunk): the ARR PATCH content 2.1-2.55 (~440 lines of 08.2), then HW → EW.
- (08 v3.34) INSTALLMENTS 3 + 4 MARKED (10 + 11 `[COND]`), same calibrated criterion. Inst.3 runs: Ziz Is So Ridiculous + Rock of Rancor (stop: Seeing Eye to Winged Eye) · Tales from the Tidus Slayer + Hungry Hungry Goobbues (stop: The Lominsan Way, which introduces Wheiskaet) · The Penitent Man + Changing of the Guard (stop: Trial by Turtle). Inst.4 delivers the biggest win so far: a **RUN OF 7 CONSECUTIVE** — the entire Wineport banquet errand chain (What Do You Mean You Forgot the Wine? → An Offer You Can Refuse → It Won't Work → Give a Man a Drink → That Weight → Not My War → Battle Scars) collapsing into ONE bridge and stopping at It Was a Very Good Year (a fight). Intra-quest `parallel` markers added where a quest hides a same-type cluster: Secret of the White Lily (show the button to 4 NPCs), Changing of the Guard (inform 3 near-identical Kikokutai), A Final Ignominy (banquet prep 0/3). DELIBERATELY LEFT UNMARKED, with reasons worth keeping: the whole MARQUES sub-thread (You Can't Take It with You / With a Little Elbow Grease / A Tall Drink of Aqua del Sol) — mechanically pure errands, but Marques IS the amnesiac Cid nan Garlond and these scenes build toward his reveal, so the GM may want to override this one; the Waking-Sands-massacre aftermath (Bringing out the Dead, Bury Me Not on the Lone Prairie — Noraxia's funeral, a tender-register beat); In the Company of Heroes (the 5 veterans' tests = the arc payoff, though mechanically a cluster); As You Wish (the immediate pre-Titan beat); Men of Honor (carries the High Houses introduction); the Coerthas arrival beats (new-area intro per §B2).
- (08 v3.34) INSTALLMENT 2 MARKED (13 `[COND]` on ~28 quests), applying the criterion the GM calibrated on the pilot: pure errands condense (INCLUDING trivial mob-kill + gather, per the 'Forest Friend' ruling — Microbrewing, Helping Horn); relays that INTRODUCE a hub/arc NPC are played (Spirited Away introduces Buscarron, whom §B2 itself names as an on-site info source; On to Little Ala Mhigo introduces Gundobald); anything with a duty, a real encounter or a manifest tie is never marked. Runs the rule now forms: **5 consecutive** (Druthers House Rules → Never Forget → Microbrewing → Like Fine Wine → Sylphish Concerns) stopping at Nouveau Riche (a fight); **Tea for Three + Foot in the Door** stopping at Meeting with the Resistance; **Come Highly Recommended + The Bear and the Young'uns' Cares** stopping at Wilred Wants You (a fight). Four marked quests stay ISOLATED between substantive beats (Brotherly Love, A Simple Gift, Ratting It Out, Helping Horn) and therefore PLAY normally — the 2+ rule working as designed; their markers are still true data if adjacent entries are later loosened. Left unmarked on purpose: Presence of the Enemy (investigation), Killing Him Softly (a persuasion scene = playable content), He Ain't Heavy (the Gallien thread), Believe in Your Sylph (the sylph-peace payoff), Highbridge Times (nominally an investigation in the masked-man arc).
- (08 v3.34 companion) PILOT REVIEWED BY THE GM — Installment 1 marking accepted, with 3 rulings on the borderline cases I had left unmarked: (1) 'Life, Materia and Everything' → CUT entirely, not merely condensed: its only content is the materia-system demo and this homebrew has NO materia (verified: the word appears nowhere else in the corpus). New `[CUT: <reason>]` marker formalised in 08.0 — stronger than `[COND]`: never played, never bridged, never an 'apre' target, the chain skips it ('Dressed to Deceive' now closes straight onto 'Lord of the Inferno'); the entry stays only as a canonical trace. Reuses the CUT pattern already in the file (the Crystal Tower fetch-errands). (2) 'Forest Friend' → `[COND: fetch]` (GM: "è comunque una fetch quest") — this forms an inter-quest RUN with the adjacent 'Dance Dance Diplomacy', so its converge target was corrected to the first unmarked entry, 'Presence of the Enemy'. (3) 'Call of the Forest' / 'Call of the Desert' (city relays introducing Miounne/Momodi) and 'Sylph-management' (Vorsaile Heuloix briefing) → KEPT UNMARKED, played. Installment 1 final: 5 `[COND]` + 1 `[CUT]` out of ~26 quests. Judgement calls the pilot validated (traps correctly left unmarked): 'A Proper Burial' looks like a burial errand but introduces MARQUES = the amnesiac Cid nan Garlond; 'For the Children' and 'First Impressions' contain fights; 'We Come in Peace' introduces Amelain, whom §B2 itself names as an arc-anchor.
- v4.73: §A1 PROSE-RULE PRUNING (GM audit: "are the prose rules still worth their space, given they were written for Sonnet and Gemini is already strong at Italian prose?"). MEASUREMENT FIRST — the 9 register exemplars were 9,830 char = **0.8%** of the 1.23 MB knowledge base, so BLOAT WAS NEVER THE ISSUE; the question is help-vs-harm. PLATFORM CONTEXT (researched): Anthropic's guidance is <~200K tokens = put everything in context, above it RAG; Claude Projects auto-enable RAG near the context limit (~10x capacity). This corpus is ~310-350K tokens, so the Project runs in RAG and 06 is RETRIEVED IN CHUNKS, not fully in context — which is precisely what condemns sample prose: an exemplar is a paragraph of Italian NARRATIVE (Ifrit, Ul'dah, Momodi), so it looks semantically like LORE and gets retrieved on CONTENT queries rather than when register guidance is needed. DECISIVE EVIDENCE: v4.65 already recorded the TRIAL exemplar as the ROOT CAUSE of Titan-as-fire, and its ELEMENT CAVEAT patch (~1,400 char) cost more than the exemplar itself — in RAG that exemplar is lexically saturated with trial/arena/primal terms, so it is preferentially retrieved on exactly the queries where it does harm. EDITS: (1) DELETED the TRIAL/PRIMAL exemplar AND its ELEMENT CAVEAT — content fully preserved by the §B10 TRIAL LORE-FIDELITY CHECKLIST (5 items, with the Titan examples) plus the cached 08 TRIAL PINS; §A1 now states DELIBERATELY NOT EXEMPLIFIED (city/arrival, cutscene/reveal, trial) with a binding DO-NOT-RE-ADD rationale. (2) PRUNED 9 exemplars → 3 CALIBRATION ANCHORS (action/ambiente+aggancio · sociale-dialogo Momodi, also the richest idiolect demo for rule (f) · emotivo-tenero, the register where the action rules BEND and the bar for the §A1 tender rule); deleted aftermath, villain-entrance, comic, città/arrivo, cutscene/rivelazione. Exemplars are kept ONLY for what abstract rules cannot convey — LENGTH, DENSITY, RHYTHM — and the lead-in now says so. (3) MERGED the overlapping style rules: COMPOSE DIRECTLY IN ITALIAN + NO ENGLISH RHETORICAL SCAFFOLDS → one rule (all failure shapes kept); VERB & PREPOSITION PRECISION absorbed into the staging check as its face (1), which the text already declared "one case of this, not a separate rule". (4) Fixed the now-dangling §B10 cross-reference to "§A1 TRIAL exemplar". KEPT INTACT (classified as NOT style): the VOI-plural rule, the Italian output labels, CD-not-DC — project SPECS no model can guess; and the anti-confabulation/coherence guards (staging/geometry check, CONCRETE≠PLAUSIBLE-SOUNDING, NEVER INVENT IDIOMS with its "the repair is DELETION" insight) — these fail on EVERY model, Gemini included, and are the highest-value lines in the section. Rules (a)-(f) kept verbatim: they are the distilled exemplars, the best value/token in §A1. ACCEPTED CONSEQUENCE (reversible): the COMIC register loses its only sample and has no compensating "rules bend" note — if comic scenes flatten in play, restore that exemplar FIRST. 06 stays 76 §.
- KNOWLEDGE-SIZE ANALYSIS (companion to v4.73; findings only, no restructuring done). Measured weight: 08.4+08.5+08.6 (the SB/ShB/EW quest indexes) = 104.8 KB = 8.5% of all knowledge — the ONLY large low-risk lever; 08.1 roadmap+manifests 74 KB and 08.2 ARR index 90 KB are active/gating and stay; 06's top sections (§B1 22K, §B6 18K, §B17 18K, §B2 17K, §B12 14K) ARE the ruleset and are not compressible without deleting binding rules; 02's 23 progression tables = 29.2 KB (13% of 02). KEY CAVEAT: no realistic pruning escapes RAG — that would need 1.23 MB → <700 KB (~43% cut) — so the goal is RETRIEVAL PRECISION, not size, which is why the §A1 work matters more than any bulk deletion. Gemini Gems cap knowledge at 10 files; the project uploads 9, one from the cap. DEFERRED (recommended, NOT executed): split 08.4-08.6 into a companion file kept in git but NOT uploaded until the campaign reaches Stormblood (currently ARR ~Lv4). Verified safe on the two risks that matter — the OST tables (all expansions) and the HW→EW TRIAL PINS both sit in the 08.2 region and would NOT move, and 08.1's manifests stay. Not done in this pass because it changes the GM's UPLOAD SET (operational) and would mix a structural refactor into a prose commit. DO-NOT-RE-LITIGATE: (a) consolidating 02's progression tables saves only ~2.4% and they are load-bearing for §D4 PC building — a wrong slot row fails SILENTLY; (b) compressing 06's big sections = deleting binding rules; (c) chasing the 200K-token threshold is not achievable for this corpus.
- v4.72: §B16 LB NO FRIENDLY FIRE (companion 05 v2.02) — a damaging LB resolves on ENEMIES ONLY, never on allies/the user/bystanders standing in the line or circle, with the explicit BOUNDARY that this is an LB-ONLY exception (ordinary AoE spells keep standard 5e friendly fire). Added to §B16 and not only to 05 because the failure was OPERATIONAL and happened in a One-Shot: 06 is the file the live assistant follows during play.
- v4.71: §B14 Phoenix prices bumped to match the 05 v2.00 revival rebalance — a hub merchant now stocks 3 Phoenix Downs (250 Gil, was 150) + 1 Phoenix Tail (1,500 Gil, was 1,000). RATIONALE (GM): a revive is strategically worth far more than any heal (it puts a body back in the fight), so even after the potency nerf (Down→1/4, Tail→1/2 in 05 Ch.12.3/18.3) the old prices read as underpriced vs the potion ladder (High Potion 150 / Max Potion 500, 05 Ch.12.4). Drops policy UNCHANGED (§A20 L171 / §A21 L180: Phoenix items stay shop-only, NEVER loot — GM chose status quo). §B14 is the only price occurrence in 06; 06 stays 76 §.
- v4.70: Titan+Thordan double-trial retest (both excellent — healer loot fixed, multi-theme music, HP/die/offense all correct, Thordan's full kit — Ascalon's Mercy / Dragon's Gaze / Knights of the Round → Ultimate End — landed from the pin; load-gate proposed Lv7→11 correctly). §B6 NO BROAD PHYSICAL RESISTANCE AT LOW LEVEL (GM decision, ALL encounter types): 'resist nonmagical bludgeoning/piercing/slashing' halves a low-level party's ENTIRE offense (no magic weapons → silent ~2× EHP, no counterplay) — do NOT give it below ~L5 (before +1 weapons are common on the §A20 ladder); fair from ~L7+ where lore warrants. A SINGLE narrow resistance (one element or one physical type) is fine at any level (prefer one lore-justified resistance over the broad bundle); still obeys the HP trade-off (resistant → low HP; never stack a broad resistance on top of longevity-HP). Prompted by a GdS-4 Titan given the full nonmagical-physical bundle AND 126 HP = ~2× over-tank vs a Lv4 party. §A23: LIST EVERY CACHED TRACK, not a subset — a five-phase trial (The Navel) prints all five in order, not just opening+climax. PRE-COMMIT SANITY FIX: reconciled a contradiction between §B11 (old: 'a raw HP bump max ~1.5× is the EXCEPTION, ONLY for a boss with NO phase') and the new §B20 TRIAL HP TARGET (1.5-2× WITH phases) — §B11 now states the elite-boss HP-RESERVE (~1.5-2×) is EXPECTED for a SOLO trial/duty boss, used TOGETHER with phase gates + LR + legendary actions (the sim showed a phase alone does not lengthen the fight enough vs 4 focus-firing PCs), never instead of them; offense still in band. 06 stays 76 §.
- v4.69: §A23 MULTIPLE THEMES — LIST THEM ALL (GM request, generalises the existing city day/night rule): whenever a single area or fight has MORE THAN ONE cached track, emit ALL of them as a list of 🎵 links so the GM knows they exist and can choose — never silently pick one. Covers a city/zone's day+night, a trial/boss PHASE PROGRESSION (e.g. The Navel/Titan lists all five: Weight of a Whisper → … → Under the Weight), and any opening/climax set. Encouraged: a short WHEN/WHICH tag before the track name ('Giorno'/'Notte', 'Fase 1'/'Fase 2', 'Apertura'/'Climax') — the one permitted label addition (the redundant '(Battle Theme)' gloss stays banned); keep cache order; if the phase mapping is uncertain, still list all tracks untagged, never drop or invent one. 06 stays 76 §.
- v4.68: Titan-trial 4th-retest — the trial itself is now dialled in (Y'shtola explicitly stays OUTSIDE because without the Echo Titan would 'asservirla' — 05 Ch.4.5 landed perfectly; [Info GM] correctly 'prosegue Lord of Crags' with the Camp Bronze Lake rendezvous, no early close; theming/HP(115, d12=Enorme)/offense/multiattack/phase all correct). §A20 ROLE ↔ PROPERTY MUST MATCH THE MECHANIC (GM-flagged): a generated item's property must apply to something the role actually uses — a HEALER item boosts HEALING/support (extra HP restored, added target, temp HP, a defensive/utility boon), NEVER '+spell attack / +save DC on HEALING spells' (a heal makes no attack roll and forces no save, so the bonus applies to nothing); a +spell-attack/+save-DC focus is a DPS MAGICO item. Softened the v4.67 shield clause per the GM: noting a mundane shield's base '+2 CA' is FINE (magic lives in the property); only a genuine MAGIC-enhanced +2 shield must be Rare. NOT issues (verified): the OST 'Weight of a Whisper' is CORRECT (the cached Navel opening theme, 08.OST L681); 'Furia Terrestre 21 (5d6)' is a dice-math slip already covered by v4.67 (5d6=~18). 06 stays 76 §.
- v4.67: Titan-trial 3rd-retest polish (all the v4.65/v4.66 fixes landed — theming, HP 135 in target, offense-in-band, Y'shtola outside, multiattack specific, phase under Azioni, no bad title/rarity). Two recurring mechanical slips fixed generically: §B6 DICE MATH RULE gains (a) HIT DIE MATCHES TAGLIA (Media d8 · Grande d10 · Enorme d12 · Mastodontica d20 — failure shape: an 'Enorme' block on 18d10, should be ~16d12) and (b) SAME MATH ON DAMAGE — the average on EVERY damage line must equal its formula, not only HP (failure shapes: '15 (3d10)' [real 16-17], '13 (2d8+2)' [real 11]). §A20: a SHIELD's base +2 AC is NOT a magic bonus — a mundane shield is written just 'Scudo' with the magic in the property (rarity from the property); a magic shield is '+1 scudo'=Uncommon / '+2 scudo'=Rare labelled at that rarity; never 'Scudo (+2 CA)' tagged Non-comune. WATCH (compliance slips, no rule change): the trial's closing line named the wrong turn-in ('Associazione degli Avventurieri' vs the correct R'ashaht Rhiki / Maelstrom Command, §B2 handoff); Earthen Fury printed 'danni da forza' (should be contundente/tuono for an earth slam) and Tumult lost its recharge. 06 stays 76 §.
- v4.66: Titan-trial retest polish (companion 05 v1.99, 08 v3.33). The v4.65 fixes worked (element/arena/rock body/offense-in-band all correct); this pass fixes the residuals. TRIAL HP TARGET (§B20, from a balance SIMULATION): a solo trial boss's HP is sized so the fight lasts ~4-5 rounds vs the party's focus-fire — in practice ≈1.5-2× the GdS band-centre HP via the elite HP-reserve (offense stays in band; more HP lengthens the showcase, never raises lethality). Failure shape: a GdS-4 trial at ~85 HP (band-centre) ending in ~2.5 rounds before Tumult/full kit land (target was ~150). At Lv4 the party has only ~38 DPR (martials have 1 attack pre-L5), so band-centre HP is far too low for a trial. §A1 L48 + the 08 Titan pin: the Navel arena IS inside a volcano (magma in the SURROUNDINGS is canon) — 'limit correctly': volcanic ambience OK, but Titan's BODY is rock and the instant-death is the knockback FALL off the edge, not a lava-boss theme; and Titan is BIPEDAL (torso on rock legs, stands and stomps — 'legless' was a model invention, never in the pin). §A5: NPC TITLES/RANKS are canonical or omitted, never coined (failure shape: Y'shtola as 'la Cospicua della Settima Alba' — she is a Figlia della Settima Alba). §A20: AC items follow their REAL 5e rarity (a ring/cloak of +1 AC = Ring/Cloak of Protection = RARE, not Uncommon; +1 shield = Uncommon; don't duplicate a bonus across the five role items). §B6: a Multiattack NAMES its specific parts, never 'usa un'azione disponibile'; phase/recurring mechanics go under Azioni/Azioni Leggendarie, not Reazioni. §B20 gains a NON-ECHO-ALLIES-STAY-OUT pointer (05 Ch.4.5). NOT changed (checked): naming 'Hydaelyn' at the Titan crystal beat is NOT a gate breach — the NAME is Scion-level knowledge by L5 (the crystals ARE 'Hydaelyn's blessing', 05 Ch.7.1); only her NATURE is gated in ARR (08 L85), and the beat didn't reveal it. 06 stays 76 §.
- v4.65: TRIAL / PRIMAL fidelity + longevity pass (companion 08 v3.32), prompted by a Titan trial test where an EARTH primal was written as fire/magma (arena over a lava abyss, obsidian body) with over-band raw damage and no phase/longevity. Root cause: §A1's TRIAL/PRIMAL register exemplar is an all-IFRIT (fire) scene and its element bled onto Titan. Fixes (all in-place, 06 stays 76 §): (F1) §A1 L48 — the trial exemplar now carries an ELEMENT CAVEAT: it is IFRIT-SPECIFIC, imitate its REGISTER not its element, re-theme every image to the ACTUAL boss (Titan = brown rock + chasm arena, Garuda = wind, Leviathan = water, Ramuh = lightning, Shiva = ice…); Titan-as-magma is the named failure shape. (F2) §B10 — NEW TRIAL LORE-FIDELITY CHECKLIST (shared): before writing a trial, fetch + make element-consistent 5 things — ELEMENT (governs all), ARENA + its REAL instant-death/hazard (Titan = knocked off the edge into a chasm, NOT lava — 05 Ch.9.6 pick the true hazard), BOSS VISUAL (Titan = living rock, not obsidian), SIGNATURE MOVES, PHASE/gimmick; arena+body+moves+damage-types all match the element. (F3) §B20 — TRIAL build discipline: a trial is a LONG mechanics-showcase, CR = party level, longevity from PHASE GATES + Legendary Resistance (1-3) + 1-2 legendary actions + HP to top-of-band/~1.5× the elite HP-reserve, NEVER raw sustained damage. (F4) §B11 — AVOIDABLE-DAMAGE CARVE-OUT (GM design): sustained/UNAVOIDABLE offense (auto-attacks AND tank busters — a tank buster is telegraphed but not dodgeable, so it stays band-level/survivable, never a tank one-shot) stays IN BAND; only DODGEABLE AoEs + FAILED-MECHANIC punishes (Weight of the Land, Earthen Fury) may EXCEED the band ("dodge = no damage"). Verification method (GM instruction): all trial lore checked ONLY on the two pinned wikis (Gamer Escape blocked WebFetch with 403 → used ConsoleGamesWiki), never a global search.
- v4.64: FULL-AUDIT CONSOLIDATION pass (companion 05 v1.98, cv22, ov10) — no new §-sections, all edits in-place (06 stays 76 §). Fixes found by a 3-phase reference/semantic/flow audit: **(M1/M2)** §B1 COMMAND CHANNEL One-Shot roster corrected to '/genera /atto X /prova /wipe /tracker' (was stale: listed /negozio /mostrami /cercano — which ov disowns — and omitted /prova /wipe /tracker). **(M3/S3)** SAVE WRITE-TRIGGER reconciled to the two-command model everywhere — §B17 (was 3 stale bullets saying write-on-'confermo' / write-on-'/fine sessione') now: '/fine sessione' NEVER writes, the WRITE happens ONLY on '/salva', a free-text 'confermo' only accepts the gate's CORRECTIONS and never writes; §B24 propose-and-fix loop clarified (if a warning first arises on a bare '/salva', propose, don't write, and write on the FOLLOWING '/salva' once confirmed). **(M4)** difficulty label kept at 3 (Facile/Media/Difficile); §A18 + §B1 now state 'Mortale' is the 5e Deadly BUDGET tier (05 Ch.10.2a) used to SIZE a fight, NOT a label to print (a lethal setpiece is built via GdS §B11). **(M6)** SLASH-ONLY command dispatch (GM decision): every natural-language trigger LIST removed — §A4 image ('mostrami'/'che aspetto ha' → '/mostrami' or the automatic first-introduction), §A18 check ('/prova' only), §A23 music ('musica'/'OST'/'tema' → '/musica' or automatic on zone entry), §B2 'prepara' phrasings, §B19 recap ('recap'/'dove eravamo rimasti' → '/recap'), §B25 'mappa MSQ' synonyms → '/mappa MSQ', §B24 stray 'carica'. A word without '/' is now always normal chat; the ONLY no-slash trigger is the pasted '=== SAVE ===' block (LOAD). Residual 'alias(es)' language removed (§B2/§B24) as it contradicted the NO-ALIASES rule. **(M6b)** ONE-SHOT is STUDY-ONLY (GM confirmed one-shots are prepared then played at the table, not live through the assistant): §C10/§C11 LIVE-PLAY branch removed (no scene-by-scene reaction, no auto act→act flow from a free-text message); acts are produced one per '/atto' request, the module ends on its prepared EPILOGUE + 'Fine' (failure close = '/wipe', §C13). **(M7)** §B22 MSQ return point unified as 'the MSQ Bookmark' (= the live working cursor at suspend, persisted to [A] on '/salva') — was named both 'LIVE WORKING CURSOR' and '[A] bookmark'. **(M8)** a '/voci' Aggancio is valid for '/accettiamo' ONLY on the turn immediately after '/voci' — any command in between clears it (§B22 + cv). NO-CHANGE decisions from the audit: **(M9)** '/accettiamo' still overwrites a full [C] slot (incl. a SOSPESA non-canonical dossier) with NO confirm — single-slot replace-freely kept by GM choice, the loss is the GM's call. **(orphans)** §A11/§A15/§B7/§B16/§B18/§C3/§C8/§C9/§D2/§D8 are leaf rules (self-cited only) — left as-is, not dead. **(§A2)** the numbering gap is intentional (never cited) — left as-is. AUDIT CLEAN: zero broken §-links, zero broken 05-Ch. refs, no removed-Ch.11/out-of-range citations, controlled vocab (Asservito/Temprato) intact.
- v4.63: NEW §C13 ONE-SHOT WIPE / FAILURE EPILOGUE (/wipe) (companion ov9) — operationalizes the failure close that §C1/§C7/§C11 already DECLARE ("Wipe = narrative failure") but had no trigger for. `/wipe [<encounter/scene/act>]` names where the party fell (one-shots are read-ahead: prepared then played; omitted → the current/most-recent point; ambiguous → ask WHICH, never invent, per §C2 MISSING INPUT); the mission is FAILED and everything AFTER the wipe point is INERT (anti-confabulation: never narrate an unreached act/reveal as if it happened). OUTPUT = ONE rich player-facing 'Da leggere ai PG' failure epilogue (§A1 register), ending 'Fine' — NO GM-facing report (GM reads it straight to the table, per GM). WIPE-TEST REFINEMENT (folded into v4.63): the epilogue OPENS from the aftermath (party already down) and does NOT re-narrate HOW the enemy won (that happened at the table); the PLOT CONSEQUENCE (what unfolds in the world because the party failed) is the developed HEART of the epilogue, after a brief sensory bridge. Kept generic — no hardcoded example lines. Honours tone/audience (§C1 — a combat-light/kids' module gets a SOFT, genre-appropriate failure, not gore); SELF-CONTAINED terminal close (no hooks/sequel bait). Reuses the victory-close epilogue engine, failure branch. §C11/§C1/§C7 gain pointers. 06 §-sections go 75→76 (new §C13 — expected, precedent §B28). REJECTED (do not add): a CAMPAIGN /wipe — there a wipe is the Echo REWIND (05 Ch.4.6/18.5), the OPPOSITE of a failure, so a same-named failure-close would contradict the no-permanent-death design; the rewind stays a table call (the assistant already re-emits the encounter/tracker on demand). 05/cv/lv/07 unchanged.
- v4.62: §A23 OST link moved from a Google search scoped-to-YouTube (`google.com/search?q=FFXIV+OST+<track>+site:youtube.com`) to a YOUTUBE MUSIC search (`music.youtube.com/search?q=FFXIV+OST+<track>`) — YT Music indexes the official game soundtrack, so the first result is the official track (companion cv21/lv9/ov8). Still a SEARCH url (never a /watch or playlist id), English query, label = track name only. Image/map links UNCHANGED (stay on Google Images, §A4). AGNOSTIC (GM-verified): the query prefix 'FFXIV OST' makes the music.youtube.com link resolve the official track as the first result on BOTH Claude Project AND Gemini/GEM — an earlier bare 'Final Fantasy XIV' variant failed on GEM; the 'OST' prefix is what works on both (the longer 'Final Fantasy XIV OST' also worked but 'FFXIV OST' is the shorter equivalent the GM confirmed), so a single agnostic format (no per-platform override needed).
- v4.61: §B6 PHILOSOPHY SHIFT — fidelity-first → SCALE-FIRST (GM design decision; companion 04 v1.3, 05 v1.97, lv8, ov7). A stat block is now BUILT to the TARGET GdS (set by §B11 / the encounter budget 05 Ch.10.2), not copied verbatim at a source's own CR. Split of concerns: the CHASSIS (a lore-fit creature from 04 / an official 5e monster / the wiki) supplies ALL the QUALITATIVE profile — type, signature moves, behaviour, AND resistances/vulnerabilities/immunities/senses — from LORE; the NUMBERS are scaled to the GdS band. ANCHOR PRINCIPLE → BUILD TO THE TARGET GdS; VIA A 'copy verbatim' → CHASSIS + SCALE (verbatim kept only as the zero-scaling shortcut when the chassis already fits); CR CALIBRATION → scale any sensible chassis; NO-ADDED-CAPABILITIES → SIGNATURE MOVES FROM LORE with numbers in band (lore moves are now WANTED, only off-band numbers/off-lore inventions are wrong); 'THE CR TABLE DOES NOT OVERRIDE A REAL BLOCK' → 'THE BAND IS THE BUILD TARGET' (elite-boss HP-reserve stays the only band exception); SOURCE FIDELITY → DOUBLE FIDELITY (lore + numbers-in-band). The band table is now the BUILD TARGET and its HP/Damage columns are RANGES (best practice: GdS = average of defensive + offensive CR, so HP TRADES OFF against defences — pick HP low for a defended/resistant creature, high for a fragile one; attack/DC stay DERIVED from stats). This keeps same-GdS creatures from having identical HP and immunises generation against fixed-data errors (04 is now a chassis, not an authority). HP FORMULA LOCK, layout, Taglia, no-XP, elite-boss reserve, telegraph — all unchanged. §D4 principle name updated. 06 stays 75 §-sections. NOTE: the earlier plan to fix 04's 12 CR/XP mismatches is now DEPRIORITIZED — 04's numbers are a scalable starting point, so those errors are harmless (the Puk 55→22 fix already done stays, as a sane reference).
- v4.60: Round-2 post-fix test (companion 05 v1.96). Generic reinforcements + compliance failure-shapes, no new parallel rules. §A8 GEOGRAPHY GROUNDING: the real canonical geography of the current location (biome/waterways/climate/settled-ness, verified §A6) governs the environment description, the plausible creatures, and (cross-ref) the danger rating + travel offer — failure shape: an inland forest hub framed as coastal (sea/bay/brine), or a wilderness ambush at a city's doorstep. 05 Ch.14.6 DANGER RATING gains a GEOGRAPHY ANCHOR (a route/camp at/adjacent to a major hub or in settled/patrolled territory is Tranquillo by default; Rischioso/Ostile need real wilderness/border/infested geography — observed: a patrolled near-Gridania leg tagged Rischioso). §B2 TRAVEL LINE: the existing trivial-hop rule now explicitly covers an INTRA-SETTLEMENT / same-area move (city → its own pier/gate) = no /viaggio offer (observed: /viaggio offered for Nuova Gridania → its Westshore Pier); /viaggio stays right for real journeys OUT of the settled area. §A5: verify the NPC's SEX (a wiki fact like race) and agree every gendered Italian word to the PERSON (observed: male Vorsaile Heuloix written 'china' not 'chino'); distinct from G2 grammatical gender. §A20 PRICE IS PRINTED: rarity is printed on EACH special-item line, not only collectively, so the GM can sanity-check on-tier. 06 stays 75 §-sections.
- v4.59: Sylph test-corposo pass (companion 05 v1.95, 07 v1.34, cv20). SUBQUEST SUSPEND+RESUME: [C] gains a STATE ATTIVA/SOSPESA (§B22/§B17/§B24) — returning to the MSQ no longer DISCARDS the subquest: `/riprendi MSQ` suspends it (kept, resumable), new `/riprendi SQ` resumes it; single slot unchanged (a new /accettiamo still replaces it), the old `/torniamo alla MSQ` is renamed to `/riprendi MSQ`. AUTO-CONDENSE broadened + made aggressive/silent (§B2): the condensable class now spans low-stakes SOCIAL RELAY and PARALLEL MICRO-OBJECTIVE/TUTORIAL clusters (the 3 sylph lessons), not just pure fetch; the STOP guarantee (play in full at the first fight/reveal/real-choice/major-arc-NPC/setpiece/pinned cutscene) is the sole guardrail; the `/gioca` force-play override is REMOVED (GM would never use it). TRAVEL EVENT VALENCE skews with the danger rating (§B26 / 05 Ch.14.6) — Tranquillo→good/neutral, Rischioso→mixed, Ostile→bad — one die, no extra branch. Fixes: §A4 image is mandatory even in a pre-generated statted branch (§B26/§B28 — observed Puk block with no image); §B20 non-hookable SEED is present-by-default AND distinct from the actionable hook (observed: all tiers fed the one hook); §A3 no invented decorative traits (Puk has no moogle pom-pom); §A5 race is always one of the 8 canonical, never a malformation (observed 'Elau' for Elezen Vorsaile Heuloix). ENCOUNTER DIFFICULTY CALIBRATION (universal, reuses the existing 05 Ch.10.2 engine — no new tables): every open-area fight is built on the Ch.10.2 XP budget at a difficulty tier set by CONTEXT — travel/camp → the zone DANGER RATING (Tranquillo→Facile/Rischioso→Media/Ostile→Difficile, §B26/§B28/Ch.14.6), a SUBQUEST → its STAKES (§B22/Ch.13.4), MSQ keeps §B11; by-the-book stat blocks §B6, no inflation (observed failure: a Tranquillo camp with 3× ~55-HP Puk, ~8× over the Facile budget). §B13 now carries the context tier-selector. §D4 PC BUILD CHECKLIST (Loremonger /pg quality, prompted by a Haiku vs Sonnet-Medium test — Sonnet Medium won, chosen for Loremonger): forces Standard Array + racials, HP = HP_ref[lvl] + CON×lvl, ALL class-table features INCLUDING the subclass at its level, spells/prepared per the class rule with names per G24, racial traits VERBATIM from 01 (never SRD defaults — Elezen = Superb Hearing not Keen Sight), naming per 07, and clean output (no meta/file-names, no image link for an invented PC). 06 stays 75 §-sections.
- v4.58: travel/camp check — THE GM ROLLS, both branches pre-generated (05 v1.94 Ch.14.6, cv19, lv7). The assistant no longer rolls: for a /viaggio travel check and a /riposo camp night check it states the danger rating + threshold and generates BOTH labelled branches in ONE turn ('Tiro ≤N (evento/agguato):' … 'Tiro >N (nessun evento):' …); the GM rolls a REAL d20 and plays the matching branch. RATIONALE: real random die (an LLM is a poor RNG) AND one message not two (stopping to wait for the result would cost a second context-reprocessing turn on a capped plan; a miss still has content — camp colour / travel quiet — so nothing is saved by omitting a branch). §B26/§B28 updated to present both branches; danger thresholds raised per GM to 5/11/16 (Tranquillo 25% / Rischioso 55% / Ostile 80%). 06 stays 75 §-sections.
- v4.56: /viaggio roll-driven + cursor-safe interrupts (05 v1.93 Ch.14.6 unified, cv17). 05 Ch.14.6 renamed 'Random Events: Travel & Camp' — one shared danger rating + single roll drives BOTH the §B26 travel check and the §B28 camp check; event menu spans GOOD/NEUTRAL/BAD (not only threats); MISS differs by branch (camp = colour event always; travel = uneventful passage / nothing). §B26 /viaggio: the in-between is now the TRAVEL CHECK vs the route's danger (hit = one vignette event, miss = nothing); the reason for walking (no Aetheryte / saving HD) is INTERNAL, never printed. §B12 + §B21: /riposo, /negozio, /cercano added to the interruptible / read-only side-output lists — all these are STATELESS at a beat boundary (no save write, no cursor advance), the next /continua resumes the exact live cursor; no 'half beat' to persist (a beat is one whole turn). cv17 mirrors the /viaggio row + a CURSOR-SAFE INTERRUPTS line. 06 stays 75 §-sections (in-place edits only).
- v4.55: REST/TRAVEL split + shop reintegration (companion 05 v1.92 Ch.14.6, cv16, lv5). §B26 /viaggio refactored = ONLY the transit beat as a travel MONTAGE (departure→passage→one optional vignette→arrival); the camp/rest clause REMOVED and migrated to the new §B28. NEW §B28 /riposo = LONG REST ONLY, never denied (GM denies by not using it), transient like /viaggio: SAFE branch (a REAL canonical shelter only — inn §A22 or a real building as makeshift, NEVER invented — fixed scene order arrivo→oste→pernottamento+cena[real FFXIV dish]→colore→sleep, closes soft §A1) / CAMP branch (outdoors when no real shelter, even urban; watch order + ONE night check vs an auto danger rating → ambush §B13 or colour event; long rest always completes). Loremonger form /riposo <luogo> [X PG] [livello N] READ-ONLY, asks PG+level only if the camp branch needs them. §B20 /voci gains a SCENE ORDER note (gather-info structure, sources voiced per tier, ref. Three-Clue Rule) — order only, outcome unchanged. §B1 COMMAND CHANNEL + cv16 command table add /riposo, /negozio, /cercano (shop engine §A20/§A22 already shared, READ-ONLY). NOTE: 06 §-sections go 74→75 (new §B28) — expected, not a break.
- v4.53: cross-model test pass (5 Claude runs + Gemini report). §B6 senses: scurovisione XOR vista cieca, never fused 'scurovisione cieca' (2 obs: Sonnet High runs); condition durations in rounds/'1 minuto', never hours ('accecato 1d3 ore' failure shape). Companion 08 v3.31: Toto-Rak NO MAGITEK/ALLAGAN (the 'terminals' are ancient Gelmorran/organic — the word itself was priming a sci-fi reframe, family-wide Gemini + Sonnet Medium drift), and Frixio IS A SYLPH (third-person idiolect, never moogle 'kupo'/pom-pom — Gemini Flash slip). REJECTED after file-check, do not add: HP cap by CR (fights SOURCE FIDELITY, already mitigated v4.52), name-vs-nature-silent (§A3 already has it + failure shape), Ultima Weapon gate (08.1 L4/L7 already gate it), rarity->price table (§A20 already has it). Stat-block PINNING considered and dropped (200-350 bespoke blocks, file bloat, loot/difficulty vary with party size). Verified: 74 §-sections unchanged.
- v4.52: ENCOUNTER PACKAGE ORDER corrected to the fix brief's own shape after GM review. Only 'Difficolta' + 'Innesco' precede the read-aloud; Terreno/Tattica/Conseguenze follow it. RATIONALE: those three are consulted DURING the fight, so hoisting them above the read-aloud pushes the fiction down the page and makes the encounter open like a form. v4.51 had wrongly grouped all setup fields above the read-aloud. Mirrored in cv14 and ov4.
- v4.51: Toto-Rak live-test pass (cv12 run) against the GM fix brief. §B1 ENCOUNTER PACKAGE — ORDER (trigger BEFORE the read-aloud, because the read-aloud describes what the trigger causes) + LAYOUT (one bold-labelled field per line); §B8 restated as a pointer to it. §B10 TELEGRAPH LIVES WITH ITS MOVE, explicitly reconciled with §B6 KEEP DESIGN COMMENTARY OUT (a telegraph is playable counterplay = mechanics; design rationale is not). §B6: Taglia mandatory in the header; NO ADDED CAPABILITIES — CHANGE CHASSIS INSTEAD; THE CR TABLE DOES NOT OVERRIDE A REAL BLOCK. §A1 verb-domain rule generalised to SPATIAL/SENSORY GEOMETRY (a described perception must be possible given the staged geometry). §A6: INTERNAL SUB-AREA NAMES ARE GM-FACING UNTIL REVEALED + A PINNED PLOT DOES NOT LICENSE ITS STAGING (counts/staging stay verified-or-generic). §A4 WIKI-REAL SUBJECTS ONLY for media links. §B9 P0(e) dark theme extended to html/body + full viewport. §B1: new [VISIONE DELL'ECO] tag (neither ALTROVE nor IN SCENA) + Echo visions hit the WHOLE party; ORIENTATION FOLLOWS [C]. §B17/§B22: [C] SUBQUEST DOSSIER for non-canonical subquests only. §B20: one non-hookable seed, inside a check tier. REJECTED from the brief after verification, do not re-apply: B2 (Lahabrea IS named in this quest per CGW — 08.1 was right), B1 in part (the Garlean/Ramuh plot IS canon), B4 (the block is a verbatim CR 2 Awakened Tree; nerfing it breaks SOURCE FIDELITY), B5 (its premise, an A1 ban on 'tutto insieme', does not exist). Verified: 74 §-sections unchanged.
- v4.50: GM test feedback pass (cv10 run, Toto-Rak). §B12 ONE ROSTER INSTANCE = ONE ENCOUNTER (the two Coeurl were merged into one '×2' fight, deleting an encounter and an interlude). §B6 LAYOUT step 3 — Vulnerabilità/Resistenze/Immunità on THREE separate lines, every label bolded, 'Descrizione visiva' bolded; + NO XP EVER ('GdS 2 (450 PE)' was printed). §B9 P0(e) inverted to a MANDATORY DARK THEME (GM was being glared at). §A21 LOOT IS NEVER OMITTED AND NEVER EMPTY ('Bottino: nessuno' on the mid-boss, no loot line at all on the final boss). §B20 /voci trigger reduced to the command alone + mandatory closing line naming /accettiamo vs /continua; §B22 START is now '/accettiamo' (canonical, no aliases) and '/subquest' is DELETED; 'lasciamo perdere'/'seguiamo l'aggancio'/'lo teniamo' aliases removed. §B1 PARTY-REFERENCE LINE restored as '⚔️ Rif. gruppo: N PG · Lv L' at the head of the footer — the v4.40 removal rested on the priming theory that TEST 1 falsified and the platform move retired; history noted inline so it is not re-litigated. §B21 LONG-SESSION FALLBACK now reads that line first. Verified: 74 §-sections unchanged.
- v4.49: §A1 — added 5 GM-approved REGISTER EXEMPLARS BY SCENE TYPE (emotivo-tenero / sociale-dialogo / città / cutscene-reveal / trial-primal), COMPLEMENTING the original 4, + an EMOTIONAL/TENDER REGISTER note (period breathes, one interior touch, close on image/silence; do NOT apply the action end-on-obstacle rules to a tender beat). Samples GM-approved; prose fixes before enshrining: fused prepositions (de Le->delle, de Il->del), clinical measurements removed from the Ifrit sample, fargli->far loro.

## 05 — Campaign

- v2.03 (LOTTO B1 dell'audit): **GLI 8 BLOCCHI `Cross-references` RIMOSSI — 2.282 B, ma non erano tutti la stessa cosa.** Sei erano **puntatori morti** (1.8, 7.8, 12.7, 13.8, 18.8, 19.7): rimandavano a capitoli dello STESSO file, in un sistema dove il modello non naviga per rimandi ma per recupero — quindi non facevano niente e competevano nel chunking. Gli altri due erano **peggio del routing**, ed è il reperto che giustifica il lotto:
  - **5.7** ristampava i valori operativi di RAISE (livello 5, slot 3°+, 1/4 PF), ARAISE (livello 9, slot 5°+, 1/2 PF), Phoenix Down/Tail, Aether Sickness (danni e cure DIMEZZATI per 2 turni) e la barra LB — tutti già in **Ch.18.3/18.4** e **Ch.6.1**, dove per giunta stanno in forma più completa (18.3 è una TABELLA con costi e limiti, 6.1 ha anche il gate del 3° segmento).
  - **9.10** ristampava la regola Tempering/Eco che vive in **Ch.4.5**.
  **Erano seconde copie di NUMERI**, cioè la cosa che diverge per prima appena una delle due viene ritoccata: bastava correggere Araise in Ch.18 e lasciare 5.7 indietro perché il file dicesse due cose diverse sullo stesso incantesimo. **Verificato prima di cancellare** che ogni valore esistesse nel capitolo d'origine — nessuna informazione persa.
  **UNA SOLA FRASE SALVATA E SPOSTATA:** «*non esiste alcun meccanismo di tempering-wipe*» stava solo in 9.10. È un divieto di invenzione, non un rimando, quindi è stata riscritta dentro **Ch.4.5** accanto alla regola che la rende vera («la protezione dell'Eco non viene MAI rimossa»), in forma positiva e operativa: *«non inventare mai un tiro, un TS o un conto alla rovescia con cui un PG diventa Temprato»*.

- v2.02: LB NO FRIENDLY FIRE (companion 06 v4.72). Prompted by a One-Shot where the party used an AoE LB2 and had to DOWN 2 ALLIES to clear the enemies. ROOT CAUSE: the DPS LB lines carried NO target scoping at all, while the Tank and Healer lines in the same section were explicitly scoped ('allies within 6/12/18 m radius') — so the assistant fell back on the 5e Fireball convention. An OMISSION, not a design choice; the fix completes the scoping the chapter already used. MADE URGENT BY v2.01: removing the save turned friendly fire from 'Dex save halves, ~14, survivable' into FULL and UNAVOIDABLE damage — at Lv4 an LB2 = 5d8 = 22.5 guaranteed downs a Black Mage (22-26 PF) outright and leaves a d8 job at 5-9 PF (exactly the observed double-down); LB3 = 8d8 = 36 downs almost every Lv4 PC. RATIONALE (recorded so it is not re-litigated): an LB is calibrated against BOSS HP (85-300, Ch.6.6) while PC HP at that tier is 22-45 (HP_ref, 02) — an effect sized to chunk a boss necessarily deletes a PC, so this is a category error, not a tuning issue; 5e precedent for ally-excluding AoEs is already in 03 (Destructive Wave 'each creature you choose', Spirit Guardians, Steel Wind Strike, Chain Lightning) and an LB sits well above a 5th-level spell; the bar charges from the WHOLE party's nat-20s (Ch.6.1 'a SHARED bar'), so the party's collective aether downing the party is incoherent, and FFXIV has zero friendly fire. NO NUMBER MOVED: the melee/AoE lever is the DIE (d12 6.5 vs d8 4.5 — melee +44% single-target boss-killer, AoE wins at 2+ enemies), and that tax was already paid with d10→d8 in v2.01; keeping friendly fire too would double-penalise an ability used 2-3 times a campaign. Positioning texture survives (you still aim the line/circle; you cannot move that turn). Edits: Ch.6.2 new binding NO-FRIENDLY-FIRE principle + the LB-ONLY BOUNDARY, Ch.6.3 DPS lines scoped 'hits every ENEMY in it', Ch.6.3 d8 rationale reworded ('everyone'→'every ENEMY caught'), Ch.6.4 area line + Ch.19 LB index row. UNCHANGED: all damage/dice/areas, Tank & Healer LBs, §6.7 names, and ENEMY AoEs (a boss's telegraphed AoE keeps its normal behaviour and Dex save — the 'shared party aether' justification does not apply to an enemy).
- v2.01: TANK+DPS LIMIT-BREAK AUDIT + AoE-LB redesign. Audit verdict: Tank LB validated (real FFXIV names Shield Wall/Stronghold + per-job LB3; defense-only mitigation ladder −1/4/−1/2/−3/4 mirrors the Healer heal ladder) — NO change. DPS LB math checked under BOTH scalings (LB dice + class/level): balanced — never a one-shot, always meaningful; the scaling is deliberately SUBLINEAR (relatively strongest at low tier), the correct anti-one-shot trade-off (a constant 'epic %' would need ~doubling the high-tier LB3 dice → boss one-shots). LB1-floor check: melee LB1 ≥ a normal average attack at every tier (guaranteed, ≈ a full single-target turn); the AoE LB1 met an average attack but sat under a premium slot-spell (Fireball+) from L5 and could be halved by a boss's save. FIX (game-designer call, Ch.6.3/6.4/6.6): ALL Limit Breaks are now UNAVOIDABLE — no attack roll, no save (matching the melee LB and FFXIV, where LBs land in full); the ranged/magical die drops d10→d8 so melee (d12, concentrated) stays the single-target boss-killer while the AoE (d8, spread) clears groups, keeping the never-one-shot ceiling. Removed the LB 'Save DC = 8+prof+key mod' line (no save remains). Recomputed AoE averages (d8, guaranteed): LB1 ~14/18/23/27/32 · LB2 ~23/32/36/45/50 · LB3 ~36/45/54/63/72. Ch.6.6 note corrected: the old '~35-45% constant' claim → the real DECLINING curve (~40-60% low tier → ~23-25% cap) + the sublinear-scaling rationale + the LB1-floor invariant. UNCHANGED: the dice-COUNT table (3/5/8 … 7/11/16), all melee values, Tank/Healer LBs, §6.7 names. Enemy telegraphed AoEs keep their Dex-save-halves (only PC LBs became unavoidable). Note: an earlier audit remark that 'DPS LB1/LB2 are unnamed' was moot — §6.7 already names them.
- v2.00: REVIVAL REBALANCE (companion 06 v4.71) — the KO/revive tiers made more distinct, a revive priced above any heal, plus a new upgraded spell. Values (Ch.5.7 / Ch.12.3 / Ch.18.3 / Ch.18.4 / Ch.19 index, all reconciled): PHOENIX DOWN full→**1/4 HP** (Uncommon, ~250 Gil); PHOENIX TAIL full→**1/2 HP** (Rare, ~1,500 Gil); RAISE stays **1/4 HP** but its casters widened from Healer-only to **Healer (WHM/SCH/AST/SGE) + Red Mage + Summoner** (FFXIV-canon raisers: Verraise / Resurrection), from L5, 3rd+ slot. NEW spell **ARAISE** = the Healer-only upgrade of Raise (4 healers only, from **L9**, consumes a **5th+ slot**) → **1/2 HP** + Mal d'Etere; it is a spell like Raise (NOT a 03 list entry, NOT a purchasable item). Mal d'Etere now lists Raise/Araise/Down/Tail (still NOT the Healer LB3). NOTE — the file already read Raise = 1/4 HP (the GM's mental model of '1 HP' was stale, no change needed there). Healer LB ladder (Ch.6.3) LEFT UNCHANGED per GM (LB1 1/4 · LB2 1/2 · LB3 3/4 heal + raise-to-3/4, no Mal d'Etere) — a proposed 'LB3 → full + raise all' revision was floated then rejected. Drops UNCHANGED: Phoenix items stay shop-only, not craftable, never loot.
- v1.99: Ch.4.5 NPC ALLIES & PRIMALS (companion 06 v4.66) — a canonical ally WITHOUT the Echo (Y'shtola, most Scions, soldiers) is NOT Tempering-safe, so they do NOT enter or fight inside a Primal battle; they support from OUTSIDE the arena while ONLY the Echo-bearing PCs (or a canonical Echo-bearer like Minfilia) confront the Primal. This is why the party is 'the only force able to fight certain enemies'. Failure shape: Y'shtola inside the Navel fighting Titan (she amplifies the aetheryte at the threshold, then the party goes in alone). Cross-ref 06 §B10/§B20.
- v1.98: Audit-consolidation companion (06 v4.64). Ch.14.2 + Ch.16.2/16.3/16.5/16.6 + Ch.20 term index: 'DC'→'CD' (8 occurrences) — the check-block TEMPLATE and worked example are reproduced in output, and 06 §A18 mandates 'CD, never DC'; the file's prose already used 'CD' (Ch.16.2 usage note), so this also removes an internal DC/CD inconsistency. No rules change.
- v1.97: Ch.10.1 companion to 06 §B6 scale-first — on-the-fly creatures are BUILT to the target GdS (chassis for lore, numbers scaled to the band-RANGE by the creature's defences), never inflated by hand; the elite-boss HP-reserve stays the only band exception. Aligns 'fair by-the-book stats for CR' with build-to-band.
- v1.96: Round-2 companion (06 v4.60). Ch.14.6 DANGER RATING GEOGRAPHY ANCHOR: a route/camp at/adjacent to a major hub or in settled/patrolled friendly territory is Tranquillo by default; Rischioso/Ostile require real wilderness/contested/infested geography (verified §A6/§A8). Fixes a patrolled near-hub leg being rated Rischioso (which then over-scaled the encounter).
- v1.95: Sylph test-corposo companion (06 v4.59). Ch.14.6 TRAVEL EVENT VALENCE SKEWS WITH THE DANGER RATING (Tranquillo→good/neutral · Rischioso→mixed · Ostile→bad; one die, no second roll). Ch.13.5/13.7 + [C] (19.3): subquest gains a SUSPEND state — `/riprendi MSQ` suspends (keeps it, resumable), `/riprendi SQ` resumes; still a single slot (a new subquest replaces it), no parked-leads LIST; `/torniamo alla MSQ` renamed to `/riprendi MSQ`. Ch.14.6 COMBAT DIFFICULTY = the danger rating on the EXISTING Ch.10.2 engine (Tranquillo→Facile/Rischioso→Media/Ostile→Difficile), by-the-book §B6, never ad-hoc. Ch.13.4/13.7 PROPORTIONATE ENCOUNTER DIFFICULTY: a subquest's fights are sized on Ch.10.2 to its stakes (Facile errand → Difficile dangerous hunt).
- v1.89 REFACTOR (data-file dedup, content-safe): save-command refs word-agnostic (defer to 06 B17, fixes stale salva/stop mismatch); Ch.1.7 per-city MSQ opening lines pointed to 08.2; Ch.19.5 RECAP+SAVE bullets compressed to 05-owned rules + pointers to 06. Ch.5.3 KEPT intact (load-bearing for 06 B24 beat->level). NO rule/number/reveal-gate changed.

## 04 — Bestiary

- v1.3: SCHEMA NOTE reframed for 06 §B6 scale-first — each block is a LORE/CHASSIS reference (type, moves, behaviour, res/vuln/imm/senses); its printed CR/HP/damage are a STARTING POINT to scale to the target GdS, NOT a verbatim authority. Consequence: known data errors here (the 12 CR/XP mismatches, the Anemone's d7) are harmless and left as-is — they scale away. Replaces the old 'stay verbatim, do NOT invent stats' note (which contradicted scale-first).
- v1.2: Puk HP data fix. The Puk entry was tagged CR 1/2 (100 XP) but carried HP 55 (10d6+20) — CR-2 HP (its CR-2 cousins Raptor/Ziz have ~51-52), a homebrewer mis-tag. Corrected to **HP 22 (4d6+8)**, matching the §B6 CR 1/2 band (24) and CON-consistent (4 HD × +2). ROOT CAUSE of the recurring "55-HP Puk" seen across tests: the model was FAITHFULLY copying this broken source (SOURCE FIDELITY / §B6 ANCHOR PRINCIPLE — 04 is a Via A source), NOT hand-inflating. So the fix is the DATA, not a rule: a §B6 'HAND-BUILT BLOCK = FAILURE' clause added in 06 v4.60 was REVERTED (false premise + it would fight the 'THE CR TABLE DOES NOT OVERRIDE A REAL BLOCK' fidelity rule). If other 04 entries show a CR/HP mismatch, fix them here likewise.

## 07 — Glossary

- v1.34: Sylph test-corposo pass (06 v4.59). Hawthorne → Biancospino, LUOGO + COGNOME (G4/G9 pins corrected from the wrong 'Capanna Hawthorne'; G1 CLASSIFY gains a NATURE/PLANT-WORD note so plant/animal/colour words render even when they read as a surname/toponym — minor names now translate automatically without a dedicated pin). G2 GRAMMATICAL GENDER AGREEMENT: article/adjective follow the Italian noun's gender, never the referent's sex or the English — 'la sentinella / le Sentinelle del Bosco / della Capanna', never 'il Sentinella' / 'di Capanna'. G10: Gods' Quiver → Faretra degli Dei pinned (recurring Gridanian order, paired with the Wood Wailers).

## 08 — MSQ Flow

- v3.42: **IL PROLOGO NON ESISTEVA NELL'ORDINE — le tre catene città ora aprono a ENTRY 0.** Emerso da un collaudo del GM: caricato il save di Sessione 0, il primo `/continua` è partito con lo sbarco a Limsa e Baderon, **saltando del tutto il risveglio dell'Eco** — cioè un pin `VISIONE DELL'ECO` del manifest ARR L1, la classe di guasto a priorità massima del progetto (lore manifest, irreversibile: una scena persa non si recupera al tavolo).
  **DOVE ERA IL BUCO.** Il contenuto non mancava: 05 Ch.1.7 (ARR CAMPAIGN OPENING, v1.18) lo descrive già per intero e canon-verificato — visione condivisa della Madrecristallo su tutti i PG insieme, NIENTE drago in fiamme, e per Limsa **la nave assalita dai pirati**. Mancava nell'**ordine**: 08 è il file autorevole per la sequenza (lo dichiara il suo stesso schema, «consult the ordered index FIRST»), e in 08.2 la catena di Limsa cominciava alla voce **1. Coming to Limsa Lominsa**. Un walker che legge la catena non vedeva niente prima della voce 1, quindi non c'era nulla da giocare prima. Il prologo non è una quest — niente giver, niente step wiki, assente da ogni elenco dei wiki — ed è esattamente per questo che si perde: è l'unico beat che nessuna fonte d'ordine elenca.
  **LA CORREZIONE, in tre punti perché 08 governa l'ordine in tre punti.** (a) Pin del manifest ARR L1: dichiara che la visione **È il beat 0**, giocato PRIMA della voce 1 e mai fuso dentro di essa, e nomina lo stato di save che lo rende dovuto — MSQ su `Coming to <City>` con «Ultimo step completato» che nomina la Sessione 0 / l'inizio campagna significa che il prologo NON è ancora avvenuto (05 Ch.1.7: si gioca al primo `/continua` dopo il caricamento di save-0). (b) Blocco Roadmap Lvl 1: riga OPENING che punta al pin e a 05 Ch.1.7. (c) 08.2: **voce 0 in tutte e tre le catene**, numerata 0 e non 1 proprio perché non è una quest.
  **ASIMMETRIA DICHIARATA, per non farla "aggiustare" a qualcuno.** Solo Limsa porta uno scontro pinnato (l'assalto dei pirati sul ponte = primo Pacchetto Incontro della campagna, verificato in 05). Gridania e Ul'dah hanno l'arrivo in carrozza e **nessun combattimento pinnato**: la voce 0 lo dice esplicitamente e vieta di promuovere un incidente a scontro obbligatorio «per pareggiare» Limsa. Le cinematic d'apertura per città **non sono documentate su ConsoleGamesWiki** (verificato in questa passata: le pagine `Coming to Limsa Lominsa` / `Coming to Gridania` / `Coming to Ul'dah` cominciano tutte a città già raggiunta, con Ryssfloh / Bertennant / Wymond, e non contengono né visione né scontro), quindi per le altre due città si resta generici invece di inventare — §A6/§A7.
- v3.33: Titan TRIAL PIN corrected (companion 06 v4.66) — the Navel arena IS inside the O'Ghomoro volcano, so magma in the SURROUNDINGS is canon (volcanic ambience OK); but Titan's BODY is rock (not a fire/magma creature) and the instant-death is the knockback FALL off the platform edge (not a lava-pool theme). Titan pinned as BIPEDAL (torso on rock legs, stands and stomps — the retest's 'legless' torso was a model invention, not in the pin). Two failure shapes now named in the pin.
- v3.32: TRIAL PINS for ALL ~24 MSQ trials ARR→EW (companion 06 v4.65 F5), each verified on ConsoleGamesWiki (§A14; Gamer Escape 403'd WebFetch). Each pin caches ELEMENT/theme · ARENA + its real instant-death/hazard · BOSS VISUAL · signature moves + phase, so the assistant themes a trial correctly without drift. ARR pins added INLINE in the 08.2 index (Ifrit/Titan/Garuda/Ultima/Leviathan/Ramuh/Shiva); HW→EW pins in a NEW consolidated "TRIAL PINS — HW → EW" block before 08.OST (Vishap[defense]/Bismarck/Ravana/Thordan/Nidhogg · Susano/Lakshmi/Shinryu/Tsukuyomi · Titania/Innocence/Hades/Elidibus · Zodiark/Hydaelyn/Endsinger + a Zenos solo-duel note). Key corrections locked: Titan = EARTH, arena over a CHASM (death = knocked off the edge, NOT lava), body of living rock not obsidian. Non-primal bosses (Thordan/Nidhogg/Hades/Elidibus/Endsinger) pinned by nature/theme; Vishap pinned as a DEFENSE trial; Zenos as a solo duel, not a trial.
- v3.26: ARR REVAMPED-DUTY LOCK (Toto-Rak) corrected - Coeurl O' Nine Tails is an OCHU (plant/Seedkin) mini-boss (x2), NOT a coeurl and NOT 'sole boss Graffias'; the earlier 'NOT plant/Ochu' note was wrong. Graffias stays the diremite final boss. Aligns with 06 v4.27 NAME != NATURE.
