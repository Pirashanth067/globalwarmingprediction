import pandas as pd
import numpy as np
import statistics
import warnings
import matplotlib.pyplot as plt
import ctypes
from tkinter.ttk import *

np.set_printoptions(threshold=np.inf)
from sklearn.linear_model import LinearRegression
warnings.filterwarnings(action="ignore", module="sklearn", message="^internal gelsd")
from termcolor import colored, cprint


from tkintertable import TableCanvas, TableModel
from tkinter import *


temp=[]
year=[]
new_year=[]
mean=[]
year2delements = []
difference=0;
yearinteger=0;
num=0
average=[]
new_num=0
data1=[]
data2=[]

fields = ["record_id","month","day","year","AverageTemperatureFahr","Humidity","City","Country"] ##record wanted coloumn in field variable and avoiding unnecessary data/coloumn
missing_values = ["n/a", "na", "--","NA"] ##to detect missing values for cleansing data step of the data analysis
field_temp=["AverageTemperatureFahr"] ## temperature for visualization graph

reviews = pd.read_csv("temperature.csv", skipinitialspace=True, usecols=fields)  #Reading the dataset with specified coloum in a dataframe using Pandas
reviews.set_index('day',inplace=True)
reviews.to_csv('newtemp.csv') ##save the created data in csv without unwanted information from the old csv file

def data_cleaning():
    reviews = pd.read_csv("newtemp.csv",  na_values=missing_values) #Reading the new dataset and avoid missing values that mention in above step

def missing_value():
    values = {'AverageTemperatureFahr': 51.9062}
    reviews.fillna(value=values, limit=2)
    reviews.dropna(inplace=True) ##remove all the values with null object from the review data frame.

def calculations(mylist = [], *args):   #method to calculate Standard deviation,mean and variance
    print(colored('Standard Deviation of temperature is ', 'red'), colored('% s '
          % (statistics.stdev(mylist)), 'green'))
    print(colored('Mean of temperature is ', 'red'), colored('% s '
          % (statistics.mean(mylist)), 'green'))
    print(colored('Variance of temperature is ', 'red'), colored('% s '
          % (statistics.variance(mylist)), 'green'))
    print(colored('Minimum of temperature is ', 'red'), colored('% s '
            % (min(mylist)), 'green'))
    print(colored('Maximum of temperature is ', 'red'), colored('% s '
            % (max(mylist)), 'green'))
    print(colored('Median of temperature is ', 'red'), colored('% s '
            % (statistics.median(mylist)), 'green'))
    mean.append((statistics.mean(mylist)))

def year_wise_calculation(styr):
    for z in range(len(year2delements)):
        print("-------------------------------------------------------")
        print(colored('Year of the calculation is  ', 'red'), colored('% s '% styr, 'green'))
        new_year.append(styr)
        calculations(year2delements[z])
        styr= styr+1
        print("-------------------------------------------------------")

data_cleaning()
missing_value()




def class1():
    global window
    window = Tk()

    window.title("Global warming prediction")
    window.geometry('600x300')
    # var_1 = StringVar()
    lbl1 = Label(window, text="Enter the country you want to predict:")
    lbl2 = Label(window, text="Enter the city you want to predict:")
    lbl3 = Label(window, text="Enter the Starting year:")
    lbl4 = Label(window, text="Enter the Ending year:")
    lbl5 = Label(window, text="Select the weather")
    lbl6 = Label(window, text="Welcome")

    lbl1.grid(column=0, row=1)
    lbl2.grid(column=0, row=3)
    lbl3.grid(column=0, row=5)
    lbl4.grid(column=0, row=7)
    lbl5.grid(column=0, row=9)
    lbl6.grid(column=0, row=0)

    # input_country1 = Entry(window, width=10, textvariable=self.entryText)
    input_country1 = Entry(window, width=10)
    # input_city1 = Entry(window, width=10, textvariable=self.testText)
    input_city1 = Entry(window, width=10)
    start_year1 = Entry(window, width=10)
    end_year1 = Entry(window, width=10)

    input_country1.grid(column=1, row=1)
    input_city1.grid(column=1, row=3)
    start_year1.grid(column=1, row=5)
    end_year1.grid(column=1, row=7)

    combo = Combobox(window)
    combo['values'] = ('Temparature', 'Humidity')
    combo.current(1)  # set the selected item
    combo.grid(column=1, row=9)

    def clicked():
        # lbl1.configure(text=input_country1.get())
        lbl6.configure(text='Loding data........Please close this window')
        passvalues(input_country1.get(), input_city1.get(), start_year1.get(), end_year1.get(), combo.get())
    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=1, row=13)
    window.mainloop()


def passvalues( getcountry, getcity, getstartyear, getendyear, getcombo):
    global input_country, input_city, start_year, end_year, data,weather,styear,val
    input_country = getcountry
    input_city = getcity
    start_year = getstartyear
    end_year = getendyear


    if not getcountry or not getcity or not getstartyear or not getendyear or not getcombo:
        ctypes.windll.user32.MessageBoxW(0, "Input is null", "Input Error Found!", 1)
    elif start_year or end_year:
        try:
            styear = int(start_year)
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, "Enter Int value to start year", "Input Error Found!", 1)

        try:
            val = int(end_year)
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, "Enter Int value to end year", "Input Error Found!", 1)
        if getcombo=="Temparature":
            data=1
            weather="Temparature"
            window.destroy()
            ctypes.windll.user32.MessageBoxW(0, "Please wait data is Loading.....!", "Alert", 1)
        elif getcombo=="Humidity":
            data = 2
            weather = "Humidity"
            window.destroy()
            ctypes.windll.user32.MessageBoxW(0, "Please wait data is Loading .....!", "Alert", 1)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Select from combobox", "Input Error Found!", 1)

class1()

for column  in reviews['Country']:
    if column == input_country:
        if reviews.iloc[num]['City'] == input_city:
            if int(reviews.iloc[num]['year'])>= styear:
                if int(reviews.iloc[num]['year']) <= val:
                    new_num=new_num+1
                    yearandmonth = str(reviews.iloc[num]['year']) + ' : ' + str(reviews.iloc[num]['month'])
                    year.append(yearandmonth)
                    if int(data)==1:
                        temp.append(reviews.iloc[num]['AverageTemperatureFahr'])
                    elif int(data)==2:
                        temp.append(reviews.iloc[num]['Humidity'])
    num=num+1
print("Data Processing..... ")

print(len(temp))
data2 = {}
newdata = {}
for z in range(len(temp)):
        newdata[z] = {'rec'+str(z): {'Year : Month': year[z], weather: str(temp[z])}}
        data2.update(newdata[z])

class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x500+200+100')
        self.main.title(weather)
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        table = TableCanvas(f, data=data2)
        # table.redrawTable()
        # table.model.data[0]['col1'] = 'XX'
        # print(table.model.columnNames)
        table.show()
        return

app=TestApp()
app.mainloop()


def lineplot_function():
    x=0;
    mynum=0;
    y=0;
    if len(year2delements) == 0:
        yearinteger = styear;
        difference=val-styear+1;
        #print(difference)
        for z in range(val-styear+1):
            year2delements.append([])
        for col in reviews['Country']:
            if col == input_country:
                if reviews.iloc[mynum]['City'] == input_city:
                    if int(reviews.iloc[mynum]['year']) >= styear:
                        if int(reviews.iloc[mynum]['year']) <= val:
                            if int(reviews.iloc[mynum]['year'])!= yearinteger:
                                yearinteger=yearinteger+1
                                x=x+1
                            if int(reviews.iloc[mynum]['AverageTemperatureFahr']) != None and int(data) == 1:
                                year2delements[x].append(reviews.iloc[mynum]['AverageTemperatureFahr'])
                                y = y + 1
                            elif int(reviews.iloc[mynum]['Humidity']) != None and int(data) == 2:
                                year2delements[x].append(reviews.iloc[mynum]['Humidity'])
                                y = y + 1
                            elif int(reviews.iloc[mynum]['AverageTemperatureFahr']) == None or int(reviews.iloc[mynum]['Humidity']) == None:
                                year2delements[x].append(np.NaN)


            mynum = mynum + 1
    year_wise_calculation(styear);

def plot_visualization():
    fig, ax = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    ax[0].plot(year, temp)
    ax[1].bar(year, temp)
    ax[2].scatter(year, temp)
    if int(data) == 1:
        fig.suptitle('World temperature : % s '% input_city)
    #     fig.suptitle('World temperature ')
    elif int(data) ==2:
        # fig.suptitle('World Humidity ')
        fig.suptitle('World Humidity : % s '%input_city)
    # ax.legend()
    plt.xticks(rotation=90)
    plt.show()

def mean_plot_visualization():
    plt.subplots()
    plt.plot(new_year, mean, label="Mean")
    plt.xlabel('Year')
    plt.ylabel('Mean')
    if int(data) == 1:
        plt.title("Mean Visualization of temperature")
    elif int(data) ==2:
        plt.title("Mean Visualization humidity")
    # ax.legend()

    plt.legend()
    plt.show()

def scatter_visualization():

    fig, ax =plt.subplots()
    # scatter the sepal_length against the sepal_width
    ax.scatter(year, temp)
    # set a title and labels
    if int(data) == 1:
        fig.suptitle('World temperature scatter plot: % s '% input_city)
        ax.set_ylabel('Temperature')
    elif int(data) ==2:
        fig.suptitle('World Humidity scatter plot% s '% input_city)
        ax.set_ylabel('Humidity')
    ax.set_xlabel('year')
    plt.text(0.5, 0.5,'matplotlib', horizontalalignment='center',verticalalignment='center',transform=ax.transAxes)
    plt.xticks(rotation=90)
    plt.show()

def piechart_visualization():
    fig1, ax1 = plt.subplots()
    ax1.pie(temp, labels = year, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.set_aspect("equal")
    ax1.legend()
    plt.xticks(rotation=90)
    plt.show()

def histogram_visualization():
    num_bins = 5
    n, bins, patches = plt.hist(temp, num_bins, facecolor='blue', alpha=0.5)
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()


def lifecycle_visualization():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(year, temp)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    if int(data) == 1:
        ax.set(xlim=[-10, 140], xlabel='fahrenheit', ylabel='Year and month',
               title='Temperature horizontal bar plot')
    elif int(data) ==2:
        ax.set(xlim=[-10, 140], xlabel='humidity', ylabel='Year and month',
               title='Humidity horizontal bar plot')


    ax.legend()
    plt.xticks(rotation=90)
    plt.show()

def yearplotvisualization():
    month=[1,2,3,4,5,6,7,8,9,10,11,12]
    plt.subplots()
    for z in range(len(year2delements)):
        if len(year2delements[z])<12:
            year2delements[z].append(None)
        plt.plot(month, year2delements[z], label=str(styear+z))
    plt.xlabel('Months')
    if int(data) == 1:
        plt.ylabel('Fahrenheit')
        plt.title("Temperature per year")
    elif int(data) == 2:
        plt.ylabel('Humidity')
        plt.title("Humidity per year")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()

def exit_code():
    exit(0)

def prediction():
    x1=pd.DataFrame(mean, columns=['mean'])
    y1=pd.DataFrame(new_year, columns=['year'])
    x_array = x1.values
    y_array = y1.values
    x = x_array.reshape(-1, 1)
    y = y_array.reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)

    # predict y from the data
    x_new = np.linspace(0, 30, 100)
    y_new = model.predict(x_new[:, np.newaxis])

    # plot the results
    plt.figure(figsize=(4, 3))
    ax = plt.axes()
    ax.scatter(mean, new_year)
    ax.plot(x_new, y_new)

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.axis('tight')
    plt.xticks(rotation=90)
    plt.show()

def visualization2():

        if selectedvalue=="CALCULATION":
            lineplot_function()
        elif selectedvalue=="YEAR-WISE LINE PLOT VISUALIZATION":
            yearplotvisualization()
        elif selectedvalue=="SCATTER VISUALIZATION":
            scatter_visualization()
        elif selectedvalue=="HISTOGRAM VISUALIZATION":
            histogram_visualization()
        elif selectedvalue=="PIE CHART VISUALIZATION":
            piechart_visualization()
        elif selectedvalue=="LIFE CYCLE VISUALIZATION":
            lifecycle_visualization()
        elif selectedvalue=="COMPLETE PLOT VISUALIZATION":
            plot_visualization()
        elif selectedvalue=="MEAN VISUALIZATION":
            mean_plot_visualization()
        elif selectedvalue=="DATA PREDICTION":
            prediction()

def gui2():
    global window,combo
    window = Tk()
    window.title("Global warming prediction")
    window.geometry('600x300')

    lbl2 = Label(window, text="Select The Visualization option")
    lbl2.grid(column=0, row=0)


    combo = Combobox(window)
    combo['values'] = ('CALCULATION', 'YEAR-WISE LINE PLOT VISUALIZATION','SCATTER VISUALIZATION','HISTOGRAM VISUALIZATION','PIE CHART VISUALIZATION'
                       ,'LIFE CYCLE VISUALIZATION','COMPLETE PLOT VISUALIZATION','MEAN VISUALIZATION','DATA PREDICTION')
    combo.current(0)  # set the selected item
    combo.grid(column=1, row=0)
    btn = Button(window, text="Generate", command=clicked)
    btn.grid(column=1, row=2)
    window.mainloop()

def clicked():
        passvalues(combo.get())
        visualization2()

def passvalues(getcombo):
    global selectedvalue
    selectedvalue = getcombo

gui2()

