class Yoga:
    """Basic set of instructions common to all practicioners"""
    
    yama_most_important_requirement = "non-violence"
    niyama_requirement = "cleanliness"
    practice_space = "indoors"
   #all attributes and methods are public as the Yoga class members can be accessed from anywhere in the program
    def __init__(self, breath_free, practice_days_per_week=7):
        """attributes that are different depending on the person practicing"""
       
        self.breath_free = breath_free
        self.practice_days_per_week = practice_days_per_week
      

    def practice(self,days_per_week):
        """prints out statement depending on how many days per week a practicioner practices"""
        self.practice_days_per_week == days_per_week
        if self.practice_days_per_week < 7:
            print("Practice a little every Day!")
        else:
            print("Observe the movement of thought, without analysing")

    @classmethod
    def change_practice_space(cls, new_practice_space):
        """this classmethod will update the location of the practice"""
        cls.practice_space = new_practice_space

    
    @staticmethod
    def should_i_do_this_pose(breath_free): 
        """This function prints out general guidelines for practicing yoga"""
        
        if breath_free == True:
            return "Enjoy the pose, hold a little longer" 
        else:
            return "Dont hold your breath, come out and let's use some props!"

    @classmethod
    def change_niyama_requirement(cls, new_niyama):
        """this classmethod will update the requirement for this practice"""
        cls.niyama_requirement = new_niyama

    
    





# yogini1 = Yoga(True,5)
# yogini1.practice(4)
#yogini1.change_practice_space("on a warm rock")
# print(f'I like to practice {yogini1.practice_space} in the mornings!')
print(Yoga.should_i_do_this_pose(True)) #===========================================>static Method
# yogini1.change_niyama_requirement("contentment")
# print(f'There are 5 major aspects to a yogi\'s practice. Each week pick one. This week well practice with {yogini1.niyama_requirement} in mind.')
