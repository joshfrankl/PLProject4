s_emp = (('ID', 'LAST_NAME', 'FIRST_NAME', 'USERID', 'START_DATE', 'COMMENTS', 'TITLE', 'SALARY', 'COMMISSION', 'DEPT_ID', 'MANAGER_ID'),
         (1, 'Martin', 'Carmen', 'martincu', '1990-03-03 00:00:00', '', 'President', 4500.0, '', 50, ''),
         (10, 'Jackson', 'Marta', 'jacksomt', '1991-02-27 00:00:00', '', 'Warehouse Manager', 1507.0, '', 45, 2),
         (11, 'Henderson', 'Colin', 'hendercs', '1990-05-14 00:00:00', '', 'Sales Representative', 1400.0, 10, 31, 3),
         (12, 'Gilson', 'Sam', 'gilsonsj', '1992-01-18 00:00:00', '', 'Sales Representative', 1490.0, 12.5, 32, 3),
         (13, 'Sanders', 'Jason', 'sanderjk', '1991-02-18 00:00:00', '', 'Sales Representative', 1515.0, 10, 33, 3),
         (14, 'Dameron', 'Andre', 'dameroap', '1991-10-09 00:00:00', '', 'Sales Representative', 1450.0, 17.5, 35, 3),
         (15, 'Hardwick', 'Elaine', 'hardwiem', '1992-02-07 00:00:00', '', 'Stock Clerk', 1400.0, '', 41, 6),
         (16, 'Brown', 'George', 'browngw', '1990-03-08 00:00:00', '', 'Stock Clerk', 940.0, '', 41, 6),
         (17, 'Washington', 'Thomas', 'washintl', '1991-02-09 00:00:00', '', 'Stock Clerk', 1200.0, '', 42, 7),
         (18, 'Patterson', 'Donald', 'patterdv', '1991-08-06 00:00:00', '', 'Stock Clerk', 795.0, '', 42, 7),
         (19, 'Bell', 'Alexander', 'bellag', '1991-05-26 00:00:00', '', 'Stock Clerk', 850.0, '', 43, 8),
         (2, 'Smith', 'Doris', 'smithdj', '1990-03-08 00:00:00', '', 'VP, Operations', 2450.0, '', 41, 1),
         (20, 'Gantos', 'Eddie', 'gantosej', '1990-11-30 00:00:00', '', 'Stock Clerk', 800.0, '', 44, 9),
         (21, 'Stephenson', 'Blaine', 'stephebs', '1991-03-17 00:00:00', '', 'Stock Clerk', 860.0, '', 45, 10),
         (22, 'Chester', 'Eddie', 'chesteek', '1990-11-30 00:00:00', '', 'Stock Clerk', 800.0, '', 44, 9),
         (23, 'Pearl', 'Roger', 'pearlrg', '1990-10-17 00:00:00', '', 'Stock Clerk', 795.0, '', 34, 9),
         (24, 'Dancer', 'Bonnie', 'dancerbw', '1991-03-17 00:00:00', '', 'Stock Clerk', 860.0, '', 45, 7),
         (25, 'Schmitt', 'Sandra', 'schmitss', '1991-05-09 00:00:00', '', 'Stock Clerk', 1100.0, '', 45, 8),
         (3, 'Norton', 'Michael', 'nortonma', '1991-06-17 00:00:00', '', 'VP, Sales', 2400.0, '', 31, 1),
         (4, 'Quentin', 'Mark', 'quentiml', '1990-04-07 00:00:00', '', 'VP, Finance', 2450.0, '', 10, 1),
         (5, 'Roper', 'Joseph', 'roperjm', '1990-03-04 00:00:00', '', 'VP, Administration', 2550.0, '', 50, 1),
         (6, 'Brown', 'Molly', 'brownmr', '1991-01-18 00:00:00', '', 'Warehouse Manager', 1600.0, '', 41, 2),
         (7, 'Hawkins', 'Roberta', 'hawkinrt', '1990-05-14 00:00:00', '', 'Warehouse Manager', 1650.0, '', 42, 2),
         (8, 'Burns', 'Ben', 'burnsba', '1990-04-07 00:00:00', '', 'Warehouse Manager', 1500.0, '', 43, 2),
         (9, 'Catskill', 'Antoinette', 'catskiaw', '1992-02-09 00:00:00', '', 'Warehouse Manager', 1700.0, '', 44, 2))


s_dept = (('ID', 'NAME', 'REGION_ID'),
        (10, 'Finance', 1),
        (31, 'Sales', 1),
        (32, 'Sales', 2),
        (33, 'Sales', 3),
        (34, 'Sales', 4),
        (35, 'Sales', 5),
        (41, 'Operations', 1),
        (42, 'Operations', 2),
        (43, 'Operations', 3),
        (44, 'Operations', 4),
        (45, 'Operations', 5),
        (50, 'Administration', 1))

# select * from s_dept
print "\nselect * from s_dept: ", [ i for i in s_dept[1::] ]

# select last_name, first_name, title, salary from s_emp
print "\nselect last_name, first_name, title, salary from s_emp:", [ [i[1], i[2], i[6], i[7]] for i in s_emp[1::] ]

# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40: ", [ [i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40 ]

# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by last_name: ", sorted([ [i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40 ], key = lambda x: x[0])

# select last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc
print "\nselect last_name, first_name, title, salary from s_emp where salary > 1500 and dept_id > 40 order by salary desc: ", sorted([ [i[1], i[2], i[6], i[7]] for i in s_emp[1::] if i[7] > 1500 and i[9] > 40 ], key = lambda x: x[3], reverse = True)

# select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id)
print "\nselect last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id): ", [ [i[1], i[2], i[6], i[7], j[1]] for i in s_emp[1::] for j in s_dept[1::] if i[9]==j[0] ]

# select dept_id, avg(salary) from s_emp group by dept_id order by dept_id
print "\nselect dept_id, avg(salary) from s_emp group by dept_id order by dept_id: "
for department in sorted({ d[9] for d in s_emp[1::] }): print (lambda dept_id, avgSal: [dept_id, avgSal])(department, (lambda l: round(sum(l) / len(l), 2))(map(float, [ e[7] for e in s_emp[1::] if e[9] == department ])))

# select dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500
print "\nselect dept_id, avg(salary) from s_emp group by dept_id having avg(salary) < 1500: "
for department in { d[9] for d in s_emp[1::] }: print (lambda dept_id, avgSal: (dept_id, avgSal) if avgSal < 1500 else '')(department, (lambda l: round(sum(l) / len(l), 2))(map(float,[ e[7] for e in s_emp[1::] if e[9] == department ])))