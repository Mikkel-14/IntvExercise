from abc import ABC, abstractmethod


class OutPutter(ABC):
    @abstractmethod
    def format(self, data):
        pass


class StringOutPutter(OutPutter):
    def format(self, data):
        if data == dict():
            return "No coincident employees were found!"
        response_strings = list()
        for key in list(data.keys()):
            response_strings.append(f'{key}: {data[key]}')
        return ','.join(response_strings)
