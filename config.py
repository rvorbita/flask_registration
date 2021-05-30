import os

class Config(object):
    """Generate a secret key"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-die'

    