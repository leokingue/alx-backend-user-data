#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, Response
from json import dumps
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      - Raise 401 Code Status
    """
    unauthorized_message = dumps({"error": "Unauthorized"})
    abort(Response(unauthorized_message, 401))


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden
    Return:
      - Raise 403 Code Status
    """
    forbidden_message = dumps({"error": "Forbidden"})
    abort(Response(forbidden_message, 403))
