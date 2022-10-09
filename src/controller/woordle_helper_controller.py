from model.clue import Clue


class WHcontroller:
    def __init__(self, reeks):
        self.clue = Clue(reeks)

    def setup(self):
        self.clue.setup_woorden_van_juiste_lengte()

    def mogelijkheden(self):
        if len(self.clue.woordenlijst) == 0:
            self.setup()
        mogelijke_woorden = []
        for woord in self.clue.woordenlijst:
            if self.clue.has_forbidden_letters(woord):
                continue
            if self.clue.fit_reeks_woord(woord):
                if self.clue.fit_woord(woord):
                    if self.clue.has_required_letters(woord):
                        mogelijke_woorden.append(woord)
        return mogelijke_woorden
