'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtract function works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiply function works '''    
    assert multiply(2,2) == 4

def test_divison():
    '''Test that divison function works '''    
    assert divide(2,2) == 1
