from Yoga import Yoga



class ForwardBend(Yoga):
    theme = "Don't round your back while in a forward bend!"
    therapeutic_benefit = "strengthen the core"
    #all attributes and methods in this function are public so they can be acccessed by the session class
    def __init__(self,name, time_in_pose, breath_free, practice_days_per_week=7):
        super().__init__(breath_free, practice_days_per_week=7)
        self.name = name
        self.time_in_pose = 0
        self.practice_days_per_week = practice_days_per_week


    def increase_time(self,breath_free):
        if breath_free == True:
            self.time_in_pose += self.time_in_pose + 1
            return self.time_in_pose
    
        else:
            print("Slowly come out of the pose relax and repeat 10x dont stay long in the pose")
  

    def should_i_do_this_pose(breath_free): 
        """This function is overriding the super class function, it will print a conditional message about doing a backbend"""
        
        if breath_free == True:
           print("Proceed without props, keep breathing!")
        else:
            print("Grab a belt and lay down, let\'s wowrk on the hamstrigs!")

    @classmethod
    def change_theme(cls, new_theme):
        """this classmethod will update the requirement for this practice"""
        cls.theme = new_theme

    @classmethod
    def change_therapeutic_benefit(cls, new_therapeutic_benefit):
        """this classmethod will update the requirement for this practice"""
        cls.therapeutic_benefit = new_therapeutic_benefit


#=========================Showing Multiple inheritace using Classes: seatedForwardBend and SeatePose:========================================================
    
    def weekly_counter(self,num_days):
        self.practice_days_per_week = num_days
        print(f'This week you have practiced {self.practice_days_per_week} times!')


    def instructions(self):
        print(f"Sit in: {self.name} and fold forward from the hips, not by rounding the back. If the hips wont rotate the torso forward, celebrate!! You have just discovered you need to work on hip flexibility to fold forward!!")



#yogini1 = ForwardBend("downwardDog",10, False, 4)
# yogini1.increase_time(True)
# yogini1.increase_time(True)
# yogini1.increase_time(True)
# yogini1.increase_time(True)
# print('----------------')
# print(yogini1.time_in_pose)
# print("----------------")
# print(ForwardBend.should_i_do_this_pose(True))
# yogini1.change_therapeutic_benefit("restore the nervous system")
# print(f'Forward bends can be very useful for your health. It\'s a powerful tool to {yogini1.therapeutic_benefit}.')
# yogini1.change_theme("healing back pain")
# print(f'Forward bends strengthen the back. Practice daily emphasizing aspects of the pose that help with {yogini1.theme}.')
#===============================Multiple inheritace example==================================
#yogini1.weekly_counter(5)
#yogini1.instructions()