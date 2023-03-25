class Room:
    length = 0.0
    breadth = 0.0

    def calculate_area(self):
        print(f'Room area: {self.length * self.breadth}')


study_room = Room()

study_room.length = 50.2
study_room.breadth = 78.9

study_room.calculate_area()
