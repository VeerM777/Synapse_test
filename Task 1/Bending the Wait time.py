# Taking input from the user
n=int(input("Enter the number of elements:"))
customers=[]
for i in range(0,n):
    arrival=int(input("enter the arrival time:"))
    time_required=int(input("enter the  time required:"))
    customers.append([arrival,time_required])
current_time=0
final=0


# loop to calculate the total waiting time
for arrival,time_required in customers:
    start_time=max(arrival,current_time)
    finishing_time=start_time+time_required
    total_time=finishing_time-arrival

    final=final+total_time
    current_time=finishing_time

average_time=final/len(customers)
print(f"The average time is {average_time}")




