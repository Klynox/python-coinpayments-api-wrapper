from apiConfig import ApiConfig


class CoinPayments(ApiConfig):
    def create_transaction(self, params=None):
        """
        Creates a transaction to give to the purchaser
        https://www.coinpayments.net/apidoc-create-transaction
        """
        if params is None:
            params = {}
        if self.ipn_url:
            params.update({'ipn_url': self.ipn_url})
        params.update({'cmd': 'create_transaction',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_basic_info(self, params=None):
        """
        Gets merchant info based on API key (callee)
        https://www.coinpayments.net/apidoc-get-basic-info
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_basic_info',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def rates(self, params=None):
        """
        Gets current rates for currencies
        https://www.coinpayments.net/apidoc-rates
        """
        if params is None:
            params = {}
        params.update({'cmd': 'rates',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def balances(self, params=None):
        """
        Get current wallet balances
        https://www.coinpayments.net/apidoc-balances
        """
        if params is None:
            params = {}
        params.update({'cmd': 'balances',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_deposit_address(self, params=None):
        """
        Get address for personal deposit use
        https://www.coinpayments.net/apidoc-get-deposit-address
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_deposit_address',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_callback_address(self, params=None):
        """
        Get a callback address to recieve info about address status
        https://www.coinpayments.net/apidoc-get-callback-address
        """
        if params is None:
            params = {}
        if self.ipn_url:
            params.update({'ipn_url': self.ipn_url})
        params.update({'cmd': 'get_callback_address',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def create_transfer(self, params=None):
        """
        Not really sure why this function exists to be honest, it transfers
        coins from your addresses to another account on coinpayments using
        merchant ID
        https://www.coinpayments.net/apidoc-create-transfer
        """
        if params is None:
            params = {}
        params.update({'cmd': 'create_transfer',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def create_withdrawal(self, params=None):
        """
        Withdraw or masswithdraw(NOT RECOMMENDED) coins to a specified address,
        optionally set a IPN when complete.
        https://www.coinpayments.net/apidoc-create-withdrawal
        """
        if params is None:
            params = {}
        params.update({'cmd': 'create_withdrawal',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def convert_coins(self, params=None):
        """
        Convert your balances from one currency to another
        https://www.coinpayments.net/apidoc-convert
        """
        if params is None:
            params = {}
        params.update({'cmd': 'convert',
                       'version': 1,
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_withdrawal_history(self, params=None):
        """
        Get list of recent withdrawals (1-100max)
        https://www.coinpayments.net/apidoc-get-withdrawal-history
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_withdrawal_history',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_withdrawal_info(self, params=None):
        """
        Get information about a specific withdrawal based on withdrawal ID
        https://www.coinpayments.net/apidoc-get-withdrawal-info
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_withdrawal_info',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_conversion_info(self, params=None):
        """
        Get information about a specific withdrawal based on withdrawal ID
        https://www.coinpayments.net/apidoc-get-conversion-info
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_conversion_info',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_tx_info(self, params=None):
        """
        Get single tx info
        https://www.coinpayments.net/apidoc-get-tx-info
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_tx_info',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)

    def get_tx_info_multi(self, params=None):
        """
        Get tx info (up to 25 ids separated by | )
        https://www.coinpayments.net/apidoc-get-tx-info
        """
        if params is None:
            params = {}
        params.update({'cmd': 'get_tx_info_multi',
                       'version': 1,
                       'format': 'json',
                       'key': self.COINPAYMENTS_PUBLIC_KEY})
        url = self._url('')
        return self._handle_request('POST', url, params)
