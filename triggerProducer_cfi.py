import FWCore.ParameterSet.Config as cms

catTrigger = cms.EDProducer("CATTriggerProducer",
    trigger = cms.PSet(
        triggerResults = cms.VInputTag(
#            cms.InputTag("TriggerResults","","HLT2"),# due to reHLT, this is the first choice
            cms.InputTag("TriggerResults","","HLT"),# if above is not found, falls to default
        ),
        objects = cms.InputTag("selectedPatTrigger"),
        prescales = cms.InputTag("patTrigger"),
        prefix = cms.vstring(
            #"HLT_Ele", "HLT_DoubleEle",
            #"HLT_Mu", "HLT_TkMu", "HLT_IsoMu", "HLT_IsoTkMu",
            #"HLT_DiMu", "HLT_DoubleIsoMu",
            #"HLT_TripleMu",
            #"HLT_PFJet",
            #"HLT_DoublePhoton", "HLT_Photon"
            #"HLT_PFMET",
            "HLT_IsoMu24_v"                                   , "HLT_IsoTkMu24_v",
            "HLT_Ele27_WPTight_Gsf_v"                         , "HLT_Ele27_eta2p1_WPTight_Gsf_v",
            "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v"              , "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
            "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v"            , "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v",
            "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v",
            "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v", "HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v",
        ),
    ),
    flags = cms.PSet(
        triggerResults = cms.VInputTag(
            cms.InputTag("TriggerResults","","RECO"),
            cms.InputTag("TriggerResults","","PAT"),
        ),
        names = cms.vstring(
            "Flag_goodVertices",
            "Flag_globalTightHalo2016Filter",
            "Flag_HBHENoiseFilter",
            "Flag_HBHENoiseIsoFilter",
            "Flag_EcalDeadCellTriggerPrimitiveFilter",
            "Flag_eeBadScFilter",
            "Flag_badMuons", "Flag_duplicateMuons", "Flag_noBadMuons",
        ),
        bools = cms.VInputTag(
            cms.InputTag("BadChargedCandidateFilter"),
            cms.InputTag("BadPFMuonFilter"),
            cms.InputTag("badECALSlewRateMitigationFilter2016"),
        ),
    ),
)
