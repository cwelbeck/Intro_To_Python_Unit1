def order(color, size):
    if color.lower() == "white":
        if(size.lower() == "l" or size.lower() == "m"):
            print("Available")
        else:
            print("Unavailable")
    elif color.lower() == "blue":
        if(size.lower() == "m" or size.lower() == "s"):
            print("Available")
        else:
            print("Unavailable")
    else:
        print("Not Available")

#order()
