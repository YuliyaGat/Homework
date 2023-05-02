import pytest

def test(file_obj):
    text = file_obj.read()
    text = text.upper()
    return (text)

def test_test():
    with open('text.txt', 'r') as f:
        text_f = test(f)
    assert text_f == 'HELLO!\nIT IS A WONDERFUL DAY!'

@pytest.fixture
def file_obj():
    with open('text.txt', 'r') as f:
        yield f

def test_test_with_fixture(file_obj):
    text_f = test(file_obj)
    assert text_f == 'HELLO!\nIT IS A WONDERFUL DAY!'



