from classes.vehicles import Vehicle
from math import ceil


class Bus(Vehicle):
    def __init__(self, vehicle_annual_expenses: float = 12000,
                 passenger_number: int = 141, bus_seats: int = 30, total_km: int = 12540,
                 years_owned: int = 2, car_bar_plate: str = 'YTR123', fuel_type: str = 'Diesel',
                 driver_license: str = 'C', fuel_consumptions: float = 22.9):

        super().__init__(total_km, years_owned, car_bar_plate, fuel_type, driver_license,
                         fuel_consumptions, vehicle_annual_expenses)
        self.passenger_number = passenger_number
        self.bus_seats = bus_seats

    def count_bus_transfer_passenger(self) -> int:
        """
        The maximum number of passengers that can be transported per trip is calculated.
        """
        return ceil(self.passenger_number / self.bus_seats)

    def transport_costs_passenger_transfer(self, fuel_price, trip_km, fuel_consumptions):
        """
        Based on the total distance driven and the bus's cost, calculates the total transport
        costs of the bus.
        """
        return round(self.variable_cost_per_km(fuel_price=fuel_price, trip_km=trip_km,
                                               fuel_consumptions=fuel_consumptions) *
                     self.count_bus_transfer_passenger(), 2)
