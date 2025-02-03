use [AZURE-SQL];
create table Subjects (Name varchar(20),Cs int,Mat int,Eng int);
Insert into Subjects values('Sam',100,95,91),('Ram',95,100,90),('Tom',55,70,75);
select * from Subjects where Cs >90 order by Name ASC;
INSERT INTO Subjects(Name, Cs, Mat, Eng) VALUES 
('John', 92, 88, 85), 
('Emily', 88, 92, 90), 
('Michael', 85, 90, 92), 
('Jessica', 90, 85, 88), 
('David', 88, 92, 90), 
('Sarah', 92, 88, 85), 
('Christopher', 90, 85, 88), 
('Olivia', 85, 90, 92), 
('Daniel', 88, 92, 90), 
('Sophia', 92, 88, 85), 
('Jacob', 90, 85, 88), 
('Isabella', 85, 90, 92), 
('William', 88, 92, 90), 
('Ava', 92, 88, 85), 
('Alexander', 90, 85, 88), 
('Emma', 85, 90, 92), 
('Benjamin', 88, 92, 90);
ALTER TABLE Subjects ADD  Department VARCHAR(50);
select * from Subjects;

INSERT INTO Subjects(Name, Cs, Mat, Eng, Department)
VALUES
('John', 92, 88, 85, 'Computer Science'),
('Emily', 88, 92, 90, 'Mathematics'),
('Michael', 85, 90, 92, 'Engineering'),
('Jessica', 90, 85, 88, 'Computer Science'),
('David', 88, 92, 90, 'Mathematics'),
('Sarah', 92, 88, 85, 'Computer Science'),
('Christopher'	, 90, 85, 88, 'Computer Science'),
('Olivia', 85, 90, 92, 'Engineering'),
('Daniel', 88, 92, 90, 'Mathematics'),
('Sophia', 92, 88, 85, 'Computer Science'),
('Jacob', 90, 85, 88, 'Computer Science'),
('Isabella', 85, 90, 92, 'Engineering'),
('William', 88, 92, 90, 'Mathematics'),
('Ava', 92, 88, 85, 'Computer Science'),
('Alexander', 90, 85, 88, 'Computer Science'),
('Emma', 85, 90, 92, 'Engineering'),
('Benjamin', 88, 92, 90, 'Mathematics'),
('Anna', 92, 88, 85, 'Computer Science'),
('Thomas', 88, 92, 90, 'Mathematics'),
('Lily', 85, 90, 92, 'Engineering');
-- Task-1) SELECT MAX(Cs) AS Highest_Cs,MAX(Mat) AS Highest_Mat,MAX(Eng) AS Highest_Eng FROM Subjects;
-- Task-2) SELECT MIN(Cs) AS Lowest_Cs,MIN(Mat) AS Lowest_Mat,MIN(Eng) AS Lowest_Eng FROM Subjects;
-- Task-3) SELECT Department,COUNT(*) AS Count FROM Subjects GROUP BY Department;