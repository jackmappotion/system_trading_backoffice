from django.db import models

# Create your models here.
from .service.broker import get_dart_broker, get_ki_broker


class KI_CONTROLLER:
    def __init__(self) -> None:
        self.ki_broker = get_ki_broker()
