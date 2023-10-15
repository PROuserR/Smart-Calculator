import sympy
from widgets import *


lines = 1
is_showed_symbols = True
is_showed_functions = True


def submit():
    txt_output.configure(state='normal')
    exprs = txt_output.get('1.0', tk.END)

    if '=' in exprs:
        solve()
    elif '<' in exprs or '>' in exprs or '≥' in exprs or '≤' in exprs:
        solve_inequality()
    else:
        if sympy.sympify(process_txt()[0]).is_Number or '°' in exprs:
            calculate()
        else:
            plot()
    txt_output.config(state='disabled')


def calculate():
    txt_output.config(state='normal')
    expr = process_txt()[0]
    try:
        txt_output.insert(tk.END, f'\n{round(float(sympy.sympify(expr)), 2)}')
    except:
        txt_output.insert(tk.END, f'\n{sympy.sympify(expr)}')
    txt_output.config(state='disabled')


def solve():
    txt_output.config(state='normal')

    exprs = process_txt()

    if len(exprs) == 1:
        solutions = sympy.solve(sympy.sympify(exprs[0]), dict=True)
    if len(exprs) == 2:
        solutions = sympy.solve((sympy.sympify(exprs[0]), sympy.sympify(exprs[1])), dict=True)

    for solution in solutions:
        txt_output.insert(tk.END, f'\n{solution}')

    txt_output.config(state='disabled')


def solve_inequality():
    txt_output.config(state='normal')

    expr = process_txt()[0]

    symbol = [symbol for symbol in sympy.solve(expr[0], dict=True)[0].items()][0][0]
    solution = [symbol for symbol in sympy.solve(expr[0], dict=True)[0].items()][0][1]

    txt_output.insert(tk.END, f'\n{symbol}{expr[1]}{solution}')

    txt_output.config(state='disabled')


def plot():
    txt_output.config(state='normal')
        
    exprs = process_txt()


    if lines == 1:
        sympy.plot(sympy.sympify(exprs[0]), title=str(exprs[0]), xlabel='x', ylabel='f(x)')
    if lines == 2:
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]),title='2 Lines' , xlabel='x', ylabel='f(x)')
    if lines == 3:
        sympy.plot(sympy.sympify(exprs[0]), sympy.sympify(exprs[1]), sympy.sympify(exprs[2]),title='Lines' , xlabel='x', ylabel='f(x)')
    txt_output.config(state='disabled')


def expand():
    txt_output.config(state='normal')
    expr = process_txt()[0]

    expr = sympy.sympify(expr)
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{expr.expand()}')
    txt_output.config(state='disabled')


def factor():
    txt_output.config(state='normal')
    expr = process_txt()[0]

    expr = sympy.sympify(expr)
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{expr.factor()}')
    txt_output.config(state='disabled')


def remove():
    txt_output.config(state='normal')
    txt_output.delete('end-2c', tk.END)
    txt_output.config(state='disabled')


# This function will find the index of the last digit after char ex: √
def digit_index(expr:str, char):
    
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
    right_parentheses = expr.index('(')
    left_parentheses = expr.index(')')


    if 'pi' not in expr:
        for char in expr[right_parentheses + 1:left_parentheses]:
            if char.isalpha():
                return True
    return False


def add_star(expr):
    for i in range(len(expr)):
        if expr[i].isdigit() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
            expr = expr[:i+1] + '*' + expr[i+1:]
        if expr[i].isalpha() and expr[i + 1].isalpha()  and expr[i+1] != '°' or expr[i] == ')' and expr[i+1] == '(' and expr[i+1] != '°':
            expr = expr[:i+1] + '*' + expr[i+1:]
    return expr


def process_txt():
    exprs = []
    for i in range(1, lines + 1):
        expr = txt_output.get(f'{i}.0', f'{i+1}.0')
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


def insert_new_line():
    txt_output.config(state='normal')
    global lines
    lines += 1
    txt_output.insert(tk.END, '\n')
    txt_output.config(state='disabled')


def insert_abs():
    txt_output.config(state='normal')
    output = txt_output.get('1.0', tk.END)
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{abs(int(output))}')
    txt_output.config(state='disabled')


def insert_limit():
    txt_output.config(state='normal')
    expr = process_txt()[0]
    value = ent_limit_value.get()
    value = value.replace('∞', str(sympy.S.Infinity))
    limit = sympy.Limit(sympy.sympify(expr), sympy.Symbol('x'), sympy.sympify(value)).doit()
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{limit}')
    txt_output.config(state='disabled')


def insert_derivative():
    txt_output.config(state='normal')
    expr = process_txt()[0]
    d = sympy.Derivative(sympy.sympify(expr), sympy.Symbol('x')).doit()
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{d}')
    txt_output.config(state='disabled')


def insert_integral():
    txt_output.config(state='normal')
    expr = process_txt()[0]
    i = sympy.Integral(sympy.sympify(expr), sympy.Symbol('x')).doit()
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{i}')
    txt_output.config(state='disabled')


def insert_summation():
    txt_output.config(state='normal')
    expr = process_txt()[0]
    x = sympy.Symbol('x')
    summation = sympy.summation(sympy.sympify(expr), (x, sympy.sympify(ent_summation_start.get()), sympy.sympify(ent_summation_n.get())))
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', f'\n{summation}')
    txt_output.config(state='disabled')   


def insert_letter(letter):
    txt_output.config(state='normal')
    txt_output.insert(f'{lines}.{len(txt_output.get(str(lines) + ".0", tk.END))}', letter)
    txt_output.config(state='disabled')


def clear_txt():
    txt_output.config(state='normal')
    txt_output.delete('1.0', tk.END)
    txt_output.config(state='disabled')


def show_symbols():
    global is_showed_symbols
    if is_showed_symbols:
        frm_symbols.pack()
        frm_standard.pack_forget()
        frm_sci.pack_forget()

    else:
        frm_standard.pack()
        frm_symbols.pack_forget()
        frm_sci.pack_forget()
        
    is_showed_symbols = not is_showed_symbols


def show_functions():
    global is_showed_functions
    if is_showed_functions:
        frm_standard.pack_forget()
        frm_symbols.pack_forget()
        frm_sci.pack()

    else:
        frm_standard.pack()
        frm_sci.pack_forget()
        frm_symbols.pack_forget()
    is_showed_functions = not is_showed_functions

