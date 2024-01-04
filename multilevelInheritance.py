class GrandFather:
    def __init__(self):
        self.name = " GrandFather"
        self._assets = 1500000

class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.name =  " Father" + self.name 
        self._inharitedAssets = self._assets 
        self._purchasedAssets = 200000
        self._totalAssets = self._inharitedAssets + self._purchasedAssets

class Child(Father):
    def __init__(self, name, assets):
        super().__init__()
        self.name =  name + " " + self.name
        self.__inharitedAssets = self._totalAssets
        self.__purchasedAssets = assets
        self._totalAssets = self.__inharitedAssets + self.__purchasedAssets
    
    def displayData(self):
        print("Name: ", self.name)
        print("Assets: ", self._totalAssets)

obj = Child("Child",100000)
obj.displayData()