#!/usr/bin/env python3
"""
Authentication Module for the API
"""
from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """
    Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method of require_auth
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        path = path.rstrip("/")
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip("/")
            if path == excluded_path:
                return False
        return True

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
