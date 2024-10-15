def free_shipping(age, prime_status, purchase_amount, parent_consent):
    if (prime_status == True or purchase_amount > 25) and (age >= 18 or parent_consent == True):
        print("free shipping applied!")
    else:
        print("ineligible for free shipping")

p = bool(input("Do you have Prime?\n>"))
cos = int(input("How much did it cost?\n>"))
a = int(input("how old are you?\n>"))
con = bool(input("Do you have your parent's consent to purchase?\n>"))

free_shipping(a, p, cos, con)