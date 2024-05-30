import typer

from rich.console import Console
from rich.table import Table

console=Console()

app=typer.Typer()


@app.command(short_help="Adds an item")
def add(task: str, category: str):
    typer.echo(f"Adding {task}, {category}")

@app.command(short_help="Deletes an item")
def delete(position: int):
    typer.echo(f"Deleting {position}")

@app.command(short_help="Updates an item")
def update(position:int, task:str=None, category:str=None):
    typer.echo(f"Updating {position}")


@app.command(short_help="Complete the function")
def complete(position:int):
    typer.echo(f"Complete: {position}")


@app.command(short_help="Show the tasks")
def show():
    tasks=[("TODO1", "Sports"), ("TODO2", "Study")]
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    table=Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS={'learn':'cyan', 'youtube':'red', 'sports':'cyan', 'study':'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c=get_category_color(task[1])
        is_done_str='✅' if True==2 else "❌"
        

if __name__=="__main__":
    app()