while True:
    
    try:
        x = int(input("Please enter a number"))
        break
    except Exception:
        print("Oops! That was not a valid number .try again ...")
        
num = int(input("pleas enter a number greater than ten :"))
if num <= 10:
    raise Exception(f'num value ({num}) is less than or equal to 10')
    


