# 1. Создать произвольный словарь
my_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    1 : 34,
    2: [1,14]
}
# 2. Добавить новый элемент с ключом типа str и значением типа int
my_dict["newkey"] = 2
print(my_dict)
# 3. Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list)
my_dict[("newkey", "hh")] = [4,3,"jjj", True,[0,0,0,0]]
print(my_dict)
# 4. Получить элемент по ключу
print(my_dict["newkey"])
# 5. Удалить элемент по ключу
my_dict.pop(("newkey", "hh"))
print(my_dict)
# 6. Получить список ключей словаря
print(my_dict.keys())
