var total;

var gradeCounter;

var grade;

var gradeValue;

var average;

var required;

var weight;

total = 0;

gradeCounter = 0;

weight = window.prompt("Enter Final Exam weight (in %)", "0");

grade = window.prompt("Enter Integer Grades of previous exams individually, -1 to Quit when finished", "0");

gradeValue = parseInt(grade);

while (gradeValue != -1) {
    total = total + gradeValue;
    gradeCounter = gradeCounter + 1;
    grade = window.prompt("Enter Integer Grade, -1 to Quit:", "0");
    gradeValue = parseInt(grade);
}

if (gradeCounter != 0) {
    average = total / gradeCounter;
    document.writeln("<h1>Student's current grade is " + average + "%</h1>");
    document.writeln("");
    required = (90 - average * (1 - weight / 100)) / (weight / 100);
    document.writeln("<h3>The student would need a score of at least " + required + " on the final exam to pass the class with an A. Good Luck!! </h3>");
} else {
    document.writeln("<p>No grades were entered.</p>");
}
