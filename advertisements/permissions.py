from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    -только создатель может изменять/удалять объявление
    -SAFE_METHODS (GET, HEAD, OPTIONS) - разрешено всем
    -Другие методы (PUT, PATCH, DELETE) - только для создателя объявления
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Для изменения/удаления проверяем, что пользователь - создатель
        return obj.creator == request.user
