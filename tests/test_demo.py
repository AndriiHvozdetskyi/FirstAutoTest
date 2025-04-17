import pytest

@pytest.fixture()
def only_text():
    print("Py py py")
    yield
    print("\nPy py py py 2")



def test_demo1():
    assert 1 == 1

def test_demo2(only_text):
    assert 1 == 1