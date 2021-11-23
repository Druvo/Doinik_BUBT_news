"""Core > views > __init__.py"""
from .home import HomePageView
from .login import Login, LogoutView
from .registration import Registration


__all__ = [
    HomePageView,
    Login,
    LogoutView,
    Registration
]
