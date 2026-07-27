from pathlib import Path
import shutil
#from .filesystem import extensionPath  # relative to package
'''
Contains:
Extension Mapping
extensionPath
fileFinder
organizeByExtensionextensions
'''
'''
Extension Mapping:
extensions dictionary is a nested dictionary. {Generic: Common_uses} -> {Common_use: extensions}
'''
extensions = { # put on a different file named extensionPath.py
    "Documents": {
                "WordProcessing": {"docx", "doc", "odt", "rtf", "txt"},
                "Spreadsheets":   {"xlsx", "xls", "csv", "ods"},
                "Presentations":  {"pptx", "ppt", "odp"},
                "PortableShared": {"pdf"},
                "WebOther":       {"html", "xml", "epub"},
                },
    "Music":     {
                "CompressedStandard":  {"mp3", "aac", "ogg", "wma", "m4a"},
                "CompressedLossless":  {"flac", "alac", "ape"},
                "NoCompressed":        {"wav", "aiff", "pcm"},
                "DataAndInstructions": {"mid", "midi", "opus", "dsd"},
                },
    "Images":    {
                "Standard":     {"jpg", "jpeg", "png", "gif", "webp"},
                "Professional": {"tiff", "tif", "bmp", "heic", "heif"},
                "Vectorial":    {"svg", "eps", "ai"},
                "Modification": {"psd", "xcf", "raw"},
                },
    "Video":     {
                "VideoUniversal":    {"mp4", "webm", "m4v"},
                "VideoLegacy":       {"mov", "avi", "wmv"},
                "VideoProfessional": {"mkv", "mts", "m2ts", "vob"},
                "VideoMobile":       {"3gp", "flv"},
                },
    "Compress": {
                "Standard":          {"zip", "rar"},
                "Hight Compression": {"7z", "tgz", "tar.gz"}, #tag.gz isn't see.. to solve
                "OS specific":       {"dmg", "iso", "cab"}
                }
    }

def extensionPath(extension: str = None, mode: int = 0) -> Path:
  '''
  Generate an extension based path
  Return a Path Based on extension like:
  mode:
    0 -> Generic
    1 -> Generic / Common_use
    2 -> Generic / Common_use / extension
    3 -> Common_use
    4 -> Common_use / extension
    5 -> extension
  '''
  if not extension: ext = ""
  else:             ext = extension.split(".")[-1].lower()
  mode = max(0, min(mode, 5))  # clamp 0 <= mode <= 5

  path = None

  for generic, subdict in extensions.items(): #Allow a single cicle on a dictionary (by key and value)
    for subgeneric, extset in subdict.items():
      if ext in extset:
        path = [generic, subgeneric, ext]
        break #innerloop
    if path:  break #loop

  if not path:  path = ["Other", "Unknown", ext]

  output = Path()

  if 0 <= mode <= 2:              output /= path[0]
  if 1 <= mode <= 4:              output /= path[1]
  if mode == 2 or 4 <= mode <= 5: output /= path[2]

  return output

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

##Organize files in a folder hierarchy based on extension

def organizeByExtension(cwd: Path = None, subFolder: bool = False):
  '''
  Divide files into folders based on their Extension
  '''
  def moveF(path: Path, destination: Path):
    try:  shutil.move(str(path), str(destination)) #change file path, it may be in use, denied permission or not found
    except (PermissionError, FileNotFoundError, OSError) as e: print(f"[ERROR] Moving {path} -> {destination}: {e}")

  if cwd is None: cwd = Path.cwd()
  try:  baseFileList = fileFinder(cwd, subFolder)
  except Exception as e:
    print(f"[ERROR] baseFileList in organizeByExtension: {e}")      
    return # cwd must be a Path

  for path in baseFileList:
    try: #file can be removed
      if not path.is_file():  continue

      #get file extension
      relPath = extensionPath(path.suffix, 2)
      #if relPath.parts and relPath.parts[0] in path.parts:  continue # check if directory is organized yet
      
      # absolute = cwd + relative + name
      newPath = cwd / relPath
      if path.parent == newPath:  continue # check if directory is organized yet

      try:  newPath.mkdir(parents=True, exist_ok=True) # create folders if they don't already exist
      except Exception as e:  # ipotetically it can be too long
        print(f"[ERROR] Creating {newPath} : {e}")
        continue
    
      destination = newPath / path.name

      # no overwrite
      counter = 1
      while destination.exists(): #file already yet
          destination = newPath / f"{path.stem}_{counter}{path.suffix}" #adding a number at end of file name, before extension
          counter += 1
      moveF(path, destination)    
    except Exception as e:
      print(f"[ERROR] in organizeByExtension: {e}")
