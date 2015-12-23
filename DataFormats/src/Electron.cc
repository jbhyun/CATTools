#include "CATTools/DataFormats/interface/Electron.h"

using namespace cat;

/// default constructor
Electron::Electron() {
}

Electron::Electron(const reco::LeafCandidate & aElectron) : Lepton( aElectron ) {
}

/// destructor
Electron::~Electron() {
}

float Electron::electronID(const std::string& name) const {
  for (std::vector<pat::Electron::IdPair>::const_iterator it = electronIDs_.begin(), ed = electronIDs_.end(); it != ed; ++it) {
    if (it->first.find(name) != std::string::npos)
      return it->second;
  }
  cms::Exception ex("Key not found");
  ex << "cat::Electron: the ID " << name << " can't be found in this cat::Electron.\n";
  ex << "The available IDs are: ";
  for (std::vector<pat::Electron::IdPair>::const_iterator it = electronIDs_.begin(), ed = electronIDs_.end(); it != ed; ++it) {
    ex << "'" << it->first << "' ";
  }
  ex << ".\n";
  throw ex;
}

float Electron::scaleFactor(const std::string& name) const {
  if (name == "mvaEleID-Spring15-25ns-Trig-V1-wp90"){
    if (this->pt()>15. && this->pt() <= 25.){
      if      ( this->eta()>-2.5 && this->eta() <= -1.5) return 0.96;
      else if ( this->eta()>-1.5 && this->eta() <= -1.0) return 0.95;
      else if ( this->eta()>-1.0 && this->eta() <= 0 ) return 0.98;
      else if ( this->eta()>0 && this->eta() <= 1.0) return 0.99;
      else if ( this->eta()>1.0 && this->eta() <= 1.5) return 0.99;
      else if ( this->eta()>1.5 && this->eta() <= 2.5) return 0.97;
      else return 1.;
    }
    else if (this->pt()>25. && this->pt() <= 35.){
      if      ( this->eta()>-2.5 && this->eta() <= -1.5) return 0.98;
      else if ( this->eta()>-1.5 && this->eta() <= -1.0) return 0.97;
      else if ( this->eta()>-1.0 && this->eta() <= 0 ) return 0.97;
      else if ( this->eta()>0 && this->eta() <= 1.0) return 0.99;
      else if ( this->eta()>1.0 && this->eta() <= 1.5) return 0.99;
      else if ( this->eta()>1.5 && this->eta() <= 2.5) return 0.98;
      else return 1.;
    }
    else if (this->pt()>35. && this->pt() <= 45.){ 
      if      ( this->eta()>-2.5 && this->eta() <= -1.5) return 0.98;
      else if ( this->eta()>-1.5 && this->eta() <= -1.0) return 0.99;
      else if ( this->eta()>-1.0 && this->eta() <= 0 ) return 0.99;
      else if ( this->eta()>0 && this->eta() <= 1.0) return 0.99;
      else if ( this->eta()>1.0 && this->eta() <= 1.5) return 0.99;
      else if ( this->eta()>1.5 && this->eta() <= 2.5) return 0.98;
      else return 1.;
    }
    else if (this->pt()>45. && this->pt() <= 55.){
      if      ( this->eta()>-2.5 && this->eta() <= -1.5) return 0.98;
      else if ( this->eta()>-1.5 && this->eta() <= -1.0) return 0.99;
      else if ( this->eta()>-1.0 && this->eta() <= 0 ) return 0.99;
      else if ( this->eta()>0. && this->eta() <= 1.0) return 0.99;
      else if ( this->eta()>1.0 && this->eta() <= 1.5) return 0.99;
      else if ( this->eta()>1.5 && this->eta() <= 2.5) return 0.99;
      else return 1.;
    }
    else if (this->pt()>55.){
      if      ( this->eta()>-2.5 && this->eta() <= -1.5) return 0.99;
      else if ( this->eta()>-1.5 && this->eta() <= -1.0) return 0.99;
      else if ( this->eta()>-1.0 && this->eta() <= 0 ) return 0.99;
      else if ( this->eta()>0 && this->eta() <= 1.0) return 1.00;
      else if ( this->eta()>1.0 && this->eta() <= 1.5) return 0.99;
      else if ( this->eta()>1.5 && this->eta() <= 2.5) return 0.99;
      else return 1.;
    }
  }
  return 1.;
}
