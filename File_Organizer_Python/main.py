import argparse
from pathlib import Path

from organizer.filesystem import fileFinder
from organizer.sorter import sortFiles
from organizer.organizer import organizeByExtension
from organizer.cleanup import removeEmptyFolders

# Testing with:
  # python main.py --cwd Testing --subfolders --sort "Default" --cleanup
  # sortFiles() decide se usare:
  #   custom sort: mySorting (educational)
  #   builtin sort: sorted() (performance reale)
  # organizeByExtension può usare la lista ordinata o scansionare comunque.

def main():
  '''
  Entry Point
  Manage the CLI
  '''

  parser = argparse.ArgumentParser(description = "Organizza file in base all'estensione")

  parser.add_argument("--cwd", type = str, default = None, help = "Directory di partenza")

  parser.add_argument("--subfolders", action = "store_true", help = "Scansiona anche sottocartelle")

  parser.add_argument("--sort", choices=["Default", "Name", "NameNoCase", "Extension", "Size"], default="Default")

  parser.add_argument("--cleanup", action="store_true", help="Rimuove cartelle vuote dopo l'organizzazione")

  args = parser.parse_args()

  cwd = Path(args.cwd) if args.cwd else Path.cwd()
 
  #print(sortFiles(fileFinder(cwd, args.subfolders), modeName = args.sort)) #demo

  organizeByExtension(cwd, args.subfolders) #rivedere, mancano le altre opzioni

  if args.cleanup:  removeEmptyFolders(cwd)


if __name__ == "__main__":
    main()
