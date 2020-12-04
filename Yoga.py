class Yoga:
    yama_most_important_requirement = "non-violence"
    niyama_requirement = "cleanliness"
    practice_space = "indoors"
    def __init__(self,breath_free, is_flexible, is_strong, practice_days_per_week=7):
        self.breath_free = breath_free
        self.is_flexible = is_flexible
        self.is_strong = is_strong
        self.practice_days_per_week = practice_days_per_week

    def practice(self, practice_days_per_week):
        if practice_days_per_week < 7:
            print("Practice a little every Day!")
        else:
            print("Observe the movement of thought, without analysing")

    @classmethod
    def change_practice_location(cls, new_practice_space):
        cls.practice_space = new_practice_space

    @staticmethod
    def should_i_do_this_pose(self, breath_free): 
        if breath_free == True:
           print("Enjoy the pose, hold a little longer")
        else:
            print("Dont hold your breath, come out and let's use some props!")










andrea = Yoga(True,True,True,5)
andrea.practice(7)
andrea.change_practice_location("on a warm rock")
print(f'I like to practice {andrea.practice_space} in the moornings!')
print(Yoga.should_i_do_this_pose(True))
