import io


def test_write():
    # seems like this is similar to StringBuilder in .NET
    out = io.StringIO()
    out.write('Test string')
    data = out.getvalue()

    # good for unit testing file output
    assert data == 'Test string'


def test_open():
    # by default opens only readable
    # same as mode='r'
    # this mode will throw error if not round
    try:
        file1 = open('testfile1.txt')
    except FileNotFoundError:
        pass

    # a file object has api to interact with it,
    # for reading and writing

    # 'r+' instead of 'rw' to emulate how C does it
    file2 = open('testfile2.txt', 'r+')
    file2.write('hello world')
    # seek moves the file cursor to a particular byte
    # you want to start reading at
    file2.seek(0)
    contents = file2.read()
    assert contents == 'hello world'
    file2.close()

    # you can also use the 'b' flag to read/write in binary
