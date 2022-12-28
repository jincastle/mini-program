def isLeapYear(year): # 윤년 boolean
    return year % 4 ==0 and year % 100 !=0 or year % 400 == 0

def lastDay(year, month): # 마지막 날짜 리턴
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    m[1] = 29 if isLeapYear(year) else 28

    return m[month - 1]

def totalDay(year, month, day): # 1년 1월 1일 부터 지난 날짜의 합계
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400

    for i in range(1, month):
        total += lastDay(year, i)
    return total + day

    # 인수로 년, 월, 일을 넘겨받아 요일을 계산해 숫자로 리턴하는 함수
    # 일요일(0), 월요일(1), 화요일(2), 수요일(3), 목요일(4), 금요일(5), 토요일(6)
def weekDay(year, month, day):
    return totalDay(year, month, day) % 7

if __name__ == "__main__":
    year, month = map(int, input('달력을 출력할 년, 월을 입력하세요 : ').split())
    print('=' * 28)
    print('         {0:4d}년{1:2d}월'.format(year, month))
    print('=' * 28)
    print(' 일   월   화   수   목   금   토 ')
    print('=' * 28) # 여기까진 달력의 윗부분

    for i in range(weekDay(year, month,1)): # 1쓰기전에 앞부분띄우기
        print('    ', end='') #

    for i in range(1, lastDay(year,month)+1): # 마지막 날짜
        print(' {0:2d} '.format(i), end = '')

        if weekDay(year, month, i) == 6 and i!=lastDay(year,month):
            print()

    print('\n' + '=' * 28)