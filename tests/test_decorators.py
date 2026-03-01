import os
import tempfile
import logging


import pytest
from src.decorators import log
import logging


@log()
def successful_function(a, b):
    return a + b


@log()
def function_with_exception(a, b):
    return a / b


def test_successful_function(capsys):
    result = successful_function(6, 4)
    assert result == 10
    captured = capsys.readouterr()

    assert "Starting successful_function with args: (6, 4) kwargs: {}" in captured.out
    assert "successful_function ok: Result: 10" in captured.out


def test_function_with_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        function_with_exception(1, 0)

    captured = capsys.readouterr()

    assert "Starting function_with_exception with args: (1, 0) kwargs: {}" in captured.out
    assert "function_with_exception error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


logging.basicConfig(
    filename='test_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)



