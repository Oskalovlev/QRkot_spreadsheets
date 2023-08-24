from typing import List
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings

JSON_SPREADSHEET = {
    'properties': {
        'title': 'Отчет на текущую дату',
        'locale': 'ru_RU'
    },
    'sheets': [
        {'properties': {
            'sheetType': 'GRID',
            'sheetId': settings.ZERO,
            'title': 'Лист1',
            'gridProperties': {
                'rowCount': settings.ROW_COUNT,
                'columnCount': settings.COLUMN_COUNT
            }
        }}
    ]
}
JSON_TABLE = [
    ['Отчет от', 'текущего времени'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]


async def spreadsheets_create(
    wrapper_services: Aiogoogle
) -> str:
    now_date_time = datetime.now().strftime(settings.FORMAT)
    JSON_SPREADSHEET['properties']['title'] = f'Отчет на {now_date_time}'

    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=JSON_SPREADSHEET)
    )
    spreadsheetid = response['spreadsheetId']
    return spreadsheetid


async def set_user_permissions(
    spreadsheetid: str,
    wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'
        ))


async def spreadsheets_update_value(
    spreadsheetid: str,
    charity_projects: List,
    wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(settings.FORMAT)

    service = await wrapper_services.discover('sheets', 'v4')
    JSON_TABLE[0] = ['Отчет от', now_date_time]
    table_values = JSON_TABLE
    for project in charity_projects:
        new_row = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description)
        ]
        if len(new_row) <= settings.ROW:
            table_values.append(new_row)

    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range='R1C1:R15C5',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
