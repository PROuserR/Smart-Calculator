from functions import *


#   Layout the main navigation panel (submit clear abc ...)
def place_nav_panel():
    txt_box.grid(row=1, column=0, sticky='new')

    i = 0
    for btn in frm_nav_buttons.children:
        frm_nav_buttons.children[btn].grid(row=0, column=i)
        i += 1


#   Layout the standard default panel
def place_std_btns():
    i,j = 0,0
    for btn in frm_standard.children:
        frm_standard.children[btn].grid(row=j, column=i)
        i += 1
        if i == 6:
            i = 0
            j += 1


#   Layout the symbols panel 
def place_symbols_btns():
    i, j = 0, 0
    for btn in frm_symbols.children:
        frm_symbols.children[btn].grid(row=j, column=i)
        i += 1
        if i % 10 == 0:
            j += 1
            i = 0


#   Layout the functions panel (sin cos tan ...)
def place_sci_func_btns():
    ent_summation_n.grid(row=0, column=0)
    btn_summation.grid(row=1, column=0)
    btn_absolute.grid(row=1, column=1)
    btn_imag.grid(row=1, column=2)
    btn_factorial.grid(row=1, column=3)
    ent_summation_start.grid(row=2, column=0)

    i = 0
    for btn in frm_calculus.children:
        frm_calculus.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_expand_factor.children:
        frm_expand_factor.children[btn].grid(row=0, column=i, padx=4)
        i += 1

    i = 0
    for btn in frm_log.children:
        frm_log.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_trig.children:
        frm_trig.children[btn].grid(row=0, column=i)
        i += 1

    i = 0
    for btn in frm_inequality.children:
        frm_inequality.children[btn].grid(row=0, column=i)
        i += 1


#   Calls the layout functions above and layout the gui elements
def init_gui_layout():
    place_nav_panel()
    place_std_btns()
    place_sci_func_btns()
    place_symbols_btns()

    frm_txtbox.pack()
    frm_nav_buttons.pack()
    frm_standard.pack()

    lbl_trigonometry.pack()
    frm_trig.pack()
    lbl_inequality.pack()
    frm_inequality.pack()
    lbl_calculus.pack()
    frm_calculus.pack()
    lbl_log.pack()
    frm_log.pack()
    lbl_other.pack()
    frm_other_sci.pack()
    frm_expand_factor.pack()


#   Make every button functional by assigning a function to it
def assign_btn_funcs():
    btn_zero.configure(command=lambda: insert_btn_txt(btn_zero))
    btn_one.configure(command=lambda: insert_btn_txt(btn_one))
    btn_two.configure(command=lambda: insert_btn_txt(btn_two))
    btn_three.configure(command=lambda: insert_btn_txt(btn_three))
    btn_four.configure(command=lambda: insert_btn_txt(btn_four))
    btn_five.configure(command=lambda: insert_btn_txt(btn_five))
    btn_six.configure(command=lambda: insert_btn_txt(btn_six))
    btn_seven.configure(command=lambda: insert_btn_txt(btn_seven))
    btn_eight.configure(command=lambda: insert_btn_txt(btn_eight))
    btn_nine.configure(command=lambda: insert_btn_txt(btn_nine))

    btn_equal.configure(command=lambda: insert_btn_txt(btn_equal))
    btn_dot.configure(command=lambda: insert_btn_txt(btn_dot))
    btn_plus.configure(command=lambda: insert_btn_txt(btn_plus))
    btn_minus.configure(command=lambda: insert_btn_txt(btn_minus))
    btn_multiply.configure(command=lambda: insert_btn_txt(btn_multiply))
    btn_divide.configure(command=lambda: insert_btn_txt(btn_divide))

    btn_parentheses_right.configure(command=lambda: insert_btn_txt(btn_parentheses_right))
    btn_parentheses_left.configure(command=lambda: insert_btn_txt(btn_parentheses_left))
    btn_square_root.configure(command=lambda: insert_btn_txt(btn_square_root))
    btn_square.configure(command=lambda: insert_btn_txt(btn_square))
    btn_cube_root.configure(command=lambda: insert_btn_txt(btn_cube_root))
    btn_cube.configure(command=lambda: insert_btn_txt(btn_cube))
    btn_x.configure(command=lambda: insert_btn_txt(btn_x))
    btn_pi.configure(command=lambda: insert_btn_txt(btn_pi))

    btn_sin.configure(command=lambda: insert_btn_txt(btn_sin))
    btn_cos.configure(command=lambda: insert_btn_txt(btn_cos))
    btn_tan.configure(command=lambda: insert_btn_txt(btn_tan))
    btn_cot.configure(command=lambda: insert_btn_txt(btn_cot))
    btn_degree.configure(command=lambda: insert_btn_txt(btn_degree))

    btn_log.configure(command=lambda: insert_btn_txt(btn_log))

    btn_e.configure(command=lambda: insert_btn_txt(btn_e))
    btn_factorial.configure(command=lambda: insert_btn_txt(btn_factorial))
    btn_absolute.configure(command=lambda: compute('absolute'))
    btn_imag.configure(command=lambda: insert_btn_txt(btn_imag))
    btn_derivative.configure(command=lambda: compute('derivative'))
    btn_integral.configure(command=lambda: compute('integral'))

    btn_greater.configure(command=lambda: insert_btn_txt(btn_greater))
    btn_greater_equal.configure(command=lambda: insert_btn_txt(btn_greater_equal))
    btn_less.configure(command=lambda: insert_btn_txt(btn_less))
    btn_less_equal.configure(command=lambda: insert_btn_txt(btn_less_equal))

    btn_submit.configure(command=lambda: submit())
    btn_remove.configure(command=lambda: remove_char())
    btn_clear_txt.configure(command=lambda: clear_txt())
    btn_new_line.configure(command=lambda: insert_new_line())
    btn_sci_functions.configure(command=lambda: show_hide_sci_functions())
    btn_symbols.configure(command=lambda: show_hide_symbols())
    btn_open_image.config(command=lambda: read_from_image(open_file()))

    btn_expand.configure(command=lambda: compute('expand_expression'))
    btn_factor.configure(command=lambda: compute('factor_expression'))

    btn_limit.configure(command=lambda: compute('limit'))
    btn_insert_infinity.configure(command=lambda: ent_limit_value.insert(tk.END, '∞'))

    btn_summation.configure(command=lambda: compute('summation'))

    btn_letter_a.configure(command=lambda: insert_btn_txt(btn_letter_a))
    btn_letter_b.configure(command=lambda: insert_btn_txt(btn_letter_b))
    btn_letter_c.configure(command=lambda: insert_btn_txt(btn_letter_c))
    btn_letter_d.configure(command=lambda: insert_btn_txt(btn_letter_d))
    btn_letter_e.configure(command=lambda: insert_btn_txt(btn_letter_e))
    btn_letter_f.configure(command=lambda: insert_btn_txt(btn_letter_f))
    btn_letter_g.configure(command=lambda: insert_btn_txt(btn_letter_g))
    btn_letter_h.configure(command=lambda: insert_btn_txt(btn_letter_h))
    btn_letter_i.configure(command=lambda: insert_btn_txt(btn_letter_i))
    btn_letter_j.configure(command=lambda: insert_btn_txt(btn_letter_j))
    btn_letter_k.configure(command=lambda: insert_btn_txt(btn_letter_k))
    btn_letter_l.configure(command=lambda: insert_btn_txt(btn_letter_l))
    btn_letter_m.configure(command=lambda: insert_btn_txt(btn_letter_m))
    btn_letter_n.configure(command=lambda: insert_btn_txt(btn_letter_n))
    btn_letter_o.configure(command=lambda: insert_btn_txt(btn_letter_o))
    btn_letter_p.configure(command=lambda: insert_btn_txt(btn_letter_p))
    btn_letter_q.configure(command=lambda: insert_btn_txt(btn_letter_q))
    btn_letter_r.configure(command=lambda: insert_btn_txt(btn_letter_r))
    btn_letter_s.configure(command=lambda: insert_btn_txt(btn_letter_s))
    btn_letter_t.configure(command=lambda: insert_btn_txt(btn_letter_t))
    btn_letter_u.configure(command=lambda: insert_btn_txt(btn_letter_u))
    btn_letter_v.configure(command=lambda: insert_btn_txt(btn_letter_v))
    btn_letter_w.configure(command=lambda: insert_btn_txt(btn_letter_w))
    btn_letter_x.configure(command=lambda: insert_btn_txt(btn_letter_x))
    btn_letter_y.configure(command=lambda: insert_btn_txt(btn_letter_y))
    btn_letter_z.configure(command=lambda: insert_btn_txt(btn_letter_z))
