class STUDENT:
    name: str = ""
    course: str = ""
    wishes: list = []

    def __init__(self, name: str, course: str, wishes: list):
        """

        :param name: Name des Schülers
        :param course: Klasse des Schülers
        :param wishes: Wünsche (Instant of)
        """
        self.name = name
        self.course = course
        self.wishes = wishes

