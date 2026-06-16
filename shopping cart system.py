cart=[]
categories=set()
prices={}

n=int (input("Enter the number of items: "))

#Add
for i in range(n):
    item=input("Enter name: ")
    price=float(input("Enter the prices: "))
    category=input("Enter category: ")

    cart.append(item)
    prices[item]=price
    categories.add(category)

#Remove  
remove_item=input("Enter the item to remove: ")

if remove_item in cart:
    cart.remove(remove_item)
    del prices[remove_item]
    print("Item removed successsfully")
else:
    print("Item not found")
    
# Display cart
print("\nItems in Cart:", cart)

# Display unique categories
print("Unique Categories:", categories)

# Calculate total bill
total = sum(prices.values())
print("Total Bill = ₹", total)    

