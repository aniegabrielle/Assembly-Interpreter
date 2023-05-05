# import the interpreter module
import interpreter


# define the main function
def main():

    command = input("Enter a command: ")

    # specify the file containing the program to run
    program_file = command + ".txt"

    # read the program from the file
    program = interpreter.read_program(program_file)
    # clean up the program by removing comments and blank lines, and replacing labels with their corresponding line

    cleaned_program = interpreter.clean_up_program(program)

    # loop until the program halts or the end of the program is reached
    while not interpreter.halt and interpreter.registers["PC"] < len(cleaned_program):
        # fetch the next instruction from the program
        mnemonic, params = cleaned_program[interpreter.registers["PC"]]

        # execute the instruction
        execution = interpreter.execute_mnemonic(mnemonic, params)

        # execute the instruction
        if execution:
            # increment the program counter
            interpreter.registers["PC"] += 1

    # print the contents of the registers after the program has completed
    print("")
    print("Registers:")
    for reg, value in interpreter.registers.items():
        print(f"{reg}: {value}")

    # print the contents of the variables after the program has completed
    print("Variables:")
    for var, value in interpreter.variables.items():
        print(f"{var}: {interpreter.memory[value]}")


# if this module is being run directly, call the main function
if __name__ == "__main__":
    main()
