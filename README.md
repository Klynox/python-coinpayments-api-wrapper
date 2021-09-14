# pycoinpayments
================================

Overview
--------
Python API client for the `CoinPayments <https://www.coinpayments.net>`

Note: This is not the official python client for the Coinpayments API

Documentation
-------------

Please see https://www.coinpayments.net/api.php for the most up-to-date documentation for the Paystack API.

# Installation

pip install pycoinpayments

# Example
You can take a look at the `sample.py` file provided in the repo.

A basic usage would be:
```python
from pycoinpayments.coinpayments import CoinPayments

create_transaction_params = {
    'amount': 10,
    'currency1': 'USDT.BEP20',
    'currency2': 'USDT.BEP20',
    'buyer_email': 'confiyobo@gmail.com'
}
cp = CoinPayments(
    'PrivateKey',
    'PublicKey')

transaction = cp.create_transaction(create_transaction_params)

if transaction['error'] == 'ok':
    print(transaction['amount'])
    print(transaction['address'])
else:
    print(transaction['error'])
```
