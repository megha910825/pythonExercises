total_blocks = int(input("Enter the number of blocks: "))

used_blocks = 0
current_row_blocks = 0
rows = 0

# A while loop running for used_blocks up to total_blocks
while used_blocks <= total_blocks:
    # Set blocks per row to 0 to start building new row
    blocks_per_row = 0
    # A while loop for building each row
    while blocks_per_row <= current_row_blocks:
        # Increment the blocks per row by 1
        blocks_per_row += 1
        # Print an asterisk to visualise the code
        print("*", end="")
    # Increment the rows and print a newline to visualise next row
    rows += 1
    print("\n")

    # Set current_row_blocks to the blocks used inside the nested loop
    current_row_blocks = blocks_per_row
    # Increment used_blocks by the amount of blocks in the current row
    used_blocks += current_row_blocks

    future_row = current_row_blocks + 1
    # Break if the future row needs more blocks than the total
    if used_blocks + future_row > total_blocks:
        break


print("The rows of the pyramid:", rows)