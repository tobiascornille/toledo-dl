import os
rootdir = './'

for subdir, dirs, files in os.walk(rootdir):
  for file in files:
    to_rename = os.path.join(subdir, file)
    os.rename(to_rename, to_rename.replace(',', ''))