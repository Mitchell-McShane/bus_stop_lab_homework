class Bus:
    def __init__(self, route_number, destination,):
        self.route_number = 22
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, new_passenger):
        self.passengers.append(new_passenger)

    def drop_off(self, drop_passenger):
        self.passengers.remove(drop_passenger)

    def empty(self):
        self.passengers = []

        