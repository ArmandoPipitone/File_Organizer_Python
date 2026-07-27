@echo off

echo Starting sort files in Testing folder

python main.py --cwd Testing --subfolders --sort "Default" --cleanup
:: sortFiles() decide se usare:
  ::   custom sort: mySorting (educational)
  ::   builtin sort: sorted() (performance reale)
  :: organizeByExtension può usare la lista ordinata o scansionare comunque.

echo Completed!

pause
