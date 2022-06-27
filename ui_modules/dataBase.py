import sqlite3
import pymysql
import os
import re

# Кастомынй класс исключения
class CustomError(Exception):
    pass

# Класс работы с базой данных
class DataBase:
    # 1.	Инициализатор класса
    def __init__(self):
        self.connection = None
        self.cursor = None
    # 2.	Подключение к базе данны
    def connect(self, mode: int = None, path: str = '', host: str = '', user: str = '', password: str = '', name: str = ''):
        try:
            if mode is None:
                raise CustomError('Не указана БД')
            elif mode == 2:
                self.connection = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=name
                )
            elif mode == 1:
                if path == '':
                    raise CustomError('Неверно указан путь')
                if not os.path.isfile(path):
                    raise CustomError('Файл отсутствует по пути')
                if not os.path.splitext(path)[1] == '.sqlite3':
                    raise CustomError('Указанный файл не имеет\nрасширения .sqlite3')
                self.connection = sqlite3.connect(path)

            self.cursor = self.connection.cursor()
        except Exception as a:
            raise a

    @staticmethod
    def __check(values: list):
        for i, val in enumerate(values):
            if re.sub(r'[\d]+', '', str(val)) in ['', '.']:
                values[i] = str(val)
            else:
                values[i] = f"'{val}'"
    # 3.	Универсальное получение данных по условию из базы данных
    def getDataCondition(self, tableName: str, objects: list, condition: list = [], distinct: bool = False):
        text = ''
        if len(condition) != 0:
            text = f' WHERE {" AND ".join(condition)}'

        dist = ''
        if distinct:
            dist = 'DISTINCT '

        self.cursor.execute(f'SELECT {dist}{",".join(objects)} FROM {tableName}{text};')
        return self.cursor.fetchall()
    # 4.	Вписывание данных в базу данных
    def insertMany(self, tableName: str, mask: list, maskValue: list, data: list):
        rec = f'INSERT INTO {tableName} ({", ".join(mask)}) VALUES ({", ".join(maskValue)});'
        self.cursor.executemany(rec, data)
        self.connection.commit()
    # 5.	Проверки наличия таблиц в базе данных
    def checkTable(self):
        self.cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table"')
        return [i[0] for i in self.cursor.fetchall()]
    # 6.	Создания таблиц в базе данных
    def createTablesSQLite(self):
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS "account" (
                "id"	INTEGER NOT NULL,
                "login"	TEXT,
                "password"	TEXT,
                "status"	INTEGER,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            CREATE TABLE IF NOT EXISTS "operation" (
                "id"	INTEGER NOT NULL,
                "code"	TEXT NOT NULL,
                "name"	TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            CREATE TABLE IF NOT EXISTS "device" (
                "id"	INTEGER NOT NULL,
                "type"	TEXT NOT NULL,
                "numb"	TEXT NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            CREATE TABLE IF NOT EXISTS "jornal" (
                "id"	INTEGER NOT NULL,
                "id_dev"	INTEGER NOT NULL,
                "id_oper"	INTEGER NOT NULL DEFAULT 2,
                "rep_to"	INTEGER,
                "note"	TEXT,
                "executor"	TEXT,
                "date"	TEXT,
                "time"	TEXT,
                PRIMARY KEY("id" AUTOINCREMENT)
            );
            DELETE FROM sqlite_sequence;
            DELETE FROM account;
            DELETE FROM operation;
        ''')
        data = [
            ['rep', 'Ремонт'],
            ['070', 'Функционирование'],
            ['075', 'Сборка'],
            ['080', 'Электромонтаж'],
            ['085', 'Заливка'],
            ['090', 'Контроль'],
            ['100', 'Технологическая вибрация'],
            ['105', 'Функционирование'],
            ['110', 'Сборка'],
            ['115', 'Герметизация'],
            ['120', 'Функционирование'],
            ['122', 'Окрашивание'],
            ['125', 'Маркирование'],
            ['130', 'Сборка'],
            ['135', 'Функционирование'],
            ['137.1', 'Настройка - Калибровка'],
            ['137.2', 'Настройка - Верификация 1'],
            ['137.3', 'Настройка - Верификация 2'],
            ['140', 'Контроль внешнего вида'],
            ['145', 'Предъявительские испытания'],
            ['150', 'Приёмосдаточные испытания'],
            ['155', 'Сборка'],
            ['160', 'Контроль внешнего вида'],
            ['170', 'Упаковка']
        ]
        self.insertMany('operation', ['code', 'name'], ['?', '?'], data)

        data = [
            ['admin', 'admin', '1'],
            ['user', 'user', '0']
        ]

        self.insertMany('account', ['login', 'password', 'status'], ['?', '?', '?'], data)

