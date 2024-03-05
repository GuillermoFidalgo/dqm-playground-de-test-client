import os, subprocess,argparse,sys
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests
import datetime
import time

# Configure and create an API client
# using an API token
# API_TOKEN = "000b74d58339656029f052a32d6f9e11fae8321f"
# MLP_URL = "https://ml4dqm-playground.web.cern.ch"

# DEVLOP_API_TOKEN= "871450223ff7d809acdf6ffe8d11ef4a18a724c6"
DEVELOP_API_TOKEN = "5ebc661c6358fb9b1ad4cb064f98d86a1910240e"
MLP_DEVELOP_URL = "https://ml4dqm-playground-develop.web.cern.ch"

configuration = swagger_client.Configuration()
configuration.host = MLP_DEVELOP_URL
client = swagger_client.ApiClient(configuration)
client.set_default_header(header_name="Content-Type", header_value="application/json")
client.set_default_header(header_name="Authorization", header_value=f"Token {DEVELOP_API_TOKEN}")

api_instance = swagger_client.ApiApi(client)


# read arguments
parser = argparse.ArgumentParser(description='Activate parsing of newly discovered files')

parser.add_argument('files',type=str,
                    nargs="+",
                    help='Input files')

parser.add_argument('--granularity', default='lum',
                     type=str,
                    choices=['lum','run'],
                    help='Granularity of the file [lumisection | run]')

parser.add_argument('-d',"--data_dimensionality",
                    type=int,
                    default=1,
                    choices=[1,2],
                    help='Indicate dimensionality of histograms in file to be parsed [ 1 | 2 ]')

parser.add_argument('--file_format',type=str,
                    choices=['csv','root'],
                    default='root',
                    help='Type of file to be parsed [ csv | root ]')

parser.add_argument('--logpath',type=str,required=True,
                    help='Where to dump the logfile. This is required.')
parser.add_argument("-v",'--verbose',action="store_true",
                    help="Prints to screen")


args = parser.parse_args()
now = datetime.datetime.now().strftime("%a_%d_%b_%Y_%H_%M")
logpath = args.logpath.rstrip('/')
logfile = open(f'{logpath}/parse_{args.granularity}_{args.data_dimensionality}_{args.file_format}_{now}.log','a')


for i,file in enumerate(args.files) :
    start = time.time()
        
    result = api_instance.list_histogram_data_files(filepath__contains=f'{file.rpartition("_")[-1]}').results 
    # the rpartition allows for use of softlinks to the eos area by just looking 
    # at the filename and not the full path in the DB.
    
    if not result:
        print("No results found")
        sys.exit()
    assert (len(result) ==1) & (type(result) == list)
    file_id = result[0].id 
    r = requests.post(
        f"{MLP_DEVELOP_URL}/api/histogram_data_files/{file_id}/start_parsing/",
        headers={"Content-Type": "application/json", "Authorization": f"Token {DEVELOP_API_TOKEN}"},
        json={'granularity':args.granularity, 'data_dimensionality':args.data_dimensionality, 'file_format':args.file_format}
    )
    
    if not r.ok:
        print(f"Parsing request not ok with file {file}",file =logfile)
        if args.verbose:
            print(f"Parsing request not ok with file {file}")
    else: 
        print(f"Parsing started for file {file}\nfile id is {file_id}",file=logfile)
        if args.verbose:
            print(f"Parsing started for file {file}\nfile id is {file_id}")
            
    end = time.time()
    delta = end-start
    if delta > 5 : 
        print("\nWaiting 10 min\n",file=logfile)
        if args.verbose:
            print("\nWaiting 10 min\n")
        time.sleep(60*10)
    elif delta > 2:
        print("Waiting a minute",file=logfile)
        time.sleep(60) # Wait a minute before trying to submit next file
