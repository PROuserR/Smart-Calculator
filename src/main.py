from widgets import win
from gui_layout import init_gui_layout, assign_gui_funcs
import matplotlib

matplotlib.use('TkAgg')
init_gui_layout()
assign_gui_funcs()

win.mainloop()
