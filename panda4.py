import pandas as pd

# Загрузка файла dz.csv в DataFrame
file_path = 'dz.csv'
df = pd.read_csv(file_path)

# Проверка первых строк для ознакомления с структурой данных (опционально)
print(df.head())

# Группировка по городу и расчет средней зарплаты
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результата
print(average_salary_by_city)
