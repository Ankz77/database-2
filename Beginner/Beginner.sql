CREATE TABLE student(
	student_id INT,
    _name VARCHAR(30),
    major VARCHAR(30),
    PRIMARY KEY(student_id)
);

DESCRIBE student;
ALTER TABLE student ADD gpa DECIMAL(3, 2);

