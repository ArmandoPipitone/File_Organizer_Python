# 📁 Smart File Organizer & Sorter (Python CLI)

Un'utilità da riga di comando (CLI) sviluppata in **Python 3.10+** per l'organizzazione, la catalogazione e il riordino automatico dei file all'interno del file system.
Il progetto sfrutta la potenza di **`pathlib`** per una gestione multipiattaforma dei percorsi, implementa una mappatura estensibile per categoria/sottocategoria, un algoritmo di ordinamento custom con **Type Hinting** e un modulo di pulizia sicura delle directory vuote.

---

## ✨ Caratteristiche Principali

* **Organizzazione Multilivello basata su Estensioni:** Catalogazione automatica dei file in gerarchie di cartelle configurabili in livelli di profondità (es. `Categoria / Sottocategoria / Estensione`).
* **Gestione Conflitti Nomi (No Overwrite):** Rilevamento dei duplicati nella destinazione con rinomina automatica progressiva (es. `documento_1.pdf`) per prevenire perdite accidentali di dati.
* **Algoritmo di Ordinamento Flessibile (Custom & Native):**
  * **Insertion Sort Personalizzato (`mySorting`):** Implementazione didattica ricca di *Type Hinting* (`Iterable`, `Callable`, `TypeVar`) e funzioni *Lambda* per ordinare file secondo metadati come dimensione, data di creazione/modifica o estensione.
  * **Fallback Nativo Ad Alte Prestazioni:** Utilizzo trasparente della funzione built-in `sorted()` di Python per la massima velocità su ampi volumi di dati.
* **Scansione Ricorsiva:** Supporto completo per la ricerca e il riordino di file presenti all'interno di sottocartelle annidate.
* **Clean-up Ricorsivo:** Pulizia automatica delle directory rasteggiate che rimangono vuote a seguito dello spostamento dei file, ignorando in sicurezza symlink e gestendo i permessi di sistema.
* **Architettura Modulare:** Codice strutturato in package con separazione netta delle responsabilità per ciascun modulo.
* **Interfaccia CLI Completa:** Controllo totale dell'esecuzione tramite argomenti da riga di comando gestiti via `argparse`.

---

## 🛠️ Tech Stack & Requisiti

* **Linguaggio:** Python 3.10+
* **Librerie di Sistema:** `pathlib` (per la gestione object-oriented dei percorsi), `shutil` (per le operazioni di I/O ad alte prestazioni).
* **Dipendenze:** Nessuna libreria esterna (100% Python Standard Library).

---

## 📐 Struttura della Mappatura Estensioni

L'organizzatore suddivide i file tramite una struttura dati a dizionario nidificato (`extensions`):

```text
Target Directory/
├── Documents/
│   ├── WordProcessing/ (.docx, .txt, .odt...)
│   ├── Spreadsheets/   (.xlsx, .csv...)
│   └── PortableShared/ (.pdf)
├── Images/
│   ├── Standard/     (.jpg, .png, .webp...)
│   └── Professional/ (.tiff, .raw, .psd...)
├── Video/
├── Music/
└── Compress/
```

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
```
