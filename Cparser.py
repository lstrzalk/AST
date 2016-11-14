#!/usr/bin/python

from scanner import Scanner
import AST


class Cparser(object):
    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()

    tokens = Scanner.tokens

    precedence = (
        ("nonassoc", 'IFX'),
        ("nonassoc", 'ELSE'),
        ("right", '='),
        ("left", 'OR'),
        ("left", 'AND'),
        ("left", '|'),
        ("left", '^'),
        ("left", '&'),
        ("nonassoc", '<', '>', 'EQ', 'NEQ', 'LE', 'GE'),
        ("left", 'SHL', 'SHR'),
        ("left", '+', '-'),
        ("left", '*', '/', '%'),
    )

    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno,
                                                                                      self.scanner.find_tok_column(p),
                                                                                      p.type, p.value))
        else:
            print("Unexpected end of input")

    # DONE
    def p_program(self, p):
        """program : declarations fundefs_opt instructions_opt"""
        declarations = p[1]
        fundefs_opt = p[2]
        instructions_opt = p[3]
        p[0] = AST.Program(declarations, fundefs_opt, instructions_opt)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_declarations(self, p):
        """declarations : declarations declaration
                        | """
        if len(p) == 3:
            if p[1] is None:
                p[0] = AST.DeclarationsList()
            else:
                p[0] = p[1]
            p[0].addDecl(p[2])
        else:
            p[0] = AST.DeclarationsList()

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_declaration(self, p):
        """declaration : TYPE inits ';'
                       | error ';' """
        if len(p) == 4:
            type = p[1]
            inits = p[2]
            p[0] = AST.Declaration(type, inits)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_inits(self, p):
        """inits : inits ',' init
                 | init """
        if len(p) == 4:
            if p[1] is None:
                p[0] = AST.Inits()
            else:
                p[0] = p[1]
            p[0].addInit(p[3])
        else:
            p[0] = AST.Inits()
            p[0].addInit(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_init(self, p):
        """init : ID '=' expression """
        id = p[1]
        expression = p[3]
        p[0] = AST.Init(id, expression)
        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_instructions_opt(self, p):
        """instructions_opt : instructions
                            | """
        if p[1] is not None:
            p[0] = AST.Instructions_opt(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_instructions(self, p):
        """instructions : instructions instruction
                        | instruction """
        if len(p) == 3:
            if p[1] is None:
                p[0] = AST.InstructionsList()
            else:
                p[0] = p[1]
            p[0].addInstr(p[2])
        else:
            p[0] = AST.InstructionsList()
            p[0].addInstr(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_instruction(self, p):
        """instruction : print_instr
                       | labeled_instr
                       | assignment
                       | choice_instr
                       | while_instr
                       | repeat_instr
                       | return_instr
                       | break_instr
                       | continue_instr
                       | compound_instr
                       | expression ';' """
        p[0] = p[1]

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_print_instr(self, p):
        """print_instr : PRINT expr_list ';'
                       | PRINT error ';' """
        expr_list = p[2]
        p[0] = AST.PrintInstruction(expr_list)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_labeled_instr(self, p):
        """labeled_instr : ID ':' instruction """
        id = p[1]
        instruction = p[3]
        p[0] = AST.LabeledInstruction(id, instruction)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_assignment(self, p):
        """assignment : ID '=' expression ';' """
        id = p[1]
        expression = p[3]
        p[0] = AST.Assigment(id, expression)
        p[0].lineno = self.scanner.lexer.lineno

    # ?
    def p_choice_instr(self, p):
        """choice_instr : IF '(' condition ')' instruction  %prec IFX
                        | IF '(' condition ')' instruction ELSE instruction
                        | IF '(' error ')' instruction  %prec IFX
                        | IF '(' error ')' instruction ELSE instruction """
        condition = p[3]
        instruction = p[5]
        if len(p) == 8:
            alternativeInstruction = p[7]
        else:
            alternativeInstruction = None
        p[0] = AST.ChoiceInstruction(condition, instruction, alternativeInstruction)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_while_instr(self, p):
        """while_instr : WHILE '(' condition ')' instruction
                       | WHILE '(' error ')' instruction """
        condition = p[3]
        instruction = p[5]
        p[0] = AST.WhileInstruction(condition, instruction)

        p[0].lineno = self.scanner.lexer.lineno

    # ?
    def p_repeat_instr(self, p):
        """repeat_instr : REPEAT instructions UNTIL condition ';' """
        instructions = p[2]
        condition = p[4]
        p[0] = AST.RepeatInstruction(instructions, condition)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_return_instr(self, p):
        """return_instr : RETURN expression ';' """
        expression = p[2]
        p[0] = AST.ReturnInstruction(expression)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_continue_instr(self, p):
        """continue_instr : CONTINUE ';' """
        p[0] = AST.ContinueInstruction()

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_break_instr(self, p):
        """break_instr : BREAK ';' """
        p[0] = AST.BreakInstruction()

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_compound_instr(self, p):
        """compound_instr : '{' declarations instructions_opt '}' """
        declarations = p[2]
        instructions_opt = p[3]
        p[0] = AST.CompoundInstruction(declarations, instructions_opt)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_condition(self, p):
        """condition : expression"""
        p[0] = p[1]
        p[0].lineno = self.scanner.lexer.lineno

    # ?
    def p_const(self, p):
        """const : INTEGER
                 | FLOAT
                 | STRING"""
        p[0] = AST.Const(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_expression(self, p):
        """expression : const
                      | ID
                      | expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression
                      | expression '%' expression
                      | expression '|' expression
                      | expression '&' expression
                      | expression '^' expression
                      | expression AND expression
                      | expression OR expression
                      | expression SHL expression
                      | expression SHR expression
                      | expression EQ expression
                      | expression NEQ expression
                      | expression '>' expression
                      | expression '<' expression
                      | expression LE expression
                      | expression GE expression
                      | '(' expression ')'
                      | '(' error ')'
                      | ID '(' expr_list_or_empty ')'
                      | ID '(' error ')' """
        if len(p) == 2:
            if isinstance(p[1], AST.Const):
                value = p[1]
            else:
                value = AST.Id(p[1])
            p[0] = value
        elif p[1] is '(':
            p[0] = p[2]
        elif p[2] is '(' and p[1] is not '(':
            name = p[1]
            args = p[3]
            p[0] = AST.FunctionCalling(name, args)
        else:
            firstExpr = p[1]
            secExpr = p[3]
            operator = p[2]
            p[0] = AST.BinExpr(operator, firstExpr, secExpr)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_expr_list_or_empty(self, p):
        """expr_list_or_empty : expr_list
                              | """
        if len(p) == 1:
            p[0] = None
        else:
            p[0] = p[1]

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_expr_list(self, p):
        """expr_list : expr_list ',' expression
                     | expression """
        if len(p) == 4:
            if p[1] is None:
                p[0] = AST.Expressions
            else:
                p[0] = p[1]
            p[0].addExpression(p[3])
        else:
            p[0] = AST.Expressions()
            p[0].addExpression(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_fundefs_opt(self, p):
        """fundefs_opt : fundefs
                       | """
        if p[1] is not None:
            fundefs = p[1]
            p[0] = AST.FunDefs_opt(fundefs)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_fundefs(self, p):
        """fundefs : fundefs fundef
                   | fundef """
        if len(p) == 3:
            if p[1] is None:
                p[0] = AST.FunDefs()
            else:
                p[0] = p[1]
            p[0].addFunDef(p[2])
        else:
            p[0] = AST.FunDefs()
            p[0].addFunDef(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_fundef(self, p):
        """fundef : TYPE ID '(' args_list_or_empty ')' compound_instr """
        type = p[1]
        id = p[2]
        args = p[4]
        comp = p[6]
        p[0] = AST.FunDef(type, id, args, comp)

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_args_list_or_empty(self, p):
        """args_list_or_empty : args_list
                              | """
        if len(p) == 1:
            p[0] = None
        else:
            p[0] = p[1]

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_args_list(self, p):
        """args_list : args_list ',' arg
                     | arg """
        if len(p) == 4:
            if p[1] is None:
                p[0] = AST.ArgsList()
            else:
                p[0] = p[1]
            p[0].addArg(p[3])
        else:
            p[0] = AST.ArgsList()
            p[0].addArg(p[1])

        p[0].lineno = self.scanner.lexer.lineno

    # DONE
    def p_arg(self, p):
        """arg : TYPE ID """
        type = p[1]
        id = p[2]
        p[0] = AST.Arg(type, id)

        p[0].lineno = self.scanner.lexer.lineno
