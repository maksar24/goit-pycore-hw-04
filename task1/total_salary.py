def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [int(line.split(",")[1]) for line in file if line.strip()]
        
        if not salaries:
            return (0, 0)

        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено")
        return (0, 0)
    except ValueError:
        print("Помилка у форматі даних")
        return (0, 0)


# Test:
total, average = total_salary("./task1/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
