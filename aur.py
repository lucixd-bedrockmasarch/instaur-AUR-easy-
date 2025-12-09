import requests
import subprocess
from rich.console import Console
from rich.progress import track
import time
import os
import random

console = Console()

# Emoji para la barra de progreso
progress_emoji = "💎"

def search_aur(pkg):
    url = f"https://aur.archlinux.org/rpc/?v=5&type=search&arg={pkg}"
    r = requests.get(url).json()
    results = r.get('results', [])
    if not results:
        console.print(f"[red]No se encontró el paquete {pkg}[/red]")
        return
    for res in results:
        console.print(f"📦 {res['Name']} - {res['Version']} - {res['Description']}")

def install_aur(pkg):
    console.print(f"[green]Clonando {pkg} desde AUR...[/green]")
    if os.path.exists(pkg):
        subprocess.run(["rm", "-rf", pkg])
    subprocess.run(["git", "clone", f"https://aur.archlinux.org/{pkg}.git"])
    
    console.print("[cyan]Compilando e instalando paquete...[/cyan]")
    for _ in track(range(100), description=f"{progress_emoji*1} Instalando {pkg} {progress_emoji*1}"):
        time.sleep(0.02)
    
    subprocess.run(["makepkg", "-si"], cwd=pkg)
