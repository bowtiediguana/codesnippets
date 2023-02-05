import web3
w3 = web3.Web3(web3.HTTPProvider('https://eth.llamarpc.com'))
address = web3.Web3.toChecksumAddress('0xYourAddressHere')
nonce = w3.eth.getTransactionCount(address)
print("The current nonce for address {} is: {}".format(address, nonce))
