class Student:
    def __init__(self, name, house, patronus):     
        self.house = house
        self.name = name
        self.patronus = patronus
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    #if we have _variable - please don't touch this
    #if we have __variable - really please don't toyuch this
    @property
    def name(self):
        return self._name   
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    #Getter - get some attibute
    @property
    def house(self):
        return self._house
    
    #Setter - set some value
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦄"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "🪄"
            
    
    
def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())



def get_student(): 
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) 
    
if __name__ == "__main__":
    main()