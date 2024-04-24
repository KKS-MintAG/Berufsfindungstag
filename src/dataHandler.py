#   Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
import os

import logging
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')


studentDataCSVPath: str = "src\\data\\schueler_wuensche.csv"
studentData: dict = {}

csv_delimiter: str = ","

def test():
    if not os.path.isfile(studentDataCSVPath):
        logging.error("Student data CSV is not a file")

if os.getcwd()[-3:] == "src":
    os.chdir(os.getcwd()[:-4])

test()

def irgend():
    import getStudentData
    print(getStudentData.getStudentData())

if __name__ == "__main__":
    irgend()