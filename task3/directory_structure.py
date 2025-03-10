import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)
print(f"sys.argv: {sys.argv}")


def directory_structure(path, indent=""):
    dir_path = Path(path).resolve()
    
    if not dir_path.exists():
        print(Fore.RED + "Вказаний шлях не існує!")
        return

    if not dir_path.is_dir():
        print(Fore.RED + "Вказаний шлях не є директорією!")
        return
    
    items = sorted(dir_path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))

    for index, item in enumerate(items):
        connector = "└─" if index == len(items) - 1 else "├─"
        if item.is_dir():
            print(Fore.BLUE + indent + connector + "📁 " + item.name)
            directory_structure(item, indent + ("  " if index == len(items) - 1 else "│ "))
        else:
            print(Fore.GREEN + indent + connector + " 📄 " + item.name)


if __name__ == "__main__":  
    path = sys.argv[1]  
    directory_structure(path)