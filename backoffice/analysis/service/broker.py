"""
Module
Broker
    : Get Private
    : Return Broker
"""
from .private import KI_PRIVATE, DART_PRIVATE


class DART_BROKER:
    def __init__(self, dart_private) -> None:
        self.dart_private = dart_private

    def __call__(self):
        import dart_fss as dart_broker

        dart_broker.set_api_key(
            api_key=self.dart_private.get_api_key(),
        )
        return dart_broker


class KI_BROKER:
    def __init__(self, ki_private) -> None:
        self.ki_private = ki_private

    def __call__(self):
        from mojito import KoreaInvestment

        ki_broker = KoreaInvestment(
            api_key=self.ki_private.get_app_key(),
            api_secret=self.ki_private.get_app_secret(),
            acc_no=self.ki_private.get_acc_number(),
        )
        return ki_broker


def get_ki_broker():
    ki_private = KI_PRIVATE()
    ki_broker = KI_BROKER(ki_private)
    return ki_broker


def get_dart_broker():
    dart_private = DART_PRIVATE()
    dart_broker = DART_BROKER(dart_private)
    return dart_broker
