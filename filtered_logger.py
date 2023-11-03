#!/usr/bin/env python3
import re
from typing import List
'''
Module for handling data
'''


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Return a log messages obfuscated"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
