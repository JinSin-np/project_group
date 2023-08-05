import cash_on_hand
import overheads
import profit_and_loss

def read_file(cash_on_hand):
    with open(cash_on_hand, 'r') as file:
        content = file.read()
        return content

def write_output(output, output_cash_on_hand):
    with open(output_cash_on_hand, 'a') as file:
        file.write(output)

if __name__ == "__main__":
    input_filenames = ["input1.txt", "input2.txt"]
    output_filename = "output.txt"

    # Initialize an empty string to store the concatenated output
    concatenated_output = ""

    # Read data from input files and concatenate them
    for filename in input_filenames:
        input_data = read_file(filename)
        concatenated_output += input_data

    # Write the concatenated output to a text file
    write_output(concatenated_output, output_filename)
