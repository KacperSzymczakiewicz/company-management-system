from pathlib import Path

from src.company import Company
from src.models.project import Project
from src.utils.file_handler import FileHandler

class TestFileHandler:

    def test_file_reader(self, tmp_path: Path, project: Project) -> None:
        file = tmp_path / "file.txt"
        file.write_text("1|Login|Opis|pending\n")
        FileHandler.file_reader(str(file), project)

        assert len(project.tasks) == 1


    def test_save_report_to_file(self, tmp_path: Path, company: Company) -> None:
        file = tmp_path / "report.json"
        FileHandler.save_report(str(file), company)

        assert file.exists()
        assert file.stat().st_size > 0