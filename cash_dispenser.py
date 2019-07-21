# cash_dispenser gives out only hryvnia

# currency code

hryvnia = 1
usd = 2
euro = 3
ruble = 4
polish_zloty = 5



money = int(input("Введите сумму, которую вы хотите получить: "))
currency = int(input("Укажите валюту (hryvnia = 1, usd = 2, euro = 3, ruble = 4, polish_zloty = 5): "))

if currency == hryvnia:
    cash = str(round(money * 1, 3)) + "\tгрн"
    print("Валюта: гривна")
elif currency == usd:
    cash = str(round(money * 25.7, 3)) + "\tгрн"
    print("Валюта: долар США")
elif currency == euro:
    cash = str(round(money * 28.775, 3)) + "\tгрн"
    print("Валюта: евро")
elif currency == ruble:
    cash = str(round(money * 0.36, 3)) + "\tгрн"
    print("Валюта: рубель")
elif currency == polish_zloty:
    cash = str(round(money * 6.6, 3)) + "\tгрн"
    print("Валюта: польский злотый")
else:
    cash = 0
    print("Неизвестная валюта")

print("К получению:", cash)