from http import HTTPStatus

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


def test_salary_list(admin_client):
    url = reverse("api:salary-list")
    assert url == "/api/salary/"
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_yet_another_view(admin_client):
    url = reverse("api:salarydetailitem-list")
    assert url == "/api/salarydetailitem/"
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK