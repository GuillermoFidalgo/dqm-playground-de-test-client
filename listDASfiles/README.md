# Files from DAS

This folder contains scripts that are used to upload files to a specific area in`eos/project/m/mlplayground/public/DQMIO/`. Files can be found here or in  `eos/project/c/cmsml4dc/ML_2020/`.

## Scripts

- First we have `listdasfiles.py` this will run a series of DAS queries in order to make a list of files found by the queries and deposits this list into a text file. This file requires that there is a `datasets.txt` somewhere. I call this *list_datasets.txt* in my case.

To create this file please run the following command or any other command that will result in your required datasets 

```shell
dasgoclient -query="dataset=/ZeroBias/Run2022*/DQMIO" | grep -v "Prompt" | grep -v "pilot" > list_datasets.txt 

dasgoclient -query="dataset=/ZeroBias/Run2023*/DQMIO" >> list_datasets.txt
```
This command will take as inputs the following arguments (optional)
```shell
  --outputdir OUTPUTDIR
                        Local directory where to put the copied file
  --outfile OUTFILE     The output text file with list of files from DAS.
  --datasets DATASETS   A text file with list of datasets from DAS.
```

- Second we have `copy_dasfiles.py` this will iterate through the contents of the generated text file and will run `xrdcp` on these files over to the user defined output. By default the files are copied to `./`. If the files are found to be already there (i.e. the same name is found) then it will continue on to upload the next file in the list.

This commands takes the follwing arguments

```shell
  --redirector REDIRECTOR
                        Redirector to read remote files
  --outputdir OUTPUTDIR
                        Local directory where to put the copied file
  --nfiles NFILES       Limit the number of files to copy. (Default: all files from the listfiles.txt will be downloaded)
  --listfiles LISTFILES
                        A text file with list of paths from DAS.
  -v, --verbose         Prints to screen what files are already found in the outputdir
```