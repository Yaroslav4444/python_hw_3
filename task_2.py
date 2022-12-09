"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.
"""


def data_collection(user_name, surname, year_of_birth, email, phone_number):
    """collecting data from the user"""
    return print(f"Имя: {user_name}, Фамилия: {surname}, Год рождения: "
                 f"{year_of_birth}, Email: {email}, Телефон: {phone_number}")


data_collection(
    user_name=input("Имя: "),
    surname=input("Фамилия: "),
    year_of_birth=input("Год рождения: "),
    email=input("Email: "),
    phone_number=input("Телефон: "))
