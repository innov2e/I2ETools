# Revisione di qualità del PRD — I2ETools

*Data: 2026-09-03 · Rubrica applicata: `.claude/skills/bmad-prd/assets/prd-validation-checklist.md` · Fonti lette: `prd.md` (target), `addendum.md` (di supporto).*

**Taratura della revisione.** Progetto personale, un solo autore, nessuna scadenza. La brevità è una scelta registrata e **non** viene contestata: nessun rilievo qui riguarda firme di approvazione, ROI, piani di rilascio o sezioni «persona». Il metro applicato è uno solo: *fra tre settimane, la stessa persona riesce a costruire da questo documento senza tirare a indovinare su un dettaglio portante?*

---

## Verdetto complessivo

Il PRD ha una tesi vera, difesa e coerente (aula prima del web, autoconsistenza, regia mai dentro la consegna), e la maggior parte dei requisiti è scritta come capacità con conseguenze effettivamente verificabili — cosa rara. Quello che cede è la **cinghia di trasmissione fra §4 (funzionalità), §6 (perimetro) e §7 (metriche)**: sette FR non hanno proprietario nel perimetro, due FR contraddicono il perimetro nel loro stesso testo, un artefatto portante (il *catalogo*) è generato secondo §4.1 ma nessun FR lo genera, e la sezione 4.2 impone un'esclusione (repository pubblico) che §6.2 rinvia. In più il glossario è violato da tre termini definiti — **Aula**, **Percorso**, **Tool** — usati altrove con un secondo significato, e in un caso il secondo significato dà il titolo a un'intera sezione di funzionalità.

Nessuno di questi difetti riguarda la lunghezza del documento. Sono tutti risolvibili con poche righe, ma finché restano il costruttore fra tre settimane deve indovinare *cosa entra nella prima versione* e *cosa significa «aula»* in ogni singolo punto.

---

## Giudizio per dimensione

| Dimensione (rubrica) | Giudizio | In una riga |
|---|---|---|
| 1. Prontezza alla decisione | **forte** | §0 dichiara le tre decisioni aperte e §4 le chiude; §6.2 nomina cosa si è rinunciato ad avere e a quale condizione si riapre; §8 contiene domande davvero aperte, ciascuna con il proprio innesco. |
| 2. Sostanza contro apparenza | **forte** | Nessun teatro. §2.2 «Chi non è l'utente» esclude davvero; §4.6 motiva la doppia soglia invece di invocare «qualità»; §1 non è intercambiabile con un altro PRD. |
| 3. Coerenza strategica | **adeguato** | Tesi chiara, ma §7 lega le metriche a FR che §6.1 non ha ammesso, e SM-C1 non bilancia realmente la metrica che dichiara di bilanciare. |
| 4. Chiarezza del «fatto» | **debole** | La maggioranza degli FR è verificabile, ma FR-13, FR-11, FR-12 e FR-4 poggiano su aggettivi senza limiti («leggibile in sala illuminata», «leggibile da proiettore», «controintuitivo», «combinazioni minime»). È la dimensione su cui si appoggerà la creazione delle storie. |
| 5. Onestà del perimetro | **debole** | §5 e §6.2 sono onesti e ben scritti, ma §6.1 lascia sette FR senza proprietario e non dice se sono dentro, fuori o impliciti. |
| 6. Usabilità a valle | **debole** | Tre violazioni di glossario, quattro sostantivi portanti non definiti (*catalogo*, *tema*, *segnaposto*, *versione viva*), indice delle assunzioni che non torna (§9 elenca assunzioni che nel corpo non compaiono mai). |
| 7. Aderenza alla forma | **forte** | Forma corretta per un progetto solista: quattro percorsi d'uso, glossario, FR come capacità, nessuna sovra-formalizzazione. La forma non è il problema. |

---

## CRITICO

### C-1 — «Aula» è un termine di glossario usato quasi ovunque con un secondo significato

**§3 (Glossario)** definisce: «**Aula** — La parte riservata a chi partecipa a un corso.» Cioè una *zona del sito*.

Nel resto del documento «aula» significa quasi sempre *la sala fisica con le persone dentro*:

- §2.1: «**Condurre un'aula** senza attrito»
- §2.3 UJ-1: «Vittorio prepara **un'aula** per un cliente specifico»
- §4.4: «**Modalità d'aula**» — titolo di un'intera sezione di funzionalità
- §7 SM-3: «il materiale viene usato **in aula**»
- §9: «non blocchi **nessuna aula** già programmata»

L'unico uso conforme al glossario è in FR-1b: «Un solo manifest descrive vetrina e **aula**». Un termine definito la cui definizione vale in un punto solo su sei non è un glossario: è una trappola. Un costruttore che legge «Modalità d'aula» dopo aver letto §3 può ragionevolmente credere che si tratti di funzionalità dell'*area riservata* — che §6.2 rinvia — e quindi non costruirla, mentre §6.1 la mette esplicitamente dentro.

*Correzione.* Rinominare il termine di glossario in **Area riservata** (o **Riservato**, in simmetria con **Vetrina**) e lasciare «aula» al suo significato ordinario di sala fisica, che è quello che il documento usa di fatto. Aggiornare FR-1b: «Un solo manifest descrive vetrina e area riservata». In alternativa, tenere «Aula» come definito e rinominare §4.4 in «Modalità sala» — ma è la strada peggiore, perché costringe a riscrivere sei occorrenze naturali invece di una tecnica.

### C-2 — Il *catalogo* è generato secondo §4.1 ma nessun FR lo genera

**§4.1 (Descrizione)** afferma: «Da lì si generano il menù, la sidebar, la mappa **e il catalogo**.»

**FR-2** però recita: «Un comando rigenera **menù, sidebar e mappa** a partire dal manifest, scrivendoli dentro le pagine.» Il catalogo non c'è. E non c'è in nessun altro FR: FR-4 è la *mappa*, e la definisce esplicitamente come cosa distinta — «Una rappresentazione visiva **del catalogo**».

Il catalogo non è un dettaglio: è nominato in §3 (dentro la definizione di **Vetrina** e dentro quella di **Tool**), in FR-1b («compare **nel catalogo** e nella mappa»), in FR-2b («entra **nel catalogo** come copia autonoma»), in FR-8 («Ogni pagina **del catalogo**») e in UJ-3 («aggiunge una riga **al catalogo**» — dove per giunta «catalogo» sembra significare *il manifest*, aggiungendo un terzo significato). §6.1 non lo elenca fra le cose dentro.

Il costruttore deve indovinare: è una pagina HTML generata? È un elenco per tema? È il manifest stesso? Coincide con la mappa?

*Correzione.* Due interventi. (a) Aggiungere **catalogo** al glossario §3 con una definizione che lo distingua da *manifest* e da *mappa* — p.es. «**Catalogo** — La pagina generata che elenca tutti gli artefatti con i loro metadati, uno per riga. È la resa testuale del manifest; la mappa ne è la resa visiva.» (b) Aggiungere «catalogo» all'elenco di FR-2 e alle sue conseguenze verificabili, e aggiungerlo a §6.1. (c) Correggere UJ-3, dove «aggiunge una riga al catalogo» va detto «aggiunge una riga **al manifest**», altrimenti il termine ha due referenti nel giro di due sezioni.

### C-3 — Sette FR non hanno proprietario nel perimetro, e uno di essi è validato da una metrica primaria

**§6.1 «Dentro»** nomina: FR-1, FR-2, FR-3, FR-4, FR-5, FR-6, FR-7, FR-8, FR-13, FR-14, FR-15, FR-16, FR-17.

**Non compaiono né in §6.1 né in §6.2**: FR-1b, FR-2b, FR-9, FR-10, FR-11, FR-12, FR-18. Sette requisiti su venti sono in un limbo: né dentro, né rinviati, né dichiarati impliciti.

Il caso peggiore è FR-10 (*Configurazione trasportabile*), perché **§7 SM-3** — una metrica **primaria** — dichiara: «il materiale viene usato in aula senza cercare soluzioni di ripiego… **Valida FR-13, FR-14, FR-10**.» Il PRD misura come successo primario un requisito che non ha ammesso nella prima versione. E FR-10 è anche il perno di UJ-1 («copia il link della configurazione… il giorno dopo apre quel link in aula»), il percorso d'uso più dettagliato del documento.

Il secondo caso grave è FR-18 (*Controlli estesi sui corsi*): §6.1 mette dentro «Controlli minimi su ogni artefatto (FR-17)» e «Riconduzione dei dieci artefatti esistenti al manifest e ai controlli», ma non dice se la checklist a trenta controlli resta in vigore nella prima versione. §4.6 dice di sì («resta in vigore la checklist esistente»); §6.1 tace.

*Correzione.* Rendere §6.1 esaustivo rispetto a §4: ogni FR compare esattamente una volta in §6.1 o in §6.2. Concretamente: portare dentro FR-1b e FR-18 (sono già veri oggi, non costano nulla), decidere su FR-9/FR-10/FR-11 (se FR-10 resta fuori, SM-3 va riscritta togliendo il riferimento e UJ-1 va marcato come percorso non ancora coperto), e mettere FR-2b e FR-12 in §6.2 con la loro condizione di riapertura, sullo stesso modello già usato bene per l'area riservata.

### C-4 — FR-13 e FR-14 dicono «ogni artefatto», §6.1 dice «sugli artefatti manipolabili», e «artefatto manipolabile» non è definito

**FR-13**: «**Ogni artefatto** offre una resa leggibile in sala illuminata». **FR-14**: «**Ogni artefatto** produce una versione da stampare priva di comandi, barre e regia.»

**§6.1**: «Modalità d'aula **sugli artefatti manipolabili** (FR-13, FR-14).»

Sono due perimetri diversi per gli stessi due requisiti, ed è una differenza di volume di lavoro grande: «ogni artefatto» include i dieci esistenti che §6.1 vuole ricondurre allo standard.

Peggio: **«artefatto manipolabile» non è nel glossario**. §3 dice che un **Artefatto** «ha esattamente uno di tre **tipi**» — deep-dive, tool, corso. «Manipolabile» è una quarta categoria, ortogonale ai tipi, introdotta di soppiatto in §4.3 e poi usata come criterio di perimetro in FR-9, FR-10, FR-11 e §6.1. Non esiste alcuna regola che dica quali artefatti sono manipolabili: è un campo del manifest? Una proprietà osservata? FR-1 elenca i campi del manifest e *non* include «manipolabile». Quindi il perimetro di §6.1 non è nemmeno calcolabile a partire dal manifest.

*Correzione.* Aggiungere al glossario: «**Manipolabile** — Qualifica ortogonale al tipo: un artefatto è manipolabile quando espone parametri che il lettore modifica e da cui l'esito ricalcola (FR-9). Un deep-dive, un tool o una lezione di corso possono esserlo.» Aggiungere il campo corrispondente ai campi facoltativi di FR-1. Poi allineare FR-13/FR-14 e §6.1 su **una** formulazione: se il perimetro è quello ristretto, FR-13 e FR-14 devono dire «Ogni artefatto manipolabile», non «Ogni artefatto».

### C-5 — FR-5 impone un'esclusione dal repository pubblico che §6.2 rinvia, e non dice con quale meccanismo

**FR-5**: «La regia vive in un file distinto da quello consegnato, **escluso dal repository pubblico**.» FR-5 è dentro il perimetro (§6.1).

**§6.2**: «**Area riservata online** (Cloudflare Access, **secondo repository**): si attiva quando esiste qualcosa che *deve* restare aggiornato online.» Il secondo repository è rinviato.

**`addendum.md`** rende la tensione esplicita: «Prerequisito comune a ogni scenario: separare il materiale riservato in un secondo repository. **Finché sta in quello pubblico, nessuna scelta di hosting produce effetto.**» E osserva sulla situazione attuale: «la separazione della regia è affidata a un gesto manuale: cancellare una cartella prima di consegnare. Funziona finché ci si ricorda.»

Quindi FR-5 nella prima versione va soddisfatto **senza** il secondo repository. Con cosa? `.gitignore`? Cartella fuori dall'albero versionato? Ramo separato? Il documento non lo dice, e la scelta ha conseguenze dirette su FR-6 (il generatore deve trovare la regia), su FR-8 (il pannello deve scriverla) e su FR-17 (il controllo «assenza di regia nel materiale pubblico» deve sapere dove *non* deve stare). È esattamente il dettaglio portante su cui il costruttore fra tre settimane si ferma.

*Correzione.* Riscrivere FR-5 in modo che la capacità sia dichiarata senza pretendere il meccanismo rinviato, e aggiungere la conseguenza mancante. P.es.: «La regia vive in un file distinto da quello consegnato e in una posizione che non entra mai nel materiale pubblicato.» Conseguenze da aggiungere: «Esiste una sola regola dichiarata che stabilisce quali percorsi non vengono pubblicati, e FR-17 la verifica»; «Un file di regia collocato per errore in una posizione pubblicabile viene segnalato prima della pubblicazione, non dopo». Poi annotare in §6.2, sotto l'area riservata, che nella prima versione l'esclusione è locale e non protegge da chi clona il repository — cosa che l'addendum sa e il PRD tace.

---

## ALTO

### A-1 — «Percorso» è definito nel glossario e usato con altri due significati, uno dei quali è un titolo di sezione

**§3**: «**Percorso** — Variante verticale di un artefatto su un tronco comune (finance, sales, legal, project).»

Ma **§2.3** si intitola «**Percorsi d'uso**» — cioè i *user journey*, che con le varianti verticali non c'entrano nulla — e **§8.1** parla di «rappresentazione dei **percorsi di apprendimento**», che è un terzo significato ancora. FR-1 usa correttamente il primo («percorsi disponibili»), FR-1 conseguenze anche («Aggiungere un percorso verticale…»).

*Correzione.* Il termine di glossario è quello giusto e coincide con l'anatomia reale dei corsi (l'addendum conferma: «Tronco comune più quattro percorsi verticali»). Rinominare gli usi confliggenti: §2.3 → «**Scenari d'uso**» (e coerentemente le UJ restano «UJ-n»); §8.1 → «rappresentazione delle **sequenze** di apprendimento».

### A-2 — «Tool» è definito, ma «strumento» è usato sia come suo sinonimo sia per cose completamente diverse

**§3**: «**Tool** — Artefatto interattivo di esercitazione, senza memoria fra una sessione e l'altra.»

Uso come sinonimo del termine definito: **UJ-2** «riusa **uno strumento** sul proprio caso» — qui «strumento» significa esattamente *Tool*.

Uso per tutt'altro, nello stesso documento: **FR-7** «rimuovendo regia e **strumenti di qualità**»; **§3 Consegna** «privato della regia e degli **strumenti di controllo qualità**»; **FR-8** «Uno **strumento** locale permette di scrivere la regia»; **§7 SM-C3** «quantità di **strumenti di supporto**».

SM-C3 è il punto in cui la deriva fa danno vero: «**SM-C3**: quantità di strumenti di supporto. Bilancia SM-1». Se «strumenti» include i **Tool**, allora SM-C3 dice di non produrre troppi artefatti di esercitazione — che è l'opposto di ciò che il PRD vuole, ed è già coperto (male) da SM-C1. Se invece intende gli script del generatore, va detto.

*Correzione.* Riservare «tool» al termine definito e usare **«utensile»** o **«script»** per l'infrastruttura. Riscrivere SM-C3: «quantità di **script di infrastruttura** (generatore, verificatore, pannello)». Riscrivere FR-7 e la definizione di **Consegna** con «**verificatore di qualità**» al posto di «strumenti di qualità». In UJ-2, scrivere «riusa **un tool** sul proprio caso».

### A-3 — FR-13 non ha conseguenze che verifichino ciò che chiede

**FR-13**: «Ogni artefatto offre una resa **leggibile in sala illuminata**: contrasto invertito e testo più grande.»
**Conseguenza verificabile (unica)**: «Attivabile in un gesto, senza ricaricare e senza perdere lo stato.»

La conseguenza verifica l'*attivazione*, non la *leggibilità*, che è la promessa del requisito. «Leggibile in sala illuminata», «contrasto invertito», «testo più grande» sono tre aggettivi senza un solo limite: più grande di quanto? Contrasto di quale rapporto? Due costruttori possono soddisfare FR-13 in modi contraddittori — uno con `filter: invert()` e `font-size: 110%`, l'altro con un tema dedicato a 24px — ed entrambi passano.

Lo stesso vale, in forma più lieve, per **FR-4**: «La mappa resta **leggibile da proiettore**» — nessun limite di dimensione minima, distanza o risoluzione.

*Correzione.* Sostituire gli aggettivi con limiti che il progetto può davvero verificare, restando corti. FR-13: «Nella vista da proiezione il corpo del testo non è inferiore a 24px e il rapporto di contrasto fra testo e fondo non è inferiore a 7:1»; aggiungere «Nessun elemento interattivo diventa irraggiungibile o esce dallo schermo quando la vista è attiva». FR-4: «Ogni etichetta della mappa resta leggibile a 1280×720 senza ingrandire».

### A-4 — «Restare aggiornato senza rifare» è un lavoro dichiarato che nessun FR realizza

**§2.1** elenca fra i lavori da svolgere: «**Restare aggiornato senza rifare**: quando la normativa cambia, cambiare in un posto solo.»

Nessun FR lo copre. FR-15 mostra *quando* il contenuto è stato aggiornato; non offre alcun modo di cambiarlo in un posto solo. §6.2 rinvia il «Versionamento dei contenuti», che è un problema diverso (più copie della stessa cosa in circolazione), non questo (una definizione normativa ripetuta in cinque artefatti). §8.3 sfiora la meccanica giusta — «Se il generatore inietta la navigazione, può iniettare anche il blocco comune» (formulazione dall'addendum) — ma la limita agli stili.

Questo è il lavoro con il più alto costo ricorrente per un manutentore solo, ed è l'unico dei sei di §2.1 senza proprietario. Gli altri cinque sono coperti (FR-13/14 e FR-10; FR-7; FR-1/FR-2; FR-5/FR-7; FR-16).

*Correzione.* O aggiungere un FR — p.es. «FR-19: Blocchi condivisi. Un frammento di contenuto dichiarato una volta viene iniettato dal generatore in tutti gli artefatti che lo richiamano; modificarlo in un posto solo aggiorna tutti gli artefatti alla generazione successiva» — oppure spostare esplicitamente il lavoro in §6.2 con la sua condizione di riapertura («si riapre quando la stessa definizione normativa compare in più di tre artefatti»). Lasciarlo in §2.1 senza proprietario è la sola opzione da escludere.

### A-5 — FR-12 impone un metodo di ricerca ma non ne dichiara i limiti: costo di realizzazione ignoto

**FR-12**: «Dove l'artefatto produce una classificazione, mostra quali modifiche la cambierebbero — **cercate nello spazio delle configurazioni**, non elencate a mano.»
**Conseguenze**: «Quando nessuna modifica singola cambia l'esito, l'artefatto **cerca le combinazioni minime** e dice che ne servono più di una»; «Quando **nessuna combinazione** cambia l'esito, lo dichiara invece di tacere».

Due problemi in una volta. Primo, «cercate nello spazio delle configurazioni» è una scelta implementativa infilata dentro un requisito di capacità: il *cosa* è «mostra quali modifiche cambierebbero l'esito», il *come* non appartiene al PRD. Secondo — ed è ciò che rende il requisito impossibile da preventivare — «nessuna combinazione» è quantificato su nulla: con dieci parametri a valori continui lo spazio non è enumerabile, e la conseguenza chiede di dichiarare un esito negativo su un insieme infinito. Non esiste implementazione che lo soddisfi letteralmente.

Va notato anche che FR-12 non ha proprietario nel perimetro (vedi C-3): è il requisito più costoso del documento e nessuno ha detto se si fa.

*Correzione.* Togliere il *come* e mettere un limite esplicito: «Dove l'artefatto produce una classificazione, mostra quali modifiche dei parametri la cambierebbero, derivandole dal modello e non da un elenco scritto a mano.» Conseguenze: «Vengono esaminate tutte le modifiche di un singolo parametro e tutte le coppie; oltre le coppie l'artefatto dichiara di non aver cercato, invece di dichiarare che non esiste soluzione»; «Ogni modifica proposta è applicabile con un gesto» (già presente, va bene). Poi collocare FR-12 in §6.1 o §6.2.

---

## MEDIO

### M-1 — FR-9 e FR-10 si contraddicono alla lettera sul ripristino dello stato

**FR-9**, conseguenza: «Nessuno stato conservato fra sessioni; **riaprendo si riparte dai valori iniziali**.»
**FR-10**, conseguenza: «**Aprendo il link, i valori ripristinati sono quelli catturati.**»

L'intenzione si capisce (nessuna memoria implicita; ripristino solo da link esplicito), ma il testo di FR-9 è assoluto e nega FR-10. Un verificatore che applichi le conseguenze alla lettera trova un conflitto.

*Correzione.* FR-9: «Nessuno stato conservato fra sessioni: **in assenza di configurazione nel link**, riaprendo si riparte dai valori iniziali.»

### M-2 — «Versione viva» è portante e non definita, e in assenza di area riservata non si sa cosa sia per un corso

**FR-16**: «Ogni artefatto contiene nome del produttore, licenza d'uso e **collegamento alla versione viva**.» **UJ-2**: «se la data è vecchia di un anno, il link lo riporta alla **versione viva**.»

Il termine non è in §3. Per un deep-dive pubblico si intuisce (l'URL sulla vetrina). Per un **corso riservato**, §6.2 rinvia l'area riservata online: non c'è alcuna versione viva raggiungibile, quindi FR-16 chiede un collegamento che nella prima versione non può esistere. E FR-17 verifica «assenza di collegamenti rotti»: un collegamento verso una pagina non ancora pubblicata è rotto o è un'eccezione? Il costruttore deve decidere da solo.

*Correzione.* Definire in §3: «**Versione viva** — L'indirizzo pubblico stabile a cui un artefatto è mantenuto aggiornato.» Aggiungere a FR-16 la conseguenza mancante: «Un artefatto senza versione viva pubblica rimanda alla propria voce di catalogo, non a un indirizzo inesistente.» E precisare in FR-17 se il controllo dei collegamenti rotti include quelli esterni (che, per la promessa «funziona senza rete», non è ovvio).

### M-3 — «Segnaposto» compare solo nella conseguenza di FR-6 e non è definito

**FR-6**, conseguenza: «Un **segnaposto** senza la sua regia, o una regia senza segnaposto, viene segnalato invece di essere ignorato.»

È l'unica occorrenza in tutto il PRD. Il concetto esiste davvero — l'addendum lo documenta: «`tools/costruisci-aula.py` — inietta la regia dai segnaposto `<!-- regia: id -->`» — ma il PRD non lo dice, e FR-8 («collocarla nel punto voluto») gira attorno alla cosa senza nominarla. Chi legge il solo PRD non sa che gli artefatti contengono marcatori né chi li scrive.

*Correzione.* Aggiungere al glossario: «**Segnaposto** — Il marcatore, presente nel file sorgente, che indica il punto in cui la regia viene iniettata alla generazione. Ha un identificatore che lo lega alla propria regia.» E riformulare la conseguenza di FR-8 «Ogni pagina del catalogo offre almeno un punto valido a cui agganciare una regia» in termini di segnaposto — oggi quella conseguenza, per giunta, verifica una proprietà **delle pagine**, non del pannello che FR-8 descrive: è collocata sotto il requisito sbagliato.

### M-4 — §4.6 e FR-18 dicono due cose diverse sulla regola di consegna, e le severità non sono mai definite

**§4.6**: «con la regola di **non consegnare finché restano rilievi bloccanti**».
**FR-18**, conseguenza: «La generazione di una consegna con rilievi bloccanti aperti **richiede una forzatura esplicita**.»

La prima è un divieto, la seconda un attrito superabile. Inoltre l'addendum riporta la regola reale con un livello in più — «non consegnare finché restano rilievi **bloccanti o gravi**» — e il PRD ha perso «gravi» senza dirlo. In tutto il documento non esiste una definizione di *bloccante*, *grave* o *rilievo*, benché FR-15 («segnalato come rilievo»), FR-17 («resta un rilievo bloccante») e FR-18 vi si appoggino per decidere il codice di uscita.

*Correzione.* Aggiungere al glossario: «**Rilievo** — Esito negativo di un controllo. È *bloccante* quando impedisce la generazione di una consegna, *segnalazione* quando la consente.» Allineare §4.6 alla formulazione di FR-18 (la forzatura esplicita è la scelta giusta per un manutentore solo — vale la pena dirlo come decisione, non lasciarlo come discrepanza).

### M-5 — «Vetrina» esclude i corsi, ma FR-1 prevede corsi aperti

**§3**: «**Vetrina** — La parte pubblica e aperta: **deep-dive, tool, catalogo, mappa**.» I corsi non ci sono.
**FR-1**: ogni artefatto ha uno «stato di accesso (**aperto** o riservato)», senza limitazioni di tipo.

Se un corso può essere aperto, dov'è? La partizione vetrina/aula non è più esaustiva. Se invece i corsi sono *sempre* riservati per costruzione, allora il campo «stato di accesso» di FR-1 è ridondante per i corsi e va detto.

*Correzione.* Scegliere e scrivere una delle due. Preferibile: «**Vetrina** — La parte pubblica e aperta: tutti gli artefatti con stato di accesso *aperto*, più catalogo e mappa» — che rende la partizione esaustiva e derivabile dal manifest, coerente con FR-1b.

### M-6 — FR-3 esclude i tool dall'indice di pagina, senza dirlo

**FR-3**: «Ogni **deep-dive** e ogni **pagina di corso** espone l'indice delle proprie sezioni in una barra laterale richiudibile.»

Il glossario ha tre tipi; FR-3 ne cita due. Un tool estratto (FR-2b) è una pagina autonoma come un deep-dive: perché non ha indice? Se è una scelta (i tool sono corti, l'indice sarebbe rumore) è una buona scelta, ma taciuta diventa un dubbio del costruttore.

*Correzione.* Rendere esplicita l'esclusione nel testo o in una conseguenza: «I tool sono esclusi: un tool che richiedesse un indice è troppo lungo per essere un tool.» Una riga chiude la questione e per giunta dice qualcosa di utile sul prodotto.

### M-7 — FR-13/14/15/16 dicono «ogni artefatto» ma un corso è una cartella di pagine

**FR-14**: «**Ogni artefatto** produce una versione da stampare». **FR-15**: «**Ogni artefatto** mostra la data». **FR-16**: «**Ogni artefatto** contiene nome del produttore, licenza…».

§3 definisce **Corso** come «una **cartella** con più pagine». Quindi: la dispensa stampabile di un corso è un unico file con tutte le lezioni o una stampa per pagina? La data e la firma stanno su ogni pagina o solo sull'`index.html`? La risposta cambia il lavoro e cambia cosa verifica FR-17 («presenza della data di aggiornamento» — su quale file?).

*Correzione.* Una riga in §4.5 che fissi la regola per l'unità composita: «Per un corso, data, firma e licenza compaiono su ogni pagina; la dispensa stampabile è un unico documento con tutte le lezioni nell'ordine del corso.»

### M-8 — L'indice delle assunzioni non torna: §9 elenca cinque assunzioni che nel corpo non compaiono mai

**§9** elenca cinque voci marcate `[ASSUNZIONE]`, ciascuna con il riferimento alla sezione: «§2.3 —», «§4.1 —», «§4.3 —», «§4.6 —», «§6.2 —».

Nel corpo del documento **nessun** marcatore `[ASSUNZIONE]` compare: né in §2.3, né in §4.1, né in §4.3, né in §4.6, né in §6.2. Il roundtrip previsto dalla rubrica è a senso unico. Chi legge §4.3 non sa che sta leggendo qualcosa che poggia su un'assunzione non verificata («i modelli manipolabili restano calcolabili nel browser senza librerie esterne») — e quella, tra l'altro, è l'assunzione che l'addendum sostiene con dati misurati (i pesi di D3, Chart.js, p5.js) e che quindi merita di essere visibile dove serve.

*Correzione.* Inserire il marcatore in linea nel punto in cui l'assunzione agisce, lasciando §9 come indice. P.es. in fondo alla descrizione di §4.3: «`[ASSUNZIONE]` I modelli restano calcolabili nel browser senza librerie esterne (pesi misurati in `addendum.md`).» Cinque righe in tutto.

### M-9 — SM-1 riformula il requisito invece di metterlo alla prova

**§7 SM-1**: «pubblicare un artefatto nuovo non richiede di modificare a mano nessun file esistente oltre al manifest. Valida FR-1, FR-2.»
**§4.1**: «Aggiungere un artefatto significa scrivere il contenuto e aggiungere una riga: **nessun altro file esistente viene toccato a mano**.»

La metrica è la descrizione del requisito con le stesse parole. Non aggiunge un criterio: se FR-1 e FR-2 sono realizzati, SM-1 è vera per costruzione. Una metrica che non può fallire indipendentemente dal requisito non lo valida.

*Correzione.* Renderla osservabile nel tempo e non per costruzione: «Sui prossimi cinque artefatti pubblicati, il numero di file esistenti modificati a mano oltre al manifest resta zero» — così misura la *tenuta* del generatore sui casi reali (compreso il caso in cui un artefatto ha bisogno di qualcosa che il manifest non prevede), che è la cosa che può davvero rompersi.

### M-10 — SM-C1 non bilancia la metrica che dichiara di bilanciare

**§7**: «**SM-C1**: numero di artefatti. **Bilancia SM-1**: dieci pagine deboli valgono meno di tre manipolabili.»

SM-1 misura l'assenza di modifiche manuali. Ottimizzare SM-1 non spinge in alcun modo a produrre più artefatti: le due grandezze non sono in tensione. La contro-metrica giusta esiste ma non ha un obiettivo da contrastare, perché nessuna SM primaria misura il volume di produzione. Per contrasto, SM-C2 e SM-C3 funzionano bene: irrigidire i controlli (SM-2) scoraggia davvero le pagine sperimentali, e automatizzare tutto (SM-1) fa davvero crescere l'infrastruttura a carico di una persona sola.

*Correzione.* Riagganciare SM-C1 a ciò che davvero contrasta — la spinta a produrre — dichiarandola come contro-metrica di sistema: «**SM-C1**: numero di artefatti. **Non è un obiettivo**: la comodità di pubblicare (SM-1) rende conveniente aggiungere pagine deboli. Dieci pagine deboli valgono meno di tre manipolabili.» In più: SM-C2 dice «oltre **una certa soglia** la conformità scoraggia le pagine strane» senza dire quale — se la soglia non è nominata, la contro-metrica non può scattare. Bastano le parole «oltre i quattro controlli minimi di FR-17 applicati alle pagine singole», che è la soglia che §4.6 di fatto già difende.

---

## BASSO

### B-1 — SM-4 e SM-5 non validano alcun FR

**§7 Secondario**: «**SM-4**: un artefatto vecchio si riapre e si aggiorna senza doverne ricostruire l'impianto» e «**SM-5**: qualcuno chiede di riusare il materiale». A differenza di SM-1, SM-2 e SM-3, nessuna delle due porta la formula «Valida FR-n».

SM-4 in particolare misura proprio il lavoro orfano di A-4. SM-5 misura un comportamento di terzi (nessuno lo controlla) e come indicatore che «il materiale circola e porta il nome giusto» dipende da FR-16, che potrebbe dirlo.

*Correzione.* Aggiungere «Valida FR-16» a SM-5. Per SM-4, agganciarla al nuovo requisito proposto in A-4, oppure marcarla come metrica di salute senza requisito («non valida alcun FR: è un segnale sul debito di §8.3»).

### B-2 — «Fuori perimetro» dentro FR-2 duplica §5 e §6.2

**FR-2**: «**Fuori perimetro:** la ricerca full-text; l'internazionalizzazione.» Ma §6.2 ha già «**Ricerca full-text**: con qualche decina di artefatti la mappa basta» e «**Traduzione in inglese**: la posizione difendibile è l'italiano». Due luoghi per la stessa esclusione: se domani si cambia idea, si aggiorna uno solo.

*Correzione.* Togliere la riga da FR-2. §6.2 è il posto giusto e già lo dice meglio, con la motivazione.

### B-3 — UJ-4 promette un'apertura che la prima versione non può mantenere

**UJ-4**: «Le aree dei corsi le vede, ma sono segnate come chiuse: sa che esistono e sa che **si aprono partecipando**.» Con l'area riservata online rinviata (§6.2), non si aprono affatto: chi partecipa riceve una cartella. Il percorso resta valido nella prima metà, ma la promessa finale non è realizzabile e nessuna conseguenza verificabile la copre.

*Correzione.* Chiudere UJ-4 su ciò che la prima versione fa davvero: «…sa che esistono e sa che il materiale gli arriva partecipando». Una parola, e il percorso torna a descrivere il prodotto che si sta costruendo.

### B-4 — La conseguenza di idempotenza di FR-2 e la data di FR-15 possono confliggere

**FR-2**: «Rigenerare due volte di seguito senza modifiche non produce differenze nei file» — ottima conseguenza, la migliore del documento. Ma se la data di FR-15 fosse iniettata dal generatore come data del giorno, l'idempotenza salta. Il PRD non dice se la data viene dal manifest (dove FR-1 la elenca fra i campi obbligatori: «data di aggiornamento») o dal generatore.

*Correzione.* Una conseguenza in FR-15: «La data proviene dal manifest, non dal momento della generazione.» Rende compatibili FR-2 e FR-15 e chiude il dubbio.

### B-5 — Il protagonista di UJ-4 non è nominato

UJ-1 e UJ-3 hanno «Vittorio»; UJ-2 ha «Un partecipante» (accettabile: è la categoria); UJ-4 ha «Un dirigente che ha seguito il corso». Su un progetto solista non è un difetto grave, ma UJ-4 è l'unico percorso il cui protagonista *non è* l'utente di riferimento di §2, e questo non è detto da nessuna parte — §2.2 esclude lo studente autodidatta e il formatore terzo, ma non chiarisce lo statuto dell'ex partecipante.

*Correzione.* Una riga in §2.2 o in testa a UJ-4: «Non è l'utente di riferimento, ma è il destinatario del materiale che circola: i suoi bisogni sono coperti da FR-4 e FR-16, non progettati a parte.»

---

## Note meccaniche

- **Numerazione degli FR.** FR-1, FR-1b, FR-2, FR-2b, FR-3…FR-18. Le lettere sono leggibili e non creano ambiguità, ma **§6.1 cita «Manifest unico, con i campi di FR-1»**: l'unicità del manifest è FR-1b, non FR-1. Il riferimento va corretto in «FR-1, FR-1b».
- **Riferimenti incrociati.** Tutti gli «Realizza UJ-n» risolvono. Verificati: UJ-1 (§4.1 no, §4.2 sì, §4.3 sì, §4.4 sì, FR-10 sì), UJ-2 (§4.2, §4.3, §4.5), UJ-3 (§4.1), UJ-4 (FR-4). Nessun UJ resta senza copertura, nessun riferimento è rotto. Buono.
- **Conteggio dei controlli.** §4.6 promette «i quattro controlli che verificano le promesse fatte» e FR-17 ne elenca esattamente quattro (risorse esterne, collegamenti rotti, regia, data). Coerente. §4.6 «trenta controlli automatici e tre a giudizio» coincide con l'addendum. Coerente.
- **Coerenza con l'addendum.** Nessuna contraddizione di merito trovata fra `prd.md` e `addendum.md`. La divisione del lavoro dichiarata in testa all'addendum («Il PRD dice *cosa*; qui c'è il *come*») è rispettata, con la sola eccezione di FR-12 (rilievo A-5), dove un *come* è finito nel PRD, e di FR-8 «Ascolta solo sull'interfaccia locale», che è la resa corretta in linguaggio di capacità di ciò che l'addendum chiama `127.0.0.1` — quella va bene così.
- **Termini portanti assenti dal glossario**, raccolti: **catalogo** (C-2), **manipolabile** (C-4), **segnaposto** (M-3), **versione viva** (M-2), **rilievo / bloccante** (M-4), **tema** — quest'ultimo usato in FR-1 («tema di appartenenza»), FR-4 («mostra i temi») e UJ-3 («l'elenco del suo tema») senza che nulla dica se i temi sono un elenco chiuso dichiarato nel manifest o testo libero. Anche questo è un dettaglio che il costruttore deve indovinare: aggiungere una riga a FR-1 basta.
- **Soglia d'accesso.** FR-1b introduce «l'indirizzo della **soglia d'accesso**», termine che non ricompare altrove e non è definito. Con l'area riservata rinviata (§6.2), a cosa punta oggi la soglia di un corso riservato? Da chiarire insieme a M-2.

---

## Come procederei

Nell'ordine, perché sono legati: **C-1** (rinominare *Aula* → *Area riservata*, ~6 sostituzioni), **C-3** (rendere §6.1 esaustivo — è l'intervento che rende il documento costruibile), **C-4** e **C-2** (definire *manipolabile* e *catalogo*, che C-3 costringe comunque a nominare), **C-5** (dire come vive la regia senza il secondo repository), poi A-1/A-2 di glossario e A-3/A-5 sui limiti mancanti. I rilievi MEDIO e BASSO sono tutti da una a tre righe ciascuno e possono essere assorbiti nello stesso passaggio.

Il documento non ha bisogno di essere più lungo. Con questi interventi cresce di circa una pagina e diventa costruibile senza congetture.
