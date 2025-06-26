import os

class App:
    @staticmethod
    def createDF(name, lic=False):
        os.makedirs(name, exist_ok=True)

        main_path = os.path.join(name, "main.py")
        with open(main_path, "w") as f:
            f.write("print('Добро пожаловать в игру!')\n")

        if lic:
            licence_path = os.path.join(name, "licence.md")
            open(licence_path, "w").close()

        print(f"Проект '{name}' успешно создан.")