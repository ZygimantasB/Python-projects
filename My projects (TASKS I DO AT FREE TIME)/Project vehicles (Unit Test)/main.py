from classes.bus import Bus
from classes.car import Car
from classes.driver import Driver
from classes.truck import Truck
from classes.vehicles import Vehicle


print('\nTruck\n')
driver = Driver()

vehicle = Vehicle(total_km=12540, years_owned=2, car_bar_plate='TRE741',
                  fuel_type='Diesel',
                  driver_license='B', vehicle_annual_expenses=12000.01,
                  next_insurance_date='2022-01-01')

truck = Truck(have_trailer=True, total_km=102540, vehicle_annual_expenses=12000)

print(truck.variable_cost_per_km(fuel_price=2.99, trip_km=801, fuel_consumptions=22.2))
print(truck.count_trips_for_cargo_transfer(cargo_weight=109, truck_transfer_weight=10,
                                           trailer_transport_weight=8))
print(truck.next_insurance_technical_inspection_date(inspection_or_insurance='2023-01-01',
                                                     checking='inspection'))
print(truck.next_insurance_technical_inspection_date(inspection_or_insurance='2024-01-01',
                                                     checking='insurance'))
print(truck.can_drive_truck_with_trailer(driver_license='D'))
print(truck.can_drive_truck_with_trailer(driver_license='E'))
print(driver.driver_vacation(duration_vacation=30, driver_vacation_start='2022-01-01'))

print('\nCar\n')

car = Car()

print(car.next_insurance_technical_inspection_date(inspection_or_insurance='2023-01-01',
                                                   checking='insurance'))
print(car.variable_cost_per_km(fuel_price=1.01, trip_km=250, fuel_consumptions=2.22))
print(car.driver_vacation())

print('\nBus\n')

bus = Bus()

print(bus.next_insurance_technical_inspection_date(inspection_or_insurance='2023-01-01',
                                                   checking='insurance'))
print(bus.variable_cost_per_km(trip_km=500, fuel_price=2.99, fuel_consumptions=1.11))
print(bus.count_bus_transfer_passenger())
print(bus.transport_costs_passenger_transfer(trip_km=500, fuel_price=2.99, fuel_consumptions=2.22))

print(driver.driver_vacation(driver_vacation_start='2022-01-01', duration_vacation=30))
