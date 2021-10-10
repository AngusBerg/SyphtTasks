# SYPHT APPLICATION TAKE-HOME TASKS

**By Angus Berg. Written on a Windows Machine with Python 3.7**

This repository contains Angus Berg's answers to the Sypht take home task provided. This Read-Me has been produced to
provide some very high-level information for my response to the tasks.

If you wish to run my responses to these take home tasks, you can download the file to your local machine and either:

- Run "python project.py" in the command line from the folder to which you have downloaded the files. Requires the
"PYTHON_HOME" environment variable to be set.
- Double-click the "runProject.bat" file from the folder to which you have downloaded the files. Requires the
"PYTHON_HOME" environment variable to be set.
- Extract the "compiledProject" zip file to a chosen location, and then run the "project.exe" file that can be found
inside the folder it contains. Running it in this way should not require a Python installation.

## Date Calculator Mandatory Task - Completed
The date calculator mandatory task has been completed. Some notes on the implementation:

- Rather than calculating the difference between two dates directly, the calculator finds how far each date is from a 
chosen starting point and then find the difference between these calculated numbers. This was done to simplify the
internal calculations.
- The chosen day 1 for this calculator was 01/01/1583. This was chosen since it was shortly after the introduction of
the Gregorian Calendar (Which was first adopted by a nation in October 1582).
- The Date-Gap-Calculator as written follows the generic Gregorian calendar from that date, and does not account for
geographical variations from that calendar, such as the date-shifts of late-adopting nations or the times that nations
have crossed the International Date Time.

### Libraries for Date Calculator:

- Typing (included with standard Python installation)
- Re (included with standard Python installation)

## Sypht Platform Bonus Task - Not Attempted
While the Sypht Platform and API are very impressive, my initial exploration of the platform shows that the solution is
optimised for documents like invoices and receipts, and I did not have access to enough documents of this kind that were
suitably anonymised for use in a test task. As such, I chose to focus on other bonus tasks.

## Progress Pie Bonus Task - Completed
The Progress Pie task has been completed with two modes; one mode simply runs the progress pie and displays it in a
Matplotlib plot, while the other reads lines in from a file with the format described in the task description.
Some notes on the implementation:

- The file-reading mode is set to take input from ".txt" files by default, but the file-dialog that is used to select
the input file can be set to accept any file. The program will run successfully on any file that can be read in a
line-by-line fashion with text-like content.
- The pie-display mode has to have its X value inverted when compared with the implementation described in the task
sheet. This is because the task sheet describes (0,0) as the bottom-left corner, while Matplotlib has (0,0) as the
top-left corner.

### Libraries for the Progress Pie:

- Typing (included with standard Python installation)
- Re (included with standard Python installation)
- Math (included with standard Python installation)
- TKinter (included with standard Python installation)
- OS (included with standard Python installation)
- Numpy
- Matplotlib

## Sentiment Analysis Bonus Task - Not Attempted
Due to time constraints, sentiment analysis task not attempted