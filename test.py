from kata import add

def test():
    # hluti 1
    assert add("") == 0

    # hluti 2
    assert add("1") == 1
    assert add("10") == 10

    # hluti 3
    assert add("1,2") == 3
    assert add("10,20") == 30

    # hluti 4
    assert add("1,2,3,4,5") == 15
    assert add("10,2,5,22,1,1") == 41
    assert add("10,10,10,10,10") == 50

    # hluti 5
    assert add("1\n2,3") == 6
    assert add("1\n2\n3") == 6

    # hluti 6
    assert add("1000, 2, 3, 1001") == 1005
    assert add("200, 1001, 1001, 10000") == 200

    # hluti 7
    assert add("-1\n-2\n3\n-2") == "Negatives not allowed:-1,-2,-2"
    assert add("2\n-3,-2,1") == "Negatives not allowed:-3,-2"
    assert add("1,-1,2,-2,-3\n-3") == "Negatives not allowed:-1,-2,-3,-3"

    # hluti 8
    assert add("//X\n1X2") == 3
    assert add("//&\n1&2&3") == 6