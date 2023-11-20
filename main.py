# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# from dataclasses import dataclass
# from typing import List
# from enum import Enum
# from sqlalchemy import (
#     Column,
#     Integer,
#     String,
#     DateTime,
#     ForeignKey,
# )
# from sqlalchemy.orm import relationship
# from database_config import Base
#
#
# @dataclass
# class Vehicle:
#     id: int
#
#
# number: str
#
#
# class Status(Enum):
#     ACTIVE = “ACTIVE”
#     EXECUTED = “EXECUTED”
#     CANCELLED = “CANCELLED”
#
#     @dataclass
#     class Reservation:
#         id: int
#
#     vehicle_id: int
#     start_datetime: DateTime
#     end_datetime: Optional[DateTime] = None
#     status: Status = Status.ACTIVE
#
#
# engine = create_engine('sqlite:///database.db’, echo=True)
# Base.metadata.create_all(engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# def get_db():
#     try:
#         db = SessionLocal()
#
#
# yield db
# finally:
# if db:
#     db.close()
#
#
# # Теперь напишем функцию для добавления новой заявки:
#
# def add_reservation(start_datetime, end_datetime=None, vehicle=None):
#     db_session = get_db()
#
#
# try:
#     vehicle = Vehicle(number=vehicle.number)
# reservation = Reservation(
#     start_datetime=start_datetime,
#     end_datetime=end_datetime,
#     vehicle_id=vehicle.id
# )
# db_session.add(reservation)
# db_session.commit()
# return reservation
# except IntegrityError as exc:
# print(exc)
# return None
#
# from datetime import datetime, timedelta
# from uuid import uuid4
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from sqlalchemy import create_engine
# from sqlalchemy.engine.url import URL
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.sql import select
#
# database_url = URL(“sqlite: // / example.db”)
# engine = create_engine(database_url)
#
# Session = sessionmaker(bind=engine)
# session = scoped_session(Session)
# Base = automap_base()  # Используем для упрощения создания моделей
#
# Base.prepare(engine, reflect=True)
# Vehicle = Base.classes.vehicle  # Получаем класс Vehicle из таблицы
# Reservation = Base.classes.reservation  # Получаем класс Reservation из таблицы
#
#
# def create_reservation(vehicle_plate, start_time, end_time):
#
#
# # Создаем новый UUID для уникального ID бронирования
# reservation_id = uuid4()
#
# # Проверяем, не закончилось ли еще текущее бронирование
# current_reservations = session.query(Reservation).filter(
#     Reservation.vehicle_id == vehicle_plate
# )
# if current_reservations.count() > 0:
#     latest_reservation = current_reservations[0]
#     if start_time <= latest_reservation.start_time:
#         return "Ошибка: Бронирование уже активно"
#
# new_reservation = Reservation(id=reservation_id,
#                               vehicle_id=vehicle_plate,
#                               start_time=start_time,
#                               end_time=end_time)
# session.add(new_reservation)
# return new_reservation
#
# vehicle_plate = “ABC123”
# start_time = datetime.now()
# end_time = start_time + timedelta(minutes=30)
#
# from datetime import timedelta
# import uuid
# from itsdangerous import BadSignature
# from itsdangerous import URLSafeTimedSerializer
# from itsdangerous.expiringjson import (
#     JSONTimeMixin,
#     TimedJSONWebSignatureSerializer,
# )
# from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
# from sqlalchemy.orm import relation
# from database_config import Base, engine
#
#
# class State(str, Enum):
#
#
#     Active = “Active”
# Executed = “Executed”
# Cancelled = “Cancelled”
#
# class Vehicle(Base):
#
#
#     tablename = “vehicles”
# id = Column(Integer, primary_key=True)
# number = Column(String, unique=True, index=True, nullable=False)
# status = relation(State)
#
#
# class Booking(Base):
#
#
#     tablename = “bookings”
#
# id = Column(
#     Integer,
#     primary_key=True
# )
#
# vehicle_id = Column(
#     ForeignKey("vehicles.id", ondelete=“CASCADE”),
# nullable = False
# )
#
# start = Column(
#     DateTime,
#     default=func.current_timestamp()
# )
#
# end = Column(
#     DateTime
# )
#
# state = Column(Enum(State))
# def __repr__(self):
#     return f"<Booking {self.id}>"
#
# @Base.event
# def load_from_db(mapper, connection, target):
# pass
#
# def create(start, end, vehicle):
# booking = Booking(
# start=start,
# end=end,
# vehicle=vehicle,
# )
#
#     try:
#         session.add(booking)
#         session.commit()
#     except:
#         raise
#
#     return booking
#
# if name == “main”:
# serializer = TimedJSONWebSignatureSerializer(
# URLSafeTimedSerializer,
# timedelta(minutes=10),
# salt=“some_salt”,
# )


from datetime import timedelta
import uuid
from enum import Enum
from os import name

from itsdangerous import BadSignature
from itsdangerous import URLSafeTimedSerializer
# from itsdangerous.expiringjson import (
#     # JSONTimeMixin,
#     # TimedJSONWebSignatureSerializer,
# )
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relation, session
from database_config import Base, engine


class State(str, Enum):
    Active = "Active"
    Executed = "Executed"
    Cancelled = "Cancelled"


class Vehicle(Base):
    tablename = "vehicles"


id = Column(Integer, primary_key=True)
number = Column(String, unique=True, index=True, nullable=False)
status = relation(State)


class Booking(Base):
    tablename = "bookings"


id = Column(
    Integer,
    primary_key=True
)

vehicle_id = Column(
    ForeignKey("vehicles.id", ondelete="CASCADE"),
    nullable=False
)

start = Column(
    DateTime,
    default=func.current_timestamp()
)

end = Column(
    DateTime
)

state = Column(Enum(State))


def __repr__(self):
    return f"<Booking {self.id}>"


@Base.event
def load_from_db(mapper, connection, target):
    pass


def create(start, end, vehicle):
    booking = Booking(
        start=start,
        end=end,
        vehicle=vehicle,
    )


try:
    session.add(booking)
    session.commit()
except:
    raise

    # return booking


class TimedJSONWebSignatureSerializer:
    pass


if name == "main":
    serializer = TimedJSONWebSignatureSerializer(
        URLSafeTimedSerializer,
        timedelta(minutes=10),
        salt="some_salt",
    )

# class FootballPlayer:
#     pass
#
#
# if __name__ == "__main__":
#     r9 = FootballPlayer()
#
#     # При присвоении значения несуществующему полю класса Python дополняет класс
#     # Синтаксис похож на словарь, где ключ указывается не в скобках [], а через точку
#     r9.name = "Роналдо"
#     r9.birthday = "18/09/1976"
#     r9.position = "Нападающий"
#     r9.height = 1.83
#     r9.wc_goals = 15
#
# print(r9.name, r9.birthday, r9.position, r9.height, r9.wc_goals)



# {
#     "ts": [{
#         "grnz": "А111AА01",
#         "model": "Лада",
#         "class_main": "Легковые ТС",
#         "name_vehicle": "Лада"
#     }, {
#         "grnz": "А113АА03",
#         "model": "Икарус",
#         "class_main": "Автобусы",
#         "name_vehicle": "Икарус"
#     }
#     ],
#     "user": 1,
#     "status": "ok",
#     "profile": {
#         "tel": "+7-999-777-55-22",
#         "email": "testik@srv.ru",
#         "type_profile": "Физическое лицо"
#     }
# }
#
# [{
#     "interval": "00:20:00",
#     "slot_uid": "ccecb848-257b-4825-a997-6aa8cad0c9dd",
#     "mapp_guid": "914e6159-a06f-40c7-bdbb-535da10d7b24",
#     "time_slot": "2022-10-23T08:30:00"
# }, {
#     "interval": "00:20:00",
#     "slot_uid": "df57bb97-5f7a-4e7b-a065-ce68481f3a63",
#     "mapp_guid": "914e6159-a06f-40c7-bdbb-535da10d7b24",
#     "time_slot": "2022-10-23T08:35:00"
# }
# ]
