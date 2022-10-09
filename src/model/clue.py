import re


class Clue:
    def __init__(self, reeks):
        woordlengte = int(len(''.join(reeks))/(2*len(reeks)))
        self._woordlengte = woordlengte
        self._reeks = reeks
        self._woordenboek = "../resource/nl_woorden.txt"
        self._woordenlijst = []
        self._forbidden_letters = ""
        self._woord_match = ""
        self._woord_match_reeks = []
        self._required_letters = {}

    def woorden_van_juiste_lengte(self):
        woordenlijst = set()
        with open(self._woordenboek) as f:
            line = f.readline().strip()
            while line:
                woord = line.split('/')[0]
                if len(woord) == self._woordlengte:
                    if woord.isalpha():
                        if woord[0].islower():
                            woordenlijst.add(woord.lower())
                line = f.readline().strip()
        self._woordenlijst = sorted(list(woordenlijst))

    @property
    def woordlengte(self):
        return self._woordlengte

    @property
    def woordenlijst(self):
        return self._woordenlijst

    @property
    def forbidden_letters(self):
        if not self._forbidden_letters:
            self._forbidden_letters = self._get_forbidden_letters()
        return self._forbidden_letters

    @property
    def required_letters(self):
        if not self._required_letters:
            self._required_letters = self._get_present_anywhere()
        return self._required_letters

    @property
    def woord_match(self):
        if not self._woord_match:
            self._woord_match = self._get_present_right_spot()
        return self._woord_match

    def has_forbidden_letters(self, woord):
        for letter in woord:
            if letter in self.forbidden_letters:
                return True
        return False

    def woord_match_reeks(self):
        if not self._woord_match_reeks:
            self._woord_match_reeks = self._get_present_wrong_spot()
        return self._woord_match_reeks

    def fit_woord(self, woord):
        if re.match(self.woord_match, woord):
            return True
        else:
            return False

    def fit_reeks_woord(self, woord):
        for clue in self.woord_match_reeks():
            if not re.match(clue, woord):
                return False
        return True

    def has_required_letters(self, woord):
        for letter in self.required_letters.keys():
            if times_letter_in_word(letter, woord) < self.required_letters[letter]:
                return False
        return True

    def _get_forbidden_letters(self):
        forbidden = set()
        sustained = set()
        for woord in self._reeks:
            for (letter, status) in (woord[i:i + 2] for i in range(0, len(woord), 2)):
                if status == '0':
                    forbidden.add(letter)
                else:
                    sustained.add(letter)
        for letter in sustained:
            if letter in forbidden:
                forbidden.remove(letter)

        return ''.join(list(forbidden))

    def _get_present_right_spot(self):
        present_right = self._init_regular_expression_woord()
        for woord in self._reeks:
            index=0
            for (letter, status) in (woord[i:i + 2] for i in range(0, len(woord), 2)):
                if status == '2':
                    if present_right[index] != '.' and present_right[index] != letter:
                        raise Exception("fout in reeks")
                    present_right[index] = letter
                index += 1
        return ''.join(present_right)

    def _get_present_wrong_spot(self):
        present_reeks = []
        for woord in self._reeks:
            present = self._init_regular_expression_woord()
            index = 0
            for (letter, status) in (woord[i:i + 2] for i in range(0, len(woord), 2)):
                if status == '1':
                    if present[index] != '.' and present[index] != "[^" + letter + "]":
                        raise Exception("fout in reeks")
                    present[index] = "[^" + letter + "]"
                index += 1
            present_reeks.append(''.join(present))
        return present_reeks

    def _get_present_anywhere(self):
        present = {}
        for woord in self._reeks:
            present_per_woord = {}
            for (letter, status) in (woord[i:i + 2] for i in range(0, len(woord), 2)):
                if status in ['1', '2']:
                    if letter in present_per_woord:
                        present_per_woord[letter] += 1
                    else:
                        present_per_woord[letter] = 1
            for letter in present_per_woord.keys():
                if letter in present:
                    if present[letter] <= present_per_woord[letter]:
                        present[letter] = present_per_woord[letter]
                else:
                    present[letter] = present_per_woord[letter]
        return present

    def _init_regular_expression_woord(self):
        woord = []
        for letter in range(0, self._woordlengte):
            woord.append('.')
        return woord


def times_letter_in_word(letter, woord):
    return woord.count(letter)