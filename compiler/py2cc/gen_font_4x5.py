#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


font = """\
32           \
____           \
____           \
____           \
____           \
____
\
33 \
_@__ \
_@__ \
_@__ \
____ \
_@__
\
34 \
@_@_ \
@_@_ \
____ \
____ \
____
\
35 \
@_@_ \
@@@@ \
@_@_ \
@@@@ \
@_@_
\
36            \
_@@_          \
@@_@          \
_@@_          \
@_@@          \
_@@_
\
37            \
@__@          \
__@_          \
_@__          \
@__@          \
____
\
38            \
_@@_          \
_@__          \
@__@          \
_@@_          \
____
\
39            \
@___          \
@___          \
____          \
____          \
____
\
40            \
___@          \
__@_          \
__@_          \
__@_          \
___@
\
41            \
@___          \
_@__          \
_@__          \
_@__          \
@___
\
42          \
____          \
@_@_          \
_@__          \
@_@_          \
____
\
43          \
____          \
_@__          \
@@@_          \
_@__          \
____
\
44          \
____          \
____          \
____          \
_@__          \
_@__
\
45          \
____          \
____          \
@@@_          \
____          \
____
\
46          \
____          \
____          \
____          \
_@__          \
____
\
47          \
__@_          \
__@_          \
_@__          \
@___          \
@___
\
48          \
_@__          \
@_@_          \
@_@_          \
@_@_          \
_@__
\
49          \
_@__          \
@@__          \
_@__          \
_@__          \
_@__
\
50          \
@@@_          \
___@          \
_@@_          \
@___          \
@@@@
\
51          \
@@@@          \
___@          \
__@_          \
@__@          \
_@@_
\
52          \
@___          \
@_@_          \
@_@_          \
@@@@          \
__@_
\
53          \
@@@@          \
@___          \
_@@_          \
___@          \
@@@_
\
54          \
_@@@          \
@___          \
@@@_          \
@__@          \
@@@_
\
55          \
@@@@          \
___@          \
__@_          \
_@__          \
_@__
\
56          \
_@@_          \
@__@          \
_@@_          \
@__@          \
_@@_
\
57          \
_@@@          \
@__@          \
_@@@          \
___@          \
___@
\
58          \
____          \
_@__          \
____          \
_@__          \
____
\
59          \
____          \
_@__          \
____          \
_@__          \
_@__
\
60          \
___@          \
__@_          \
_@__          \
__@_          \
___@
\
61          \
____          \
@@@_          \
____          \
@@@_          \
____
\
62          \
_@__          \
__@_          \
___@          \
__@_          \
_@__
\
63          \
_@@_          \
@__@          \
__@_          \
____          \
_@@_
\
64          \
_@@@          \
@_@@          \
@_@@          \
@___          \
_@@_
\
65          \
_@@_          \
@__@          \
@__@          \
@@@@          \
@__@
\
66          \
@@@_          \
@__@          \
@@@_          \
@__@          \
@@@_
\
67          \
_@@@          \
@___          \
@___          \
@___          \
_@@@
\
68          \
@@@_          \
@__@          \
@__@          \
@__@          \
@@@_
\
69          \
@@@@          \
@___          \
@@@_          \
@___          \
@@@@
\
70          \
@@@@          \
@___          \
@@@_          \
@___          \
@___
\
71          \
_@@@          \
@___          \
@_@@          \
@__@          \
_@@@
\
72          \
@__@          \
@__@          \
@@@@          \
@__@          \
@__@
\
73          \
@@@_          \
_@__          \
_@__          \
_@__          \
@@@_
\
74          \
@@@@           \
___@           \
___@           \
@__@           \
_@@_
\
75           \
@__@           \
@_@_           \
@@__           \
@_@_           \
@__@
\
76           \
@___           \
@___           \
@___           \
@___           \
@@@@
\
77           \
@__@           \
@@@@           \
@@@@           \
@@@@           \
@__@
\
78           \
@__@           \
@@_@           \
@_@@           \
@_@@           \
@__@
\
79           \
_@@_           \
@__@           \
@__@           \
@__@           \
_@@_
\
80           \
@@@_           \
@__@           \
@@@_           \
@___           \
@___
\
81           \
_@@_           \
@__@           \
@__@           \
_@@_           \
__@@
\
82           \
@@@_           \
@__@           \
@@@_           \
@__@           \
@__@
\
83           \
_@@@           \
@___           \
_@@_           \
___@           \
@@@_
\
84           \
_@@@           \
__@_           \
__@_           \
__@_           \
__@_
\
85           \
@__@           \
@__@           \
@__@           \
@__@           \
_@@_
\
86           \
@__@           \
@__@           \
@__@           \
@_@_           \
_@__
\
87           \
@__@           \
@_@@           \
@@@@           \
@@@@           \
@__@
\
88           \
@__@           \
@__@           \
_@@_           \
@__@           \
@__@
\
89           \
@__@           \
_@_@           \
__@_           \
_@__           \
@___
\
90           \
@@@@           \
__@_           \
_@__           \
@___           \
@@@@
\
91           \
__@@           \
__@_           \
__@_           \
__@_           \
__@@
\
92           \
_@__           \
_@__           \
__@_           \
___@           \
___@
\
93           \
@@__           \
_@__           \
_@__           \
_@__           \
@@__
\
94           \
_@__           \
@_@_           \
____           \
____           \
____
\
95           \
____           \
____           \
____           \
____           \
@@@@
\
96           \
_@__           \
__@_           \
____           \
____           \
____
\
97           \
____           \
_@@@           \
@__@           \
_@@@           \
____
\
98           \
@___           \
@@@_          \
@__@           \
@@@_           \
____
\
99           \
____           \
_@@@           \
@___           \
_@@@           \
____
\
100           \
___@           \
_@@@           \
@__@           \
_@@@           \
____
\
101           \
_@@_           \
@__@           \
@@@_           \
_@@@           \
____
\
102           \
__@@           \
_@__           \
@@@_           \
_@__           \
____
\
103           \
____          \
@@@@           \
@__@           \
@@@@           \
@@@@
\
104           \
@___           \
@@@_           \
@__@           \
@__@           \
____
\
105           \
_@@_           \
____           \
_@@_           \
_@@_           \
____
\
106           \
__@_           \
____           \
_@__           \
_@__           \
@___
\
107           \
@___           \
@_@@           \
@@@_           \
@__@           \
____
\
108           \
_@__           \
_@__           \
_@__           \
_@@_           \
____
\
109           \
____           \
@@@_           \
@_@@           \
@_@@           \
____
\
110           \
____           \
@@__           \
@_@_           \
@_@_           \
____
\
111           \
____           \
_@@_           \
@__@           \
_@@_           \
____
\
112           \
____           \
@@@_           \
@__@           \
@@@_           \
@___
\
113           \
____           \
_@@@           \
@__@           \
_@@@           \
___@
\
114           \
____           \
__@@           \
_@__           \
_@__           \
____
\
115           \
____           \
__@@           \
_@@_           \
@@@_           \
____
\
116           \
_@__           \
_@@_           \
_@__           \
__@_           \
____
\
117           \
____           \
@__@           \
@__@           \
_@@@           \
____
\
118           \
____           \
@__@           \
@_@_           \
_@__           \
____
\
119           \
____           \
@__@           \
@_@@           \
_@@_           \
____
\
120           \
____           \
@__@           \
_@@_           \
@__@           \
____
\
121           \
____           \
@__@           \
@@_@           \
__@_           \
@@__
\
122           \
____           \
@@@@           \
_@__           \
@@@@           \
____
\
123           \
__@@           \
__@_           \
_@@_           \
__@_           \
__@@
\
124           \
_@__           \
_@__           \
_@__           \
_@__           \
_@__
\
125           \
@@__           \
_@__           \
_@@_           \
_@__           \
@@__
\
126           \
_@_@           \
@_@_           \
____           \
____           \
____"""

if __name__ == "__main__":
    import pprint
    import os

    raw_font_def = [x.split() for x in font.split("\n") ]
    font_def = [ [int(a),[b,c,d,e,f]] for a,b,c,d,e,f in raw_font_def ]
    nfont_def = []
    for ascval, raw in font_def:
        nb = []
        for line in raw:
            nl = ""
            for c in line:
                nc = ("0" if (c=="." or c=="_") else "1")
                nl += nc
            nl = "0b" + nl
            nb.append(nl)
        binary = nb

        items = ", ".join(binary)
        nfont_def.append( "{" + str(ascval)+", "+ items+ "}" )

    c_standalone_template = """\
#include <stdio.h>

int main(int argc, char* argv[]) {

    %FONTDEF%

    printf("Hello \\%d\\n", 0b100);
    return 0;q
}
"""

    c_include_template = """\
/*                                                                 */
/* DO NOT EDIT THIS (autogenerated) FILE                           */
/* To make changes to the font, edit py2cc/gen_font_4x5.py instead */
/*                                                                 */
%FONTDEF%
"""

    array_def = ",\n                      ".join(nfont_def)

    font_lines = ( "   const unsigned char font[95][6] = {" + "\n" 
                   "                      " + array_def + "\n"
                   "                     };" + "\n" )

    STANDALONE = os.path.join(os.path.expanduser("~"), "spark_font.c")

    c_prog = c_standalone_template
    c_prog = c_prog.replace("%FONTDEF%", font_lines)

    f = open(STANDALONE, "w")
    f.write(c_prog);
    f.flush()
    f.close()

    # NOTE: Assumes this is being run in this directory.
    # Having a better way of finding where to generate the font would be good.
    INCLUDE_FILE = os.path.join("../../dal/spark_font.h")

    c_prog = c_include_template
    c_prog = c_prog.replace("%FONTDEF%", font_lines)

    f = open(INCLUDE_FILE, "w")
    f.write(c_prog);
    f.flush()
    f.close()

