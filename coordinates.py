import ipinfo
import config

from dataclasses import dataclass
from requests.exceptions import HTTPError
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    longitude: float
    latitude: float


def _get_ipinfo_coordinates() -> Coordinates:
    handler = ipinfo.getHandler(config.ACCESS_TOKEN)
    try:
        details = handler.getDetails()
    except HTTPError:
        raise CantGetCoordinates
    latitude = float(details.latitude)
    longitude = float(details.longitude)
    return Coordinates(longitude=longitude, latitude=latitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 1),
        [coordinates.longitude, coordinates.latitude]
    ))


def get_gps_coordinates() -> Coordinates:
    """ Возвращает текущие координаты используя IP-адресс """
    coordinates = _get_ipinfo_coordinates()
    return _round_coordinates(coordinates)
