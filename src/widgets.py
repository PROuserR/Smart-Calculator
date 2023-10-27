#   Defining widgets to use them in other modules
import tkinter as tk


#   Main window
win = tk.Tk()
win.title('Smart Calculator')



frm_txtbox = tk.Frame()

txt_box = tk.Text(master=frm_txtbox, width=32, height=8, state='disabled', font=('default', 16))
txt_box.config(state='normal')
txt_box.insert(tk.INSERT, 'Type here your math problem ...')
txt_box.config(state='disabled')


#   Navigation gui elements
frm_nav_buttons = tk.Frame(pady=8, padx=5)

btn_submit = tk.Button(master=frm_nav_buttons, text='Submit', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_remove = tk.Button(master=frm_nav_buttons, text='⌫', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_clear_txt = tk.Button(master=frm_nav_buttons, text='Clear', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_new_line = tk.Button(master=frm_nav_buttons, text='⤶', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_sci_functions = tk.Button(master=frm_nav_buttons, text='∑ⅆഽ', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_symbols = tk.Button(master=frm_nav_buttons, text='abc', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))
btn_open_image = tk.Button(master=frm_nav_buttons, text='🖼', bg='lightgray', width=5, height=2, cursor='hand2', font=('default', 11))


#   Scientific mode gui elements
frm_sci = tk.LabelFrame(text='Sci', font=('default', 12))

lbl_trigonometry = tk.Label(master=frm_sci, text='Trigonometry:', font=('default', 12))
lbl_inequality = tk.Label(master=frm_sci, text='Inequality:', width=8, height=1, font=('default', 12))
lbl_calculus = tk.Label(master=frm_sci, text='Calculus:', width=8, height=1, font=('default', 12))
lbl_log = tk.Label(master=frm_sci, text='Log:', width=4, height=1, font=('default', 12))
lbl_other = tk.Label(master=frm_sci, text='Other:', width=4, height=1, font=('default', 12))


frm_trig = tk.Frame(master=frm_sci, pady=8)

deg_type_choice = tk.IntVar()
btn_sin = tk.Button(master=frm_trig, text='sin', width=5, height=1, font=('default', 12),  cursor='hand2')
btn_cos = tk.Button(master=frm_trig, text='cos', width=5, height=1, font=('default', 12), cursor='hand2')
btn_tan = tk.Button(master=frm_trig, text='tan', width=5, height=1, font=('default', 12), cursor='hand2')
btn_cot = tk.Button(master=frm_trig, text='cot', width=5, height=1, font=('default', 12), cursor='hand2')
btn_degree = tk.Button(master=frm_trig, text='°', width=5, height=1, font=('default', 12), cursor='hand2')


frm_inequality = tk.Frame(master=frm_sci, pady=8)

btn_greater = tk.Button(master=frm_inequality, text='>', width=5, height=1, font=('default', 12), cursor='hand2')
btn_greater_equal = tk.Button(master=frm_inequality, text='≥', width=5, height=1, font=('default', 12), cursor='hand2')
btn_less = tk.Button(master=frm_inequality, text='<', width=5, height=1, font=('default', 12), cursor='hand2')
btn_less_equal = tk.Button(master=frm_inequality, text='≤', width=5, height=1, font=('default', 12), cursor='hand2')


frm_calculus = tk.Frame(master=frm_sci, pady=8)

btn_limit = tk.Button(master=frm_calculus ,text='Limit:\n x-->', width=5, height=1, font=('default', 12), cursor='hand2')
ent_limit_value = tk.Entry(master=frm_calculus, width=5, font=('default', 12))
btn_insert_infinity = tk.Button(master=frm_calculus, text='∞', width=5, height=1, font=('default', 12), cursor='hand2')
btn_derivative = tk.Button(master=frm_calculus, text='ⅆ', width=5, height=1, font=('default', 12), cursor='hand2')
btn_integral = tk.Button(master=frm_calculus, text='⎰', width=5, height=1, font=('default', 12), cursor='hand2')


frm_log = tk.Frame(master=frm_sci, pady=8)

base_choice = tk.IntVar()
btn_log = tk.Button(master=frm_log, text='log', width=5, height=1, font=('default', 12))
lbl_base = tk.Label(master=frm_log, text='Base:', width=5, height=1, font=('default', 12))
ent_base = tk.Entry(master=frm_log,  width=5, font=('default', 12))
btn_e = tk.Button(master=frm_log, text='e', width=5, height=1, font=('default', 12), cursor='hand2')


frm_expand_factor = tk.Frame(master=frm_sci, pady=8)

btn_expand = tk.Button(master=frm_expand_factor, text='Expand', bg='white', width=6, height=1, font=('default', 12), cursor='hand2')
btn_factor = tk.Button(master=frm_expand_factor, text='Factor', bg='white', width=6, height=1, font=('default', 12), cursor='hand2')


frm_other_sci = tk.Frame(master=frm_sci, pady=8)

ent_summation_n = tk.Entry(master=frm_other_sci, width=5, font=('default', 12))
btn_summation = tk.Button(master=frm_other_sci, text='∑',  width=5, height=1, font=('default', 12), cursor='hand2')
btn_absolute = tk.Button(master=frm_other_sci, text='| |',  width=5, height=1, font=('default', 12), cursor='hand2')
btn_imag = tk.Button(master=frm_other_sci, text='I',  width=5, height=1, font=('default', 12), cursor='hand2')
btn_factorial = tk.Button(master=frm_other_sci, text='!',  width=5, height=1, font=('default', 12), cursor='hand2')
ent_summation_start = tk.Entry(master=frm_other_sci, width=5, font=('default', 12))


#   Standard mode gui elements
frm_standard = tk.LabelFrame(text='Standard', font=('default', 12))

btn_parentheses_right = tk.Button(master=frm_standard, text='(', width=5, height=2, cursor='hand2', font=('default', 12))
btn_parentheses_left = tk.Button(master=frm_standard, text=')', width=5, height=2, cursor='hand2', font=('default', 12))
btn_seven = tk.Button(master=frm_standard, text='7', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_eight = tk.Button(master=frm_standard, text='8', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_nine = tk.Button(master=frm_standard, text='9', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_divide = tk.Button(master=frm_standard, text='/', width=5, height=2, cursor='hand2', font=('default', 12))

btn_square = tk.Button(master=frm_standard, text='²', width=5, height=2, cursor='hand2', font=('default', 12))
btn_square_root = tk.Button(master=frm_standard, text='√', width=5, height=2, cursor='hand2', font=('default', 12))
btn_four = tk.Button(master=frm_standard, text='4', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_five = tk.Button(master=frm_standard, text='5', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_six = tk.Button(master=frm_standard, text='6', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_multiply = tk.Button(master=frm_standard, text='*', width=5, height=2, cursor='hand2', font=('default', 12))

btn_cube = tk.Button(master=frm_standard, text='³', width=5, height=2, cursor='hand2', font=('default', 12))
btn_cube_root = tk.Button(master=frm_standard, text='∛', width=5, height=2, cursor='hand2', font=('default', 12))
btn_one = tk.Button(master=frm_standard, text='1', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_two = tk.Button(master=frm_standard, text='2', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_three = tk.Button(master=frm_standard, text='3', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_minus = tk.Button(master=frm_standard, text='-', width=5, height=2, cursor='hand2', font=('default', 12))

btn_pi = tk.Button(master=frm_standard, text='Ⲡ', width=5, height=2, cursor='hand2', font=('default', 12))
btn_x = tk.Button(master=frm_standard, text='x', width=5, height=2, cursor='hand2', font=('default', 12))
btn_zero = tk.Button(master=frm_standard, text='0', bg='white', width=5, height=2, cursor='hand2', font=('default', 12))
btn_dot = tk.Button(master=frm_standard, text='.', width=5, height=2, cursor='hand2', font=('default', 12))
btn_equal = tk.Button(master=frm_standard, text='=', width=5, height=2, cursor='hand2', font=('default', 12))
btn_plus = tk.Button(master=frm_standard, text='+', width=5, height=2, cursor='hand2', font=('default', 12))


#   Symbols mode gui elements
frm_symbols = tk.LabelFrame(text='Symbols', font=('default', 12))

btn_letter_a = tk.Button(master=frm_symbols, text='a', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_b = tk.Button(master=frm_symbols, text='b', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_c = tk.Button(master=frm_symbols, text='c', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_d = tk.Button(master=frm_symbols, text='d', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_e = tk.Button(master=frm_symbols, text='e', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_f = tk.Button(master=frm_symbols, text='f', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_g = tk.Button(master=frm_symbols, text='g', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_h = tk.Button(master=frm_symbols, text='h', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_i = tk.Button(master=frm_symbols, text='i', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_j = tk.Button(master=frm_symbols, text='j', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_k = tk.Button(master=frm_symbols, text='k', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_l = tk.Button(master=frm_symbols, text='l', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_m = tk.Button(master=frm_symbols, text='m', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_n = tk.Button(master=frm_symbols, text='n', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_o = tk.Button(master=frm_symbols, text='o', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_p = tk.Button(master=frm_symbols, text='p', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_q = tk.Button(master=frm_symbols, text='q', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_r = tk.Button(master=frm_symbols, text='r', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_s = tk.Button(master=frm_symbols, text='s', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_t = tk.Button(master=frm_symbols, text='t', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_u = tk.Button(master=frm_symbols, text='u', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_v = tk.Button(master=frm_symbols, text='v', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_w = tk.Button(master=frm_symbols, text='w', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_x = tk.Button(master=frm_symbols, text='x', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_y = tk.Button(master=frm_symbols, text='y', width=5, height=2, cursor='hand2', font=('default', 12))
btn_letter_z = tk.Button(master=frm_symbols, text='z', width=5, height=2, cursor='hand2', font=('default', 12))
