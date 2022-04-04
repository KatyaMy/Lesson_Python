# log_file = "all.log"  -- путь к файлу
# warning_logfile = "warning.log" -- путь к файлу в который будет записана информация
# warnings = [] -- сохраниение всего  в лист

# with open(log_file, 'r') as file: -- открыть и прочитать файл(по линиям) и выбрать файлы с WARNING
# file --- название переменной с которой мы будем оперировать
#     for line in file.readlines():
#         if "WARNING" in line: -- проверка строки на файл WARNING
#             warnings.append(line)

# --- Запись  в новый файл-----
# with open(warning_logfile, 'w') as file:
#     for item in warnings:
#         file.write(item)
