"""
Скрипт для импорта данных из db_export.json в БД.
"""
import os
import sys
import django
import json

# Настройка Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_with_restrictions.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from advertisements.models import Advertisement, AdvertisementStatusChoices


def import_data():
    """Импорт данных из JSON файла."""
    
    json_file = os.path.join(os.path.dirname(__file__), 'db_export.json')
    
    if not os.path.exists(json_file):
        print(f"Ошибка: файл {json_file} не найден")
        return
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Создаем пользователей
    user_mapping = {}
    for user_data in data['users']:
        username = user_data['username']
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'first_name': user_data.get('first_name', ''),
                'last_name': user_data.get('last_name', ''),
            }
        )
        user_mapping[user_data['id']] = user
        status = "создан" if created else "найден"
        print(f"Пользователь {username}: {status}")
    
    # Создаем объявления
    for ad_data in data['advertisements']:
        creator = user_mapping.get(ad_data['creator_id'])
        if not creator:
            print(f"Ошибка: не найден создатель для объявления {ad_data['title']}")
            continue
        
        # Парсим дату
        created_at = datetime.fromisoformat(ad_data['created_at'].replace('Z', '+00:00'))
        
        advertisement, created = Advertisement.objects.get_or_create(
            title=ad_data['title'],
            creator=creator,
            defaults={
                'description': ad_data.get('description', ''),
                'status': ad_data.get('status', 'OPEN'),
            }
        )
        
        # Обновляем дату создания
        Advertisement.objects.filter(pk=advertisement.pk).update(created_at=created_at)
        
        status = "создано" if created else "найдено"
        print(f"Объявление '{advertisement.title}': {status}")
    
    print(f"\nИмпорт завершен!")
    print(f"Всего пользователей: {len(data['users'])}")
    print(f"Всего объявлений: {len(data['advertisements'])}")


if __name__ == '__main__':
    import_data()
