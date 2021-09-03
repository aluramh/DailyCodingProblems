def getCanonicalForm(str):
    return "".join(sorted(str))


def findRotatedString(originalString, rotatedString):
    """
    If 2nd string is 1st string rotated, return the index from the original where the rotation starts.
    Otherwise return None.
    """
    # Input may be null, so we need to escape it
    if originalString is None or rotatedString is None:
        return None

    # Input may not be a rotated version of itself, so we need to see if they are canonical
    if getCanonicalForm(originalString) != getCanonicalForm(rotatedString):
        return None

    # Main logic to find rotation
    i = 0
    j = 0
    rotation_index = None

    # O(n)
    while i < len(originalString):
        if originalString[i] == rotatedString[j]:
            if rotation_index is None:
                rotation_index = i
            j += 1
        else:
            rotation_index = None

        i += 1

    return rotation_index


try:
    r = findRotatedString("interview", "viewinter")
    assert (r == 5)

    r = findRotatedString("interview", "erviewint")
    assert (r == 3)
    print("Sucess!")
except AssertionError as e:
    print("Error")
