import datetime as dt


def main():
    while True:
        try:
            user_input = input("Enter a year (or 'q' to quit): ").lower()

            if user_input.lower() == 'q':
                print("Goodbye!")
                break  # exits the while loop

            user_year = int(user_input)

            year = dt.datetime.today().year
            if year <= user_year or user_year < 1:
                raise ValueError

            print(year - user_year)

        except ValueError:
            print("Please enter a valid year")
        except KeyboardInterrupt:
            print("\nUser interrupted")
            break


if __name__ == "__main__":
    main()
