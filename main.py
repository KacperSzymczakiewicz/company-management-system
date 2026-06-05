from src.members.engineer import Engineer
from src.members.manager import Manager
from src.members.team_lead import TeamLead
from src.models.project import Project
from src.company import Company
from src.utils.file_handler import FileHandler


def main() -> None:
    try:
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
        print(task.info())

        engineer.implement_task(1)
        print(task.info())

        team_lead.add_task(task)
        team_lead.review_task(1)
        print(task.info())

        manager.complete_task(task)
        print(task.info())

        print(engineer.info())
        print(manager.info())
        print(team_lead.info())

        company.save_report("data/report.json")
        print("Report saved to data/report.json")
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
