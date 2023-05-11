def read_parameters_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing white spaces
                if line:  # Skip empty lines
                    parameters = line.split()  # Split line into three parameters
                    if len(parameters) == 3:
                        param1, param2, param3 = parameters
                        print(
                            f"Parameter 1: {param1}, Parameter 2: {param2}, Parameter 3: {param3}"
                        )
                    else:
                        print(f"Invalid line format: {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


# Usage example
filename = "trade_details.txt"  # Replace with the actual filename
read_parameters_from_file(filename)
