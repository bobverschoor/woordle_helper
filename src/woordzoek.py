from controller.woordle_helper_controller import WHcontroller


def main(reeks=None):
    wh = WHcontroller(reeks)
    mogelijke_woorden = wh.mogelijkheden()

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


main(["b0a1d1e1n0"])
