from distutils.cmd import Command
from msvcrt import kbhit
import tkinter as tk
from tkinter import font as tkfont
from zohoAPI import zohoConnect, zohoSend, zohoSubmitted
from handmatigInput import handmatigeInput


def mainDebug():
    print("Platform-20 IP Debug Console Started.")
    username = handmatigeInput("Gebruikersnaam: \n")
    password = handmatigeInput("Wachtwoord: \n")
    ## for future authentication method.

mainDebug()


class SelectorPageBackEnd(tk.Tk):
    def __init__(self, *args, **kwargs):
        print("Selector Back-End running")
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight='bold', slant='italic')

        # Container Stack, this is where we store all the GUI Frames on top of each other. 
        # On the click of a button, we can cycle through these frames to get the needed window.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (inputGUIZoho, SubmittingPageZoho, SelectorPageFrontEnd):
            page_name = F.__name__
            frame = F(parent=container,controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SelectorPageFrontEnd")

    def show_frame(self, page_name):
        '''Show a frame for the given page name '''
        frame = self.frames[page_name]
        frame.tkraise() # tkraise perhaps not working? all windows are shown at once.

class SelectorPageFrontEnd(tk.Frame):
    def __init__(self, parent, controller):
        print("Selector Page Front-End running, waiting for switch...")
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.selectWindowButtonLabel = tk.Label(text="Select Process to execute", font=controller.title_font)
        self.selectWindowButtonLabel.pack(side="top", fill="x")

        self.selectWindowButtonZoho = tk.Button(text="Verstuur naar Zoho", command=lambda: controller.show_frame("InputGUIZoho"))
        self.selectWindowButtonZoho.pack()
            
class inputGUIZoho(tk.Frame):
    def __init__(self, parent, controller):
        print("Window Switched: input GUI Zoho.")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.labelTitleInputGUI = tk.Label(text="Handmatige Input Venster", font=controller.title_font)
        self.labelTitleInputGUI.pack(side="top", fill="x", pady=10)
        # Input Variabeles
        self.inputVeld1Value = tk.StringVar()
        self.inputVeld2Value = tk.StringVar()
        self.inputVeld3Value = tk.StringVar()
        self.inputVeld4Value = tk.StringVar()

        # Input Velden
        self.inputVeld1 = tk.Entry(textvariable=self.inputVeld1Value)
        self.inputVeld2 = tk.Entry(textvariable=self.inputVeld2Value)
        self.inputVeld3 = tk.Entry(textvariable=self.inputVeld3Value)
        self.inputVeld4 = tk.Entry(textvariable=self.inputVeld4Value)

        # Pak Input velden in window
        self.inputVeld1.pack()
        self.inputVeld2.pack()
        self.inputVeld3.pack()
        self.inputVeld4.pack()


        submitInputButton = tk.Button(self, text="Verstuur input naar Zoho", command=lambda:zohoSubmitted())

        submitInputButton.pack()


class SubmittingPageZoho(tk.Frame):
    def __init__(self, parent, controller):
        print("Window Switched: Submitting Page Zoho.")
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.submittingPleaseWaitZohoLabel = tk.Label(text="Please wait. Attempting to send input data to Zoho Servers.", font=controller.title_font)
        self.submittingPleaseWaitZohoLabel.pack(side="top", fill="x", pady=10)





# Run the app
if __name__ == "__main__":
    app = SelectorPageBackEnd()
    app.mainloop()
        