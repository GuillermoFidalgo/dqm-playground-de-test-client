# # IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal at the working directory.
import subprocess, os, argparse


# read arguments
parser = argparse.ArgumentParser(description='Copy files from DAS to local')
parser.add_argument('--redirector', default='root://cms-xrd-global.cern.ch/',
                  help='Redirector to read remote files')
parser.add_argument('--outdir', default=os.path.abspath('.'),
                  help='Local directory where to put the copied file')
parser.add_argument('--nfiles', default=None,type=int,
                  help="Limit the number of files to copy. (Default: all files from the listfiles.txt will be downloaded)")
parser.add_argument("--listfiles",type=str,
                    default='listfiles.txt',
                    help='A text file with list of paths from DAS.')
parser.add_argument("-v","--verbose",action="store_true",
                    help="Prints to screen what files are already found in the outputdir")

args = parser.parse_args()

redirector = args.redirector
outputdir = args.outdir
nfiles=args.nfiles
listfiles = args.listfiles
verbose = args.verbose

f = open(listfiles,'r')
files = [i.rstrip('\n') for i in f.readlines()]
f.close()
del f

def file_downloaded(filename,directory='./'):
    return os.path.exists(directory.rstrip('/')+"/"+filename)


if os.path.exists(outputdir):
    print(f'Directory {outputdir} already exists. Downloading to {outputdir}')
else:
    print(f'Downloading to {outputdir}')
    os.makedirs(outputdir)

if nfiles != None:
    print(f"Downloading {nfiles} files into {outputdir}")

for file in files[slice(nfiles)]:
    fname = file.strip('/').replace('/','_')
    cmd = f'xrdcp {redirector}{file} {outputdir}/{fname}'
    if file_downloaded(fname,outputdir): 
        if verbose:
            print(f'{fname} already present. Moving on the the next!')
        continue
    else: 
            subprocess.run(cmd, shell=True, check=False,)

            