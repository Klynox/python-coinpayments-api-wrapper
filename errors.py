class CoinpaymentError(Exception):
    """
    SDK Error
    """
    pass


class MissingAuthKeyError(CoinpaymentError):
    """
    We can't find the authentication key
    """
    pass


class ImproperlyConfigured(CoinpaymentError):
    """
    Invalid coinpayments configuration details
    """


class InvalidMethodError(CoinpaymentError):
    """
    Invalid or unrecoginised/unimplemented HTTP request method
    """
    pass


class InvalidDataError(CoinpaymentError):
    """
    Invalid input recognised. Saves unecessary trip to server
    """
    pass
