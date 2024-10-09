wind_speed = int(input("What is the wind speed of the hurricane?\n>"))


if wind_speed < 74:
    print("The hurricane is a Tropical Storm")

elif wind_speed < 96:
    print("The hurricane is Category 1")

elif wind_speed < 111:
    print("The hurricane is Category 2")

elif wind_speed < 130:
    print("The hurricane is Category 3")

elif wind_speed < 157:
    print("The hurricane is Category 4")

elif wind_speed >= 157:
    print("The hurricane is Category 5")

else:
    print("not a valid wind speed")