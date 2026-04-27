class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = int(year)

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = int(doors)

    def __str__(self):
        return f" [Car] {super().__str__()} | Fuel: {self.fuel_type} | {self.doors} Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = int(max_load)
        self.axles = int(axles)

    def __str__(self):
        return f" [Truck] {super().__str__()} | Load: {self.max_load}kg | {self.axles} Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, m_type):
        super().__init__(vid, model, year)
        self.engine_cc = int(engine_cc)
        self.m_type = m_type

    def __str__(self):
        return f" [Motorcycle] {super().__str__()} | Eng: {self.engine_cc}cc | Type: {self.m_type}"

def save_fleet_to_file(vehicles, filename):
    with open(filename, "w") as f:
        for v in vehicles:
            if isinstance(v, Car):
                f.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")
            elif isinstance(v, Truck):
                f.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")
            elif isinstance(v, Motorcycle):
                f.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.m_type}\n")

def load_fleet_from_file(filename):
    fleet = []
    with open(filename, "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            if not parts or parts[0] == "":
                continue
            v_type = parts[0]
            if v_type == "Car":
                fleet.append(Car(parts[1], parts[2], parts[3], parts[4], parts[5]))
            elif v_type == "Truck":
                fleet.append(Truck(parts[1], parts[2], parts[3], parts[4], parts[5]))
            elif v_type == "Motorcycle":
                fleet.append(Motorcycle(parts[1], parts[2], parts[3], parts[4], parts[5]))
    return fleet

fleet_data = [
    Car("V501", "BMW i4", 2024, "Electric", 4),
    Truck("T888", "Scania R500", 2020, 32000, 8),
    Motorcycle("M999", "Ducati Panigale", 2025, 1103, "Sport"),
    Car("V502", "Honda Civic", 2017, "Petrol", 4),
    Truck("T889", "MAN TGX", 2023, 22000, 4),
    Motorcycle("M998", "Indian Chief", 2016, 1811, "Cruiser")
]

save_fleet_to_file(fleet_data, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
loaded_vehicles = load_fleet_from_file("fleet.txt")
print(f" {len(loaded_vehicles)} vehicles loaded successfully.")

print(" --- All Vehicles ---")
for v in loaded_vehicles:
    print(v)

print(" --- Recent Vehicles (Last 4 Years) ---")
for v in loaded_vehicles:
    if v.is_new(4):
        print(v)

print(" --- Electric Cars Only ---")
for v in loaded_vehicles:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)