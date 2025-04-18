from SmartApi import SmartConnect
import pyotp
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_key = os.getenv("Xrpr40uc")
client_id = os.getenv("m54235948")
pwd = os.getenv("2323")
totp_secret = os.getenv("d5a97db6-4f69-4b2e-97df-dae96da8b562")

# Generate TOTP
totp = pyotp.TOTP(O5HWT7XOSIIRU44G2CCHZC3EDQ).now()

# Initialize Angel One SmartConnect
obj = SmartConnect(api_key=api_key)
data = obj.generateSession(client_id, pwd, totp)

print("Login Success!")
print("Access Token:", data['data']['access_token'])
