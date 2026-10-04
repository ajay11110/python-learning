# match-case works like switch-case
# It checks a value against different cases.

command = input("Enter command: ")

match command:

    case "start":
        print("Car started")

    case "stop":
        print("Car stopped")

    case "pause":
        print("Car paused")

    # Default case
    # Runs if no case matches
    case _:
        print("Unknown command")