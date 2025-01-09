# src/__init__.py
"""
sync-guardian: Reliable directory synchronization with task scheduling.
"""

__version__ = '0.1.0'
__author__ = 'sync-guardian contributors'

from .sync_guardian import DirectorySync

__all__ = ['DirectorySync']
