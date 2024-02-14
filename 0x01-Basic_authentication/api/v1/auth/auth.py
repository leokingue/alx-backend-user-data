#!/usr/bin/env python3
"""
Authentication Module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method of require_auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method of authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method of current_user
        """
        return None
