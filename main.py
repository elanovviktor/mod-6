class Horse:

    x_distance = 0
    sound = 'frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repet'

    def fly(self, dy):
        self. y_distance += dy
        return self. y_distance

class Pegasus(Horse, Eagle):
    Horse.__init__(self)
    Eagle.__init__(self)

    def __init__(self):
        Horse = 0
        Eagle = 0

    def move(self, dx, dy):
        super(). run(dx)
        super(). fly(dy)
    def get_pos(self):
        return self.x_distance, self.y_distance
    def voice(self):

        print(Eagle. sound)
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
