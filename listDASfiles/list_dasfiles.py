# IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal and then cd into the working directory.

import subprocess,os, argparse



# read arguments
parser = argparse.ArgumentParser(description='Make a list of files found on DAS')

parser.add_argument('--outputdir', default=os.path.abspath('.'),
                  help='Local directory where to put the copied file')


parser.add_argument("--outfile",type=str,
                    default='listfiles.txt',
                    help='The output text file with list of files from DAS.')

parser.add_argument("--datasets",type=str,
                    default='/eos/home-g/gfidalgo/SWAN_projects/dqm-playground-de-test-client/listDASfiles/list_datasets.txt',
                    help='A text file with list of datasets from DAS.')

parser.add_argument("-v",'--verbose',
		    action='store_true'
		    )

args = parser.parse_args()

outputdir = args.outputdir
outfile = args.outfile
datasets_file = args.datasets
verbose = args.verbose

file = open(datasets_file)
datasets= [line.strip() for line in file.readlines()]
file.close()
del file


if verbose :
    for i,dataset in enumerate(datasets):
        if i == 0:
            cmd = f'dasgoclient -query="file dataset={dataset}" > {outputdir}/{outfile}'
        else:
            cmd = f'dasgoclient -query="file dataset={dataset}" >> {outputdir}/{outfile}'
        
        print(cmd)
        subprocess.run(cmd, shell=True, check=False)
        
else:
    for i,dataset in enumerate(datasets):
        if i == 0:
            cmd = f'dasgoclient -query="file dataset={dataset}" > {outputdir}/{outfile}'
        else:
            cmd = f'dasgoclient -query="file dataset={dataset}" >> {outputdir}/{outfile}'

        subprocess.run(cmd, shell=True, check=False)

