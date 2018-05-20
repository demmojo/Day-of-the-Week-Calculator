from data_dict import month_dict_2, day_dict
from input_data import user_input
from calculate_day import calculate_day

if __name__ == '__main__':
    while True:
        day, month, year = user_input()
        day_calc = calculate_day(day, month, year)
        print(month_dict_2[str(month)], day + ', ', year, 'is on a', day_dict[str(day_calc)] + '.')

        # Continue code until terminated by user
        print('Would you like to continue? Type n and press Enter to stop')
        yes_no = input()
        if yes_no == 'n':
            print('Goodbye!')
            break

