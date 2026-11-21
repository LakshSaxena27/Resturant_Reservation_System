from twilio.rest import Client

# My Twilio credentials
account_sid = "ACf01f6ff1a8c26bebd2e5c8ef02c6df27"
auth_token = "8bed64fdcdfb72c361c1be476988f74c"

# Create a client instance
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body="HIII",
    from_="+44 7307 241651",  # My Twilio phone number
    to="+44 7999 554751"      # The customer's phone number
)

print(f"Message sent! SID: {message.sid}")
