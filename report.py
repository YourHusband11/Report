import requests

def get_instagram_details(username):
    # Hypothetical endpoint to fetch user details
    url = f"https://api.instagram.com/user/{username}"

    # Headers, including authentication tokens if necessary
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }

    # Send the request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch details for {username}. Status code: {response.status_code}, Response: {response.text}")
        return None

def report_instagram_account(username, details):
    # Hypothetical reporting endpoint
    url = "https://api.instagram.com/report/user"

    # Headers, including authentication tokens if necessary
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }

    # Payload containing the report details
    payload = {
        "username": username,
        "reason": "Spam or fake account",
        "description": f"This account is engaging in spam activities. Details: {details}"
    }

    # Send the report
    response = requests.post(url, json=payload, headers=headers)

    # Check the response
    if response.status_code == 200:
        print(f"Successfully reported the account {username}.")
    else:
        print(f"Failed to report the account {username}. Status code: {response.status_code}, Response: {response.text}")

def main():
    username = input("Enter the Instagram username to report: ")
    details = get_instagram_details(username)

    if details:
        print(f"Details for {username}: {details}")
        report_instagram_account(username, details)
    else:
        print("Could not fetch details for the account. Please check the username and try again.")

if __name__ == "__main__":
    main()
