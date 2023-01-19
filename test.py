# coding=utf-8
import pytest

from Commom.Logger import MemoryLog


@pytest.fixture
def driver():
    m = MemoryLog()
    yield m
    m.preservation()


@pytest.mark.parametrize("dr", [1, 2, 3, 4])
def test(driver, dr):
    driver.add("开始验证")
    driver.add("验证完成")
    assert 1 == dr
