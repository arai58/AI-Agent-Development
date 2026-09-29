from tools import roll_dice,generate_password,get_current_time


print(get_current_time()," : dice rolled and yoohoo you got : ", roll_dice())
password_length=int(input(f"{get_current_time()} : Enter size of password you want : "))
print(get_current_time(),f" : password generated of {password_length} chars : ",generate_password(password_length))