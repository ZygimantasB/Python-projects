from datetime import datetime, timedelta


class Vehicle:
    def __init__(self, total_km, years_owned, car_bar_plate, fuel_type,
                 driver_license, vehicle_annual_expenses, next_insurance_date):
        self.total_km = total_km
        self.years_owned = years_owned
        self.bus_bar_plate = car_bar_plate
        self.fuel_type = fuel_type
        self.driver_license = driver_license
        self.vehicle_annual_expenses = vehicle_annual_expenses
        self.next_insurance_date = next_insurance_date

    def variable_cost_per_km(self, fuel_price, trip_km, fuel_consumptions) -> float:
        """
        Variable costs per kilometer are calculated based on the bus's gasoline consumption
        and its volume of fuel.
        """
        return round(fuel_price * fuel_consumptions / 100 * trip_km, 2)

    def expenses_per_yearly_per_km(self):
        return self.vehicle_annual_expenses / self.total_km

    def next_insurance_technical_inspection_date(self, inspection_or_insurance: str,
                                                 checking: str):
        """
        Determines if insurance is required in the next month based on the current date and the
        expiration date of the current insurance.
        """
        today = datetime.now()
        next_month = today.replace(day=28) + timedelta(days=3)
        next_month = next_month.replace(day=1)
        if checking.casefold() in 'insurance':
            if datetime.strptime(inspection_or_insurance,'%Y-%m-%d') < next_month:
                return True
        else:
            if datetime.strptime(inspection_or_insurance, '%Y-%m-%d') < next_month:
                return True
        return False
