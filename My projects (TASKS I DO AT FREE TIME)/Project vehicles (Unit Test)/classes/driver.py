from classes.vehicles import Vehicle
from datetime import datetime, timedelta


class Driver(Vehicle):
    def __init__(self, vehicle_annual_expenses: float = 12255.01,
                 salary_per_km: float = 2.22, total_km: float = 25896, years_owned: int = 2,
                 car_bar_plate: str = 'YHN964', fuel_type: str = 'Diesel', driver_license: str = 'B',
                 fuel_consumptions: float = 8.12):
        super().__init__(total_km, years_owned, car_bar_plate, fuel_type, driver_license,
                         fuel_consumptions, vehicle_annual_expenses)
        self.salary_per_km = salary_per_km

    def driver_vacation(self, driver_vacation_start, duration_vacation) -> bool:
        """
        Checks if driver is on vacations or not
        """
        return True if (datetime.strptime(driver_vacation_start, '%Y-%m-%d') +
                        timedelta(days=duration_vacation)) >= datetime.now() else False
