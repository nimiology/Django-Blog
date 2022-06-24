import os
import random
import string

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView


def slug_genrator():
    letters_str = string.ascii_letters + string.digits
    letters = list(letters_str)
    return "".join(random.choice(letters) for _ in range(50))


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_article_picture(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"articles/{instance.id}{ext}"
    return f"{final_name}"


class CreateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView, CreateAPIView):
    def get_queryset(self):
        if not (self.request.user and self.request.user.is_superuser):
            return self.queryset.filter(published=True)
        return self.queryset


class MyListAPIView(ListAPIView):
    def get_queryset(self):
        if not (self.request.user and self.request.user.is_superuser):
            return self.queryset.filter(published=True)
        return self.queryset
