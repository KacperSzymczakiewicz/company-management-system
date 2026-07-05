import sys
import logging

from src.members.engineer import Engineer
from src.members.manager import Manager
from src.members.team_lead import TeamLead
from src.models.project import Project
from src.company import Company

logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(asctime)s | %(levelname)-8s | %(name)-30s | %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S'
                    )
logger = logging.getLogger(__name__)


def main() -> None:
    try:
        logger.info("Application started")
        engineer = Engineer(1, "Anna Kowalska", 28, specialization="backend")
        manager = Manager(2, "Jan Nowak", 45)
        team_lead = TeamLead(3, "Piotr Wiśniewski", 35, specialization="fullstack")

        company = Company()
        company.add_member(engineer)
        company.add_member(manager)
        company.add_member(team_lead)

        company.create_team(team_lead, [engineer])

        project = Project("System HR", 50000)
        company.assign_project_to_team(team_lead, project)

        company.load_tasks_from_file("data/tasks.txt", project)

        task = project.tasks[1]

        engineer.add_task(task)
        engineer.perform_task(1)

        engineer.implement_task(1)

        team_lead.add_task(task)
        team_lead.review_task(task)

        manager.complete_task(task)

        company.save_report("data/report.json")
        logger.info("Application finished successfully")
    except (ValueError, FileNotFoundError) as e:
        logger.error(f"Application failed with error: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
