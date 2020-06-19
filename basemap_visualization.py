import tkinter as tk
from tkinter import *
from tkinter.ttk import *


class my_gui(tk.Frame):
    def __init__(self):
        print("in init")

    # def __call__(self, foo, bar, baz=None):
    def class1(self):
        global window
        window = Tk()
        self.entryText = tk.StringVar()
        self.testText = tk.StringVar()

        window.title("Global warming prediction")
        window.geometry('400x300')
        var_1 = StringVar()
        lbl1 = Label(window, text="Enter the country you want to predict:")
        lbl2 = Label(window, text="Enter the city you want to predict:")
        lbl3 = Label(window, text="Enter the Starting year:")
        lbl4 = Label(window, text="Enter the Ending year:")
        lbl5 = Label(window, text="Select the weather")

        lbl1.grid(column=0, row=0)
        lbl2.grid(column=0, row=1)
        lbl3.grid(column=0, row=2)
        lbl4.grid(column=0, row=3)
        lbl5.grid(column=0, row=4)

        input_country1 = Entry(window, width=10, textvariable=self.entryText)
        input_city1 = Entry(window, width=10,textvariable=self.testText)
        start_year1 = Entry(window, width=10)
        end_year1 = Entry(window, width=10)

        input_country1.grid(column=1, row=0)
        input_city1.grid(column=1, row=1)
        start_year1.grid(column=1, row=2)
        end_year1.grid(column=1, row=3)


        combo = Combobox(window)
        combo['values'] = ('Temparature','Humidity')
        combo.current(1)  # set the selected item
        combo.grid(column=1, row=4)

        def clicked():
            lbl1.configure(text=input_country1.get())
            entryText = input_country1.get()
            testText = input_city1.get()
            var_1.set(entryText)
            self.passvalues(input_country1.get(),input_city1.get(),start_year1.get(),end_year1.get(),combo.get())
            # getValues(entryText)
            lbl2.configure(text=input_city1.get())
            lbl3.configure(text=start_year1.get())
            lbl4.configure(text=end_year1.get())
            lbl5.configure(text=combo.get())
            # print(entryText)

        country = input_country1.get()
        btn = Button(window, text="Click Me", command=clicked)
        btn.grid(column=2, row=4)
        window.mainloop()
        #self.print_message()

    def passvalues(self, getcountry,getcity,getstartyear,getendyear,getcombo ):
        global country1, city, startyear, endyear, weather
        country1=getcountry
        city=getcity
        startyear=getstartyear
        endyear=getendyear
        weather=getcombo
        print(country1)
        print(city)
        print(startyear)
        print(endyear)
        print(weather)

    # def print_message(self):
    #
    #     print(country1)
    #     print(self.testText)

