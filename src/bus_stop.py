class BusStop:
    def __init__(self, passenger):
        self.passenger = passenger
        self.queue = []

    def add_to_queue(self, passenger):
        self.queue.append(passenger)

