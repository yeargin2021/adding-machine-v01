import csv


# Append user input to 'tape.txt' file
def write_to_file(file_name):
    with open(file_name, 'a') as w:
        while True:
            amount = input('Enter an amount: ')
            if amount.lower() == 'stop':
                break
            w.write(amount + ',')


# Read from 'tape.txt' file and calculate the sum
def read_and_sum_from_file(file_name):
    total = 0
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for value in row:
                try:
                    total += int(value)
                except ValueError:
                    print(f"Skipping invalid entry: '{value}'")
    return total


# Main function execution
if __name__ == "__main__":
    file_name = 'tape.txt'
    write_to_file(file_name)
    total = read_and_sum_from_file(file_name)
    print(f"Total Sum: ${total}")