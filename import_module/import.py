import importlib

params = importlib.import_module("path.main")

print(params.exploit)
params.exploit()
