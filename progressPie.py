###############################################################################################
#IMPORTS
from typing import List
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from math import sqrt, acos, pi
from tkinter import filedialog
from os import getcwd
import tkinter as tk
import numpy as np
import re

###############################################################################################
#CONSTANTS
PIE_RADIUS = 50

"""
###############################################################################################
FUNCTION TO CALCULATE THE LENGTH OF A LINE SECTION
"""
def calculateLengthOfLine(xp: float, yp: float, xc: float = PIE_RADIUS, yc: float = PIE_RADIUS) -> float:
    return sqrt(abs(xp - xc)**2 + abs(yp - yc)**2)

"""
###############################################################################################
FUNCTION TO CALCULATE THE CLOCKWISE ROTATION OF A POINT FROM THE UPPER VERTICAL
"""
def calculateAngleOfPointFromCentre(xp: float, yp: float, xc: float = PIE_RADIUS, yc: float = PIE_RADIUS) -> float:
    #Calculate the position changes and the line length
    dX = xp - xc
    dY = yp - yc
    ll = calculateLengthOfLine(xp, yp, xc, yc)

    #Calculate the angle from the vertical using the Y displacement and length of line segment
    try:
        aa = acos(dX/ll)

        #Return the value extracted based on which side of the vertical it is on
        if dY >= 0:
            return aa
        else:
            return 2 * pi - aa

    except ZeroDivisionError:
        #This case covers when the position being tested is the centre of the circle
        return 0

"""
###############################################################################################
FUNCTION TO CALCULATE THE PERCENTAGE OF ROTATION THAT AN ANGLE REPRESENTS
"""
def calculatePercentageOfRotation(radians: float) -> float:
    return round(((radians * 100) / (2 * pi)), 0)

"""
###############################################################################################
FUNCTION TO DETERMINE IF A GIVEN PIXEL IN THE PIE SHOULD BE FILLED
"""
def shouldPixelOfPieBeFilled(pp: float, xx: float, yy: float) -> bool:
    #Calculate the length and percentage associated with the given pixel
    pixelLength = calculateLengthOfLine(xx, yy)
    pixelAngle = calculateAngleOfPointFromCentre(xx, yy)
    pixelPercentage = calculatePercentageOfRotation(pixelAngle)

    #Return a boolean based on the length and percentage
    return pixelLength <= PIE_RADIUS and pixelPercentage <= pp

"""
###############################################################################################
FUNCTION TO GENERATE A PIE MATCHING THE CURRENT PERCENTAGE
"""
def createPieForPercentage(percent: float) -> np.array:
    #Create an empty pie that is twice the specified radius in width
    pieDiameter = int(2 * PIE_RADIUS + 1)
    piePixels = np.zeros((pieDiameter, pieDiameter))

    #Run through each pixel and set to either true or false
    for yy in range(0, pieDiameter):
        for xx in range(0, pieDiameter):
            testX = pieDiameter - xx - 1
            testY = yy
            piePixels[xx, yy] = shouldPixelOfPieBeFilled(percent, testX, testY)

    #Return the pie that has been generated
    return piePixels

"""
###############################################################################################
FUNCTION TO UPDATE THE PIE THAT IS CURRENTLY BEING DISPLAYED
"""
def updateCurrentPie(frame, *fargs):
    #The frame is the current percentage; calculate the pie as appropriate for the percentage
    piePixels = createPieForPercentage(frame)

    #The positional arguments are the images that need updating; update and return
    for image in fargs: image.set_array(piePixels)
    return

"""
###############################################################################################
FUNCTION TO DISPLAY THE LOADING PIE
"""
def runLoadingPie(milliDelay: int = 10):
    #Start the empty figure
    figure = plt.figure()
    display = figure.add_subplot(1, 1, 1)
    image = display.imshow(createPieForPercentage(0), animated=True)

    #Run the animation of the loading pie
    anim = FuncAnimation(figure, updateCurrentPie, frames=101, fargs=(image,), interval=milliDelay, repeat=True)
    print("Close the pie figure to continue.")
    plt.show()

    #Delay so that the results can be seen and return
    return

"""
###############################################################################################
FUNCTION TO EXTRACT ALL SEGMENTS WHICH MATCH A REGEX PATTERN FROM A STRING
"""
def extractAllMatches(string: str, pattern: str) -> List[str]:
    output = []
    startPos = 0

    while True:
        #Look for a match in the string
        currString = string[startPos:]
        match = re.search(pattern, currString)

        #Return if there is no match. Else, process the new match
        if match is None:
            return output
        else:
            output.append(currString[match.start():match.end()])
            startPos += match.end()

"""
###############################################################################################
FUNCTION TO RUN A SET OF POSITIONAL TESTS FROM A FILE
"""
def runPositionalTestsFromFile():
    #Initialise tkinter
    window = tk.Tk()

    #Use the file dialog to select the file, starting from the CWD
    filePath = filedialog.askopenfilename(initialdir = getcwd(), title = "Select a File",
                                          filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))

    #Run the update to complete the file dialog process
    window.update_idletasks()
    window.update()
    window.destroy()

    #Open the file and read in the first line; check it for a number
    numericalRegex = "[0-9]+"
    targetFile = open(filePath, mode="r")

    firstLineText = targetFile.readline()
    firstLineNumber = re.search(numericalRegex, firstLineText)

    if firstLineNumber is None:
        #The first line of this file doesn't contain a number, this file is not valid input
        print("\n\rERROR: This file does not have a case count number in its first line")

    else:
        #Extract the case count number. Initialise other directing variables
        caseLimit = int(firstLineText[firstLineNumber.start():firstLineNumber.end()])
        caseCount = 1

        #Loop through the lines of the file, producing results as appropriate
        for line in targetFile:
            #Extract the numbers from the line of the file
            numberText = extractAllMatches(line, numericalRegex)
            lineNumbers = [float(x) for x in numberText]

            #Branch based on the case that is being tested
            if len(lineNumbers) < 3:
                print("Case #{}: Not enough numbers in line to calculate result".format(caseCount))
            elif not min([(0 <= x <= (2 * PIE_RADIUS)) for x in lineNumbers[:3]]):
                print("Case #{}: Numbers extracted for case were outside the valid bounds".format(caseCount))
            elif shouldPixelOfPieBeFilled(lineNumbers[0], lineNumbers[1], lineNumbers[2]):
                print("Case #{}: Black".format(caseCount))
            else:
                print("Case #{}: White".format(caseCount))

            #Increment the case number and check if the end has been reached
            caseCount += 1
            if caseCount > caseLimit: break

    #Close the file, print the exit message and return
    targetFile.close()
    print("\n\rExtraction of data from chosen file completed. Returning from process.\n\r")
    return

###############################################################################################
#RUNNER FOR WHEN THIS FILE IS CALLED DIRECTLY
if __name__ == '__main__':
    runPositionalTestsFromFile()