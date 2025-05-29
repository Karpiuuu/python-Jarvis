import subprocess
import tempfile

class ShowCommands:
    name = "show_commands"
    description = "Pokazuje wszystkie dostępne komendy w Notatniku"

    def execute(self, argument: str = "", commands_list: list = []) -> str:
        lines = ["Dostępne komendy:\n"]
        for cmd in commands_list:
            name = getattr(cmd, "name", "brak_nazwy")
            desc = getattr(cmd, "description", "")
            lines.append(f"- {name}: {desc}")

        content = "\n".join(lines)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
            f.write(content)
            temp_file_path = f.name

        subprocess.Popen(["notepad.exe", temp_file_path])
        return "Wyświetlam listę komend w Notatniku."