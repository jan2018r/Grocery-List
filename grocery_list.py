'''
Program:               Grocery List Script
Author:                
Class:                 IT-140-T5093 Introduction to scripting 18EW5
Instructor             
Date:                  3 Jun 2018
Description:        A program that by INPUT's dictionary type data from the user on grocery store 
                    Items, quantity, and price of multiple items. Finally, the program OUTPUTS the total
                    amount of the purchased items the person has chosen in the form of a 'List'.
'''


grocery_history = list()

stop = 'go'
#Placing a dictionary data structure here it makes sure that all items 
#get rendered when all the necessary steps have been placed (item name, quantity, price). 
while stop != 'q':
    item_name = input("Item name:\n")
    quantity = int(input("Quantity purchased:\n"))
    cost = float(input("Price per item:\n"))
    grocery_item = {'name': item_name, 'number': int(quantity), 'price': float(cost)}
    grocery_history.append(grocery_item)
    stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit: ")
#Placing a loop it makes sure that while every time the software user continues or stops 'c' or 'q'. 
#With the 'c' user will be able to continue on entering items and prices, while hitting 'q' will end 
#the program and automatically give a subtotal of everything entered.     
grand_total = 0
print()

for grocery_item in grocery_history:
    item_total = grocery_item['number'] * grocery_item['price']
    grand_total += item_total
    print("{} {} @ ${} ea ${}".format(grocery_item['number'], grocery_item['name'], grocery_item['price'], item_total))
    #item_total = 0
print("Grand total: $",grand_total)
