import pytest
from car import Car


@pytest.fixture
def car_with_initial_limit_200():
    return Car("Toyota", "Corolla", 200)


@pytest.fixture
def car_without_initial_limit():
    return Car("Honda", "Accord")


@pytest.fixture
def car_with_limit_100():
    return Car("Ford", "Focus", 100)


@pytest.fixture
def car_with_limit_150():
    return Car("Chevrolet", "Malibu", 150)


@pytest.fixture
def car_with_limit_50():
    return Car("Nissan", "Sentra", 50)


@pytest.fixture
def car_already_running():
    car = Car("Mazda", "CX-5")
    car.start_engine()
    return car


@pytest.fixture
def car_already_off():
    return Car("Kia", "Optima")


@pytest.fixture
def car_for_start_stop_test():
    return Car("Volkswagen", "Jetta", 100)


@pytest.fixture
def car_for_multiple_start_stop_test():
    car = Car("Hyundai", "Elantra", 200)
    car.start_engine()
    car.stop_engine()
    car.start_engine()
    return car
