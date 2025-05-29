import requests

def lookup_email_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "JailbirdX",
        "hibp-api-key": "YOUR_HIBP_API_KEY"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"status": "No breaches found."}
        else:
            return {"error": f"Error {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}
