class Node(object):
    def __str__(self):
        return self.printTree()

# DONE
class Program(Node):
    def __init__(self, declarations, fundefs_opt, intructions):
        self.declarations = declarations
        self.fundefs_opt = fundefs_opt
        self.instructions = intructions

# DONE
class DeclarationsList(Node):
    def __init__(self):
        self.declarations = []
    def addDecl(self, decl):
        self.declarations.append(decl)

# DONE
class Declaration(Node):
    def __init__(self, type, inits):
        self.type = type
        self.inits = inits

# DONE
class Inits(Node):
    def __init__(self):
        self.inits = []
    def addInit(self, init):
        self.inits.append(init)

# DONE
class Init(Node):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

# DONE
class Instructions_opt(Node):
    def __init__(self, instructions):
        self.instructions = instructions

# DONE
class InstructionsList(Node):
    def __init__(self):
        self.instructions = []
    def addInstr(self, instruction):
        self.instructions.append(instruction)

# DONE
class PrintInstruction(Node):
    def __init__(self, expr_list):
        self.expr_list = expr_list

# DONE
class LabeledInstruction(Node):
    def __init__(self, id, instruction):
        self.id = id
        self.instruction = instruction

# DONE
class Assigment(Node):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

# ?
class ChoiceInstruction(Node):
    def __init__(self, condition, instruction, alternative):
        self.condition = condition
        self.instruction = instruction
        self.alternative = alternative

# DONE
class WhileInstruction(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

# ?
class RepeatInstruction(Node):
    def __init__(self, instructions, condition):
        self.instructions = instructions
        self.condition = condition

# DONE
class ReturnInstruction(Node):
    def __init__(self, expression):
        self.expression = expression

# DONE
class ContinueInstruction(Node):
    pass

# DONE
class BreakInstruction(Node):
    pass

# DONE
class CompoundInstruction(Node):
    def __init__(self, declarations, instructions_opt):
        self.declarations = declarations
        self.instructions_opt = instructions_opt

#DONE
class Const(Node):
    def __init__(self, value):
        self.value = value

# DONE
class Expressions(Node):
    def __init__(self):
        self.expressions = []
    def addExpression(self, expression):
        self.expressions.append(expression)

# DONE
class FunDefs_opt(Node):
    def __init__(self, fundefs):
        self.fundefs = fundefs

# DONE
class FunDefs(Node):
    def __init__(self):
        self.fundefs = []
    def addFunDef(self, fundef):
        self.fundefs.append(fundef)

# DONE
class FunDef(Node):
    def __init__(self, type, id, args, comp):
        self.type = type
        self.id = id
        self.args = args
        self.comp = comp

# DONE
class ArgsList(Node):
    def __init__(self):
        self.args = []
    def addArg(self, arg):
        self.args.append(arg)

# DONE
class Arg(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id

# DONE
class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

# DONE
class FunctionCalling(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

#DONE
class Id(Node):
    def __init__(self, id):
        self.id = id