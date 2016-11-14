import AST

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

class TreePrinter:
    # DONE
    @classmethod
    def printNode(cls, string, depth):
        print "| " * depth + string

    # DONE
    @addToClass(AST.Node)
    def printTree(self):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    # DONE
    @addToClass(AST.Program)
    def printTree(self, depth):
        self.declarations.printTree(depth)
        self.fundefs_opt.printTree(depth)
        self.instructions.printTree(depth)

    # DONE
    @addToClass(AST.DeclarationsList)
    def printTree(self, depth):
        for declaration in self.declarations:
            declaration.printTree(depth)

    # DONE
    @addToClass(AST.Declaration)
    def printTree(self, depth):
        TreePrinter.printNode("DECL", depth)
        self.inits.printTree(depth+1)

    # DONE
    @addToClass(AST.Inits)
    def printTree(self, depth):
        for init in self.inits:
            init.printTree(depth)

    # DONE
    @addToClass(AST.Init)
    def printTree(self, depth):
        TreePrinter.printNode("=", depth)
        TreePrinter.printNode(self.id, depth+1)
        self.expression.printTree(depth+1)

    # DONE
    @addToClass(AST.Instructions_opt)
    def printTree(self, depth):
        self.instructions.printTree(depth)

    # DONE
    @addToClass(AST.InstructionsList)
    def printTree(self, depth):
        for instruction in self.instructions:
            instruction.printTree(depth)

    # DONE
    @addToClass(AST.PrintInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("PRINT", depth)
        self.expr_list.printTree(depth+1)

    # DONE
    @addToClass(AST.LabeledInstruction)
    def printTree(self, depth):
        TreePrinter.printNode(self.id + ":", depth)
        self.instruction.printTree(depth)

    # DONE
    @addToClass(AST.Assigment)
    def printTree(self, depth):
        TreePrinter.printNode("=", depth)
        TreePrinter.printNode(self.id, depth+1)
        self.expression.printTree(depth+1)

    # DONE
    @addToClass(AST.ChoiceInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("IF", depth)
        self.condition.printTree(depth+1)
        self.instruction.printTree(depth+1)
        if self.alternative is not None:
            TreePrinter.printNode("ELSE", depth)
            self.alternative.printTree(depth+1)

    # DONE
    @addToClass(AST.WhileInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("WHILE", depth)
        self.condition.printTree(depth+1)
        self.instruction.printTree(depth+1)

    # DONE
    @addToClass(AST.RepeatInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("REPEAT", depth)
        self.instruction.printTree(depth+1)
        TreePrinter.printNode("UNTIL", depth)
        self.condition.printTree(depth+1)

    # DONE
    @addToClass(AST.ReturnInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("RETURN", depth)
        self.expression.printTree(depth+1)

    # DONE
    @addToClass(AST.ContinueInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("CONTINUE", depth)

    # DONE
    @addToClass(AST.BreakInstruction)
    def printTree(self, depth):
        TreePrinter.printNode("BREAK", depth)

    # DONE
    @addToClass(AST.CompoundInstruction)
    def printTree(self, depth):
        self.declarations.printTree(depth)
        self.instructions_opt.printTree(depth)

    # DONE
    @addToClass(AST.Const)
    def printTree(self, depth):
        TreePrinter.printNode(self.value, depth)

    # DONE
    @addToClass(AST.Expressions)
    def printTree(self, depth):
        for expression in self.expressions:
            expression.printTree(depth)

    # DONE
    @addToClass(AST.FunDefs_opt)
    def printTree(self, depth):
        self.fundefs.printTree(depth)

    # DONE
    @addToClass(AST.FunDefs)
    def printTree(self, depth):
        for fundef in self.fundefs:
            fundef.printTree(depth)

    # DONE
    @addToClass(AST.FunDef)
    def printTree(self, depth):
        TreePrinter.printNode("FUNDEF", depth)
        TreePrinter.printNode(self.id, depth+1)
        TreePrinter.printNode("RET " + self.type, depth+1)
        self.args.printTree(depth+1)
        self.comp.printTree(depth+1)

    # DONE
    @addToClass(AST.ArgsList)
    def printTree(self, depth):
        for arg in self.args:
            arg.printTree(depth)

    # DONE
    @addToClass(AST.Arg)
    def printTree(self, depth):
        TreePrinter.printNode("ARG " + self.id, depth)

    # DONE
    @addToClass(AST.BinExpr)
    def printTree(self, depth):
        TreePrinter.printNode(self.op, depth)
        self.left.printTree(depth + 1)
        self.right.printTree(depth + 1)

    # DONE
    @addToClass(AST.FunctionCalling)
    def printTree(self, depth):
        TreePrinter.printNode("FUNCALL", depth)
        TreePrinter.printNode(self.name, depth+1)
        self.args.printTree(depth+1)

    # DONE
    @addToClass(AST.Id)
    def printTree(self, depth):
        TreePrinter.printNode(self.id, depth)