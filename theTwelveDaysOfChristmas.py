giftList = ["partridge in a pear tree","turtle doves","french hens","calling birds","gold rings","geese a laying","swans a swimming","maids a milking","ladies dancing","lords of leaping","pipers piping","drummers drumming"]


def getIntFormated(inp): # convert int to string with correct suffix
    return "1st" if inp == 1 else "2nd" if inp == 2 else  "3rd" if inp ==3 else f"{inp}th"

for i in range(len(giftList)): # loop through the list of gifts for each day
    print(f"On the {getIntFormated(i+1)} day of Christmas my true love gave to me: ") # print the day of christmas
    print(*list(f"and a {giftList[0]}" if ii == 0 and i != 0 else f"A {giftList[0]}" if i == 0 else f"{ii+1} {giftList[ii]}" for ii in range(i,-1,-1))) 
    # Iterate through the list of gifts up to and including the current day in reverse. 
    # Then add the necessary formatting adding "and a", "A", or the number of the gift. 
    # Then print it out nicely.