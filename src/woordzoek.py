from model.clue import Clue


def mogelijkheden(clue):
    mogelijke_woorden = []
    for woord in clue.woordenlijst:
        if clue.has_forbidden_letters(woord):
            continue
        if clue.fit_reeks_woord(woord):
            if clue.fit_woord(woord):
                if clue.has_required_letters(woord):
                    mogelijke_woorden.append(woord)
    return mogelijke_woorden


def main(reeks=None):
    clue = Clue(reeks)
    clue.woorden_van_juiste_lengte()
    mogelijke_woorden = mogelijkheden(clue)

    print("verboden letters")
    print(clue.forbidden_letters)
    print("Gevonden: " + str(len(mogelijke_woorden)))
    eerste_letter = ""
    woorden = ""
    for woord in mogelijke_woorden:
        if eerste_letter == woord[0]:
            woorden += " " + woord
        else:
            if len(woorden) != 0:
                print(str(len(woorden)) + ": " + woorden)
            woorden = woord
            eerste_letter = woord[0]
    print(str(len(woorden)) + ": " + woorden)


main(["o0c1e2a0a0n0", "v0l0e2c2h2t2"])
# "t0a1k0e1l0t0", "o0c0e1a2a2n2" => gedaan
# "a0a0n0t0a1l0", "e0r0o1p0a1f0", "m0i0m0o2s0a2"
# "t0a0n0t0e1", "b0e0d0e2l2", "k0o2g0e2l2", "f0o2r0e2l2" => zowel
# "k2a0b0e0l1", "k2o2b0e0l1", "k2o2o1e0n0"
# "k0a2b0e1l0", "m0a2n2e1n0" => tante
# "a0n1g0e1l0", "d0i0n2e1r0", "b0e2n2d0e2", "r0e2n2t1e2" => tenue

