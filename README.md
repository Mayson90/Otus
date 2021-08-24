## PythonBase 2021-02 Project Work

> Andrey M
___
**Project name:** 

&nbsp;&nbsp;Интернет магазин ИТ техники на Django

**Project description:**

&nbsp;&nbsp;В проекте реализована ecommerce схема продажи товаров:

- добавление товара через admin'ку приложения
- авторизация пользователя
- добавление пользователем выбранных товаров в корзину
- форма для просмотра/изменения товаров в корзине
- форма оплаты через Stripe API

&nbsp;&nbsp;При этом через admin'ку приложения создаются ордера с товарами в заказе.

&nbsp;&nbsp;Проект упакован в docker, сотоящий из двух контейнеров:

- контейнер с приложением
- контейнер с базой данных на psql

&nbsp;&nbsp;Проект готов для демо - при деплое база данных заполняется элементами

&nbsp;&nbsp;с помощью management скрипта fill_db.py и create_users.py. Также есть 

&nbsp;&nbsp;возможность очищения базы данных через скрипт remove_from_db.py.

**Run project:**

    $ docker compose up -d --build
    
&nbsp;&nbsp;go to your localhost http://0.0.0.0:8000/

