###### Hall A Software src SConscript Build File #####
###### Author:  Edward Brash (brash@jlab.org) June 2013

from podd_util import build_library, write_compiledata
Import('baseenv')

libname = 'HallA'

# Sources and headers
src = """
BdataLoc.C                ExtraData.C                FileInclude.C
FixedArrayVar.C           MethodVar.C                SeqCollectionMethodVar.C
SeqCollectionVar.C        THaADCHelicity.C           THaAnalysisObject.C
THaAnalyzer.C             THaApparatus.C             THaArrayString.C
THaAvgVertex.C            THaBeam.C                  THaBeamDet.C
THaBeamEloss.C            THaBeamInfo.C              THaBeamModule.C
THaBPM.C                  THaCherenkov.C             THaCluster.C
THaCodaRun.C              THaCoincTime.C             THaCut.C
THaCutList.C              THaDebugModule.C           THaDecData.C
THaDetectorBase.C         THaDetector.C              THaDetMap.C
THaElectronKine.C         THaElossCorrection.C       THaEpicsEbeam.C
THaEpicsEvtHandler.C      THaEvent.C                 THaEvt125Handler.C
THaEvtTypeHandler.C       THaExtTarCor.C             THaFilter.C
THaFormula.C              THaG0Helicity.C            THaG0HelicityReader.C
THaGoldenTrack.C          THaHelicity.C              THaHelicityDet.C
THaHRS.C                  THaIdealBeam.C             THaInterface.C
THaNamedList.C            THaNonTrackingDetector.C   THaOutput.C
THaParticleInfo.C         THaPhotoReaction.C         THaPhysicsModule.C
THaPidDetector.C          THaPIDinfo.C               THaPostProcess.C
THaPrimaryKine.C          THaPrintOption.C           THaQWEAKHelicity.C
THaQWEAKHelicityReader.C  THaRaster.C                THaRasteredBeam.C
THaReacPointFoil.C        THaReactionPoint.C         THaRTTI.C
THaRunBase.C              THaRun.C                   THaRunParameters.C
THaS2CoincTime.C          THaSAProtonEP.C            THaScalerEvtHandler.C
THaScintillator.C         THaSecondaryKine.C         THaShower.C
THaSpectrometer.C         THaSpectrometerDetector.C  THaString.C
THaSubDetector.C          THaTextvars.C              THaTotalShower.C
THaTrack.C                THaTrackEloss.C            THaTrackID.C
THaTrackInfo.C            THaTrackingDetector.C      THaTrackingModule.C
THaTrackOut.C             THaTrackProj.C             THaTriggerTime.C
THaTwoarmVertex.C         THaUnRasteredBeam.C        THaVar.C
THaVarList.C              THaVDCAnalyticTTDConv.C    THaVDC.C
THaVDCChamber.C           THaVDCCluster.C            THaVDCHit.C
THaVDCPlane.C             THaVDCPoint.C              THaVDCPointPair.C
THaVDCTimeToDistConv.C    THaVDCTrackID.C            THaVDCWire.C
THaVertexModule.C         THaVform.C                 THaVhist.C
VariableArrayVar.C        Variable.C                 VDCeff.C
VectorObjMethodVar.C      VectorObjVar.C             VectorVar.C
"""

# Generate ha_compiledata.h header file
compiledata = 'ha_compiledata.h'
write_compiledata(baseenv,compiledata)

extrahdrs = ['VarDef.h','VarType.h',compiledata]

poddlib = build_library(baseenv, libname, src, extrahdrs,
                        extradicthdrs = ['THaGlobals.h'],
                        useenv = False,
                        versioned = True,
                        destdir = baseenv.subst('$HA_DIR')
                        )
Clean(poddlib, compiledata)
