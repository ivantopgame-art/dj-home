import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from model_bakery import baker
from students.models import Course


@pytest.mark.django_db
def test_course_list():
    """Тест: получение списка всех курсов"""
    client = APIClient()
    baker.make(Course, _quantity=3)

    url = reverse('course-list')  # ← ИСПРАВЛЕНО!
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_course_retrieve():
    """Тест: получение одного курса по id"""
    client = APIClient()
    course = baker.make(Course)

    url = reverse('course-detail', args=[course.id])  # ← ИСПРАВЛЕНО!
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == course.id


@pytest.mark.django_db
def test_course_create():
    """Тест: создание нового курса"""
    client = APIClient()
    url = reverse('course-list')  # ← ИСПРАВЛЕНО!
    data = {'name': 'Test Course'}

    response = client.post(url, data)

    assert response.status_code == 201
    assert Course.objects.count() == 1
    assert Course.objects.first().name == 'Test Course'


@pytest.mark.django_db
def test_course_update():
    """Тест: обновление курса"""
    client = APIClient()
    course = baker.make(Course, name='Old Name')

    url = reverse('course-detail', args=[course.id])  # ← ИСПРАВЛЕНО!
    data = {'name': 'New Name'}

    response = client.put(url, data)

    assert response.status_code == 200
    course.refresh_from_db()
    assert course.name == 'New Name'


@pytest.mark.django_db
def test_course_delete():
    """Тест: удаление курса"""
    client = APIClient()
    course = baker.make(Course)

    url = reverse('course-detail', args=[course.id])  # ← ИСПРАВЛЕНО!
    response = client.delete(url)

    assert response.status_code == 204
    assert Course.objects.count() == 0


@pytest.mark.django_db
def test_course_filter_by_id():
    """Тест: фильтрация курсов по id"""
    client = APIClient()
    course1 = baker.make(Course)
    baker.make(Course)

    url = reverse('course-list')  # ← ИСПРАВЛЕНО!
    response = client.get(url, {'id': course1.id})

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == course1.id
