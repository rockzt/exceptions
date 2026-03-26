import sys
from custom_exceptions.exceptions import WrongOsError

def window_interaction():
    pass

def linux_interaction():
    if not sys.platform.startswith('linux'):
        raise WrongOsError(
            (
                'Linux Only,'
                f"Your Sytem: {sys.platform}"
            )
        )
    print("Linux Interaction.....")

def macos_interaction():
    if not sys.platform.startswith('darwin'):
        raise WrongOsError(
            (
                'Darwin Only,'
                f"Your System: {sys.platform}"
            )
        )
    print("Darwin Interaction.....")


try:
    linux_interaction()
    #macos_interaction()
except WrongOsError as error:
    print(f"Something went wrong :( - Error {error}")
else:
    print("No problem, work done.")
    print("Read logging file ...")
    try:
        with open("file.log") as log_file:
            print(log_file.read())
    # Using built-in exception
    except FileNotFoundError as fnf_error:
        print(f"Something went wrong :( - Error {fnf_error}")
finally:
    print("Cleaning up despite any exceptions ...")

print("Happens after")