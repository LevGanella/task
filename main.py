from games.hok import play_hok
from games.geomprog import play_geomprog

def run_game(game):
    game()

def main():
    print("Выберите игру:")
    print("1 - Наименьшее общее кратное (НОК)")
    print("2 - Геометрическая прогрессия")

    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        run_game(play_hok)
    elif choice == '2':
        run_game(play_geomprog)
    else:
        print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
