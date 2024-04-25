# Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
"""
dataHandler.py manges the data (Students, Lectures, etc.) for the program.
NOT the actual storaging of the data
"""
import os
import logging
import csv

# ---------------------------------------------------------------------------
#   For logging purposes
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# ---------------------------------------------------------------------------
#   CSV
# ---------------------------------------------------------------------------

data_folder: str = "src/data/"
studentDataCSVPath: str = f"{data_folder}schueler_wuensche.csv"
presentationDataCSVPath: str = f"{data_folder}presentation.csv"
csv_delimiter: str = ","

# ---------------------------------------------------------------------------
#   DATA
# ---------------------------------------------------------------------------

studentData: dict = {}
presentationData: dict = {}

"""
def test():
    if not os.path.isfile(studentDataCSVPath):
        logging.error("Student data CSV is not a file")


if os.getcwd()[-3:] == "src":
    os.chdir(os.getcwd()[:-4])

test()
"""


def loadStudentData():
    """
    Loads the students data from the csv file
    :return:
    """
    global studentData
    studentData = {}
    with open(studentDataCSVPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=csv_delimiter)
        for row in reader:
            studentData[row[0]] = {}
            studentData[row[0]]["CLASS"] = row[1]
            studentData[row[0]]["WUENSCHE"] = [row[2], row[3], row[4], row[5], row[6]]
    return studentData


def loadPresentationData():
    """
    Loads the students data from the csv file
    :return:
    """
    global presentationData
    presentationData = {}
    with open(presentationDataCSVPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=csv_delimiter)
        for row in reader:
            studentData[row[0]] = {}
            studentData[row[0]]["MAX-ANZAHL"] = row[1]
            studentData[row[0]]["WUENSCHE"] = [row[2], row[3], row[4], row[5], row[6]]
    return studentData
