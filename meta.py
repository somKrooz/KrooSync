from .lib import assetCreator
import hou
import os
import json

class AssetFactory:

    @staticmethod
    def GenerateAsset(JSON):
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, "r") as f:
            data = json.load(f)
            state = data["USDstate"]

        if state:
            if JSON[0]['type'] == '3d':
                assetCreator.USD(JSON).Generator()
            else:
                print("Import Failed : Only 3d assets are supported at the moment....")
        else:
            if JSON[0]['type'] == 'surface':
                assetCreator.Material(JSON).Generator()

            if JSON[0]['type'] == '3d':
                assetCreator.Asset(JSON).Generator()
                
            if JSON[0]['type'] == '3dplant':
                assetCreator.Plants(JSON).Generator()