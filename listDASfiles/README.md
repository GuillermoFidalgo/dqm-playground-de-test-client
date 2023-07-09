# Files from DAS

This folder contains scripts that are used to upload files to a specific area in`eos/project/m/mlplayground/public/DQMIO/`. Files can be found here or in  `eos/project/c/cmsml4dc/ML_2020/`.

## Scripts

- First we have `listdasfiles.py` this will run a series of DAS queries in order to make a list of files found by the queries and deposits this list into a text file.
- Second we have `copy_dasfiles.py` this will iterate through the contents of the generated text file and will run `xrdcp` on these files over to the user defined output. By default the files are copied to `./`. If the files are found to be already there (i.e. the same name is found) then it will continue on to upload the next file in the list.