from exceptions import CantGetCoordinates, ApiServiceError


def errors_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func_result = func(*args, **kwargs)
        except CantGetCoordinates:
            print('Не смог получить координаты')
            exit(1)
        except ApiServiceError:
            print('Не смог получить данные в API-сервиса погода')
            exit(1)
        return func_result
    return wrapper
