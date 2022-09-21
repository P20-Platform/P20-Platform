import tkinter
from tkinter import font as tkfont



def zohoConnect():
    zohoAPIKey = float(input("Voer uw Zoho API Key in: \n"))
    print("Zoho Connect Started")
    if zohoAPIKey == 0:
        return "Error, no API key/secret specified."
    else:
        print("Key Provided, Continuing...")

def zohoSend():
    print("Zoho API Response OK. Sending data...")

def zohoSubmitted():
    print("Submit Zoho button pressed. Submitting...")
    # Go to next frame through this file, and get the stringvars value, send those to assigned values in Zoho Contacts.