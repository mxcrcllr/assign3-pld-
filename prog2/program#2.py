def calculate_max_apples(apple_price, money):
    max_apples = money // apple_price
    remaining_money = max_apples * apple_price - money
    return (max_apples, remaining_money)

from pyfiglet import Figlet
invita = Figlet(font='invita')
mini = Figlet(font='mini')
digital = Figlet(font='digital')

print(invita.renderText("Hello customer!\n"))

money = float(input("Enter the amount of money you have right now: "))
apple_price = float(input("Enter the price of an apple: "))
max_apples, remaining_money = calculate_max_apples(apple_price,money)

print(mini.renderText(f"\nYou can buy {max_apples} apples"))
print(mini.renderText(f"You will be left with {remaining_money} pesos"))

