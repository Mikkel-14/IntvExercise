from FileManager.File import PlainTextFile
from FileManager.Parser import PlainTextParser


def main(argv):
    if len(argv) <= 1:
        return "Employee file missing"
    file_path = argv[1]
    file = PlainTextFile(file_path, PlainTextParser())
    file.get_contents()
    try:
        employee_info = file.parse()
    except ValueError:
        return "Unrecognized format"

    return employee_info
