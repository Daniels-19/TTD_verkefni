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
