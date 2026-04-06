"""
Program: test_rotation_utils.py
Author: Sadikshya
Date: 04/06/2026
"""

import pytest 
from rotation_utils import adjust_rotation

#Normal rotation test
def test_adjust_rotation_100():
    """Check that 100 stays 100"""
    assert adjust_rotation(100) == 100

def test_adjust_rotation_460():
    """Check 460 wraps to 100"""
    assert adjust_rotation(460) == 100

def test_adjust_rotation_820():
    """Check 820 wraps to 100"""
    assert adjust_rotation(820) == 100

def test_adjust_rotation_negative_100():
    """Check -100 wraps to 260"""
    assert adjust_rotation(-100) == 260

def test_adjust_rotation_negative_460():
    """Check -460 wraps to 260"""
    assert adjust_rotation(-460) == 260

def test_adjust_rotation_negative_820():
    """Check -820 wraps to 260"""
    assert adjust_rotation(-820) == 260

#Non numeric input test
def test_adjust_rotation_type_error():
    """Passing a string should raise TypeError"""
    with pytest.raises(TypeError):
        adjust_rotation("abc")

#AI Diclosure:
#I used Chatgpt to help explain the concepts related to pytest and unit testing.