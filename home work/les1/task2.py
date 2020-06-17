seconds = input("Введите случайно количество секунд\n")
seconds = int(seconds)
hours = seconds // (60*60)
seconds %= (60*60)
minutes = seconds // 60
seconds %= 60
print(f'{hours:02}:{minutes:02}:{seconds:.2f}')