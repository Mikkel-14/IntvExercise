from abc import ABC, abstractmethod
import re
from .const import DAYS


class Parser(ABC):
    @abstractmethod
    def parse(self, info):
        pass


class PlainTextParser(Parser):
    RE_EXP = r'[A-Z]+=((MO|TU|WE|TH|FR|SA|SU)[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2},?)+'

    def parse(self, info):
        if len(info) == 0:
            raise ValueError("Unrecognized format")
        if re.match(self.RE_EXP, info[0]) is None:
            raise ValueError("Unrecognized format")
        employee_info = dict()
        for line in info:
            parts = line.split('=')
            employee_name, employee_schedule = parts[0], parts[1]
            days = [(None, None) for x in range(DAYS.MO, DAYS.SU + 1)]
            schedule_days = employee_schedule.split(',')
            for day in schedule_days:
                day_name = day[0:2]
                start_hour, start_frac = int(day[2:4]), int(day[5:7]) / 60
                end_hour, end_frac = int(day[8:10]), int(day[11:]) / 60
                days[DAYS[day_name]] = (start_hour + start_frac, end_hour + end_frac)
            employee_info[employee_name] = days

        return employee_info
