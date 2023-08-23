from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict[str, int]]:
        projects = await session.execute(
            select([CharityProject.id]).where(
                CharityProject.close_date is True
            ).order_by(CharityProject.close_date)
        )
        projects = projects.all()
        return projects


charity_project_crud = CRUDCharityProject(CharityProject)
