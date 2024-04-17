def check_age(age: int) -> str:
    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'
    return result

import pytest

@pytest.mark.parametrize("age, expected_result", [
    (17, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (19, 'Доступ разрешён'),
    (0, 'Доступ запрещён'),
    (-10, 'Доступ запрещён'),
])
def test_check_age(age, expected_result):
    assert check_age(age) == expected_result


    
def get_cost(weight: int) -> str:
   if weight <= 10:
       result = "Стоимость доставки: 200 руб."
   else:
       result = "Стоимость доставки: 500 руб."
   return result

import pytest

@pytest.mark.parametrize("weight, expected_output", [
    (10, "Стоимость доставки: 200 руб."),
    (9, "Стоимость доставки: 200 руб."),
    (11, "Стоимость доставки: 500 руб."),
    (0, "Стоимость доставки: 200 руб."),
    (-1, "Стоимость доставки: 200 руб."),
    (100, "Стоимость доставки: 500 руб.")
])
def test_get_cost(weight, expected_output):
    assert get_cost(weight) == expected_output



def check_triangle(side1: int, side2: int, side3: int) -> str:
    if side1 <= 0 or side2 <= 0 or side3 <= 0 or (side1 + side2) <= side3 or (side2 + side3) <= side1 or (side1 + side3) <= side2:
        return "Треугольник не существует"
    elif side1 == side2 == side3:
        return "Равносторонний треугольник"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

import pytest

@pytest.mark.parametrize("sides, expected_result", [
    ((1, 1, 1), "Равносторонний треугольник"),
    ((2, 2, 3), "Равнобедренный треугольник"),
    ((3, 4, 5), "Разносторонний треугольник"),
    ((10, 1, 1), "Треугольник не существует"),
    ((0, 2, 2), "Треугольник не существует"),
    ((-1, -1, -1), "Треугольник не существует")
])
def test_check_triangle(sides, expected_result):
    side1, side2, side3 = sides
    assert check_triangle(side1, side2, side3) == expected_result




import requests
import pytest

# Необходимо заменить 'your_oauth_token' на ваш действительный OAuth токен.
TOKEN = 'https://oauth.yandex.ru/authorize?response_type=code&client_id=<YOUR_CLIENT_ID>&redirect_uri=<YOUR_REDIRECT_URI>&scope=disk:write'
HEADERS = {'Authorization': f'OAuth {TOKEN}'}
API_BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

def create_folder(path):
    response = requests.put(f"{API_BASE_URL}?path={path}", headers=HEADERS)
    return response

def check_folder_exists(path):
    response = requests.get(f"{API_BASE_URL}?path={path}", headers=HEADERS)
    return response.status_code == 200

@pytest.mark.parametrize("folder_name", [
    ("TestFolder"),
])
def test_create_folder(folder_name):
    response = create_folder(folder_name)
    assert response.status_code == 201  # для успешного создания папки статус должен быть 201

    assert check_folder_exists(folder_name)

@pytest.mark.parametrize("folder_name", [
    ("/invalid/path/with/<<<"),
    (""),
])
def test_create_folder_negative(folder_name):

    response = create_folder(folder_name)
    assert response.status_code == 400 

if __name__ == "__main__":
    pytest.main()