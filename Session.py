from Backbend import Backbend
from ForwardBend import ForwardBend



class Session:
    on_class_start = "sit quietly"
    dress_code = "remove shoes"
    #all attributes and methods in this function are public so they can be acccessed anywhere in the program
    def __init__(self, duration, theme):
        self.duration = duration
        self.theme = theme
        self.sequence = []

    def add_backbend(self, breath_free, practice_days_per_week=7, *name):
        """using composition to import function objects into the function"""
        new_backbend = Backbend(name, breath_free, practice_days_per_week=7)
        self.sequence.append(new_backbend)

    def add_forwardBend(self, time_in_pose, breath_free, practice_days_per_week=7, *name):
        new_forwardbend = ForwardBend(name, time_in_pose, breath_free, practice_days_per_week=7)
        self.sequence.append(new_forwardbend)


    def display_sequence(self):
        """adding names of poses to the sequence list This function prints them out """
        for s in self.sequence:
            print(s.name)

    @classmethod
    def change_on_class_start(cls, new_on_class_start):
        """this classmethod will update the requirement for this practice"""
        cls.on_class_start = new_on_class_start
        print(cls.on_class_start)

    @classmethod
    def change_dress_code(cls, new_dress_code):
        """this classmethod will update the requirement for this practice"""
        cls.dress_code = new_dress_code
        print(cls.dress_code)


yogini1= Session(30, "Restorative Practice")#===================================>
# print(yogini1.theme)
# print("======================")
# yogini1.add_backbend("upward dog", True, 7)
# yogini1.add_backbend("Downward Dog", True, 7)
# yogini1.add_backbend("Hanumanasana", True, 7)
# yogini1.add_backbend("Padangusthasana", True, 7)
# # yogini1.add_backbend("Pincha Mayurasana", True, 7)
# print("======================")
yogini1.add_forwardBend( 30,True, 6, "Utanasana", "padagusthasana", "Downward Dog", "maricyasana")#=========================>
# yogini1.add_backbend(True, 7, "pose1", "pose2", "pose3")
yogini1.display_sequence()#=============================================>
# print(yogini1.change_on_class_start("ommm,ommmm,ommmm"))
# print(yogini1.change_dress_code("Before practice, remove your socks!"))

