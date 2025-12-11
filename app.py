from utils import add_numbers, greet_user

def main():
    print("Running Application...")
    result = add_numbers(10, 20)
    print(f"Addition Result: {result}")

    message = greet_user("Suraj")
    print(message)

if __name__ == "__main__":
    main()
