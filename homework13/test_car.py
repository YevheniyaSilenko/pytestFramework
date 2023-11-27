import pytest
from car import Car  # Import the Car class from your project's structure

def test_initial_miles_limit():
    car = Car("Toyota", "Corolla", 200)
    assert car.miles_limit == 200

def test_start_and_stop_engine():
    car = Car("Honda", "Accord")
    assert car.start_engine() == "Engine started."
    assert car.stop_engine() == "Engine stopped."

def test_drive_when_engine_is_off():
    car = Car("Ford", "Focus", 100)
    assert car.drive(50) == "Cannot drive. Engine is off."

def test_drive_within_miles_limit():
    car = Car("Chevrolet", "Malibu", 150)
    car.start_engine()
    assert car.drive(100) == "Driving 100 miles."
    assert car.miles_limit == 50

def test_drive_exceeding_miles_limit():
    car = Car("Nissan", "Sentra", 50)
    car.start_engine()
    assert car.drive(60) == "The miles limit has been exceeded"

def test_start_engine_when_already_running():
    car = Car("Mazda", "CX-5")
    car.start_engine()
    assert car.start_engine() == "Engine is already running."

def test_stop_engine_when_already_off():
    car = Car("Kia", "Optima")
    assert car.stop_engine() == "Engine is already off."

def test_drive_when_engine_is_off_then_started():
    car = Car("Subaru", "Outback", 100)
    assert car.drive(30) == "Cannot drive. Engine is off."
    car.start_engine()
    assert car.drive(50) == "Driving 50 miles."
    assert car.miles_limit == 50

def test_drive_when_engine_is_off_then_started_and_stopped():
    car = Car("Volkswagen", "Jetta", 100)
    assert car.drive(30) == "Cannot drive. Engine is off."
    car.start_engine()
    car.stop_engine()
    assert car.drive(40) == "Cannot drive. Engine is off."

def test_drive_when_engine_is_on_and_off_multiple_times():
    car = Car("Hyundai", "Elantra", 200)
    car.start_engine()
    car.stop_engine()
    car.start_engine()
    assert car.drive(150) == "Driving 150 miles."
    assert car.miles_limit == 50

if __name__ == '__main__':
    pytest.main()
