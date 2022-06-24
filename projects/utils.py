from blog.utils import get_filename_ext


def upload_project_picture(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"projects/{instance.id}{ext}"
    return f"{final_name}"
