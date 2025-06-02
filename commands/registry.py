from commands.youtube import OpenYouTubeCommand
from commands.show_commands import ShowCommands
import json

COMMANDS = [
    OpenYouTubeCommand(),
    ShowCommands(),
]

def get_commands_json() -> str:
    data = [
        {"name": cmd.name, "description": cmd.description}
        for cmd in COMMANDS
    ]
    return json.dumps(data, ensure_ascii=False, indent=2)

def execute_command(name: str, argument: str = "") -> str | None:
    for command in COMMANDS:
        if getattr(command, "name", None) == name:
            if name == "show_commands":
                return command.execute(argument, COMMANDS)
            return command.execute(argument)
    return None
