import random



class Hat:
  #  def __init__(self):
  #      self.house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
  
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.house)
        print(name, "is in", house)
    
Hat.sort("Harry")