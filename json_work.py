import json
from os import stat
from Sortings import sortings as s


class Json_Saver:
    def __init__(self, sort_name):
        self.filename = f"Sortings/{sort_name}.json"
        f = open(self.filename, 'a', encoding="utf8")
        f.close()
        self.cases = dict()

    def add_case(self, case, name):
        """
        :param case: массив данных для какого-либо случая например [(5000, 1.25), (6000, 1.67), ...]
        :name: имя случая
        :return:
        """
        case = dict(case)

        with open(self.filename, encoding="utf8") as f:
            if stat(self.filename).st_size != 0:
                data = json.load(f)
                data[name] = case
            else:
                data = {name: case}
            with open(self.filename, 'w', encoding="utf8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)

    def get_case(self, name):
        try:
            with open(self.filename, 'r', encoding="utf8") as f:
                data = json.load(f)
            return data[name]
        except FileNotFoundError:
            print("Файл не найден.")
        except:
            print("Ошибка при полученнии данных.")


if __name__ == "__main__":
    print("Запущен json_work.py")

