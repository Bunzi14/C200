#Bob takes 5min/per pizza
#tom takes 2min/per pizza
#sue takes 1min/per pizza

Bob = 5
Tom = 2
Sue = 1

def pizzaTime(t, n):
    total_time = t * n 
    return total_time

#individual times 
print(pizzaTime(Bob, 5))
print(pizzaTime(Tom, 3))
print(pizzaTime(Sue, 2))

#total time 
print(pizzaTime(Bob, 5) + pizzaTime(Tom, 3) + pizzaTime(Sue, 2))