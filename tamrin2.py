# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_afO0zn7UpzW_VrH65YGrwWT--2zu3nh
"""

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def place_Order(drink):
 if drink in Menu:
  Order.append(drink)
  print(f"{drink}added to your order")
 else:
  print(f"{drink}doesn`t exist")
  #ثبت سفارش

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def cancel_Order(drink):
  if drink in Order:
    Order.remove(drink)
    print(f"{drink}removed from order")
  else:
    print(f"{drink}doesn`t exist in order")
    #لغو سفارش

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def best_selling_drink():
  if not Order:
    return"not order"
drink_count={}
for drink in Order:
  if drink in drink_count:
    drink_count[drink]+=1
  else:
    drink_count[drink]=1
    #شناسایی پرفروش ترین

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def Order_index(drink):
  if drink in Order:
    index=Order.index(drink)
    print(f"index{drink}in order:{index}")
  else:
    print(f"{drink}doesn`t exist in order")
    #ایندکس سفارش

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def sort_Order():
  Order.sort()
  print("سفارشات به ترتیب حروف الفبا",Order)
  #مرتب سازی

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def clear_Order():
  Order.clear()
  print("all orders are delete")
  #پاک کردن

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
def safe_place_Order(drink):
  place_Order(drink)
  #ثبت سفارش موجود در منو

Menu=["اسموتی","چای","موکا","قهوه","هات چاکلت"]
Order=[]
if Order.count("هات چاکلت")>5:
  print("هات چاکلت پرفروش ترین ایتم امروز است")
  #چک کردن تعداد هات چاکلت