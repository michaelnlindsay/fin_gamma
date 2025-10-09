import gammalib
import ctools

print("CTA Data Pipeline at your service...")

models=gammalib.GModels()
print(models)

sim = ctools.ctobssim()
sim["ra"]  = 83.63
sim["dec"] = 22.01
sim.execute()