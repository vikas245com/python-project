start = int(input("Enter starting number : "))
end = int(input("Enter ending number : ")) 
even_count = 0
even_sum = 0
odd_count = 0
odd_sum = 0
for num in range(start , end + 1):
    if num % 2 == 0:
        even_count += 1
        even_sum += num 
    else:
        odd_count += 1
        odd_sum += num 
print("-" * 35)
print(f"even numbers count = {even_count} , sum = {even_sum}")
print(f"odd numbers count = {odd_count} , sum = {odd_sum}") 