from flask import request, jsonify
from functools import wraps
from app.models import User

def token_required(api_route):
    @wraps(api_route)
    def decorator_function(*args, **kwargs):
        token=request.headers.get('access-token')
        if not token:
            return jsonify({'Access denied' : 'No API token - pleaes register to receive your API token.'}), 401
        if not User.query.filter_by(api_token=token).first():
            return jsonify({'Invalid API token' : 'Please check your API token or request a new one.'})
        return api_route(*args, **kwargs)
    return decorator_function