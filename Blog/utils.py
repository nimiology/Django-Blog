import os
import random
import string


def slug_genrator():
    letters_str = string.ascii_letters + string.digits
    letters = list(letters_str)
    return "".join(random.choice(letters) for _ in range(50))


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_project_picture(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{slug_genrator()}{ext}"
    return f"singleTrack/cover/{final_name}"
