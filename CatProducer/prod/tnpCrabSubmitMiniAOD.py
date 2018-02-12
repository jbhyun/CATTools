from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

mainOutputDir = '/store/user/jbhyun/CatBox/TrigStudy' 
config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'PAT2CAT_cfg.py'
#config.JobType.sendExternalFolder     = True

config.Data.inputDBS = 'global'
config.Data.publication = False
config.Data.allowNonValidInputDataset = False

config.Site.storageSite = 'T3_KR_KISTI'
config.Site.blacklist = ['T1_RU_JINR', 'T2_RU_JINR']


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_project'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'MC')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 1
    config.JobType.pyCfgParams  = ['useMiniAOD=True']
#
#    config.General.requestName  = 'DYJets_MG_10to50_TrigInfoSample'
#    config.Data.inputDataset    = '/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
#    submit(config)
#
    config.General.requestName  = 'DYJets_MG_TrigInfoSample_v3'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
    submit(config)
#
#    config.General.requestName  = 'TT_powheg_TrigInfoSample'
#    config.Data.inputDataset    = '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
#    submit(config)


#    sys.exit(0)

#    ##### now submit DATA
#    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'Data')
#    config.Data.splitting     = 'LumiBased'
#    config.Data.lumiMask      = 'Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
#    config.Data.unitsPerJob   = 50
#    config.JobType.pyCfgParams  = ['useMiniAOD=True','runOnMC=False']
# 
#    config.General.requestName  = 'SingleMuon_Run16B'
#    config.Data.inputDataset    = '/SingleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16C'
#    config.Data.inputDataset    = '/SingleMuon/Run2016C-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16D'
#    config.Data.inputDataset    = '/SingleMuon/Run2016D-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16E'
#    config.Data.inputDataset    = '/SingleMuon/Run2016E-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16F'
#    config.Data.inputDataset    = '/SingleMuon/Run2016F-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16G'
#    config.Data.inputDataset    = '/SingleMuon/Run2016G-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16Hv2'
#    config.Data.inputDataset    = '/SingleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleMuon_Run16Hv3'
#    config.Data.inputDataset    = '/SingleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD'
#    submit(config)

#    config.General.requestName  = 'SingleElectron_Run16B'
#    config.Data.inputDataset    = '/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16C'
#    config.Data.inputDataset    = '/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16D'
#    config.Data.inputDataset    = '/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16E'
#    config.Data.inputDataset    = '/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16F'
#    config.Data.inputDataset    = '/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16G'
#    config.Data.inputDataset    = '/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16Hv2'
#    config.Data.inputDataset    = '/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'SingleElectron_Run16Hv3'
#    config.Data.inputDataset    = '/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD'
#    submit(config)

#    config.General.requestName  = 'MuonEG_Run16B'
#    config.Data.inputDataset    = '/MuonEG/Run2016B-03Feb2017_ver2-v2/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16C'
#    config.Data.inputDataset    = '/MuonEG/Run2016C-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16D'
#    config.Data.inputDataset    = '/MuonEG/Run2016D-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16E'
#    config.Data.inputDataset    = '/MuonEG/Run2016E-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16F'
#    config.Data.inputDataset    = '/MuonEG/Run2016F-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16G'
#    config.Data.inputDataset    = '/MuonEG/Run2016G-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16Hv2'
#    config.Data.inputDataset    = '/MuonEG/Run2016H-03Feb2017_ver2-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'MuonEG_Run16Hv3'
#    config.Data.inputDataset    = '/MuonEG/Run2016H-03Feb2017_ver3-v1/MINIAOD'
#    submit(config)

#    config.General.requestName  = 'DoubleMuon_Run16B'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016B-03Feb2017_ver2-v2/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16C'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16D'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016D-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16E'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016E-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16F'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016F-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16G'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016G-03Feb2017-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16Hv2'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016H-03Feb2017_ver2-v1/MINIAOD'
#    submit(config)
#    config.General.requestName  = 'DoubleMuon_Run16Hv3'
#    config.Data.inputDataset    = '/DoubleMuon/Run2016H-03Feb2017_ver3-v1/MINIAOD'
#    submit(config)
