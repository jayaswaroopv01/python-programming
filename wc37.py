print("1=vote")
print("2=against")
print("3=neutral")
vote=0
against=0
neutral=0
count=1
n=int(input("enter number of members:"))
while(count<=n):
    count=count+1
    opt=int(input("enter num of votes"))
    if opt==1:
        vote=vote+1
        print("you have voted")
    elif opt==2:
        against=against+1
        print("you are against")
    elif opt==3:
        neutral=neutral+1
        print("you are neutral")
    else:
        print("your entered option is invalid")
print("number of votes for vote",vote)
print("number of votes for against",against)
print("number of votes for neutral",neutral)
total_votes=vote+against+neutral
print("total number of people voted are=",total_votes)