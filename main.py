import typer

app = typer.Typer()

@app.command()
def saludar(nombre: str, edad: int = typer.Option(None, help="Tu edad")):
    """Ejemplo de CLI con typer."""
    print(f"Hola, {nombre}!")
    if edad:
        print(f"Tienes {edad} años.")

if "__main__" == __name__:
    app()