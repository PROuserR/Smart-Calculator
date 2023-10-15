from functions import *


def place_basic_panel():
    lbl_expression.grid(row=0, column=0, sticky='new')
    txt_output.grid(row=1, column=0, sticky='new')

    btn_submit.grid(row=0, column=0)
    btn_symbols.grid(row=0, column=2)
    btn_functions.grid(row=0, column=3)
    btn_new_line.grid(row=0, column=4)
    btn_remove.grid(row=0, column=5)
    btn_clear_txt.grid(row=0, column=6)


def place_std_btns():
    btn_parentheses_right.grid(row=1, column=0)
    btn_parentheses_left.grid(row=1, column=1)
    btn_seven.grid(row=1, column=2)
    btn_eight.grid(row=1, column=3)
    btn_nine.grid(row=1, column=4)
    btn_divide.grid(row=1, column=5)

    btn_square.grid(row=2, column=0)
    btn_square_root.grid(row=2, column=1)
    btn_four.grid(row=2, column=2)
    btn_five.grid(row=2, column=3)
    btn_six.grid(row=2, column=4)
    btn_multiply.grid(row=2, column=5)

    btn_cube.grid(row=3, column=0)
    btn_cube_root.grid(row=3, column=1)
    btn_one.grid(row=3, column=2)
    btn_two.grid(row=3, column=3)
    btn_three.grid(row=3, column=4)
    btn_minus.grid(row=3, column=5)

    btn_pi.grid(row=4, column=0)
    btn_x.grid(row=4, column=1)
    btn_zero.grid(row=4, column=2)
    btn_dot.grid(row=4, column=3)
    btn_equal.grid(row=4, column=4)
    btn_plus.grid(row=4, column=5)


def place_symbols_btns():
    i, j = 0, 0
    for btn in frm_symbols.children:
        frm_symbols.children[btn].grid(row=j, column=i)
        i += 1
        if i % 10 == 0:
            j += 1
            i = 0


def place_func_btns():
    btn_sin.grid(row=1, column=0)
    btn_cos.grid(row=1, column=1)
    btn_tan.grid(row=1, column=2)
    btn_cot.grid(row=1, column=3)
    btn_degree.grid(row=1, column=4)

    btn_greater.grid(row=3, column=0)
    btn_greater_equal.grid(row=3, column=1)
    btn_less.grid(row=3, column=2)
    btn_less_equal.grid(row=3, column=3)

    btn_log.grid(row=0, column=0)
    lbl_base.grid(row=0, column=1)
    ent_base.grid(row=0, column=2)
    btn_e.grid(row=0, column=3)

    btn_abs.grid(row=1, column=1)
    btn_imag.grid(row=1, column=2)
    btn_factorial.grid(row=1, column=3)
    ent_summation_n.grid(row=0, column=0)
    btn_summation.grid(row=1, column=0)
    ent_summation_start.grid(row=2, column=0)

    btn_limit.grid(row=0, column=0)
    ent_limit_value.grid(row=0, column=1)
    btn_insert_infinity.grid(row=0, column=2)
    btn_derivative.grid(row=0, column=3)
    btn_integral.grid(row=0, column=4)

    btn_expand.grid(row=0, column=2)
    btn_factor.grid(row=0, column=3)


def init_gui_layout():
    place_basic_panel()
    place_std_btns()
    place_func_btns()
    place_symbols_btns()

    frm_output.pack()
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


def assign_gui_funcs():
    btn_zero.configure(command=lambda: insert_letter(btn_zero['text']))
    btn_one.configure(command=lambda: insert_letter(btn_one['text']))
    btn_two.configure(command=lambda: insert_letter(btn_two['text']))
    btn_three.configure(command=lambda: insert_letter(btn_three['text']))
    btn_four.configure(command=lambda: insert_letter(btn_four['text']))
    btn_five.configure(command=lambda: insert_letter(btn_five['text']))
    btn_six.configure(command=lambda: insert_letter(btn_six['text']))
    btn_seven.configure(command=lambda: insert_letter(btn_seven['text']))
    btn_eight.configure(command=lambda: insert_letter(btn_eight['text']))
    btn_nine.configure(command=lambda: insert_letter(btn_nine['text']))

    btn_equal.configure(command=lambda: insert_letter(btn_equal['text']))
    btn_dot.configure(command=lambda: insert_letter(btn_dot['text']))
    btn_plus.configure(command=lambda: insert_letter(btn_plus['text']))
    btn_minus.configure(command=lambda: insert_letter(btn_minus['text']))
    btn_multiply.configure(command=lambda: insert_letter(btn_multiply['text']))
    btn_divide.configure(command=lambda: insert_letter(btn_divide['text']))

    btn_parentheses_right.configure(command=lambda: insert_letter(btn_parentheses_right['text']))
    btn_parentheses_left.configure(command=lambda: insert_letter(btn_parentheses_left['text']))
    btn_square_root.configure(command=lambda: insert_letter(btn_square_root['text']))
    btn_square.configure(command=lambda: insert_letter(btn_square['text']))
    btn_cube_root.configure(command=lambda: insert_letter(btn_cube_root['text']))
    btn_cube.configure(command=lambda: insert_letter(btn_cube['text']))
    btn_x.configure(command=lambda: insert_letter(btn_x['text']))
    btn_pi.configure(command=lambda: insert_letter(btn_pi['text']))

    btn_sin.configure(command=lambda: insert_letter(btn_sin['text']))
    btn_cos.configure(command=lambda: insert_letter(btn_cos['text']))
    btn_tan.configure(command=lambda: insert_letter(btn_tan['text']))
    btn_cot.configure(command=lambda: insert_letter(btn_cot['text']))
    btn_degree.configure(command=lambda: insert_letter(btn_degree['text']))

    btn_log.configure(command=lambda: insert_letter(btn_log['text']))

    btn_e.configure(command=lambda: insert_letter(btn_e['text']))
    btn_factorial.configure(command=lambda: insert_letter(btn_factorial['text']))
    btn_abs.configure(command=insert_abs)
    btn_imag.configure(command=lambda: insert_letter(btn_imag['text']))
    btn_derivative.configure(command=insert_derivative)
    btn_integral.configure(command=insert_integral)

    btn_greater.configure(command=lambda: insert_letter(btn_greater['text']))
    btn_greater_equal.configure(command=lambda: insert_letter(btn_greater_equal['text']))
    btn_less.configure(command=lambda: insert_letter(btn_less['text']))
    btn_less_equal.configure(command=lambda: insert_letter(btn_less_equal['text']))

    btn_remove.configure(command=remove)
    btn_clear_txt.configure(command=clear_txt)
    btn_new_line.configure(command=insert_new_line)
    btn_functions.configure(command=show_functions)
    btn_symbols.configure(command=show_symbols)

    btn_submit.configure(command=submit)
    btn_expand.configure(command=expand)
    btn_factor.configure(command=factor)

    btn_limit.configure(command=insert_limit)
    btn_insert_infinity.configure(command=lambda: ent_limit_value.insert(tk.END, '∞'))

    btn_summation.configure(command=insert_summation)

    btn_letter_a.configure(command=lambda: insert_letter(btn_letter_a['text']))
    btn_letter_b.configure(command=lambda: insert_letter(btn_letter_b['text']))
    btn_letter_c.configure(command=lambda: insert_letter(btn_letter_c['text']))
    btn_letter_d.configure(command=lambda: insert_letter(btn_letter_d['text']))
    btn_letter_e.configure(command=lambda: insert_letter(btn_letter_e['text']))
    btn_letter_f.configure(command=lambda: insert_letter(btn_letter_f['text']))
    btn_letter_g.configure(command=lambda: insert_letter(btn_letter_g['text']))
    btn_letter_h.configure(command=lambda: insert_letter(btn_letter_h['text']))
    btn_letter_i.configure(command=lambda: insert_letter(btn_letter_i['text']))
    btn_letter_j.configure(command=lambda: insert_letter(btn_letter_j['text']))
    btn_letter_k.configure(command=lambda: insert_letter(btn_letter_k['text']))
    btn_letter_l.configure(command=lambda: insert_letter(btn_letter_l['text']))
    btn_letter_m.configure(command=lambda: insert_letter(btn_letter_m['text']))
    btn_letter_n.configure(command=lambda: insert_letter(btn_letter_n['text']))
    btn_letter_o.configure(command=lambda: insert_letter(btn_letter_o['text']))
    btn_letter_p.configure(command=lambda: insert_letter(btn_letter_p['text']))
    btn_letter_q.configure(command=lambda: insert_letter(btn_letter_q['text']))
    btn_letter_r.configure(command=lambda: insert_letter(btn_letter_r['text']))
    btn_letter_s.configure(command=lambda: insert_letter(btn_letter_s['text']))
    btn_letter_t.configure(command=lambda: insert_letter(btn_letter_t['text']))
    btn_letter_u.configure(command=lambda: insert_letter(btn_letter_u['text']))
    btn_letter_v.configure(command=lambda: insert_letter(btn_letter_v['text']))
    btn_letter_w.configure(command=lambda: insert_letter(btn_letter_w['text']))
    btn_letter_x.configure(command=lambda: insert_letter(btn_letter_x['text']))
    btn_letter_y.configure(command=lambda: insert_letter(btn_letter_y['text']))
    btn_letter_z.configure(command=lambda: insert_letter(btn_letter_z['text']))
