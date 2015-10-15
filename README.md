## MC_production
```
CMSSW_7_5_0_pre4
cmsrel CMSSW_7_5_0_pre4
cd CMSSW_7_5_0_pre4/src
cmsenv
```

La chiave e' tutta nella configuration card, per il quale devi conoscere il CMSSW configuration language

https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookConfigFileIntro




cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py --fileout file:RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_FULLSIM.root --mc --eventcontent AODSIM --datatier GEN-SIM --conditions auto:mc --beamspot Realistic8TeVCollision --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,RAW2DIGI,L1Reco,RECO --python_filename RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_FULLSIM_cfg.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 64


Mo non so perche' FASTSIM non funziona, ma insomma non importa

cmsDriver crea un .py  (--fileout) che volendo puoi girare con cmsRun

Ah ho capito: ci sono 2 FILE, il secondo dei quali viene creato nella cartella work e che fa gli import

il secondo file .py  viene chiamato "configuration file"

https://github.com/cms-sw/genproductions/tree/master/python/ThirteenTeV

navighi un po' e ti trovi Zprimo. meglio ancora te lo cloni e vabbe


Al che poi per fare i plot
http://cmslxr.fnal.gov/lxr/search?v=CMSSW_7_6_X_2015-09-24-2300&_string=&_advanced=&_filestring=&_casesensitive=

Questi sono piu' belli
https://cmssdt.cern.ch/SDT/doxygen/CMSSW_7_4_9/doc/html/d0/d6d/classreco_1_1GsfElectron.html

Manuale di Pythia
http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html