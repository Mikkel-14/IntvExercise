import sys
from MainApp.StartApp import main
from MainApp.EmployeeRoster import EmployeeRoster
from MainApp.PairGenerator import EmployeePairGenerator
from MainApp.OutPutter import StringOutPutter

result = main(sys.argv)
if isinstance(result, str):
    print(result)
else:
    coincidences = EmployeeRoster(result).compute_coincident_employees(EmployeePairGenerator())
    print(StringOutPutter().format(coincidences))
