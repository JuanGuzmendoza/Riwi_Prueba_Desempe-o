from datetime import date

library_inventory=[]
book_categories=["Horror", "love", "fiction", "action", "fantasy"]
sales_history=[]




#===============
#-BUSINESS LOGIC
#===============
def add_book_inventory(book_title,book_author,book_category,book_price,book_quantity):
  
    library_inventory.append({book_title:{
        "author":book_author,
        "category":book_category,
        "price":book_price,
        "quantity":book_quantity
    }})

def search_book(book_name):

    for i in library_inventory:
        if book_name in i:
                print("=== Product Found ===")
                print(f"📕 Title: {book_name}")
                print(f"🧑 Author: {i[book_name]["author"]}")
                print(f"📋 Categorie: {book_categories[int(i[book_name]["category"])]}")
                print(f"💸 Price: {i[book_name]["price"]}")
                print(f"📦 Stock: {i[book_name]["quantity"]}")
                print("=====================")
                return True
    print("🚫 Product not found")
    return False

def update_price_book(book_name,new_book_price):
    for i in library_inventory:
        if book_name in i:
            i[book_name]["price"]=new_book_price
            return True
    return False

def update_quantity_book(book_name,new_book_quantity):
    for i in library_inventory:
        if book_name in i:
            i[book_name]["quantity"]=int(new_book_quantity)
            return True
    return False


def delete_book(book_name):

    for i in library_inventory:
        if book_name in i:
            library_inventory.remove(i)
            print(f"✅ The Book '{book_name}' was successfully deleted.")
            return True
    print("🚫 Book not found.")
    return False

def register_book_sale(book_name,name_cliente,quantity_sell,book_author,purcharse_total):

    
    if quantity_sell>3:
        descuent=10
    elif quantity_sell>5:
        descuent=20
    else:
        descuent="does not apply"
    sales_history.append(
        {"customer":name_cliente,
         "book_sell":book_name,
         "quantity_sell":quantity_sell,
         "date":date.today(),
         "descuent":descuent,
         "author_book":book_author,
         "purcharse_total":purcharse_total
         }
    )


def get_three_best():
    position_1=("",0)
    position_2=("",0)
    position_3=("",0)
    for i in sales_history:
        if int(i["quantity_sell"])>position_1[1]:
            position_2=position_1
            position_1=(i["book_sell"],int(i["quantity_sell"]))
        elif int(i["quantity_sell"])>position_2[1]:
            position_3=position_2
            position_2=(i["book_sell"],int(i["quantity_sell"]))
        elif int(i["quantity_sell"])>position_3[1]:
            position_3=(i["book_sell"],int(i["quantity_sell"]))
    print("==💸The 3 best-selling books💸==")
    print(f"== Position 1 ===")
    print(f"📕 Bock: {position_1[0]}")
    print(f"📦 Quantity sells: {position_1[1]}")
    print("-" * 30)
    print(f"=== Position 2 ===")
    print(f"📕 Bock: {position_2[0]}")
    print(f"📦 Quantity sells: {position_2[1]}")
    print("-" * 30)
    print(f"=== Position 3 ===")
    print(f"📕 Bock: {position_3[0]}")
    print(f"📦 Quantity sells: {position_3[1]}")
    print("-" * 30)

def calculate_sales_value_total():
    total_sales_value=0
    total_quantity_value=0
    for i in sales_history:
        total_quantity_value+=int(i["quantity_sell"])
        total_sales_value+=i["purcharse_total"]
    print(f"-Total money obtained {total_sales_value}")
    print(f"-Total quantity sold {total_sales_value}")

#=====================
#-VALIDATION FUNCTIONS
#=====================

def validation_numbers(value,tipe):
    try:
        return True if tipe(value)>-1 else print("only can values positive")
    except:
        if tipe==float:
            print(f"only can of values positive and float")
        else:
            print(f"only can of values positive and numbers in the range")
            
        return False
    
def validation_equality_book(book_title):
    for i in library_inventory:
        if book_title in i:
            return True
    return False

def validate_book_in_stock(book_title):

    for i in library_inventory:
        if book_title in i:
            if int(i[book_title]["quantity"])==0:
                return True
    return False


#==============
#-MENU INTERFAZ
#==============
def sales_report_by_author(autor):

    cant_books_sells=0
    price_books_sells=0
    for i in sales_history:
        if autor == i["author_book"]:
            cant_books_sells+=int(i["quantity_sell"])
            price_books_sells+=i["purcharse_total"]
    if cant_books_sells ==0 and price_books_sells ==0:
        print(" -- Author not found --")
    else:
        print(cant_books_sells)
        print(f"{price_books_sells:.3f}")
        print(f"🧑Name author: {autor}")
        print(f"💸 Total sold: {price_books_sells}")
        print(f"📦 quantities sold: {cant_books_sells}")

def show_book_categories():
    print("--📚 \033[92m BOOK CATEGORIES \033[0m 📚--")
    for i,name in enumerate(book_categories):
        print(f"-{i}: {name}")


def show_all_books_sells():
    if not sales_history:
        print("🚫 The history sales is empty.")
        return False
    print("=== 🗂️ \033[33mAll Books sells\033[0m ===")
    for book_sell in sales_history:
        print(f"🧑 customer: {book_sell['customer']}")
        print(f"📕 Title book: {book_sell['book_sell']}")
        print(f"📦 Stock: {book_sell['quantity_sell']}")
        print(f"🗓️ Sale date: {book_sell['date']}")
        print(f"💸 descuent: {book_sell['descuent']}%")
        print("-" * 30)


def show_all_books():
    if not library_inventory:
        print("🚫 The inventory is empty.")
        return False
    print("=== 🗂️ \033[33mAll Books in Inventory\033[0m ===")
    for book in library_inventory:
        for name_book, details in book.items():
            print(f"📕 Title: {name_book}")
            print(f"🧑 Author: {details['author']}")
            print(f"📋 Categorie: {book_categories[int(details['category'])]}")
            print(f"💸 Price: {details['price']}")
            print(f"📦 Stock: {details['quantity']}")
            print("-" * 30)



def menu_interface():
    while True:
        print("\n")
        print("--📚 \033[92m  Comprehensive Inventory and Sales Management System with Dynamic Reports \033[0m 📚-- ".center(40))
        print("="*20)
        print("\033[33mFunction modules\033[0m")
        print("="*20)
        
        print("1.Inventory management ")
        print("2.Sales registration and consultation")
        print("3.Report functions")
        option_modules=input("-")
        match option_modules:
            case"1":
                while True:
                    print("\n")
                    print("="*20)
                    print("\033[92mMODULE OF INVENTORY MANAGEMENT\033[0m")
                    print("="*20)
                    print("1. Add a book")
                    print("2. Search a book")
                    print("3. show all books in inventory")
                    print("4. Update the price")
                    print("5. Update the quantity")
                    print("6. Delete a book")
                    print("7. Return to main menu")
                    option_function_of_module=input("-")
                    if validation_numbers(option_function_of_module,int):
                        if int(option_function_of_module)==7:
                            break
                        if int(option_function_of_module)>=1 and int(option_function_of_module)<=6:
                            return (option_modules,option_function_of_module)
                        else:
                            print("Only numbers in the range 1-6")

            case"2":
                while True:
                    print("\n")
                    print("="*20)
                    print("\033[92mMODULE OF SALES REGISTRATION AND CONSULTATION\033[0m")
                    print("="*20)
                    print("1.Hold a book sale")
                    print("2. Return to main menu")
                    option_function_of_module=input("-")
                    if validation_numbers(option_function_of_module,int):
                        if int(option_function_of_module)==2:
                            break
                        if int(option_function_of_module)>=1 and int(option_function_of_module)<=2:
                            return (option_modules,option_function_of_module)
                        else:
                            print("Only numbers in the range 1-2")
            case"3":
                while True:
                    print("\n")
                    print("="*20)
                    print("\033[92mMODULE OF REPORT FUNCTIONS\033[0m")
                    print("="*20)
                    print("1.Display the top 3 best-selling products.")
                    print("2.Generate a report of total sales grouped by author.")
                    print("3.Calculate net and gross income ")
                    print("4.Show sales history ")
                    print("5. Return to main menu")
                    option_function_of_module=input("-")
                    if validation_numbers(option_function_of_module,int):
                        if int(option_function_of_module)==5:
                            break
                        if int(option_function_of_module)>=1 and int(option_function_of_module)<=4:
                            return (option_modules,option_function_of_module)
                        else:
                            print("Only numbers in the range 1-4")



#==============
#-MAIN FUNCTION
#==============
def main():
    while True:
        opciones_menu=menu_interface()
        match opciones_menu[0]:
            case "1":
                match opciones_menu[1]:
                    case "1":
                        print("="*30)
                        print("=== 📦\033[36mAdd a book\033[0m📦 ")
                        while True:
                            book_title=input("-Name of product \n")
                            if validation_equality_book(book_title):
                                print("\033[31m !the book already exists! \033[0m!")   
                            else:
                                break

                        book_author=input("-Name of book author\n")

                        while True:
                            show_book_categories()
                            print("="*20)
                            print("Select the book category id")
                            print("="*20)
                            book_categorie=input("-")
                            if validation_numbers(book_categorie,int):
                                if int(book_categorie)<=len(book_categories):
                                    print(f"\033[92m ! {book_categories[int(book_categorie)]} IS SELECT !\033[0m ")
                                    break
                                else:               
                                    print(f"Only numbers in the range 0-{len(book_categories)-1}")
                    
                        while True:
                            book_price=input("-Price of book \n")
                            if validation_numbers(book_price,int):
                                break
                    
                        while True:
                            book_quantity=input("-Amount of book \n")
                            if validation_numbers(book_quantity,int):
                                break
                        
                
                        add_book_inventory(book_title,book_author,book_categorie,book_price,book_quantity)



                    case "2":
                        print("=== 📦\033[36mSearch a book\033[0m📦 ")
                        if show_all_books()==False:
                            continue   
                        product_name=input("-Title of book to Search details\n")
                        search_book(product_name)
                  
                  
                    case "3":
                        show_all_books()
                  
                  
                    case "4":
                        print("=== 📦\033[Update the price of a book\033[0m📦 ")
                        if show_all_books()==False:
                            continue    
                        book_title=input("-Title of book to update price\n")
                        if validation_equality_book(book_title):
                            while True:
                                try:
                                    book_price=int(input("-Price of book \n"))
                                    break
                                except:
                                    print("Only integers or floating points")
                            update_price_book(book_title,book_price)
                            print("=== Book price updated successfully ===")
                        else:
                            print("🚫 Book not found. Please try again.")

            
                    case "5":
                        print("=== 📦\033[Update the quantity of a book\033[0m📦 ")
                        if show_all_books()==False:
                            continue    
                        while True:
                            book_title=input("-Title of book to update quantity\n")
                            if validation_equality_book(book_title):
                                while True:
                                    book_quantity=input("-Quantity of book \n")
                                    if validation_numbers(book_quantity,int):
                                        break
                                update_quantity_book(book_title,book_quantity)
                                print("=== Book quantity updated successfully ===")
                                break
                            else:
                                print("🚫 Book not found. Please try again.")
                  
                  
                    case "6":
                        print("=== 🗑️ Delete a Book ===")
                        if show_all_books()==False:
                            continue    
                        while True:
                            book_name = input("- Title of book to delete\n")
                            if validation_equality_book(book_name):
                                delete_book(book_name)
                                break
                            else:
                                print("🚫 Book not found. Please try again.")
                                
            case "2":
                match opciones_menu[1]:
                    case "1":
                        print("=== 💲\033[Register book sale\033[0m💲 ===") 
                        if show_all_books()==False:
                            continue    
                        while True:
                            book_title=input("-Title of book to buy \n")
                            if validation_equality_book(book_title):
                                if validate_book_in_stock(book_title):
                                    print("Out of stock")
                                    break
                                name_client=input("-Name of client \n")
                                while True:
                                    book_quantity=input("-Quantity of book \n")
                                    if validation_numbers(book_quantity,int):
                                        for i in library_inventory:
                                            if book_title in i:
                                                if int(book_quantity)>int(i[book_title]["quantity"]):
                                                    print("The book does not have enough quantities")
                                                    print(f"quantity the book: {i[book_title]["quantity"]}")
                                                    continue
                                                else:
                                                    i[book_title]["quantity"]=int(i[book_title]["quantity"])-int(book_quantity)
                                                    register_book_sale(book_title,name_client,int(book_quantity),i[book_title]["author"],(int(i[book_title]["price"])*int(book_quantity)))
                                                    print("=== Book buy successfully ===")
                                                    break
                                    break
                                break
                            else:
                                print("🚫 Book not found. Please try again.")
                        
            case "3":
                match opciones_menu[1]:
                    case "1":

                        get_three_best()
                    case "2":

                        print("===💸 Total sales grouped by author 💸===")
                        book_author=input("-Enter the name of the author who wants to make the report\n")
                        sales_report_by_author(book_author)
                    case "3":
                        print("===💸 Total value of books sold 💸===")
                        calculate_sales_value_total()
                    case "4":
                        show_all_books_sells()
main()