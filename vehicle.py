from employee import Employee


class Vehicle:
    def __init__(
        self, make: str, model: str, year: int, license: str, horsepower: float
    ):
        self.make = make
        self.model = model
        self.year = year
        self.license = license
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.make} {self.model} ({self.year}), License: {self.license}"

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")


# Implementation of inheritance
class Bus(Vehicle):
    def __str__(self):
        return f"{self.make} {self.model} ({self.year}), License: {self.license}, Type: Bus"

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        license: str,
        horsepower: float,
        driver=None,
    ):
        super().__init__(make, model, year, license, horsepower)

        # Bus has a driver, which is an instance of Employee (aggregation)
        self.driver = None

    # Assign driver to bus
    def assign_driver(self, driver):
        self.driver = driver

    def unassign_driver(self):
        self.driver = None

    def start(self):
        if self.driver:
            print(
                f"{self.make} {self.model} is starting with driver {self.driver.name}."
            )
        else:
            print(f"{self.make} {self.model} is starting without a driver.")

    def stop(self):
        if self.driver:
            print(
                f"{self.make} {self.model} is stopping with driver {self.driver.name}."
            )
        else:
            print(f"{self.make} {self.model} is stopping without a driver.")


bus = Bus("Toyota", "Coaster", 1969, "EGN6754", 150)

is_instance = isinstance(bus, Vehicle)
if is_instance:
    print("Is bus an instance of Vehicle?", "yes")
else:
    print("Is bus an instance of Vehicle?", "no")

# Employee object is created and exists independently
driver = Employee("Charon", 20, 2000.0)
bus.assign_driver(driver)
bus.start()
bus.stop()

# Bus start() and stop() can be called independently without a driver
bus.unassign_driver()
bus.start()
bus.stop()
