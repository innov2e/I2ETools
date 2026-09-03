---
title: I2ETools
status: final
created: 2026-09-03
updated: 2026-09-03
---

# PRD: I2ETools
*Titolo di lavoro — è il nome del repository, non ancora un nome di prodotto.*

## 0. Scopo del documento

PRD di un progetto personale, tenuto corto di proposito. Serve a decidere tre cose che oggi sono aperte e che si condizionano a vicenda: come si tengono insieme artefatti nati in momenti diversi, dove passa il confine fra ciò che si consegna e ciò che si trattiene, e con quale meccanica si aggiunge materiale senza rimettere mano a quello esistente.

Non descrive i contenuti didattici, che esistono già e non hanno bisogno di un PRD. Le scelte tecniche di dettaglio — hosting, formato del manifest, struttura degli strumenti — stanno in `addendum.md`. Il registro delle decisioni con i loro motivi è in `.memlog.md`.

Due ricerche condotte il 3 settembre 2026 fanno da base: una sul panorama delle *explorable explanations*, una sulle opzioni reali di protezione di un'area riservata su hosting statico. Le conclusioni che contano sono citate dove servono.

## 1. Visione

INNOV2E produce materiale didattico sull'AI che si **manipola**, non si guarda. Il mercato italiano della formazione sull'AI Act vende webinar, moduli e-learning e video con quiz; il canone internazionale delle *explorable explanations* — Nicky Case, Bartosz Ciechanowski, Distill, Red Blob Games — dimostra da vent'anni che si impara di più muovendo una leva che ascoltando qualcuno spiegare la leva. Nessuno in Italia lo applica alla governance dell'AI, e nessuno al mondo lo applica pensando a chi deve decidere un budget invece che a chi scrive codice.

Il materiale è fatto per l'aula prima che per il web. Ogni artefatto funziona senza rete, si proietta, si stampa e si porta via: chi partecipa esce con un oggetto che gli resta, non con un accesso che scade. Questo vincolo non è nostalgia tecnica, è la condizione perché il materiale sia usabile davvero — in una sala riunioni con il wi-fi degli ospiti, davanti a venti persone che aspettano.

Attorno agli artefatti serve una struttura minima: un catalogo che li tenga insieme, una navigazione che permetta di trovarli e una regola che separi quello che si regala da quello che si vende. Oggi mancano tutte e tre.

## 2. Utente di riferimento

### 2.1 Lavori da svolgere

- **Condurre un'aula senza attrito**: proiettare, scandire i tempi, sapere dove fermarsi, arrivare con la configurazione già pronta sul caso del cliente.
- **Consegnare qualcosa che resti**: materiale che il partecipante riapre sei mesi dopo, sul suo computer, senza credenziali.
- **Aggiungere un contenuto senza rimettere mano al resto**: scrivere l'artefatto e vederlo comparire nel catalogo, nel menù e nella mappa.
- **Non consegnare per sbaglio ciò che non va consegnato**: la regia, le soluzioni, la chiave dei test.
- **Restare aggiornato senza rifare**: quando la normativa cambia, cambiare in un posto solo.
- **Farsi riconoscere**: che il materiale in circolazione porti il nome di chi l'ha fatto.

### 2.2 Chi non è l'utente

- Lo studente autodidatta che cerca un corso online da seguire da solo: il materiale nasce per l'aula condotta.
- Lo sviluppatore che vuole capire i modelli dall'interno: lo servono già Polo Club, Distill e Bycroft, meglio di quanto potremmo noi.
- Il formatore terzo come destinatario primario: è servito dagli stessi pezzi, ma non è per lui che si progetta (vedi §5).

### 2.3 Casi d'uso

- **UJ-1. Vittorio prepara un'aula per un cliente specifico, la sera prima.**
  Apre la pagina dell'AI Act, imposta il configuratore sul caso reale del cliente — selezione del personale, sistema che decide da solo, profilazione attiva — e copia il link della configurazione. Il giorno dopo apre quel link in aula: la pagina parte già sul caso che interessa, senza dover toccare sei controlli davanti a tutti. Attiva la vista da proiezione, perché la sala ha le finestre, e la regia, che gli ricorda di far indovinare la stanza prima di rivelare l'esito. **Caso limite:** se la rete della sala non funziona, apre la stessa pagina dalla copia sul portatile, e la configurazione arriva comunque dal link.

- **UJ-2. Un partecipante riapre il materiale tre mesi dopo, da solo.**
  Ha la consegna sul computer, ricevuta a fine giornata. Doppio clic su `index.html`, nessuna rete, nessun accesso. Rivede la lezione, rifà l'esercizio, riusa uno strumento sul proprio caso. Nella consegna non c'è la regia né la chiave dei test: quelli non li ha mai avuti. In fondo a ogni pagina trova la data di aggiornamento e il nome di chi l'ha prodotta — e se la data è vecchia di un anno, il link lo riporta alla versione viva.

- **UJ-3. Vittorio pubblica un nuovo deep-dive.**
  Scrive la pagina come ha sempre fatto, aggiunge una riga al manifest, lancia il generatore. La pagina compare nel menù in alto, nella mappa e nell'elenco del suo tema; la copia con la regia viene prodotta a parte e non finisce online. Non ha aperto nessuno degli altri file.

- **UJ-4. Un dirigente che ha seguito il corso torna sul sito.**
  Non ricorda come si chiamava «quella cosa sui rischi». Apre la mappa, riconosce la zona della normativa, entra. Le aree riservate le vede, ma segnate come chiuse: sa che esistono e sa che si aprono partecipando.

## 3. Glossario

- **Artefatto** — Un contenuto didattico autonomo. Ha esattamente uno di tre **tipi**.
- **Deep-dive** — Artefatto costituito da una singola pagina HTML autoconsistente, con CSS e JS incorporati. Si consulta da solo, si scarica, funziona senza rete.
- **Tool** — Artefatto interattivo di esercitazione, senza memoria fra una sessione e l'altra. Può produrre un file da scaricare (PDF, CSV, JSON) e accettarne uno in ingresso. Nel catalogo compare sempre come copia autonoma e autoconsistente, anche quando nasce dentro un corso; in quel caso ne dichiara la **provenienza**.
- **Corso** — Artefatto costituito da una **cartella** con più pagine, collegamenti relativi e un foglio di stile condiviso. L'autoconsistenza è a livello di cartella: si sposta, si rinomina, si copia su chiavetta.
- **Consegna** — Il pacchetto che riceve chi partecipa: un corso privato della regia e degli strumenti di controllo qualità. Si genera, non si ottiene cancellando a mano.
- **Regia** — Il materiale che serve a chi conduce e non a chi partecipa: scaletta al minuto, chiave dei test, domande di riserva, inciampi ricorrenti, avvertenze operative. Non è mai dentro un file consegnato.
- **Manifest** — Il file unico che descrive tutti gli artefatti. Unica fonte di verità per navigazione, catalogo e mappa.
- **Catalogo** — L'elenco testuale degli artefatti, generato dal manifest. È l'attuale pagina d'ingresso a schede.
- **Mappa** — La rappresentazione visiva del catalogo: temi, artefatti e loro rapporti. Stessa fonte, resa diversa.
- **Artefatto manipolabile** — Artefatto in cui il lettore modifica dei parametri e l'esito si ricalcola. Non è un tipo a sé: un deep-dive, un tool o una pagina di corso possono esserlo.
- **Istruzioni operative** — Indicazioni sulle condizioni in cui l'esercizio funziona — disattivare la ricerca sul web, caricare in anticipo i documenti. Riguardano chi partecipa, **restano nella consegna**, e non vanno confuse con la regia.
- **Vetrina** — La parte pubblica e aperta: deep-dive, tool, catalogo, mappa.
- **Area riservata** — La parte del sito accessibile solo a chi partecipa a un corso. Da non confondere con l'**aula**, che in questo documento è sempre la sala fisica in cui si conduce.
- **Percorso** — Variante verticale di un artefatto su un tronco comune (finance, sales, legal, project). Facoltativo: la maggior parte degli artefatti non ne ha, e non deve dichiararlo.
- **Provenienza** — Il corso e la lezione da cui un tool è stato estratto, quando esiste.

## 4. Funzionalità

### 4.1 Il manifest come unica fonte di verità

**Descrizione.** Un solo file descrive tutti gli artefatti: cosa sono, dove stanno, a quale tema appartengono, se sono aperti o riservati. Da lì si generano il menù, la sidebar, la mappa e il catalogo. Aggiungere un artefatto significa scrivere il contenuto e aggiungere una riga: nessun altro file esistente viene toccato a mano. Realizza UJ-3.

**Requisiti funzionali**

#### FR-1: Descrizione di un artefatto
Il manifest descrive ogni artefatto con: titolo, tipo, indirizzo, tema di appartenenza, stato di accesso (aperto o riservato), data di aggiornamento. Sono facoltativi, presenti solo dove hanno senso: durata, numero di lezioni, livello, prerequisiti, percorsi disponibili, provenienza, riferimento al Body of Knowledge e livello EQF.

**Conseguenze verificabili:**
- Un artefatto assente dal manifest non compare in nessuna navigazione, in nessuna mappa e in nessun catalogo.
- Un artefatto presente nel manifest ma con un indirizzo locale inesistente produce un errore in fase di generazione, non una pagina rotta.
- Un artefatto senza percorsi verticali non dichiara nulla al riguardo: l'assenza del campo è la condizione normale.
- Aggiungere un percorso verticale a un artefatto che già ne ha è una voce in più, non una modifica della struttura del manifest.

#### FR-1b: Il manifest è unico, pubblico e si ferma al catalogo
Un solo manifest descrive vetrina e area riservata. Degli artefatti riservati contiene i metadati e l'indirizzo della soglia d'accesso, mai l'elenco delle loro parti interne.

**Conseguenze verificabili:**
- Un artefatto riservato compare nel catalogo e nella mappa con titolo e metadati, e il suo indirizzo porta alla soglia, non a un file interno.
- Il manifest non contiene indirizzi di regia, di soluzioni o di singole lezioni di un corso riservato.
- Non esiste un secondo manifest da tenere allineato.

#### FR-2: Generazione della navigazione
Un comando rigenera menù, catalogo, sidebar e mappa a partire dal manifest, scrivendoli dentro le pagine.

**Conseguenze verificabili:**
- La navigazione è presente nel sorgente HTML prima che il browser esegua JavaScript.
- Rigenerare due volte di seguito senza modifiche non produce differenze nei file.
- La generazione non altera il contenuto redazionale di una pagina, solo i blocchi delimitati.

#### FR-2b: Estrazione di un tool da un corso
Un tool nato dentro un corso entra nel catalogo come copia autonoma, con stile e comportamenti incorporati, e dichiara la propria provenienza.

**Conseguenze verificabili:**
- La copia estratta funziona aperta da sola, senza i file della cartella del corso.
- La copia non contiene collegamenti a materiale riservato del corso di origine.
- La provenienza è visibile a chi la usa, con il rimando al corso da cui viene.

#### FR-3: Indice della pagina corrente
Ogni deep-dive e ogni pagina di corso espone l'indice delle proprie sezioni in una barra laterale richiudibile.

**Conseguenze verificabili:**
- L'indice si ricava dai titoli presenti nella pagina: nessun elenco da mantenere a mano.
- Su schermo stretto la barra è chiusa e non copre il contenuto.
- Aprendo il file dal disco l'indice funziona ugualmente.

#### FR-4: Mappa di scoperta
Una rappresentazione visiva del catalogo mostra i temi, gli artefatti che contengono e i loro rapporti — generata dallo stesso manifest della navigazione. Realizza UJ-4.

**Conseguenze verificabili:**
- Ogni artefatto del manifest compare nella mappa: non esiste un secondo elenco da tenere allineato.
- Gli artefatti riservati compaiono visibilmente chiusi, con il titolo leggibile e l'accesso negato.
- La mappa resta leggibile da proiettore.

### 4.2 La regia, mai dentro ciò che si consegna

**Descrizione.** Una regola sola, due rese secondo l'anatomia dell'artefatto: nei corsi la regia è una pagina separata, com'è già oggi; nei deep-dive è una copia generata a parte. In entrambi i casi il materiale consegnato non contiene la regia, nemmeno nascosta. Realizza UJ-1, UJ-2.

**Requisiti funzionali**

#### FR-5: Separazione della regia
La regia vive in un file distinto da quello consegnato, escluso dal repository pubblico.

**Conseguenze verificabili:**
- Nel file pubblico la ricerca dei testi della regia non produce risultati.
- L'assenza della regia non lascia nel file consegnato controlli, pulsanti o riferimenti inerti.
- Eliminare la regia non rompe alcun collegamento.

#### FR-6: Generazione della copia per chi conduce
Un comando produce la versione con la regia: per un deep-dive, un file affiancato; per un corso, il pacchetto completo.

**Conseguenze verificabili:**
- La copia generata resta utilizzabile senza rete.
- Un segnaposto senza la sua regia, o una regia senza segnaposto, viene segnalato invece di essere ignorato.

#### FR-7: Generazione del pacchetto da consegnare
Un comando produce la consegna a partire da un corso, rimuovendo le **cartelle** dichiarate come non consegnabili e verificando che non resti alcun collegamento rotto.

**Conseguenze verificabili:**
- L'esclusione avviene per cartella dichiarata — oggi `docente/` e `qualita/` — mai per corrispondenza di nome: `materiali/checklist-qualita.html` è materiale didattico e resta nella consegna.
- Le istruzioni operative restano nella consegna: senza di esse l'esercizio non funziona.
- Nessun collegamento della consegna punta a un file rimosso.
- La consegna si apre e si naviga per intero partendo dal suo `index.html`, senza rete.

#### FR-8: Pannello locale di redazione
Uno strumento locale permette di scrivere la regia, collocarla nel punto voluto e rigenerare, senza usare il terminale.

**Conseguenze verificabili:**
- Ascolta solo sull'interfaccia locale.
- Aperto senza il proprio server, spiega come avviarlo invece di mostrare un errore.
- Ogni artefatto del catalogo offre almeno un punto valido a cui agganciare una regia.

### 4.3 Artefatti manipolabili

**Descrizione.** Il tratto distintivo: il lettore muove qualcosa e il risultato cambia. Non simulazioni fedeli dei modelli, ma modelli del *suo* problema — costi, rischi, obblighi, tempi. Il repertorio che serve è ristretto e alla portata: numeri trascinabili dentro la frase, parametri regolabili, verdetti che cambiano, confronti prima/dopo, autovalutazioni che diagnosticano invece di dare un voto. Realizza UJ-1, UJ-2.

**Requisiti funzionali**

#### FR-9: Modello manipolabile
Un artefatto manipolabile espone parametri modificabili e ricalcola il proprio esito a ogni modifica, interamente nel browser.

**Conseguenze verificabili:**
- Nessuna chiamata di rete: funziona aperto dal disco.
- Nessuno stato conservato fra sessioni; riaprendo si riparte dai valori iniziali.
- Ogni parametro dichiara le proprie unità e i propri limiti; i valori assurdi sono impediti, non solo segnalati.
- Le stime dichiarano come sono calcolate.

#### FR-10: Configurazione trasportabile
Lo stato di un artefatto manipolabile si può catturare in un link e ripristinare aprendolo. Realizza UJ-1.

**Conseguenze verificabili:**
- Il link si costruisce dai valori correnti anche quando il browser impedisce di aggiornare l'indirizzo, come accade aprendo un file dal disco.
- Aprendo il link, i valori ripristinati sono quelli catturati.
- Un link senza configurazione apre i valori iniziali.

#### FR-11: Casi preimpostati
Ogni artefatto manipolabile offre configurazioni pronte che portano il lettore nei punti dove il modello insegna qualcosa.

**Conseguenze verificabili:**
- Almeno un caso porta a una condizione limite o a un esito controintuitivo.
- Il caso attivo è riconoscibile finché non si modifica un parametro.

#### FR-12: Conseguenze delle scelte
Dove l'artefatto produce una classificazione, mostra quali modifiche la cambierebbero — cercate nello spazio delle configurazioni, non elencate a mano.

**Conseguenze verificabili:**
- Quando nessuna modifica singola cambia l'esito, l'artefatto cerca le combinazioni minime e dice che ne servono più di una.
- Quando nessuna combinazione cambia l'esito, lo dichiara invece di tacere.
- Ogni modifica proposta è applicabile con un gesto.

### 4.4 Modalità d'aula

**Descrizione.** Le condizioni reali di una sala: proiettore, luce, venti persone, nessuna rete garantita. Nessun artefatto del canone internazionale si occupa di questo — è materiale pensato per un lettore solo davanti al suo schermo. Realizza UJ-1.

**Requisiti funzionali**

#### FR-13: Vista da proiezione
Ogni artefatto offre una resa leggibile in sala illuminata: contrasto invertito e testo più grande.

**Conseguenze verificabili:**
- Attivabile in un gesto, senza ricaricare e senza perdere lo stato.

#### FR-14: Dispensa stampabile
Ogni artefatto produce una versione da stampare priva di comandi, barre e regia.

**Conseguenze verificabili:**
- La stampa non contiene la regia nemmeno partendo dalla copia per chi conduce.
- Nessun blocco viene tagliato a metà pagina.

### 4.5 Firma, data e licenza

**Descrizione.** Il controllo su ciò che circola non è tecnico: è la freschezza del contenuto, la firma di chi l'ha fatto e la licenza scritta. Sulla normativa questo basta: una copia di oggi fra dodici mesi è sbagliata, e il problema diventa di chi la usa. Realizza UJ-2.

**Requisiti funzionali**

#### FR-15: Data di aggiornamento visibile
Ogni artefatto mostra la data a cui il contenuto è aggiornato.

**Conseguenze verificabili:**
- La data compare anche nella versione stampata.
- Un artefatto senza data è segnalato come rilievo.

#### FR-16: Firma e licenza
Ogni artefatto contiene nome del produttore, licenza d'uso e collegamento alla versione viva. La licenza è: *«Uso consentito con citazione della fonte. Vietata la rivendita.»*

**Conseguenze verificabili:**
- Le tre informazioni sopravvivono a copia, spostamento e stampa.

#### FR-16b: Dati fittizi negli esercizi
Società, persone, importi, documenti e riferimenti usati negli esercizi sono inventati e costruiti per l'aula. Dove un esercizio può tentare l'uso di materiale aziendale reale, l'artefatto lo dice esplicitamente.

**Conseguenze verificabili:**
- Nessun artefatto contiene dati riconducibili a un'organizzazione reale.
- Gli esercizi che potrebbero indurre a caricare documenti interni riportano la condizione: solo con lo strumento approvato dalla propria organizzazione.

### 4.6 Qualità a due regimi

**Descrizione.** I corsi sono consegne e hanno già uno standard: trenta controlli automatici e tre a giudizio, con la regola di non consegnare finché restano rilievi bloccanti. Alle pagine singole si applicano solo i quattro controlli che verificano le promesse fatte: senza di quelli la promessa «funziona senza rete» si rompe in silenzio. Trenta regole su una pagina sperimentale ucciderebbero le idee nuove.

**Requisiti funzionali**

#### FR-17: Controlli minimi su ogni artefatto
Un comando verifica su qualunque artefatto: assenza di risorse esterne **caricate**, assenza di collegamenti locali rotti, assenza di regia nel materiale pubblico, presenza della data di aggiornamento.

**Conseguenze verificabili:**
- È vietato ciò che il browser carica — script, fogli di stile, font, immagini, richieste di rete — perché rompe la promessa di funzionare senza rete. È ammesso ciò su cui il lettore clicca: i rimandi bibliografici non sono un rilievo.
- Esce con codice diverso da zero quando resta un rilievo bloccante.
- Segnala il file e la riga.

#### FR-18: Controlli estesi sui corsi
Sui corsi resta in vigore la checklist esistente — controlli automatici e controlli a giudizio — eseguita prima di generare una consegna.

**Conseguenze verificabili:**
- La generazione di una consegna con rilievi bloccanti aperti richiede una forzatura esplicita.
- I controlli a giudizio non vengono automatizzati né silenziati: restano una domanda posta a chi produce. Sono il contrappeso a SM-C2.
- Il codice colore delle tre parti resta un controllo bloccante: qualunque intervento sugli stili condivisi lo deve rispettare.

## 5. Non obiettivi

- **Non è una piattaforma di e-learning.** Niente iscrizioni, progressi, certificati, tracciamento.
- **Non si adotta un framework.** Il canone delle explorable è fatto a mano; i framework di documentazione risolvono un problema che non abbiamo e ne creano uno di manutenzione che non possiamo permetterci.
- **Non si insegue la fedeltà tecnica** degli explainer sui modelli: inferenza nel browser e 3D sono fuori portata e fuori bersaglio.
- **Non si progetta per il formatore terzo.** È servito dagli stessi pezzi e ben accetto, ma i suoi incentivi sono misti — passa lavoro quando non ha tempo di farlo lui — quindi le scelte di prodotto si prendono guardando l'aula propria.
- **Non si protegge con la cifratura.** Chi riceve un file lo può copiare; fingere il contrario costa e non serve.
- **Non si insegue l'indicizzazione**: il valore non è nel traffico.

## 6. Perimetro della prima versione

### 6.1 Dentro

*Diviso fra ciò che esiste già e ciò che manca: metà del lavoro è fatto e non va rifatto.*

**Già costruito e conforme — da riconoscere, non da rifare**
- Artefatti manipolabili con configurazione trasportabile, casi preimpostati e conseguenze delle scelte (FR-9, FR-10, FR-11, FR-12): due implementazioni funzionanti.
- Regia separata e generazione della copia per chi conduce, nella resa deep-dive (FR-5, FR-6), con pannello locale di redazione (FR-8).
- Vista da proiezione e dispensa stampabile, su una pagina (FR-13, FR-14).
- Checklist estesa sui corsi, con verifica eseguibile (FR-18).

**Da costruire**
- Manifest unico e pubblico con i campi di FR-1 (FR-1, FR-1b).
- Generazione di menù, catalogo, sidebar e mappa (FR-2, FR-3, FR-4).
- Estrazione dei tool dai corsi come artefatti autonomi (FR-2b).
- Regia nella resa a cartella e generazione della consegna (FR-7).
- Firma, data, licenza e regola dei dati fittizi su tutti gli artefatti (FR-15, FR-16, FR-16b).
- Controlli minimi su ogni artefatto (FR-17).
- Vista da proiezione e dispensa stampabile estese a tutti gli artefatti (FR-13, FR-14).
- **Secondo repository privato**, per i sorgenti dei corsi e la regia. Entra qui non per riservatezza ma per conservazione: oggi quel materiale è escluso dal controllo di versione e vive in copia unica.
- Riconduzione dei dieci artefatti esistenti al manifest e ai controlli.

### 6.2 Fuori, per ora

- **Controllo d'accesso online all'area riservata** (Cloudflare Access, dominio proprio): si attiva quando esiste qualcosa che *deve* restare aggiornato online. Fino ad allora la Consegna offline copre il bisogno. `[NOTA PER IL PM]` Vittorio propende per questa via: è una questione di sequenza, non di direzione. Il secondo repository privato è invece in perimetro (§6.1): serve a conservare i sorgenti, non a proteggerli dal pubblico.
- **Ricerca full-text**: con qualche decina di artefatti la mappa basta.
- **Versionamento dei contenuti**: la data di aggiornamento è sufficiente finché non ci sono più consegne in circolazione della stessa cosa.
- **Vendita e distribuzione a pagamento**: non prima che esista una domanda pagante.
- **Traduzione in inglese**: la posizione difendibile è l'italiano.
- **Assistente di redazione degli artefatti**: comporre nuovi tool, pagine e corsi passando una richiesta a un modello guidato da un contratto che codifica formato, layout e convenzioni. `[NOTA PER IL PM]` Non è remoto come sembra: la checklist v0.01 *è già* quel contratto, ed è eseguibile — il che permette un ciclo genera, verifica, correggi invece di una generazione da rileggere a mano. Si affronta quando il manifest e i controlli minimi sono in piedi, perché sono loro il bersaglio contro cui l'assistente genererebbe.

## 7. Come si capisce se funziona

**Primario**
- **SM-1**: pubblicare un artefatto nuovo non richiede di modificare a mano nessun file esistente oltre al manifest. Valida FR-1, FR-2.
- **SM-2**: nessuna consegna esce con la regia dentro, e nessuna consegna esce priva di qualcosa che serviva. Valida FR-5, FR-7.
- **SM-3**: il materiale viene usato in aula senza cercare soluzioni di ripiego — niente PDF di riserva, niente slide parallele. Valida FR-13, FR-14, FR-10.

**Secondario**
- **SM-4**: un artefatto vecchio si riapre e si aggiorna senza doverne ricostruire l'impianto.
- **SM-5**: qualcuno chiede di riusare il materiale — segnale che circola e porta il nome giusto.

**Contro-metriche (da non ottimizzare)**
- **SM-C1**: numero di artefatti. Bilancia SM-1: dieci pagine deboli valgono meno di tre manipolabili.
- **SM-C2**: numero di controlli di qualità. Bilancia SM-2: oltre una certa soglia la conformità scoraggia le pagine strane, che sono il prodotto.
- **SM-C3**: quantità di strumenti di supporto. Bilancia SM-1: ogni pezzo di infrastruttura è manutenzione a carico di una persona sola.

## 8. Domande aperte

*Le domande sulla forma del manifest sono state risolte e sono confluite in §3 e §4.1. Restano quelle che si decidono meglio più avanti, ciascuna con la condizione che le riapre.*

1. **Che cos'è la mappa**: mappa concettuale dei temi o rappresentazione dei percorsi di apprendimento? *Si riapre quando si costruisce la mappa: il manifest la regge in entrambi i casi, ed è una scelta che si prende meglio con le pagine sotto gli occhi.*
2. **In che ordine ricondurre allo standard i dieci artefatti esistenti**, senza fermare la produzione di contenuti nuovi. *È pianificazione, non requisito: si affronta nelle epiche.*
3. **Il debito degli stili duplicati** — la stessa classe definita in modo diverso in file diversi. Il generatore lo assorbe o resta debito accettato? *Si riapre quando il generatore inietta la navigazione. Vincolo da rispettare: il codice colore delle tre parti è un controllo bloccante dei corsi, e un blocco di stile comune non lo può contraddire.*
4. **La checklist può diventare il contratto di generazione?** Se un assistente di redazione compone gli artefatti contro i controlli, aumentare i controlli migliora gli artefatti invece di irrigidirli — e la contro-metrica SM-C2 va riscritta. *Si riapre quando si valuta l'assistente di redazione (§6.2).*
5. **Quali controlli della checklist valgono anche fuori dai corsi?** Oggi sono due regimi separati per scelta. Il codice colore, per esempio, potrebbe avere senso anche nei deep-dive. *Si riapre alla seconda o terza pagina nuova costruita con il manifest.*

## 9. Indice delle assunzioni

- §2.3 — I casi d'uso sono ricostruiti dalla sessione di lavoro, non da osservazione diretta di aule reali. `[ASSUNZIONE]`
- §4.1 — Si assume che il manifest resti abbastanza piccolo da essere scritto a mano, senza interfaccia dedicata. `[ASSUNZIONE]`
- §4.2 — Si assume che l'elenco delle cartelle non consegnabili resti breve e dichiarato, senza bisogno di regole più fini del singolo file. `[ASSUNZIONE]`
- §4.3 — Si assume che i modelli manipolabili restino calcolabili nel browser senza librerie esterne. `[ASSUNZIONE]`
- §4.6 — Si assume che i quattro controlli minimi siano estraibili dallo script esistente senza riscriverlo. `[ASSUNZIONE]`
- §6.2 — Si assume che l'assenza di area riservata online non blocchi nessuna aula già programmata. `[ASSUNZIONE]`
