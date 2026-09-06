# FFXIV × D&D 5e — assistente per il GM

Tre assistenti che girano su un chatbot ospitato (Gemini Gems, OpenAI Projects) e aiutano un GM a
condurre una campagna homebrew FFXIV in D&D 5e: uno **conduce la campagna**, uno **prepara one-shot**,
uno **risponde da wiki**. Non c'è codice in esecuzione: c'è una casella di istruzioni e dei file di
conoscenza, e tutto il comportamento nasce da come sono scritti.

**Questo file è una MAPPA, non un regolamento.** Dice dove vive cosa e come si lavora. Non ripete
nessuna regola: se lo facesse, diventerebbe una copia che diverge, che è il guasto più caro della
storia di questo progetto. È dev-only e **non va mai allegato a un assistente.**

---

## La cosa da capire prima di toccare qualsiasi file

Esistono **due strati**, e sbagliare quale possiede cosa è la causa di quasi ogni guasto che abbiamo avuto.

| | **CONTROL LAYER** | **KNOWLEDGE** |
|---|---|---|
| cos'è | la casella delle istruzioni | i file allegati |
| presenza | **100% in contesto, ogni turno** | recuperato a pezzi, per similarità |
| possiede | **QUANDO fare una cosa** — quale comando è stato digitato, cosa legge, cosa cambia, che forma ha la risposta | **COM'È FATTA una cosa** — layout, prosa, tabelle, contenuto della campagna |
| dimensione | ~6-8 KB, e la dimensione conta | centinaia di KB, e la dimensione non conta |

**La regola, misurata:** *il knowledge dice com'è fatta una cosa, le istruzioni dicono quando farla.*
Un file di conoscenza può essere grande; non può essere **imperativo**. Quando 06 conteneva
comportamento, quel comportamento competeva col control layer e **vinceva** — perché arrivava più
lungo, più dettagliato e più imperativo della riga di dispatch.

Due corollari che costano cari se si dimenticano:
- **Le istruzioni non elencano mai cosa consultare.** Né `§B6` né «la sezione dello stat block»: è la
  lista in sé a essere un ordine di recuperare, eseguito a ogni turno. Il formato si recupera da solo
  mentre scrivi, perché lì la query è ricca di vocabolario.
- **Il knowledge non nomina mai un comando.** Il token è l'amo che pesca i pezzi sbagliati.

---

## I file

### Control layer — si incolla nella casella istruzioni
| file | | |
|---|---|---|
| `Instructions_Campaign.txt` | **cv** | conduce la campagna MSQ |
| `Instructions_OneShot.txt` | **ov** | prepara one-shot autoconclusivi |
| `Instructions_Loremonger.txt` | **lv** | wiki, regole, generatori. **Read-only** |

Stessa struttura nei tre: `role` · `knowledge` · `scope` · `commands` · `beat`/`act`/`output` ·
`output_contract` · `contract`. Il blocco `output_contract` è **identico al byte** nei tre file.

### Knowledge — si allega
| file | possiede |
|---|---|
| `01_Manual.md` | razze, Job, incantesimi, creature — quattro manuali in quattro PARTI numerate |
| `05_Campaign.md` | regole di campagna |
| `06_Procedures_and_Format.md` | **tutti i formati**, 71 sezioni §. Il file che conta di più |
| `07_Glossary.md` | nomi e rese italiane vincolanti |
| `08_MSQ_Flow.md` | indice MSQ ordinato, pin delle cutscene, tabelle OST |

### Dev-only — non si allega mai
| file | |
|---|---|
| `CHANGELOG.md` | cosa è cambiato, quando e **perché**. Ogni intervento con la sua misura |
| `Project_Memory.md` | le lezioni: cosa abbiamo provato, cosa ha fallito, cosa non riproporre |
| `README.md` | questo |
| `combat_tracker.html` | l'app web standalone che il GM apre in un browser al tavolo; si alimenta incollando il blocco `### 🗡️ Pacchetto Incontro` generato dall'assistente per tracciare turni, PF, CA e condizioni |
| `map_navigator.html` | l'app web standalone per la navigazione interattiva tra le mappe ufficiali di FFXIV tramite API di ConsoleGamesWiki, cursore Party, transizioni automatiche tra zone confinanti, motore toponomastico (07/08) e sincronizzazione con il GEM |

---

## Come si allega

Cinque file, gli stessi ovunque: **`01_Manual` · `05` · `06` · `07` · `08`.** Sta nel limite di OpenAI
Projects (max 5 file, istruzioni entro 8.000 caratteri) e va bene anche sui Gemini, che non hanno vincoli.

I numeri **02, 03 e 04 non esistono più come file**: sono le PARTI dentro `01_Manual`. Il buco nella
numerazione è voluto — i rimandi negli altri file usano il NUMERO, che identifica la parte, quindi
continuano a risolvere. Le aggiunte future vanno dentro la parte che le riguarda.

---

## Come si lavora

Queste non sono buone maniere: sono le sei cose che, non facendole, sono costate settimane.

**1. Una modifica per volta, contro un baseline che ha una buona corsa misurata.** Quattro riscritture
integrali hanno introdotto una regressione ciascuna, tutte silenziose.

**2. Una singola run non è una misura.** Il guasto tipico è intermittente: una versione ha fatto 4/4 ed
è caduta alla prima ripetizione. **Due run in chat nuove**, e si annota *quale turno* cade, non solo se
cade.

**3. Prima di riscrivere una regola che sembra rotta, cerca la contraddizione.** Otto tentativi falliti
su un bug si sono spiegati con un **fossile**: una riga in §B2 che ordinava il comportamento opposto,
sopravvissuta al divieto che l'aveva superata.

**4. Una regola disattesa non si riscrive: si rende CONTABILE.** §A9 tiene i controlli contati (oggi
nove). Tre difetti di fila — bottino del boss, musica, nomi delle stanze — erano regole *già scritte* e
ignorate; il conteggio le ha fatte sparare.

**5. Una correzione non porta con sé la sua giustificazione.** Il perché di una modifica va nel
`CHANGELOG`, mai nel file di conoscenza: lì la frase «non è X, è Y» non è una prova, è un **secondo
candidato**, e mette il termine sbagliato nello stesso pezzo recuperabile di quello giusto. Il test è
uno: *se togliessi la negazione, da dove arriverebbe l'errore?* Se solo dalla frase stessa, si toglie.
Se dalla wiki che facciamo leggere, o dal nome stesso, resta.

**6. E si ritira, se non basta.** Una regola resa contabile che fallisce **due volte** non si riscrive
una terza: o è un limite del modello, o è nello strato sbagliato. Esce dal file e resta come limite
noto in `Project_Memory`. Senza questo, i file crescono e basta.

### Il test standard
Chat nuova, un messaggio per turno, e si guarda **quale** turno sbaglia:

```
/pippo   →  una riga: non esiste
/carica  +  blocco save   →  Save caricato: …
/continua                 →  il beat
/salva                    →  Ancora save: … + blocco save + riga di diff
```

`/pippo` non è uno scherzo: verifica che il roster sia chiuso, ed è il turno che storicamente innesca
i guasti di dispatch.

---

## Il modello

Il **pavimento** è Gemini 3.6 Flash: una regola vale se tiene lì. Il Loremonger gira due gradini più
sotto (Haiku 4.5 / Gemini 3.5 Flash-lite), quindi il suo file è più magro. Sonnet 5 e Opus 5 fanno
girare tutto e assorbono le ambiguità — utile saperlo quando una regola non tiene sul pavimento: la
scelta fra «riscriverla» e «cambiare modello» è una decisione di progetto, non un fallimento.

La configurazione (modello **e** livello di ragionamento) va annotata insieme a ogni risultato: una
prova fatta a impostazioni diverse non è confrontabile.

---

## Dove sta il resto

- **perché una cosa è com'è** → `CHANGELOG.md`, in ordine inverso di data
- **cosa abbiamo già provato e non ha funzionato** → `Project_Memory.md`, sezione LEZIONI, e
  `2.16 REJECTED DECISIONS — do not re-propose`

Prima di proporre un'idea che sembra ovvia, cercala lì: buona parte delle idee ovvie è già stata
provata, e alcune sono già costate care.
