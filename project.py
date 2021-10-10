###############################################################################################
#IMPORTS
import dateCalculator as dc
import progressPie as pp

"""
###############################################################################################
FUNCTION TO RUN THE ENTIRE SYPHT TAKE-HOME TASK
"""
def runSyphtTasks():
    #Print entry message
    print("#############################################################################################\n\r" +
          "BEGINNING THE SYPHT TAKE HOME PROJECT\n\r" +
          "#############################################################################################")

    #Run the main while loop to hold the different tasks for the project
    while True:
        #Print the options for the Sypht take home tasks. Get the user selection
        print("Project options:\n\r" +
              "< 1 > --- Interstitial Day Period Calculator (Mandatory Task)\n\r" +
              "< 2 > --- Progress Pie Display and Calculator (Bonus Problem 2)\n\r"
              "< Q > --- Quit the project")

        userInput = input("Please enter the number of the project you would like to run:")

        #Branch to the needed case
        if userInput[0].lower() == "1":
            dc.dateCalculatorMain()
        elif userInput[0].lower() == "2":
            pp.progressPieMain()
        elif userInput[0].lower() == "q":
            break
        else:
            print("\n\rERROR: User entry '{}' is not a valid input.\n\r".format(userInput))

    #Print the exit message and return
    print("\n\n\r#############################################################################################\n\r" +
          "EXITING THE SYPHT TAKE HOME PROJECT\n\r" +
          "#############################################################################################")
    return

###############################################################################################
#RUNNER FOR WHEN THIS FILE IS CALLED DIRECTLY
if __name__ == '__main__':
    runSyphtTasks()