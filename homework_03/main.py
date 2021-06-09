"""
Домашнее задание №3
Асинхронная работа с сетью и бд
доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy import select, func, join
from sqlalchemy.orm import selectinload

from homework_03.models import engine, Base, User, Session, Post
from sqlalchemy.ext.asyncio import AsyncSession
from homework_03.jsonplaceholder_requests import fetch_json


async def new_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def sync_db(rows: list):
    async with Session() as session:
        session: AsyncSession

        async with session.begin():
            session.add_all(rows)


def json_user_model(user: dict) -> User:
    u = User(id=user['id'],
             name=user['name'],
             username=user['username'],
             email=user['email'])
    return u


def json_post_model(post: dict) -> Post:
    p = Post(title=post['title'],
             body=post['body'],
             user_id=post['userId'])
    return p


async def fetch_users_posts():
    async with Session() as session:
        session: AsyncSession

        statement = select(User).options(selectinload(User.posts))

        result = await session.execute(statement)
        print(f"users: {result}")

        for user in result.scalars():
            print(user)
            print(user.posts)


async def fetch_users_posts_count():
    async with Session() as session:
        session: AsyncSession

        user_posts_count = func.count(Post.user_id).label("total_posts")
        j = join(User, Post, User.id == Post.user_id)
        stmt = select(User.username, User.email, user_posts_count) \
            .select_from(j) \
            .group_by(User.username, User.email) \
            .order_by(User.username)

        result = await session.execute(stmt)
        for user in result:
            print(user)


async def async_main():
    await new_table()
    raw_users, raw_posts = await fetch_json()
    users = [json_user_model(user) for user in raw_users]
    posts = [json_post_model(post) for post in raw_posts]
    await sync_db(users)
    await sync_db(posts)

    await asyncio.gather(
        fetch_users_posts(),
        fetch_users_posts_count()
    )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
