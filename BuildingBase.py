import sys 

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.__south = south
        self.__west = west
        self.__width_WE = width_WE
        self.__width_NS = width_NS
        self.__height = height

    def corners(self):
        return {"north-west": [self.__south + self.__width_NS, self.__west],
                "north-east": [self.__south + self.__width_NS, self.__west + self.__width_WE],
                "south-west": [self.__south, self.__west],
                "south-east": [self.__south, self.__west + self.__width_WE]}

    def area(self):
        return self.__width_NS * self.__width_WE

    def volume(self):
        return self.__width_NS * self.__width_WE * self.__height

    def __repr__(self):
        return "Building({}, {}, {}, {}, {})".format(self.__south, 
                                                     self.__west, 
                                                     self.__width_WE, 
                                                     self.__width_NS, 
                                                     self.__height)


if __name__ == "__main__":
    b1 = Building(0, 0, 10.5, 2.546)
    assert str(b1) == "Building(0, 0, 10.5, 2.546, 10)"
    assert Building(1, 2.5, 4.2, 1.25).area() == 5.25
    assert Building(1, 2.5, 4.2, 1.25, 101).volume() == 530.25
    assert Building(1, 2, 2, 2).corners() == {"north-west": [3, 2], 
                                              "north-east": [3, 4], 
                                              "south-west": [1, 2], 
                                              "south-east": [1, 4]}
