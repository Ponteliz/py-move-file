import os


def move_file(command: str) -> None:
    _, source, destination = command.split()

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)

    destination_dir = os.path.dirname(destination)

    if destination_dir:
        current_path = ""

        for directory in destination_dir.split("/"):
            current_path = (
                directory
                if current_path == ""
                else current_path + "/" + directory
            )

            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as source_file:
        content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(content)

    os.remove(source)
