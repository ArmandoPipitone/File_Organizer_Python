File Organizer (Python)
*   Script per l’organizzazione automatica di file in directory strutturate per tipologia (documenti, immagini, video, audio).
*   Gestione filesystem con pathlib e shutil
*   Classificazione dinamica tramite mapping estensioni → categorie
*   Gestione collisioni file (rename automatico incrementale)
*   Supporto scansione ricorsiva directory
*   Architettura modulare e riutilizzabile
(Implementazione algoritmo di sorting generico a scopi didattici)

#Nota: il progetto include un'implementazione custom dell'algoritmo Insertion Sort in forma sfruttando:
- Tipo generico
- Funzioni custom (key)
di default verrebbe comunque utilizzato il "sorted()" built-in per le migliori performance

file-organizer/
│
├── main.py                  ← Entry point, CLI / esecuzione principale
├── organizer/               ← Package principale dei moduli
│   ├── __init__.py         ← rende la cartella un package Python
│   ├── sorter.py            ← funzioni di sorting generiche / didattiche
│   ├── filesystem.py     ← fileFinder, funzioni di scansione
│   ├── organizer.py       ← organizeByExtension
│   └── cleanup.py         ← removeEmptyFolders
│
└── README.md          ← documentazione del progetto


file		-> responsabilità
sorter.py		-> Ordinamento
filesystem.py 	-> lettura file
organizer.py	-> logica organizzazione
cleanup.py	-> pulizia
