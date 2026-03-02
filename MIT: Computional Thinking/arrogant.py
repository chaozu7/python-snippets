class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
      #  print( 'I believe that ' + Person.say(self,stuff)  )
        return 'I believe that ' + Person.say(self,stuff)

class Professor(Lecturer): 
    def say(self, stuff): 
      #  print( self.name + ' says: ' + Lecturer.lecture(self,stuff))
        return self.name + ' says: ' + Lecturer.lecture(self,stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)

    def say(self, stuff):
       return self.name + ' says: ' + self.lecture(stuff) 
    
e = Person('eric') 
le = Lecturer('kamil') 
pe = Professor('alek') 
ae = ArrogantProfessor('arnold')

e.say('the sky is blue')
le.say('the sky is blue')
le.lecture('the sky is blue')
pe.say('the sky is blue')
pe.lecture('the sky is blue')
ae.say('the sky is blue')
ae.lecture('the sky is blue')