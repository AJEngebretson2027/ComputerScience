# AMAZON FREE SHIPPING ELIGIBILTY SYSTEM
# loyalty customers OR purchases of over $25
# under 18, you need a parent consent to purchase

def free_shipping(age, prime_status, purchase_amount, parent_consent):
    if (prime_status == True or purchase_amount > 25) and (age >= 18 or parent_consent == True):
        print("free shipping applied!")
    else:
        print("ineligible for free shipping")

p = False
cos = 100
a = 12
con = True

free_shipping(a, p, cos, con)