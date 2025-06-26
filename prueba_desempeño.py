from datetime import date

library_inventory=[]
book_categories=["Horror", "love", "fiction", "action", "fantasy"]
sales_history=[]




#===============
#-BUSINESS LOGIC
#===============


def add_book_inventory(book_title,book_author,book_category,book_price,book_quantity):
    """
    This function saves an entire book into the main book library dictionary.
    #IMPORTANT#
    -The key to every book is its own title.
    -The structure list(dictionary(dictionaries)) is being used
    """
    library_inventory.append({book_title:{
        "author":book_author,
        "category":book_category,
        "price":book_price,
        "quantity":book_quantity
    }})



def search_book(book_name):
    """
    This function searches for a specific book within the main book library.
    """
   
    for i in library_inventory:
        if book_name in i:
                print("=== Book Found ===")
                print(f"📕 Title: {book_name}")
                print(f"🧑 Author: {i[book_name]["author"]}")
                print(f"📋 Categorie: {book_categories[int(i[book_name]["category"])]}")
                print(f"💸 Price: {i[book_name]["price"]}")
                print(f"📦 Stock: {i[book_name]["quantity"]}")
                print("=====================")
                return True
        
    print("🚫 Book not found")
    return False



def update_book_property(book_name,new_value,parameter):
    """
    This function updates a property of a book, 
    it grabs the name of the book with the new value and the parameter that will change
    """
    
    for i in library_inventory:
        if book_name in i:
            i[book_name][parameter]=new_value
            return True
        
    return False



def delete_book(book_name):
    """
    This function deletes a book from the main library of books, 
    it takes the name of the book and looks for a dictionary 
    in the list of the library where all the books are.
    """
    
    for i in library_inventory:
        if book_name in i:
            library_inventory.remove(i)
            print(f"✅ The Book '{book_name}' was successfully deleted.")
            return True
        
    print("🚫 Book not found.")
    return False



def register_book_sale(book_name,name_cliente,quantity_sell,book_author,purcharse_total):
    """
    This function records a new sale in the sales history list and also displays the final invoice for the book sale.
    """

    if quantity_sell>3:
        descuent=10
    elif quantity_sell>5:
        descuent=20
    else:
        descuent=0
    p_t=((purcharse_total*descuent)/100)-purcharse_total
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
    print("============================")
    print("== 💸 Purcharse receipt 💸==")
    print(f"🧑 customer: {name_cliente}")
    print(f"📕 Title book: {book_name}")
    print(f"📦 Quantity sell: {quantity_sell}")
    print(f"🗓️ Sale date: {date.today()}")
    if descuent>0:
        print(f"💸 descuent of {descuent}: {(purcharse_total*descuent)/100}")
        print(f"==TOTAL VALUE==")
        print(p_t)
    else:
        print(f"💸 descuent: does not apply ")
        print(f"==TOTAL VALUE==")
        print(p_t)



def get_three_best():
    """
    This function searches for the top 3 best-selling books using the list of books sold history.
    """
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
    """
    This function calculates the total value collected from all sales.
    """
    total_sales_value=0
    total_sales_value_with_descuent=0
    total_quantity_value=0
    for i in sales_history:
        total_quantity_value+=int(i["quantity_sell"])
        total_sales_value+=i["purcharse_total"]
        total_sales_value_with_descuent+=(i["purcharse_total"]-(i["purcharse_total"]*int(i["descuent"])/100))
    print(f"-Total money obtained {total_sales_value}")
    print(f"-Total quantity sold {total_sales_value}")
    print(f"-Total quantity sold with descuent {total_sales_value_with_descuent}")




#=====================
#-VALIDATION FUNCTIONS
#=====================
def validation_numbers(value,tipe):
    """
    This function allows you to validate a value as an integer or float.
    """
    try:
        return True if tipe(value)>-1 else print("only can values positive")
    except:
        if tipe==float:
            print(f"only can of values positive and float")
        else:
            print(f"only can of values positive and numbers in the range")
            
        return False
    


def validation_equality_book(book_title):
    """
    This function allows you to know if a book already exists in the book library.
    """
    for i in library_inventory:
        if book_title in i:
            return True
        
    return False



def validate_book_in_stock(book_title):
    """
    This function allows you to know if a book has stock to be sold.
    """
    for i in library_inventory:
        if book_title in i:
            if int(i[book_title]["quantity"])==0:
                return True
            
    return False


#==============
#-MENU INTERFAZ
#==============
def sales_report_by_author(autor):
    """
    This feature allows you to search for the total value sold by a specific author in the sales history.
    """
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
    """
    This function shows all categories of books
    """

    print("--📚 \033[92m BOOK CATEGORIES \033[0m 📚--")
    for i,name in enumerate(book_categories):
        print(f"-{i}: {name}")



def show_all_books_sells():
    """
    This feature shows the history of books sold
    """

    if not sales_history:
        print("🚫 The history sales is empty.")
        return False
    print("=== 🗂️ \033[33mAll Books sells\033[0m ===")
    for book_sell in sales_history:
        print(f"🧑 customer: {book_sell['customer']}")
        print(f"📕 Title book: {book_sell['book_sell']}")
        print(f"📦 Stock: {book_sell['quantity_sell']}")
        print(f"🗓️ Sale date: {book_sell['date']}")
        if int(book_sell['descuent'])>0:
            print(f"💸 descuent of {book_sell['descuent']}: {(int(book_sell['purcharse_total'])*int(book_sell['descuent']))/100}")
            print(f"💰 purcharse_total: {book_sell['purcharse_total']}")
        else:
            print(f"💸 descuent: does not apply ")
            print(f"💰 purcharse_total: {book_sell['purcharse_total']}")
        print(f"✍️ author_book: {book_sell['author_book']}")
        print("-" * 30)
        #  "descuent":descuent,
        #  "author_book":book_author,
        #  "purcharse_total":purcharse_total

def show_all_books():
    """
    This function shows all the books that are in the bookstore's inventory.
    """

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
    """
    This function shows the main menu which is divided into 3 modules 
    with different functions allowing for separation and a much more organized menu.
    """
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

        #IMPORTANT#
        #This function returns a tuple specifying which function was selected plus the module it was in.
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
                    print("1.Display the top 3 best-selling books.")
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
    """
    This is the main function which has a similarity in the menu structure when executing the functions of each module.
    """
    while True:
        opciones_menu=menu_interface()
        match opciones_menu[0]:
            
            #-------------------------START MODULE 1-------------------------
            case "1":
                match opciones_menu[1]:

                    #BOX 1 where the code is executed to add a new book
                    case "1":
                        print("="*30)
                        print("=== 📦\033[36mAdd a book\033[0m📦 ")

                        #Validation to know if the book exists
                        while True:
                            book_title=input("-Name of book \n")
                            if validation_equality_book(book_title):
                                print("\033[31m !the book already exists! \033[0m!")   
                            else:
                                break
                       #-----------------------------------------

                        book_author=input("-Name of book author\n")

                        #Category selection part by category list ID
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
                        #-----------------------------------------

                        #Validation of prices and quantities using the numbers validation function
                        while True:
                            book_price=input("-Price of book \n")
                            if validation_numbers(book_price,int):
                                break
                    
                        while True:
                            book_quantity=input("-Amount of book \n")
                            if validation_numbers(book_quantity,int):
                                break
                        #-----------------------------------------

                        #THE NEW BOOK IS ADDED AT THE END
                        add_book_inventory(book_title,book_author,book_categorie,book_price,book_quantity)


                    #BOX 2 where the code is executed to search for a book
                    case "2":
                        print("=== 📦\033[36mSearch a book\033[0m📦 ")
                        if show_all_books()==False:
                            continue   
                        book_name=input("-Title of book to Search details\n")
                        search_book(book_name)
                  

                    #BOX 3 where the function is executed to show all the books in the inventory
                    case "3":
                        show_all_books()
                  
                  
                    #BOX 4 where the code is executed to update the price of a product
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
                            update_book_property(book_title,book_price,"price")
                            print("=== Book price updated successfully ===")
                        else:
                            print("🚫 Book not found. Please try again.")


                    #BOX 5 where the code is executed to update the quantity of a product
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
                                update_book_property(book_title,int(book_quantity),"quantity")
                                print("=== Book quantity updated successfully ===")
                                break
                            else:
                                print("🚫 Book not found. Please try again.")
                  

                   #BOX 6 where the function to delete a book is executed
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

            #-------------------------END MODULE 1-------------------------     
            
            
            #-------------------------START MODULE 2------------------------- 
            case "2":
                match opciones_menu[1]:
                    #BOX 1 where the code is executed to register a sale
                    case "1":
                        print("=== 💲\033[Register book sale\033[0m💲 ===") 
                        if show_all_books()==False:
                            continue    
                        while True:
                            book_title=input("-Title of book to buy \n") 

                            #Validation to know if the book exists
                            if validation_equality_book(book_title):

                                #Validation to know if the book is in stock
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
            #-------------------------END MODULE 2-------------------------     

            #-------------------------START MODULE 3------------------------- 
            case "3":
                match opciones_menu[1]:
                    #BOX 1 where the code is executed to see the 3 best-selling products
                    case "1":
                        get_three_best()

                    #BOX 2 where the code is executed to see the sales history of an author
                    case "2":
                        print("===💸 Total sales grouped by author 💸===")
                        book_author=input("-Enter the name of the author who wants to make the report\n")
                        sales_report_by_author(book_author)
                    
                    #BOX 3 where the code is executed to see the total number of books sold
                    case "3":
                        print("===💸 Total value of books sold 💸===")
                        calculate_sales_value_total()
                    
                    #BOX 4 where the history of books sold is shown
                    case "4":
                        show_all_books_sells()
            #-------------------------END MODULE 3-------------------------     




#Execution of the main function
main()