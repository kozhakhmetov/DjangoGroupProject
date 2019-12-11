import os
import shutil


def document_path(instance, filename):
    profile_id = instance.id
    return f'profile_avatars/{profile_id}/{filename}'

def delete_path(document):
    print(document)
    task_path = os.path.abspath(os.path.join(document.path, '..'))
    shutil.rmtree(task_path)
