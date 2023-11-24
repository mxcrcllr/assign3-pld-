from art import *
from fancify_text import *
from colorama import Fore, Back, Style, init
init()

def calculate_cost(apple_quantity, orange_quantity):
    apple_price = 20
    orange_price = 25
    return (apple_price * apple_quantity) + (orange_price *orange_quantity)

tprint("Welcome  customer!\n")

apple_quantity = int(input(f"{Style.BRIGHT}{Fore.CYAN}{Back.MAGENTA}How many apples do you wanna buy?{Style.RESET_ALL} "))
orange_quantity = int(input(f"\n{Style.BRIGHT}{Fore.MAGENTA}{Back.CYAN}How many oranges do you wanna buy?{Style.RESET_ALL} "))
total = calculate_cost(apple_quantity, orange_quantity)

print(wide(f"\nThe total amount is {total} pesos"))
