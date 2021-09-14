from pycoinpayments import CoinPayments

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

post_params1 = {
    'txid': transaction['txn_id'],
}
transactionInfo = cp.get_tx_info(post_params1)

if transactionInfo['error'] == 'ok':
    print(transactionInfo['amountf'])
    print(transactionInfo['payment_address'])
else:
    print(transactionInfo['error'])
