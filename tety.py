import os
size = os.get_terminal_size()
e1 = "😱"
fs = (size.columns * size.lines)
hfs = (fs / 2)

print(e1 * hfs + " e", e1 * hfs)
