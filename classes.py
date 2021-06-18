class Animal:
    eatProperty=""
    walkProperty=""
    sleepProperty=""
    nameProperty=""
    def __init__(self,name,eat):
        self.nameProperty=name
        self.eatProperty=eat
    def Animaltype(self) :
        animal_type=input("what category of food does the animal eat")
        return self.eatProperty
    def getname(self) :
        return self.nameProperty
    def animal_traits(self):
        return self.walkProperty
        return self.sleepProperty
animal1= Animal("Lion","Canivorous")  
animal1.Animaltype
print (animal1.Animaltype)         
    