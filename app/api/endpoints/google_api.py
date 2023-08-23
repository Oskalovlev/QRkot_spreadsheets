# Понадобится для того, чтобы задать временные интервалы
from datetime import datetime

# Класс «обёртки»
from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.services.google_api import (
    spreadsheets_create,
    set_user_permissions,
    spreadsheets_update_value
)

# Создаём экземпляр класса APIRouter
router = APIRouter()


@router.post(
    '/',
    # Тип возвращаемого эндпоинтом ответа
    response_model=list[dict[str, int]],
    # Определяем зависимости
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        # Начало периода
        # from_reserve: datetime,
        # # Конец периода
        # to_reserve: datetime,
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    """Только для суперюзеров."""
    reservations = await charity_project_crud.get_projects_by_completion_rate(
        session
    )

    # Вызов функций
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(
        spreadsheetid, reservations, wrapper_services
    )
    return reservations
