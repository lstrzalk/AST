
class Node(object):

    def __str__(self):
        return self.printTree()


class BinExpr(Node):

    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Const(Node):
    def __init__(self,value):
        self.value=value

class Integer(Const):
    pass
    #...


class Float(Const):
    pass
    #...


class String(Const):
    pass
    #...


class Variable(Node):
    pass
    #...

class Program(Node):
    def __init__(self,declarations,fundefs_opt,intructions):
        self.declarations=declarations
        self.fundefs_opt=fundefs_opt
        self.instructions=intructions
class DeclarationsList(Node):
    def __init__(self):
        self.declarations=[]
    def addDecl(self,decl):
        self.declarations.append(decl)
class Declaration(Node):
    def __init__(self,type,inits):
        self.type=type
        self.inits=inits
class Inits(Node):
    def __init__(self):
        self.inits=[]
    def addInit(self,init):
        self.inits.append(init)
class Init(Node):
    def __init__(self,id,expression):
        self.id=id
        self.expression=expression
class Instructions_opt(Node):
    def __init__(self,instructions):
        self.instructions=instructions
class InstructionsList(Node):
    def __init__(self):
        self.instructions=[]
    def addInstr(self,instruction):
        self.instructions.append(instruction)
class PrintInstruction(Node):
    def __init__(self,instr):
        self.instr=instr
class LabeledInstruction(Node):
    def __init__(self,id,instruction):
        self.id=id
        self.instruction=instruction
class Assigment(Node):
    def __init__(self,id,expr):
        self.id=id
        self.expr=expr
class ChoiceInstruction(Node):
    def __init__(self,condition,instruction,alternative):
        self.condition=condition
        self.instruction=instruction
        self.alternative=alternative
class WhileInstruction(Node):
    def __init__(self,condition,instruction):
        self.condition=condition
        self.instruction=instruction
class RepeatInstruction(Node):
    def __init__(self,instruction,condition):
        self.instruction=instruction
        self.consition=condition
class ReturnInstruction(Node):
    def __init__(self,expression):
        self.expression=expression
class ContinueInstruction(Node):
    pass
class BreakInstruction(Node):
    pass
class CompoundInstruction(Node):
    def __init__(self,declarations,instructions_opt):
        self.declarations=declarations
        self.instructions_opt=instructions_opt
class FunctionCalling(Node):
    def __init__(self,name,args):
        self.name=name
        self.args=args
class BracketsExpression(Node):
    def __init__(self,expr):
        self.expr=expr
class Expressions(Node):
    def __init__(self):
        self.expressions=[]
    def addExpression(self,expression):
        self.expressions.append(expression)
class FunDefs_opt(Node):
    def __init__(self,fundefs):
        self.fundefs=fundefs
class FunDefs(Node):
    def __init__(self):
        self.fundefs=[]
    def addFunDef(self,fundef):
        self.fundefs.append(fundef)
class FunDef(Node):
    def __init__(self,type,id,args,comp):
        self.type=type
        self.id=id
        self.args=args
        self.comp=comp
class ArgsList(Node):
    def __init__(self):
        self.args=[]
    def addArg(self,arg):
        self.args.append(arg)
class Arg(Node):
    def __init__(self,type,id):
        self.type=type
        self.id=id

