import sys
# assertions from https://docs.python.org/3/library/functions.html


def test_abs():
    assert abs(-4) == 4


def test_all():
    iterable = [True, True, True]
    assert all(iterable) == True

    iterable.append(False)
    assert all(iterable) == False


def test_any():
    iterable = [True, False]
    assert any(iterable) == True


def test_bin():
    # '0b' prefix denotes binary representation, not base10
    assert bin(2) == '0b10'


def test_bool():
    assert bool(0) == False
    assert bool(1) == True


def test_bytearray():
    # passing int will create array with default values
    b1 = bytearray(4)
    assert any(b1) == False
    assert b1[2] == 0

    # passing in str and encoding
    b2 = bytearray('a', 'ascii')
    # see http://www.asciitable.com/
    # in ascii, a can be represented as 97 decimal
    assert b2[0] == 97

    # bytearray is mutable
    b2[0] = 98
    assert b2[0] == 98


def test_bytes():
    # similar to bytearray() but immutable
    b1 = bytes(3)
    try:
        b1[0] = 1
    except TypeError:
        # throws a TypeError if you try to assign to elements
        assert True
    else:
        assert False


def test_callable():
    class CallIt:

        def __call__(self):
            return True
    obj = CallIt()

    # callable returns true if obj has __call__ method defined
    assert callable(obj) == True


def test_chr():
    # returns corresponding unicode char for a given int
    assert chr(97) == 'a'


def test_complex():
    # creates a complex number
    # with a real and imaginary component
    num = complex(1, 2)
    assert repr(num) == '(1+2j)'


def test_delattr():
    class SomeClass:

        @property
        def foobar(self):
            self._foobar

        @foobar.setter
        def foobar(self, value):
            self._foobar = value

    x = SomeClass()
    # like javascript, object properties can be treated like strings
    setattr(x, 'property', 123)
    assert x.property == 123

    delattr(x, 'property')
    try:
        print(x.property)
    except AttributeError:
        assert True
    else:
        assert False


def test_dict():
    # 3 constructors
    # first accepts 'kwargs' (keyword arguments)
    d1 = dict(fname='Daniel', lname='Lillja')
    assert d1['fname'] == 'Daniel'


def test_divmod():
    # returns a tuple with division result and remainder
    result = divmod(19, 6)
    assert result[0] == 3
    assert result[1] == 1


def test_enumerate():
    # creates an enumerable
    # which is a list of tuples of (index, value)
    test_list = ['t1', 't2']
    test_enum = list(enumerate(test_list))
    # outputs a list (0, 't1') and (1, 't2')
    # useful if you need the index but want to use convinient loop
    assert test_enum[0][0] == 0
    assert test_enum[0][1] == 't1'


def test_eval():
    x = 1
    x += 1
    # uses assignments about to evaluate string to answer
    # using lexical scope surrounding it
    assert eval('x+1') == 3


def test_filter():
    # filter takes in a lambda function and a list of items to check
    # will return elements in list that when run though
    # the function return true

    # 0 to 9
    test_list = range(0, 10)
    # only take values greater than 7
    filtered = filter(lambda e: e > 7, test_list)
    # convert to list for testing
    filtered = list(filtered)
    assert filtered[0] == 8


def test_float():
    # creates a float object

    # can be used with strings
    x = float(1.23)
    assert x == 1.23

    # infinity is defined
    x = float('Infinity')

    # scientific notation is allowed
    x = float('1E3')
    assert x == 1000


def test_format():
    # used to format strings
    x = '{0}, {1}, {2}'.format(1, 2, 3)
    assert x == '1, 2, 3'

    # able to take in kwargs
    x = '({lat},{lon})'.format(lat=1.234, lon=2.345)
    assert x == '(1.234,2.345)'

    # formating as percent
    percent = 0.203
    x = '{0:.2%}'.format(percent)
    assert x == '20.30%'

    # there is a lot more to this but moving on for now...


def test_frozenset():
    # main difference from set is that frozen set is immutable
    # giving it slightly better performance

    # constructor takes in a iterable
    iterable = [1, 2, 3, 1]
    fs = frozenset(iterable)

    # sets cannot have duplicate elements
    assert len(fs) == 3


def test_hash():
    class Hashable:

        def __hash__(self):
            return 1

    # hashable objects implement __hash__(self)
    # hash functions are supposted to return ints
    # you want to mimize collisions
    h1 = Hashable()
    assert hash(h1) == 1


def test_hex():
    # convert an int to hexadecimal
    h = hex(16)
    assert str(h) == '0x10'

    class IdTesting:

        def __init__(self):
            pass


class IdTesting:

    def __init__(self):
        pass


def test_id():
    i0 = IdTesting()
    i1 = IdTesting()

    # id returns a unique runtime id for each instaniated object
    assert id(i0) != id(i1)
    assert id(i0) == id(i0)


def test_isinstance():
    # isinstance is one way to compare types
    # a isinstance(subclass, parent) will return true
    # but there also is a issubclass method that only checks inheritance
    string = str('hello world')
    assert isinstance(string, str)


class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        # move first
        self.index = self.index - 1
        # then return
        return self.data[self.index]


def test_version():
    assert sys.version_info[0] == 3


def test_iter():
    # iter very basically enables nice looking for-loops like:
    for c in 'python':
        pass

    # iter transforms iterable (like a list) -> iterator
    # iterator defines next()

    x = iter([1, 2, 3])
    # convert to list for testing
    # this constructor for list seems pretty important...
    x = list(x)
    assert x[0] == 1

    # so next just moves to the next element and returns it
    # is essenence iterator just the movement strategy
    # in lists it is pretty simple but get more complicated for custom
    # data structures

    rev = Reverse('test')
    x = list(iter(rev))
    # convert back to string
    x = ''.join(x)
    assert x == 'tset'


def test_locals():
    # locals outputs a dictionary of key-value pairs
    # with key:variable name, value:variable value
    x = 3
    lcs = locals()
    assert lcs['x'] == 3
    assert lcs['x'] == x


def test_map():
    the_input = [1, 4, 9]
    the_output = list(map(lambda x: x * 2, the_input))

    # above map call is calling lambda for each element
    # and outputs the transformed results
    assert the_output[0] == 2
    assert the_output[1] == 8


def test_max_min():
    the_input = [1, 4, 9]
    assert max(the_input) == 9
    assert min(the_input) == 1


def test_next():
    # next essentially is a nice wrapper
    # for calling an iter's __next__()
    # so you don't have to include underscores?
    rev = Reverse('rev')
    assert next(rev) == 'v'


def test_object():
    # object is the default
    # base class for all other objects
    tobj = object()
    assert tobj is not None
