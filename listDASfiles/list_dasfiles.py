# IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal and then cd into the working directory.

import subprocess,os, argparse



# read arguments
parser = argparse.ArgumentParser(description='Make a list of files found on DAS')

parser.add_argument('--outputdir', default=os.path.abspath('.'),
                  help='Local directory where to put the copied file')


parser.add_argument("--listfiles",type=str,
                    default='listfiles.txt',
                    help='A text file with list of paths from DAS.')

args = parser.parse_args()


outputdir = args.outputdir

listfiles = args.listfiles


eras = ['A','B','C','D','E','F','G']
for i in eras:
    
    if i == 'A':
        cmd = f'dasgoclient -query="file dataset=/ZeroBias/Run2022{i}-19Jan2023-v2/DQMIO" | grep "/store" > {outputdir}/{listfiles}' 
    else:
        cmd = f'dasgoclient -query="file dataset=/ZeroBias/Run2022{i}-19Jan2023-v2/DQMIO" | grep "/store" >> {outputdir}/{listfiles}'
    
    subprocess.run(cmd, shell=True, check=False)