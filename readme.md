KrooSync is a plugin that Connects with Megascans bridge to modify the the asset import behavior

##call script

from KrooSync import main as m
import importlib

importlib.reload(m)

vr = m.Sync()
vr.show()