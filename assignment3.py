def calculate_stats(numbers):

    total_sum = sum(numbers)
    

    average = total_sum / len(numbers) if numbers else 0
    
  
    largest_number = max(numbers) if numbers else None
    

    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Largest Number: {largest_number}")


numbers = [4, 30, 70, 100, 5000]  
calculate_stats(numbers)


