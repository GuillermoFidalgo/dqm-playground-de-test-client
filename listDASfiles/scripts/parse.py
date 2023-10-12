import os, subprocess,argparse,sys
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import requests
import datetime

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

parser.add_argument("--data_dimensionality",
                    type=int,
                    default=1,
                    choices=[1,2],
                    help='Indicate dimensionality of histograms in file to be parsed [ 1 | 2 ]')

parser.add_argument('--file_format',type=str,
                    choices=['csv','root'],
                    default='root',
                    help='Type of file to be parsed [ csv | root ]')


args = parser.parse_args()
now = datetime.datetime.now().strftime("%a_%d_%b_%Y_%H_%M")
logfile = open(f'parse_{now}.log','a')

for file in args.files :

    result = api_instance.list_histogram_data_files(filepath__contains=f'{file}').results
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
    else: 
        print(f"Parsing started for file {file}\nfile id is {file_id}",file=logfile)