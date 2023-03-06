class CantGetCoordinates(Exception):
    """ Программа не может получить текущие координаты """

    pass


class ApiServiceError(Exception):
    """ Программа не может получить данные от API-сервиса погоды """

    pass
