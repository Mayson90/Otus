## PythonBase 2021-02 Project Work

> Andrey M
___
**Project name:**

&nbsp;&nbsp;<span style="color:#208782">Online store of IT equipment on Django</span>

**Project description:**

&nbsp;&nbsp;The website displays products. Users can add and remove products to/from their cart while also specifying
the quantity of each item. They can then enter their address and choose Stripe to handle the payment processing.

- admin panel with handling categories, vendors, products, orders, addresses, payments and users
- login/logout/register user page
- products with sorting by category and by vendor
- user cart with displaying products quantity in there
- checkout form with editing quantity of products and show total order
- payment form with address and Stripe online payment processing

&nbsp;&nbsp;Project released in Docker and contains from 2 containers:

- web app
- postgres db

**Features:**

- management scripts to fill db (project ready for demo)
- GitHub CI with django tests and exporting test coverage to CodCov (if tests are successful - it sends message to Telegram Bot)

**Run project:**

    $ docker compose up -d --build

&nbsp;&nbsp;go to your localhost http://0.0.0.0:8000/
___
**Ideas & improvements:**

- deploy to Heroku
- user profile
- product coupons and refunds
- advertising banners
- ecommerce tracking and analytics
