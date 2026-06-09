"""
This programme has been designed to perform three functions. The first is to generate a 
Diceware-style password (a password generator that uses words). The second is to enter 
your own password and assess how secure it is. The third is to compare the two so that 
users can draw their own conclusions.
"""

import random # Required for password creation
import math # Required for bits calculations
import os # Required to open .txt file and clean the terminal
import time # Required to add delays between lines

# Colour palette
CYAN    = "\033[96m"  # A very bright electric sky blue
GREEN   = "\033[92m"  # A neon green
YELLOW  = "\033[93m"  # A very clean, bright golden shade
RED     = "\033[91m"  # A deep crimson shade
MAGENTA = "\033[95m"  # A very modern bright purple
WHITE   = "\033[97m"  # A pure white
GRAY    = "\033[90m"  # A dark ash tone
# Text style
BOLD    = "\033[1m"   # Double the thickness and brightness
UNDER   = "\033[4m"   # Color + a solid line underneath
RESET   = "\033[0m"   # Turns off the colour so the rest of the PC isn’t coloured

def main():
    # If it detects that you are running Windows (‘nt’), it initialises the console to process ANSI, so that you can use colours without any problems or the need for installation
    if os.name == "nt":
        os.system("") # When a user runs this programme on a Windows system, the condition will become true, and the line will be activated

    # Load the list just once at the start
    base_dictionary = os.path.dirname(os.path.abspath(__file__)) # Get the folder where this script is saved (Final_work.py)
    file_path = os.path.join(base_dictionary, "diceware.txt") # Concatenates that folder with the filename
    dictionary = load_dictionary(file_path) # Now loads the dictionary using the full path
    
    # Start the program
    while True: 
        show_menu()
        opcion = get_int_input(f"{MAGENTA}Choose you would try:{RESET} ", 1, 4) # Any selection other than 1 to 4 will result in an error
        # It helps you to create strong passwords that are hard to hack but easy to remember
        if opcion == 1: 
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to enter the diceware module
            show_menu_diceware()
            opcion = get_int_input(f"{MAGENTA}Choose you would try:{RESET} ", 1, 2) # Any selection other than 1 to 2 will result in an error
            if opcion == 2:
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
                continue
            else: # Password contruction
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to start a diceware password
                num_words = get_int_input(f"{MAGENTA}How many words do you want in your phrase? (recomended 5 or +):{RESET} ", 1, 10) # Any selection other than 1 to 10 will result in an error

                # Roll the dice as many times as the user has said
                print(f"\n{CYAN}Throwing the dices...{RESET}")
                time.sleep(1)
                password_list = [] # We create an empty list to store the selected words
                for i in range(num_words):
                    code = finding_words() # Return number between 11111 and 66666
                    word = dictionary.get(code, "") # We are looking for a code in our list
                    time.sleep(0.4) # One second delay
                    print(f"{CYAN}Throw {i+1}: Dice... {code} -----> Word: {RESET} {WHITE}{word}{RESET}") # Print step by step instructions for the user to see
                    password_list.append(word) # We add the result to the list created before the loop
                time.sleep(1)
                print(f"\n{CYAN}Your password selected are{RESET}: {WHITE}{'-'.join(password_list)}{RESET}")
                time.sleep(1)
                
                # Shannon's mathematical formula (adapted by Arnold Reinhold) for entropy: E = N * log2(7776)
                # E = Bits; N = number of words; 7776 = 6^5 possible words with dice; Log2(7776) = 12'92 bits
                final_bits_diceware = num_words * math.log2(7776)
                print(f"\n{CYAN}{UNDER}ENTROPY CALCULATOR{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}Power:{RESET} {WHITE}{final_bits_diceware:.2f}bits{RESET}")
                time.sleep(1)
                
                # Calculate the result
                real_speed = 10_000_000_000_000 # Calculations have been made based on the theory. This constant serves to illustrate that reality is very different with current technology
                combinations = 7776 ** num_words # Calculate the total number of combinations for the dictionary attack
                time_diceware = combinations / real_speed # Calculate the total time in seconds
                final_time_diceware, unit_diceware = temporary_adjustment(time_diceware) # Convert the time in seconds to the correct unit (hours, days, etc.)
                
                # Conclusion (Green-yellow-red) and advice
                print(f"\n{CYAN}If the hacker KNOW you use that sort of password...{RESET}\n")
                time.sleep(1)
                if num_words < 5:
                    print(f"{CYAN}{UNDER}THIS PASSWORD IS:{RESET} {RED}RED{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}Estimated time to crack (with dictionary):{RESET} {WHITE}{final_time_diceware:.2g} {unit_diceware}{RESET}") # The result is displayed
                    time.sleep(0.4)
                    print(f"{CYAN}These days, even fewer than 5 random words can be easily cracked{RESET}") # Advice
                elif num_words < 7:
                    print(f"{CYAN}{UNDER}THIS PASSWORD IS:{RESET} {YELLOW}YELLOW{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}Estimated time to crack (with dictionary):{RESET} {WHITE}{final_time_diceware:.2g} {unit_diceware}{RESET}") # The result is displayed
                    time.sleep(0.4)
                    print(f"{CYAN}Ideal for everyday use. It is secure and very easy to remember{RESET}") # Advice
                else:
                    print(f"{CYAN}{UNDER}THIS PASSWORD IS:{RESET} {GREEN}GREEN{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}Estimated time to crack (with dictionary):{RESET} {WHITE}{final_time_diceware:.2g} {unit_diceware}{RESET}") # The result is displayed
                    time.sleep(0.4)
                    print(f"{CYAN}This phrase is completely immune to modern brute-force attacks{RESET}") # Advice

                # End the module
                time.sleep(1)
                input(f"\n{GRAY}---\nPress Enter to return to the menu...{RESET}")
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu

        # It helps you to check any posswords is it strong or not
        elif opcion == 2:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to enter the analyser module
            show_menu_analyser()
            opcion = get_int_input(f"{MAGENTA}Choose you would try:{RESET} ", 1, 2) # Any selection other than 1 to 2 will result in an error
            if opcion == 2:
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
                continue
            else: # Password contruction
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to start the password analyser
                password_user = input(F"{MAGENTA}Put any password:{RESET} ") # Ask for any password the user chooses
                
                # Check if user put any character
                if len(password_user) == 0:
                    print(f"\n{RED}No characters were found{RESET}")
                    input(f"\n{GRAY}---\nPress Enter to return to the menu...{RESET}")
                    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
                    continue # Jump to main menu

                # How long is the user password
                print(f"\n{CYAN}This password contains{RESET} {WHITE}{len(password_user)}{RESET} {CYAN}characters{RESET}") # "len()" help to add strings
                password_length = len(password_user)
                time.sleep(1)
                # Specify whether the user password contains uppercase letters, lowercase letters, numbers and special character for the bit calculations
                rang = 0
                rang += check_password_islower(password_user, True)
                time.sleep(0.4)
                rang += check_password_isupper(password_user, True)
                time.sleep(0.4)
                rang += check_password_isdigit(password_user, True)
                time.sleep(0.4)
                rang += check_password_isalnum(password_user, True)
                time.sleep(1)
                
                # If the user enters something very unusual and it returns 0, we assign a minimum value of 1 to avoid an error in log2
                if rang == 0: 
                    rang = 1

                # Shannon's mathematical formula for entropy: E = L * log2(R)
                # E = Bits; L = Number of characters; R = Rang: Mayus (26 opcions); Minus (26 opcions); Numbers (10 opcions); symbols (32 opcions)
                final_bits = password_length * math.log2(rang)
                print(f"\n{CYAN}{UNDER}ENTROPY CALCULATOR{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}Power:{RESET} {WHITE}{final_bits:.2f}bits{RESET}")
                time.sleep(1)
                
                # Protective capacity. I made up the following table because I couldn't find an official one 
                # (other than the fact that 40 is weak and 120 is strong)
                print(f"\n{CYAN}{UNDER}RESILIENCE TO ATTACKS{RESET}")
                time.sleep(0.4)
                entropy_thermometer(final_bits)
                time.sleep(1)

                # Estimated time to crack a password (T = R(L)/V)
                # "Time to crack (T) equals the size of the character pool (R) raised to the power of the Length (L), divided by the Guessing Velocity (V)."
                theoric_calculations_domestic_pc, theoric_calculations_supercomputer, theoric_calculations_hacker_farm = time_calculations_diferents_PC(final_bits)
                
                # Changes theoric for real speed (the reality is very different with today’s technology)
                real_acceleration = 1_000 # Simulates the jump from CPU to high-performance GPU hacking (like Hashcat or John the Ripper)
                real_calculations_domestic_pc = theoric_calculations_domestic_pc / real_acceleration
                real_calculations_supercomputer = theoric_calculations_supercomputer / real_acceleration
                real_calculations_hacker_farm =  theoric_calculations_hacker_farm / real_acceleration
                
                # Changes real for predictable password speed
                predictable_acceleration = 10_000 # Simulates smart dictionary attacks that target human predictable pattern
                predictable_calculations_domestic_pc = real_calculations_domestic_pc / predictable_acceleration
                predictable_calculations_supercomputer = real_calculations_supercomputer / predictable_acceleration
                predictable_calculations_hacker_farm =  real_calculations_hacker_farm / predictable_acceleration

                # Change the real bits obtained into other paramethers to undertand them better: seconds, minutes, hours, days, years...
                # Domestic PC
                theoric_final_time_calculations_domestic_PC, theoric_time_pc = temporary_adjustment(theoric_calculations_domestic_pc)
                real_final_time_calculations_domestic_PC, real_time_pc = temporary_adjustment(real_calculations_domestic_pc)
                predictable_final_time_calculations_domestic_PC, predictable_pc_time = temporary_adjustment(predictable_calculations_domestic_pc)
                # Supercomputer
                theoric_final_time_calculations_supercomputer, theoric_supercomputer_time = temporary_adjustment(theoric_calculations_supercomputer)
                real_final_time_calculations_supercomputer, real_supercomputer_time = temporary_adjustment(real_calculations_supercomputer)
                predictable_final_time_calculations_supercomputer, predictable_supercomputer_time = temporary_adjustment(predictable_calculations_supercomputer)
                # Hacker farm
                theoric_final_time_calculations_hacker_farm, theoric_hacker_farm_time = temporary_adjustment(theoric_calculations_hacker_farm)
                real_final_time_calculations_hacker_farm, real_hacker_farm_time = temporary_adjustment(real_calculations_hacker_farm)
                predictable_final_time_calculations_hacker_farm, predictable_hacker_farm_time = temporary_adjustment(predictable_calculations_hacker_farm)
                
                # Show the results comparing theory with practice (:.2g is the smart way in Python where it decides which notation to use)
                print(f"\n{CYAN}{UNDER}ESTIMATED TIME TO CRACK A PASSWORD{RESET}")
                time.sleep(0.4)
                # Domestic PC + time
                print(f"{CYAN}-- THEORIC -- Domestic PC:{RESET} {WHITE}{theoric_final_time_calculations_domestic_PC:.2g} {theoric_time_pc}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}-- REAL -- Domestic PC:{RESET} {WHITE}{real_final_time_calculations_domestic_PC:.2g} {real_time_pc}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}-- PREDICTABLE -- Domestic PC:{RESET} {WHITE}{predictable_final_time_calculations_domestic_PC:.2g} {predictable_pc_time}{RESET}")
                print("")
                time.sleep(1)

                # Supercomputer + time
                print(f"{CYAN}~~ THEORIC ~~ Supercomputer:{RESET} {WHITE}{theoric_final_time_calculations_supercomputer:.2g} {theoric_supercomputer_time}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}~~ REAL ~~ Supercomputer:{RESET} {WHITE}{real_final_time_calculations_supercomputer:.2g} {real_supercomputer_time}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}~~ PREDICTABLE ~~ Supercomputer:{RESET} {WHITE}{predictable_final_time_calculations_supercomputer:.2g} {predictable_supercomputer_time}{RESET}")
                print("")
                time.sleep(1)
                
                # Hacker farm + time
                print(f"{CYAN}** THEORIC ** Hacker farm:{RESET} {WHITE}{theoric_final_time_calculations_hacker_farm:.2g} {theoric_hacker_farm_time}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}** REAL ** Hacker farm:{RESET} {WHITE}{real_final_time_calculations_hacker_farm:.2g} {real_hacker_farm_time}{RESET}")
                time.sleep(0.4)
                print(f"{CYAN}** PREDICTABLE ** Hacker farm:{RESET} {WHITE}{predictable_final_time_calculations_hacker_farm:.2g} {predictable_hacker_farm_time}{RESET}")
                print("")
                time.sleep(1)

                # Conclusion (Green-yellow-red) and suggestion
                if final_bits < 80:
                    print(f"{CYAN}THIS PASSWORD IS:{RESET} {RED}RED{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}I recommend that you change your password as soon as possible{RESET}")
                elif final_bits < 120:
                    print(f"{CYAN}THIS PASSWORD IS:{RESET} {YELLOW}YELLOW{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}I recommend you set a stronger password{RESET}")
                else:
                    print(f"{CYAN}THIS PASSWORD IS:{RESET} {GREEN}GREEN{RESET}")
                    time.sleep(0.4)
                    print(f"{CYAN}Your password is very strong{RESET}")

                # End the module
                time.sleep(1)
                input(f"\n{GRAY}---\nPress Enter to return to the menu...{RESET}")
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu

        # Helps you compare the two types of passwords
        elif opcion == 3:
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to enter the comparison module
            show_menu_comparison()
            opcion = get_int_input(f"{MAGENTA}Choose you would try:{RESET} ", 1, 2) # Any selection other than 1 to 2 will result in an error
            if opcion == 2:
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
                continue
            else:
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to start a comparative password
                user_comparison = input(f"{MAGENTA}Put any password:{RESET} ") # Request a password and perform the calculations
                
                # Check if user put any character
                if len(user_comparison) == 0:
                    print(f"\n{RED}No characters were found{RESET}")
                    input(f"\n{GRAY}---\nPress Enter to return to the menu...{RESET}")
                    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
                    continue # Jump to main menu

                # Enter the number of words for diceware password
                diceware_comparison = get_int_input(f"{MAGENTA}How many words would the Diceware phrase have for comparison? {RESET}", 1, 10) # Any selection other than 1 to 10 will result in an error
                time.sleep(0.4)

                # Start comparison between analyser password and diceware password
                bits_for_metaphor = check_password_comparison(dictionary, user_comparison, diceware_comparison)

                # It displays a metaphor depending on how strong the chosen password is
                print(f"{CYAN}\n{"~"*40}\n\n{UNDER}UNDERTANDING YOUR SAFETY THROUGH METAPHORS{RESET}\n")
                time.sleep(1)
                metaphors_about_analyser(bits_for_metaphor) # metaphor through bits
                metaphors_about_diceware(diceware_comparison) # metaphor through the number of words

                # End the module
                time.sleep(1)
                input(f"\n{GRAY}---\nPress Enter to return to the menu...{RESET}")
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen to come back the main menu
        # End the program
        elif opcion == 4:
            # Clear the terminal screen
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"{GREEN}I hope you've found this programme helpful{RESET}")
            break

# Show the main menu
def show_menu():
    print(f"""{CYAN}{BOLD}
{"~"*26}
WELLCOME TO LEARN PASSWORD
{"~"*26}
1. Password Diceware
2. Password Analyser
3. Password Comparison
4. Exit{RESET}
""")

# Show the diceware menu
def show_menu_diceware():
    print(f"""{CYAN}{BOLD}
{"~"*22}
[ DICEWARE GENERATOR ]
{"~"*22}
1. Start
2. Return{RESET}
""")

# Show the analyser menu
def show_menu_analyser():
    print(f"""{CYAN}{BOLD}
{"~"*22}
[ ANALYSER GENERATOR ]
{"~"*22}
1. Start
2. Return{RESET}
""")

# Show the comparision menu
def show_menu_comparison():
    print(f"""{CYAN}{BOLD}
{"~"*25}
[ COMPARISION GENERATOR ]
{"~"*25}
1. Start
2. Return{RESET}
""")

# Avoid spelling mistakes menu
def get_int_input(prompt, minimum, maximum):
    while True:
        # Start a test block to catch any errors that might cause the programme to crash
        try:
            get_int = int(input(prompt))
            # Check whether the number entered is less than zero, as it makes no financial sense to deposit or withdraw negative amounts.
            if get_int < 1:
                print(f"""
{CYAN}{BOLD}{"-"*45}{RESET}
{RED}Error: The number cannot be zero o negative{RESET}
{CYAN}{BOLD}{"-"*45}{RESET}
""")
                continue # Instruct the programme to return to the start of the while loop
            elif get_int < minimum or get_int > maximum:
                print(f"""
{CYAN}{BOLD}{"-"*47}{RESET}
{RED}Error: You must enter a number between {minimum} and {maximum}{RESET}
{CYAN}{BOLD}{"-"*47}{RESET}
""")
                continue # Instruct the programme to return to the start of the while loop
            return get_int # If the code reaches this point, it means the number is valid. The function ends
        # If entered text, we'll catch the error here
        except ValueError:
            print(f"""
{CYAN}{BOLD}{"-"*46}{RESET}
{RED}Error 400: Bad Request (Only numbers, please){RESET}
{CYAN}{BOLD}{"-"*46}{RESET}
""")

# Load and convert the text file into a dictionary
def load_dictionary(diceware):
    words_dictionary = {} # It loads the file once and saves it to a new dictionary
    try: # Start a safe block to prevent the programme from crashing if the file does not exist
        with open(diceware, 'r') as file: # Open the file in read mode (“r”) and ensure it closes automatically when finished
            for line in file:
                # We separate the line with a space [code, word]
                parts = line.split() # Break a list of words into separate lines, using the spaces as delimiters
                if len(parts) >= 2: # Check that the line we’ll be using in our file contains at least two elements (the code and the word)
                    code = parts[0] # Store the first element of the list
                    word = parts[1] # Store the second element of the list
                    words_dictionary[code] = word # Adds a new key-value pair to the dictionary, associating the code with its word
    except FileNotFoundError: # Display a warning message to the user instead of crashing
        print(f"{RED}Error: The file 'diceware.txt' doesn't exist...{RESET}")
    # This print is used to check whether the file has been loaded
    # print(f"DEBUG: {len(words_dictionary)} words have been loaded.")
    return words_dictionary

# Finding to words by rolling dice. The reult number is that
def finding_words():
    code = "" # Initialise an empty string variable to store the numbers
    for _ in range(5):
        code += str(random.randint(1,6)) # Generate a five numbers between one and six, and convert to string (and append the variable "code")
    return code # Return code between 11111 and 66666

# Ask is any lowercase in the password posted by the user
def check_password_islower(user_input, show_print=True):
    for check in user_input: # Check every character in the string
        if check.islower(): # If you find one, stop the search and let us know
            if show_print:
                print(f"{CYAN}Lowercase{RESET} {WHITE}found{RESET}{CYAN}...{RESET}")
            return 26
    if show_print:
        print(f"{CYAN}Lowercase{RESET} {WHITE}not found{RESET}{CYAN}...{RESET}") # If you reach the end without having found a single one
    return 0

# Ask is any uppercase in the password posted by the user
def check_password_isupper(user_input, show_print=True):
    for check in user_input: # Check every character in the string
        if check.isupper(): # If you find one, stop the search and let us know
            if show_print:    
                print(f"{CYAN}Uppercase{RESET} {WHITE}found{RESET}{CYAN}...{RESET}")
            return 26
    if show_print:
        print(f"{CYAN}Uppercase{RESET} {WHITE}not found{RESET}{CYAN}...{RESET}") # If you reach the end without having found a single one
    return 0

# Ask is any number in the password posted by the user
def check_password_isdigit(user_input, show_print=True):
    for check in user_input: # Check every number in the string
        if check.isdigit(): # If you find one, stop the search and let us know
            if show_print:
                print(f"{CYAN}Numbers{RESET} {WHITE}found{RESET}{CYAN}...{RESET}")
            return 10
    if show_print:
        print(f"{CYAN}Numbers{RESET} {WHITE}not found{RESET}{CYAN}...{RESET}") # If you reach the end without having found a single one
    return 0

# Ask is any special character in the password posted by the user
def check_password_isalnum(user_input, show_print=True):
    for check in user_input: # Check every special character in the string
        if not check.isalnum(): # If you find one, stop the search and let us know
            if show_print:
                print(f"{CYAN}Special characters{RESET} {WHITE}found{RESET}{CYAN}...{RESET}")
            return 32
    if show_print:
        print(f"{CYAN}Special characters{RESET} {WHITE}not found{RESET}{CYAN}...{RESET}") # If you reach the end without having found a single one
    return 0

# Entropy thermometer to know how weak or strong is a password
def entropy_thermometer(final_bits):
    if final_bits < 40:
        print(f"{CYAN}DOWN [{RESET}{WHITE}###···············{RESET}{CYAN}] HIGH{RESET}") # Extremely weak
    elif final_bits < 60:
        print(f"{CYAN}DOWN [{RESET}{WHITE}######············{RESET}{CYAN}] HIGH{RESET}") # Weak
    elif final_bits < 80:
        print(f"{CYAN}DOWN [{RESET}{WHITE}#########·········{RESET}{CYAN}] HIGH{RESET}") # Moderate
    elif final_bits < 100:
        print(f"{CYAN}DOWN [{RESET}{WHITE}############······{RESET}{CYAN}] HIGH{RESET}") # Strong
    elif final_bits < 120:
        print(f"{CYAN}DOWN [{RESET}{WHITE}###############···{RESET}{CYAN}] HIGH{RESET}") # Very strong
    else:
        print(f"{CYAN}DOWN [{RESET}{WHITE}##################{RESET}{CYAN}] HIGH{RESET}") # Extremely strong

# Calculate the estimated time, in seconds, required to exhaust the search space for a key of “bits” in length, comparing a home PC, a supercomputer and a server farm (hacker farm).
def time_calculations_diferents_PC(bits):
    total_combinations = 2 ** bits # Calculate the total number of combinations
    domestic_pc = 100_000_000 # 100 millions/second
    super_computer = 1_000_000_000_000 # 1 bilion/second
    hacker_farm = 500_000_000_000_000 # 500 bilions/second

    # Different calculations are performed depending on the computing capabilities specified
    calculations_domestic_pc = total_combinations / domestic_pc
    calculations_supercomputer = total_combinations / super_computer
    calculations_hacker_farm = total_combinations / hacker_farm

    # Return the results
    return calculations_domestic_pc, calculations_supercomputer, calculations_hacker_farm

# A list of units of measurement, ordered from largest to smallest, to determine the most appropriate time scale
def temporary_adjustment(diferents_times):
    # Small scale
    one_picosecond = 1e-12 # Move the decimal point twelve places to the left
    one_nanosecond = 1e-9 # Move the decimal point nine places to the left
    one_microsecond = 1e-6 # 1e-6 == 0.000001s
    one_milisecond = 1e-3 # 1e-3 == 0.001s

    # Standard scale
    one_second = 1
    one_minute = 60
    one_hour = 3_600
    one_day = 86_400
    one_week = 604_800      # 7 days
    one_month = 2_592_000   # 30 days
    one_year = 31_536_000   # 365 days

    # Large scale
    one_decade = 315_360_000
    one_century = 3_153_600_000
    one_millennium = 31_536_000_000
    one_aeon = 31_536_000_000_000_000 # one bilion years
    
    # Each range with its corresponding conversion. It is better to use a tuple than an "if" statement and lots of "elif" clauses
    # The list must be sorted from largest to smallest
    list_diferent_times = [
        ("aeon", one_aeon, "aeons"),
        ("millennium", one_millennium, "millenniums"),
        ("century", one_century, "centuries"),
        ("decade", one_decade, "decades"),
        ("year", one_year, "years"),
        ("month", one_month, "months"),
        ("week", one_week, "weeks"),
        ("day", one_day, "days"),
        ("hour", one_hour, "hours"),
        ("minute", one_minute, "minutes"),
        ("second", one_second, "seconds"),
        ("millisecond", one_milisecond, "milliseconds"),
        ("microsecond", one_microsecond, "microseconds"),
        ("nanosecond", one_nanosecond, "nanoseconds"),
        ("picosecond", one_picosecond, "picoseconds")
    ]
    # Use a for to iterate through the tuple until we find the specified value
    for singular_name, choose_time, plural_name in list_diferent_times:
        if diferents_times >= choose_time:
            total = diferents_times / choose_time
            # Choose a singular o plural name and return with the time selected
            if total == 1:
                return total, singular_name
            else:
                return total, plural_name

    return diferents_times, "seconds"

# It compares two different passwords chosen by the user (the user’s own password and a diceware password) and determines various parameters
def check_password_comparison(dictionary, comparison_user, comparison_diceware):
    print(f"""\n{CYAN}
{"~"*40}
          COMPARISON RESULTS
{"~"*40}{RESET}
""")
    time.sleep(1)
    
    # Specify whether the user password contains uppercase letters, lowercase letters, numbers and special character for the bit calculations
    rang_bits = 0
    rang_bits += check_password_islower(comparison_user, False) # It's False to hide the print inside the function
    rang_bits += check_password_isupper(comparison_user, False)
    rang_bits += check_password_isdigit(comparison_user, False)
    rang_bits += check_password_isalnum(comparison_user, False)

    # If the user enters something very unusual and it returns 0, we assign a minimum value of 1 to avoid an error in log2
    if rang_bits == 0:
        rang_bits = 1

    # We create an empty list to store the selected words
    password_list = []
    for i in range(comparison_diceware):
        code = finding_words() # Return number between 11111 and 66666
        word = dictionary.get(code, "") # We are looking for a code in our list
        password_list.append(word) # We add the result to the list created before the loop

    # Mathematical calculations for entropy
    password_text = '-'.join(password_list) # We store the final text of the password in a variable so that we can count the characters using len()
    diceware_length = len(password_text)
    user_length = len(comparison_user)

    bits_user = user_length * math.log2(rang_bits) # Shannon's mathematical formula for entropy: E = L * log2(R)
    bits_diceware = comparison_diceware * math.log2(7776) # Shannon's mathematical formula (adapted by Arnold Reinhold) for entropy: E = N * log2(7776)

    # Show the passwords selected
    print(f"{CYAN}{UNDER}PASSWORDS SELECTED{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}-- User password --:{RESET} {WHITE}{comparison_user}{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}~~ Diceware password ~~:{RESET} {WHITE}{'-'.join(password_list)}{RESET}")
    time.sleep(1)

    # Show the length of two different passwords
    print(f"\n{CYAN}{UNDER}LENGTH OF THE PASSWORDS{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}-- User password -- contains{RESET} {WHITE}{user_length}{RESET} {CYAN}characters{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}~~ Diceware password ~~ contains{RESET} {WHITE}{diceware_length}{RESET} {CYAN}characters{RESET}") 
    time.sleep(1)

    # Strength of your current password
    print(f"\n{CYAN}{UNDER}STRENGTH OF YOUR CURRENT PASSWORD{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}-- User password --{RESET}")
    time.sleep(0.4)
    entropy_thermometer(bits_user)
    time.sleep(0.4)
    print(f"{CYAN}~~ Diceware password ~~{RESET}")
    time.sleep(0.4)
    entropy_thermometer(bits_diceware)
    time.sleep(1)

    # Calculate the difference
    diff = bits_diceware - bits_user
    print(f"\n{CYAN}{UNDER}ENTROPY CALCULATOR{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}Your current password:{RESET}   {WHITE}{bits_user:.2f}{RESET} {CYAN}bits of entropy{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}Diceware suggestion:{RESET}     {WHITE}{bits_diceware:.2f}{RESET} {CYAN}bits of entropy{RESET}\n")
    time.sleep(1)
    
    # Print suggestion based on the result
    print(f"{CYAN}{UNDER}SUGGESTION{RESET}")
    time.sleep(0.4)
    if bits_user < 80 and comparison_diceware < 5: # Both passwords are really weak
        print(f"{RED}Warning! Both passwords are very weak{RESET}")
        time.sleep(0.4)
        print(f"{YELLOW}Recommendation: increase your password to at least 80 bits{RESET}")
        time.sleep(0.4)
        print(f"{YELLOW}Recommendation: generate a diceware password with five words or more{RESET}")
        time.sleep(1)
    elif bits_user < 80: # Only the user password is weak
        print(f"{RED}Warning! The user password is very weak{RESET}")
        time.sleep(0.4)
        print(f"{YELLOW}Recommendation: increase your password to at least 80 bits{RESET}")
        time.sleep(1)
    elif comparison_diceware < 5: # Only the diceware password is weak
        print(f"{RED}Warning! The diceware password is very weak{RESET}")
        time.sleep(0.4)
        print(f"{YELLOW}Recommendation: generate a diceware password with five words or more{RESET}")
        time.sleep(1)
    else: # Both passwords are at the minimum
        if diff > 0: # The diceware password is stronger than the user password
            print(f"{CYAN}Your current password meets the security standard{RESET}")
            time.sleep(0.4)
            print(f"{CYAN}However, diceware is still{RESET} {WHITE}{abs(diff):.2f}{RESET} {CYAN}bits stronger{RESET}")
            time.sleep(0.4)
            print(f"{YELLOW}Recommendation: use the diceware password for greater security{RESET}")
            time.sleep(1)
        elif diff < 0: # # The user password is stronger than the diceware password
            print(f"{GREEN}Your current password is secure{RESET}")
            time.sleep(0.4)
            print(f"{CYAN}It is{RESET} {WHITE}{abs(diff):.2f}{RESET} {CYAN}bits stronger than the diceware suggestion{RESET}")
            time.sleep(1)
        else: # An unlikely scenario, but one that is mathematically possible: a tie that is identical bit for bit
            print(f"{GREEN}Both passwords are safe and have the exact same strength{RESET}")
            time.sleep(1)

    # Recommendation to create an unbreakable password
    print(f"""{CYAN}
{"~"*40}
      WHAT I RECOMMEND TO YOU
{"~"*40}{RESET}
""")
    time.sleep(1)

    # Combination of diceware password
    additions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "&", "*"] 
    
    # We go through the list of words to find the exact position of the words created
    for i in range (len(password_list)):
        # add one additions every other word, anywhere (though never together)
        if (i + 1) % 2 == 0 or len(password_list) == 1:
            chosen_additions = random.choice(additions) # Choose an intruder character from the above list completely at random
            if len(password_list) == 1: # Protecting the code against future changes
                word_addition_to_modify = 0 # Avoid unnecessary calculations and safeguard the logic
            else: # If there is only one word, we modify to 0 so that we can change it
                word_addition_to_modify = random.randint(0, len(password_list) - 1) # Choose a random word from the list to decide which word will be changed
            word_to_modify = password_list[word_addition_to_modify] # Extract the selected word from the list and store it in a temporary variable
            character_position = random.randint(1, len(word_to_modify) - 1) if len(word_to_modify) > 2 else 1 # Choose a random position WITHIN the letters of that word (avoiding the start or end)
            modified_word = word_to_modify[:character_position] + chosen_additions + word_to_modify[character_position:] # Split the word into two parts and insert the addition character right in the middle
            password_list[word_addition_to_modify] = modified_word # Replace the original word in the list with the new modified word containing the addition

    # Displays the generate passwords
    print(f"{CYAN}-- User password --:{RESET} {WHITE}{comparison_user}{RESET}")
    time.sleep(0.4)
    print(f"{CYAN}~~ Diceware password ~~:{RESET} {WHITE}{password_text}{RESET}")
    time.sleep(0.4)
    print(f"\n{CYAN}Something like this: inserting something different between words and randomly \nadding “additions” so that they can't use a dictionary to crack your password{RESET}\n")
    time.sleep(1)
    
    # Displays the generated Diceware phrase on the screen so that the user can see diferent examples of the mix
    final_suggestion = random.randint(0, 100)
    if final_suggestion < 26:
        print(f"{GREEN}** Suggested phrase **:{RESET} {WHITE}{'*-*'.join(password_list)}{RESET}")
    elif final_suggestion < 51:
        print(f"{GREEN}** Suggested phrase **:{RESET} {WHITE}{'*/'.join(password_list)}{RESET}")
    elif final_suggestion < 76:
        print(f"{GREEN}** Suggested phrase **:{RESET} {WHITE}{'~'.join(password_list)}{RESET}")
    else:
        print(f"{GREEN}** Suggested phrase **:{RESET} {WHITE}{']['.join(password_list)}{RESET}")

    return bits_user # Required to display the corresponding metaphor that follows this function

# A series of metaphors to help understand the scalability of bits in passwords
def metaphors_about_analyser(bits_metaphor):
    print(f"{CYAN}Analyser visual metaphor:{RESET}")
    time.sleep(0.4)
    if bits_metaphor < 40:
        print(f"{MAGENTA}Your password is like leaving your front door wide open with a huge neon sign\nsaying 'come in and have a look' to anyone passing by{RESET}")
    elif bits_metaphor < 60:
        print(f"{MAGENTA}Your password is like locking your door, but leaving the key underneath the doormat.\nIt gives you a false sense of security, but any amateur thief knows exactly where to look{RESET}")
    elif bits_metaphor < 80:
        print(f"{MAGENTA}Your password is like a standard wooden door with a basic lock. It stops a random\npasserby from pushing it open, but a burglar with a simple crowbar could easly get in{RESET}")
    elif bits_metaphor < 100:
        print(f"{MAGENTA}Your password is like a solid armored door with multiple bolts. A thief can't just\nkick it down; they would need specialized heavy tools, noise, and plenty of time{RESET}")
    elif bits_metaphor < 120:
        print(f"{MAGENTA}Your password is like transforming your house into a high-security bank vault.\nTo get in, the hacker needs a whole Hollywood-style team, lasers, and a miracle{RESET}")
    else:
        print(f"{MAGENTA}Your password is like moving your house to a secret bunker on Mars, surrounded by aliens.\nIt is so mathematically secure not even all the computers on Earth combined could crack it{RESET}")

# A series of metaphors to help understand the scalability of adding more words to passphrases
def metaphors_about_diceware(num_words_diceware):
    print(f"\n{CYAN}Diceware visual metaphor:{RESET}")
    time.sleep(0.4)
    if num_words_diceware == 1:
        print(f"{MAGENTA}With 1 word, the hacker is standing right next to you on the bus, looking\ndirectly at your phone screen over your shoulder{RESET}")
    elif num_words_diceware == 2:
        print(f"{MAGENTA}With 2 words, you've pushed the hacker away. Now, to see your password,\nthey need to stand 3 meters away with binoculars{RESET}")
    elif num_words_diceware == 3:
        print(f"{MAGENTA}With 3 words, you've built a brick wall between you and the hacker. Now,\nthey don't just need binoculars; they have to bring a ladder to look over it{RESET}")
    elif num_words_diceware == 4:
        print(f"{MAGENTA}With 4 words, the wall becomes a castle moat filled with hungry crocodiles.\nThe hacker now has to figure out how to swim across without getting eaten{RESET}")
    elif num_words_diceware == 5:
        print(f"{MAGENTA}With 5 words, that's when things start to get seriously complicated for them.\nYour castle now flies in the sky! The hacker is stuck on the ground, staring\nthrough a telescope while crocodiles guard an empty moat. You are safe{RESET}")
    elif num_words_diceware == 6:
        print(f"{MAGENTA}With 6 words, you've wrapped your flying castle in an invisible shield and\nteleported it to another dimension. The hacker's telescope doesn't know where to look{RESET}")
    elif num_words_diceware == 7:
        print(f"{MAGENTA}With 7 words, even if the hacker turns into a sci-fi supercomputer god,\nyour password is hidden in a black hole{RESET}")
    elif num_words_diceware == 8:
        print(f"{MAGENTA}With 8 words, you have created a completely separate parallel universe just to\nstore this single phrase. The hacker is left trying to hack reality itself{RESET}")
    elif num_words_diceware == 9:
        print(f"{MAGENTA}With 9 words, your password will outlive the lifespan of our universe{RESET}")
    else:
        print(f"{MAGENTA}With 10 words, you have reached the absolute peak of cybersecurity overkill.\nTrying to crack this is like trying to guess the exact position of every atom in the\nuniverse on your first try: mathematically impossible{RESET}")

# This line tells Python: ‘If this file is run, start with the main function’.
if __name__ == "__main__":
    main()