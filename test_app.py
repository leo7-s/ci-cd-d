from app import hello

def test_hello_default():
  assert hello() == "Hello, World"

def test_hello_name():
  assert hello ("Hess") == "Hello, Hess"
