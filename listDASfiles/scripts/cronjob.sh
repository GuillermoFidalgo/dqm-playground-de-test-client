#### export X509_USER_PROXY = /tmp/x509up_u111865
export X509_USER_KEY=/afs/cern.ch/user/g/gfidalgo/.globus/userkey.pem
export X509_USER_CERT=/afs/cern.ch/user/g/gfidalgo/.globus/usercert.pem
voms-proxy-init -voms cms -rfc

workpath=/eos/user/g/gfidalgo/SWAN_projects/dqm-playground-de-test-client/listDASfiles
eospath=/eos/project/m/mlplayground/public/DQMIO/nanodqmio_from_das
now=$(date +%a_%d_%b_%Y_%H_%M)
logfile=$eospath/cronoutput/cron_$now.log


# activating venv to enable script and have packages available
source $workpath/../venv/bin/activate 


############### Trigger creation of list of files to be copied #####################

echo "Creating List of files from desired datasets" &> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile

python3 $workpath/scripts/list_dasfiles.py \
--outdir=$eospath \
--datasets=$workpath/cronoutput/datasets.txt \
--outfile=files_$now.txt -v \
&>> $logfile


### Copy the files

echo "Initializing copying of files from desired datasets" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile

python3 $workpath/scripts/copy_dasfiles.py \
--outdir=$eospath \
--listfiles=$eospath/files_$now.txt -v \
&>> $logfile


### Discovery files

echo "Initializing file discovery" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile
python3 $workpath/scripts/discover.py 


### Parse files
echo "Initializing file parsing" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile
echo "Parsing 1D histograms in files" &>> $logfile

python3 $workpath/scripts/parse.py \
$eospath/*.root \
-d 1 \
--granularity lum \
--file_format root \
--logpath $eospath/cronoutput/ -v &>> $logfile

echo "Parsing 2D histograms in files" &>> $logfile

python3 $workpath/scripts/parse.py \
$eospath/*.root \
-d 2 \
--granularity lum \
--file_format root \
--logpath $eospath/cronoutput/ -v &>> $logfile

echo "======================= Cron Job is done! ========================" &>> $logfile





####################### Same process but for HI files ###########################
workpath=/eos/user/g/gfidalgo/SWAN_projects/dqm-playground-de-test-client/listDASfiles
eospath=/eos/project/m/mlplayground/public/DQMIO/nanodqmio_from_das/HI
now=$(date +%a_%d_%b_%Y_%H_%M)
logfile=$eospath/cronoutput/HIcron_$now.log


echo "Creating List of files from desired datasets" &> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile

python3 $workpath/scripts/list_dasfiles.py \
--outdir=$eospath \
--datasets=$workpath/cronoutput/HI_datasets.txt \
--outfile=HI_files_$now.txt -v \
&>> $logfile


### Copy the files

echo "Initializing copying of files from desired datasets" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile

python3 $workpath/scripts/copy_dasfiles.py \
--outdir=$eospath \
--listfiles=$eospath/HI_files_$now.txt -v \
&>> $logfile


### Discovery files

echo "Initializing file discovery" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile
python3 $workpath/scripts/discover.py 



### Parse files

echo "Initializing file parsing" &>> $logfile
echo $(date) &>> $logfile
echo "====================================================================" &>> $logfile
echo "Parsing 1D histograms in files" &>> $logfile

python3 $workpath/scripts/parse.py \
$eospath/*.root \
-d 1 \
--granularity lum \
--file_format root \
--logpath $eospath/cronoutput/ -v &>> $logfile

echo "Parsing 2D histograms in files" &>> $logfile

python3 $workpath/scripts/parse.py \
$eospath/*.root \
-d 2 \
--granularity lum \
--file_format root \
--logpath $eospath/cronoutput/ -v &>> $logfile


echo "======================= Cron Job is done! ========================" &>> $logfile

