If you want to support me please use my [faucet reference link](drip.community/faucet?buddy=0xf81a4D3e44Daa168cdD9a0b97AA62F528e298858).

![alt text](https://github.com/faflik/Drip_Faucet_AutoHydrate/blob/main/Diagram.png)

Buy some VPS or Raspberry Pi to run script 24 hours per day, then follow steps below

1. `pip install -r requirements.txt`

2. create .env file 
    - `touch .env`

3. paste to the .env file yours wallet address and private key for this address
    - `ADDRESS=0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
    - `KEY=0xVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV`

    If you have hardware wallet use "mnemonic code converter"
    
4. use crontab to run script automatically once a day 00:00
   - `crontab -e`
   - `0 0 * * * python3 /PATH_TO_FILE/run.py`

5. To configure edit config.py:
   - MIN_BALANCE = 0.02  # minimum account BNB balance below which stop compound and hydrate
   - PERIOD = 0         
        - 0 - hydrate every day
        - 1 - claim every day
        - e.g. 4 - claim every fourth day, hydrate on the rest

If this is helpful, send me an airdrop for beer:
 0x74ABf1db8c8b45aD529Bd3012bE1990F605360D6
 <p align="center"> 
  Visitor count<br>
  <img src="https://profile-counter.glitch.me/faucet/count.svg" />
</p>
