item=[]
price=[]
for i in range(5):
    items=input("Enter Item Name: ")
    prices=int(input("Enter Item Price: "))

    item.append(items)
    price.append(prices)

print(sum(price))


# maxi=price.index(max(price))
# mini=price.index(min(price))
# print(item[maxi])
# print(item[mini])

mx=price[0]
mx_item=item[0]
mn=price[0]
mn_item=item[0]
for i in range(5):
    if price[i]> mx:
        mx_item=item[i]
        mx=price[i]
    elif price[i]< mn:
        mn_item=item[i]
        mn=price[i]
print(f'{mx_item,mx} and {mn_item,mn}')