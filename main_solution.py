import cash_on_hand

def some_function():
    # Replace this with your desired function or code that produces some output
    return "Hello, World!"

def main():
    # Redirecting the standard output to a text file
    with open('output.txt', 'w') as f:
        sys.stdout = f  # Redirect standard output to the file

        # Call your function or code here that produces the output
        result = some_function()

        # Printing the output to the file
        print(result)

        # Resetting the standard output to its default value (terminal)
        sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()