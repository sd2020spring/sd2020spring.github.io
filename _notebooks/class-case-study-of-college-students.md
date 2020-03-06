---
date: 2020-03-05T18:19:09-05:00
source: notebooks/class-case-study-of-college-students.ipynb
---

{% include toc %}


#  Classes Case Study Using College Students

This notebook walks through a (hopefully) relatable example of why one might endeavor to set up classes in Python projects.

Let's say that we are interested in having Software Design students write a program that can help them find potential partners for Mini-Project 4.

##  When there's a need for more structure than built-in objects can provide

We can capture a few notable attributes of a student in a list.

```
ronald_mcstudent = ['Ronald McStudent','18','computer science', '96']
```

We have some useful information captured, but it is hard to tell what some of the information means.
Is Ronald a first-year college student, class of 2018 majoring in computer science who was born in '96?
Is Ronald an 18 year-old high school senior enrolled in a course named computer science who is averaging 96% on all of his work?

We can clarify by using another one of Python's built-in objects: a dictionary.

```
ronald_mcstudent = {'name' : 'Ronald McStudent', 'age' : 18, 'class' : 'computer science', 'average' : 96}
```

We might want to do more than what is possible with lists, dictionaries, or combinations of the two. For example, we might find it useful to give every student a function that will help ascertain whether the student might make a good partner to another student.


## Creating a college student class

You can make a barebones class very quickly, to get a quick win under your belt.

```
class CollegeStudent:
    pass
```


### Adding attributes

There are some common attributes that college students have. Each college student can be described using a custom-created object called a class. Every time that we want to keep track of a unique student in our computer's memory or saved as a file on the hard drive, we use a class as a template to make an "instance" of a "CollegeStudent" in this case.
```
class CollegeStudent:
    # "initializes" each instance of a class, storing instance attributes
    def __init__(self, name, gradyear):
        self.name = name
        self.gradyear = gradyear
```

The "self" is there because we are confident that every college student will not have the same name, so we do not say CollegeStudent.name = name. Choosing to use the word self serves as a reminder that "instances" made of the class will each have a name to itself.




```python
class CollegeStudent:
    # "initializes" each instance of a class, storing instance attributes
    def __init__(self, name, gradyear):
        self.name = name
        self.gradyear = gradyear

sophie = CollegeStudent('Sophie', 2024)
dezzie = CollegeStudent('Dezzie', 2025)

print("{} and {} are a SoftDes students graduating in {} and {} respectively".format(sophie.name, dezzie.name, sophie.gradyear, dezzie.gradyear))
```

## Things to notice about creating classes

We never called the `__init__()` function. We never have to. That one runs automatically every time a class is created. It's special.

We used dot notation to gain access to attributes (values of a variable in a particular instance of a class in this case).

## Instance methods

A function that is created to be run from within a class is called a method.
We are looking to help assess whether a particular student will be a good partner on a class project, and we believe that students who bring unique perspectives to partnerships are best. We will write a method called different_perspective(). This method will look at a potential partner and return true if that person does not have the exact same experience as the student does OR the two students are not the same incoming class. Notice that we add an `experience` attribute.


```python
class CollegeStudent:
    # "initializes" each instance of a class, storing instance attributes
    def __init__(self, name, gradyear, experience):
        self.name = name
        self.gradyear = gradyear
        self.experience = experience


    # compares the experience of two students
    def different_perspective(self, potential_partner):
        if self.experience == potential_partner.experience:
            return False
        elif self.gradyear == potential_partner.gradyear:
            return False
        else:
            return True

sophie = CollegeStudent('Sophie', 2024, 'text mining')
dezzie = CollegeStudent('Dezzie', 2025, 'computational art')
ian = CollegeStudent('Ian', 2024, 'gene finding')

print("it is {} that {} and {} would probably make good MP4 partners".format(sophie.different_perspective(dezzie), sophie.name, dezzie.name))
print("it is {} that {} and {} would probably make good MP4 partners".format(sophie.different_perspective(ian), sophie.name, ian.name))

```

## Parent and child classes

In the case of Software Design, there are at least three different types of students in the room at any given time. They are very similar, but have some important differences. We could choose to make three classes that were mostly the same, but had minor differences to keep track of: Olin students, Babson students, and course assistants. However, we can use the notion of inheritance to use a parent class to define most behaviors and make children classes that will vary in a few ways.


We will expand what the CollegeStudent class does.


```python
class CollegeStudent:
    #Class Attribute    
    college = 'Olin'

    # "initializes" each instance of a class, storing instance attributes
    def __init__(self, name, gradyear, experience, major, overdue_assignments):
        self.name = name
        self.gradyear = gradyear
        self.experience = experience
        self.major = major
        self.overdue_assignments = overdue_assignments


    # compares the experience of two students
    def different_perspective(self, potential_partner):
        if self.experience == potential_partner.experience:
            return False
        elif self.gradyear == potential_partner.gradyear:
            return False
        else:
            return True


    # prints how on top of their work the student is
    def on_top_of_it(self):
        return "{} has yet to turn in {} assignments".format(self.name, self.overdue_assignments)

sophie = CollegeStudent('Sophie', 2024, 'text mining', 'computing', 1)
dezzie = CollegeStudent('Dezzie', 2025, 'computational art', 'mechanical engineering', 3)
ian = CollegeStudent('Ian', 2024, 'gene finding', 'undeclared', 2)

print(ian.on_top_of_it())

```

We will make two subclass named OlinSoftDesStudent and BabsonSoftDesStudent. Each will have a need for slightly different functions. Notice that they are defined with a relationship to CollegeStudent in parentheses.

```
class OlinSoftDesStudent(CollegeStudent):
    def course_counts_toward(self):
        if major == 'computing':
            return 'major credits'
        else:
            return 'elective credits'


class BabsonSoftDesStudent(CollegeStudent):
    def course_counts_toward(self):
        return 'Olin certificate or general credit'
```


Additionally, children classes can override properties of the parent - either methods or attributes.


```python
class CollegeStudent:
    #Class Attribute    
    college = 'Olin'

    # "initializes" each instance of a class, storing instance attributes
    def __init__(self, name, gradyear, experience, major, overdue_assignments):
        self.name = name
        self.gradyear = gradyear
        self.experience = experience
        self.major = major
        self.overdue_assignments = overdue_assignments


    # compares the experience of two students
    def different_perspective(self, potential_partner):
        if self.experience == potential_partner.experience:
            return False
        elif self.gradyear == potential_partner.gradyear:
            return False
        else:
            return True


    # prints how on top of their work the student is
    def on_top_of_it(self):
        return "{} has yet to turn in {} assignments".format(self.name, self.overdue_assignments)


class OlinSoftDesStudent(CollegeStudent):
    def course_counts_toward(self):
        if major == 'computing':
            return 'major credits'
        else:
            return 'elective credits'

    def on_top_of_it(self):
        if self.overdue_assignments > 5:
            return 'email a warning to student_life_concerns@olin.edu'
        else:
            return 'pretty on top of it'


class BabsonSoftDesStudent(CollegeStudent):
    def course_counts_toward(self):
        return 'Olin certificate or general credit'

    def on_top_of_it(self):
        if self.overdue_assignments > 5:
            return 'email a warning to cross_reg_adviser@babson.edu'
        else:
            return 'pretty on top of it'


class SoftDesCourseAssistant(CollegeStudent):
    def on_top_of_it(self):
        return "{} has yet to grade {} student assignments".format(self.name, self.overdue_assignments)


sophie = OlinSoftDesStudent('Sophie', 2024, 'text mining', 'computing', 6)
dezzie = BabsonSoftDesStudent('Dezzie', 2025, 'computational art', 'mechanical engineering', 3)
ian = SoftDesCourseAssistant('Ian', 2024, 'gene finding', 'undeclared', 2)

print(ian.on_top_of_it())
print(dezzie.on_top_of_it())
print(sophie.on_top_of_it())

```
## Questions

To check what you have explored with classes and inheritance, think about what these terms mean to you, and how you think they relate to each other.

What is a class?

What is an instance? Can you make multiple instances?

What is an attribute?

What is a method?

How do you get the value of an attribute or call a behavior of an instance of a class?

Do you need to call the __init__ method?

What role does the word self play?

Describe a scenario where you would want to use inheritance.

Are children classes able to override methods and attributes of their parents?
