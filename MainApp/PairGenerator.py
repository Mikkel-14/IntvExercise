from abc import ABC, abstractmethod


class PairGenerator(ABC):
    @abstractmethod
    def generate(self, items):
        pass


class EmployeePairGenerator(PairGenerator):
    def generate(self, items):#O(n^2)
        pairs = list()
        for idx in range(0, len(items)-1):
            employee_one = items[idx]
            new_pairs = [(employee_one, emp_two) for emp_two in items[idx+1:]] #O(n-1) worst case
            pairs.extend(new_pairs)
        return pairs

