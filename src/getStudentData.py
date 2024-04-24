#   Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
import csv
import dataHandler

def getStudentData() -> dict:
    """
    Loads the students data from the csv file specified in dataHandler.py.
    :return:
    """
    studentData: dict = {}

    with open(dataHandler.studentDataCSVPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=dataHandler.csv_delimiter)
        for row in reader:
            studentData[row[0]] = {}
            studentData[row[0]]["CLASS"] = row[1]
            studentData[row[0]]["WUENSCHE"] = [row[2], row[3], row[4], row[5], row[6]]
    return studentData


if __name__ == '__main__':
    getStudentData()