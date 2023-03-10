#Class for simulating races. It has a method called simulate. It receives the formula_one_repository as dependency. 
from repositories import formula_one_repository

class FormulaOneRepository():
    #constructor that accepts the formula one repository as dependency
    def __init__(self, formula_one_repository: formula_one_repository.FormulaOneRepository):
        self.formula_one_repository = formula_one_repository

    #simulate method that executes the simulation
    def simulate(self):
        cars = self.formula_one_repository.get_all()
        