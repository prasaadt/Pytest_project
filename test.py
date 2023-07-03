import pytest
from django.urls import reverse
from customer.models import Item

@pytest.mark.django_db
def test_item_list(client):
    url = reverse('item_list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_item_detail(client):
    item = Item.objects.create(name='Test Item', description='Test description', price=9.99)
    url = reverse('item_detail', args=[item.pk])
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_item_create(client):
    url = reverse('item_create')
    data = {
        'name': 'New Item',
        'description': 'New description',
        'price': 19.99
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Item.objects.filter(name='New Item').exists()

@pytest.mark.django_db
def test_item_update(client):
    item = Item.objects.create(name='Test Item', description='Test description', price=9.99)
    url = reverse('item_update', args=[item.pk])
    data = {
        'name': 'Updated Item',
        'description': 'Updated description',
        'price': 29.99
    }
    response = client.post(url, data)
    assert response.status_code == 302
    updated_item = Item.objects.get(pk=item.pk)
    assert updated_item.name == 'Updated Item'

@pytest.mark.django_db
def test_item_delete(client):
    item = Item.objects.create(name='Test Item', description='Test description', price=9.99)
    url = reverse('item_delete', args=[item.pk])
    response = client.post(url)
    assert response.status_code == 302
    assert not Item.objects.filter(pk=item.pk).exists()
