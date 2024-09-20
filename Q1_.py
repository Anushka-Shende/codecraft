def reverse_stack(stack):
    if not stack:
        return
    
    # Step 1: Remove the top element
    top = stack.pop()
    
    # Step 2: Reverse the remaining stack
    reverse_stack(stack)
    
    # Step 3: Insert the top element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    # If stack is empty, push the item
    if not stack:
        stack.append(item)
        return
    
    # Step 1: Remove the top element
    top = stack.pop()
    
    # Step 2: Recursively insert the item at the bottom
    insert_at_bottom(stack, item)
    
    # Step 3: Push the top element back
    stack.append(top)

# Example usage
if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    reverse_stack(stack)
    print(stack)  # Output should be [5, 4, 3, 2, 1]
