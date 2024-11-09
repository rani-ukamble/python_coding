# Assignment 36:

# In a fair coin we have an equal chance (50%) of either getting a „head‟ or „tail‟. That is if we toss the coin a large number of times we 
# would observe head approximately 50% of the time. Write a program to implement a biased coin toss where the chance of getting a 
# head is 70% (and tail 30%). That is if we invoke the program 1000 times we should see the head randomly approximately 700 times.


import random

def biased_coin_toss():
    # Generate a random number between 0 and 1
    toss = random.random()
    
    # Print for debugging purposes
    # print(f"Random number generated: {toss}")
    
    # 70% chance for head
    if toss < 0.7:
        return 'Head'
    else:
        return 'Tail'

# Function to simulate the biased coin toss multiple times
def simulate_tosses(num_tosses):
    heads_count = 0
    tails_count = 0
    
    for i in range(num_tosses):
        result = biased_coin_toss()
        if result == 'Head':
            heads_count += 1
        else:
            tails_count += 1
    
    return heads_count, tails_count


if __name__ == "__main__":
# Simulate the toss 1000 times
    num_tosses = 1000
    heads, tails = simulate_tosses(num_tosses)

# Print results
    print(f"Out of {num_tosses} tosses:")
    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
