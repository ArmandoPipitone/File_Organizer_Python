# 📂 File Organizer (Python)

Uno strumento CLI modulare e automatizzato per l'organizzazione intelligente dei file in directory strutturate per tipologia.
Il progetto include la gestione avanzata delle collisioni dei nomi, la scansione ricorsiva del filesystem e un'implementazione didattica di un algoritmo di **Insertion Sort generico**.

---

## ✨ Caratteristiche Principali

* **Classificazione Dinamica:** Organizzazione automatica dei file basata su mappatura configurabile `estensione -> categoria` (Documenti, Immagini, Video, Audio, ecc.).
* **Gestione Collisioni Nomi:** Ridenominazione automatica e incrementale dei file in caso di duplicati per evitare la sovrascrittura accidentale dei dati.
* **Scansione Ricorsiva:** Supporto completo per la ricerca e il riordino di file presenti all'interno di sottocartelle annidate.
* **Pulizia Automatica:** Rimozione automatica delle directory vuote residue dopo lo spostamento dei file.
* **Architettura Modulare:** Codice strutturato in package con separazione netta delle responsabilità per ciascun modulo.

---

## 🛠️ Tech Stack & Requisiti

* **Linguaggio:** Python 3.10+
* **Librerie di Sistema:** `pathlib` (per la gestione object-oriented dei percorsi), `shutil` (per le operazioni di I/O ad alte prestazioni).
* **Dipendenze:** Nessuna libreria esterna (100% Python Standard Library).

---

## 🗂️ Struttura del Progetto

```text
file-organizer/
├── main.py                # Entry point dell'applicazione (CLI / Execution)
└── organizer/             # Package principale dei moduli
    ├── __init__.py        # Inizializzazione del package Python
    ├── sorter.py          # Algoritmi di ordinamento (custom e built-in)
    ├── filesystem.py      # Scansione del filesystem e ricerca file
    ├── organizer.py       # Logica core di smistamento ed estensioni
    └── cleanup.py         # Utility per la rimozione delle cartelle vuote
