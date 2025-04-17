from SmartApi import SmartConnect
import pyotp
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

api_key = os.getenv("API_KEY")
client_id = os.getenv("CLIENT_ID")
pwd = os.getenv("PASSWORD")
totp_secret = os.getenv("TOTP_SECRET")

# Generate TOTP
totp = pyotp.TOTP(totp_secret).now()

# Initialize Angel One SmartConnect
obj = SmartConnect(api_key=api_key)
data = obj.generateSession(client_id, pwd, totp)

print("Login Success!")
print("Access Token:", data['data']['access_token'])
