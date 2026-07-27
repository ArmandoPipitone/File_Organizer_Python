from pathlib import Path
import shutil
def removeEmptyFolders(cwd: Path = None):
  '''
  Find and removing empty folder
  '''
  def eraseEmptyFolder(path: Path):
    try:  path.rmdir()  #remove
    except (PermissionError, FileNotFoundError) as e: print(f"[ERROR] Erasing {path}: {e}") # subclass of OSError
    except OSError: pass # No empty, do nothing

  if cwd is None: cwd = Path.cwd()
  try:
    for path in cwd.iterdir():
      if path.is_symlink():  continue #skip symlink (collegamenti)
      if path.is_dir():
        removeEmptyFolders(path)
        #if not any(path.iterdir()): eraseF(path) # check useless, eraseF remove only if it's an empty folder
        eraseEmptyFolder(path)

  except (PermissionError, OSError) as e:
    print(f"[ERROR] Accessing {cwd}: {e}")
