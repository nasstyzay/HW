import requests
from bs4 import BeautifulSoup
import json

search_keywords = "Python"
locations = {"Москва": "1", "Санкт-Петербург": "2"}
base_url = "https://hh.ru/search/vacancy"


params = {
    "text": search_keywords,
    "area": list(locations.values()),
    "page": 0,
    "per_page": 50
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(base_url, params=params, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    vacancies_list = []

    for vacancy in soup.find_all("div", {"class": "vacancy-serp-item"}):
        vacancy_data = {}

        title_element = vacancy.find("a", {"data-qa": "vacancy-serp__vacancy-title"})
        if not title_element:
            continue
        vacancy_data["link"] = title_element.get("href")

        salary_element = vacancy.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"})
        vacancy_data["salary"] = salary_element.text if salary_element else "Не указано"

        company_element = vacancy.find("a", {"data-qa": "vacancy-serp__vacancy-employer"})
        vacancy_data["company"] = company_element.text.strip() if company_element else "Не указано"

        location_element = vacancy.find("span", {"data-qa": "vacancy-serp__vacancy-address"})
        vacancy_data["city"] = location_element.text.strip() if location_element else "Не указано"


        vacancy_description = str(vacancy.find("div", {"class": "g-user-content"})).lower()
        if "python" in vacancy_description or "flask" in vacancy_description:
            vacancies_list.append(vacancy_data)


    with open("vacancies.json", "w", encoding="utf-8") as file:
        json.dump(vacancies_list, file, ensure_ascii=False, indent=4)

    print(f"Найдено {len(vacancies_list)} вакансий по вашему запросу.")
else:
    print("Ошибка получения данных с HH.ru")

