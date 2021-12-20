from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, obj):
        with open(self.file_path, 'a') as file:
            file.write(obj)
            file.write('\n')

class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)

class LoggersFactory:
    def __init__(self, environment='dev', logs_file_path=None):
        self.logger = None
        self.logs_file_path = logs_file_path
        self.environment = environment
        self.__init_logger()


    def get(self):
        return self.logger


    def __init_logger(self):
        if self.environment == 'prod':
            self.logger = StdoutLogger()
        self.logger = FileLogger(self.logs_file_path)


loggers_factory = LoggersFactory()

print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
print(loggers_factory.get())
