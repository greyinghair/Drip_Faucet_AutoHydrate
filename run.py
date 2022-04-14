from web3 import Web3
import math
import abi, config
import dotenv, os, sys, time


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

with open(dir_path+'round.txt') as f:
    no_round = int(f.readline())

def hydrate():
    nonce = web3.eth.get_transaction_count(address)
    
    tx = contract.functions.roll().buildTransaction({
        'nonce': nonce,
        'gas': 500000,
        'gasPrice': web3.toWei('5','gwei'),
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key=os.environ['KEY'])
    txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    with open(dir_path+'/log.txt','a') as file:
        file.write(f"{time.strftime(format('%d.%m %H:%M'))} Hydrate TX: {web3.toHex(txn)}\n")

def claim():
    nonce = web3.eth.get_transaction_count(address)
       
    tx = contract.functions.claim().buildTransaction({
        'nonce': nonce,
        'gas': 500000,
        'gasPrice': web3.toWei('5','gwei'),
    })
    
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=os.environ['KEY'])
    txn = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    with open(dir_path+'/log.txt','a') as file:
        file.write(f"{time.strftime(format('%d.%m %H:%M'))} Claim TX: {web3.toHex(txn)}\n")

def update_round():
    global no_round
    no_round += 1
    with open(dir_path+'round.txt', 'w') as f:
        f.write(f'{no_round}\n')
         
def main():
    global no_round
    
    if balance < config.MIN_BALANCE:        
        with open(dir_path+'/log.txt','a') as file:
            file.write(f"{time.strftime(format('%d.%m %H:%M'))} BNB balance too low {balance}\n")
        sys.exit()
        
    try:        
        if (no_round % config.PERIOD == 0):            
            claim()          
            update_round()
        else:            
            hydrate()
            update_round()
    except:        
        hydrate()
        update_round()


if __name__ == "__main__":
    main()
