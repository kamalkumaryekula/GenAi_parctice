items=["tomato","potato"]
selling_price=["30","25"]
cost_price=["20","15"]
while True:
    print("*" * 45)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("*" * 45)
    print("1.admin")
    print("2.user")
    print("3.exit")
    print("*" * 45)
    choice=int(input("enter the choice:"))
    if choice == 1:
        
        while True:
            print("=" * 45)
            print("Admin")
            print("=" * 45)
            print("1.View the items")
            print("2.add the items")
            print("3.Remove new item")
            print("4.update the price")
            print("5.profit of the item")
            print("6.Exit")
            admin_choice=int(input("enter your admin_choice:"))
            if  admin_choice == 1:
                print("=" * 45)
                print("INDEX   ITEM        SP      CP")
                print("=" * 45)
                for i, item in enumerate(items):
                    print(f"{i:<7}{item:<12}{selling_price[i]:<8}{cost_price[i]:<8}")

                print("=" * 45)
                      
            elif admin_choice == 2:
                    new_item=input("Add new item:")
                    item_sp=input("Add selling price:")
                    item_cp=input("Add cost price:")
                    items.append(new_item)
                    selling_price.append(item_sp)
                    cost_price.append(item_cp)
                    print("Added items:",items)
                    print("selling price for item:",selling_price)
                    print("cost price for item:",cost_price)
                    
            elif admin_choice == 3:
                
                    remv_item=input("enter remove item:")
                    if remv_item in items:
                        index=items.index(remv_item)
                        items.pop(index)
                        selling_price.pop(index)
                        cost_price.pop(index)
                        print("Item removed successfully")
                    else:
                        print("item not found")
                        admin_choice=int(input("enter your admin_choice:"))  
            elif admin_choice == 4:
                indx=int(input("enter the index num:"))
                new_sellingprice=int(input("enter the new selling price:"))
                new_costprice=int(input("enter the new cost price:"))
                selling_price[indx] = new_sellingprice
                cost_price[indx]=new_costprice
                print(f"updated price -> selling:{selling_price},cost:{cost_price}")
                    
            elif admin_choice == 5:
                indx=int(input("enter the index num:"))
                profit=(int(selling_price[indx])-int(cost_price[indx]))
                print("Profit of the item",items[indx],profit)
            else:
                    print("Exit")
                    choice=int(input("enter the choice:"))
                    break
                    

    elif choice == 2:
        cart = []
        while True:
            print("=" * 45)
            print("user")
            print("=" * 45)
            print("1.Add items to cart")
            print("2.view items in cart")
            print("3.remove items from cart")
            print("4.modify items in cart")
            print("5.bill the items")
            print("6.exit")
            user_choice = int(input("enter the user_choice:"))
            if user_choice == 1:
                    indx=int(input("enter the index number:"))
                    qunty=int(input("enter the quantity:"))
                    cart.append([items[indx],qunty])
                    
                    print(f"item added to cart :{cart}")
            elif user_choice == 2:
                
                    print(f"view in cart:{cart}")
            elif user_choice == 3:
                indx=int(input("enter the index number:"))
                cart.pop(indx)
                
                print("remove item from cart")
            elif user_choice == 4:
                indx=int(input("enter the index number:"))
                modify_item=input("enter the item:")
                cart[indx] = modify_item
                
                print(f"modify item in cart:{cart}")
            elif user_choice == 5:
                total = 0
                for item ,qunty in cart:
                    index=items.index(item) 
                    total+=int(selling_price[index])* qunty
                    
                print("bill the items",total)
            else:
                    print("Exit")
                    break
                    
                    
        

            
    else:
        break
        
    


