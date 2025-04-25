#1 Канкулятор индекса массы телы(ИМТ)
import matplotlib.pyplot as plt

def main():
    weight = float(input("Введите ваш вес (в кг): "))
    height = float(input("Введите ваш рост (в метрах): "))
    
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        classification = "Недостаточный вес"
    elif bmi < 24.9:
        classification = "Нормальный вес"
    elif bmi < 29.9:
        classification = "Избыточный вес"
    else:
        classification = "Ожирение"
    
    print(f"Ваш ИМТ: {bmi:.2f} ({classification})")
    
    # Построение простого графика
    plt.figure(figsize=(10, 6))
    
    # Создаем диапазоны ИМТ
    bmi_ranges = [0, 18.5, 24.9, 29.9, 40]
    bmi_labels = ['Недостаточный вес', 'Нормальный вес', 'Избыточный вес', 'Ожирение']
    
    # Рисуем прямоугольники для каждого диапазона ИМТ
    plt.axvspan(0, 18.5, alpha=0.3, color='lightblue')
    plt.axvspan(18.5, 24.9, alpha=0.3, color='green')
    plt.axvspan(24.9, 29.9, alpha=0.3, color='orange')
    plt.axvspan(29.9, 40, alpha=0.3, color='red')
    
    # Отмечаем текущий ИМТ пользователя
    plt.plot(bmi, 0, 'ro', markersize=10)
    
    # Настройка графика
    plt.xlim(0, 40)
    plt.ylim(-0.5, 0.5)
    plt.xlabel('Индекс массы тела (ИМТ)')
    plt.title('Диаграмма ИМТ')
    
    # Убираем метки по оси Y
    plt.yticks([])
    
    # Добавляем текстовые метки для диапазонов ИМТ
    plt.text(9, 0.3, 'Недостаточный вес', ha='center')
    plt.text(21.7, 0.3, 'Нормальный вес', ha='center')
    plt.text(27.4, 0.3, 'Избыточный вес', ha='center')
    plt.text(35, 0.3, 'Ожирение', ha='center')
    
    # Добавляем метку для текущего ИМТ
    plt.text(bmi, -0.3, f'Ваш ИМТ: {bmi:.2f}', ha='center', color='red')
    
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

main()