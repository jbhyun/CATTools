#!/bin/bash
# Author: Jihwan Bhyun, 15. Feb. 2017
# DatasetListToRun's 1st column should be dataset name

if [[ ! -e DatasetListToRun.txt ]]; then echo "DatasetList not exist, exiting"; exit 1; fi
if [[ ! -d FileListBox ]]; then mkdir FileListBox; echo "Made FileListBox"; fi

NSample=$( wc -l DatasetListToRun.txt | cut -d ' ' -f1 )

for (( i=1; i<${NSample}+1; i++ ))
do
  Process=$( sed "${i}q;d" DatasetListToRun.txt | cut -d ' ' -f1 )

  FileListName=dataset_${Process}_MiniAOD.txt
  if [[ -e FileListBox/${FileListName} ]]; then echo "FileListBox/${FileListName} exists, skipped"; continue; fi;
  if [[ ! -d "/xrootd/store/user/jbhyun/${Process}" ]];
  then 
    if [[ -e MissingList.txt ]]; then touch MissingList.txt; fi
    echo "${Process}" >> MissingList.txt
    echo "/xrootd/store/user/jbhyun/${Process} does not exist, skipped"; continue;
  fi
  touch FileListBox/${FileListName}
  find /xrootd/store/user/jbhyun/${Process}/ -name "*root" >> FileListBox/${FileListName}

  sed -i "s/^\/xrootd//g" FileListBox/${FileListName}

  echo "Produced FileListBox/${FileListName}"
done
