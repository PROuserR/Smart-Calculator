import sympy
from widgets import *


def submit():
    exprs = txt_box.get('1.0', tk.END)

    if '=' in exprs:
        compute('solve_equality')
    elif '<' in exprs or '>' in exprs or '≥' in exprs or '≤' in exprs:
        compute('solve_inequality')
    else:
        if has_symbol(exprs):
            plot_expression()
        else:
            compute('calculate_expression')


def plot_expression():
    exprs = process_input()

    if txt_box.index(tk.INSERT)[0] == '1':
        sympy.plot(sympy.sympify(exprs[0]), xlabel='x', ylabel='f(x)')
    if txt_box.index(tk.INSERT)[0] == '2':
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]), xlabel='x', ylabel='f(x)')
    if txt_box.index(tk.INSERT)[0] == '3':
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]), sympy.sympify(exprs[2]), xlabel='x', ylabel='f(x)')


# This function will find the index of the last digit after char ex: √
def digit_index(expr, char): 
	start_index = expr.index(char) + 1
	index = 0
	while True:
		if expr[start_index].isdigit() or expr[start_index].isalpha():
			index = start_index
		else:
			return index
		start_index += 1


#This functions will remove all terms to the left side and change their signs with the equal sign removed
def process_equation(equation):
	equal_index = equation.index('=')

	expr1 = sympy.sympify(equation[:equal_index])
	expr2 = sympy.sympify(equation[equal_index + 1:])
	return expr1 - expr2


#This functions will remove all terms to the left side and change their signs with the inequal sign removed
def process_inequality(inequality, char):
    inequality_index = inequality.index(char)
    expr1 = sympy.sympify(inequality[:inequality_index])
    expr2 = sympy.sympify(inequality[inequality_index + 1:])
    final_expr = expr1 - expr2
    coeff = int(final_expr.coeff([x for x in final_expr.free_symbols][0]))
    if coeff < 0:
        if char == '>':
            return final_expr, '<'
        elif char == '<':
            return final_expr, '>'
        elif char == '≥':
            return final_expr, '≤'
        elif char == '≤':
            return final_expr, '≥'
    else:
        return final_expr, char


def extract_numbers(expr):
	numbers = []
	for char in expr:
		if char.isdigit():
			numbers.append(char)
	return float(''.join(numbers))


def has_symbol(expr):
    try:
        right_parentheses = expr.index('(')
        left_parentheses = expr.index(')')


        if 'pi' not in expr:
            for char in expr[right_parentheses + 1:left_parentheses]:
                if char.isalpha():
                    return True
        return False
    except:
        for char in expr:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                return True
        return False


def add_star(expr):
    for i in range(len(expr)):
        if expr[i].isdigit() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
            expr = expr[:i+1] + '*' + expr[i+1:]
        if expr[i].isalpha() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
            if str(sympy.pi) not in expr:
                expr = expr[:i+1] + '*' + expr[i+1:]
    return expr


def process_input():
    exprs = []

    for i in range(1, int(txt_box.index(tk.INSERT)[0]) + 1):
        expr = txt_box.get(f'{i}.0', f'{i+1}.0')
        expr = expr.replace('Ⲡ', str(sympy.pi))
        expr = expr.replace('e', str(sympy.E))
        expr = expr.replace('²', '** 2 ')
        expr = expr.replace('³', '** 3 ')
        expr = add_star(expr)
        if '(' in expr and expr[0] != '(' and 'sin' not in expr and 'cos' not in expr and 'tan' not in expr and 'cot' not in expr:
            expr = expr.replace('(', '*(')
        if '√' in expr:
            square_root_index = digit_index(expr, '√') 
            expr = expr.replace('√', '')
            expr = expr[:square_root_index] + '** 0.5 ' + expr[square_root_index:]
        if '∛' in expr:
            cube_root_index = digit_index(expr, '∛')
            expr = expr.replace('∛', '')
            expr = expr[:cube_root_index] + '** (1/3) ' + expr[cube_root_index:]
        if '°' in expr:
            deg = extract_numbers(expr)
            func = expr[:3]
            expr = f'{func}({sympy.rad(deg)})'
        if '=' in expr:
            expr = process_equation(expr)

        if '>' in str(expr):
            expr = process_inequality(expr, '>')
        elif '≥' in str(expr):
            expr = process_inequality(expr, '≥')
        elif '<' in str(expr):
            expr = process_inequality(expr, '<')
        elif '≤' in str(expr):
            expr = process_inequality(expr, '≤')

        try:    
            i_index = expr.index('i')
            if expr[i_index - 1].isdigit():
                expr = expr.replace('i', 'j')
        except:
            pass

        exprs.append(expr)
    return exprs   


def compute(operation):
    txt_box.config(state='normal')
    expr = process_input()[0]

    if operation == 'calculate_expression':
        result = f'{round(float(sympy.sympify(expr)), 2)}'
    elif operation == 'solve_equality':
        exprs = process_input()
        solutions = None
        if len(exprs) == 1:
            solutions = sympy.solve(sympy.sympify(exprs[0]), dict=True)
        elif len(exprs) == 2:
            solutions = sympy.solve((sympy.sympify(exprs[0]), sympy.sympify(exprs[1])), dict=True)
        
        result = solutions
    elif operation == 'solve_inequality':
        symbol = [symbol for symbol in sympy.solve(expr[0], dict=True)[0].items()][0][0]
        solution = [symbol for symbol in sympy.solve(expr[0], dict=True)[0].items()][0][1]
        result = f'{symbol}{expr[1]}{solution}'
    elif operation == 'factor_expression':
        result = sympy.sympify(expr).factor()
    elif operation == 'expand_expression':
        result = sympy.sympify(expr).expand()
    elif operation == 'absolute':
        result = abs(int(sympy.sympify(expr)))    
    elif operation == 'limit':
        value = ent_limit_value.get()
        value = value.replace('∞', str(sympy.S.Infinity))
        limit = sympy.Limit(sympy.sympify(expr), sympy.Symbol('x'), sympy.sympify(value)).doit()
        result = limit
    elif operation == 'derivative':
        derivative = sympy.Derivative(sympy.sympify(expr), sympy.Symbol('x')).doit()
        result = derivative
    elif operation == 'integral':
        integral = sympy.Integral(sympy.sympify(expr), sympy.Symbol('x')).doit()
        result = integral
    elif operation == 'summation':
        x = sympy.Symbol('x')
        summation = sympy.summation(sympy.sympify(expr), (x, sympy.sympify(ent_summation_start.get()), sympy.sympify(ent_summation_n.get())))
        result = summation

    txt_box.insert(tk.END, f'\n{result}')
    txt_box.config(state='disabled')
 

def insert_btn_txt(btn):
    txt_box.config(state='normal')
    txt_box.insert(tk.END, btn['text'])
    txt_box.config(state='disabled')


def insert_new_line():
    txt_box.config(state='normal')
    txt_box.insert(tk.END, '\n')
    txt_box.config(state='disabled')


def remove_char():
    txt_box.config(state='normal')
    txt_box.delete('end-2c', tk.END)
    txt_box.config(state='disabled')


def clear_txt():
    txt_box.config(state='normal')
    txt_box.delete('1.0', tk.END)
    txt_box.config(state='disabled')


def show_symbols():
    if frm_symbols.winfo_ismapped():
        frm_standard.pack()
        frm_symbols.pack_forget()
        frm_sci.pack_forget()
    else:
        frm_symbols.pack()
        frm_standard.pack_forget()
        frm_sci.pack_forget() 


def show_functions():
    if frm_sci.winfo_ismapped():
        frm_standard.pack()
        frm_sci.pack_forget()
        frm_symbols.pack_forget()
    else:
        frm_standard.pack_forget()
        frm_symbols.pack_forget()
        frm_sci.pack()
