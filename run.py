from web3 import Web3
import math
import abi
import dotenv, os, sys


MIN_BALANCE = 0.01
   
dir_path = os.path.dirname(os.path.realpath(__file__))
dotenv.load_dotenv(dir_path+'/.env')

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

try:
    address = web3.toChecksumAddress(os.environ['ADDRESS'])
    balance = web3.eth.getBalance(os.environ['ADDRESS'])
    balance = web3.fromWei(balance, 'ether')
except:
    print('Set correct dir_path value')
    sys.exit()
    
contract_adres = web3.toChecksumAddress("0xFFE811714ab35360b67eE195acE7C10D93f89D8C")
contract = web3.eth.contract(address=contract_adres, abi=abi.ABI)
 

def send_transaction():      
    nonce = web3.eth.get_transaction_count(address)
    
    tx = contract.functions.roll().buildTransaction({
        'nonce': nonce,
        'gas': 2500000,
        'gasPrice': web3.toWei('5','gwei'),
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=os.environ['KEY'])
    txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    with open(dir_path+'/log.txt','a') as file:
        file.write(f" TX: {web3.toHex(txn)}\n")


def main():
    
    if balance < MIN_BALANCE:
        # print('balance BNB too small')
        sys.exit()     
        
    send_transaction()


if __name__ == "__main__":
    main()
    