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