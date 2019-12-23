from django.shortcuts import render
from core.serializers import CommentSerializer
from rest_framework.response import Response


def comment(request):
    if request.method == 'POST':
        return CommentSerializer.save(user=request.user)