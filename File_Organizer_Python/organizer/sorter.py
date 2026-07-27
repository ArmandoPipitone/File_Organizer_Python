from typing import Iterable, Callable, TypeVar, Any
from pathlib import Path

T = TypeVar("T")
'''
Sort
Generic InsertionSort, using a Parameter
the Parameter key is a lambda function applying to elements.
(It's useful for writing code once and using it in multiple ways)
'''

def mySorting(item: Iterable[T] = None, key: Callable[[T], Any] = None, reverse: bool = False) -> list[T]:
  '''
  Insertion Sort [O(N^2)]

  item must be an Iterable[T] -> list[T], tuple[T], set[T], ecc...
  key represents what is being ordered 
  key is a function who take T as argument and return 'Any' type (Any is in typing module)
  reverse is a boolean that reverses the sorting logic
  '''

  if item is None:  item = list(Path().iterdir())  #This check allows listdir() to be evaluated at call (runtime).
  else: item = list(item)   #convert Iterable to a List
  if not item: return []    #no element was found

  if key is None: key = lambda x: x.name   #identity

  index = [0]

  for actual in range(1, len(item)):  #see yet
    for sortedYet in range(len(index)): #already seen
      left  = key(item[actual])       #inside the inner loop because it can change
      right = key(item[index[sortedYet]])
      if (left < right and not reverse) or (left > right and reverse):
        index.insert(sortedYet, actual)
        break
    else: index.append(actual)

  Output = [item[i] for i in index]
  #if reverse: Output.reverse() #alternative -> inverting result, not the sorting logic
  return Output

SORT_MODE = {
             "Name":             lambda x: x.name,
             "NameNoCase":       lambda x: x.name.lower(),
             "Extension":        lambda x: x.suffix,
             "Size":             lambda x: x.stat().st_size,
             "TimeCreation":     lambda x: x.stat().st_ctime, # st_ctime: creation time (Windows) / metadata change (Unix)
             "TimeModification": lambda x: x.stat().st_mtime,
             "TimeAccess":       lambda x: x.stat().st_atime
             }
        
def sortFiles(item: Iterable[T] = None, modeName: str = "Default", reverse: bool = False) -> list[T]:
  '''
  mode:
    "Name"    "NameNoCase"    "Extension"
    "Size"    "TimeCreation"  "TimeModification"
    "TimeAccess"  "Default"
  '''
  if item == None: return []
  
  keyF = SORT_MODE.get(modeName)
  if keyF is None or modeName == "Default": return sorted(item, reverse = reverse) # built-in sorted more performing and optimized
  
  return mySorting(item, keyF, reverse)
  

