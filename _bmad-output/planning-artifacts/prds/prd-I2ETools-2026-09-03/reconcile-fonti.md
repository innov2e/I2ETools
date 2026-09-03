# Riconciliazione del PRD con le fonti

**Data:** 3 settembre 2026 · **Oggetto:** `prd.md` + `addendum.md` confrontati con i due corsi in `docs/templates/`, la checklist qualità, gli artefatti già costruiti e gli strumenti in `tools/`.

Il PRD è corto di proposito e va bene così. Questo documento non chiede di allungarlo: chiede di verificare, voce per voce, se qualcosa di **portante** è caduto per strada. Dove propongo un'aggiunta, è una riga o un campo, non una sezione.

Fonti lette:
`docs/templates/0 Corso Prompting di base - Completo/` (LEGGIMI.txt, index.html, lezioni/lezione-01/index.html, lezioni/lezione-01/esercitazioni/tool-token.html, docente/lezione-01.html, materiali/bok.html, materiali/checklist-qualita.html, materiali/casi-studio.html, qualita/LEGGIMI.txt, qualita/Checklist v0.01, qualita/verifica_corso.py) · `docs/templates/0 Prompting Avanzato - Modulo 1/` (LEGGIMI.txt, index.html, impianto.html, comune/commessa.html, percorsi/finance/modulo-01/docente.html) · `memoria-e-contesto-ai.html` · `normativa-ai-scadenze-obblighi.html` · `tools/costruisci-aula.py` · `tools/regia-server.py` · `index.html` · `.gitignore`.

---

## 1. I vuoti che contano, in ordine di peso

### 1.1 — «Strumenti di qualità» è un'espressione ambigua che può far cancellare il filo conduttore didattico del corso base

**PRD §3 (glossario, «Consegna»)** e **FR-7**: *«Un comando produce la consegna a partire da un corso, rimuovendo regia e strumenti di qualità»*, con conseguenza verificabile *«Nella consegna non compaiono file di regia né strumenti di controllo qualità»*.

Nel corso base esistono **due cose diverse che si chiamano entrambe «qualità»**:

- `qualita/` — gli strumenti di verifica. `qualita/LEGGIMI.txt`: *«Questa cartella NON fa parte del materiale didattico… va rimossa dai pacchetti destinati agli studenti, come la cartella "docente"»*. Questa si toglie.
- `materiali/checklist-qualita.html` — **la Checklist di Qualità degli output**, sette domande. `index.html` del corso la descrive come *«Filo conduttore»*, e il testo della pagina dice: *«nel debrief della Lezione 1 le sette righe si fanno emergere dai partecipanti… Cresce durante il corso»*. È materiale per i partecipanti, è **il** filo che attraversa tutte e cinque le lezioni, ed è il ponte verso il deliverable finale. Questa deve restare.

La regola operativa vera, ricavabile dalle fonti, è **per cartella, non per parola**: si rimuovono `docente/` e `qualita/` (e nel corso avanzato i quattro `docente.html`), null'altro. FR-7 come è scritto autorizza a fare la cosa sbagliata, e a farla in modo automatico e silenzioso.

**Correzione minima:** FR-7 nomina le cartelle da rimuovere invece della categoria; il glossario §3 distingue «regia e strumenti di verifica» da «materiali trasversali».

### 1.2 — La regola dei dati fittizi e del divieto di dati reali non esiste nel PRD

È l'unica regola che entrambi i corsi ripetono in tre punti ciascuno.

- LEGGIMI avanzato, sezione **DATI**: *«Societa', persone, importi, siti, contratti e riferimenti normativi degli esercizi sono interamente fittizi e costruiti per l'aula.»*
- `comune/commessa.html`: *«Tutto quello che segue è inventato… Non riproducono alcuna commessa, cliente o documento reale.»*
- `materiali/casi-studio.html`: *«Nessun partecipante deve caricare documenti aziendali reali su strumenti non approvati dalla propria organizzazione.»*
- LEGGIMI base, avvertenza 2: *«Un documento aziendale interno va usato solo se lo strumento e' quello approvato dall'organizzazione.»*
- Hub Lezione 1: *«VINCOLI: non si scrive codice, non si usano dati reali»*.

Il PRD non ne parla in nessun punto. **§4.5 «Firma, data e licenza»** è il posto naturale: firma, data, licenza e **dichiarazione di finzione dei dati** sono la stessa famiglia — sono ciò che rende il materiale consegnabile a un cliente aziendale. Ed è verificabile, quindi appartiene anche a **FR-17**: un artefatto che contiene un caso, un dataset o un documento e non dichiara che è inventato è un rilievo.

Non è un dettaglio redazionale: è la premessa che permette di portare in aula esercizi su bilanci, contratti e clienti morosi.

### 1.3 — La preparazione d'aula anticipata non ha un requisito, e rischia di finire nella regia

Il PRD ha un solo meccanismo di preparazione: il link di configurazione di **UJ-1 / FR-10**. Le fonti ne descrivono altri due, entrambi bloccanti per la riuscita della giornata:

- LEGGIMI avanzato, **PREPARAZIONE DELL'AULA**: *«I documenti della Data Room del percorso vanno caricati in anticipo su OneDrive o SharePoint dei partecipanti: Copilot li richiama da li'. Farlo in aula costa venti minuti che nella scaletta non ci sono.»* È un prerequisito **a carico di terzi** (l'IT del cliente), da concordare giorni prima.
- LEGGIMI base, **TRE AVVERTENZE OPERATIVE**: la ricerca sul web va disattivata in 1.1, 1.2 e 4.3, *«altrimenti… il difetto da osservare resta invisibile»*.

La seconda è il caso interessante, perché **compare da entrambi i lati**: `docente/lezione-01.html` la tratta come regia (*«Verificate personalmente, prima della lezione, che sullo strumento scelto la ricerca sia disattivabile»*), ma `lezioni/lezione-01/index.html` — pagina consegnata — la ripete al partecipante sotto il titolo *«Una impostazione da controllare prima di iniziare»*.

Il PRD tratta la separazione come binaria (**§4.2**, **FR-5**: la regia *«non è mai dentro un file consegnato»*). Applicata alla lettera a un generatore automatico, questa regola **cancella dal materiale dello studente istruzioni che oggi ci sono e devono restarci**. Manca la categoria intermedia: *prerequisito d'aula*, che vive nella consegna e ha una versione più dettagliata nella regia.

**Correzione minima:** una riga nel glossario §3 accanto a «Regia», e una conseguenza verificabile in FR-7 del tipo «la consegna conserva i prerequisiti d'aula».

### 1.4 — Il registro dei colori delle tre parti è normativo, e il PRD non lo sa

Checklist v0.01, §4.2, sotto la tabella del gruppo S: **«Registro dei colori. Va rispettato in tutti i corsi, non solo in questo»** — Lezione/indaco/`--c-lez`, Esercitazioni/verde/`--c-ese`, Materiale/ambra/`--c-mat`. Il controllo **S3 è BLOCCANTE**: `stile.css` deve definire `body[data-sezione="…"]` e le tre variabili. S1, S2 e S5 sono GRAVI e coprono `data-sezione` sul `<body>`, la fascia `class="sezbar"` e la legenda nell'hub.

Il PRD non lo nomina mai. L'addendum lo cita come descrizione (*«tre parti con codice colore stabile: lezione (indaco), esercitazioni (verde), materiale (ambra)»*), ma un addendum descrittivo non vincola nulla.

Conta perché **§8, domanda aperta 3** propone che il generatore assorba «il blocco comune di stile e comportamento». Se quel blocco viene progettato ignorando che esistono già tre variabili obbligatorie con un registro dichiarato valido *per tutti i corsi*, il generatore romperà S3 al primo corso rigenerato. È una convenzione con vent'anni di vita davanti che costa una riga citarla.

### 1.5 — Il Body of Knowledge EQF non è un file: è ciò che rende il corso un'offerta formativa, e non compare nei metadati

**C6 è BLOCCANTE**: *«`materiali/bok.html` esiste, cita EQF e contiene i tre descrittori»*. La pagina è molto più di un adempimento: dichiara il **livello EQF 4** con la motivazione, segnala l'elemento che sconfina in 5 (*«la responsabilità piena e non delegabile sull'output diffuso (area A9)»*), spiega perché il descrittore 2017 è «responsabilità e autonomia» e non «competenze», e raccorda al D.lgs. 13/2013. Chiude con un'onestà rara: *«La collocazione è una stima argomentata, non un referenziamento formale, che spetta a un'autorità nazionale.»* Le dieci aree hanno un peso percentuale e la mappatura alle lezioni (`A2 · 15% · L1, L2`).

**PRD FR-1** elenca i campi facoltativi del manifest: *«durata, numero di lezioni, livello, prerequisiti, percorsi disponibili, provenienza»*. «Livello» è generico. Se il manifest è *«unica fonte di verità per navigazione, mappa e catalogo»* (**FR-1**), il livello EQF e il rimando al BoK sono esattamente ciò che un catalogo formativo deve esporre — e costano un campo facoltativo, non una sezione.

C'è anche un vuoto di coerenza: nessun requisito lega un corso al suo BoK, quindi niente impedisce che le lezioni cambino e il BoK resti fermo. La checklist controlla che il file esista, non che dica il vero.

### 1.6 — I tre controlli a giudizio spariscono, e sono quelli che proteggono il prodotto

**PRD §4.6** li nomina — *«trenta controlli automatici e tre a giudizio»* — e poi **FR-18** parla solo di codice di uscita e rilievi bloccanti. Ma la checklist è esplicita: *«Questi tre non producono un codice di uscita. Producono una dichiarazione dell'agente, che va scritta e non sottintesa.»*

I tre sono:
- **P1** — *«Per ogni scelta strutturale rilevante, l'agente sa indicare l'alternativa scartata e perché. Se non sa dirlo, non ha scelto: ha eseguito.»*
- **P2** — *«Design professionale ma molto accattivante… Verifica pratica: aprendo tre pagine a caso si capisce che appartengono allo stesso corso e in quale parte ci si trova.»*
- **P3** — *«Prosa italiana naturale, senza gergo non spiegato e senza formule vuote. Nessun testo scritto per riempire uno spazio.»*

Sono l'antidoto esatto alla contro-metrica **SM-C2** (*«oltre una certa soglia la conformità scoraggia le pagine strane, che sono il prodotto»*): i trenta controlli automatici misurano la conformità, i tre a giudizio misurano se la pagina è viva. Toglierli lascia in piedi solo la metà che il PRD stesso teme.

Nella stessa famiglia, e altrettanto assente: la regola di governo dell'agente che costruisce i corsi — *«Non deve mai disattivare un controllo per farlo passare. Se ritiene che un controllo sia sbagliato, lo segnala e chiede, invece di modificarlo di propria iniziativa»* — e la sua gemella sulle soglie: *«Cambiarle è legittimo… ma la modifica va dichiarata insieme al motivo»*. Sono i requisiti di una modalità di lavoro reale (un agente che scrive i corsi), non teoria.

### 1.7 — «Un esercizio senza materiale allegato non entra nel corso»

`impianto.html`, sezione **La regola dei materiali**: *«Ogni esercizio del laboratorio nasce da un documento reale della Data Room, non da una descrizione a parole. Il partecipante apre un file, lo incolla o lo carica, e lavora su quello. Un esercizio senza materiale allegato non entra nel corso. Vale anche per gli esercizi di riserva: la banca di varianti attinge alla stessa Data Room.»*

È una regola di ammissione del contenuto, formulata come divieto, verificabile, e coerente con la terza parte «Materiale» (ambra) del corso base e con il controllo **L10**. Il PRD non ha nulla di equivalente. È il tipo di vincolo che, se non scritto, sparisce al primo modulo scritto di fretta — e produce esattamente il corso da webinar che **§1** dice di non voler fare.

### 1.8 — «Gli strumenti non salvano nulla» ha una conseguenza che il PRD non trae

**FR-9** stabilisce il vincolo: *«Nessuno stato conservato fra sessioni; riaprendo si riparte dai valori iniziali.»* Corretto e coerente con tutto il resto.

Ma le fonti ne traggono un obbligo che il PRD non ha:
- LEGGIMI base: *«ATTENZIONE: gli strumenti della Lezione 5 non salvano nulla. Il file va copiato fuori dal browser prima di chiudere la pagina.»*
- LEGGIMI avanzato: *«Gli strumenti non salvano nulla: quello che si produce va copiato fuori prima di chiudere la pagina.»*
- `materiali/checklist-qualita.html`: *«Le caselle non vengono salvate: la pagina serve durante la valutazione, non dopo.»*

Il deliverable dichiarato del corso base (*«una libreria di cinque prompt documentati, collaudati e validati da un collega»*) **dipende interamente** dal fatto che lo strumento della Lezione 5 permetta di portare fuori il risultato e lo dica ad alta voce. Nel glossario **§3** l'esportazione è facoltativa: un tool *«può produrre un file da scaricare»*.

**Correzione minima:** una conseguenza verificabile in FR-9 — un tool che produce un deliverable dichiara l'assenza di persistenza e offre una via d'uscita del dato. Costa una riga e salva il prodotto finale di un corso da 10 ore.

### 1.9 — La convenzione delle anticipazioni e il glossario ancorato alla lezione

**C5** (BLOCCANTE) chiede che ogni voce del glossario dichiari la lezione che la introduce. **C7** (GRAVE) vieta di usare un termine prima di quella lezione, se non marcato `class="anticipo"` con una glossa. La checklist spiega il perché e ne rivendica l'effetto: *«la marcatura obbliga chi scrive a decidere se l'anticipazione serve. Se non vale una glossa, probabilmente il termine andava evitato.»* E mette un paletto sui falsi positivi: aggiungere una voce a `TERMINI_COMUNI` *«è una decisione editoriale, non una scorciatoia per far passare il controllo: va fatta solo quando il termine è ambiguo in italiano corrente, mai per silenziare un'anticipazione reale.»*

Nulla di tutto questo è nel PRD. È una convenzione di scrittura che vincola ogni artefatto nuovo, non solo i corsi, e che ha già una macchina che la applica.

### 1.10 — Il Progetto NEMBO: un mondo condiviso che il modello dei dati non sa rappresentare

`comune/commessa.html` è un artefatto di tipo nuovo: non è una lezione, non è un tool, non è materiale di un percorso. È **il contesto canonico di quattro percorsi** — *«Progetto NEMBO: una sola commessa, quattro scrivanie diverse… Stessi nomi, stesse date, stessi numeri. Chi legge questo dossier una volta non deve più ricostruire il contesto a ogni esercizio.»* Contiene un'anagrafica precisa (P-2026-NEMBO, 18.400.000 €, fermata 07/09→26/10/2026, penale 0,5% a settimana, dodici nomi propri, i centri di costo CC-41xx) che ogni esercizio di ogni percorso deve rispettare.

Il glossario **§3** ha «Percorso» (variante verticale) e «Provenienza» (da quale corso viene un tool). Non ha niente per un **mondo narrativo condiviso**. Conseguenze:

- il manifest (**FR-1**) non può dire che il Modulo 2 vive nello stesso mondo del Modulo 1;
- nessun controllo (**FR-17/FR-18**) può accorgersi che un modulo nuovo scrive «Vertek Power S.r.l.» invece di «S.p.A.», o cambia il valore del contratto;
- **§2.1** promette *«Restare aggiornato senza rifare: quando la normativa cambia, cambiare in un posto solo»* — lo stesso problema, applicato ai dati di finzione, non è nominato.

L'impianto dichiara anche una dipendenza forte che il campo facoltativo «prerequisiti» copre solo a metà: *«La sequenza è cumulativa: ogni modulo usa il deliverable del precedente come materiale di partenza. Chi salta un modulo arriva al successivo senza l'oggetto su cui lavorare — ed è voluto.»*

### 1.11 — Vincoli fisici e strumentali dell'aula, oltre al proiettore

**§4.4 «Modalità d'aula»** copre luce, proiettore e rete. Le fonti ne dichiarano altri, che sono vincoli di progettazione degli artefatti, non contorno:

- `index.html` corso base: *«Aula 8–16 partecipanti, un dispositivo a testa»*; *«Learning by doing: 65% laboratorio, 25% teoria, 10% debrief»*.
- Hub Lezione 1: *«Serve un solo strumento, in versione gratuita, e deve essere lo stesso per tutta l'aula: il valore della lezione sta nel confronto fra i risultati.»*
- `docente/lezione-01.html`: *«Gli abbonamenti a pagamento non sono necessari. Se qualcuno in aula ne ha uno, chiedetegli di usare comunque il modello gratuito durante gli esercizi»*; e l'esclusione motivata di Playground e AI Studio (*«Sono ambienti tecnici… mostrano parametri che nell'interfaccia chat non esistono»*).

«Piano gratuito, stesso strumento per tutti, nessuna API» è un vincolo che decide cosa un tool può presupporre. Il PRD lo dà per scontato e quindi non lo protegge.

### 1.12 — L'allineamento fra i due percorsi non è un invariante del PRD

**C3** (BLOCCANTE): *«Per ogni lezione esiste la guida corrispondente, e viceversa»*. **C4** (BLOCCANTE): *«Nessuna pagina fuori da `docente/` vi rimanda»* — è ciò che rende la cartella cancellabile senza collegamenti rotti, e il LEGGIMI lo dichiara al lettore: *«si puo' cancellare quella cartella e il materiale per i partecipanti resta completo e navigabile»*. **C8**: nessuna pagina orfana.

**FR-6** ha l'invariante giusto ma solo per i deep-dive (*«Un segnaposto senza la sua regia, o una regia senza segnaposto, viene segnalato»*). Per i corsi, FR-6 e FR-7 non chiedono l'allineamento uno-a-uno. La nota **L8** della checklist racconta perché serve: *«ha già trovato un errore reale: una guida del docente che elencava dieci domande mentre il test ne aveva sette, perché una sostituzione automatica era fallita in silenzio.»* Ed è un errore che oggi è ancora lì: `docente/lezione-01.html` contiene la frase duplicata *«Il test è di sette domande. Il test è di sette domande.»*

---

## 2. Intento qualitativo a rischio

Questa parte non produce requisiti. Produce il motivo per cui, quando qualcuno leggerà il PRD fra un anno per costruire il generatore, non trasformerà il materiale in un template riempito.

### 2.1 La filosofia didattica: predire, sbagliare, costruire

Attraversa tutte le fonti e nel PRD sopravvive in una sola subordinata di **UJ-1** (*«gli ricordano di far indovinare la stanza prima di rivelare l'esito»*), senza diventare nulla.

- **Il criterio si costruisce, non si consegna.** `checklist-qualita.html`: *«Va costruita in aula, non consegnata… Una checklist ricevuta si legge; una checklist che si è contribuito a scrivere si usa.»* `docente/lezione-01.html`: *«La checklist va fatta emergere, non distribuita… Trascriveteli alla lavagna con le loro parole, non con le vostre… Chiudete facendo trascrivere la checklist a ciascuno. Chi la scrive a mano la usa; chi riceve un foglio no.»*
- **L'errore è il materiale.** La chiave del test non elenca risposte: per ogni domanda dà *«il distrattore che merita una discussione, perché l'errore è più istruttivo della risposta giusta»*. `percorsi/finance/…/docente.html` fa lo stesso lavoro sui distrattori (*«La confusione tipica è fra la 2 e la 3…»*).
- **Le trappole volontarie.** `casi-studio.html`: *«Trappola volontaria. Il risparmio del marketing non è un risparmio: è uno slittamento di fatturazione. Un modello che si limita a calcolare la differenza lo classificherà come positivo… ed è il punto didattico dell'esercizio.»* Lo stesso in Finance: *«Quasi sempre l'aula indica i 142.000 €, che è il numero più grande — ed è giusto per caso… hanno trovato la conseguenza, non la causa.»*
- **La predizione prima della rivelazione.** L'apertura della Lezione 1: *«ognuno scrive su un foglio il prompt che userebbe oggi… Non anticipate a cosa serve.»*

**FR-11** è il parente più prossimo (*«Almeno un caso porta a una condizione limite o a un esito controintuitivo»*) ed è molto più povero: sposta il lettore in un punto interessante, non gli chiede di scommettere prima. **§4.3** parla di *«autovalutazioni che diagnosticano invece di dare un voto»* — è il pezzo di questa filosofia che è sopravvissuto, e da solo si legge come una preferenza di interfaccia anziché come una postura.

### 2.2 La voce

Due registri distinti e coerenti, mai dichiarati:

- **Al partecipante**, il «voi» e il perché prima del cosa: *«Scrivete qualcosa e guardatelo frammentare. Le parole comuni restano intere, quelle lunghe o rare si spezzano — ed è lì che si capisce perché si parla di token e non di parole.»* (`tool-token.html`)
- **A chi conduce**, l'imperativo operativo e il consiglio con il motivo: *«Introducete il Banco dei 4 Pilastri qui, non prima. Se lo aprite durante la teoria, l'aula smette di ascoltare.»*; *«Non tagliate le slide 8, 11 e 12.»*; *«Non è tempo di riserva. Se lo mangiate, la lezione perde il suo prodotto.»*

P3 lo codifica in negativo (*«senza gergo non spiegato e senza formule vuote»*); le pagine lo praticano in positivo. Il PRD scrive bene ma non dice mai nulla sul registro degli artefatti, e la voce è metà del prodotto.

### 2.3 L'onestà epistemica come convenzione ricorrente

Compare, con la stessa forma, in fonti che non si parlano fra loro:

- `bok.html`: *«La collocazione è una stima argomentata, non un referenziamento formale.»*
- `normativa-ai-scadenze-obblighi.html`, configuratore: *«A cosa serve e a cosa no. È uno strumento didattico… non è una valutazione di conformità, non sostituisce l'analisi del caso concreto»*; footer: *«Non costituisce parere legale»*.
- `memoria-e-contesto-ai.html`: *«Come sono calcolati i numeri. Stime, non fatturazione: 1 pagina ≈ 500 parole… I prezzi al milione di token variano per modello e fornitore: metti il tuo.»*
- `tipi-di-ai.html`: *«dove il dibattito è aperto (AGI, teoria della mente…) il testo lo segnala esplicitamente anziché presentare una posizione come consenso.»*
- Checklist v0.01, §7: *«Che cosa questa versione non copre ancora. Dichiarato per onestà e come lista di lavoro per la v0.02.»*

**FR-9** ne cattura un quarto (*«Le stime dichiarano come sono calcolate»*). Il resto — dichiarare il limite di validità, distinguere stima da fatto, segnalare il dibattito aperto invece di risolverlo — è la convenzione che rende il materiale credibile davanti a un dirigente e difendibile su un tema normativo. Appartiene a **§4.5**, accanto a firma, data e licenza.

### 2.4 L'abbondanza dichiarata, e perché SM-C1 non la riguarda

Le soglie della checklist non sono burocrazia: *«`banca_min` 20 — sotto le 20 voci l'esercizio non regge senza docente»*, *«`copione_parole_min` 60 — sotto, il copione non è utilizzabile da un doppiatore»*, *«`slide_min` 8 — sotto le 8 slide non c'è una parte teorica strutturata»*. La Lezione 1 dichiara *«4 esercizi, banca di 44 casi»* — più del doppio del minimo.

La contro-metrica **SM-C3** (*«ogni pezzo di infrastruttura è manutenzione a carico di una persona sola»*) e **SM-C1** (*«dieci pagine deboli valgono meno di tre manipolabili»*) sono giuste per gli artefatti e per gli strumenti, e vanno lette come **non applicabili alla banca dei casi**, dove l'abbondanza è il requisito. Un lettore veloce del PRD userebbe SM-C1 per giustificare un laboratorio con otto varianti.

### 2.5 L'identità visiva come criterio, non come gusto

**P2** ha una verifica praticabile che vale la pena non perdere: *«aprendo tre pagine a caso si capisce che appartengono allo stesso corso e in quale parte ci si trova»*. È la formulazione utile della **domanda aperta §8.3** sugli stili duplicati, vista dal lato dell'effetto invece che da quello del debito. La risposta a «il generatore assorbe il debito o no?» dovrebbe passare da qui.

---

## 3. Contraddizioni e cose sovra- o sotto-dichiarate

### 3.1 §1 promette al presente ciò che è un obiettivo

*«Ogni artefatto funziona senza rete, si proietta, si stampa e si porta via.»* Lo stato reale, misurato sulle nove pagine di contenuto alla radice:

| Promessa | Stato |
|---|---|
| Vista da proiezione (FR-13) | 1 pagina su 9 (`memoria-e-contesto-ai.html`); traccia parziale in `tipi-di-ai.html` |
| `@media print` (FR-14) | 2 pagine su 9 |
| Footer con data | 6 su 9; `timeline_tecnologica.html` non ha footer |
| Nome del produttore (FR-16) | 2 file lo nominano (`index.html`, `Il Libro dei Prompting.html`) |
| Licenza (FR-16) | **0 su 9** |
| Link alla versione viva (FR-16) | **0 su 9** |
| Logo incorporato (G1 della checklist) | 0 su 9 |

Coerente con **§6.1** («Riconduzione dei dieci artefatti esistenti»), ma **§1** va letto come intenzione, non come descrizione. L'addendum lo dice meglio del PRD, sotto «Debito tecnico già visibile».

### 3.2 FR-16 non è implementabile: manca la licenza, e manca la domanda aperta corrispondente

*«Ogni artefatto contiene nome del produttore, licenza d'uso e collegamento alla versione viva.»* Nessuna fonte dice **quale** licenza, nessuna pagina ne ha una, e **§8 «Domande aperte»** non la elenca. Il tema è delicato per un progetto che vive di consegne offline copiabili e che in **§5** dichiara *«Chi riceve un file lo può copiare»*: la licenza è l'unico strumento di controllo residuo, e **§4.5** lo dice apertamente (*«Il controllo su ciò che circola non è tecnico: è… la licenza scritta»*). È l'unica cosa portante che il PRD dichiara necessaria e lascia indefinita senza accorgersene.

### 3.3 «Assenza di risorse esterne caricate» (FR-17) lascia passare il caso reale

`tipi-di-ai.html` contiene **dieci link `href="http…"`** (Stanford Encyclopedia, Wikipedia, artificialintelligenceact.eu, Gartner/IDC…) e `Il Libro dei Prompting.html` uno. Non sono risorse *caricate* — la pagina funziona offline — quindi FR-17 come è scritto li ignora. Il controllo esistente **G4** invece li boccia (BLOCCANTE): *«Nessun `href`/`src` che inizi con `/` o `http`»*.

Due letture opposte, entrambe difendibili: per un corso in cartella G4 ha ragione (un link esterno rotto in aula è un imbarazzo), per un deep-dive con bibliografia i link alle fonti sono un pregio e coerenti con l'onestà epistemica di §2.3. **Il PRD deve scegliere**, perché **§9** assume che i quattro controlli minimi siano *«estraibili dallo script esistente senza riscriverlo»* — e su questo punto l'estrazione a copia produrrebbe il comportamento sbagliato per la vetrina. (Il resto dell'assunzione regge: `verifica_corso.py` è 351 righe con `SOGLIE` in testa e controlli in funzioni separate. Ma **la data di aggiornamento non è fra i controlli esistenti**: quello va scritto da zero, non estratto.)

### 3.4 §4.2: «nei corsi la regia è una pagina separata, com'è già oggi» sottostima il problema

La frase suggerisce che il caso corso sia già a posto. L'addendum è più preciso: *«In entrambi i corsi la separazione della regia è affidata a un gesto manuale: cancellare una cartella prima di consegnare. Funziona finché ci si ricorda.»* Oggi la separazione **fisica** esiste ed è pulita (C4 la garantisce), ma **non esiste alcun comando** che produca una consegna: FR-7 non è un consolidamento, è codice nuovo. Vale anche per **SM-2** (*«nessuna consegna esce con la regia dentro»*): oggi non è una metrica, è una speranza — che è appunto il motivo per cui il PRD esiste.

### 3.5 §2.2 esclude un utente che le fonti prevedono

*«Lo studente autodidatta che cerca un corso online da seguire da solo: il materiale nasce per l'aula condotta.»* Ma `docente/lezione-01.html`, sulle tre domande di riserva: *«Servono come sostituzioni… e come integrazione nella versione online del corso, dove la verifica può essere più estesa perché manca il debrief in presenza.»*

O il materiale contiene un ramo progettato per uno scenario che il PRD ha chiuso, o il non-obiettivo è più netto della realtà. Va deciso: se la versione online resta fuori perimetro, quella frase nella regia è debito da rimuovere; se rientra, **§2.2** e **§5** vanno corretti.

### 3.6 «I dieci artefatti esistenti» (§6.1) e la scheda fantasma

Alla radice ci sono 9 pagine di contenuto più `index.html`; `index.html` espone 9 schede più **una decima commentata con `href="nome-file.html"`** (righe 269-277), il modello da copiare per aggiungere una voce a mano. Lo stesso pattern è nel corso base (commento nell'indice: *«Per aggiungere una lezione futura, copiare una voce e sostituire numero, titolo, messaggio chiave e href»*).

Quel commento è la **prova materiale** del problema che **FR-1 e FR-2** risolvono, e vale più di qualsiasi argomentazione: il modo attuale di pubblicare un artefatto è duplicare a mano un blocco HTML dentro un file esistente. Vale la pena citarlo in **§4.1** al posto di una riga di descrizione.

### 3.7 FR-5, prima conseguenza verificabile: già oggi il file pubblico contiene la stringa «regia»

*«Nel file pubblico la ricerca dei testi della regia non produce risultati.»* `memoria-e-contesto-ai.html` contiene un segnaposto `<!-- regia: … -->` — nessun testo di nota, ma la parola c'è e resta nel file consegnato. È il meccanismo previsto da `costruisci-aula.py` e va bene così: la conseguenza verificabile va riformulata su *il testo delle note*, altrimenti FR-5 dichiara non conforme il proprio stesso strumento.

---

## 4. Requisiti già soddisfatti dal codice esistente

Il PRD scrive **§4.3** e **§4.4** al futuro. In buona parte sono già lì, e riconoscerlo cambia la stima delle epiche e conferma le assunzioni di **§9**.

### FR-12 «Conseguenze delle scelte» — già implementato per intero
`normativa-ai-scadenze-obblighi.html`, configuratore `id="rischio"`, blocco *«Cosa sposterebbe l'esito»* (righe ~1460-1471). Il commento nel sorgente dice esattamente ciò che chiede il PRD: *«invece di scriverli a mano, i controfattuali in fondo»*. Le tre conseguenze verificabili di FR-12 sono soddisfatte una per una:

- ricerca a modifica singola nello spazio delle configurazioni, non elenco a mano → sì;
- *«Quando nessuna modifica singola cambia l'esito, l'artefatto cerca le combinazioni minime e dice che ne servono più di una»* → `'Cosa sposterebbe l'esito — servono due modifiche insieme'`;
- *«Quando nessuna combinazione cambia l'esito, lo dichiara invece di tacere»* → `'Nessuna combinazione di parametri cambia l'esito: qui si sposta solo ripensando la finalità del sistema.'`

FR-12 non è un requisito da costruire: è un **comportamento esistente da estrarre e riusare**. È anche il vuoto di mercato dichiarato nell'addendum (*«Nessuno mostra quali decisioni progettuali spostano la classificazione»*) — cioè il pezzo più differenziante del prodotto è già in produzione, e il PRD lo tratta come da fare.

### FR-10 «Configurazione trasportabile» — implementato in due artefatti
`history.replaceState` + `location.hash` + il pulsante *«Copia link a questa configurazione»* in `memoria-e-contesto-ai.html` e in `normativa-ai-scadenze-obblighi.html`. L'uso dell'hash risolve già la conseguenza *«anche quando il browser impedisce di aggiornare l'indirizzo, come accade aprendo un file dal disco»*. **UJ-1 è un percorso che oggi funziona**, non un desiderio.

### FR-11 «Casi preimpostati» — implementato, incluso il caso limite
`memoria-e-contesto-ai.html`: *«Preset: progetto pilota · Preset: reparto legale · Preset: contesto saturo»* — l'ultimo è la condizione limite richiesta. `normativa-…`: *«Selezione del personale · Chatbot di assistenza · Controllo qualità in fabbrica · Analisi del tono in call center»*.

### FR-9 «Modello manipolabile» — soddisfatto, compresa la clausola sulle stime
Nessuna risorsa esterna caricata in nessuno dei due file; nessuna persistenza; *«Le stime dichiarano come sono calcolate»* è già praticato con il blocco *«Come sono calcolati i numeri»* (memoria) e *«A cosa serve e a cosa no»* (normativa). Il repertorio che l'addendum indica come *«alla portata»* — numeri trascinabili dentro la frase — **esiste già**, scritto a mano: *«trascina i numeri ↔ oppure clicca e digita»*. Non serve né Tangle né una valutazione: serve estrarre il componente.

### FR-5, FR-6, FR-8 — la resa deep-dive è completa
`tools/costruisci-aula.py` + `tools/regia-server.py` + `tools/regia-pannello.html` + `.gitignore` (`regia/`, `*.docente.html`). Puntualmente:

- **FR-6, conseguenza 2** (*«Un segnaposto senza la sua regia, o una regia senza segnaposto, viene segnalato invece di essere ignorato»*) → già entrambe: `sys.exit(f"regia mancante in {sorgente.name} per: …")` e `attenzione: blocchi di regia senza segnaposto: …`.
- **FR-8, conseguenza 1** (*«Ascolta solo sull'interfaccia locale»*) → docstring di `regia-server.py`: *«Serve il pannello e le pagine del sito su 127.0.0.1, e basta: non ascolta sulla rete, non va pubblicato, non ha autenticazione perché non ne ha bisogno.»*
- **FR-8, conseguenza 3** (*«Ogni pagina del catalogo offre almeno un punto valido a cui agganciare una regia»*) → `regia-server.py` già calcola i punti di aggancio (`SEZIONE`, `TITOLO_CON_ID`, `FINE_PAGINA`).
- **FR-5, conseguenza 3** (*«Eliminare la regia non rompe alcun collegamento»*) → garantito per costruzione: la nota è iniettata inline, non collegata.

Resta da fare la **resa corso** di FR-6/FR-7 (nessun comando produce oggi una consegna) e il **controllo del PRD sul PRD**: `.gitignore` esclude `regia/` e `*.docente.html`, quindi **SM-2 è già strutturalmente vera per i deep-dive**. La superficie di rischio residua è tutta sui corsi.

### FR-17 — tre dei quattro controlli minimi esistono già in `verifica_corso.py`
G4 copre risorse esterne e collegamenti rotti; C4 copre l'assenza di rimandi al materiale riservato; il codice di uscita 0/1/2 e la severità sono già la meccanica richiesta dalla conseguenza *«Esce con codice diverso da zero quando resta un rilievo bloccante»*. **Manca solo la data di aggiornamento**, che va scritta. L'assunzione di §9 regge, con la riserva di §3.3 sui link esterni.

---

## 5. In sintesi: cosa cambierei nel PRD, e nient'altro

Nessuna sezione nuova. Sette interventi puntuali:

1. **FR-7** — nominare le cartelle da rimuovere (`docente/`, `qualita/`) invece della categoria «strumenti di qualità», e dichiarare che i materiali trasversali restano (§1.1).
2. **§4.5 / FR-17** — aggiungere la dichiarazione di finzione dei dati fra le informazioni obbligatorie e fra i controlli minimi (§1.2).
3. **§3 glossario + FR-7** — introdurre il *prerequisito d'aula* come categoria che sopravvive alla consegna (§1.3).
4. **FR-1** — aggiungere fra i campi facoltativi il livello EQF e il rimando al BoK (§1.5); e un campo per il mondo condiviso, se si vuole che NEMBO sopravviva al Modulo 2 (§1.10).
5. **FR-18** — chiedere la dichiarazione esplicita su P1/P2/P3, che il PRD nomina in §4.6 e poi perde (§1.6).
6. **FR-9** — una conseguenza sull'uscita del dato per i tool che producono un deliverable (§1.8).
7. **§8** — aggiungere la domanda aperta sulla licenza (§3.2) e quella sui link esterni nei deep-dive (§3.3).

E due riscritture di descrizione, a costo zero: **§4.3** va scritta sapendo che FR-9, FR-10, FR-11 e FR-12 sono già in produzione (§4), e **§1** va letta come intenzione, non come stato di fatto (§3.1).
