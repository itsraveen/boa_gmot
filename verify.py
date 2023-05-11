import sqlite3


def read_parameters_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing white spaces
                if line:  # Skip empty lines
                    parameters = line.split()  # Split line into three parameters
                    if len(parameters) == 3:
                        (
                            client,
                            commission_difference,
                            gross_amount_difference,
                        ) = parameters
                        print(
                            f"\nClient: {client}, Commission Differnce: {commission_difference}, Gross Amount Differnce: {gross_amount_difference}"
                        )
                        # verify_trade_details(param1, param2, param3)
                        # do some DB pulling here
                        # Connect to the database
                        conn = sqlite3.connect("database.db")

                        # Create a cursor object
                        cursor = conn.cursor()

                        # Select the first three rows from the table
                        select_query = """
                        SELECT com_tolerance, gross_amt_tolerance
                        FROM client_config
                        WHERE client_no=?
                        """

                        cursor.execute(select_query, (client,))
                        result = cursor.fetchall()

                        print(result)
                        config_commission_tolerance = result[0][0]
                        config_gross_amount_tolerance = result[0][1]

                        if abs(int(commission_difference)) > int(
                            config_commission_tolerance
                        ):
                            print(
                                f"❌ FAIL: The commision differnce of {commission_difference} is greater than {config_commission_tolerance} for {client}"
                            )
                        if abs(int(gross_amount_difference)) > int(
                            config_gross_amount_tolerance
                        ):
                            print(
                                f"❌ FAIL: The gross amount differnce of {gross_amount_difference} is greater than {config_gross_amount_tolerance} for {client}"
                            )
                        # if client config is missing: print(f"FAIL: Client {clinet} is missing configuration")
                        else:
                            print("✅ Success")

                    else:
                        print(f"Invalid line format: {line}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def verify_trade_details(client, commission_difference, gross_amount_difference):

    # do some DB pulling here
    # Connect to the database
    conn = sqlite3.connect("database.db")

    # Create a cursor object
    cursor = conn.cursor()

    # Select the first three rows from the table
    select_query = """
    SELECT com_tolerance, gross_amt_tolerance
    FROM client_config
    WHERE client_no=?
    """

    cursor.execute(select_query, (client,))
    result = cursor.fetchall()
    print(result)

    config_commission_tolerance = 0
    config_gross_amount_tolerance = 0
    if abs(commission_difference) > config_commission_tolerance:
        print(
            f"❌ FAIL: The commision differnce of {commission_difference} is greater than {config_commission_tolerance} for {client}"
        )
    if abs(gross_amount_difference) > config_gross_amount_tolerance:
        print(
            f"❌ FAIL: The commision differnce of {gross_amount_difference} is greater than {config_gross_amount_tolerance} for {client}"
        )
    # if client config is missing: print(f"FAIL: Client {clinet} is missing configuration")
    else:
        print("✅ Success")


# Usage example
filename = "trade_details.txt"  # Replace with the actual filename
read_parameters_from_file(filename)
