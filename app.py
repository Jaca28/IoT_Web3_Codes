##Script de ejecución de la función transacción: Con la llave privada del medidor se firman las transacciones para subir a la blockchain los datos de hash de códigos del medidor, energía y estampa de tiempo 

import json
#Import web3 lib and connect with infura node
from web3 import Web3
def trans(var1, e1, x1):
 print("app.py Corriendo.....")
 infura_url = "https://rinkeby.infura.io/v3/162c6026989446e08fb54b3fe3888f12"
 web3 = Web3(Web3.HTTPProvider(infura_url))
 print ("Conectado con Infura: " + str(web3.isConnected()))
 #Public key
 account = web3.toChecksumAddress("0x186a991219b1ccC102e187446b27e3C70Fc696aB")
 #Private Key
 private_key = "90e30661c3b65ea1decdf51d55923e4a0069f596a678ffcfbeb965e1c769cf89"
 abi = json.loads('[{"constant":true,"inputs":[],"name":"longitud_medidas","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_hash_medidor","type":"string"},{"name":"_energia","type":"uint256"},{"name":"_tiempo","type":"string"}],"name":"nueva_medida","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"uint256"}],"name":"pk2medidas","outputs":[{"name":"ID","type":"uint256"},{"name":"hash_medidor","type":"string"},{"name":"energia","type":"uint256"},{"name":"tiempo","type":"string"},{"name":"pk_medidor","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"pk2cuenta_medidas","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"medidas","outputs":[{"name":"ID","type":"uint256"},{"name":"hash_medidor","type":"string"},{"name":"energia","type":"uint256"},{"name":"tiempo","type":"string"},{"name":"pk_medidor","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
 contractAddress = web3.toChecksumAddress("0xe7357d40168d23b15e7c5516b5304680aac5a358")
 #print (web3.isAddress('0x341401DCe923952ec27D9D890c4d7956947EC619'))
 contract = web3.eth.contract(address=contractAddress, abi=abi)
 print ("Contrato instanciado: " + str(contract) + "****")
 #Aleatory data generation
 #  var = uuid.uuid4().hex
 #  var1 = str(var)
 #  x = datetime.datetime.now()
 #  x1 = str(x)

 print ("Nuevo hash en app: " + var1)
 print ("Nuevo dato de energía en app: " + str(e1))
 print ("Nuevo tiempo en app: " + x1)

 #contract.functions.newHash(var1).transact()
 nonce = web3.eth.getTransactionCount(account)
 data_tx = contract.functions.nueva_medida(var1, e1, x1).buildTransaction({
    #'chainId': 0x1,
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'nonce': nonce,
    })

 print(data_tx)
 # Sign transaction
 signed_tx = web3.eth.account.signTransaction(data_tx, private_key=private_key)
 signed_tx.rawTransaction
 #Broadcast transaction
 tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
 #web3.eth.sendRawTransaction(signed_tx.rawTransaction)
 print ("Hash de la transacción: " + str(web3.toHex(tx_hash)))
