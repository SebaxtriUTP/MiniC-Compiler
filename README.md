# MiniC-Compiler
Este es un compilador para un subconjunto del lenguaje de programación C. Fue
escrito en Python durante noviembre del 2022.

El lexer y el analizador se construyeron usando PLY de Dave Beazley (Python
Lex-Yacc), una implementación Python de código abierto de GNU
lex/yacc. Etapas de compilación (generación del árbol de símbolos, tipo
control de flujo, control de flujo, etc.) se realizan utilizando un
patrón de diseño orientado a objetos llamado visitante (GoF 1995). La salida
es un interprete que trabaja sobre python

---------------------------------------------------------------
CARACTERISTICAS DEL LENGUAJE 
---------------------------------------------------------------

El subconjunto del lenguaje MC implementado aquí incluye:

    * Funciones, variables (local y global), y caracteres.

    * Assignments (=, +=, etc), estandar de aritmetica binaria y unary
      operatores (+,-,*, etc), logica binaria y operadores (!,
      ==, <, etc).


    * Control de flujo de bucles while y for,
      if/then/else condicional y recursion.

    * Incremento y decremento en pre-fijo/posfijo ++ , --



---------------------------------------------------------------
ARCHIVOS Y DIRECTORIOS
---------------------------------------------------------------

    lex.py       - Python Lex (this is part of PLY).
    yacc.py      - Python Yacc (this is part of PLY).
    clex.py      - Mini-C lexer.
    cparse.py    - Mini-C parser.  contiene yacc reglas para Mini-C y
                   define las clases para hacer el AST.
    cinterp.py   - Interprete para hacer que el minic funcione 
    mc.py        - Front-end del compilador.  este toma el comando-
                   con el nombre de los archivos
    Tests/       - Este guarda las pruebas en mini c .mc para probar con el compilador 

---------------------------------------------------------------
USING THE COMPILER
---------------------------------------------------------------

La sintaxis para usar el compilador mini-c es la siguiente:

    python mc.py <Tests/file.mc>

---------------------------------------------------------------
UNIVERSIDAD TECNOLOGICA DE PEREIRA 
---------------------------------------------------------------