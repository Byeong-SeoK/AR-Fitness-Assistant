from works import working
from exercise import exercising

def main():
    # works일때, exercise일때 조건문
    # 작업 중 일시
    while True:

        num = int(input("works이면 1, exercise이면 2, 전체 종료 3:"))

        # working일때
        if num ==1:
            working()

        # exercising일때
        elif num ==2:
            exercising()

        elif num ==3:
            print("프로그램 종료")
            break

        else:
            print("잘못된 입력입니다.")




if __name__ == "__main__":
    main()