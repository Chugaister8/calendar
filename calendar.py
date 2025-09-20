import calendar

# Словники для української локалізації
ukrainian_months = {
    1: "Січень",
    2: "Лютий",
    3: "Березень",
    4: "Квітень",
    5: "Травень",
    6: "Червень",
    7: "Липень",
    8: "Серпень",
    9: "Вересень",
    10: "Жовтень",
    11: "Листопад",
    12: "Грудень"
}

ukrainian_days = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя"
}

def print_month_calendar():
    try:
        # Запитуємо рік і місяць у користувача
        yy = int(input("Введіть рік (наприклад, 2025): "))
        mm = int(input("Введіть місяць (1-12): "))
        
        # Перевіряємо коректність введених даних
        if mm < 1 or mm > 12:
            print("Помилка: Місяць має бути від 1 до 12")
            return
            
        # Встановлюємо початок тижня з понеділка
        calendar.setfirstweekday(calendar.MONDAY)
        
        # Отримуємо текст календаря
        cal = calendar.month(yy, mm).splitlines()
        
        # Замінюємо назву місяця на українську
        cal[0] = f"  {ukrainian_months[mm]} {yy}"
        
        # Замінюємо скорочення днів тижня на українські
        cal[1] = "Пн Вт Ср Чт Пт Сб Нд"
        
        # Виводимо календар
        print(f"\nКалендар на {ukrainian_months[mm]} {yy} року:\n")
        for line in cal:
            print(line)
        
        # Додаємо додаткову інформацію
        print(f"\nЦей місяць має {calendar.monthrange(yy, mm)[1]} днів")
        print(f"Перший день місяця - {ukrainian_days[calendar.monthrange(yy, mm)[0]]}")

    except ValueError:
        print("Помилка: Будь ласка, введіть числові значення для року та місяця")

# Викликаємо функцію
if __name__ == "__main__":
    print_month_calendar()
    
    # Додаємо можливість повторити
    while True:
        again = input("\nБажаєте вивести календар для іншого місяця? (так/ні): ").lower()
        if again in ['так', 't', 'y', 'yes']:
            print_month_calendar()
        else:
            print("Дякуємо за використання програми!")
            break
