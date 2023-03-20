# import formula one class
import mongoengine
from model.formula_one import FormulaOne
from repositories.formula_one_mongo_repository import FormulaOneMongoRepository
from race_simulator import RaceSimulator

# create main method
if __name__ == "__main__":
    mongoengine.connect("localhost:27017")

    # create a formula one object
    hamilton = FormulaOne(car_number=44, driver_name="Lewis Hamilton")
    alonso = FormulaOne(car_number=14, driver_name="Fernando Alonso")

    formula_one_repository = FormulaOneMongoRepository()
    formula_one_repository.create(hamilton)
    formula_one_repository.create(alonso)

    # create the race simulator object with the formula one mongo repository as dependency
    simulator = RaceSimulator(formula_one_repository)
    # call the simulate method
    simulator.simulate()
