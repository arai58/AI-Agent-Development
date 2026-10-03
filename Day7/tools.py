from datetime import datetime
import random
import string
import secrets

#Get current time - system time
def get_current_time():
    return datetime.now().strftime("%d-%m-%Y %l:%M:%S %p")


#Dice Roller
def roll_dice():
    return random.randint(1,6)


#Generate Password
def generate_password():

    length=12
    character_list=(string.ascii_letters + string.digits + string.punctuation)

    password=""

    for _ in range(length):
        password+=secrets.choice(character_list)

    return password

