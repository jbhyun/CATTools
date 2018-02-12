#!/bin/bash
#Author  : Jihwan Bhyun , 30. Jul. 2016
#Context : Run create batch for making catntuples
#Usage   : ./Runner <Step> <previous output>
#          eg. ./Runner CAT ${Process}_step3_filelist.txt

TrigStorage='xrootd' ##'xrootd' || 'scratch'


#tmp Val allocation
StepName='flatcat'
CfgFile='run_ntupleMaker_snu_data_fulltrig_cfg.py';
DestLoc='';
NmaxFile=5 #For PrivSample
#NmaxFile=1


##Main Code
if [[ -z $CMSSW_BASE ]]; then echo "cmsenv needed, exiting"; exit 1; fi
if [[ $( pwd ) != "${CMSSW_BASE}/src/CATTools/CatAnalyzer/SNUsubmission/snu" ]]; then echo "Run at proper place, exiting"; exit 1; fi
if [[ ! -e DatasetListToRun.txt ]]; then echo "No datasetlist to run, exiting"; exit 1; fi
if [[ ! -e ${CfgFile} ]]; then echo "No script to run. exiting"; exit 1; fi

if [[ ${TrigStorage} == 'xrootd' ]]; then DestLoc='/store/user/jbhyun/flatcat/Debug';
elif [[ ${TrigStorage} == 'scratch' ]]; then DestLoc=$( pwd ); 
else echo "TrigStorage value is set wrong, exited"; exit 1; fi




while read SampleName
do
  FileList=FileListBox/dataset_${SampleName}.txt
   
  echo "./create-batch --jobName SNU_v8-0-7_${SampleName} --cfg ${CfgFile} --maxFiles ${NmaxFile} --fileList ${FileList} --transferDest ${DestLoc}/SNU_v8-0-7_${SampleName}"
  ./create-batch --jobName SNU_v8-0-7_${SampleName} --cfg ${CfgFile} --maxFiles ${NmaxFile} --fileList ${FileList} --transferDest ${DestLoc}/SNU_v8-0-7_${SampleName}
  echo

done < DatasetListToRun.txt 
