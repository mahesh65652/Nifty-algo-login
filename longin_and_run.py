
# Generate TOTP
totp = pyotp.TOTP(totp_secret).now()

# Initialize SmartAPI
obj = SmartConnect(api_key=api_key)
data = obj.generateSession(client_id, pwd, totp)

print("Longin Success!")
print("Access Token:", data['data']['access_token'])
