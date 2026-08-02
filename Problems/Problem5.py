item=[]
price=[]
for i in range(5):
    items=input("Enter Item Name: ")
    prices=int(input("Enter Item Price: "))

    item.append(items)
    price.append(prices)

print(sum(price))


maxi=price.index(max(price))
mini=price.index(min(price))
print(item[maxi])
print(item[mini])


