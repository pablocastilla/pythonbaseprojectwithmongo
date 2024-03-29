# mongo implementation of the formula one repository
from typing import List
from model.formula_one import FormulaOne
from repositories.formula_one_repository import FormulaOneRepository


class FormulaOneMongoRepository(FormulaOneRepository):  # type: ignore
    def create(self, formula_one: FormulaOne) -> FormulaOne:
        formula_one.save()
        return formula_one

    def update(self, formula_one: FormulaOne) -> FormulaOne:
        formula_one.save()
        return formula_one

    def delete(self, formula_one: FormulaOne) -> FormulaOne:
        formula_one.delete()
        return formula_one

    def get_all(self) -> List[FormulaOne]:
        return FormulaOne.objects.all()  # type: ignore
