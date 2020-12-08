from Yoga import Yoga


class Backbend(Yoga):
    important_prop = "yoga_mat"
    feet_position = "parallell"
        #all attributes and methods in this function are public so they can be acccessed by the session class
    def __init__(self, name, breath_free, practice_days_per_week=7):
        super().__init__(breath_free, practice_days_per_week=7)
        self.backbends = []
        self.name = name
        self.breath_free = breath_free
        self.practice_days_per_week = practice_days_per_week

    def favorite_backbends(self, *fav_backbend):
        '''this function will add backbend names to a list '''
        for b in fav_backbend:
            self.backbends.append(b)
    @staticmethod
    def should_i_do_this_pose(breath_free): 
        """This function is overriding the super class function, it will print a conditional message about doing a backbend"""
        
        if breath_free == True:
           print("Proceed without props, keep breathing!")
        else:
            print("Grab a chair and practice a supported backbend for a few months")

    @classmethod
    def change_feet_position(cls, new_feet_position):
        """this classmethod will update the requirement for this practice"""
        cls.feet_position = new_feet_position
        

    @classmethod
    def change_prop(cls, new_prop):
        """this classmethod will update the requirement for this practice"""
        cls.important_prop = new_prop  
        






#yogini1= Backbend("Urdhva Danurasana", True, 3)#instantiating the object
# yogini1.favorite_backbends("Camel", "Urdhva Danurasana", "backbend on a chair")#calling instance method adding backbend names to a list
# print(f'If you are not sure which backbend to work on today... Here is a list of options:{yogini1.backbends}')
print("================")
print(Backbend.should_i_do_this_pose(True)) ##SttcMthd I just call the class and not my object
print("================")
# yogini1.change_feet_position("turn feet in, heels out toes in")
# print (f"Save your back {yogini1.feet_position} when you practice back bends!")
# yogini1.change_prop("chair")
# print(f'If you can\'t bend back into a backbend, you dont need a mat, instead use a {yogini1.important_prop} to support your backbend!')