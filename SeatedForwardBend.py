from ForwardBend import ForwardBend
from SeatedPose import SeatedPose

class SeatedForwardBend(ForwardBend, SeatedPose):
    """multiple inheritace from ForwardBend class and the seatedPose class to create a seatedforwardbend class"""
    def __init__(self,name, time_in_pose, breath_free, practice_days_per_week=7):
        ForwardBend.__init__(self, name, time_in_pose, breath_free, practice_days_per_week=7)
        SeatedPose.__init__(self, name)

    def instructions(self):
        ForwardBend.instructions(self)
        SeatedPose.instructions(self)

    #=============Calling a function from one of the inherited classe ForwardBend--

    

yogini1 = SeatedForwardBend("dandasana",10,True,4)
yogini1.instructions() # here I customized my instructions fuction by adding both messages from the parent super classes!
yogini1.weekly_counter(7) #here I just have to call the func I want from the super class that has it!