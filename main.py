from school_schedule.student import Student

#first instance
quinn = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]
            )

quinn.add_class("Painting")
print(quinn.get_num_classes())
# quinn.summary()
# print(quinn.summary())
print(quinn)

# second instance
claire = Student(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

print(claire.get_num_classes())
# claire.summary()
# print(claire.summary())

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function