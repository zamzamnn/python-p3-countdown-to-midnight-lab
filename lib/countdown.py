
import time  # Add this import statement

def countdown(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number > 0:
        print(f"{number} SECOND(S)!")
        time.sleep(1)  # Delay for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")
