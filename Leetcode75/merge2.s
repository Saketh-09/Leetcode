.data
# A - Original list
# list - Sorted List

A:     .space 128
list:  .space 128

size_prompt:  .asciiz "Enter the number of values - "
inp_prompt:   .asciiz "Enter value - "
SL_prompt:    .asciiz "After merge sort - : "
new_line:     .asciiz "\n"
space_prompt: .asciiz " "


.text
.globl main

main:
  # Take keyboard input from the user for the number of elements in the list (i.e., n)

  li   $v0, 4           # set $v0 = 4 for printing string
  la   $a0, size_prompt  # set the address of size_prompt to $a0
  syscall

  li   $v0, 5           # set $v0 to 5 (service code for reading an integer)
  syscall
  move $s0, $v0         # move the value stored in $v0 register to $s0

  # Load Addresses of Original List -> A and Sorted List -> list
  la   $s1, A
  la   $s2, list

  addi $t0, $zero, 0    # set i = 0 (index of A)
  addi $t1, $s1, 0      # $t1 = Addr. of A (copy Addr. of A into $t1 temporarily)

  # Input loop: get integers from the user and store them in the array A
  inp_loop:
    slt $t2, $t0, $s0      # if i < n, then set $t2 = 1
    beq $t2, $zero, inp_done  # if $t2 = 0, then jump to inp_done

    li  $v0, 4            # set $v0 = 4 for printing string
    la  $a0, inp_prompt   # set the address of inp_prompt to $a0
    syscall

    li  $v0, 5            # set $v0 to 5 (service code for reading an integer)
    syscall
    sw  $v0, 0($t1)        # store input value stored in $v0 into A[i]

    addi $t0, $t0, 1      # i = i + 1
    addi $t1, $t1, 4      # Move to the next Addr. of A ie &A[i+1]
    j inp_loop

  inp_done:
    addi $s3, $zero, 2      # Initializing window size = 2

  while1:
    slt $t0, $s0, $s3        # if window size > n, then set $t0 = 1
    bne $t0, $zero, exit1    # if $t0 = 1 or window size > n, then jump to exit1

    addi $s4, $zero, 0        # Initialize st = 0
    addi $s6, $s0, -1         # $s6 = n - 1
    addi $t0, $s3, -1         # $t0 = size - 1
    add $s5, $s4, $t0         # Initialize end = st + (size - 1)

  while2:
    slt $t0, $s6, $s5         # if end > (n - 1), then set $t0 = 1
    bne $t0, $zero, exit2     # if $t0 = 1 or end > (n - 1), then jump to exit2

    # Set input params before calling the merge function
    addi $a0, $s1, 0           # Setting $a0 = Addr. of A before calling merge
    addi $a1, $s4, 0           # Setting $a1 = st before calling merge
    addi $a2, $s5, 0           # Setting $a2 = end before calling merge
    addi $a3, $s2, 0           # Setting $a3 = Addr. of list before calling merge

    # call merge function
    jal merge

    add $s4, $s4, $s3          # st = st + size
    add $s5, $s5, $s3          # end = end + size
    j while2                   # jump unconditionally to label while2

  exit2:
    # copy elements from list to A
    addi $t0, $zero, 0         # initialize i = 0 (list index)

  copy_loop:
    slt $t1, $t0, $s0          # if i < n, then set $t1 = 1
    beq $t1, $zero, copy_done   # if i >= n, then jump to copy_done

    sll $t2, $t0, 2            # $t2 = 4 * i
    add $t3, $s2, $t2          # $t3 = Addr of list + 4i
    lw $t3, 0($t3)             # $t3 = list[i]

    add $t4, $s1, $t2          # $t4 = Addr of A + 4i
    sw $t3, 0($t4)             # store A[i] = list[i]

    addi $t0, $t0, 1           # i = i + 1
    j copy_loop                # jump unconditionally to label copy_loop

  copy_done:
    sll $s3, $s3, 1            # window size = (window size) * 2
    j while1                   # jump unconditionally to label while1

  exit1:
    # print the final sorted array
    li $v0, 4                  # set $v0 = 4 for printing string

    la $a0, new_line           # set the address of new_line to $a0
    syscall

    la $a0, SL_prompt          # set the address of SL_prompt to $a0
    syscall

  print_loop:
    beq $s0, 0, main_exit       # if n = 0, then jump to main_exit

    li $v0, 1                   # set $v0 = 1 for printing integer
    lw $a0, 0($s2)              # set the address of $s2 with offset 0 to $a0 -> to print $s2
    syscall

    li $v0, 4                   # set $v0 = 4 for printing string
    la $a0, space_prompt        # set the address of space_prompt to $a0
    syscall

    addi $s2, $s2, 4            # $s2 = $s2 + 4 (moving to the next element in the sorted list)
    addi $s0, $s0, -1           # n = n - 1

    j print_loop                # jump unconditionally to label print_loop

  main_exit:
    # exit
    li $v0, 10                  # set service code = 10 in $v0 for terminating execution
    syscall                     # terminate execution

merge:
  # Merges two sorted sub-lists A and B into one final sorted list...

  # Arguments => $a0 = Addr. of A, $a1 = st, $a2 = end, $a3 = Addr. of list

  # preserving all saved registers used here ->
  # $s0 -> mid = (st + end)/2

  addi $sp, $sp, -4            # make room on the stack for 1 register
  sw $s0, 0($sp)               # save $s0 on the stack

  # set mid ($s0) = (st + end)/2
  add $s0, $a1, $a2            # $s0 = (st + end)
  srl $s0, $s0, 1              # $s0 = (st + end)/2

  # list A -> i = st to i = mid
  # list B -> j = mid+1 to i = end

  addi $t0, $a1, 0             # i = st      (list A index)
  addi $t1, $s0, 1             # j = mid + 1 (list B index)

  sll $t5, $a1, 2              # $t5 = 4 * st
  add $t5, $a3, $t5            # $t5 = Addr of list[st]

  whileAB:
    slt $t2, $s0, $t0          # if i > mid, then set $t2 = 1
    bne $t2, $zero, whileB     # if i > mid, then jump to whileB
    slt $t3, $a2, $t1          # if j > end, then set $t3 = 1
    bne $t3, $zero, whileA     # if j > end, then jump to whileA

  if:
    sll $t2, $t0, 2            # $t2 = 4 * i
    add $t2, $a0, $t2          # $t2 = Addr of A + 4i
    lw $t2, 0($t2)             # $t2 = A[i]
    sll $t3, $t1, 2            # $t3 = 4 * j
    add $t3, $a0, $t3          # $t3 = Addr of A + 4j
    lw $t3, 0($t3)             # $t3 = A[j]

    slt $t4, $t2, $t3          # if A[i] < A[j], then set $t4 = 1
    beq $t4, $zero, else       # if A[i] >= A[j], then jump to else

    sw $t2, 0($t5)             # store list[k] = A[i]
    addi $t0, $t0, 1           # i = i + 1
    j whileAB_end              # jump to whileAB_end without going to else

  else:
    sw $t3, 0($t5)             # store list[k] = A[j]
    addi $t1, $t1, 1           # j = j + 1

  whileAB_end:
    addi $t5, $t5, 4           # $t5 = Addr of list[k+1]
    j whileAB                   # loop whileAB again

  whileA:
    slt $t2, $s0, $t0          # if i > mid, then set $t2 = 1
    bne $t2, $zero, exit       # if i > mid, then jump to exit

    sll $t2, $t0, 2            # $t2 = 4 * i
    add $t2, $a0, $t2          # $t2 = Addr of A + 4i
    lw $t2, 0($t2)             # $t2 = A[i]

    sw $t2, 0($t5)             # store list[k] = A[i]

    addi $t0, $t0, 1           # i = i + 1
    addi $t5, $t5, 4           # $t5 = Addr of list[k+1]
    j whileA                   # loop whileA again

  whileB:
    slt $t3, $a2, $t1          # if j > end, then set $t3 = 1
    bne $t3, $zero, exit       # if j > end, then jump to exit

    sll $t3, $t1, 2            # $t3 = 4 * j
    add $t3, $a0, $t3          # $t3 = Addr of A + 4j
    lw $t3, 0($t3)             # $t3 = A[j]

    sw $t3, 0($t5)             # store list[k] = A[j]

    addi $t1, $t1, 1           # j = j + 1
    addi $t5, $t5, 4           # $t5 = Addr of list[k+1]
    j whileB                   # loop whileB again

  exit:
    lw $s0, 0($sp)              # restore $s0 from the stack
    addi $sp, $sp, 4            # restore the stack pointer
    jr $ra                      # return