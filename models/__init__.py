#!/bin/usr/python3
"""
Creates a unique FileStorage instance for  application
"""

from models.engine.file_storege import FileStorage
storage = FileStorage()
storage.reload()
