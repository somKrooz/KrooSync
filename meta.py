from .lib import assetCreator

class AssetFactory:
    
    @staticmethod
    def GenerateAsset(json, state):

        if state:
            pass
        else:
            if json[0]['type'] == 'surface':
                assetCreator.Material(json).Generator()

            if json[0]['type'] == '3d':
                assetCreator.Asset(json).Generator()
                
            if json[0]['type'] == '3dplant':
                return "yet to be implemented"