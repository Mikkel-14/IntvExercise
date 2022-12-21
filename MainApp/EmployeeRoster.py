from .PairGenerator import PairGenerator


class EmployeeRoster:
    def __init__(self, roster_list):
        self.roster_list = roster_list

    def compute_coincident_employees(self, pair_generator: PairGenerator):
        coincident_employees = dict()
        pairs = pair_generator.generate(list(self.roster_list.keys()))
        for pair in pairs:
            employee_a = pair[0]
            employee_b = pair[1]
            schedule_a = self.roster_list[employee_a]
            schedule_b = self.roster_list[employee_b]
            coincidences = 0
            for day in zip(schedule_a, schedule_b):
                if day[0] == (None, None) or day[1] == (None, None):
                    continue
                else:
                    interval_a = day[0]
                    interval_b = day[1]
                    is_a_in_b = (interval_a[0] - interval_b[0] >= 0) and (interval_b[1] - interval_a[1] >= 0)
                    is_b_in_a = (interval_b[0] - interval_a[0] >= 0) and (interval_a[1] - interval_b[1] >= 0)
                    is_a_over_b = interval_b[1] >= interval_a[1] > interval_b[0]
                    is_b_over_a = interval_a[1] >= interval_b[1] > interval_a[0]
                    are_coincident_intervals = is_a_in_b or is_b_in_a or is_a_over_b or is_b_over_a
                    if are_coincident_intervals:
                        coincidences += 1
            if coincidences > 0:
                coincident_employees[f'{employee_a}-{employee_b}'] = coincidences
        return coincident_employees
