# Berufsfindungstag © 2024 by KKS-Mint-AG is licensed under CC BY-NC-SA 4.0
"""
A simple program to organize a career orientation day for students.
"""
import logging
import src.dataHandler as dataHandler

__authors__ = [r"Jan *****", r"David *****"]
__github__ = r"https://github.com/KKS-MintAG/Berufsfindungstag"
__website__ = r"https://www.kks-hannover.de/erleben/ganztagsangebot/arbeitsgemeinschaften/3d-ag/"
__status__ = r"production"
__version__ = r"0.0.1"
__date__ = r"2024-04-25"

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


class Berufsfindungstag:

    def phase_one(self) -> None:
        print(dataHandler.studentData)

    def __init__(self):
        dataHandler.loadStudentData()
        self.phase_one()
        pass


if __name__ == '__main__':
    logging.info("Starting Program...")
    Berufsfindungstag()
    logging.info("Program finished")
