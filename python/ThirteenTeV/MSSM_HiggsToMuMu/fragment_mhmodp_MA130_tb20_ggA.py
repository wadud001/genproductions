COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2A3 = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     2.00000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.51000000E+03   # At
        12     1.51000000E+03   # Ab
        13     1.51000000E+03   # Atau
        23     2.00000000E+02   # MUE
        25     2.00000000E+01   # TB
        26     1.30000000E+02   # MA0
        27     1.52852342E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95845890E+02   # MSf(1,1,1)
   1000011     5.02289514E+02   # MSf(1,2,1)
   2000011     5.01838716E+02   # MSf(2,2,1)
   1000002     1.49903009E+03   # MSf(1,3,1)
   2000002     1.49959059E+03   # MSf(2,3,1)
   1000001     1.50117388E+03   # MSf(1,4,1)
   2000001     1.50020460E+03   # MSf(2,4,1)
   1000014     4.95845890E+02   # MSf(1,1,2)
   1000013     5.02541395E+02   # MSf(1,2,2)
   2000013     5.01586505E+02   # MSf(2,2,2)
   1000004     1.49903061E+03   # MSf(1,3,2)
   2000004     1.49959117E+03   # MSf(2,3,2)
   1000003     1.50118944E+03   # MSf(1,4,2)
   2000003     1.50018903E+03   # MSf(2,4,2)
   1000016     9.97929430E+02   # MSf(1,1,3)
   1000015     9.98819801E+02   # MSf(1,2,3)
   2000015     1.00324582E+03   # MSf(2,2,3)
   1000006     8.76429378E+02   # MSf(1,3,3)
   2000006     1.13478243E+03   # MSf(2,3,3)
   1000005     9.96111023E+02   # MSf(1,4,3)
   2000005     1.00594745E+03   # MSf(2,4,3)
        25     1.21634331E+02   # Mh0
        35     1.33478471E+02   # MHH
        36     1.30000000E+02   # MA0
        37     1.54196995E+02   # MHp
   1000022     8.78206612E+01   # MNeu(1)
   1000023     1.51359250E+02   # MNeu(2)
   1000025    -2.10117348E+02   # MNeu(3)
   1000035     2.66409088E+02   # MNeu(4)
   1000024     1.47528170E+02   # MCha(1)
   1000037     2.66764158E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     5.90518816E-01   # Delta Mh0
        35     1.20850755E-01   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     2.51765454E-02   # Delta MHp
BLOCK NMIX
     1   1     9.30213894E-01   # ZNeu(1,1)
     1   2    -1.18546783E-01   # ZNeu(1,2)
     1   3     3.13311260E-01   # ZNeu(1,3)
     1   4    -1.49949409E-01   # ZNeu(1,4)
     2   1    -3.23202104E-01   # ZNeu(2,1)
     2   2    -6.93891430E-01   # ZNeu(2,2)
     2   3     5.08023191E-01   # ZNeu(2,3)
     2   4    -3.94927234E-01   # ZNeu(2,4)
     3   1     9.59510181E-02   # ZNeu(3,1)
     3   2    -1.33592266E-01   # ZNeu(3,2)
     3   3    -6.78206777E-01   # ZNeu(3,3)
     3   4    -7.16227671E-01   # ZNeu(3,4)
     4   1    -1.45037624E-01   # ZNeu(4,1)
     4   2     6.97577558E-01   # ZNeu(4,2)
     4   3     4.28700431E-01   # ZNeu(4,3)
     4   4    -5.55486794E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.08113363E-01   # UCha(1,1)
     1   2     7.93850198E-01   # UCha(1,2)
     2   1     7.93850198E-01   # UCha(2,1)
     2   2     6.08113363E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.93850198E-01   # VCha(1,1)
     1   2     6.08113363E-01   # VCha(1,2)
     2   1     6.08113363E-01   # VCha(2,1)
     2   2     7.93850198E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     6.88810103E-01   # USf(1,1)
     1   2     7.24941820E-01   # USf(1,2)
     2   1     7.24941820E-01   # USf(2,1)
     2   2    -6.88810103E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08249465E-01   # USf(1,1)
     1   2    -7.05962248E-01   # USf(1,2)
     2   1     7.05962248E-01   # USf(2,1)
     2   2     7.08249465E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.52799510E-01   # USf(1,1)
     1   2     7.57530726E-01   # USf(1,2)
     2   1     7.57530726E-01   # USf(2,1)
     2   2    -6.52799510E-01   # USf(2,2)
BLOCK ALPHA
              -5.72410305E-01   # Alpha
BLOCK DALPHA
               7.25065677E-02   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     2.00000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51000000E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51000000E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.51000000E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     5.87736714E-05   # Yf(1,1)
     2   2     1.21525301E-02   # Yf(2,2)
     3   3     2.04389044E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72525825E-05   # Yf(1,1)
     2   2     7.39560703E-03   # Yf(2,2)
     3   3     9.96049095E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     6.76269414E-04   # Yf(1,1)
     2   2     1.07071436E-02   # Yf(2,2)
     3   3     4.49839737E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     3.08627457E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.50403413E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     6.79258003E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99989805E-01   # UASf(1,1)
     1   4    -4.51557869E-03   # UASf(1,4)
     2   2     8.57926156E-01   # UASf(2,2)
     2   5    -5.13773015E-01   # UASf(2,5)
     3   3     6.88810103E-01   # UASf(3,3)
     3   6     7.24941820E-01   # UASf(3,6)
     4   1     4.51557869E-03   # UASf(4,1)
     4   4     9.99989805E-01   # UASf(4,4)
     5   2     5.13773015E-01   # UASf(5,2)
     5   5     8.57926156E-01   # UASf(5,5)
     6   3     7.24941820E-01   # UASf(6,3)
     6   6    -6.88810103E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     1.78495859E-05   # UASf(1,4)
     2   2     9.99970732E-01   # UASf(2,2)
     2   5     7.65085064E-03   # UASf(2,5)
     3   3     7.08249465E-01   # UASf(3,3)
     3   6    -7.05962248E-01   # UASf(3,6)
     4   1    -1.78495859E-05   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -7.65085064E-03   # UASf(5,2)
     5   5     9.99970732E-01   # UASf(5,5)
     6   3     7.05962248E-01   # UASf(6,3)
     6   6     7.08249465E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99967318E-01   # UASf(1,1)
     1   4    -8.08468495E-03   # UASf(1,4)
     2   2     9.92157399E-01   # UASf(2,2)
     2   5    -1.24994779E-01   # UASf(2,5)
     3   3     6.52799510E-01   # UASf(3,3)
     3   6     7.57530726E-01   # UASf(3,6)
     4   1     8.08468495E-03   # UASf(4,1)
     4   4     9.99967318E-01   # UASf(4,4)
     5   2     1.24994779E-01   # UASf(5,2)
     5   5     9.92157399E-01   # UASf(5,5)
     6   3     7.57530726E-01   # UASf(6,3)
     6   6    -6.52799510E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.09286602E-01   # UH(1,1)
     1   2     4.16170488E-01   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.16170488E-01   # UH(2,1)
     2   2     9.09286602E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     2.62658673E-01   # Gamma(h0)
     3.00541358E-05   2        22        22   # BR(h0 -> photon photon)
     1.19184638E-05   2        22        23   # BR(h0 -> photon Z)
     1.98722702E-04   2        23        23   # BR(h0 -> Z Z)
     1.75686861E-03   2       -24        24   # BR(h0 -> W W)
     7.00850936E-04   2        21        21   # BR(h0 -> gluon gluon)
     9.18277497E-09   2       -11        11   # BR(h0 -> Electron electron)
     4.08462840E-04   2       -13        13   # BR(h0 -> Muon muon)
     1.15603973E-01   2       -15        15   # BR(h0 -> Tau tau)
     2.09891069E-09   2        -2         2   # BR(h0 -> Up up)
     2.90714262E-04   2        -4         4   # BR(h0 -> Charm charm)
     1.41782553E-06   2        -1         1   # BR(h0 -> Down down)
     3.56042248E-04   2        -3         3   # BR(h0 -> Strange strange)
     8.80640964E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     6.37366614E-01   # Gamma(HH)
     2.18577979E-06   2        22        22   # BR(HH -> photon photon)
     4.90167891E-06   2        22        23   # BR(HH -> photon Z)
     1.12231928E-04   2        23        23   # BR(HH -> Z Z)
     8.08971089E-04   2       -24        24   # BR(HH -> W W)
     1.55260106E-03   2        21        21   # BR(HH -> gluon gluon)
     9.46245361E-09   2       -11        11   # BR(HH -> Electron electron)
     4.20915212E-04   2       -13        13   # BR(HH -> Muon muon)
     1.18924076E-01   2       -15        15   # BR(HH -> Tau tau)
     4.03917345E-10   2        -2         2   # BR(HH -> Up up)
     5.59500160E-05   2        -4         4   # BR(HH -> Charm charm)
     1.42548220E-06   2        -1         1   # BR(HH -> Down down)
     3.57963412E-04   2        -3         3   # BR(HH -> Strange strange)
     8.77758768E-01   2        -5         5   # BR(HH -> Bottom bottom)
     6.34574337E-10   2        23        36   # BR(HH -> Z A0)
DECAY        36     8.93419961E-01   # Gamma(A0)
    -2.34995341E-07   2        22        22   # BR(A0 -> photon photon)
    -3.54983224E-08   2        22        23   # BR(A0 -> photon Z)
    -9.57019761E-04   2        21        21   # BR(A0 -> gluon gluon)
    -9.38419357E-09   2       -11        11   # BR(A0 -> Electron electron)
     4.17431765E-04   2       -13        13   # BR(A0 -> Muon muon)
    -1.18073313E-01   2       -15        15   # BR(A0 -> Tau tau)
    -2.09032387E-12   2        -2         2   # BR(A0 -> Up up)
    -2.99719999E-07   2        -4         4   # BR(A0 -> Charm charm)
    -1.42338238E-06   2        -1         1   # BR(A0 -> Down down)
    -3.57436794E-04   2        -3         3   # BR(A0 -> Strange strange)
    -8.80192784E-01   2        -5         5   # BR(A0 -> Bottom bottom)
    -1.14285594E-08   2        23        25   # BR(A0 -> Z h0)
DECAY        37     1.25502536E-01   # Gamma(Hp)
     8.13380214E-08   2       -11        12   # BR(Hp -> Electron nu_e)
     3.47745059E-03   2       -13        14   # BR(Hp -> Muon nu_mu)
     9.83394607E-01   2       -15        16   # BR(Hp -> Tau nu_tau)
     1.08875149E-05   2        -1         2   # BR(Hp -> Down up)
     1.21744225E-04   2        -3         2   # BR(Hp -> Strange up)
     7.13399184E-05   2        -5         2   # BR(Hp -> Bottom up)
     5.92447169E-07   2        -1         4   # BR(Hp -> Down charm)
     2.72660471E-03   2        -3         4   # BR(Hp -> Strange charm)
     9.98875104E-03   2        -5         4   # BR(Hp -> Bottom charm)
     2.99915293E-05   2        -5         6   # BR(Hp -> Bottom top)
     7.77101663E-05   2        24        25   # BR(Hp -> W h0)
     2.61849917E-05   2        24        35   # BR(Hp -> W HH)
     7.40548895E-05   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37802950E+00   # Gamma(top)
     9.95098676E-01   2         5        24   # BR(top -> bottom W)
     4.90132353E-03   2         5        37   # BR(top -> bottom Hp)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
