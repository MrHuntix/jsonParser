# jsonParser
A json parser that generates an appropriate equation as described in a json file.  
  
Could not achieve the second goal i.e.  
Transform the expression so that you have ‘x’ on one side , and all the operations on the
other side. In this example, a transformed expression can be: x = (21 − 1) / 10  
You should then print this simplified expression

REQUIRES SYMPY:  
pip install sympy  
  
Steps to run:  
1> Clone or download repo.  
2> cd into the directory.  
3> run tester.py  

jsonParser.py contains Parser class.  
  
disp_json(): display the contents of json file  
parse_lhs(jsonObject): helper function to parse the nested json object  
get_prefix(): JSON to prefix converter  
print_prefix(): output after going through the json file. This output is used to generate the resulting infix expression  
get_infix(): converts prefix expression to infix expression  
get_x(): function to calculate x
