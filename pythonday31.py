# student class

class Student:
    # every method inside of a class needs to also pass in the name of the blueprint, so we can change it
    def __init__(self, name, hometown, major):  # initialise 
        self.name = name # the first value that i put in has to be name
        self.hometown = hometown
        self.major = major
        self.courses = []
        
    def change_major(self, new_major):
        self.major = new_major
        print('Welcome to {}.'.format(new_major))
        
    def __str__(self):
        return "{}: a {} student taking {} courses.".format(self.name, self.major, len(self.courses))
    # just tells you memory location
    
    def __eq__(self, other):
        if self.name == other.name and self.hometown == other.hometown:
            return True
        else:
            return False
        # doesn't have to make sense!

    def register(self, course):
        self.courses.append(course)
        print('Registered for ' + course.name)

    def __lt__(self, other):
        return self.hometown < other.hometown
    # data type of hometown is str - str class has lt method defined
    # can't sort without lt
    
    def __ge__(self, other):
        return self.hometown >= other.hometown
    
    def has_mcdaniel(self):
        for c in self.courses:
            if c.instructor == 'McDaniel':
                return True
        return False # none of the courses had McDaniel

    def full_load(self):
        num_hours = 0
        for c in self.courses:
            num_hours += c.hours
        if num_hours >= 12:
            return True
        else:
            return False

class Course:
    def __init__(self,name,hours,i='Unknown'): # i is default parameter
        self.name = name
        self.hours = hours
        self.instructor = i
    def __str__(self):
        # returns string representation of the object
        return '{} is {} hours taught by {}'.format(self.name,self.hours,self.instructor)
        

collin = Student('Collin', 'Demorest', 'CM')
mycourse = Course('CS2316',3,'McDaniel')
othercourse = Course('CS1331',3)
print(othercourse.instructor)
# collin.register('CS2316') # doesn't give us any info about the course itself
collin.register(mycourse)
collin.register(othercourse)

# how many hours is collin registered for?
hours = 0
for c in collin.courses:
    print(c)
    hours += c.hours
print(hours)

# write a method for the student class that returns True if a student has McDaniel
# of any of their classes - return True if it finds

print(collin.has_mcdaniel())

# write a method for the Student class that returns True if the student is taking
# 12 or more hours


