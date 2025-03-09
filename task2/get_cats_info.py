def get_cats_info(path):
    try:
        data = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    id_, name, age = parts 
                    data.append({"id": id_, "name": name, "age": age})  
        return data

    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
    

#Test:
cats_info = get_cats_info("./task2/cats_file.txt")
print(cats_info)
