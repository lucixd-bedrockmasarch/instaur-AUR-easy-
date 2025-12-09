import subprocess
from rich.progress import track
from rich.console import Console
import time

console = Console()

progress_emoji = "💎"

def install_official(pkg):
    console.print(f"[green]Instalando {pkg} desde repos oficiales...[/green]")
    for _ in track(range(100), description=f"{progress_emoji*1} Instalando {pkg} {progress_emoji*1}"):
        time.sleep(0.02)
    subprocess.run(["sudo", "pacman", "-S", pkg])

def update_all():
    console.print("[cyan]Actualizando repos oficiales...[/cyan]")
    for _ in track(range(100), description=f"{progress_emoji*1} Actualizando {progress_emoji*1}"):
        time.sleep(0.01)
    subprocess.run(["sudo", "pacman", "-Syu"])
