# This program will be able to convert from one currency to another.


    
NGN_to_USD = 700
NGN_to_EUR = 850

msg = """
Welcome to our currency converter app.

Amount (NGN): #{user_amount}
Amount (EUR): ${amount_eur}
Amount (USD): &{amount_usd}

"""

def convert_to_USD(from_value):
    amount_in_dollar = float(from_value) * NGN_to_USD
    return amount_in_dollar

def convert_to_EUR(from_value):
    amount_in_euro = float(from_value) * NGN_to_EUR
    return amount_in_euro

#allow user input
amount_in_naira = input("Enter amount (NGN): ")
     
#invoke function
to_value_USD = convert_to_USD(amount_in_naira)
to_value_EUR = convert_to_EUR(amount_in_naira)

print("enter in naira")
#print(to_value_USD)
#print(to_value_EUR)
print(msg.format(user_amount=amount_in_naira, amount_eur=to_value_EUR, amount_usd=to_value_USD))