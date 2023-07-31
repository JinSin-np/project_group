import sys

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


# Manually type in the calculated output amount as a temporarily value for the variable "Answer_output" 
Answer_output = [["EMP01", "7508.08","153","22","131","210.81","2044.81"],["EMP02","5876.89","138","17","121","70.15","1764.15"],["EMP03","9604.83","156","22","134","432.58","2308.58"]] 

# name the text file as "paymentSummary.txt"
with open("paymentSummary.txt", "w") as file: 
    # adding title into the text file, using "\n" to move a new line to the next row 
#     file.write("FashionStore Payment Summary\n============================\nEmployee ID, Total Sales, Total Hours, Break Hours, Total Hours Clocked, Commission, Total Pay\n") 
    header = "FashionStore Payment Summary\n============================\nEmployee ID, Total Sales, Total Hours, Break Hours, Total Hours Clocked, Commission, Total Pay\n"
    file.write(header)

    # assigning the Answer_output values via factors 0 to 6, using "\n" to move a new line to the next row 
    for factor in Answer_output:
        file.write(f"{factor[0]},{factor[1]},{factor[2]},{factor[3]},{factor[4]},{factor[5]},{factor[6]}\n") 
