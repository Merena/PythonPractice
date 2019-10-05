import calendar
import locale

cal = calendar.month(2019, 10)
print(cal)

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')
cal = calendar.month(2019, 10)
print(cal)

locale.setlocale(locale.LC_ALL, '')

cal = calendar.calendar(2019)
print(cal)