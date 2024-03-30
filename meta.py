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
            assetCreator.USD(JSON).Generator()
        else:
            if JSON[0]['type'] == 'surface':
                assetCreator.Material(JSON).Generator()

            if JSON[0]['type'] == '3d':
                assetCreator.Asset(JSON).Generator()
                
            if JSON[0]['type'] == '3dplant':
                return "yet to be implemented"