# app/services/google_api.py

from datetime import datetime

from aiogoogle import Aiogoogle

# В секретах лежит адрес вашего личного google-аккаунта
from app.core.config import settings

# Константа с форматом строкового представления времени
FORMAT = "%Y/%m/%d %H:%M:%S"


# Создаём документ
async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    # Получаем текущую дату для заголовка документа
    now_date_time = datetime.now().strftime(FORMAT)
    # Создаём экземпляр класса Resourse
    service = await wrapper_services.discover('sheets', 'v4')
    # Формируем тело запроса
    spreadsheet_body = {
        'properties': {
            'title': f'Отчет на {now_date_time}',
            'locale': 'ru_RU'
        },
        'sheets': [
            {'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {'rowCount': 100, 'columnCount': 11}
            }}
        ]
    }
    # Выполняем запрос
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


# Предоставляем права доступа
async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.EMAIL}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields="id"
        ))


# Наполняем документ данными
async def spreadsheets_update_value(
        spreadsheetid: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)

    service = await wrapper_services.discover('sheets', 'v4')
    # Здесь формируется тело таблицы
    table_values = [
        ['Отчет от', now_date_time],
        ['Топ проектов по скорости закрытия'],
        ['Название проекта', 'Время сбора', 'Описание']
    ]
    # Здесь в таблицу добавляются строчки
    for project in charity_projects:
        create_date = datetime(project['create_date'])
        close_date = datetime(project['close_date'])
        pass_time = close_date - create_date
        new_row = [
            str(project['name']),
            str(project[pass_time]),
            str(project['description'])
        ]
        table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
