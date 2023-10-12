import os, subprocess,argparse,sys
import datetime


# read arguments
parser = argparse.ArgumentParser(description='Get information from either a list of datasets or info from the files retrieved from a DAS query')

parser.add_argument('input_file',type=argparse.FileType('r'),
                    help='Input text file that contains a list')

parser.add_argument("-o",'--outfile',
                    default = sys.stdout,
                    help='The file to dump with desired info. If the file exists it will overwrite the contents. If not specified, print to stdout')

parser.add_argument('-t',"--type",type=str,required=True,
                    default='file',choices=['file','dataset'],
                    help='Indicate what the input file is listing [root files| datasets]')




args = parser.parse_args()

infile = args.input_file
outfile = args.outfile
file_type = args.type

if outfile != sys.stdout:
    outputfile = open(outfile,'w')
    
if file_type == 'dataset':
    datasets= [line.strip() for line in infile.readlines()]
    scriptlines=[]
    
    for i,dataset in enumerate(datasets):

        cmd = f'echo {dataset} - $(dasgoclient -query="release dataset={dataset}")' 
        scriptlines.append(cmd+'\n')        
        
    script = open('make_dataset_with_release.sh','w')
    script.writelines(scriptlines)
    script.close()
    process=subprocess.run('bash '+script.name, shell=True,
                           stdout=subprocess.PIPE if outfile != sys.stdout else None,
                          stderr=subprocess.PIPE )
    if process.stderr:
        logfile = open("info.log",'w')
        # add datetime log here for when file listing fails
        logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} :\n{process.stderr.decode()}')
        print("Check the info.log file")
        logfile.close()

    if outfile != sys.stdout : 
        outputfile.write(process.stdout.decode())
        outputfile.close()
    os.remove(script.name)




# Add section what to do with list of root files is given to the script
# Script should return a das query that enumerates file - run number


if file_type == 'file':
    rootfiles= [line.strip() for line in infile.readlines()]
    scriptlines=[]
    
    for i,rootfile in enumerate(rootfiles):

        cmd = f'echo {rootfile} - $(dasgoclient -query="run file={rootfile}")' 
        scriptlines.append(cmd+'\n')        

    script = open('make_rootfiles_with_runs.sh','w')
    script.writelines(scriptlines)
    script.close()
    process=subprocess.run('bash '+script.name, shell=True,
                           stdout=subprocess.PIPE if outfile != sys.stdout else None,
                          stderr=subprocess.PIPE )
    if process.stderr:
        logfile = open("info.log",'w')
        # add datetime log here for when file listing fails
        logfile.write(f'Error at {datetime.datetime.now().strftime("%c")} :\n{process.stderr.decode()}')
        print("Check the info.log file")
        logfile.close()
        
    if outfile != sys.stdout : 
        outputfile.write(process.stdout.decode())
        outputfile.close()

    os.remove(script.name)