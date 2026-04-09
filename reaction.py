# Import required libraries for GPIO control, time delay, and random number generation
from gpiozero import LED, Button
from time import sleep
from random import uniform

# Hardware pin definition (Raspberry Pi GPIO numbering)
led = LED(4)                # LED connected to GPIO pin 4
left_btn = Button(14)       # Left player button connected to GPIO pin 14
right_btn = Button(15)      # Right player button connected to GPIO pin 15

# Get player names from user input
left_name = input("Left Player Name: ")
right_name = input("Right Player Name: ")

# Main game logic start
print("Ready! Press the button quickly after the LED turns off!")
led.on()  # Turn on the LED to signal game preparation
# Random delay between 5 and 10 seconds to increase game randomness
sleep(uniform(5, 10))
led.off() # Turn off the LED, start the reaction challenge

# Define the function to determine the winner and exit the program
def win(button):
    # Check which button was pressed
    if button.pin.number == 14:
        print(f"{left_name} wins the game!")
    else:
        print(f"{right_name} wins the game!")
    exit()  # Terminate the program after declaring the winner

# Bind button press events to the win function
left_btn.when_pressed = win
right_btn.when_pressed = win
