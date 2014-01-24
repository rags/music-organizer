import os
import quodlibet
from quodlibet.formats import MusicFile

quodlibet.config.quit()
quodlibet.config.init()

def musicfiles(folder, *exts):
    exts = exts or ['']
    for root, dirnames, filenames in os.walk(folder):
      for filename in filenames:
          if not filename.endswith(tuple(exts)):
              continue
          file_path = os.path.join(root, filename)
          yield file_path, MusicFile(file_path)


