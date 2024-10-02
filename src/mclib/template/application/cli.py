import typer

from mclib.template.sample import *  # TODO: update this

main = typer.Typer()

@main.command()
def sample_command(
    input_1: str = typer.Option(
        ...,
        prompt="Sample Input 1",
        help="Sample Input 1",
    ),
    input_2: float = typer.Option(
        ...,
        prompt="Sample Input 2",
        help="Sample Input 2",
    ),
):
    raise NotImplementedError()


# Entry point for the CLI app
if __name__ == "__main__":
    main()
