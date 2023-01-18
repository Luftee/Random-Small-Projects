def inputCheck(item):
    inputStr = input(item)

    if len(inputStr) != 4:
        quit()
    if int(inputStr) > 2359:
        quit()
    if int(str(inputStr)[-2:]) >= 60:
        quit()

    inputArray = [int(str(inputStr)[:-2]), int(str(inputStr)[-2:])]
    return inputArray

def main():
    oldZone = inputCheck('Original timezone: ')
    oldTime = inputCheck('Original time: ')
    newZone = inputCheck('New timezone: ')

    newTimeHour = oldTime[0] - oldZone[0] + newZone[0]
    newTimeMinute = oldTime[1] - oldZone[1] + newZone[1]
    newTime = [newTimeHour, newTimeMinute]
    
    if newTime[1] >= 60:
        newTime = [newTime[0] + 1, newTime[1] - 60]
    if int(f'{newTime[0]}{newTime[1]}') > 2359:
        newTime[0] = newTime[0] - 24

    for i in newTime:
        if int(newTime[i]) < 10:
            newTime[i] = f'0{newTime[i]}'

    print(f'\nNew time: {newTime[0]}{newTime[1]}')

if __name__ == '__main__':
    main()