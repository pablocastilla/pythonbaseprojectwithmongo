# import formula one class
from model.car import FormulaOne

#create main method
if __name__ == '__main__':
    #create a formula one object
    f1 = FormulaOne('Ferrari')
    #start the car
    f1.start()
    #open the drs
    f1.open_drs()
    #drive the car
    f1.drive()