# Constants
REGISTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]
MEMORY_SIZE = 1024

# Variables
memory = [0] * MEMORY_SIZE # Initializes memory with 0's
registers = {reg: 0 for reg in REGISTERS} # Initializes registers with 0's
registers["PC"] = 0 # Initializes program counter to 0
registers["CR"] = False # Initializes comparison register to False
labels = {} # Initializes dictionary to hold label addresses
variables = {} #Initializes dictionary to hold variable addresses
halt = False # Initializes halt flag to False

# define functions for each mnemonic
def mnemonic_move(params):
    set_value(params[0], get_value(params[1]))
    return True

def mnemonic_add(params):
    set_value(params[0], get_location_value(params[0]) + get_value(params[1]) )
    return True


def mnemonic_subt(params):
    set_value(params[0], get_location_value(params[0]) - get_value(params[1]) )
    return True


def mnemonic_mult(params):
    set_value(params[0], get_location_value(params[0]) * get_value(params[1]) )
    return True


def mnemonic_div(params):
    set_value(params[0], get_location_value(params[0]) // get_value(params[1]) )
    return True


def mnemonic_jump(params):
    registers["PC"] = int(params[0])
    return False


def mnemonic_cmp(params):
    value1 = get_location_value(params[0])
    value2 = get_value(params[1])
    registers["CR"] = value1 == value2
    return True


def mnemonic_cmajor(params):
    value1 = get_location_value(params[0])
    value2 = get_value(params[1])
    registers["CR"] = value1 > value2
    return True


def mnemonic_cminor(params):
    value1 = get_location_value(params[0])
    value2 = get_value(params[1])
    registers["CR"] = value1 < value2
    return True


def mnemonic_jtrue(params):
    if registers["CR"]:
        registers["PC"] = int(params[0])
        return False
    else:
        return True


def mnemonic_jfalse(params):
    if not registers["CR"]:
        registers["PC"] = int(params[0])-1
        return False
    else:
        return True


def mnemonic_int1(params):
    value = ord(input("Enter a character: "))
    set_value(params[1], value)
    return True


def mnemonic_int2(params):
    value = chr(get_location_value(params[1]))
    print(value, end="")
    return True


def mnemonic_var(params):
    variables[params[0]] = get_value(params[1])
    return True


def mnemonic_halt(params):
    global halt
    halt = True
    return True


# define the mapping of mnemonics to functions
mnemonic_functions = {
    "MOVE": mnemonic_move,
    "ADD": mnemonic_add,
    "SUBT": mnemonic_subt,
    "MULT": mnemonic_mult,
    "DIV": mnemonic_div,
    "JUMP": mnemonic_jump,
    "CMP": mnemonic_cmp,
    "CMAIOR": mnemonic_cmajor,
    "CMENOR": mnemonic_cminor,
    "JTRUE": mnemonic_jtrue,
    "JFALSE": mnemonic_jfalse,
    "INT": {"1": mnemonic_int1, "2": mnemonic_int2},
    "VAR": mnemonic_var,
    "HALT": mnemonic_halt
}


# Functions
def read_program(file_name):
    """Reads the program from a file and returns a list of lines."""
    with open(file_name) as file:
        return file.readlines()


def remove_comments(program):
    """Removes comments from program lines and returns cleaned program as a string."""
    cleaned_program = []

    cleaned_line = program.split('--')[0].strip()

    if cleaned_line:
        cleaned_program.append(cleaned_line)
    return '\n'.join(cleaned_program)


def parse_instruction(line):
    """Parses a single program line and returns the label, mnemonic, and parameters as a tuple."""

    line = remove_comments(line)
    parts = line.strip().split(" ")
    label = None
    mnemonic = None
    params = []

    for i, part in enumerate(parts):
        if part.endswith(":"):
            label = part[:-1]
        elif not mnemonic:
            mnemonic = part
        else:
            params.append(part)

    return label, mnemonic, params[:2]


def clean_up_program(program):
    """Cleans up the program by removing comments and labels, and replacing label references with their addresses."""
    cleaned_lines = []
    labels = {}

    for i, line in enumerate(program):
        # Ignore empty lines
        if not line.strip():
            continue

        # Parse the instruction
        label, mnemonic, params = parse_instruction(line)

        if label:
            # This is a label, add it to the dictionary
            labels[label] = i
        
        if mnemonic:
            # This is a mnemonic with parameters
            cleaned_params = [p.replace(",", "") for p in params]
            cleaned_lines.append((mnemonic, cleaned_params))

    cleaned_program = []
    for mnemonic, params in cleaned_lines:
        # Replace label references with their addresses
        for label, address in labels.items():
            for i in range(len(params)):
                params[i] = params[i].replace(label, str(address))

        cleaned_program.append((mnemonic, params))

    return cleaned_program


def execute_mnemonic(mnemonic, params):
    """Executes a mnemonic with the given parameters and returns
    True if execution should continue or False if it should halt."""

    # call the function for the given mnemonic
    try:
        function = mnemonic_functions[mnemonic]
    except KeyError:
        raise ValueError(f"Invalid mnemonic: {mnemonic}")

    if mnemonic == "INT":
        return function[params[0]](params)
    else:
        return function(params)


def get_value(param):
    """Returns the value of a parameter."""
    if is_register(param):
        return registers[param]
    elif is_variable(param):
        return memory[variables[param]]
    else:
        return int(param)


def get_location_value(param):
    """Returns the location of a parameter."""
    if is_register(param):
        return registers[param]
    elif is_memory_address(param):
        return memory[get_memory_address(param)]


def set_value(param, value):
    """Set the value of a parameter."""
    if is_register(param):
        registers[param] = value
    elif is_memory_address(param):
        memory[get_memory_address(param)] = value


def is_memory_address(param):
    """Returns True if the parameter is a valid memory address or label."""
    if param in labels:
        return True
    elif is_variable(param):
        return True
    else:
        try:
            address = int(param)
            return 0 <= address < MEMORY_SIZE
        except ValueError:
            return False


def get_memory_address(param):
    """Returns the memory address of a parameter."""
    if param in labels:
        return labels[param]
    elif is_variable(param):
        return variables[param]
    else:
        return int(param)


def is_register(param):
    """Returns True if the parameter is a valid register."""
    return param in REGISTERS

def is_variable(param):
    """Returns True if the parameter is a valid variable."""
    return param in variables