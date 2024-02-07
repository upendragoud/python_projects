missionaries_on_right = 3
cannibals_on_right = 3
boat_side = 'Right'
missionaries_on_left = 0
cannibals_on_left = 0

print(f'missionaries_on_right:{missionaries_on_right}, cannibals_on_right:{cannibals_on_right}, boat_side:{boat_side}, '
      f'missionaries_on_left:{missionaries_on_left}, cannibals_on_left:{cannibals_on_left}')
while True:
    if boat_side == 'Right':
        cannibals, missionaries = list(map(int, input('select C / M: ').split()))
        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals
        boat_side = 'Left'
        missionaries_on_left += missionaries
        cannibals_on_left += cannibals
        print(
            f'missionaries_on_left:{missionaries_on_left}, cannibals_on_left:{cannibals_on_left}, boat_side:{boat_side}, '
            f'missionaries_on_right:{missionaries_on_right}, cannibals_on_right:{cannibals_on_right}')
        if missionaries_on_left == 3 and cannibals_on_left == 3 and missionaries_on_right == 0 and cannibals_on_right == 0:
            print('You succeeded')
            break
        elif (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
            print('Better luck next time')
            break

    elif boat_side == 'Left':

        cannibals, missionaries = list(map(int, input('select C / M: ').split()))
        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        boat_side = 'Right'
        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals
        print(
            f'missionaries_on_right:{missionaries_on_right}, caribbans_on_right:{cannibals_on_right}, '
            f'boat_side:{boat_side}, missionaries_on_left:{missionaries_on_left}, caribbans_on_left:{cannibals_on_left}')
        if missionaries_on_left == 3 and cannibals_on_left == 3 and missionaries_on_right == 0 and cannibals_on_right == 0:
            print('You succeeded')
            break

        elif (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (
                missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):

            print('Better luck next time')

            break

"""
key:[[1 1], [0 1], [2 0], [1 0], [0 2], [1 1], [0 2], [1 0], [2 0], [1 0], [2 0]]
"""