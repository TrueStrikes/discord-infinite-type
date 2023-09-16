import requests
import time

# Define the headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "yourusertokengoeshere",
    "Content-Length": "0",
}

# Infinite loop to send the request every second
while True:
    try:
        response = requests.post("https://discord.com/api/v9/channels/ get rid of the spaces and fill in your channel id here /typing", headers=headers)
        if response.status_code == 204:
            print("Typing indicator sent successfully.")
        else:
            print(f"Failed to send typing indicator. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Sleep for one second before sending the next request
    time.sleep(1)
