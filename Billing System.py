from tabulate import tabulate

cart=[]
quantity=[]
price1=[]
studoff=[]
deliveryamt=[]
Total=0
final_bil=[]

menu=print(tabulate([[ 1,'Mcveggie',110],[2,'Alootikka',150],[3,'French Fries',80] ],headers=['sl.', 'Food' , 'Price']))

while True:
    food=input("Enter a food to buy (q to quit) : ")
    if food=="q":
        break
    cart.append(food)
    
    quantity1=int(input("How many quantity : "))
    quantity.append(quantity1)
    amount=int(input("Enter the price of the food : "))
    price=amount*quantity1
    price1.append(price)
    (sum(price1))
    menu=print(tabulate([[ 1,'Mcveggie',110],[2,'Alootikka',150],[3,'French Fries',80] ],headers=['sl.', 'Food' , 'Price']))
    
    
offferplan=input("Are you a student [yes/no] : ")
if offferplan=="yes":
    print(f"You have receive an 20% off ")
    offercal1=(price*20)/100
    offercal2=price-offercal1
    studoff.append(offercal2)
    
    
else:
    print("You are not valid for the off")

delivery=input("Do u want to delivery [yes/no] : ")
if delivery=="yes":
    print(f"Adding 5% as delivery charge")
    offercal2=offercal2*1.05
    deliveryamt.append(offercal2)
    
else:
    print("No delivery charge")

tips=0
tip=input("Do want to give a tip [yes/no] : ")
if tip=="yes":
    tip1=(int(input("How much : 2 , 5 , 10 : ")))
    if tip1==2:
        tips=(float(offercal2+tip1))
    if tip1==5:
       tips=(float(offercal2+tip1))
    if tip1==10:
        tips=(float(offercal2+tip1))
        
    
print("\n\n----------Here is your total bill----------\n\n")
final_bill=print((tabulate([[1.  ,  'Cart'  ,  cart  ],[2.  ,  'Quantity'  ,  quantity  ],[3.  ,  'Student_offer'  ,  '20%'  ,  studoff  ],[4.  ,  'Delivery_charges'  ,  '5%',   deliveryamt  ],[  5.  ,  'Tip'  ,  tip1  ],[6.  ,  'Total_Amount'  ,  tips ]])))
print("\n\n     Thank you and come again!!")
