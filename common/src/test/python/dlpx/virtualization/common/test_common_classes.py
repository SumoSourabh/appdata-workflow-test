#
# Copyright (c) 2019, 2021 by Delphix. All rights reserved.
#

import pytest
from dlpx.virtualization.common._common_classes import ArithmeticOperations
from dlpx.virtualization.common.exceptions import ArithmeticException


@pytest.fixture
def first():
    return 5


@pytest.fixture
def second():
    return 6


class TestArithmeticOperations:
    @staticmethod
    def test_init_arithmetic_operation_success(first, second):
        ArithmeticOperations(first, second)

    @staticmethod
    def test_init_arithmetic_operation_null_first(second):
        with pytest.raises(ArithmeticException) as err_info:
            ArithmeticOperations('', second)
        assert err_info.value.message == "First variable can not be null or zero."

    @staticmethod
    def test_init_arithmetic_operation_null_second(first):
        with pytest.raises(ArithmeticException) as err_info:
            ArithmeticOperations(first, '')
        assert err_info.value.message == "Second variable can not be null or zero."

    @staticmethod
    def test_add_arithmetic_operation_success(first, second):
        ao = ArithmeticOperations(first, second)
        value = ao.add()
        assert value == 11

    @staticmethod
    def test_subtract_arithmetic_operation_success(first, second):
        ao = ArithmeticOperations(first, second)
        value = ao.subtract()
        assert value == -1
        ao = ArithmeticOperations(ao.add(), second)
        value = ao.subtract()
        assert value == 5

    @staticmethod
    def test_multiply_arithmetic_operation_success(first, second):
        ao = ArithmeticOperations(first, second)
        value = ao.multiply()
        assert value == 30

    @staticmethod
    def test_divide_arithmetic_operation_success(first, second):
        ao = ArithmeticOperations(second, first)
        value = ao.divide()
        assert value == 1

    @staticmethod
    def test_divide_arithmetic_operation_failure(second):
        with pytest.raises(ArithmeticException) as err_info:
            ArithmeticOperations(second, 0)
        assert err_info.value.message == "Second variable can not be null or zero."
