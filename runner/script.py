import gammalib
import ctools
import cscripts

print("CTA Data Pipeline at your service...")

sim = ctools.ctobssim()
sim["ra"]  = 83.63
sim["dec"] = 22.01
sim.execute()

lightcrv = cscripts.cslightcrv()
lightcrv.execute()

models=gammalib.GModels()
print(models)