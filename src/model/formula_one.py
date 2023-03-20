from mongoengine import Document, IntField, StringField


# Class that inherits from mongoengine and it is called formula one,
# it has a method to open the drs and another one for closing it,
# also for accelerating and braking
class FormulaOne(Document):
    car_number = IntField(required=True, primary_key=True)
    driver_name = StringField(required=True)

    # open drs
    def open_drs(self):
        print("Opening drs")

    # close drs
    def close_drs(self):
        print("Closing drs")

    # accelerate
    def accelerate(self):
        print("Accelerating")

    # brake
    def brake(self):
        print("Braking")
