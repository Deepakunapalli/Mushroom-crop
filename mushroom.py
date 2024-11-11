import datetime

class Crop:
    def _init_(self, name, growth_period_days, water_requirement_per_day):
        self.name = name
        self.growth_period_days = growth_period_days
        self.water_requirement_per_day = water_requirement_per_day
        self.planted_date = None
        self.harvest_date = None

    def plant(self, date):
        self.planted_date = date
        self.harvest_date = date + datetime.timedelta(days=self.growth_period_days)
        print(f"Planted {self.name} on {self.planted_date}. Harvest on {self.harvest_date}.")

    def water_needed(self):
        if self.planted_date is None:
            return 0
        days_until_harvest = (self.harvest_date - datetime.datetime.now().date()).days
        return days_until_harvest * self.water_requirement_per_day

    def status(self):
        if self.planted_date is None:
            return f"{self.name} is not planted."
        today = datetime.datetime.now().date()
        if today >= self.harvest_date:
            return "{self.name} is ready for harvest."
        else:
           return rf"{self.name} is growing. Days until harvest:"
