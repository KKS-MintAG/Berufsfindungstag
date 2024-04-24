#   Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0

#   Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
import csv, random, dataHandler

vornamen = ['anton', 'bert', 'carl', 'dora', 'emil', 'frieda', 'gerda', 'hans', 'ilse', 'joachim', 'klaus',
            'leo', 'manfred', 'nina', 'otto', 'paul', 'richard', 'susi', 'theo', 'uwe', 'verena',
            'wilfried']
klassen = ["9a", "9b", "9c", "9d", "9e", "9f"]

wishes = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14"]

def gen_schueler_wuensche():
    with open(dataHandler.studentDataCSVPath, 'w') as file:
        filewriter = csv.writer(file, delimiter=dataHandler.csv_delimiter)
        for i in range(50):
            student = []
            student.append(random.choice(vornamen))
            student.append(random.choice(klassen))
            for a in range(5):
                student.append(random.choice(wishes))
            filewriter.writerow(student)
    pass


if __name__ == '__main__':
    gen_schueler_wuensche()