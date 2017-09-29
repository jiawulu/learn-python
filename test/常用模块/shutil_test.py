import shutil

## 文件copy
shutil.copy('readme.md','readme.bak')
shutil.copymode('readme.md','readme.bak')
shutil.copystat('readme.md','readme.bak')
