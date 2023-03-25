import unittest

from classes.bus import Bus
from classes.truck import Truck
from classes.car import Car


class TestVehicles(unittest.TestCase):
    def test_count_cargo(self):
        truck = Truck()
        self.assertEqual((7, 5), truck.count_trips_for_cargo_transfer(cargo_weight=109,
                                                                      truck_transfer_weight=10,
                                                                      trailer_transport_weight=8))
        self.assertEqual((3, False), truck.count_trips_for_cargo_transfer(cargo_weight=36,
                                                                          truck_transfer_weight=12,
                                                                          trailer_transport_weight=6))
        self.assertEqual((2, 2), truck.count_trips_for_cargo_transfer(cargo_weight=109,
                                                                      truck_transfer_weight=12,
                                                                      trailer_transport_weight=50))
        self.assertTrue(True, truck.have_trailer)
        self.assertEqual((2, 1), truck.count_trips_for_cargo_transfer(cargo_weight=70,
                                                                      truck_transfer_weight=10,
                                                                      trailer_transport_weight=50))
        self.assertEqual((1, 1), truck.count_trips_for_cargo_transfer(cargo_weight=100,
                                                                      truck_transfer_weight=50,
                                                                      trailer_transport_weight=50))
        self.assertEqual(False, truck.next_insurance_technical_inspection_date(checking='insurance',
                                                                               inspection_or_insurance='2024-01-01'))
        self.assertEqual(True, truck.next_insurance_technical_inspection_date(
            checking='inspection', inspection_or_insurance='2023-02-24'))

    def test_count_transfer_passenger(self):
        truck = Truck()
        bus = Bus(passenger_number=452, bus_seats=9)
        self.assertEqual(51, bus.count_bus_transfer_passenger())
        self.assertNotEqual(45, bus.count_bus_transfer_passenger())
        self.assertIsInstance(bus, Bus, bus.count_bus_transfer_passenger())
        self.assertNotIsInstance(bus, Truck, truck.variable_cost_per_km(fuel_consumptions=2,
                                                                        fuel_price=3, trip_km=8))

    def test_transport_cost_passenger(self):
        bus = Bus()
        self.assertEqual(25594.4, bus.transport_costs_passenger_transfer(trip_km=12200,
                                                                         fuel_price=2.22,
                                                                         fuel_consumptions=18.9))
        self.assertEqual(208.1, bus.variable_cost_per_km(fuel_consumptions=12, fuel_price=2.99,
                                                         trip_km=580))
        self.assertEqual(330.05, bus.transport_costs_passenger_transfer(trip_km=999,
                                                                        fuel_price=2.99,
                                                                        fuel_consumptions=2.21))

    def test_car_methods(self):
        car = Car()
        self.assertEqual(False, car.driver_vacation(duration_vacation=30,
                                                  vacation_start='2022-01-01'))
        self.assertIsInstance(car, Car, car.driver_vacation())
        self.assertEqual(10.94, car.variable_cost_per_km(fuel_consumptions=2.22,
                                                           fuel_price=2.22, trip_km=222))
        self.assertIsInstance(car, Car, car.variable_cost_per_km(trip_km=1, fuel_price=1,
                                                                 fuel_consumptions=4))
