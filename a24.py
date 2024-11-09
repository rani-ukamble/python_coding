# Assignment 24:

# A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the 
# teacher rewards them with chocolates.
# Write a Python function to
# 1. Find the total number of chocolates received by all the children put together.
# Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each 
# child is stored in a list.
# 2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
#  If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", 
# should be displayed.
#  If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the 
# extra chocolates provided for the child must be added to his/her existing number of chocolates and 
# display the list containing the total number of chocolates received by each child.



def total_chocolates(children_ids, chocolates, id=None, extra_chocolates=0):
    print("Total chocolates = ", sum(chocolates)) 

    if id is not None:
        if id not in children_ids:
            print("Child id is invalid")
        elif extra_chocolates<1:
            print("Extra chocolates is less than 1") 
        else:
            index = children_ids.index(id)
            chocolates[index]+=extra_chocolates
            print(f"Updated chocolates: {chocolates}")
            
            
if __name__ == "__main__":
    children_ids = (101, 102, 103, 104, 105)
    chocolates = [10, 5, 8, 12, 15]

    total_chocolates(children_ids, chocolates)
    print("")                   # Case 1
    total_chocolates(children_ids, chocolates, 102, 3)           # Case 2
    print("") 
    total_chocolates(children_ids, chocolates, 999, 3)           # Case 3
    print("") 
    total_chocolates(children_ids, chocolates, 103, 0)           # Case 4
    print("") 
