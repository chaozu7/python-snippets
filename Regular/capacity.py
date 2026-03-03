class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    # method
    def add_passanger(self, name):
        if not self.opn_seats():
            return False
        self.passangers.append(name)
        return True

    def opn_seats(self):
        return self.capacity - len(self.passangers)


flight = Flight(4)

people = ["Jan", "Maria", "Jola", "Kama"]
for person in people:
    success = flight.add_passanger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
