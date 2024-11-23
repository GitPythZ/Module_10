import datetime
import time
import multiprocessing

files_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


def read_info_multi(*name):
    all_data = []
    my_str = ''
    for one_file in name:
        with open(one_file, 'r') as file:
            while True:
                line = file.readline()
                if line != '':
                    all_data.append(line)
                if not line:
                    break


def read_info_usual(name):
    all_data = []
    my_str = ''
    for one_file in name:
        with open(one_file, 'r') as file:
            while True:
                line = file.readline()
                if line != '':
                    all_data.append(line)
                if not line:
                    break


time_start = datetime.datetime.now()
read_info_usual(files_list)
time_end = datetime.datetime.now()
print(time_end - time_start)
# 0:00:06.336093


# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=8) as pool:
#         time_start = datetime.datetime.now()
#         pool.map(read_info_multi, files_list)
#     time_end = datetime.datetime.now()
#     print(time_end - time_start)
# 0:00:02.344728
