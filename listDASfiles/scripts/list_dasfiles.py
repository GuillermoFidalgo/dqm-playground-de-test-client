# IMPORTANT This file does not run form inside SWAN env. Only run this on a terminal and then cd into the working directory.

import subprocess,os, argparse,datetime




# read arguments
parser = argparse.ArgumentParser(description='Make a list of files found on DAS')

parser.add_argument('--outdir', default=os.path.abspath('.'),required=True,
                  help='Local directory where to put the copied file')


parser.add_argument("--outfile",type=str,
                    default='listfiles.txt',required=True,
                    help='The output text file with list of files from DAS.')

parser.add_argument("--datasets",type=str,required=True,
                    help='A text file with list of datasets from DAS.')

parser.add_argument("-v",'--verbose',action='store_true')




args = parser.parse_args()

outputdir = args.outdir.rstrip('/')
outfile = args.outfile
datasets_file = args.datasets
verbose = args.verbose

file = open(datasets_file)
text = file.read().splitlines()

# datasets= [line.strip() for line in file.readlines()]
datasets=[i.rsplit()[0] for i in text ]
file.close()




if os.path.exists(outputdir):
    print(f'Directory {outputdir} already exists.\nWriting to {outputdir}')
else:
    print(f'Creating {outputdir}')
    os.makedirs(outputdir)

logfile = open(outputdir+'/list_dasfiles.log','w')

if verbose :
    for i,dataset in enumerate(datasets):
        if i == 0:
            cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query="file dataset={dataset}" > {outputdir}/{outfile}'
        else:
            cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query="file dataset={dataset}" >> {outputdir}/{outfile}'
        
        print(cmd)
        process = subprocess.run(cmd, shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE  
                                )
        if process.stderr:
            # add datetime log here for when file listing fails
            logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} :\n{process.stderr.decode()}')
            print("Check the list_dasfiles.log file")
        else: 
            logfile.write(process.stdout.decode())
            
else:
    for i,dataset in enumerate(datasets):
        if i == 0:
            cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query="file dataset={dataset}" > {outputdir}/{outfile}'
        else:
            cmd = f'/cvmfs/cms.cern.ch/common/dasgoclient -query="file dataset={dataset}" >> {outputdir}/{outfile}'

        process = subprocess.run(cmd, shell=True,  
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE  
                                )
        if process.stderr:
            # add datetime log here for when file listing fails
            logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} :\n{process.stderr.decode()}')
            print("Check the list_dasfiles.log file")

        else: 
            logfile.write(process.stdout.decode())
        
        
logfile.close()
