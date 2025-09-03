%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Читаем CSV файл
df = pd.read_csv('graf.csv')

# Показываем данные
print("Данные из CSV:")
print(df)
print("\nСтолбцы:", df.columns.tolist())

# Создаем график
plt.figure(figsize=(12, 7))

# График продаж
plt.plot(df['name'], df['home'], 'o-', linewidth=3, markersize=8, label='Sales', color='blue')

# График расходов
plt.plot(df['name'], df['village'], 's--', linewidth=2, markersize=6, label='Expenses', color='red')

# График прибыли
plt.plot(df['name'], df['cyti'], '^-', linewidth=2, markersize=6, label='Profit', color='green')

# Настройки графика
plt.title('Business Metrics Overview', fontsize=16, fontweight='bold')
plt.xlabel('name', fontsize=14)
plt.ylabel('Amount ($)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xticks(rotation=45)

# Добавляем подписи значений
for i, (sales, expenses, profit) in enumerate(zip(df['home'], df['village'], df['cyti'])):
    plt.annotate(f'{sales}', (i, sales), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
    plt.annotate(f'{expenses}', (i, expenses), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=9)
    plt.annotate(f'{profit}', (i, profit), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

plt.tight_layout()
plt.show()