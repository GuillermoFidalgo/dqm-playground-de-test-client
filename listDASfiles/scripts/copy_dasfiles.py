# # IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal at the working directory.
import subprocess, os, argparse,datetime


# read arguments
parser = argparse.ArgumentParser(description='Copy files from DAS to local')
parser.add_argument('--redirector', default='root://cms-xrd-global.cern.ch/',
                  help='Redirector to read remote files')
parser.add_argument('--outdir', default=os.path.abspath('.'),
                  help='Local directory where to put the copied file')
parser.add_argument('--nfiles', default=None,type=int,
                  help="Limit the number of files to copy. (Default: all files from the listfiles.txt will be downloaded)")
parser.add_argument("--listfiles",type=str,required=True,
                    help='A text file with list of paths from DAS.')
parser.add_argument("-v","--verbose",action="store_true",
                    help="Prints to screen what files are already found in the outputdir")

args = parser.parse_args()

redirector = args.redirector
outputdir = args.outdir
nfiles = args.nfiles
listfiles = args.listfiles
verbose = args.verbose

f = open(listfiles,'r')
files = [i.rstrip('\n') for i in f.readlines()]
f.close()
del f


def file_downloaded(filename,directory='./'):
    return os.path.exists(directory.rstrip('/')+"/"+filename)

if os.path.exists(outputdir):
    print(f'Directory {outputdir} already exists. \nDownloading to {outputdir}')
else:
    print(f'Downloading to {outputdir}')
    os.makedirs(outputdir)

logfile = open(outputdir+'/copy_dasfiles.log','w')

if nfiles != None:
    print(f"Downloading {nfiles} files into {outputdir}")

# for file in files[slice(nfiles)]:
#     fname = file.strip('/').replace('/','_')
#     cmd = f'xrdcp {redirector}{file} {outputdir}/{fname}'
#     if verbose: 
#         if file_downloaded(fname,outputdir): 
#             print(f'{fname} already present. Moving on the the next!')
#             continue
#         else:
#             print(f'Downloading {fname}')
#             process=subprocess.run(cmd, shell=True, 
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE )
#     else: 
#             process=subprocess.run(cmd, shell=True, 
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE )

if verbose:
    for file in files[slice(nfiles)]:
        fname = file.strip('/').replace('/','_')
        cmd = f'xrdcp {redirector}{file} {outputdir}/{fname}'
        if file_downloaded(fname,outputdir): 
            print(f'{fname} already present. Moving on the the next!')
            continue
        print(f'Downloading {fname}')
        process=subprocess.run(cmd, shell=True, 
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE )
        if process.stderr:
            # add datetime log here for when file listing fails
            logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} with file {file} : \n{process.stderr.decode()} \n')
            print(f"Check the {logfile.name} file")
        else: 
            logfile.write(process.stdout.decode())

else:
    for file in files[slice(nfiles)]:
        fname = file.strip('/').replace('/','_')
        cmd = f'xrdcp {redirector}{file} {outputdir}/{fname}'
        if file_downloaded(fname,outputdir): 
            continue
        process=subprocess.run(cmd, shell=True, 
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE )
        if process.stderr:
            # add datetime log here for when file listing fails
            logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} with file {file} : \n{process.stderr.decode()} \n')
        else: 
            logfile.write(process.stdout.decode())
            
logfile.close()