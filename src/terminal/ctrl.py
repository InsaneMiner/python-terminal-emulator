NUL = 0x0  # NULL
SP = 0x20  # space
BEL = 0x07 # ^G) beeps;
BS = 0x08  # ^H) backspaces one column (but not past the beginning of the line);
HT = 0x09  # ^I) goes to the next tab stop or to the end of the line if there is no earlier tab stop;
LF = 0x0A  # ^J)
VT = 0x0B  # ^K) and FF (0x0C, ^L) all give a linefeed, and if LF/NL (new-line mode) is set also a carriage return;
FF = 0x0C  # see VT 
CR = 0x0D  # ^M) gives a carriage return;
SO = 0x0E  # ^N) activates the G1 character set;
SI = 0x0F  # ^O) activates the G0 character set;
CAN = 0x18 # ^X) and SUB (0x1A, ^Z) interrupt escape sequences;
SUB = 0x1A # see CAN 
ESC = 0x1B # ^[) starts an escape sequence;
DEL = 0x7F # is ignored;
CSI = 0x9B # is equivalent to ESC [. 
