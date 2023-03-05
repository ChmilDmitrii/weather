import ipinfo

import config
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def get_gps_coordinates() -> Coordinates:
    """ Возвращает текущие координаты используя IP-адресс """

    handler = ipinfo.getHandler(config.access_token)
    details = handler.getDetails()

    longitude = details.longitude
    latitude = details.latitude

    return Coordinates(longitude=longitude, latitude=latitude)
