from web3 import Web3
infura_url = "https://rinkeby.infura.io/v3/162c6026989446e08fb54b3fe3888f12"
web3 = Web3(Web3.HTTPProvider(infura_url))
print ("Conectado con Infura: " + str(web3.isConnected()))

account_1 = web3.toChecksumAddress("0x341401DCe923952ec27D9D890c4d7956947EC619")
account_2 = web3.toChecksumAddress("0x3066e155B42F8BBc4448dF1F9f46e29F2901C271")

private_key = "510EA21CF6534188791B3F1A4FD90FFCC4A7B6899460F698C081C8537D7FEC74"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print (web3.toHex(tx_hash))