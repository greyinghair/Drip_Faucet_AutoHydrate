Buy some VPS or Raspberry Pi to run script 24 hours per day, then follow steps below

1. `pip install -r requirements.txt`

2. create .env file 
    - `touch .env`

3. paste to the .env file yours wallet address and private key for this address
    - `ADDRESS=0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
    - `KEY=0xVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV`

4. use crontab to run script automatically once a day 00:00
   - `crontab -e`
   - `0 0 * * * python3 /PATH_TO_FILE/run.py`

5. Configure:   
   - MIN_BALANCE = 0.01  # minimum account BNB balance below which stop compound

If this is helpful, send me an airdrop for beer:
 0x74ABf1db8c8b45aD529Bd3012bE1990F605360D6