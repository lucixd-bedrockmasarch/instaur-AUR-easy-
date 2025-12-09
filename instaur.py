#!/usr/bin/env python
import sys
import os
import random

# Asegura que Python pueda encontrar los módulos aur.py y pacman.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from aur import search_aur, install_aur
from pacman import install_official, update_all
from rich.console import Console

console = Console()

# Mensajes tipo "Sabías que..."
tips = [
    "💡 Sabías que LibreOffice es gratuito y compatible con documentos de Microsoft Office?",
    "💡 Sabías que GIMP es un editor de imágenes libre y potente?",
    "💡 Sabías que VLC puede reproducir casi cualquier video o audio?",
    "💡 Sabías que Firefox tiene muchas extensiones gratuitas para mejorar tu privacidad?",
    "💡 Sabías que Inkscape permite crear gráficos vectoriales profesionales?",
    "💡 Sabías que Audacity es un editor de audio libre y multiplataforma?"
]

def main():
    console.print("[bold cyan]Bienvenido a INSTAUR - Tu gestor AUR futurista[/bold cyan]")
    
    while True:
        console.print("\nOpciones:")
        console.print("1. Buscar paquete")
        console.print("2. Instalar paquete")
        console.print("3. Actualizar repos oficiales")
        console.print("4. Salir")

        choice = console.input("\nIngresa opción: ")

        if choice == "1":
            pkg = console.input("Nombre del paquete: ")
            search_aur(pkg)
        elif choice == "2":
            pkg = console.input("Nombre del paquete: ")
            tipo = console.input("¿AUR (a) o oficial (o)? [a/o]: ")
            tip = random.choice(tips)
            console.print(f"[magenta]{tip}[/magenta]")
            if tipo.lower() == "a":
                install_aur(pkg)
            else:
                install_official(pkg)
        elif choice == "3":
            tip = random.choice(tips)
            console.print(f"[magenta]{tip}[/magenta]")
            update_all()
        elif choice == "4":
            console.print("[bold green]Adiós![/bold green]")
            break
        else:
            console.print("[red]Opción inválida[/red]")

if __name__ == "__main__":
    main()

