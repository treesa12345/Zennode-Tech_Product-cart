


#welcome User
itemAvailabledict={}
shoppingDict={ }
userName=input("Please enter yourname:")
welcomeMessage=f"Welcome to my store  {userName}"
lenWCMsg=len(welcomeMessage)
print("_"*lenWCMsg)
print(welcomeMessage)
print("_"*lenWCMsg) 

#read data from textfile

my_file=open("available_items.txt")
file_line=my_file.readline()
itemsAvailable=my_file.readlines()
my_file.close()

#fetch items from list and add to a dictionary

print("____________PRODUCTS AVAILABLE IN OUR STORE____________")
for item in itemsAvailable:
  item_name=item.split() [0]
  item_price=item.split()[1]
  print(f"{item_name}:{item_price}")
  itemAvailabledict.update({item_name.title():int(item_price)})
print("_"*20) 




#prompt user to add items
  
proceedshopping=input("Do you wish to proceed shopping(yes/no)")
while proceedshopping.lower()=="yes":
  item_added=input("Add an item:  ")
  if item_added.title() in itemAvailabledict:
    item_qty=float(input("Add Quantity"))
    shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailabledict[item_added.title()]*item_qty}})
    print(shoppingDict)
  else:
    print("Unable to add, unavailable item") 
  proceedshopping=input("Do you want to add more items(yes/no):")
else:
 print("\n")
 print("*****Bill Summary*****")
 print("\n")
 print("Item       Quantity      Subtotal")
 Total=0
 totalquantity=0
 for key in shoppingDict:
   print(f"{key}     {shoppingDict[key]['quantity']}          {shoppingDict[key]['subtotal']}")
   Total=shoppingDict[key]['subtotal']+Total
   totalquantity=shoppingDict[key]['quantity']+totalquantity
print(f"Total:{Total}")
print("\n")
#print(f"Totalquantity:{totalquantity}")

#discount
if  (Total>0) :
    
   if Total>200:
    dis=Total-10
   elif item_qty<10:
    dis=item_qty*0.05
   elif totalquantity>20:
    dis=Total*0.1
   elif totalquantity>30 and item_qty>15:
    dis= item_qty*0.5   
   print("discount : ",dis)
   print("Netpay :",Total-dis)
else:
  print("Invalid")

print("***********Thank You***********")
print("Hope to see you back soon! ")


