import tkinter as tk


# Define Widgets
win = tk.Tk()
win.title('Smart Calculator')

frm_output = tk.Frame()
frm_nav_buttons = tk.Frame()
frm_standard = tk.LabelFrame(text='Standard')
frm_abc = tk.LabelFrame(text='Symbols')

frm_sci = tk.LabelFrame(text='Sci')
frm_trig = tk.Frame(master=frm_sci)
frm_inequality = tk.Frame(master=frm_sci)
frm_expand_factor = tk.Frame(master=frm_sci)
frm_other_sci = tk.Frame(master=frm_sci)
frm_log = tk.Frame(master=frm_sci)

frm_limit = tk.Frame(master=frm_sci)
frm_summation = tk.Frame(master=frm_sci)

lbl_expression = tk.Label(master=frm_output, text='Expression goes here:')
txt_output = tk.Text(master=frm_output, width=35, height=8, state='disabled')
ent_base = tk.Entry(master=frm_log, width=2)
ent_limit_value = tk.Entry(master=frm_limit, width=2)
ent_summation_start = tk.Entry(master=frm_summation, width=2)
ent_summation_n = tk.Entry(master=frm_summation, width=2)

deg_type_choice = tk.IntVar()

btn_zero = tk.Button(master=frm_standard, text='0', bg='white')
btn_one = tk.Button(master=frm_standard, text='1', bg='white')
btn_two = tk.Button(master=frm_standard, text='2', bg='white')
btn_three = tk.Button(master=frm_standard, text='3', bg='white')
btn_four = tk.Button(master=frm_standard, text='4', bg='white')
btn_five = tk.Button(master=frm_standard, text='5', bg='white')
btn_six = tk.Button(master=frm_standard, text='6', bg='white')
btn_seven = tk.Button(master=frm_standard, text='7', bg='white')
btn_eight = tk.Button(master=frm_standard, text='8', bg='white')
btn_nine = tk.Button(master=frm_standard, text='9', bg='white')

btn_equal = tk.Button(master=frm_standard, text='=')
btn_dot = tk.Button(master=frm_standard, text='.')
btn_plus = tk.Button(master=frm_standard, text='+')
btn_minus = tk.Button(master=frm_standard, text='-')
btn_multiply = tk.Button(master=frm_standard, text='*')
btn_divide = tk.Button(master=frm_standard, text='/')

btn_parentheses_right = tk.Button(master=frm_standard, text='(')
btn_parentheses_left = tk.Button(master=frm_standard, text=')')
btn_square_root = tk.Button(master=frm_standard, text='√')
btn_square = tk.Button(master=frm_standard, text='²')
btn_cube_root = tk.Button(master=frm_standard, text='∛')
btn_cube = tk.Button(master=frm_standard, text='³')
btn_x = tk.Button(master=frm_standard, text='x')
btn_pi = tk.Button(master=frm_standard, text='Ⲡ')


btn_sin = tk.Button(master=frm_trig, text='sin')
btn_cos = tk.Button(master=frm_trig, text='cos')
btn_tan = tk.Button(master=frm_trig, text='tan')
btn_cot = tk.Button(master=frm_trig, text='cot')
btn_degree = tk.Button(master=frm_trig, text='°')

btn_expand = tk.Button(master=frm_expand_factor, text='Expand')
btn_factor = tk.Button(master=frm_expand_factor, text='Factor')


base_choice = tk.IntVar()
btn_log = tk.Button(master=frm_log, text='log')
lbl_base = tk.Label(master=frm_log, text='Base:')


btn_e = tk.Button(master=frm_other_sci, text='e')
btn_factorial = tk.Button(master=frm_other_sci, text='!')
btn_abs = tk.Button(master=frm_other_sci, text='| |')
btn_imag = tk.Button(master=frm_other_sci, text='i')
btn_derivative = tk.Button(master=frm_other_sci, text='ⅆ')
btn_integral = tk.Button(master=frm_other_sci, text='⎰')

btn_greater = tk.Button(master=frm_inequality, text='>')
btn_greater_equal = tk.Button(master=frm_inequality, text='≥')
btn_less = tk.Button(master=frm_inequality, text='<')
btn_less_equal = tk.Button(master=frm_inequality, text='≤')

btn_submit = tk.Button(master=frm_nav_buttons, text='Submit', bg='#c2b9b6')
btn_remove = tk.Button(master=frm_nav_buttons, text='⌫', bg='#c2b9b6')
btn_new_line = tk.Button(master=frm_nav_buttons, text='⤶', bg='#c2b9b6')
btn_functions = tk.Button(master=frm_nav_buttons, text='∑∫ഽ', bg='#c2b9b6')
btn_abc = tk.Button(master=frm_nav_buttons, text='abc', bg='#c2b9b6')

btn_limit = tk.Button(master=frm_limit, text='Limit:\n x-->')
btn_insert_infinity = tk.Button(master=frm_limit, text='∞')


btn_summation = tk.Button(master=frm_summation, text='∑')


btn_a = tk.Button(master=frm_abc, text='a')
btn_b = tk.Button(master=frm_abc, text='b')
btn_c = tk.Button(master=frm_abc, text='c')
btn_d = tk.Button(master=frm_abc, text='d')
btn_letter_e = tk.Button(master=frm_abc, text='e')  # To distinguish between e euler and letter e
btn_f = tk.Button(master=frm_abc, text='f')
btn_g = tk.Button(master=frm_abc, text='g')
btn_h = tk.Button(master=frm_abc, text='h')
btn_i = tk.Button(master=frm_abc, text='i')
btn_j = tk.Button(master=frm_abc, text='j')
btn_k = tk.Button(master=frm_abc, text='k')
btn_l = tk.Button(master=frm_abc, text='l')
btn_m = tk.Button(master=frm_abc, text='m')
btn_n = tk.Button(master=frm_abc, text='n')
btn_o = tk.Button(master=frm_abc, text='o')
btn_p = tk.Button(master=frm_abc, text='p')
btn_q = tk.Button(master=frm_abc, text='q')
btn_r = tk.Button(master=frm_abc, text='r')
btn_s = tk.Button(master=frm_abc, text='s')
btn_t = tk.Button(master=frm_abc, text='t')
btn_u = tk.Button(master=frm_abc, text='u')
btn_v = tk.Button(master=frm_abc, text='v')
btn_w = tk.Button(master=frm_abc, text='w')
btn_letter_x = tk.Button(master=frm_abc, text='x')
btn_y = tk.Button(master=frm_abc, text='y')
btn_z = tk.Button(master=frm_abc, text='z')

# Layout
lbl_expression.grid(row=0, column=0, sticky='new')
txt_output.grid(row=1, column=0, sticky='new')

btn_pi.grid(row=4, column=0)
btn_x.grid(row=4, column=1)

btn_zero.grid(row=4, column=2)
btn_dot.grid(row=4, column=3)
btn_equal.grid(row=4, column=4)
btn_plus.grid(row=4, column=5)


btn_cube.grid(row=3, column=0)
btn_cube_root.grid(row=3, column=1)
btn_one.grid(row=3, column=2)
btn_two.grid(row=3, column=3)
btn_three.grid(row=3, column=4)
btn_minus.grid(row=3, column=5)


btn_square.grid(row=2, column=0)
btn_square_root.grid(row=2, column=1)
btn_four.grid(row=2, column=2)
btn_five.grid(row=2, column=3)
btn_six.grid(row=2, column=4)
btn_multiply.grid(row=2, column=5)

btn_parentheses_right.grid(row=1, column=0)
btn_parentheses_left.grid(row=1, column=1)
btn_seven.grid(row=1, column=2)
btn_eight.grid(row=1, column=3)
btn_nine.grid(row=1, column=4)
btn_divide.grid(row=1, column=5)

btn_abc.grid(row=0, column=2)
btn_functions.grid(row=0, column=3)
btn_new_line.grid(row=0, column=4)
btn_remove.grid(row=0, column=5)

btn_submit.grid(row=0, column=0)
btn_expand.grid(row=0, column=2)
btn_factor.grid(row=0, column=3)

btn_sin.grid(row=0, column=0)
btn_cos.grid(row=0, column=1)
btn_tan.grid(row=0, column=2)
btn_cot.grid(row=0, column=3)
btn_degree.grid(row=0, column=4)


btn_log.grid(row=1, column=0)
lbl_base.grid(row=1, column=1)
ent_base.grid(row=1, column=2)

btn_abs.grid(row=2, column=0)
btn_imag.grid(row=2, column=1)
btn_e.grid(row=2, column=2)
btn_factorial.grid(row=2, column=3)
btn_derivative.grid(row=2, column=4)
btn_integral.grid(row=2, column=5)

btn_greater.grid(row=3, column=0)
btn_greater_equal.grid(row=3, column=1)
btn_less.grid(row=3, column=2)
btn_less_equal.grid(row=3, column=3)

btn_limit.grid(row=0, column=0)
ent_limit_value.grid(row=0, column=1)
btn_insert_infinity.grid(row=0, column=2)

ent_summation_n.grid(row=0, column=0)
btn_summation.grid(row=1, column=0)
ent_summation_start.grid(row=2, column=0)
