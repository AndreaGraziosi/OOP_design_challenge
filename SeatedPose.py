class SeatedPose:
    """just a quick class to practice multiple inheritance"""#all data members are public 
    def __init__(self, name):
        self.name = name

    def sit(self,name):
        self.name = name
        print(f"Seated poses can be held for a lond time, let\'s practice a seated pose today, sit in:{self.name}")

    def instructions(self):
        print(f"Sit in: {self.name} and stay.") 









# yogini1 = SeatedPose("baddhaKonasana")
# yogini1.sit("gomukasana")
# yogini1.instructions()