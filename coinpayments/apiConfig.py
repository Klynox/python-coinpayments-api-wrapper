import os
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import hmac
import hashlib
import json

from coinpayments.errors import (MissingAuthKeyError, ImproperlyConfigured)


class ApiConfig:
    """
    API configuration for the coinpayments SDK
    """
    _CONTENT_TYPE = "application/x-www-form-urlencoded"
    _API_END_POINT = "https://www.coinpayments.net/api.php"

    def __init__(self, private_key=None, public_key=None, ipn_url=None):
        self.ipn_url = ipn_url
        if not ipn_url:
            self.ipn_url = os.getenv(
                'COINPAYMENTS_IPN_URL', None)
        if private_key and public_key:
            self.COINPAYMENTS_PRIVATE_KEY = private_key
            self.COINPAYMENTS_PUBLIC_KEY = public_key
        else:
            self.COINPAYMENTS_PRIVATE_KEY = os.getenv(
                'COINPAYMENTS_PRIVATE_KEY', None)
            self.COINPAYMENTS_PUBLIC_KEY = os.getenv(
                'COINPAYMENTS_PUBLIC_KEY', None)

        if not self._authorization_keys_available():
            raise MissingAuthKeyError(
                "Private and public keys must be provided.")
        if ipn_url:
            if not os.getenv('COINPAYMENTS_IPN_URL', None) or \
                    not os.getenv('COINPAYMENTS_IPN_URL', None):
                raise ImproperlyConfigured(
                    'COINPAYMENTS_IPN_SECRET and COINPAYMENTS_MERCHANT_ID'
                    'are required if IPN is turned on!')

        self.request_headers = {
            "Content-Type": self._CONTENT_TYPE,
        }

    def _authorization_keys_available(self):
        return self.COINPAYMENTS_PRIVATE_KEY is not None and \
            self.COINPAYMENTS_PUBLIC_KEY is not None

    def _url(self, path):
        return self._API_END_POINT + path

    def create_hmac(self, **params):
        """
        Generate an HMAC based upon the url arguments/parameters
        We generate the encoded url here and return it to request because
        the hmac on both sides depends upon the order of the parameters, any
        change in the order and the hmacs wouldn't match
        """
        encoded = urllib.parse.urlencode(params).encode('utf-8')
        return encoded, hmac.new(
            bytearray(self.COINPAYMENTS_PRIVATE_KEY, 'utf-8'),
            encoded, hashlib.sha512).hexdigest()

    def _parse_json(self, response_obj):
        response_body = response_obj.read()
        response_body_decoded = json.loads(
            response_body)
        response_body_decoded.update(response_body_decoded['result'])
        response_body_decoded.pop('result', None)
        return response_body_decoded

    def _handle_request(self, method, url, data=None):
        """
        Generic function to handle all API url calls
        Returns a python tuple of status code, status(bool), message, data
        """
        encoded, sig = self.create_hmac(**data)
        self.request_headers['hmac'] = sig
        req = urllib.request.Request(
            url, data=encoded, headers=self.request_headers)

        try:
            response = urllib.request.urlopen(req)
            response_body_decoded = self._parse_json(response)
        except urllib.error.HTTPError as e:
            response_body = e.read()
            response_body_decoded = json.loads(
                response_body)
            return response_body_decoded
        return response_body_decoded
