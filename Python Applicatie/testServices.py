from cgi import test
from email.mime import base
from socket import has_dualstack_ipv6
from handmatigInput import handmatigeInput
from zohoAPI import zohoConnect
import main

def testHandmatigeInput():
    baseValue = str(input("Voer Willekeurige letter in: \n"))
    returnValue = handmatigeInput("Voer nogmaals uw gekozen willekeurige letter in: \n")
    if returnValue == baseValue:
        print("Test Passed. OK!")
        handmatigeInputTestResult = str("ok")
        return handmatigeInputTestResult

def testZohoConnect():
    zohoConnect(float(input("Voer API Key in.")))




def testAll():
    testHandmatigeInput()
    testZohoConnect()

selectedTest=int(input("Selecteer test: \n 1. test handmatige input functies. \n 2. test Zoho API connectie. \n 3. test alle functies. \n Voer getal in: "))
if selectedTest == 1:
    testHandmatigeInput()
if selectedTest == 2:
    testZohoConnect()
if selectedTest == 3:
    testAll()


