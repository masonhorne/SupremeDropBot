import tkinter as tk
from tkinter import messagebox
import time
from PIL import ImageTk, Image

from supremedropbot import Application
# This contains the GUI which collects info from user to find and purchase product with
# Uses Application from supremedropbot for web scraping


class Window:
    # This appears when input provided is invalid
    @staticmethod
    def invalidinput():
        tk.messagebox.showinfo("Invalid Input", "All fields must be filled in to continue.")

    # This appears when the item couldn't be found within 15 minutes
    @staticmethod
    def unavailable():
        tk.messagebox.showerror("Product Unavailable", "The product wasn't found within 15 minutes... Try again!")

    # Method that runs when submit button is selected
    def submit(self):
        # Loads in information from gui
        keydict = {
            'name': namefield.get(),
            'email': emailfield.get(),
            'tele': telephonefield.get(),
            'address': addressfield.get(),
            'zip': zipfield.get(),
            'city': cityfield.get(),
            'state': statefield.get(),
            'country': countryfield.get(),
            'ccn': creditcardfield.get(),
            'ccem': expirationmonthfield.get(),
            'ccey': expirationyearfield.get(),
            'cvv': securityfield.get(),
            'itemSize': itemsizefield.get(),
            'itemName': itemnamefield.get(),
            'itemColor': itemcolorfield.get(),
            'itemCategory': categoryfield.get()
        }
        info = keydict.values()
        # Checks all info has been filled in
        for d in info:
            if d == "":
                self.invalidinput()
                return
        # Creates web scraping application with the dictionary
        app = Application(keydict)
        productfound = False
        count = 0
        # Searchs until product is found of 15 minutes have passed
        while not productfound:
            productfound = app.search_product()
            count = count + 1
            time.sleep(5)  # waits 5 seconds before trying again
            if count == 180:  # 15 minutes have passed and the product hasn't been posted
                app.cancel_search()
                self.unavailable()
                return
        # Product is then added to cart and checked out
        app.add_product()
        app.checkout()
        # User is prompted to stop automation and complete purchase and stopper prevents driver from ending
        tk.messagebox.showinfo("Complete Purchase", "End browser control to accept terms and complete CAPTCHA")
        stopper = input("Press enter to end...")

    # This constructs the GUI window
    def __init__(self):
        # Creates root widget of GUI
        global root
        root = tk.Tk()
        w = 685  # width for the Tk root
        h = 445  # height for the Tk root
        # get screen width and height
        ws = root.winfo_screenwidth()  # width of the screen
        hs = root.winfo_screenheight()  # height of the screen
        # Calculate coordinates
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 1.5)
        # set the dimensions of the screen
        # and where it is placed
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(False, False)
        root.title("SupremeDropBot")
        p1 = tk.PhotoImage(file='images/SIcon.png')
        root.iconphoto(False, p1)
        # Creates logo at top of application
        img = ImageTk.PhotoImage(Image.open('images/SupremeDropBot.png'))
        imagelabel = tk.Label(image=img)
        imagelabel.grid(row=0, column=0, columnspan=5)
        # Creates input field for name
        namelabel = tk.Label(root, text="Name: ", borderwidth=5)
        namelabel.grid(row=1, column=0)
        global namefield
        namefield = tk.Entry(root)
        namefield.grid(row=1, column=1)
        # Creates input field for email
        emaillabel = tk.Label(root, text="Email: ", borderwidth=5)
        emaillabel.grid(row=2, column=0)
        global emailfield
        emailfield = tk.Entry(root)
        emailfield.grid(row=2, column=1)
        # Creates input field for telephone
        telephonelabel = tk.Label(root, text="Telephone: ", borderwidth=5)
        telephonelabel.grid(row=3, column=0)
        global telephonefield
        telephonefield = tk.Entry(root)
        telephonefield.grid(row=3, column=1)
        # Creates input field for address
        addresslabel = tk.Label(root, text="Address: ", borderwidth=5)
        addresslabel.grid(row=4, column=0)
        global addressfield
        addressfield = tk.Entry(root)
        addressfield.grid(row=4, column=1)
        # Creates input field for zip
        ziplabel = tk.Label(root, text="Zip: ", borderwidth=5)
        ziplabel.grid(row=5, column=0)
        global zipfield
        zipfield = tk.Entry(root)
        zipfield.grid(row=5, column=1)
        # Creates input field for city
        citylabel = tk.Label(root, text="City: ", borderwidth=5)
        citylabel.grid(row=6, column=0)
        global cityfield
        cityfield = tk.Entry(root)
        cityfield.grid(row=6, column=1)
        # Creates input field for state
        statelabel = tk.Label(root, text="State(eg. FL): ", borderwidth=5)
        statelabel.grid(row=7, column=0)
        global statefield
        statefield = tk.Entry(root)
        statefield.grid(row=7, column=1)
        # Creates input field for country
        countrylabel = tk.Label(root, text="Country(eg. USA): ", borderwidth=5)
        countrylabel.grid(row=8, column=0)
        global countryfield
        countryfield = tk.Entry(root)
        countryfield.grid(row=8, column=1)
        # Creates input field for item name
        itemnamelabel = tk.Label(root, text="Item Name: ", borderwidth=5)
        itemnamelabel.grid(row=1, column=3)
        global itemnamefield
        itemnamefield = tk.Entry(root)
        itemnamefield.grid(row=1, column=4)
        # Creates input field for item color
        itemcolorlabel = tk.Label(root, text="Item Color: ", borderwidth=5)
        itemcolorlabel.grid(row=2, column=3)
        global itemcolorfield
        itemcolorfield = tk.Entry(root)
        itemcolorfield.grid(row=2, column=4)
        # Creates input field for item size
        itemsizelabel = tk.Label(root, text="Item Size: ", borderwidth=5)
        itemsizelabel.grid(row=3, column=3)
        global itemsizefield
        itemsizefield = tk.Entry(root)
        itemsizefield.grid(row=3, column=4)
        # Creates input field for item category
        categorylabel = tk.Label(root, text="Item Category: ", borderwidth=5)
        categorylabel.grid(row=4, column=3)
        global categoryfield
        categoryfield = tk.Entry(root)
        categoryfield.grid(row=4, column=4)
        # Creates input field for credit card number
        creditcardlabel = tk.Label(root, text="Credit Card #: ", borderwidth=5)
        creditcardlabel.grid(row=5, column=3)
        global creditcardfield
        creditcardfield = tk.Entry(root)
        creditcardfield.grid(row=5, column=4)
        # Creates input field for credit card expiration month
        expirationmonthlabel = tk.Label(root, text="Exp. Month(eg. 01): ")
        expirationmonthlabel.grid(row=6, column=3)
        global expirationmonthfield
        expirationmonthfield = tk.Entry(root)
        expirationmonthfield.grid(row=6, column=4)
        # Creates input field for credit card expiration year
        expirationyearlabel = tk.Label(root, text="Exp. Year(eg. 2022): ", borderwidth=5)
        expirationyearlabel.grid(row=7, column=3)
        global expirationyearfield
        expirationyearfield = tk.Entry(root)
        expirationyearfield.grid(row=7, column=4)
        # Creates input field for credit card security code
        securitylabel = tk.Label(root, text="CVV: ", borderwidth=5)
        securitylabel.grid(row=8, column=3)
        global securityfield
        securityfield = tk.Entry(root)
        securityfield.grid(row=8, column=4)
        # Creates submit button
        btn = tk.Button(root, text="Submit", padx=50, pady=10, command=self.submit)
        btn.grid(row=9, column=0, columnspan=5)
        root.mainloop()


Window()
