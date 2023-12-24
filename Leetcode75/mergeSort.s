# following code implements merge sort in bottom up appproach (iterative)

.data
inputArray:     .space 128
list:  .space 128
promptOne: .asciiz "Enter the size of array: "
promptTwo: .asciiz "Enter the array element: "
printNewLine: .asciiz "\n"
printSpace: .asciiz " "
prompt: .asciiz "Following are the elements of sorted array: "

.text
.globl main
main:

# user input for size
  li   $v0, 4
  la   $a0, promptOne
  syscall
  li   $v0, 5
  syscall
  # $s0 has size of array
  move $s0, $v0

  # load addresses of user input array & sorted array
  la   $s1, inputArray
  la   $s2, list
  # t0 has the current index & t1 has the current address of array
  addi $t0, $zero, 0
  addi $t1, $s1, 0

  # taking user input for elements of array
  arrayInput:
    slt $t2, $t0, $s0
    beq $t2, $zero, exitInput
    li  $v0, 4
    la  $a0, promptTwo
    syscall
    li  $v0, 5
    syscall
    # t1 has the address of current array element
    sw  $v0, 0($t1)

    addi $t0, $t0, 1
    addi $t1, $t1, 4
    j arrayInput

  exitInput:
    # initially sum of 2 sub arrays sizes is 2
    addi $s3, $zero, 2

  outerLoop:
    # if sum of 2 sub arrays sizes > n, then set $t0 = 1
    slt $t0, $s0, $s3
    # if $t0 = 1 or window size > n, then jump to exitOuterLoop
    bne $t0, $zero, exitOuterLoop

    addi $s4, $zero, 0
    addi $s6, $s0, -1
    addi $t0, $s3, -1
    add $s5, $s4, $t0

  innerLoop:
    slt $t0, $s6, $s5
    bne $t0, $zero, exitInnerLoop

    # Set input params before calling the merge function
    # initializing $a0 with address inputArray before calling merge
    addi $a0, $s1, 0
    # initializing $a1 with st before calling merge
    addi $a1, $s4, 0
    addi $a2, $s5, 0
    addi $a3, $s2, 0

    # calling the merge sub routine
    jal merge
    # st = st + size
    add $s4, $s4, $s3
    # end = end + size
    add $s5, $s5, $s3
    j innerLoop

  exitInnerLoop:
    # copy elements from list to inputArray
    addi $t0, $zero, 0

  copyMergedResult:
    slt $t1, $t0, $s0
    beq $t1, $zero, exitCopy

    sll $t2, $t0, 2
    add $t3, $s2, $t2
    lw $t3, 0($t3)

    add $t4, $s1, $t2
    sw $t3, 0($t4)

    addi $t0, $t0, 1
    j copyMergedResult

  exitCopy:
    sll $s3, $s3, 1
    j outerLoop

  exitOuterLoop:
    # print the final sorted array
    li $v0, 4

    la $a0, printNewLine
    syscall

    la $a0, prompt
    syscall

  printArray:
    beq $s0, 0, exitMergeSort

    li $v0, 1
    lw $a0, 0($s2)
    syscall

    li $v0, 4
    la $a0, printSpace
    syscall

    addi $s2, $s2, 4
    addi $s0, $s0, -1

    j printArray

  exitMergeSort:
    li $v0, 10
    syscall

merge:
  # merge sub routine to merge 2 sub arrays

  addi $sp, $sp, -4
  sw $s0, 0($sp)

  add $s0, $a1, $a2
  srl $s0, $s0, 1

  # list A -> i = st to i = mid
  # list B -> j = mid+1 to i = end

  addi $t0, $a1, 0
  addi $t1, $s0, 1

  sll $t5, $a1, 2
  add $t5, $a3, $t5

  loopOne:
    slt $t2, $s0, $t0
    bne $t2, $zero, loopTwo
    slt $t3, $a2, $t1          # if j > end, then set $t3 = 1
    bne $t3, $zero, loopThree     # if j > end, then jump to loopThree

  if:
    sll $t2, $t0, 2            # $t2 = 4 * i
    add $t2, $a0, $t2
    lw $t2, 0($t2)
    sll $t3, $t1, 2            # $t3 = 4 * j
    add $t3, $a0, $t3
    lw $t3, 0($t3)

    slt $t4, $t2, $t3
    beq $t4, $zero, else

    sw $t2, 0($t5)             # store list[k] = A[i]
    addi $t0, $t0, 1           # i = i + 1
    j exitLoopOne

  else:
    sw $t3, 0($t5)             # store list[k] = A[j]
    addi $t1, $t1, 1           # j = j + 1

  exitLoopOne:
    addi $t5, $t5, 4           # $t5 = Addr of list[k+1]
    j loopOne                   # loop loopOne again

  loopThree:
    slt $t2, $s0, $t0          # if i > mid, then set $t2 = 1
    bne $t2, $zero, exit       # if i > mid, then jump to exit

    sll $t2, $t0, 2            # $t2 = 4 * i
    add $t2, $a0, $t2          # $t2 = Addr of A + 4i
    lw $t2, 0($t2)

    sw $t2, 0($t5)             # store list[k] = A[i]

    addi $t0, $t0, 1           # i = i + 1
    addi $t5, $t5, 4
    j loopThree                   # loop loopThree again

  loopTwo:
    slt $t3, $a2, $t1          # if j > end, then set $t3 = 1
    bne $t3, $zero, exit       # if j > end, then jump to exit

    sll $t3, $t1, 2
    add $t3, $a0, $t3
    lw $t3, 0($t3)

    sw $t3, 0($t5)

    addi $t1, $t1, 1
    addi $t5, $t5, 4
    j loopTwo

  exit:
    lw $s0, 0($sp)
    addi $sp, $sp, 4
    jr $ra