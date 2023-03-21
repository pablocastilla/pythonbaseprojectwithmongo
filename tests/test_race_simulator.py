# unit test start method of the car class
import mongomock
import pytest_mock
from model import formula_one
from race_simulator import RaceSimulator
from repositories.formula_one_mongo_repository import FormulaOneMongoRepository
from mongoengine import connect


class TestFaceSimulator:
    def test_simulate_with_mocker(self, mocker: pytest_mock.plugin.MockerFixture) -> None:
        repository = mocker.patch("repositories.formula_one_repository.FormulaOneRepository")
        mocker.patch(
            "repositories.formula_one_repository.FormulaOneRepository.get_all",
            return_value=[
                formula_one.FormulaOne(car_number=44, driver_name="Lewis Hamilton"),
                formula_one.FormulaOne(car_number=14, driver_name="Fernando Alonso"),
            ],
        )

        simulator = RaceSimulator(repository)
        simulator.simulate()

        repository.get_all.assert_called_once()

    def test_simulate_with_mongomock(self) -> None:
        connect("mongoenginetest", host="mongodb://localhost", mongo_client_class=mongomock.MongoClient)
        repository = FormulaOneMongoRepository()
        repository.create(formula_one.FormulaOne(car_number=44, driver_name="Lewis Hamilton"))
        repository.create(formula_one.FormulaOne(car_number=14, driver_name="Fernando Alonso"))

        simulator = RaceSimulator(repository)
        simulator.simulate()
