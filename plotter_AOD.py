import ROOT
from DataFormats.FWLite import Events, Handle
ROOT.gROOT.SetStyle('Plain') # white background
#events = Events ('ZprimeToEE_M_5000_Tune4C_13TeV_pythia8_FULLSIM.root') #this is AOD

#files=['ZprimeToEE_M_3000_Tune4C_13TeV_pythia8_FULLSIM.root','ZprimeToEE_M_3000_width50_Tune4C_13TeV_pythia8_FULLSIM.root','ZprimeToEE_M_3000_width100_Tune4C_13TeV_pythia8_FULLSIM.root','ZprimeToEE_M_3000_width200_Tune4C_13TeV_pythia8_FULLSIM.root','ZprimeToEE_M_3000_width300_Tune4C_13TeV_pythia8_FULLSIM.root','ZprimeToEE_M_3000_width500_Tune4C_13TeV_pythia8_FULLSIM.root']
files=['ZprimeToEE_M_3000_width500_Tune4C_13TeV_pythia8_FULLSIM.root']

for file in files:
    events = Events (file) 
    handle  = Handle ("std::vector<reco::GenParticle>") #devi conoscere handle e label (con edmDumpEvent .root > dump.dat
    label = ("genParticles")
    # loop over events
    #Mass_hist = ROOT.TH1F ("Mass_hist", "Mass_hist", 100, 4000, 6000)
    Mass_hist = ROOT.TH1F ("Mass_hist", "Mass_hist", 100, 2000, 4000)
    for event in events:
        event.getByLabel (label, handle)
        electrons = handle.product()
        count_plus=0
        count_minus=0
        for electron in electrons:
            if electron.pdgId()== 11 and electron.mother(0).pdgId()==32:
                count_plus=count_plus + 1
                ele_plus=ROOT.TLorentzVector()
                ele_plus.SetPtEtaPhiE(electron.pt(),electron.eta(),electron.phi(),electron.energy())
            elif electron.pdgId()== -11 and electron.mother(0).pdgId()==32:
                ele_minus=ROOT.TLorentzVector()
                ele_minus.SetPtEtaPhiE(electron.pt(),electron.eta(),electron.phi(),electron.energy())
                count_minus=count_minus + 1
        #print count_plus, count_minus # Trova sempre 1 e+ e 1 e- con madre Zprime
        Zprime=ele_plus + ele_minus
        #print Zprime.M()
        Mass_hist.Fill(Zprime.M())
    # make a canvas, draw, and save it
    c1 = ROOT.TCanvas()
    Mass_hist.Draw()
    name=file.split(".root")
    c1.SaveAs(str("~/scratch1/www/Zprime/"+name[0]+".png"))
    
