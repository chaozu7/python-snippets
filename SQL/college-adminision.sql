SELECT sID, sName, GPA from Student
WHERE GPA > 3.5
ORDER BY GPA DESC;

SELECT distinct sName, major   #bez duplikatów
FROM Student
WHERE Student.sID = Apply.sID;


#kiedy zawiera bio
SELECT sID, sName, major
FROM Apply
WHERE major like %bio%;

SELECT GPA*(sizeHS/1000) as scaledGPA
FROM Student;