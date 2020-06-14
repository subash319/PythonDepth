# 7. D  = {'pen':10, 'pencil':5, 'eraser':8, 'marker':15, 'ruler':19 }
# Draw the following chart for this dictionary
#
# pen         ----------
#
# pencil      -----
#
# eraser      --------
#
# marker      ---------------
#
# ruler       -------------------

D  = {'pen':10, 'pencil':5, 'eraser':8, 'marker':15, 'ruler':19 }
for key, value in D.items():
    print(f"{key.ljust(8)}:{'-'*value}")