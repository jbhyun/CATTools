#!/bin/bash
#Author  : Jihwan Bhyun , 30. Jul. 2016
#Context : Run create batch for making catntuples
#Usage   : ./Runner <Step> <previous output>
#          eg. ./Runner CAT ${Process}_step3_filelist.txt

TrigStorage='xrootd' ##'xrootd' || 'scratch'

#tmp Val allocation
StepName='CAT'
CfgFile='PAT2CAT_cfg.py';
DestLoc='';
NmaxFile=50 #For PrivSample
#NmaxFile=1


##Main Code
if [[ -z $CMSSW_BASE ]]; then echo "cmsenv needed, exiting"; exit 1; fi
if [[ $( pwd ) != "${CMSSW_BASE}/src/CATTools/CatProducer/prod" ]]; then echo "Run at proper place, exiting"; exit 1; fi
if [[ ! -e DatasetListToRun.txt ]]; then echo "No datasetlist to run, exiting"; exit 1; fi
if [[ ! -e ${CfgFile} ]]; then echo "No script to run. exiting"; exit 1; fi

if [[ ${TrigStorage} == 'xrootd' ]]; then DestLoc='/store/user/jbhyun/CatBox';
elif [[ ${TrigStorage} == 'scratch' ]]; then DestLoc=$( pwd ); 
else echo "TrigStorage value is set wrong, exited"; exit 1; fi




while read SampleName
do
  FileList=FileListBox/dataset_${SampleName}_MiniAOD.txt
   
  echo "./create-batch --jobName ${SampleName}_${StepName} --cfg ${CfgFile} --maxFiles ${NmaxFile} --fileList ${FileList} --transferDest ${DestLoc}/${SampleName}_${StepName}"
        ./create-batch --jobName ${SampleName}_${StepName} --cfg ${CfgFile} --maxFiles ${NmaxFile} --fileList ${FileList} --transferDest ${DestLoc}/${SampleName}_${StepName}
  echo

done < DatasetListToRun.txt 
