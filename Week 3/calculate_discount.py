# calculate_discount.py

# ---------------------------------------------------------------------------------------------------------------------
# Author:   Oguntuase Victor
# email:    freelanceel0@gmail.com
# ---------------------------------------------------------------------------------------------------------------------
# Assignment:   PLP-Python Module, Cohort 4, Week 3.
# Instructions: Create a function named calculate_discount(price, discount_percent) that calculates the final price 
#               after applying a discount. The function should take the original price (price) and the discount 
#               percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; 
#               otherwise, return the original price.

#               Using the calculate_discount function, prompt the user to enter the original price of an item 
#               and the discount percentage. Print the final price after applying the discount, 
#               or if no discount was applied, print the original price.

# ---------------------------------------------------------------------------------------------------------------------

def get_final_price():
    """ Docstring: This function prompts the user to enter values for price and discount_percent and returns the final price.

        Args: none

        Returns:
            final-price -> str
    """
    splash_msg = """
                                .-----------------------------------------------------.
                                | FINAL PRICE CALCULATOR BASED ON APPLICABLE DISCOUNT |
                                *-----------------------------------------------------*

[INFO]: This program calculates a final value for an item based on applicable discount. Remember to enter the discount in a percentage value
        i.e. enter 20 for a 20% discount.
                """
    print(splash_msg)
    RUNNING = True
    counter = 1

    # CREATING A LOOP TILL USER EXITS
    while RUNNING:
        print("\nEnter the Original Price of the Item: ")
        price = float(input(">> "))
        print("\nEnter the applicable discount in percentage: ")
        discount = float(input(">> "))
        print(f"\nThe final price for this item is {calculate_discount(price, discount):.2f} ")
        
        VALID_CHOICE = False

        while not VALID_CHOICE:
            print("\n\n[Alert]: Would you like to calculate discount for another item?\n\t Enter 1 or 2.\n[1] Yes\n[2] No\n")
            choice = input(">> ")

            # updating the loop breakers
            VALID_CHOICE = True if (choice == "1" or choice == "2") else False
            if not VALID_CHOICE:
                print("\n[Error]: Please make a valid selection by entering 1 or 2 at the prompt!")
            else:
                if choice == "1":
                    print("\n[Info]: Now running the program for new inputs!")
                else:
                    RUNNING = False
            
    

def calculate_discount(price, discount_percent):
    """ Docstring: This function returns a discounted price if discount is at least 20%.

        Args:
            price -> int, discount_percent -> int : Original price of item and applicable discount percentage.

        Returns:
            final-price -> int
    """
    return price if discount_percent < 20 else price * (1 - discount_percent/100)


def main():
    return get_final_price()


if __name__ == "__main__":
    main()