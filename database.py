import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor object
cursor = conn.cursor()

# # Create the clients table
# create_table_query = """
# CREATE TABLE IF NOT EXISTS clients (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     client_name TEXT,
#     commission INTEGER,
#     gross_amount INTEGER
# )
# """
# cursor.execute(create_table_query)

# Create the employee table
create_table_employee = """
CREATE TABLE IF NOT EXISTS employee (
    employee_id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    is_superuser INT NOT NULL
    );
"""
cursor.execute(create_table_employee)


create_table_audit_record = """
CREATE TABLE IF NOT EXISTS audit_records (
    audit_no TEXT PRIMARY KEY NOT NULL,
    col_changed TEXT NOT NULL,
    prev_audit_no TEXT DEFAULT NULL,
    FOREIGN KEY (prev_audit_no) REFERENCES audit_records (audit_no)
);
"""

cursor.execute(create_table_audit_record)

create_table_client_config = """
CREATE TABLE IF NOT EXISTS client_config (
    client_no TEXT PRIMARY KEY NOT NULL,
    com_tolerance FLOAT NOT NULL,
    gross_amt_tolerance FLOAT NOT NULL,
    initial_submitter TEXT NOT NULL,
    initial_approver TEXT NOT NULL,
    latest_audit_id TEXT NOT NULL,
    FOREIGN KEY (initial_approver) REFERENCES employee (employee_id),
    FOREIGN KEY (latest_audit_id) REFERENCES audit_records (audit_no),
    FOREIGN KEY (initial_submitter) REFERENCES employee (employee_id)
);
"""
cursor.execute(create_table_client_config)

create_table_change_request = """
CREATE TABLE IF NOT EXISTS change_request  (
    change_id TEXT PRIMARY KEY NOT NULL,
    client_no TEXT NOT NULL,
    new_commission_tolerance FLOAT NOT NULL,
    new_gross_amt_tolerance FLOAT NOT NULL,
    change_submitter TEXT NOT NULL,
    change_approver TEXT NOT NULL,
    is_approved INT NOT NULL,
    is_com_tol_changed INT NOT NULL,
    is_gross_tol_changed INT NOT NULL,
    time_submitted DATETIME NOT NULL,
    time_approved DATETIME DEFAULT NULL,
    FOREIGN KEY (change_approver) REFERENCES employee (employee_id),
    FOREIGN KEY (change_submitter) REFERENCES employee (employee_id)
);
"""
cursor.execute(create_table_change_request)

add_foreign = """
ALTER TABLE audit_records ADD COLUMN change_id TEXT REFERENCES change_request (change_id);
"""
cursor.execute(add_foreign)

# -- CONSTRAINT `FK_change_id` FOREIGN KEY (`change_id`) REFERENCES `change_request` (`change_id`)

# conn.commit()

insert_query_employee = """ 
INSERT INTO employee VALUES 
(2001, "JENNY JIAN JIE", 0),
(2002, "RAVEEN PRABHU", 0),
(2003, "TAN KIAN LIN", 1),
(2004, "JASON LIM", 0),
(2005, "KELLY WONG", 0),
(2006, "CYNTHIA SIM", 0),
(2007, "MICHELLE KONG", 1),
(2008, "AJAY WILSON", 0),
(2009, "BENJAMIN LOW", 0),
(2010, "CASS FONG", 0);
"""

cursor.execute(insert_query_employee)

insert_query_audit = """
INSERT INTO audit_records VALUES 
("A1000100001-1", "NEW", NULL, "C1000100001-1"),
("A1000100002-1", "NEW", NULL, "C1000100002-1"),
("A1000100003-1", "NEW", NULL, "C1000100003-1"),
("A1000100004-1", "NEW", NULL, "C1000100004-1"),
("A1000100005-1", "NEW", NULL, "C1000100005-1");
"""

cursor.execute(insert_query_audit)

insert_query_client_config = """
INSERT INTO client_config VALUES 
(1000100001, 50, 100, 2001, 2004, "A1000100001-1"),
(1000100002, 60, 75.45, 2002, 2005, "A1000100002-1"),
(1000100003, 44.50, 56.2, 2006, 2002, "A1000100003-1"),
(1000100004, 34.60, 100.3, 2007, 2009, "A1000100004-1"),
(1000100005, 22.1, 62, 2005, 2008, "A1000100005-1");
"""

cursor.execute(insert_query_client_config)

insert_query_change_request = """
INSERT INTO change_request VALUES 
("C1000100001-1", 1000100001, 50, 100, 2001, 2004, 1, 1, 1, '2023-05-09 01:15:00', '2023-05-09 16:23:22'),
("C1000100002-1", 1000100002, 60, 75.45, 2002, 2005, 1, 1, 1, '2023-05-09 01:16:23', '2023-05-09 16:25:45'),
("C1000100003-1", 1000100003, 44.50, 56.2, 2006, 2002, 1, 1, 1, '2023-05-09 01:17:46', '2023-05-09 16:28:24'),
("C1000100004-1", 1000100004, 34.60, 100.3, 2007, 2009, 1, 1, 1, '2023-05-09 01:20:07', '2023-05-09 16:33:56'),
("C1000100005-1", 1000100005, 22.1, 62, 2005, 2008, 1, 1, 1, '2023-05-09 01:22:14', '2023-05-09 16:44:22');
"""

cursor.execute(insert_query_change_request)

# Commit the changes
conn.commit()

# # Select the first three rows from the table
# select_query = """
# SELECT * FROM client_config LIMIT 8
# """
# cursor.execute(select_query)
# result = cursor.fetchall()
# for row in result:
#     print(row)

# # Close the connection
# conn.close()
