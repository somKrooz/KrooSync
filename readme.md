## call the plugin like this from houdini python console:

from KrooSync import main as mg
import importlib

importlib.reload(mg)

view = mg.Sync()
view.show()
