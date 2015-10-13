## MC_production

```
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py --fileout file:RSGravitonToZZ_kMpl01_M_1000_TuneCUET\
P8M1_13TeV_pythia8_FULLSIM.root --mc --eventcontent AODSIM --datatier GEN-SIM --conditions auto:mc --beamspot Realistic8TeVCollision --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun,R\
AW2DIGI,L1Reco,RECO --python_filename RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_FULLSIM_cfg.py --customise Configuration/DataProcessing/Utils.addMonitoring -n 64
```
