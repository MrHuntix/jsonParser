import json
from sympy.solvers import solve
from sympy import Symbol
import re

#A parser class that parses a particular json file to return appropriate outputs
class Parser:
    symbols={'add':'+','subtract':'-','multiply':'*','divide':'=','equal':'='}
    operators=['+','-','*','/','=']
    expr=""
    infix=""
    
    def __init__(self,fileName):
        with open(fileName, encoding='utf-8') as data_file:
            self.data = json.loads(data_file.read())

    #function to display the contents of json file
    def disp_json(self):
        print(self.data)

    #helper function to parse the nested json key
    def parse_lhs(self,lhsSide):
        op = ''
        op += Parser.symbols[lhsSide['op']] + ' '

        lhs = ""
        if (isinstance(lhsSide['lhs'], dict)):
            lhs += self.parse_lhs(lhsSide['lhs'])
        else:
            lhs += str(lhsSide['lhs']) + ' '

        rhs = ""
        if (isinstance(lhsSide['rhs'], dict)):
            rhs += self.parse_lhs(lhsSide['rhs'])
        else:
            rhs += str(lhsSide['rhs']) + ' '

        return op + lhs + rhs

    #JSON to prefix converter
    def get_prefix(self):
        op = Parser.symbols[self.data['op']]
        lhs=self.parse_lhs(self.data['lhs'])
        rhs=str(self.data['rhs'])
        self.expr=op+' '+lhs+rhs

    #output after going through the json file. This output is used to generate the resulting infix expression.
    def print_prefix(self):
        print('Prefix expression:\n',self.expr,'\n')
        
    #prefix expression to infix expression
    def get_infix(self):
        self.get_prefix()    
        stack=[]
        temp_list=self.expr.split(' ')
        n=len(temp_list)-1
        while n>=0:
            e_char=temp_list[n]
            if e_char not in Parser.operators:
                stack.append(e_char)
            else:
                a1=str(stack.pop())
                a2=str(stack.pop())
                if e_char=='=':
                    stack.append(a1 +' '+ e_char +' '+ a2)
                else:
                    stack.append('( ' + a1 +' '+ e_char +' '+ a2 + ' )')
            n-=1
        self.infix=stack.pop()
        temp=self.infix.split('=')
        temp[0]=temp[0][1:-2]
        self.infix=temp[0].strip()+' ='+temp[1]
        return self.infix

    #function to calculate x
    def get_x(self):
        x=Symbol('x')
        new_expr=self.infix.split('=')
        new_expr=new_expr[0]+' - '+new_expr[1]
        new_expr=solve(new_expr,x)
        if len(new_expr)==1:
            print('x = ',new_expr[0])
        else:
            print('x = +|-',new_expr[0])
                  
