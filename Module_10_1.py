import datetime
from time import sleep
from datetime import datetime
from threading import Thread

t_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i, j in enumerate(range(word_count)):
            file.write(f"Какое-то слово № {j + 1}\n")
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

thr_5 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_6 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_7 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_8 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_5.start()
thr_6.start()
thr_7.start()
thr_8.start()

thr_5.join()
thr_6.join()
thr_7.join()
thr_8.join()

t_final = datetime.now()
print(t_final - t_start)