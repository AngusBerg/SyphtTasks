###############################################################################################
#IMPORTS
from typing import Tuple, List, Optional
import re

###############################################################################################
#CONSTANTS
MINIMUM_YEAR = 1583
MONTH_LENGTHS = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

"""
###############################################################################################
CLASS TO HOLD THE PARSED DATE VALUE
"""
class ParsedDate:
    def __init__(self, dateString: str, day: int, month: int, year: int):
        self.dateString = dateString
        self.day = day
        self.month = month
        self.year = year

"""
###############################################################################################
FUNCTION TO DETERMINE IF THE CURRENT YEAR IS A LEAP YEAR
"""
def checkLeapYear(year: int) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

"""
###############################################################################################
FUNCTION TO CHECK IF THE CURRENT DAY IS THE FEBRUARY 29TH LEAP DAY
"""
def checkLeapDay(day: int, month: int, year: int) -> bool:
    if day == 29 and month == 2 and checkLeapYear(year):
        return True
    else:
        return False

"""
###############################################################################################
FUNCTION TO PARSE A DATE STRING INTO THE VALID DATE PARTS
"""
def parseDateString(dateString: str) -> Optional[ParsedDate]:
    #Split the date-string at the split character and convert into integers
    dateParts = [int(part) for part in dateString.split('/')]
    day: int = dateParts[0]
    month: int = dateParts[1]
    year: int = dateParts[2]

    #If the year is a 2-digit number, add 1900
    if 0 < year < 100:
        year += 1900

    #Check if any of the elements are invalid
    if year < MINIMUM_YEAR:
        print("ERROR: The string {} is prior to the introduction of the Gregorian Calendar".format(dateString))
        return None

    if 1 > month > 12:
        print("ERROR: The string {} is not a valid date".format(dateString))
        return None

    elif day > MONTH_LENGTHS[month] and not checkLeapDay(day, month, year):
        print("ERROR: The string {} is not a valid date".format(dateString))
        return None

    else:
        #This datestring is valid; return the parsed value
        return ParsedDate(dateString, day, month, year)

"""
###############################################################################################
FUNCTION TO EXTRACT A CORRECTLY FORMATTED DATE STRING/S FROM AN INPUT STRING
"""
def extractDatesFromString(rawInput: str, currentOutput: Tuple[int, List[ParsedDate]] = (0, [])) \
        -> Tuple[int, List[ParsedDate]]:
    #Determine if there is a match for an Australian Date in the raw string (dd/mm/yyyy)
    dateMatch = re.search(r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{2,4}", rawInput)

    #Check if a match was made. If not, return the current output. Else, parse the extract and recurse
    if dateMatch is None:
        return currentOutput
    else:
        #Parse the date string pulled. Reconstruct the output
        parsedDate = parseDateString(rawInput[dateMatch.start():dateMatch.end()])

        if parsedDate is not None:
            currentOutput = (currentOutput[0] + 1, currentOutput[1].copy())
            currentOutput[1].append(parsedDate)

        #Recurse to search for another matching string after the first input
        return extractDatesFromString(rawInput[dateMatch.end():], currentOutput)

"""
###############################################################################################
FUNCTION TO CALCULATE HOW MANY DAYS AFTER 1ST JANUARY IN THE MINIMUM YEAR THE DATE IN QUESTION OCCURRED
"""
def calculateGregorianDaysElapsed(date: ParsedDate) -> int:
    #Get the total number of days from the years that have elapsed since the minimum year
    daysDeltaFromYears = 365 * (date.year - MINIMUM_YEAR)

    #Get the total number of days from the months that have elapsed this year
    daysDeltaFromMonths = sum([MONTH_LENGTHS[mm] for mm in range(0, date.month)])

    #Get the total number of days from leap years that have elapsed since the minimum year
    daysDeltaFromLeaps = sum([int(checkLeapYear(yy)) for yy in range(MINIMUM_YEAR, date.year)])
    if date.month > 2 and checkLeapYear(date.year): daysDeltaFromLeaps += 1

    #Sum the day values and return the total
    return daysDeltaFromYears + daysDeltaFromMonths + daysDeltaFromLeaps + date.day

"""
###############################################################################################
FUNCTION TO CALCULATE THE TIME THAT HAS PASSED BETWEEN EACH PAIR OF DATES PASSED IN
"""
def calculateTimeChangeBetweenDatePairs(dates: List[ParsedDate]) -> List[List[Tuple[int, str, str]]]:
    print("\n\rCalculating Interstitial Date Periods:")

    #Run through each combination of the dates provided
    dateCount = len(dates)
    outputLists = []

    for i in range(dateCount):
        #Append a fresh list to hold the calculated results
        outputLists.append([])

        for j in range(dateCount):
            #Calculate the time passed between the two dates. Append into the output lists
            daysPassed = abs(calculateGregorianDaysElapsed(dates[i]) - calculateGregorianDaysElapsed(dates[j]))
            if daysPassed > 0: daysPassed -= 1

            outputLists[i].append((daysPassed, dates[i].dateString, dates[j].dateString))

            #If this case ia above the diagonal, print the result (Ensures uniqueness)
            if i < j:
                print("  - Between {} and {}, the number of days which passed was {}"
                      .format(dates[i].dateString, dates[j].dateString, daysPassed))

    #Return the results of the calculations
    print("")
    return outputLists

"""
###############################################################################################
MAIN FUNCTION OF THE DATE CALCULATOR
"""
def dateCalculatorMain():
    #Print a message to mark that the date-gap calculator is starting
    print("#########################################################################\n\r" +
          "ENTERING INTERSTITIAL DAY PERIOD CALCULATOR\n\r" +
          "#########################################################################")

    #Enter an infinite loop within which to perform the  calculations
    while True:
        #Get input from the user
        userInput1 = input("Please enter the date/s for which you would like to find " +
                           "the interstitial number of days, or 'Q' to quit:\n\r")

        #Check if the user wishes to Quit
        if 'q' in userInput1.lower() and len(userInput1) == 1:
            break

        #If the user doesn't wish to quit, try to extract dates from the input
        datesExtracted = extractDatesFromString(userInput1)

        #Check how many dates were extracted and branch to the desired behaviour
        if datesExtracted[0] > 1:
            #More than 1 date was extracted; Calculate the interstitials
            calculateTimeChangeBetweenDatePairs(datesExtracted[1])

        elif datesExtracted[0] == 1:
            #Only one date was provided; See if the user wishes to enter another
            print("\n\rOne date extracted from previous input.")
            userInput2 = input("Please enter additional date/s for interstitial calculation, leave blank to " +
                               "calculate days passed since {}, or 'Q' to quit:\n\r".format(MINIMUM_YEAR))

            #Check if the user wishes to Quit
            if 'q' in userInput2.lower() and len(userInput2) == 1:
                break

            #Extract dates again
            furtherExtracts = extractDatesFromString(userInput2, datesExtracted)

            #Branch based on the number of dates extracted
            if furtherExtracts[0] > 1:
                #More than 1 date was extracted; Calculate the interstitials
                calculateTimeChangeBetweenDatePairs(furtherExtracts[1])

            else:
                #No additional date was entered; append on the default date and calculate interstitials
                furtherExtracts[1].append(ParsedDate("01/01/{}".format(str(MINIMUM_YEAR)), 1, 1, MINIMUM_YEAR))
                calculateTimeChangeBetweenDatePairs(furtherExtracts[1])

        else:
            #No valid dates found in the input string; Print message and loop
            print("\n\rERROR: No valid date found in the input string '{}'\n\r".format(userInput1))

    #Print a message to announce that the calculator is quitting and return to caller
    print("\n\r#########################################################################\n\r" +
          "EXITING INTERSTITIAL DAY PERIOD CALCULATOR\n\r" +
          "#########################################################################")
    return

###############################################################################################
#RUNNER FOR WHEN THIS FILE IS CALLED DIRECTLY
if __name__ == '__main__':
    dateCalculatorMain()