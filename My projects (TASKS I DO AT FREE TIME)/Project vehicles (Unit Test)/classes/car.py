from datetime import datetime, timedelta
from classes.vehicles import Vehicle


class Car(Vehicle):
    def __init__(self, next_insurance_date: str = '2022-01-01', vehicle_annual_expenses: float =
    12255.01,
                 total_km: int = 100, years_owned: int = 2, car_bar_plate: str = 'TRE741',
                 fuel_type: str = 'Electric', driver_license: str = 'B'):
        super().__init__(total_km, years_owned, car_bar_plate, fuel_type, driver_license,
                         vehicle_annual_expenses, next_insurance_date)

    def driver_vacation(self, vacation_start: str = '2021-01-01', duration_vacation: int = 30) \
            -> str:
        start_date = datetime.strptime(vacation_start, '%Y-%m-%d')
        end_date = start_date + timedelta(days=duration_vacation)
        return True if (start_date <=
                        datetime.now() <= end_date) else False
