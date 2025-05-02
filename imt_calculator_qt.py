# Импорт необходимых модулей
import sys  # Импорт модуля sys для работы с системными функциями
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                        QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)  # Импорт виджетов PyQt5
from PyQt5.QtCore import Qt  # Импорт основных классов Qt
from PyQt5.QtGui import QFont  # Импорт класса для работы со шрифтами
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  # Импорт холста для отображения графиков
from matplotlib.figure import Figure  # Импорт класса для создания фигур

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        # Настройка основного окна
        self.setWindowTitle("Калькулятор ИМТ")  # Установка заголовка окна
        self.setMinimumSize(800, 600)  # Установка минимального размера окна
        
        # Создание центрального виджета и основного layout
        central_widget = QWidget()  # Создание центрального виджета
        self.setCentralWidget(central_widget)  # Установка центрального виджета
        layout = QVBoxLayout(central_widget)  # Создание вертикального layout
        
        # Создание layout для полей ввода (вес и рост)
        input_layout = QHBoxLayout()  # Создание горизонтального layout для полей ввода
        
        # Создание поля ввода для веса
        weight_layout = QVBoxLayout()  # Создание вертикального layout для веса
        weight_label = QLabel("Вес (кг):")  # Создание метки для поля веса
        self.weight_input = QLineEdit()  # Создание поля ввода для веса
        self.weight_input.setPlaceholderText("Введите ваш вес")  # Установка подсказки в поле ввода
        weight_layout.addWidget(weight_label)  # Добавление метки в layout
        weight_layout.addWidget(self.weight_input)  # Добавление поля ввода в layout
        
        # Создание поля ввода для роста
        height_layout = QVBoxLayout()  # Создание вертикального layout для роста
        height_label = QLabel("Рост (м):")  # Создание метки для поля роста
        self.height_input = QLineEdit()  # Создание поля ввода для роста
        self.height_input.setPlaceholderText("Введите ваш рост")  # Установка подсказки в поле ввода
        height_layout.addWidget(height_label)  # Добавление метки в layout
        height_layout.addWidget(self.height_input)  # Добавление поля ввода в layout
        
        # Добавление полей ввода в горизонтальный layout
        input_layout.addLayout(weight_layout)  # Добавление layout веса
        input_layout.addLayout(height_layout)  # Добавление layout роста
        
        # Создание кнопки расчета и подключение обработчика события
        self.calculate_button = QPushButton("Рассчитать ИМТ")  # Создание кнопки
        self.calculate_button.clicked.connect(self.calculate_bmi)  # Подключение обработчика нажатия
        # Установка стилей для кнопки расчета
        self.calculate_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 5px;
                min-width: 150px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        
        # Создание метки для отображения результата
        self.result_label = QLabel("")  # Создание пустой метки
        self.result_label.setAlignment(Qt.AlignCenter)  # Выравнивание по центру
        self.result_label.setFont(QFont("Arial", 14))  # Установка шрифта
        
        # Создание области для графика
        self.figure = Figure(figsize=(10, 4))  # Создание фигуры для графика
        self.canvas = FigureCanvas(self.figure)  # Создание холста для отображения графика
        
        # Добавление всех элементов в основной layout
        layout.addLayout(input_layout)  # Добавление layout полей ввода
        layout.addWidget(self.calculate_button)  # Добавление кнопки
        layout.addWidget(self.result_label)  # Добавление метки результата
        layout.addWidget(self.canvas)  # Добавление графика
        
        # Установка стилей для элементов интерфейса
        self.setStyleSheet("""
            QMainWindow {                   
                background-color: #f0f0f0; 
            }
            QWidget {                      
                font-family: Arial;        
            }
            QLabel {                        
                font-size: 14px;           
                color: #333333;             
            }
            QLineEdit {                     
                padding: 8px;              
                border: 1px solid #cccccc;  
                border-radius: 4px;         
                font-size: 14px;            
                background-color: white;    
            }
            QLineEdit:focus {               
                border: 1px solid #4CAF50;  
            }
        """)
    
    def calculate_bmi(self):
        """
        Метод для расчета ИМТ и обновления интерфейса.
        Вызывается при нажатии на кнопку расчета.
        """
        try:
            # Получение и проверка введенных значений
            weight = float(self.weight_input.text())  # Получение веса из поля ввода
            height = float(self.height_input.text())  # Получение роста из поля ввода
            
            if weight <= 0 or height <= 0:  # Проверка на положительные значения
                QMessageBox.warning(self, "Ошибка", "Вес и рост должны быть положительными числами")
                return
            
            # Расчет ИМТ
            bmi = weight / (height ** 2)  # Формула расчета ИМТ
            
            # Определение категории веса и соответствующего цвета
            if bmi < 18.5:  # Проверка на недостаточный вес
                classification = "Недостаточный вес"
                color = "#000080"  # темно-синий
            elif bmi < 24.9:  # Проверка на нормальный вес
                classification = "Нормальный вес"
                color = "#006400"  # темно-зеленый
            elif bmi < 29.9:  # Проверка на избыточный вес
                classification = "Избыточный вес"
                color = "#8B4513"  # темно-оранжевый
            else:  # Ожирение
                classification = "Ожирение"
                color = "#8B0000"  # темно-красный
            
            # Обновление метки с результатом
            self.result_label.setText(f"Ваш ИМТ: {bmi:.2f} ({classification})")  # Установка текста результата
            self.result_label.setStyleSheet(f"color: {color}; font-size: 16px; font-weight: bold;")  # Установка стиля
            
            # Обновление графика
            self.update_plot(bmi)  # Вызов метода обновления графика
            
        except ValueError:  # Обработка ошибки ввода
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения")
    
    def update_plot(self, bmi):
        """
        Метод для обновления графика ИМТ.
        Создает визуальное представление диапазонов ИМТ и отмечает текущее значение.
        Аргументы:
            bmi (float): Рассчитанное значение ИМТ
        """
        self.figure.clear()  # Очистка предыдущего графика
        ax = self.figure.add_subplot(111)  # Создание подграфика
        
        # Определение диапазонов ИМТ и их визуального оформления
        bmi_ranges = [0, 18.5, 24.9, 29.9, 40]  # Границы диапазонов ИМТ
        bmi_labels = ['Недостаточный\nвес', 'Нормальный\nвес', 'Избыточный\nвес', 'Ожирение']  # Подписи диапазонов
        colors = ['#0066CC', '#009933', '#FF6600', '#CC0000']  # Цвета для каждого диапазона
        
        # Создание столбцов для каждого диапазона ИМТ
        bars = ax.bar(
            range(4),  # 4 столбца для 4 диапазонов ИМТ
            [18.5, 6.4, 5, 10.1],  # высоты столбцов
            bottom=[0, 18.5, 24.9, 29.9],  # нижние позиции
            color=colors,  # цвета из списка colors
            alpha=0.7,  # прозрачность
            width=0.9  # ширина столбцов
        )
        # Добавление подписей к столбцам диаграммы
        for i in range(len(bars)):
            bar = bars[i]
            # Вычисление центра столбца
            center_x = bar.get_x() + bar.get_width()/2
            center_y = bar.get_y() + bar.get_height()/2
            
            # Добавление текстовой метки в центр столбца
            ax.text(center_x, center_y, bmi_labels[i], 
                ha='center',  # горизонтальное выравнивание по центру
                va='center',  # вертикальное выравнивание по центру
                fontsize=10,  # размер шрифта
                fontweight='bold',  # жирный шрифт
                color='white')  # белый цвет текста
        # Определение позиции для отметки текущего ИМТ
        display_bmi = min(bmi, 40)  # Ограничение максимального отображаемого значения
        for i in range(len(bmi_ranges)-1):
            if bmi_ranges[i] <= display_bmi < bmi_ranges[i+1]:
                x_pos = i
                break
        else:
            x_pos = len(bmi_ranges)-2
            
        x_pos = x_pos + 0.6  # Корректировка позиции по X
        
        # Добавление точки, обозначающей текущий ИМТ
        ax.plot(x_pos, display_bmi, 'ro', markersize=10, markeredgewidth=1.5, 
                markerfacecolor='red', markeredgecolor='white')
        
        # Добавление подписи к точке
        bmi_text = f'Ваш ИМТ: {bmi:.2f}' if bmi <= 40 else f'Ваш ИМТ: {bmi:.2f} (максимум)'
        ax.text(x_pos + 0.1, display_bmi, bmi_text, 
                ha='left', va='center', 
                color='red', fontweight='bold')
        
        # Настройка внешнего вида графика
        ax.set_xlim(-0.5, len(bmi_ranges)-0.7)  # Установка пределов по X
        ax.set_ylim(0, 40)  # Установка пределов по Y
        ax.set_xlabel('Диапазоны ИМТ', fontweight='bold', fontsize=12)  # Подпись оси X
        ax.set_ylabel('Значения ИМТ', fontweight='bold', fontsize=12)  # Подпись оси Y
        ax.set_title('Диаграмма ИМТ', fontweight='bold', pad=15, fontsize=14)  # Заголовок графика
        
        # Настройка сетки и границ
        ax.grid(axis='y', linestyle='--', alpha=0.7, color='gray')  # Добавление сетки
        ax.set_xticks([])  # Удаление меток по оси X
        
        # Добавление горизонтальных линий, разделяющих диапазоны
        for i in range(1, len(bmi_ranges)-1):
            ax.axhline(y=bmi_ranges[i], color='black', linestyle='-', linewidth=1, alpha=0.7)
        
        # Настройка фона и легенды
        ax.set_facecolor('#F5F5F5')  # Установка цвета фона
        ax.legend(['Ваш ИМТ'], loc='lower right')  # Добавление легенды
        
        # Оптимизация отображения
        self.figure.tight_layout()  # Автоматическая настройка расположения элементов
        self.canvas.draw()  # Обновление отображения графика

if __name__ == '__main__':
    # Создание и запуск приложения
    app = QApplication(sys.argv)  # Создание объекта приложения
    window = BMICalculator()  # Создание главного окна
    window.show()  # Отображение окна
    sys.exit(app.exec_())  # Запуск главного цикла приложения 