from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, path, parse_algorithm):
        self.path = path
        self.parse_algorithm = parse_algorithm

    @abstractmethod
    def get_contents(self):
        pass

    def parse(self):
        return self.parse_algorithm.parse(self.get_contents())


class PlainTextFile(File):
    def __init__(self, path, parse_algorithm):
        super().__init__(path, parse_algorithm)

    def get_contents(self):
        contents = list()
        with open(self.path) as file:
            for line in file:
                contents.append(line.strip('\n'))
            return contents
