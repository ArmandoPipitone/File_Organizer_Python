from pathlib import Path
import os

def fileFinder(cwd: Path = None, subFolder: bool = False) -> list[Path]:
  '''
  Taking File on indicated Path (or CWD) and (if True) in subFolders
  '''
  if cwd is None: cwd = Path.cwd()
  
  fileList = []
  try:
    for item in cwd.iterdir():
      if item.is_symlink():  continue #skip symlink (collegamenti)
      if item.is_dir(): #directory
        if subFolder:  fileList.extend(fileFinder(item, subFolder))
        #se vuota elimino -> meglio metodo a parte
      else: fileList.append(item)
  except (PermissionError, OSError) as e:
    print(f"[ERROR] {cwd}: {e}")

  return fileList