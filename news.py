from random import randrange
day_by_day = []
all_day = []
rn_ton = 0
ton = 0
rn_demand = 0

demand = 0
revenue = 0
lp = 0
slvg = 0
purchase_value_of_70_np = round((.33 * 70), 2)
dp = 0

def rn_for_ton(k): #2 function
    for i in range (k):
        global rn_ton, day_by_day
        day_by_day = [] # reset the list to empty
        rn_ton = randrange(100)
        day_by_day.append(i+1)
        day_by_day.append(rn_ton)
        type_of_news_day() #3 call

def type_of_news_day(): #3 function
    global ton
    if rn_ton < 36:
        ton = "good"
    elif rn_ton < 81:
        ton = "fair"
    elif rn_ton < 101:
        ton = "poor"
    day_by_day.append(ton)
    
    rn_for_demand() #4 call

def rn_for_demand(): #4 function
    global rn_demand
    rn_demand = randrange(100)
    day_by_day.append(rn_demand)
    _demand() #5 call
    
def _demand(): #5 function
    global demand
    if ton == "poor" and rn_demand < 45:
        demand = 40
    elif ton == "poor" and rn_demand < 67:
        demand = 50
    elif ton == "poor" and rn_demand < 83:
        demand = 60
    elif ton == "poor" and rn_demand < 95:
        demand = 70
    elif ton == "poor" and rn_demand < 101:
        demand = 80
    elif ton == "fair" and rn_demand < 11:
        demand = 40
    elif ton == "fair" and rn_demand < 29:
        demand = 50
    elif ton == "fair" and rn_demand < 69:
        demand = 60
    elif ton == "fair" and rn_demand < 89:
        demand = 70
    elif ton == "fair" and rn_demand < 97:
        demand = 80
    elif ton == "fair" and rn_demand < 101:
        demand = 90
    elif ton == "good" and rn_demand < 4:
        demand = 40
    elif ton == "good" and rn_demand < 9:
        demand = 50
    elif ton == "good" and rn_demand < 24:
        demand = 60
    elif ton == "good" and rn_demand < 44:
        demand = 70
    elif ton == "good" and rn_demand < 79:
        demand = 80
    elif ton == "good" and rn_demand < 94:
        demand = 90
    elif ton == "good" and rn_demand < 101:
        demand = 100
    else:
        demand = 0
    
    day_by_day.append(demand)
    _revenue() #6 call
    
def _revenue(): #6 function
    global revenue
    revenue = demand * .5
    day_by_day.append(revenue)
    profit_lost() #7 call
    
def profit_lost(): #7 function
    global lp
    if demand > 70:
        lp = (demand - 70) * .17
    else:
        lp = 0
    day_by_day.append(round(lp, 2))
    salvage() #8 call

def salvage(): #8 function
    global slvg
    if demand < 70:
        slvg = (70 - demand) * .05
    else:
        slvg = 0
    day_by_day.append(slvg)
    daily_profit() #9 call

def daily_profit(): #9 function
    global dp
    dp = revenue - purchase_value_of_70_np - lp + slvg
    day_by_day.append(round(dp, 2))
    day_by_day.append(purchase_value_of_70_np)
    all_day.append(day_by_day)
    #end of one loop initiated in function 2
    
rn_for_ton(30) #1 #2 call

import pandas as pd
df = pd.DataFrame(all_day, columns = ['Day', ' RN for TON ', ' TON ', ' RN for Demand ', ' Demand ', ' Revenue ', ' Lost Profit ', ' Salvage ', ' Daily Profit ', ' Purchase Value of 70'])

df=df.set_index('Day')
pd.set_option('display.colheader_justify', 'center')

print(df)
