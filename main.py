# Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
"""
A simple program to organize a career orientation day for students.
"""
import logging
from typing import List

import src.dataHandler as dataHandler
import random

__projekt_path_name__: str = r"Berufsfindungstag"
__authors__: list[str] = [r"Jan *****", r"David *****"]
__github__: str = r"https://github.com/KKS-MintAG/Berufsfindungstag"
__website__: str = r"https://www.kks-hannover.de/erleben/ganztagsangebot/arbeitsgemeinschaften/3d-ag/"
__status__: str = r"production"
__version__: str = r"0.0.1"
__date__: str = r"2024-04-25"

print("-" * 89)
print("Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0")
print(f"Berufsfindungstag {__version__} ({__date__}) (status: {__status__})")
print(f"Running on Python {__import__('sys').version}")
print(f"Authors: {', '.join(__authors__)}")
print(f"For more information, visit {__github__} or {__website__}")
print(f"See ACKNOWLEDGEMENTS.md")
print("-" * 89)

# ---------------------------------------------------------------------------
#   For logging purposes
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')


def first_phase():
    """
    First phase of the program
    """
    local_student_data = dataHandler.studentData
    local_presentation_data = dataHandler.presentationData
    while len(local_student_data) > 0:
        student_random_index = random.randint(0, len(local_student_data) - 1)
        student = local_student_data[student_random_index]
        print(student)
        local_student_data.pop(student)
        print(local_student_data[student_random_index])
    pass


def init() -> None:
    """
    Initializes the program
    """
    dataHandler.loadStudentData()
    dataHandler.loadPresentationData()
    pass


def main() -> None:
    logging.error("Todo: test and  classes")
    init()
    first_phase()
    pass


if __name__ == '__main__':
    logging.info("Starting Program...")
    main()
    logging.info("Program finished")
