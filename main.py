from Yoga import Yoga
from Backbend import Backbend
from ForwardBend import ForwardBend
from Session import Session
from SeatedPose import SeatedPose
from SeatedForwardBend import SeatedForwardBend
#=============================================
# object for Yoga Class
#=============================================
print("========class Yoga=============")
yogini1 = Yoga(True,5)
yogini1.practice(4)
print("=====================")
yogini1.change_practice_space("on a warm rock")
print(f'I like to practice {yogini1.practice_space} in the mornings!')
print("=====================")
print(Yoga.should_i_do_this_pose(True)) #static Method
print("=====================")
yogini1.change_niyama_requirement("contentment")
print(f'There are 5 major aspects to a yogi\'s practice. Each week pick one. This week well practice with {yogini1.niyama_requirement} in mind.')

#==============================================
#object for Session Class
#==============================================
print("========class Session=============")
yogini1= Session(30, "Restorative Practice")
print(yogini1.theme)
print("======================")
# yogini1.add_backbend("upward dog", True, 7)
# yogini1.add_backbend("Downward Dog", True, 7)
# yogini1.add_backbend("Hanumanasana", True, 7)
# yogini1.add_backbend("Padangusthasana", True, 7)
# yogini1.add_backbend("Pincha Mayurasana", True, 7)

yogini1.add_forwardBend( 30,True, 6, "Utanasana", "padagusthasana", "Downward Dog", "maricyasana")
yogini1.display_sequence()
print("======================")
yogini1.add_backbend(True, 7, "pose1", "pose2", "pose3")
yogini1.display_sequence()
print("======================")
print(yogini1.change_on_class_start("ommm,ommmm,ommmm"))
print("======================")
print(yogini1.change_dress_code("Before practice, remove your socks!"))

#==============================================
#object for BackBend Class
#==============================================
print("======BackBend===============")
yogini1= Backbend("Urdhva Danurasana", True, 3)#instantiating the object
yogini1.favorite_backbends("Camel", "Urdhva Danurasana", "backbend on a chair")#calling instance method adding backbend names to a list
print(f'If you are not sure which backbend to work on today... Here is a list of options:{yogini1.backbends}')
print("=====================")
Backbend.should_i_do_this_pose(True) ##SttcMthd I just call the class and not my object
print("=====================")
yogini1.change_feet_position("turn feet in, heels out toes in")
print (f"Save your back {yogini1.feet_position} when you practice back bends!")
print("=====================")
yogini1.change_prop("chair")
print(f'If you can\'t bend back into a backbend, you dont need a mat, instead use a {yogini1.important_prop} to support your backbend!')
print("=====================")

#==============================================
#object for Forward Bend Class
#==============================================
print("=======Forward Bend==============")
yogini1 = ForwardBend("downwardDog",10, False, 4)
yogini1.increase_time(True)
yogini1.increase_time(True)
yogini1.increase_time(True)
yogini1.increase_time(True)
print("=====================")
print(yogini1.time_in_pose) #prints out how many minutes one should stay in the pose
print("=====================")
print(ForwardBend.should_i_do_this_pose(True))
print("=====================")
yogini1.change_therapeutic_benefit("restore the nervous system")
print(f'Forward bends can be very useful for your health. It\'s a powerful tool to {yogini1.therapeutic_benefit}.')
print("=====================")
yogini1.change_theme("healing back pain")
print(f'Forward bends strengthen the back. Practice daily emphasizing aspects of the pose that help with {yogini1.theme}.')
#=====================Multiple Inheritance ====================
yogini1.weekly_counter(5)
yogini1.instructions()

print("=====================")
#====================================================
# object for SeatedPose class
#====================================================
yogini1 = SeatedPose("baddhaKonasana")
yogini1.sit("gomukasana")
yogini1.instructions()

print("=====================")

#====================================================
# object for SeatedForward bend class
#====================================================