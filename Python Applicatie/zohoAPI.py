def zohoConnect():
    zohoAPIKey = float(input("Voer uw Zoho API Key in: \n"))
    print("Zoho Connect Started")
    if zohoAPIKey == 0:
        return "Error, no API key/secret specified."
    else:
        print("Key Provided, Continuing...")

def zohoSend():
    print("Zoho API Response OK. Sending data...")