# -- coding: cp1251 --
# =========================
# ?? BIRCH 2.0
# Повна інтеграція з Python
# =========================

import sys, os

variables = {}

# =========================
# Обробка коментарів і пустих рядків
# =========================
def clean_lines(code):
    lines = []
    for line in code.split("\n"):
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        lines.append(line)
    return lines

# =========================
# Виконання рядка BIRCH
# =========================
def exec_line(line):
    global variables
    # birch say
    if line.startswith("birch say"):
        expr = line.replace("birch say","").strip()
        try:
            print(eval(expr, {}, variables))
        except:
            print(expr)
    # birch set
    elif line.startswith("birch set"):
        rest = line.replace("birch set","").strip()
        if "=" in rest:
            name, expr = rest.split("=",1)
            variables[name.strip()] = eval(expr, {}, variables)
    # birch import
    elif line.startswith("birch import"):
        module_name = line.replace("birch import","").strip()
        variables[module_name] = __import__(module_name)
    # birch exec
    elif line.startswith("birch exec"):
        code_line = line.replace("birch exec","").strip()
        exec(code_line, {}, variables)

# =========================
# Основний запуск
# =========================
def run(code):
    lines = clean_lines(code)
    i = 0
    while i < len(lines):
        line = lines[i]
        # birch while
        if line.startswith("birch while"):
            cond = line.replace("birch while","").strip()
            block = []
            i += 1
            while i < len(lines) and lines[i] != "birch end":
                block.append(lines[i])
                i += 1
            while eval(cond, {}, variables):
                run("\n".join(block))
        # birch for
        elif line.startswith("birch for"):
            expr = line.replace("birch for","").strip()
            block = []
            i += 1
            while i < len(lines) and lines[i] != "birch end":
                block.append(lines[i])
                i += 1
            exec(f"for {expr}: run('''\n{chr(10).join(block)}\n''')", {}, variables)
        else:
            exec_line(line)
        i += 1

# =========================
# Головний блок
# =========================
if __name__== "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Вкажи шлях до .birch файлу:\n")

    if not os.path.isfile(path):
        print(f"? Файл не знайдено: {path}")
    else:
        try:
            with open(path, encoding="cp1251") as f:
                code = f.read()
            run(code)
        except Exception as e:
            print(f"? Помилка: {e}")

    input("\nНатисни Enter щоб закрити...")
