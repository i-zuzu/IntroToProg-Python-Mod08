# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# IZubova,3.7.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = '' # Captures the user option selection
strStatus = '' # Captures the status of the processing functions

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        IZubova,3.7,2021,Modified code to complete assignment 8
    """

    #-- Constructor --
    def __init__(self):
        self.__str_prod_name = ''
        self.__flt_prod_price = None

    # -- Properties --
    # prod_name
    @property
    def str_prod_name(self): # (getter or accessor)
        return str(self.__str_prod_name).title()  # Title case

    @str_prod_name.setter  # The NAME MUST MATCH the property's!
    def str_prod_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__str_prod_name = value.strip()
        else:
            raise Exception("Names cannot be numbers")

                # prod_price
    @property
    def flt_prod_price(self):  # (getter or accessor)
        return self.__flt_prod_price  # Title case

    @flt_prod_price.setter  # The NAME MUST MATCH the property's!
    def flt_prod_price(self, value):  # (setter or mutator)
        try:
            self.__flt_prod_price = float(value)
        except ValueError:
            raise Exception("Price should be a float number, instead {value} provided")

    # def __str__(self):
    #     return self.__str_prod_name + " " + str(self.__flt_prod_price)



# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        IZubova,3.7,2021,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows

            :param file_name: (string) with name of file:
            :param lstOfProductObjects: (list) you want filled with file data:
            :return: (list) of rows
        """
        lstOfProductObjects.clear()  # clear current data
        try:
            with open(file_name, "r") as file:
                for line in file:
                    prod, price = line.split(",")
                    objNewProd = Product()
                    objNewProd.str_prod_name =  prod
                    objNewProd.flt_prod_price =  price
                    lstOfProductObjects.append(objNewProd)
        except (FileNotFoundError):
            print ("\n Text file is not created\n")
        return lstOfProductObjects, 'Success'

    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        """ Saves data to a file from list of dictionary rows

            :param file_name: (string) with name of file:
            :param lstOfProductObjects: (list) you want write to file:
            :return: (list) of rows
        """
        with open(file_name, "w") as file:
            for row in lstOfProductObjects:
                file.write(row.str_prod_name + ", " + str(row.flt_prod_price)+ '\n')
        return lstOfProductObjects, 'Success'


# Processing  ------------------------------------------------------------- #
class Processor:
    """Processes product and price data to add it to the list:

    methods:
        add_data_to_list(lstOfProductObjects, prod, price):

    changelog: (When,Who,What)
        IZubova,3.7,2021,Modified code to complete assignment 8
    """

    @staticmethod
    def add_data_to_list(lstOfProductObjects, prod, price):
        """ Reads data from a file into a list of dictionary rows

            :param file_name: (string) with name of file:
            :param list_of_product_objects: (list) you want filled with file data:
            :return: (string) Success/Fail
        """
        try:
            objNewProd = Product()
            objNewProd.str_prod_name = prod
            objNewProd.flt_prod_price = price
            lstOfProductObjects.append(objNewProd)
        except Exception as e:
            # print(e)
            print('Bad format.')
            return 'Fail'
        return 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks:

       methods:
           print_menu_Tasks():
           input_menu_choice():
           print_current_Tasks_in_list():
           input_new_prod_and_price():
           input_press_to_continue(optional_message=''):
           input_yes_no_choice(message)

       changelog: (When,Who,What)
           IZubova,3.7,2021,Modified code to complete assignment 8
       """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user
            :return: nothing
        """
        print('''
            Menu of Options
            1) Show current data
            2) Add data to the list of product objects
            3) Save Data to File and Exit        
            ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
            :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice


    @staticmethod
    def print_current_Tasks_in_list(lstOfProductObjects):
        """ Shows the current Tasks in the list of dictionaries rows

            :param list_of_product_objects: (list) of rows you want to display
            :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in lstOfProductObjects:
            print(row.str_prod_name + ", " + str(row.flt_prod_price))
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_prod_and_price():
        """ Gets the name of a new task and priority to add to the list from a user
            :return: string, string
        """
        prod = input("Enter the product: ")
        price = input("Enter the price: ")
        return prod, price

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from strFileName.
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
IO.print_current_Tasks_in_list(lstOfProductObjects)  # Show current data in the list

while(True):
    # Step 2 - Display a menu of choices to the user
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 3 Show current data
    if strChoice.strip() == '1':  # Print current data
        IO.print_current_Tasks_in_list(lstOfProductObjects)  # Show current data in the list/table
        continue

    # Step 4 - Add new product and price
    if strChoice.strip() == '2':  # Add a new product and price
        prod, price = IO.input_new_prod_and_price()
        result = Processor.add_data_to_list(lstOfProductObjects, prod, price)
        if result == 'Success':
            strStatus = "\n Product added.\n"
        else:
            strStatus = '\n Product was not added.\n'
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # Step 5 - Save product and price and exit
    if strChoice == '3':             # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            strStatus = "\n Data saved to file.\n"
            IO.input_press_to_continue(strStatus)
            break
        else:
            IO.input_press_to_continue("Save Cancelled!")
            break
print('\n Good bye!')