
-- ############################## --
	-- INSERT SAMPLE RECORDS --
-- ############################## --


-- EMPLOYEES
INSERT INTO employee VALUES (2001, "JENNY JIAN JIE", 0);
INSERT INTO employee VALUES (2002, "RAVEEN PRABHU", 0);
INSERT INTO employee VALUES (2003, "TAN KIAN LIN", 1);
INSERT INTO employee VALUES (2004, "JASON LIM", 0);
INSERT INTO employee VALUES (2005, "KELLY WONG", 0);
INSERT INTO employee VALUES (2006, "CYNTHIA SIM", 0);
INSERT INTO employee VALUES (2007, "MICHELLE KONG", 1);
INSERT INTO employee VALUES (2008, "AJAY WILSON", 0);
INSERT INTO employee VALUES (2009, "BENJAMIN LOW", 0);
INSERT INTO employee VALUES (2010, "CASS FONG", 0);


-- AUDIT_RECORDS
-- (audit_no, col_changed, change_id, prev_audit_no)
INSERT INTO audit_records VALUES ("A1000100001-1", "NEW", "C1000100001-1", NULL);
INSERT INTO audit_records VALUES ("A1000100002-1", "NEW", "C1000100002-1", NULL);
INSERT INTO audit_records VALUES ("A1000100003-1", "NEW", "C1000100003-1", NULL);
INSERT INTO audit_records VALUES ("A1000100004-1", "NEW", "C1000100004-1", NULL);
INSERT INTO audit_records VALUES ("A1000100005-1", "NEW", "C1000100005-1", NULL);


-- CLIENT_CONFIG
-- (client_no, com_tolerance, gorss_amt_tolerance, initial_submitter, initial_approver, latest_audit_id)
INSERT INTO client_config VALUES (1000100001, 50, 100, 2001, 2004, "A1000100001-1");
INSERT INTO client_config VALUES (1000100002, 60, 75.45, 2002, 2005, "A1000100002-1");
INSERT INTO client_config VALUES (1000100003, 44.50, 56.2, 2006, 2002, "A1000100003-1");
INSERT INTO client_config VALUES (1000100004, 34.60, 100.3, 2007, 2009, "A1000100004-1");
INSERT INTO client_config VALUES (1000100005, 22.1, 62, 2005, 2008, "A1000100005-1");


-- CHANGE_REQUEST
-- (change_id, client_no, new_com_tolerance, new_gross_amt_tolerance, change_submitter, change_approver, is_approved, 
-- is_com_tol_changed, is_gross_tol_changed, time_submitted, time_approved)
INSERT INTO change_request VALUES ("C1000100001-1", 1000100001, 50, 100, 2001, 2004, 1, 1, 1, '2023-05-09 01:15:00', '2023-05-09 16:23:22');
INSERT INTO change_request VALUES ("C1000100002-1", 1000100002, 60, 75.45, 2002, 2005, 1, 1, 1, '2023-05-09 01:16:23', '2023-05-09 16:25:45');
INSERT INTO change_request VALUES ("C1000100003-1", 1000100003, 44.50, 56.2, 2006, 2002, 1, 1, 1, '2023-05-09 01:17:46', '2023-05-09 16:28:24');
INSERT INTO change_request VALUES ("C1000100004-1", 1000100004, 34.60, 100.3, 2007, 2009, 1, 1, 1, '2023-05-09 01:20:07', '2023-05-09 16:33:56');
INSERT INTO change_request VALUES ("C1000100005-1", 1000100005, 22.1, 62, 2005, 2008, 1, 1, 1, '2023-05-09 01:22:14', '2023-05-09 16:44:22');




