# Addendum — I2ETools

Materiale emerso durante la stesura che non appartiene al PRD ma serve a chi progetta l'architettura o la UX. Il PRD dice *cosa*; qui c'è il *come* e il *perché non altrimenti*.

## Hosting e area riservata — alternative valutate

Ricerca del 3 settembre 2026. Vincolo di partenza: repository pubblico su GitHub Pages in modalità legacy, nessuna build, un solo manutentore.

**Perché il repository pubblico rende inutile qualunque protezione applicata al sito.** `codeload.github.com/<utente>/<repo>/zip/refs/heads/main` restituisce l'intero albero senza autenticazione; `raw.githubusercontent.com` serve il singolo file; le API dei contenuti enumerano i percorsi; `git clone` porta anche la cronologia, quindi un file cancellato resta. Ogni schema a URL non indicizzati o password in JavaScript è decorativo.

| Opzione | Costo/anno | Protezione | Sforzo |
|---|---|---|---|
| **Cloudflare Pages + Access** (consigliata) | ~15 € di dominio | reale, per persona, revocabile; elenco email + PIN monouso | 2 h + migrazione DNS |
| Netlify Pro | 240 € | password condivisa, non revocabile per singolo | minimo |
| Vercel | ~2.040 € | password condivisa | minimo |
| StatiCrypt su Pages | 0 € | AES reale ma forzabile offline, chiave unica per la classe | 20 min |
| GitHub Enterprise Cloud | ~250 €/utente | reale, ma richiede un account GitHub per studente | alto |
| Vendita del pacchetto (Payhip, SendOwl) | 0 € + ~5% | è distribuzione, non hosting | basso |

Sull'opzione consigliata: Access richiede un dominio attivo su Cloudflare e non copre `*.pages.dev`; il piano gratuito è indicato fino a circa 50 utenti (dato di fonte terza); ricorrono segnalazioni di richiesta di carta di credito anche sul piano a zero euro, non verificate per il 2026.

`robots.txt` non è uno strumento di riservatezza: è un elenco pubblico di ciò che si vorrebbe nascondere, e Google indicizza comunque gli URL trovati altrove. Su GitHub Pages non si possono emettere intestazioni HTTP, quindi `X-Robots-Tag` non è disponibile e resta solo il `noindex` nella pagina.

Prerequisito comune a ogni scenario: separare il materiale riservato in un secondo repository. Finché sta in quello pubblico, nessuna scelta di hosting produce effetto.

## Il canone delle explorable explanations — come è costruito

| Opera | Framework | Build | Hosting |
|---|---|---|---|
| ciechanow.ski | nessuno — 327 KB di JS per articolo, canvas e WebGL scritti a mano | nessuna | nginx proprio |
| ncase.me/trust | nessuno — 39 script semplici, Pixi e howler | nessuna | GitHub Pages |
| Red Blob Games | nessuno nel bundle servito | una riga di esbuild | nginx proprio |
| Distill.pub | nessuno — d3 più JS per articolo | nessuna | — |
| Polo Club (Transformer Explainer, CNN, GAN Lab) | Svelte, D3, TF.js/ONNX | sì | GitHub Pages |
| joshwcomeau.com, bbycroft.net | Next.js | sì | Vercel |

Gli autori singoli lavorano senza framework; le istituzioni e gli studi no. **Idyll**, l'unico framework nato per le explorable, è fermo a febbraio 2023. **Tangle** di Bret Victor — i numeri trascinabili dentro la frase — è 13 KB, MIT, senza dipendenze: si incorpora e basta.

Pesi misurati, per decidere cosa non caricare: Alpine.js 44,8 KB; Chart.js 205,9 KB; D3 v7 279,7 KB; p5.js 1,06 MB; Mermaid 3,57 MB. Su una pagina che deve stare in 60-140 KB, l'approccio praticabile è SVG in linea più transizioni CSS più JavaScript essenziale con eventi puntatore.

Fuori portata senza un reparto di sviluppo: inferenza nel browser, 3D in tempo reale, illustrazione su commissione. Alla portata e con l'80% del valore didattico: numeri trascinabili, parametri regolabili, confronti prima/dopo, autovalutazioni diagnostiche, alberi decisionali, sandbox lato client.

## Repertorio delle interazioni, per rapporto valore/costo

| Interazione | A cosa serve | Costo | Quando si ritorce contro |
|---|---|---|---|
| Numero trascinabile nella frase | far possedere l'ipotesi a chi legge | mezza giornata | se il numero derivato non si muove visibilmente |
| Parametro regolabile | costruire intuizione su una relazione | 1-2 h | oltre due o tre parametri insieme |
| Autovalutazione diagnostica | far emergere il fraintendimento | 2-4 h | se sembra un voto invece di uno specchio |
| Confronto prima/dopo | rendere concreta una regola | 1-2 h | se la differenza è troppo lunga da tenere a mente |
| Albero decisionale | applicare una tassonomia al proprio caso | 1-2 giorni | se l'esito sembra arbitrario |
| Scrollytelling | sequenziare un argomento lungo | 3-5 giorni | sempre: toglie il controllo del ritmo, è video con passaggi in più |

## Vuoti di mercato rilevati

- **Formazione italiana sull'articolo 4**: mercato attivo — PwC Italia, Fondo For.Te, Vega Formazione, CSQA, Impact Skills, Kinetikon — tutti con moduli e-learning, webinar e video con quiz. Nessuno vende un prodotto basato su simulazione manipolabile.
- **Explorable in italiano**: `explorabl.es` non ne elenca; la lista `awesome-explorables` non contiene voci non inglesi.
- **Strumenti sull'AI Act**: quelli esistenti sono navigatori di documenti (AI Act Explorer del FLI) o questionari lineari (verificatore della Commissione, verificatore FLI, entrambi disponibili in italiano). Nessuno mostra *quali decisioni progettuali spostano la classificazione*.
- **Explorable per decisori**: il genere serve ingegneri, ragazzi e ricercatori. Chi decide un budget vuole manipolare teste, ore, tassi di errore ed esposizione, non parametri di modello.
- **Materiale d'aula**: nessuna opera del canone prevede modalità docente, stato nell'URL, resa da proiettore o dispensa stampabile.
- **Quasi-concorrente da guardare**: `no-ai-act.eu` di Matteo Angeloni — MIT, Phaser 3, giocabile, in italiano, sull'AI Act, ma rivolto a scuole e studenti.

## Anatomia dei corsi esistenti

Ricavata da `docs/templates/`, fuori dal repository pubblico.

**Corso base — Tecniche di base di prompt engineering.** 5 lezioni, 10 ore. Due punti d'ingresso allineati e separati: `index.html` per chi partecipa, `docente/index.html` per chi conduce. Ogni lezione in tre parti con codice colore stabile: lezione (indaco), esercitazioni (verde), materiale (ambra). Quindici tool interattivi. Materiali trasversali: glossario con la lezione di introduzione, cinque casi studio per dominio, checklist di qualità degli output, Body of Knowledge su dieci aree secondo i descrittori EQF. Risultato dichiarato: chi partecipa esce con cinque prompt documentati e validati da un collega.

**Prompting avanzato — Modulo 1.** Tronco comune più quattro percorsi verticali (finance, sales, legal, project), ciascuno con la propria data room, laboratorio, test e guida per chi conduce. Un unico mondo narrativo — il Progetto NEMBO — fa da contesto a tutti gli esercizi. Istruzioni operative documentate: i documenti vanno caricati in anticipo sul sistema dei partecipanti.

**Controllo qualità.** `qualita/` contiene la checklist v0.01 — 30 controlli automatici, 3 a giudizio, con ambiti, soglie modificabili e registro delle versioni — e `verifica_corso.py`, che la applica ed esce con codice diverso da zero quando restano rilievi. Regola dichiarata: non consegnare finché restano rilievi bloccanti o gravi. La cartella va rimossa dalla consegna, come `docente/`.

**Osservazione per il PRD.** In entrambi i corsi la separazione della regia è affidata a un gesto manuale: cancellare una cartella prima di consegnare. Funziona finché ci si ricorda.

## Debito tecnico già visibile

Le pagine sciolte duplicano stili e comportamenti: `.xbtn` è definita in due file con valori diversi, la barra della modalità d'aula esiste in una sola pagina, i temi condividono la struttura delle variabili ma non i valori. Ogni artefatto nuovo riscrive gli stessi blocchi. Se il generatore inietta la navigazione, può iniettare anche il blocco comune di stile e comportamento — è la stessa meccanica applicata a un secondo tipo di contenuto.

## Script già esistenti

- `tools/costruisci-aula.py` — inietta la regia dai segnaposto `<!-- regia: id -->` e produce la copia `.docente.html`.
- `tools/regia-server.py` + `tools/regia-pannello.html` — pannello locale su 127.0.0.1 per scrivere la regia, collocarla e rigenerare.
- `docs/templates/.../qualita/verifica_corso.py` — verifica di conformità dei corsi.

## Assistente di redazione degli artefatti — perché è praticabile

Idea di Vittorio, fuori dal perimetro della prima versione, annotata perché la strada è più corta di quanto sembri.

**L'idea.** Uno strumento a cui si descrive quello che serve — «un tool che mostri il costo di un contesto lungo», «una lezione sul recupero delle informazioni» — che passa la richiesta a un modello guidato da un contratto su formato, layout e convenzioni, e deposita l'artefatto nel progetto già conforme.

**Perché non è un salto nel vuoto.** Il pezzo che di solito manca a queste idee è il contratto: una descrizione di cosa sia un artefatto conforme, abbastanza precisa da essere seguita e abbastanza formale da essere verificata. Qui esiste già ed è la checklist v0.01, per giunta **eseguibile**.

Da qui il ciclo **genera, verifica, correggi**: il modello produce, lo script boccia, il modello ripara i rilievi. Nessuno rilegge trenta pagine a mano sperando che il codice colore sia giusto.

**La conseguenza sul PRD.** La contro-metrica SM-C2 dice di non aumentare i controlli, perché la conformità scoraggia le pagine strane, che sono il prodotto. Se i controlli diventano il contratto di generazione, la relazione si rovescia: ogni controllo in più è una cosa in meno da correggere a mano. La contro-metrica non sparisce — protegge ancora la sperimentazione — ma va riscritta per distinguere i controlli che *vincolano chi scrive* da quelli che *guidano chi genera*.

**Prerequisiti, nell'ordine.** Il manifest, perché l'artefatto generato deve sapere dove collocarsi. I controlli minimi di FR-17, perché sono il bersaglio per gli artefatti fuori dai corsi. La distinzione fra regia e istruzioni operative, perché un generatore che le confonde produce consegne rotte.

**Il rischio da tenere d'occhio.** Un generatore addestrato sulla conformità produce artefatti conformi e mediocri: il canone delle explorable vive di pagine strane, e la stranezza non è un controllo. La divisione probabile: l'assistente compone l'impianto — struttura, stile, navigazione, controlli — e l'idea interattiva resta a chi scrive.
