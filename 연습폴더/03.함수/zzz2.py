from function import menuPrint,inputNum
sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

def insert():
    codes=[]
    for s in sale:
        codes.append(s['code'])
        new_code = max(codes) +1

        print(f"상품코드>{new_code}")
        name = input('상품이름>')
        price = inputNum('상품가격')
        qnt = inputNum('판매수량')
        sale.append({'code': new_code, 'name':name, 'price':price, 'qnt':qnt})
        print('입력성공!')

def search(code):
    isFind = False
    for index, s in enumerate(sale):
        if s['code'] == code:
            isFind = True
            sum = s['price']*s['qnt']
            print(index, s['code'], s['name'], s['price'], s['qnt'], sum)
        if isFind == False:
            print("상품이 존재하지 않습니다.")
            return isFind 

while True:
    menuPrint('상품관리')
    menu = input('메뉴선택')
    if menu == "0":
        print('프로그램을 종료합니다.')
        break

    elif menu == "1":
        insert()

    elif menu == "2":
        code = inputNum('검색코드')
        search(code)

    elif menu == "3":
        

