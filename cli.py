import click

@click.group()
def main():
    pass

@main.command()
@click.argument("numero1", type=int, default=0)
@click.argument("numero2", type=int, default=0)
@click.option("--numero1", prompt="Ingresa numero")
@click.option("--numero2", prompt="Ingresa numero")

def suma(numero1, numero2):
    n1 = numero1
    n2 = numero2
    res = float(n1) + float(n2)
    click.echo("RESULTADO: "+str(res))

@main.command()
@click.argument("numero1", type=int, default=0)
@click.argument("numero2", type=int, default=0)
@click.option("--numero1", prompt="Ingresa numero")
@click.option("--numero2", prompt="Ingresa numero")

def resta(numero1, numero2):
    n1 = numero1
    n2 = numero2
    res = float(n1) - float(n2)
    click.echo("RESULTADO: "+str(res))

@main.command()
@click.argument("numero1", type=int, default=0)
@click.argument("numero2", type=int, default=0)
@click.option("--numero1", prompt="Ingresa numero")
@click.option("--numero2", prompt="Ingresa numero")

def producto(numero1, numero2):
    n1 = numero1
    n2 = numero2
    res = float(n1) * float(n2)
    click.echo("RESULTADO: "+str(res))

@main.command()
@click.argument("numero1", type=int, default=0)
@click.argument("numero2", type=int, default=0)
@click.option("--numero1", prompt="Ingresa numero")
@click.option("--numero2", prompt="Ingresa numero")

def division(numero1, numero2):
    n1 = numero1
    n2 = numero2
    res = float(n1) / float(n2)
    click.echo("RESULTADO: "+str(res))


if __name__ == "__main__":
    main()



     

