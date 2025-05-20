class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}"

    def move(self):
        pass

class Car(Transport):
    def __init__(self, brand, model, year, passenger_count):
        super().__init__(brand, model, year)
        self.passenger_count = passenger_count

    def get_info(self):
        return f"{super().get_info()}, Кількість пасажирів: {self.passenger_count}"

    def get_passenger_capacity(self):
        return self.passenger_count

    def move(self):
        return "Автомобіль їде по дорозі"

class Truck(Transport):
    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def get_info(self):
        return f"{super().get_info()}, Вантажопідйомність: {self.cargo_capacity} тонн"

    def get_cargo_capacity(self):
        return self.cargo_capacity

    def move(self):
        return "Вантажівка перевозить вантаж"

class Bike(Transport):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def get_info(self):
        return f"{super().get_info()}, Об'єм двигуна: {self.engine_volume} куб. см"

    def get_engine_volume(self):
        return self.engine_volume

    def move(self):
        return "Мотоцикл мчить трасою"

def test_transport_system():
    car = Car("Toyota", "Corolla", 2015, 5)
    truck = Truck("Volvo", "FH16", 2020, 20)
    bike = Bike("Yamaha", "YZF-R1", 2022, 1000)

    vehicles = [car, truck, bike]
    
    for vehicle in vehicles:
        print(vehicle.get_info())
        print(vehicle.move())
        print()

if __name__ == "__main__":
    test_transport_system()