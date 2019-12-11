import os
import shutil
from datetime import datetime


def document_path(instance, filename):
    return f'users/{instance.user_id}/{filename}'


# def task_delete_path(document):
#     file_path = document.path
#     if os.path.isfile(file_path):
#         os.remove(file_path)


def delete_path(document):
    datetime_path = os.path.abspath(os.path.join(document.path, '..'))
    shutil.rmtree(datetime_path)
