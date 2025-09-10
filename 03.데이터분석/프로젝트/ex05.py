import os
import pandas as pd
file_score = 'data/학생성적.csv'
file_info = 'data/학생정보.csv'

def submenu():
    while True:
        score = pd.read_csv(file_score)
        info = pd.read_csv(file_info)
        merge = pd.merge(score, info, how='right', on='지원번호')
        merge.fillna(0)
        cols = merge.columns
        merge.ser_index('지원번호', inplace = True)
        cols = merge.columns
        idxs = merge.index
        os.system('cls')
        print('-' * 50)
        print('**********성적관리*********')
        print('-' * 50)
        print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
        print('-' * 50)
        menu = input('메뉴선택>')
        if menu == '0':
            print('프로그램 종료')
            break
        elif menu == '1':
            input('아무키나 누르시오')
        elif menu == '2':
            for idx in idxs:
                for col in cols:
                    row = merge.loc[idx]
                    print(f'{col}:{row[col]}', end=' ')
                print()
                print('-' * 60)
            input('아무키나 누르시오')
        elif menu == '3':
            input('아무키나 누르시오')
        elif menu == '4':
            input('아무키나 누르시오')
        elif menu == '5':
            input('아무키나 누르시오')
        else:
            input('0~5를 입력하시오')



if __name__ == '__main__':
    submenu()