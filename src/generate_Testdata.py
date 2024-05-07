# Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
import csv
import os

import dataHandler
import random

first_names = ['anton', 'bert', 'carl', 'dora', 'emil', 'frieda', 'gerda', 'hans', 'ilse', 'joachim', 'klaus',
               'leo', 'manfred', 'nina', 'otto', 'paul', 'richard', 'susi', 'theo', 'uwe', 'verena',
               'wilfried']
classes = ["9a", "9b", "9c", "9d", "9e", "9f"]

wishes = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17",
          "V18", "V19", "V20"]


def gen_schueler_wuensche():
    with open(dataHandler.studentDataCSVPath, 'w') as file:
        filewriter = csv.writer(file, delimiter=dataHandler.csv_delimiter)
        for i in range(30 * 5):
            student = []
            student.append(f"{random.choice(first_names)} {random.choice(first_names)}".capitalize())
            student.append(random.choice(classes))
            for a in range(5):
                student.append(random.choice(wishes))
            filewriter.writerow(student)
    pass


def gen_presentation():
    with open(dataHandler.presentationDataCSVPath, 'w') as file:
        filewriter = csv.writer(file, delimiter=dataHandler.csv_delimiter)
        for i in range(1, 20 + 1):
            presentation = []
            presentation.append(f"V{i}")
            presentation.append(random.randint(1, 20))
            hi = random.randint(1, 3)
            if hi == 1:
                presentation.append(135)
            elif hi == 2:
                presentation.append(35)
            elif hi == 3:
                presentation.append(3)
            filewriter.writerow(presentation)
    pass


if __name__ == '__main__':
    if os.getcwd()[-3:] == "src":
        os.chdir(os.getcwd()[:-4])
    gen_schueler_wuensche()
    gen_presentation()
