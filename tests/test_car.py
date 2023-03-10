#unit test start method of the car class
import pytest
from model.car import Car

class TestCar:
    def test_start(self):
        #create a car object
        car = Car()
        #start the car
        car.start()
        #assert that the state of the car is started
        assert car.state == "started"