# 외부로부터 vidid_list를 받아 DATASET을 생성.
# 파라미터로 vidid_list, 저장할 경로, 저장할 filename을 받는다.

import os
import time as t


def print_log(string) :
    print("{} : {}".format(t.strftime('%x %X', t.localtime(t.time())), string))    


def dataset_savior(vidid_list, folder, filename, extension) :

    truefoleder = "./" + folder + "/"

    # 없으면 생성
    if not os.path.exists(truefoleder):
        os.makedirs(truefoleder)

    # 모든 vidid에 대해
    for i, vidid in enumerate(vidid_list) :
        
        # vidid로 ccparser에서 받아오기
        
        # 경로에 저장
        path = truefoleder + filename + str(i+1) + extension
        with open(path, 'w', encoding='utf-8') as file:
            file.write("this is file {}.".format(i+1))
        print_log("FILE {} SAVED.".format(i+1))
        



if __name__ == "__main__" :
    
    # INIT VARS.
    FOLDER = "./faufau/"
    FILENAME = "fau"
    EXTENSION = ".txt"

    # 없으면 생성
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    # 경로에 저장
    for i in range(5) :
        path = FOLDER + FILENAME + str(i+1) + EXTENSION
        with open(path, 'w', encoding='utf-8') as f:
            f.write("this is file {}.".format(i+1))
        print("FILE {} SAVED.".format(i+1))
