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
    for i in range(0, 2):
        driver.info(f"开始验证{i}=={dr}")
        if pytest.assume(i == dr):
            driver.info("验证完成")
        else:
            driver.error(f"验证错误")
    driver.info("\n")
