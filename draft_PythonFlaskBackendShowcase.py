# First import the Flask class from the flask package into Python
from flask import Flask

# Setting variable "app" to instance of Flask class, since Python will be running the script, __name__ = __main__
app = Flask(__name__)

# Create route(s) for home page
@app.route("/")
@app.route("/home")
def home():                                                                                                                      # Create empty function for each page
    return '''<h1>Hello!</h1>                                                                                         <!-- Return in flask is automatically converted into response object for each page -->
              <h2>Welcome to Zab's  project, which showcases different mock Exam Logistics in order to highlight the features of Flask: a Python Framework for building web-applications</h2>
              <p><strong>To navigate to a page, simply type the shortcut of the page at the end of the url! For example, type "localhost:5000/xyz" to navigate to a page with shortcut "xyz"</strong></p>

              <ul>
                <li><strong>Class Grade Average Calculator</strong><i>(allows user to find the average grade for a class of any size)</i><strong>(shortcut: calc)</strong></li>
                <li><strong>Examination Statistics</strong><i>(allows user to compare exam results of entire class)</i><strong>(shortcut: stats)</strong></li>
                <li><strong>Final Grade Resolver</strong><i>(allows user to find necessary score to receive an A based on previous exams and weight)</i><strong>(shortcut: resolve)</strong></li>
              </ul>'''

# Create route for Class Grade Average Calculator
@app.route("/calc", methods = ["GET", "POST"])                                                                                   # GET message is sent, and server returns data. Most common method
def calculator():                                                                                                                # POST sends HTML form data to server. Received data is not cached
    return '''<html>                                                                                                             <!-- Create standard HTML template with JavaScript script inside multiline quote -->
                   <head>
                      <meta charset="utf-8">
                      <title>Class Average Program</title>
                      <script type="text/javascript">

                         var total;                                                                                              <!-- Declare all variables that will be used for calulator -->
                         var gradeCounter;
                         var grade;
                         var gradeValue;
                         var average;
                         var students;

                         total = 0;                                                                                              <!-- Assign known values to variables/prompt user -->
                         gradeCounter = 1;
                         students = window.prompt("How many students in this class?");

                         while (gradeCounter <= students)   {                                                                    <!-- Loop asking for student grades while our incremented variable iterates through students -->
                            grade = window.prompt("Enter integer grade for student " + gradeCounter + ":", "0")
                            gradeValue = parseInt(grade);
                            total = total + gradeValue;                                                                          <!-- Add each grade to rolling sum -->
                            gradeCounter = gradeCounter + 1;
                         }

                         average = total / students;                                                                             <!-- Compute average and display JavaScript variable using HTML styling, parsed by flask -->
                         document.writeln("<h1>Class average is " + average + "</h1>");

                         if (average <= 60) {                                                                                    <!-- Conditional to display comments according to Grade average results -->
                            document.writeln("<h3>Class average was too low! Retake!</h3>");
                         } else if (average == 100) {
                            document.writeln("<h3>Class average 100%! Excelsior instructor! </h3>")
                         } else {
                            document.writeln("<h3>Class average was as expected. Good job. </h3>")
                         }

                      </script>
                   </head>
                   <body>

                   </body>
             </html>'''                                                                                                          # Close HTML tags and end multiline string

# Create route for Examination Statistics and define methods that will be used
@app.route("/stats", methods = ["GET", "POST"])
def statistics():
    return '''<html>                                                                                                             <!-- Create standard HTML template with JavaScript script inside multiline quote -->
                   <head>
                      <meta charset="utf-8">
                      <title>Examination Results Program</title>
                      <script type="text/javascript">

                         var passes;                                                                                             <!-- Declare all variables that will be used for statistics -->
                         var failures;
                         var student;
                         var result;
                         var totalStudents;

                         totalStudents = window.prompt("How many students in this class?");                                      <!-- Assign known values to variables/prompt user -->
                         passes = 0;
                         failures = 0;
                         student = 1;

                      do {                                                                                                       <!-- Loop asking user to input 1 for every student who passed -->
                         result = window.prompt("Enter result of student " + student + " (1=pass,any other input=fail)", "0");

                         if (result == "1") {                                                                                    <!-- Conditional to add pass/fail count to rolling sums -->
                            passes = passes +1;
                         }
                         else {
                            failures = failures + 1;
                         }
                         student = student + 1;
                      } while (student <= totalStudents);

                      document.writeln("<h1>Examination Results</h1>");                                                          <!-- Display results -->
                      document.writeln("<h3>Passed: " + passes + "; Failed: " + failures + "</h3>");

                      if (passes > (totalStudents * 0.6)) {                                                                      <!-- Conditional to display comments according to Exam statistics results -->
                         document.writeln("<h3>Excelsior instructor!</h3>");
                      }
                      </script>
                   </head>
                   <body>

                   </body>
             </html>'''                                                                                                          # Close HTML tags and end multiline string

# Create route for Final Grade Resolver and define methods that will be used
@app.route("/resolve", methods = ["GET", "POST"])
def resolver():
    return '''<html>                                                                                                             <!-- Create standard HTML template with JavaScript script inside multiline quote -->
                   <head>
                      <meta charset="utf-8">
                      <title>Final Grade Resolver</title>
                      <script type="text/javascript">

                      var total;                                                                                                 <!-- Declare all variables that will be used for statistics -->
                      var gradeCounter;
                      var grade;
                      var gradeValue;
                      var average;
                      var required;
                      var weight;

                      total = 0;                                                                                                 <!-- Assign known values to variables/prompt user -->
                      gradeCounter = 0;
                      weight = window.prompt("Enter Final Exam weight (in %)", "0");
                      grade = window.prompt("Enter Integer Grades of previous exams individually, -1 to Quit when finished", "0");

                      gradeValue = parseInt(grade);                                                                              <!-- Make variable usable for mathematics -->

                      while (gradeValue != -1)   {                                                                               <!-- Loop asking user to input grades until -1 is entered -->
                         total = total + gradeValue;
                         gradeCounter = gradeCounter + 1;

                         grade = window.prompt("Enter Integer Grade, -1 to Quit:", "0");
                         gradeValue = parseInt(grade);                                                                           <!-- Make variable usable for mathematics -->
                      }

                      if (gradeCounter != 0)   {                                                                                 <!-- Conditional for running and displaying math code -->
                         average = total / gradeCounter;
                         document.writeln("<h1>Student's current grade is " + average + "%</h1>");                               <!-- Calculate current age and what student would need based on user entries. Display -->
                         document.writeln("");
                         required = (90 - (average * (1 - (weight / 100)))) / (weight / 100);
                         document.writeln("<h3>The student would need a score of at least " + required + " on the final exam to pass the class with an A. Good Luck!! </h3>");
                      }
                      else {                                                                                                     <!-- Condition for when no grades are entered -->
                         document.writeln("<p>No grades were entered.</p>")
                      }

                      </script>
                   </head>
                   <body>

                   </body>
             </html>'''                                                                                                          # Close HTML tags and end multiline string

if __name__ == "__main__":                                                                                                       # Create conditional for when we execute using Python
    app.run(debug=True)                                                                                                          # Allows flask to know where to run the active Debugger
