from math import ceil
from classes.vehicles import Vehicle


class Truck(Vehicle):
    def __init__(self, vehicle_annual_expenses: float=12000, have_trailer: bool = True,
                 total_km: int = 102540, years_owned: int = 2, car_bar_plate: str = 'TRS852',
                 fuel_type: str = 'Diesel', driver_license: str = 'D', fuel_consumptions: float =
                 31.9):
        super().__init__(total_km, years_owned, car_bar_plate, fuel_type,
                         driver_license, fuel_consumptions, vehicle_annual_expenses)
        self.have_trailer = have_trailer

    def can_drive_truck_with_trailer(self, driver_license) -> bool:
        """
        Checks whether the driver has the necessary licenses to drive the vehicle
        """
        return True if self.driver_license in 'D' == driver_license else False

    def count_trips_for_cargo_transfer(self, truck_transfer_weight: float = 8,
                                       trailer_transport_weight: float = 10, cargo_weight:
            float = 109) -> tuple:
        """
        Calculates how we can most efficiently transport our cargo with and without a trailer
        """
        truck, trailer = 0, 0

        trips_without_trailer = cargo_weight / truck_transfer_weight
        trips_with_trailer = ceil(cargo_weight / (trailer_transport_weight +
                                                  truck_transfer_weight))

        if trailer_transport_weight != truck_transfer_weight:
            if trips_without_trailer == trips_with_trailer:
                return trips_without_trailer, False
            elif cargo_weight % (trailer_transport_weight + truck_transfer_weight) == 0:
                trips_with_trailer = ceil((cargo_weight / (trailer_transport_weight +
                                                           truck_transfer_weight) + 0.1))
                if trips_without_trailer == trips_with_trailer:
                    return trips_without_trailer, False

        if trailer_transport_weight > truck_transfer_weight:
            while cargo_weight > 0:
                if truck_transfer_weight >= cargo_weight:
                    cargo_weight -= truck_transfer_weight
                    truck += 1
                elif trailer_transport_weight > truck_transfer_weight:
                    cargo_weight -= (truck_transfer_weight + trailer_transport_weight)
                    truck += 1
                    trailer += 1

        while cargo_weight >= 0 and cargo_weight >= trailer_transport_weight:
            if cargo_weight < truck_transfer_weight:
                cargo_weight -= truck_transfer_weight
                truck += 1
            elif cargo_weight >= 0 or cargo_weight >= trailer_transport_weight:
                cargo_weight -= truck_transfer_weight
                truck += 1
                if cargo_weight <= 0:
                    break
            if cargo_weight >= (truck_transfer_weight + trailer_transport_weight):
                cargo_weight -= trailer_transport_weight
                trailer += 1
            elif 0 <= cargo_weight <= trailer_transport_weight:
                cargo_weight -= trailer_transport_weight
                trailer += 1

        return truck, trailer
