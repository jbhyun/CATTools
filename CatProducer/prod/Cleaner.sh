#!/bin/bash

if [[ -z $CMSSW_BASE ]]; then echo "cmsenv needed, exiting"; exit 1; fi
if [[ $( pwd ) != "${CMSSW_BASE}/src/CATTools/CatProducer/prod" ]]; then echo "Run at proper place, exiting"; exit 1; fi
if [[ ! -e DatasetListToRun.txt ]]; then echo "No datasetlist to run, exiting"; exit 1; fi
if [[ ! -d CATBox ]]; then echo "Made CATBox"; mkdir CATBox; fi

Nexist=0

while read line 
do
  if [[ -d CATBox/${line}_CAT ]]; then 
    echo "CATBox/${line}_CAT exist"
    let Nexist++
  fi
done < DatasetListToRun.txt

if [[ ${Nexist} -gt 0 ]]; then
  echo "There are already existing Dirs with same name. override? (y/n)"
  read answer
  if [[ ${answer} == 'n' ]]; then echo "Okay, quit."; exit 1;
  elif [[ ${answer} != 'y' ]]; then echo "Wrong answer, quit"; exit 1;
  else echo "Will override"
  fi
fi

while read line
do
  if [[ ! -d CATBox/${line}_CAT ]];then mkdir CATBox/${line}_CAT; fi
  mv ${line}_CAT/*root CATBox/${line}_CAT
  rm -r ${line}_CAT
done < DatasetListToRun.txt
