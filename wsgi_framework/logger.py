import os


class SingletonMeta(type):
    """
    За основу взят пример из https://refactoring.guru/ru/design-patterns/singleton/python/example#example-0--main-py
    Разница в названии ключа хранилища объектов: наименование логгера
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        if instance.name not in cls._instances:
            cls._instances[instance.name] = instance
        return cls._instances[instance.name]


class Logger(metaclass=SingletonMeta):
    def __init__(self, name, logs_dir):
        self.name = name
        self.logs_dir = logs_dir
        self.handlers = []

    def set_handler(self, handler):
        self.handlers.append(handler)

    def _log(self, log_record):
        for each in self.handlers:
            each.handle(log_record)  # don't forget to implement handle func for handler

    def info(self, log_record):
        log_record = 'INFO: ' + log_record
        self._log(log_record)

    def debug(self, log_record):
        log_record = 'DEBUG: ' + log_record
        self._log(log_record)

    def error(self, log_record):
        log_record = 'ERROR: ' + log_record
        self._log(log_record)

    def warning(self, log_record):
        log_record = 'WARNING: ' + log_record
        self._log(log_record)


class FileHandler:
    def __init__(self, filename, logs_dir, mode='a'):
        self.filename = filename
        self.mode = mode
        self.logs_dir = logs_dir

    def handle(self, log_record):
        with open(os.path.join(self.logs_dir, '{}.log'.format(self.filename)), self.mode) as f:
            f.write(log_record)
