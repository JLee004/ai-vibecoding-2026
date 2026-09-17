"""2단부터 9단까지 출력하거나, 선택한 단만 출력하는 구구단 프로그램."""


def print_table(dan: int) -> None:
    """입력받은 단의 구구단을 출력한다."""
    print(f"\n[{dan}단]")
    for number in range(1, 10):
        print(f"{dan} x {number} = {dan * number}")


def main() -> None:
    choice = input("출력할 단을 입력하세요 (2~9, Enter: 전체 출력): ").strip()

    if not choice:
        for dan in range(2, 10):
            print_table(dan)
        return

    if not choice.isdigit() or not 2 <= int(choice) <= 9:
        print("2부터 9 사이의 숫자를 입력하세요.")
        return

    print_table(int(choice))


if __name__ == "__main__":
    main()

