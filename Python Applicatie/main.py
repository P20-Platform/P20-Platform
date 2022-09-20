import tkinter as tk
from zohoAPI import zohoConnect, zohoSend
from handmatigInput import handmatigeInput


def main():
    print("Platform-20 IP Debug Console Started.")
    username = handmatigeInput("Gebruikersnaam: \n")
    password = handmatigeInput("Wachtwoord: \n")
    ## for future authentication method.


    
    startButton = tk.Button(text="Start", command=StartWindowNext)
    startButton.pack()
    tk.Tk()
    

def StartWindowNext(): # enter next Tk frame for menu.
    print("Start Button Pressed.")


def zohoDataSendButtonPressed(): # When the send data button is pressed, clean the values and send the data to the Zoho API.
    zohoConnect()
    zohoSend()

main()