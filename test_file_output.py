import io


def test_write():
    # seems like this is similar to StringBuilder in .NET
    out = io.StringIO()
    out.write('Test string')
    data = out.getvalue()

    # good for unit testing file output
    assert data == 'Test string'
