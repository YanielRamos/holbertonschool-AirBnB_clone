#!/bin/usr/python3
"""create a unique filestorage instance for  application"""

from models.engine.file_storege import FileStorage
storage = FileStorage()
storage.reload()
