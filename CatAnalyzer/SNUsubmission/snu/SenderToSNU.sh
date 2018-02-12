#!/bin/bash

#declare -a StreamList=('DoubleMuon' 'SingleMuon' 'MuonEG' 'SingleElectron')
#declare -a StreamList=('MuonEG' 'SingleElectron')
#declare -a PeriodList=('B' 'C' 'D' 'E' 'F' 'G' 'H_v2' 'H_v3')
declare -a StreamList=('SingleElectron')
declare -a PeriodList=('C')

#FilePathBase_Kisti="/xrootd/store/user/jbhyun/flatcat/TrigSkim"
FilePathBase_Kisti="/xrootd/store/user/jbhyun/flatcat/Debug"
FilePathBase_SNU="/data7/DATA/FlatCat_jh/Data/v8-0-7_TrigInfoSample"
DestIP="147.47.242.42"
catver="v8-0-7"
for Stream in "${StreamList[@]}"
do
  for Period in "${PeriodList[@]}"
  do
    echo "ssh jbhyun@147.47.242.42" "mkdir -p ${FilePathBase_SNU}/${Stream}/period${Period}"
    ssh jbhyun@${DestIP} "mkdir -p ${FilePathBase_SNU}/${Stream}/period${Period}"
    scp -r ${FilePathBase_Kisti}/SNU_${catver}_${Stream}_Run2016${Period}/*root jbhyun@${DestIP}:${FilePathBase_SNU}/${Stream}/period${Period}/
  done
done
