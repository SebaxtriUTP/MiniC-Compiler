'''
cast.py

Estructura del árbol de síntaxis abstracto
'''
#from ast import Str
from dataclasses import *
from typing import Any, List
#from unicodedata import name
from multimethod import multimeta

#---------------------------------------------------------------
#clases abstractas
#---------------------------------------------------------------

@dataclass
class Visitor(metaclass=multimeta): #clase abstracta para el visitor es una clase que tiene un metodo visit para cada clase de nodo
    pass


#################################################
@dataclass
class Node(): #clase abstracta para los nodos
    def accept(self, vis: Visitor): #no son punteros como en C
        return vis.visit(self)

@dataclass
class Statement(Node): #clase abstracta para los nodos de declaracion
    pass

@dataclass
class Expression(Node): #clase abstracta para los nodos de expresion
    pass

@dataclass
class Declaration(Statement): #clase abstracta para los nodos de declaracion
    pass

#---------------------------------------------------------------
#  Nodos del Tipo Declaration, son Statement especiales que declaran la existencia de algo
#---------------------------------------------------------------
@dataclass
class ClassDeclaration(Declaration):  #clase que declara una clase
    name   : str
    sclass : str
    methods: List[Statement] = field(default_factory=list)


@dataclass
class FuncDeclaration(Declaration): #clase que declara una funcion
    name   : str
    parameters: List[Expression] = field(default_factory=list)
    stmts  : List[Statement] = field(default_factory=list)

@dataclass
class VarDeclaration(Declaration): #clase que declara una variable
    name   : str
    expr   : Expression


#---------------------------------------------------------------
# Statement representan acciones sin valores asociados
#---------------------------------------------------------------

@dataclass
class Program(Statement): #clase que representa un programa
    decl   : List[Statement] = field(default_factory=list)

@dataclass
class Print(Statement): #clase que representa un print
    expr   : Expression

@dataclass
class MFUNC(Expression):
    name   : str
    value  : Expression

@dataclass
class IfStmt(Statement): #clase que representa un if
    cond   : Expression
    cons   : List [Statement]=field(default_factory=list) #el consecuente
    altr   : List [Statement]=field(default_factory=list)

@dataclass
class WhileStmt(Statement): #clase que representa un while
    
    cond  : Expression
    body  : List[Statement]=field(default_factory=list)
    in_loop: bool = True

@dataclass
class ForStmt(Statement): #clase que representa un for
    for_init : Expression # inicializacion
    for_cond : Expression # condicion
    for_increment : Expression # incremento
    for_body : List[Statement]=field(default_factory=list)

@dataclass
class Return(Statement): #clase que representa un return
    expr  : Expression

@dataclass
class ExprStmt(Statement): #clase que representa una expresion
    expr  : Expression

@dataclass
class Block(Statement): #clase que representa un bloque
    stmts :  List[Statement] = field(default_factory=list)

#---------------------------------------------------------------
# Expression representan valores
#---------------------------------------------------------------

@dataclass
class Literal(Expression): #clase que representa un literal
    #todo lo de primary
    value  : Any

@dataclass #clase que representa una variable
class Binary(Expression): #tiene un hijo izquierdo y un hijo derecho, o sea, suma, resta, multiplicación y división
    op     : str
    left   : Expression
    right  : Expression


@dataclass
class Logical(Expression):
    op     : str            # <, <=, >, >=, ==, !=, && , ||
    left   : Expression
    right  : Expression


@dataclass
class Unary(Expression):
    op     : str           # -, !
    expr   : Expression

@dataclass
class Grouping(Expression): # no es obligatorio
    expr  : Expression


@dataclass
class Variable(Expression):
    name   : str

@dataclass
class Assign(Expression):
    op     : str        # =, +=, -=, *=, /=
    name   : str
    expr   : Expression


#intento de hacer el ultimo punto de la tarea
@dataclass
class AssignArray(Expression):
    name   : str
    index  : Expression
    expr   : Expression

@dataclass
class Call(Expression):
    func  : Expression
    args  : List[Expression]=field(default_factory=list)


@dataclass
class Set(Expression):
    obj   : str
    name  : str
    expr  : Expression


@dataclass
class Get(Expression):
    obj   : str
    name  : str


@dataclass
class Super(Expression):
    name   : str

@dataclass
class List(Expression):
    name   : str

@dataclass
class This(Expression):
    pass

#---------------------------------------------------------------
#---------------------------------------------------------------

#más aelante usaremos el Visitor para imprimir el AST de forma bonita usando tree.py
#repositorio de rich en github, el archivo tree

@dataclass
class ContinueStmt(Statement):
    "una sentencia continue para el for"
    pass

@dataclass
class BreakStmt(Statement):
    "una sentencia break para el for"
    pass


@dataclass
class PostExp(Expression):
    op     : str            
    name   : str
    expr   : Expression

@dataclass
class PreExp(Expression):
    op     : str            
    name   : str
    expr   : Expression

@dataclass
class Format(Expression):
    format : Expression