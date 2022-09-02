n = int(input())

for k in range(1,n+1):
    total_possible_positions = k*k # number of available positions on the board
    total_possible_ways = (total_possible_positions*(total_possible_positions-1))//2 # total ways of selecting two positions

    if k>2:
        # https://math.stackexchange.com/questions/3266257/number-of-ways-two-knights-can-be-placed-such-that-they-dont-attack

        '''
        for two knights to be attacking each other, they must be within a 2x3 or 3x2 box, and for each box, there are two arrangements of the knights. Number of 2x3 boxes = (n-1)(n-2), since the top left of the box can be placed anywhere in a (n-1)X(n-2) matrix
        Number of 3x2 boxes = (n-2)(n-1)
        Thus total boxes = 2*(n-1)(n-2) and since there are two arrangements of the knights, multiply by two again.
        '''

        total_possible_ways -= 4*(k-1)*(k-2) # check out the above link for the reason for the formula used

    print(total_possible_ways)