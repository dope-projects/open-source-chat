import logging
import os
from dataclasses import dataclass

from .log import setup_log

setup_log()

from logging import *

import pytest

alog = getLogger("app")


@dataclass(slots=True)
class Testcase:
    level: int  # Union[INFO, DEBUG, WARN, ERROR, CRITICAL]
    content: str


test_cases = [
    Testcase(DEBUG, "Hiro-debug"),
    Testcase(INFO, "Hiro-info"),
    Testcase(WARN, "Hiro-warn"),
    Testcase(ERROR, "Hiro-error"),
    Testcase(CRITICAL, "Hiro-critical"),
]

level_map_files = {
    10: "debug",
    20: "info",
    30: "warn",
    40: "error",
    50: "critical"
}


@pytest.mark.run(order=1)
def test_log():
    info_str = "TestLog"

    logging.info(info_str)

    with open('logs/root.log') as f1:
        lines = f1.readlines()
        assert len(lines) > 0
        last_line = lines[-1].strip()
        assert info_str in last_line

# @pytest.mark.run(order=2)
# @pytest.mark.parametrize("testcase", test_cases)
# def test_logs(testcase: Testcase):
#     level = testcase.level
#     cnt = testcase.content
#     log(level, cnt)
#
#     log_file = level_map_files[level]
#
#     with open(f'logs/{log_file}.log') as f1:
#         lines = f1.readlines()
#         assert len(lines) > 0
#         last_line = lines[-1].strip()
#         assert cnt in last_line
#
#
# @pytest.mark.no_cache
# @pytest.mark.run(order=1)
# @pytest.mark.parametrize("testcase", test_cases)
# def test_app_logs(testcase: Testcase):
#     level = testcase.level
#     cnt = f"app{testcase.content}"
#     ignored_levels = []
#
#     if level in ignored_levels: return
#
#     alog.log(level, cnt)
#
#     if level is INFO:
#         log_file = "app"
#     else:
#         log_file = f"app_{level_map_files[level]}"
#
#     with open(f'logs/{log_file}.log') as f1:
#         lines = f1.readlines()
#         assert len(lines) > 0
#         last_line = lines[-1].strip()
#         assert cnt in last_line
