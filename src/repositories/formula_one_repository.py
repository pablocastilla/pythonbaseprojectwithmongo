from abc import ABC, abstractmethod
from typing import List
from model.formula_one import FormulaOne


# abstract repository for the formula one entity.
# It has the methods to create, update, delete and get all
class FormulaOneRepository(ABC):
    @abstractmethod
    def create(self, formula_one: FormulaOne) -> FormulaOne:
        pass

    @abstractmethod
    def update(self, formula_one: FormulaOne) -> FormulaOne:
        pass

    @abstractmethod
    def delete(self, formula_one: FormulaOne) -> FormulaOne:
        pass

    @abstractmethod
    def get_all(self) -> List[FormulaOne]:
        pass
