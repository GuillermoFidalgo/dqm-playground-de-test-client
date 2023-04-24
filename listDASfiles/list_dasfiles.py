# IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal and then cd into the working directory.

import subprocess

eras = ['A','B','C','D','E','F','G']
for i in eras:
    
    if i == 'A':
        cmd = f'dasgoclient -query="file dataset=/ZeroBias/Run2022{i}-19Jan2023-v2/DQMIO" | grep "/store" > listfiles.txt' 
    else:
        cmd = f'dasgoclient -query="file dataset=/ZeroBias/Run2022{i}-19Jan2023-v2/DQMIO" | grep "/store" >> listfiles.txt'
    
    subprocess.run(cmd, shell=True, check=False)