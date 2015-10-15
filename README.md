## MC_production
Ho seguito un po' questa twiki

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro

https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideCMSDataAnalysisSchool2015GeneratorExerciseatBari

```
CMSSW_7_5_0_pre4
cmsrel CMSSW_7_5_0_pre4
cd CMSSW_7_5_0_pre4/src
cmsenv
```

Ti serve sicuramente un .py da lanciare con cmsDriver.py

esempio Configuration/GenProduction/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py

cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py --fileout file:RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_FULLSIM.root --mc --eventcontent AODSIM --datatier GEN-SIM --conditions auto:mc --beamspot Realistic8TeVCollision --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO --python_filename RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_FULLSIM_cfg.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 64

Se fai caso viene generato un altro .py e un .root. Volendo il .py puo' essere girato con cmsRun

Mo non so perche' FASTSIM non funziona, ma insomma non importa


**Questo in generale**, adesso supponiamo tu voglia generare Zprimo SSM con una certa width, come fai a scrivere il .py da dare in pasto a cmsDriver ?

La cosa piu' facile e':

https://github.com/cms-sw/genproductions/tree/master/python/ThirteenTeV

navighi un po' e ti trovi Zprimo. meglio ancora te lo cloni e vabbe

Al che poi per fare i plot
http://cmslxr.fnal.gov/lxr/search?v=CMSSW_7_6_X_2015-09-24-2300&_string=&_advanced=&_filestring=&_casesensitive=

Questi sono piu' belli
https://cmssdt.cern.ch/SDT/doxygen/CMSSW_7_4_9/doc/html/d0/d6d/classreco_1_1GsfElectron.html

Manuale di Pythia
http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html

In generale, i generatori NNLO non fanno il parton showering, ma producono dei file LHE con il diagramma partonico. Tale diagramma deve essere poi correttamente matchato con 
inital state radiation, final state radiation e parton showering.
Gli LHE Les Houches file (dal posto dove gli esperti di MC si incontrano e decidono gli standard), sono gli output di generatore da matchare con algoritmi di parton showering,
tipo ALPGEN di Mangano.

Pythia ha la particolarita' di poter essere stand-alone cioe' fa tutto lui, diagramma partonico e showering e quindi non produce gli LHE (e' quello che sto facendo in questo README) oppure puo' anche produrre solo gli LHE da dover poi matchare con lo showering (non e' il mio caso)