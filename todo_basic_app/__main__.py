"""To-Do Basic App entry point script."""
# todo_basic_app/__main__.py

from todo_basic_app import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()
