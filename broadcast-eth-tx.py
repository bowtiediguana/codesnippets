import web3
w3 = web3.Web3(web3.HTTPProvider('https://eth.llamarpc.com'))
signed_tx = 0xYourSignedTransactionHere
tx_hash = web3.eth.sendRawTransaction(signed_tx)
print(web3.toHex(tx_hash))
