from functions import *


#Commands
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
btn_new_line.configure(command=insert_new_line)
btn_functions.configure(command=show_functions)
btn_abc.configure(command=show_abc)

btn_submit.configure(command=submit)
btn_expand.configure(command=expand)
btn_factor.configure(command=factor)

btn_limit.configure(command=insert_limit)
btn_insert_infinity.configure(command=lambda: ent_limit_value.insert(tk.END, '∞'))

btn_summation.configure(command=insert_summation)

btn_a.configure(command=lambda: insert_letter(btn_a['text']))
btn_b.configure(command=lambda: insert_letter(btn_b['text']))
btn_c.configure(command=lambda: insert_letter(btn_c['text']))
btn_d.configure(command=lambda: insert_letter(btn_d['text']))
btn_letter_e.configure(command=lambda: insert_letter(btn_letter_e['text']))
btn_f.configure(command=lambda: insert_letter(btn_f['text']))
btn_g.configure(command=lambda: insert_letter(btn_g['text']))
btn_h.configure(command=lambda: insert_letter(btn_h['text']))
btn_i.configure(command=lambda: insert_letter(btn_i['text']))
btn_j.configure(command=lambda: insert_letter(btn_j['text']))
btn_k.configure(command=lambda: insert_letter(btn_k['text']))
btn_l.configure(command=lambda: insert_letter(btn_l['text']))
btn_m.configure(command=lambda: insert_letter(btn_m['text']))
btn_n.configure(command=lambda: insert_letter(btn_n['text']))
btn_o.configure(command=lambda: insert_letter(btn_o['text']))
btn_p.configure(command=lambda: insert_letter(btn_p['text']))
btn_q.configure(command=lambda: insert_letter(btn_q['text']))
btn_r.configure(command=lambda: insert_letter(btn_r['text']))
btn_s.configure(command=lambda: insert_letter(btn_s['text']))
btn_t.configure(command=lambda: insert_letter(btn_t['text']))
btn_u.configure(command=lambda: insert_letter(btn_u['text']))
btn_v.configure(command=lambda: insert_letter(btn_v['text']))
btn_w.configure(command=lambda: insert_letter(btn_w['text']))
btn_letter_x.configure(command=lambda: insert_letter(btn_letter_x['text']))
btn_y.configure(command=lambda: insert_letter(btn_y['text']))
btn_z.configure(command=lambda: insert_letter(btn_z['text']))
#------------------------------------------------------------

place_abc_btns()

frm_output.pack()
frm_main_functions.pack()
frm_nav_buttons.pack()
frm_standard.pack()

frm_trig.pack()
frm_other_sci.pack()
frm_log.pack()
frm_limit.pack()
frm_summation.pack()


win.mainloop()