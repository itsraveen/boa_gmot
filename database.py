import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create a cursor object
cursor = conn.cursor()

##########################
##### TABLE CREATION #####
##########################

# Create the employee table
create_table_employee = """
CREATE TABLE IF NOT EXISTS employee (
    employee_id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    is_superuser INT NOT NULL
    );
"""
cursor.execute(create_table_employee)

# Create the audit_record table
create_table_audit_record = """
CREATE TABLE IF NOT EXISTS audit_records (
    audit_no TEXT PRIMARY KEY NOT NULL,
    col_changed TEXT NOT NULL,
    prev_audit_no TEXT DEFAULT NULL,
    FOREIGN KEY (prev_audit_no) REFERENCES audit_records (audit_no)
);
"""

cursor.execute(create_table_audit_record)


# Create the client_config table
create_table_client_config = """
CREATE TABLE IF NOT EXISTS client_config (
    client_no TEXT PRIMARY KEY NOT NULL,
    initial_submitter TEXT NOT NULL,
    initial_approver TEXT NOT NULL,
    latest_audit_id TEXT NOT NULL,
    FOREIGN KEY (initial_approver) REFERENCES employee (employee_id),
    FOREIGN KEY (latest_audit_id) REFERENCES audit_records (audit_no),
    FOREIGN KEY (initial_submitter) REFERENCES employee (employee_id)
);
"""
cursor.execute(create_table_client_config)


# Create the client_com_tol table
create_table_client_com_tol = """
CREATE TABLE IF NOT EXISTS client_com_tol (
    client_no TEXT PRIMARY KEY NOT NULL,
    com_tolerance FLOAT NOT NULL,
    FOREIGN KEY (client_no) REFERENCES client_config (client_no)
);
"""

cursor.execute(create_table_client_com_tol)


# Create the client_gross_amt_tol table
create_table_client_gross_amt_tol = """
CREATE TABLE IF NOT EXISTS client_gross_amt_tol (
    client_no TEXT PRIMARY KEY NOT NULL,
    gross_amt_tolerance FLOAT NOT NULL,
    FOREIGN KEY (client_no) REFERENCES client_config (client_no)
);
"""

cursor.execute(create_table_client_gross_amt_tol)


# Create the change_request table
create_table_change_request = """
CREATE TABLE IF NOT EXISTS change_request  (
    change_id TEXT PRIMARY KEY NOT NULL,
    client_no TEXT NOT NULL,
    new_commission_tolerance FLOAT NOT NULL,
    new_gross_amt_tolerance FLOAT NOT NULL,
    change_submitter TEXT NOT NULL,
    change_approver TEXT NOT NULL,
    is_approved TEXT,
    is_com_tol_changed INT NOT NULL,
    is_gross_tol_changed INT NOT NULL,
    time_submitted DATETIME NOT NULL,
    time_approved DATETIME DEFAULT NULL,
    FOREIGN KEY (change_approver) REFERENCES employee (employee_id),
    FOREIGN KEY (change_submitter) REFERENCES employee (employee_id)
);
"""
cursor.execute(create_table_change_request)


# Add in Foreign Key Constraints
add_foreign = """
ALTER TABLE audit_records ADD COLUMN change_id TEXT REFERENCES change_request (change_id);
"""
cursor.execute(add_foreign)


#################################
##### INSERT SAMPLE RECORDS #####
#################################

# INSERT sample records
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
(1000100001, 2001, 2004, "A1000100001-1"),
(1000100002, 2002, 2005, "A1000100002-1"),
(1000100003, 2006, 2002, "A1000100003-1"),
(1000100004, 2007, 2009, "A1000100004-1"),
(1000100005, 2005, 2008, "A1000100005-1");
"""

cursor.execute(insert_query_client_config)

insert_query_client_com_tol = """
INSERT INTO client_com_tol VALUES 
(1000100001, 50),
(1000100002, 60),
(1000100003, 44.50),
(1000100004, 34.60),
(1000100005, 22.1)
"""

cursor.execute(insert_query_client_com_tol)

insert_query_client_gross_amt_tol = """
INSERT INTO client_gross_amt_tol VALUES 
(1000100001, 100),
(1000100002, 75.45), 
(1000100003, 56.2),
(1000100004, 100.3),
(1000100005, 62)
"""

cursor.execute(insert_query_client_gross_amt_tol)

insert_query_change_request = """
INSERT INTO change_request VALUES 
("C1000100001-1", 1000100001, 50, 100, 2001, 2004, "Y", 1, 1, '2023-05-09 01:15:00', '2023-05-09 16:23:22'),
("C1000100002-1", 1000100002, 60, 75.45, 2002, 2005, "Y", 1, 1, '2023-05-09 01:16:23', '2023-05-09 16:25:45'),
("C1000100003-1", 1000100003, 44.50, 56.2, 2006, 2002, "Y", 1, 1, '2023-05-09 01:17:46', '2023-05-09 16:28:24'),
("C1000100004-1", 1000100004, 34.60, 100.3, 2007, 2009, "Y", 1, 1, '2023-05-09 01:20:07', '2023-05-09 16:33:56'),
("C1000100005-1", 1000100005, 22.1, 62, 2005, 2008, "Y", 1, 1, '2023-05-09 01:22:14', '2023-05-09 16:44:22');
"""

cursor.execute(insert_query_change_request)

# Commit the changes
conn.commit()
