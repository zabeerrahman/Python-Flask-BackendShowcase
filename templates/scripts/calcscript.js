var total;

var gradeCounter;

var grade;

var gradeValue;

var average;

var students;

total = 0;

gradeCounter = 1;

students = window.prompt("How many students in this class?");

while (gradeCounter <= students) {
    grade = window.prompt("Enter integer grade for student " + gradeCounter + ":", "0");
    gradeValue = parseInt(grade);
    total = total + gradeValue;
    gradeCounter = gradeCounter + 1;
}

average = total / students;

document.writeln("<h1>Class average is " + average + "</h1>");

if (average <= 60) {
    document.writeln("<h3>Class average was too low! Retake!</h3>");
} else if (average == 100) {
    document.writeln("<h3>Class average 100%! Excelsior instructor! </h3>");
} else {
    document.writeln("<h3>Class average was as expected. Good job. </h3>");
}
