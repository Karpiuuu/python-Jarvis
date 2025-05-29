
from commands.youtube import OpenYouTubeCommand

COMMANDS = [
    OpenYouTubeCommand(),
]

def execute_command(classified_text):
    if not classified_text:
        return None

    parts = classified_text.split(" ", 1)
    command_name = parts[0]
    command_arg = parts[1] if len(parts) > 1 else ""

    for command in COMMANDS:
        if hasattr(command, "name") and command.name == command_name:
            return command.execute(command_arg)

    return None