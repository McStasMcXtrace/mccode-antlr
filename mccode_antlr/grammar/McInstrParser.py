# Generated from /home/gst/PycharmProjects/mccode4/mccode_antlr/grammar/McInstr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,192,514,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,87,8,1,1,1,3,1,90,8,1,1,1,3,1,93,8,
        1,1,1,3,1,96,8,1,1,1,3,1,99,8,1,1,1,3,1,102,8,1,1,1,3,1,105,8,1,
        1,1,1,1,3,1,109,8,1,1,1,3,1,112,8,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,
        120,8,2,10,2,12,2,123,9,2,3,2,125,8,2,1,2,1,2,1,3,3,3,130,8,3,1,
        3,1,3,3,3,134,8,3,1,3,1,3,3,3,138,8,3,1,3,1,3,1,3,3,3,143,8,3,1,
        3,1,3,3,3,147,8,3,1,3,1,3,1,3,3,3,152,8,3,1,3,1,3,3,3,156,8,3,1,
        3,1,3,3,3,160,8,3,3,3,162,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,4,5,171,
        8,5,11,5,12,5,172,3,5,175,8,5,1,6,4,6,178,8,6,11,6,12,6,179,1,7,
        1,7,1,7,1,8,3,8,186,8,8,1,8,3,8,189,8,8,1,8,3,8,192,8,8,1,8,1,8,
        1,8,1,8,1,8,3,8,199,8,8,1,8,3,8,202,8,8,1,8,1,8,3,8,206,8,8,1,8,
        3,8,209,8,8,1,8,3,8,212,8,8,1,8,3,8,215,8,8,1,8,5,8,218,8,8,10,8,
        12,8,221,9,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,229,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,237,8,10,1,11,1,11,1,11,1,11,5,11,243,8,11,10,
        11,12,11,246,9,11,3,11,248,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,3,12,261,8,12,1,13,1,13,1,13,3,13,266,8,13,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,18,4,18,283,8,18,11,18,12,18,284,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,1,20,3,20,296,8,20,1,20,1,20,1,20,1,20,1,20,3,20,
        303,8,20,1,20,3,20,306,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,
        22,315,8,22,1,22,3,22,318,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,1,24,3,24,332,8,24,3,24,334,8,24,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,346,8,26,3,26,348,8,26,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,360,8,28,
        3,28,362,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,371,8,29,3,
        29,373,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,382,8,30,3,30,
        384,8,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,
        1,33,5,33,398,8,33,10,33,12,33,401,9,33,1,33,1,33,1,34,1,34,1,34,
        1,34,1,35,1,35,1,35,1,35,1,35,5,35,414,8,35,10,35,12,35,417,9,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,5,35,435,8,35,10,35,12,35,438,9,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,453,8,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,5,35,497,8,35,10,35,12,35,500,9,35,1,36,1,36,1,36,
        1,37,1,37,1,37,1,37,1,37,3,37,510,8,37,1,38,1,38,1,38,0,1,70,39,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,7,3,0,1,1,48,48,
        52,52,1,0,33,34,2,0,30,30,32,32,2,0,52,52,179,179,1,0,138,139,1,
        0,140,141,1,0,165,166,566,0,78,1,0,0,0,2,81,1,0,0,0,4,115,1,0,0,
        0,6,161,1,0,0,0,8,163,1,0,0,0,10,166,1,0,0,0,12,177,1,0,0,0,14,181,
        1,0,0,0,16,185,1,0,0,0,18,228,1,0,0,0,20,236,1,0,0,0,22,238,1,0,
        0,0,24,260,1,0,0,0,26,262,1,0,0,0,28,267,1,0,0,0,30,270,1,0,0,0,
        32,274,1,0,0,0,34,278,1,0,0,0,36,282,1,0,0,0,38,286,1,0,0,0,40,305,
        1,0,0,0,42,307,1,0,0,0,44,317,1,0,0,0,46,319,1,0,0,0,48,333,1,0,
        0,0,50,335,1,0,0,0,52,347,1,0,0,0,54,349,1,0,0,0,56,361,1,0,0,0,
        58,372,1,0,0,0,60,383,1,0,0,0,62,385,1,0,0,0,64,390,1,0,0,0,66,393,
        1,0,0,0,68,404,1,0,0,0,70,452,1,0,0,0,72,501,1,0,0,0,74,509,1,0,
        0,0,76,511,1,0,0,0,78,79,3,2,1,0,79,80,5,0,0,1,80,1,1,0,0,0,81,82,
        5,9,0,0,82,83,5,16,0,0,83,84,5,179,0,0,84,86,3,4,2,0,85,87,3,72,
        36,0,86,85,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,90,3,74,37,0,89,
        88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,93,3,12,6,0,92,91,1,0,
        0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,96,3,50,25,0,95,94,1,0,0,0,95,
        96,1,0,0,0,96,98,1,0,0,0,97,99,3,52,26,0,98,97,1,0,0,0,98,99,1,0,
        0,0,99,101,1,0,0,0,100,102,3,54,27,0,101,100,1,0,0,0,101,102,1,0,
        0,0,102,104,1,0,0,0,103,105,3,56,28,0,104,103,1,0,0,0,104,105,1,
        0,0,0,105,106,1,0,0,0,106,108,3,10,5,0,107,109,3,58,29,0,108,107,
        1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,112,3,60,30,0,111,110,
        1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,5,12,0,0,114,3,1,
        0,0,0,115,124,5,132,0,0,116,121,3,6,3,0,117,118,5,169,0,0,118,120,
        3,6,3,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,124,116,1,0,0,0,124,125,
        1,0,0,0,125,126,1,0,0,0,126,127,5,133,0,0,127,5,1,0,0,0,128,130,
        5,78,0,0,129,128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,133,
        5,179,0,0,132,134,3,8,4,0,133,132,1,0,0,0,133,134,1,0,0,0,134,137,
        1,0,0,0,135,136,5,148,0,0,136,138,3,70,35,0,137,135,1,0,0,0,137,
        138,1,0,0,0,138,162,1,0,0,0,139,140,5,93,0,0,140,142,5,179,0,0,141,
        143,3,8,4,0,142,141,1,0,0,0,142,143,1,0,0,0,143,146,1,0,0,0,144,
        145,5,148,0,0,145,147,3,70,35,0,146,144,1,0,0,0,146,147,1,0,0,0,
        147,162,1,0,0,0,148,152,5,43,0,0,149,150,5,66,0,0,150,152,5,140,
        0,0,151,148,1,0,0,0,151,149,1,0,0,0,152,153,1,0,0,0,153,155,5,179,
        0,0,154,156,3,8,4,0,155,154,1,0,0,0,155,156,1,0,0,0,156,159,1,0,
        0,0,157,158,5,148,0,0,158,160,7,0,0,0,159,157,1,0,0,0,159,160,1,
        0,0,0,160,162,1,0,0,0,161,129,1,0,0,0,161,139,1,0,0,0,161,151,1,
        0,0,0,162,7,1,0,0,0,163,164,5,141,0,0,164,165,5,52,0,0,165,9,1,0,
        0,0,166,174,5,24,0,0,167,171,3,16,8,0,168,171,3,74,37,0,169,171,
        3,14,7,0,170,167,1,0,0,0,170,168,1,0,0,0,170,169,1,0,0,0,171,172,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,175,1,0,0,0,174,170,
        1,0,0,0,174,175,1,0,0,0,175,11,1,0,0,0,176,178,3,62,31,0,177,176,
        1,0,0,0,178,179,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,13,1,
        0,0,0,181,182,5,47,0,0,182,183,5,52,0,0,183,15,1,0,0,0,184,186,5,
        36,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,189,5,
        37,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,192,3,
        26,13,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,194,
        5,7,0,0,194,195,3,18,9,0,195,196,5,148,0,0,196,198,3,20,10,0,197,
        199,3,22,11,0,198,197,1,0,0,0,198,199,1,0,0,0,199,201,1,0,0,0,200,
        202,3,28,14,0,201,200,1,0,0,0,201,202,1,0,0,0,202,203,1,0,0,0,203,
        205,3,30,15,0,204,206,3,32,16,0,205,204,1,0,0,0,205,206,1,0,0,0,
        206,208,1,0,0,0,207,209,3,34,17,0,208,207,1,0,0,0,208,209,1,0,0,
        0,209,211,1,0,0,0,210,212,3,42,21,0,211,210,1,0,0,0,211,212,1,0,
        0,0,212,214,1,0,0,0,213,215,3,36,18,0,214,213,1,0,0,0,214,215,1,
        0,0,0,215,219,1,0,0,0,216,218,3,62,31,0,217,216,1,0,0,0,218,221,
        1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,17,1,0,0,0,221,219,1,
        0,0,0,222,223,5,34,0,0,223,224,5,132,0,0,224,225,5,179,0,0,225,229,
        5,133,0,0,226,229,7,1,0,0,227,229,5,179,0,0,228,222,1,0,0,0,228,
        226,1,0,0,0,228,227,1,0,0,0,229,19,1,0,0,0,230,231,5,34,0,0,231,
        232,5,132,0,0,232,233,3,44,22,0,233,234,5,133,0,0,234,237,1,0,0,
        0,235,237,5,179,0,0,236,230,1,0,0,0,236,235,1,0,0,0,237,21,1,0,0,
        0,238,247,5,132,0,0,239,244,3,24,12,0,240,241,5,169,0,0,241,243,
        3,24,12,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,247,239,1,0,0,0,247,248,
        1,0,0,0,248,249,1,0,0,0,249,250,5,133,0,0,250,23,1,0,0,0,251,252,
        5,179,0,0,252,253,5,148,0,0,253,261,3,70,35,0,254,255,5,179,0,0,
        255,256,5,148,0,0,256,261,5,48,0,0,257,258,5,179,0,0,258,259,5,148,
        0,0,259,261,3,66,33,0,260,251,1,0,0,0,260,254,1,0,0,0,260,257,1,
        0,0,0,261,25,1,0,0,0,262,265,5,35,0,0,263,266,1,0,0,0,264,266,3,
        70,35,0,265,263,1,0,0,0,265,264,1,0,0,0,266,27,1,0,0,0,267,268,5,
        30,0,0,268,269,3,70,35,0,269,29,1,0,0,0,270,271,5,5,0,0,271,272,
        3,46,23,0,272,273,3,48,24,0,273,31,1,0,0,0,274,275,5,21,0,0,275,
        276,3,46,23,0,276,277,3,48,24,0,277,33,1,0,0,0,278,279,5,27,0,0,
        279,280,5,179,0,0,280,35,1,0,0,0,281,283,3,38,19,0,282,281,1,0,0,
        0,283,284,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,37,1,0,0,0,
        286,287,5,29,0,0,287,288,3,40,20,0,288,289,7,2,0,0,289,290,3,70,
        35,0,290,39,1,0,0,0,291,295,5,22,0,0,292,293,5,132,0,0,293,294,5,
        49,0,0,294,296,5,133,0,0,295,292,1,0,0,0,295,296,1,0,0,0,296,306,
        1,0,0,0,297,306,5,33,0,0,298,302,5,31,0,0,299,300,5,132,0,0,300,
        301,5,49,0,0,301,303,5,133,0,0,302,299,1,0,0,0,302,303,1,0,0,0,303,
        306,1,0,0,0,304,306,5,179,0,0,305,291,1,0,0,0,305,297,1,0,0,0,305,
        298,1,0,0,0,305,304,1,0,0,0,306,41,1,0,0,0,307,308,5,26,0,0,308,
        309,3,76,38,0,309,43,1,0,0,0,310,314,5,22,0,0,311,312,5,132,0,0,
        312,313,5,49,0,0,313,315,5,133,0,0,314,311,1,0,0,0,314,315,1,0,0,
        0,315,318,1,0,0,0,316,318,5,179,0,0,317,310,1,0,0,0,317,316,1,0,
        0,0,318,45,1,0,0,0,319,320,5,132,0,0,320,321,3,70,35,0,321,322,5,
        169,0,0,322,323,3,70,35,0,323,324,5,169,0,0,324,325,3,70,35,0,325,
        326,5,133,0,0,326,47,1,0,0,0,327,334,5,4,0,0,328,331,5,20,0,0,329,
        332,5,4,0,0,330,332,3,44,22,0,331,329,1,0,0,0,331,330,1,0,0,0,332,
        334,1,0,0,0,333,327,1,0,0,0,333,328,1,0,0,0,334,49,1,0,0,0,335,336,
        5,39,0,0,336,337,5,52,0,0,337,51,1,0,0,0,338,339,5,10,0,0,339,348,
        3,76,38,0,340,341,5,10,0,0,341,342,5,34,0,0,342,345,5,179,0,0,343,
        344,5,26,0,0,344,346,3,76,38,0,345,343,1,0,0,0,345,346,1,0,0,0,346,
        348,1,0,0,0,347,338,1,0,0,0,347,340,1,0,0,0,348,53,1,0,0,0,349,350,
        5,8,0,0,350,351,3,76,38,0,351,55,1,0,0,0,352,353,5,15,0,0,353,362,
        3,76,38,0,354,355,5,15,0,0,355,356,5,34,0,0,356,359,5,179,0,0,357,
        358,5,26,0,0,358,360,3,76,38,0,359,357,1,0,0,0,359,360,1,0,0,0,360,
        362,1,0,0,0,361,352,1,0,0,0,361,354,1,0,0,0,362,57,1,0,0,0,363,364,
        5,28,0,0,364,373,3,76,38,0,365,366,5,28,0,0,366,367,5,34,0,0,367,
        370,5,179,0,0,368,369,5,26,0,0,369,371,3,76,38,0,370,368,1,0,0,0,
        370,371,1,0,0,0,371,373,1,0,0,0,372,363,1,0,0,0,372,365,1,0,0,0,
        373,59,1,0,0,0,374,375,5,14,0,0,375,384,3,76,38,0,376,377,5,14,0,
        0,377,378,5,34,0,0,378,381,5,179,0,0,379,380,5,26,0,0,380,382,3,
        76,38,0,381,379,1,0,0,0,381,382,1,0,0,0,382,384,1,0,0,0,383,374,
        1,0,0,0,383,376,1,0,0,0,384,61,1,0,0,0,385,386,5,42,0,0,386,387,
        7,3,0,0,387,388,7,3,0,0,388,389,3,76,38,0,389,63,1,0,0,0,390,391,
        5,6,0,0,391,392,7,3,0,0,392,65,1,0,0,0,393,394,5,136,0,0,394,399,
        3,70,35,0,395,396,5,169,0,0,396,398,3,70,35,0,397,395,1,0,0,0,398,
        401,1,0,0,0,399,397,1,0,0,0,399,400,1,0,0,0,400,402,1,0,0,0,401,
        399,1,0,0,0,402,403,5,137,0,0,403,67,1,0,0,0,404,405,5,179,0,0,405,
        406,5,148,0,0,406,407,3,70,35,0,407,69,1,0,0,0,408,409,6,35,-1,0,
        409,453,5,1,0,0,410,453,5,49,0,0,411,453,5,51,0,0,412,414,5,52,0,
        0,413,412,1,0,0,0,414,417,1,0,0,0,415,413,1,0,0,0,415,416,1,0,0,
        0,416,453,1,0,0,0,417,415,1,0,0,0,418,419,5,179,0,0,419,420,5,171,
        0,0,420,453,3,70,35,23,421,422,5,179,0,0,422,423,5,176,0,0,423,453,
        3,70,35,22,424,425,5,179,0,0,425,426,5,134,0,0,426,427,3,70,35,0,
        427,428,5,135,0,0,428,453,1,0,0,0,429,430,5,179,0,0,430,431,5,132,
        0,0,431,436,3,70,35,0,432,433,5,169,0,0,433,435,3,70,35,0,434,432,
        1,0,0,0,435,438,1,0,0,0,436,434,1,0,0,0,436,437,1,0,0,0,437,439,
        1,0,0,0,438,436,1,0,0,0,439,440,5,133,0,0,440,453,1,0,0,0,441,442,
        5,132,0,0,442,443,3,70,35,0,443,444,5,133,0,0,444,453,1,0,0,0,445,
        446,7,4,0,0,446,453,3,70,35,18,447,453,5,179,0,0,448,449,5,147,0,
        0,449,453,3,70,35,5,450,453,5,22,0,0,451,453,5,33,0,0,452,408,1,
        0,0,0,452,410,1,0,0,0,452,411,1,0,0,0,452,415,1,0,0,0,452,418,1,
        0,0,0,452,421,1,0,0,0,452,424,1,0,0,0,452,429,1,0,0,0,452,441,1,
        0,0,0,452,445,1,0,0,0,452,447,1,0,0,0,452,448,1,0,0,0,452,450,1,
        0,0,0,452,451,1,0,0,0,453,498,1,0,0,0,454,455,10,17,0,0,455,456,
        5,143,0,0,456,497,3,70,35,17,457,458,10,16,0,0,458,459,7,5,0,0,459,
        497,3,70,35,17,460,461,10,15,0,0,461,462,7,4,0,0,462,497,3,70,35,
        16,463,464,10,14,0,0,464,465,5,142,0,0,465,497,3,70,35,15,466,467,
        10,13,0,0,467,468,5,2,0,0,468,497,3,70,35,14,469,470,10,12,0,0,470,
        471,5,3,0,0,471,497,3,70,35,13,472,473,10,10,0,0,473,474,5,161,0,
        0,474,497,3,70,35,11,475,476,10,9,0,0,476,477,5,163,0,0,477,497,
        3,70,35,10,478,479,10,8,0,0,479,480,5,164,0,0,480,497,3,70,35,9,
        481,482,10,7,0,0,482,483,5,149,0,0,483,497,3,70,35,8,484,485,10,
        6,0,0,485,486,5,150,0,0,486,497,3,70,35,7,487,488,10,4,0,0,488,489,
        7,6,0,0,489,497,3,70,35,5,490,491,10,3,0,0,491,492,5,172,0,0,492,
        493,3,70,35,0,493,494,5,173,0,0,494,495,3,70,35,4,495,497,1,0,0,
        0,496,454,1,0,0,0,496,457,1,0,0,0,496,460,1,0,0,0,496,463,1,0,0,
        0,496,466,1,0,0,0,496,469,1,0,0,0,496,472,1,0,0,0,496,475,1,0,0,
        0,496,478,1,0,0,0,496,481,1,0,0,0,496,484,1,0,0,0,496,487,1,0,0,
        0,496,490,1,0,0,0,497,500,1,0,0,0,498,496,1,0,0,0,498,499,1,0,0,
        0,499,71,1,0,0,0,500,498,1,0,0,0,501,502,5,40,0,0,502,503,5,52,0,
        0,503,73,1,0,0,0,504,505,5,41,0,0,505,510,5,52,0,0,506,507,5,41,
        0,0,507,508,5,40,0,0,508,510,5,52,0,0,509,504,1,0,0,0,509,506,1,
        0,0,0,510,75,1,0,0,0,511,512,5,46,0,0,512,77,1,0,0,0,63,86,89,92,
        95,98,101,104,108,111,121,124,129,133,137,142,146,151,155,159,161,
        170,172,174,179,185,188,191,198,201,205,208,211,214,219,228,236,
        244,247,260,265,284,295,302,305,314,317,331,333,345,347,359,361,
        370,372,381,383,399,415,436,452,496,498,509
    ]

class McInstrParser ( Parser ):

    grammarFileName = "McInstr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'0'", "'>>'", "'<<'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'string'", "'vector'", "'symbol'", "<INVALID>", 
                     "'%include'", "'NULL'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'alignas'", "'alignof'", 
                     "'asm'", "'auto'", "'bool'", "'break'", "'case'", "'catch'", 
                     "'char'", "'char16_t'", "'char32_t'", "'class'", "'const'", 
                     "'constexpr'", "'const_cast'", "'continue'", "'decltype'", 
                     "'default'", "'delete'", "'do'", "'double'", "'dynamic_cast'", 
                     "'else'", "'enum'", "'explicit'", "'export'", "'extern'", 
                     "'false'", "'final'", "'float'", "'for'", "'friend'", 
                     "'goto'", "'if'", "'inline'", "'int'", "'long'", "'mutable'", 
                     "'namespace'", "'new'", "'noexcept'", "'nullptr'", 
                     "'operator'", "'override'", "'protected'", "'public'", 
                     "'register'", "'reinterpret_cast'", "'return'", "'short'", 
                     "'signed'", "'sizeof'", "'static'", "'static_assert'", 
                     "'static_cast'", "'struct'", "'switch'", "'template'", 
                     "'this'", "'thread_local'", "'throw'", "'true'", "'try'", 
                     "'typedef'", "'typeid'", "'typename'", "'union'", "'unsigned'", 
                     "'using'", "'virtual'", "'void'", "'volatile'", "'wchar_t'", 
                     "'while'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'&'", "'|'", 
                     "'~'", "<INVALID>", "'='", "'<'", "'>'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'^='", "'&='", "'|='", "'<<='", 
                     "'>>='", "'=='", "'!='", "'<='", "'>='", "<INVALID>", 
                     "<INVALID>", "'++'", "'--'", "','", "'->*'", "'->'", 
                     "'?'", "':'", "'::'", "';'", "'.'", "'.*'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Absolute", "At", "Category", "Component", "UserVars", 
                      "Define", "Declare", "Definition", "End", "McDisplay", 
                      "Finally", "Initialize", "Instrument", "Output", "Private", 
                      "Parameters", "Relative", "Rotated", "Previous", "Setting", 
                      "Trace", "Share", "Extend", "Group", "Save", "Jump", 
                      "When", "Next", "Iterate", "Myself", "Copy", "Split", 
                      "Removable", "Cpu", "NoAcc", "Dependency", "Shell", 
                      "Search", "MetaData", "String", "Vector", "Symbol", 
                      "UnparsedBlock", "Include", "Null", "IntegerLiteral", 
                      "CharacterLiteral", "FloatingLiteral", "StringLiteral", 
                      "BooleanLitteral", "PointerLiteral", "UserDefinedLiteral", 
                      "MultiLineMacro", "Directive", "Alignas", "Alignof", 
                      "Asm", "Auto", "Bool", "Break", "Case", "Catch", "Char", 
                      "Char16", "Char32", "Class", "Const", "Constexpr", 
                      "Const_cast", "Continue", "Decltype", "Default", "Delete", 
                      "Do", "Double", "Dynamic_cast", "Else", "Enum", "Explicit", 
                      "Export", "Extern", "False_", "Final", "Float", "For", 
                      "Friend", "Goto", "If", "Inline", "Int", "Long", "Mutable", 
                      "Namespace", "New", "Noexcept", "Nullptr", "Operator", 
                      "Override", "Protected", "Public", "Register", "Reinterpret_cast", 
                      "Return", "Short", "Signed", "Sizeof", "Static", "Static_assert", 
                      "Static_cast", "Struct", "Switch", "Template", "This", 
                      "Thread_local", "Throw", "True_", "Try", "Typedef", 
                      "Typeid_", "Typename_", "Union", "Unsigned", "Using", 
                      "Virtual", "Void", "Volatile", "Wchar", "While", "LeftParen", 
                      "RightParen", "LeftBracket", "RightBracket", "LeftBrace", 
                      "RightBrace", "Plus", "Minus", "Star", "Div", "Mod", 
                      "Caret", "And", "Or", "Tilde", "Not", "Assign", "Less", 
                      "Greater", "PlusAssign", "MinusAssign", "StarAssign", 
                      "DivAssign", "ModAssign", "XorAssign", "AndAssign", 
                      "OrAssign", "LeftShiftAssign", "RightShiftAssign", 
                      "Equal", "NotEqual", "LessEqual", "GreaterEqual", 
                      "AndAnd", "OrOr", "PlusPlus", "MinusMinus", "Comma", 
                      "ArrowStar", "Arrow", "Question", "Colon", "Doublecolon", 
                      "Semi", "Dot", "DotStar", "Ellipsis", "Identifier", 
                      "DecimalLiteral", "OctalLiteral", "HexadecimalLiteral", 
                      "BinaryLiteral", "IntegerSuffix", "UserDefinedIntegerLiteral", 
                      "UserDefinedFloatingLiteral", "UserDefinedStringLiteral", 
                      "UserDefinedCharacterLiteral", "Whitespace", "Newline", 
                      "BlockComment", "LineComment" ]

    RULE_prog = 0
    RULE_instrument_definition = 1
    RULE_instrument_parameters = 2
    RULE_instrument_parameter = 3
    RULE_instrument_parameter_unit = 4
    RULE_instrument_trace = 5
    RULE_instrument_metadata = 6
    RULE_instrument_trace_include = 7
    RULE_component_instance = 8
    RULE_instance_name = 9
    RULE_component_type = 10
    RULE_instance_parameters = 11
    RULE_instance_parameter = 12
    RULE_split = 13
    RULE_when = 14
    RULE_place = 15
    RULE_orientation = 16
    RULE_groupref = 17
    RULE_jumps = 18
    RULE_jump = 19
    RULE_jumpname = 20
    RULE_extend = 21
    RULE_component_ref = 22
    RULE_coords = 23
    RULE_reference = 24
    RULE_dependency = 25
    RULE_declare = 26
    RULE_uservars = 27
    RULE_initialize = 28
    RULE_save = 29
    RULE_finally_ = 30
    RULE_metadata = 31
    RULE_category = 32
    RULE_initializerlist = 33
    RULE_assignment = 34
    RULE_expr = 35
    RULE_shell = 36
    RULE_search = 37
    RULE_unparsed_block = 38

    ruleNames =  [ "prog", "instrument_definition", "instrument_parameters", 
                   "instrument_parameter", "instrument_parameter_unit", 
                   "instrument_trace", "instrument_metadata", "instrument_trace_include", 
                   "component_instance", "instance_name", "component_type", 
                   "instance_parameters", "instance_parameter", "split", 
                   "when", "place", "orientation", "groupref", "jumps", 
                   "jump", "jumpname", "extend", "component_ref", "coords", 
                   "reference", "dependency", "declare", "uservars", "initialize", 
                   "save", "finally_", "metadata", "category", "initializerlist", 
                   "assignment", "expr", "shell", "search", "unparsed_block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Absolute=4
    At=5
    Category=6
    Component=7
    UserVars=8
    Define=9
    Declare=10
    Definition=11
    End=12
    McDisplay=13
    Finally=14
    Initialize=15
    Instrument=16
    Output=17
    Private=18
    Parameters=19
    Relative=20
    Rotated=21
    Previous=22
    Setting=23
    Trace=24
    Share=25
    Extend=26
    Group=27
    Save=28
    Jump=29
    When=30
    Next=31
    Iterate=32
    Myself=33
    Copy=34
    Split=35
    Removable=36
    Cpu=37
    NoAcc=38
    Dependency=39
    Shell=40
    Search=41
    MetaData=42
    String=43
    Vector=44
    Symbol=45
    UnparsedBlock=46
    Include=47
    Null=48
    IntegerLiteral=49
    CharacterLiteral=50
    FloatingLiteral=51
    StringLiteral=52
    BooleanLitteral=53
    PointerLiteral=54
    UserDefinedLiteral=55
    MultiLineMacro=56
    Directive=57
    Alignas=58
    Alignof=59
    Asm=60
    Auto=61
    Bool=62
    Break=63
    Case=64
    Catch=65
    Char=66
    Char16=67
    Char32=68
    Class=69
    Const=70
    Constexpr=71
    Const_cast=72
    Continue=73
    Decltype=74
    Default=75
    Delete=76
    Do=77
    Double=78
    Dynamic_cast=79
    Else=80
    Enum=81
    Explicit=82
    Export=83
    Extern=84
    False_=85
    Final=86
    Float=87
    For=88
    Friend=89
    Goto=90
    If=91
    Inline=92
    Int=93
    Long=94
    Mutable=95
    Namespace=96
    New=97
    Noexcept=98
    Nullptr=99
    Operator=100
    Override=101
    Protected=102
    Public=103
    Register=104
    Reinterpret_cast=105
    Return=106
    Short=107
    Signed=108
    Sizeof=109
    Static=110
    Static_assert=111
    Static_cast=112
    Struct=113
    Switch=114
    Template=115
    This=116
    Thread_local=117
    Throw=118
    True_=119
    Try=120
    Typedef=121
    Typeid_=122
    Typename_=123
    Union=124
    Unsigned=125
    Using=126
    Virtual=127
    Void=128
    Volatile=129
    Wchar=130
    While=131
    LeftParen=132
    RightParen=133
    LeftBracket=134
    RightBracket=135
    LeftBrace=136
    RightBrace=137
    Plus=138
    Minus=139
    Star=140
    Div=141
    Mod=142
    Caret=143
    And=144
    Or=145
    Tilde=146
    Not=147
    Assign=148
    Less=149
    Greater=150
    PlusAssign=151
    MinusAssign=152
    StarAssign=153
    DivAssign=154
    ModAssign=155
    XorAssign=156
    AndAssign=157
    OrAssign=158
    LeftShiftAssign=159
    RightShiftAssign=160
    Equal=161
    NotEqual=162
    LessEqual=163
    GreaterEqual=164
    AndAnd=165
    OrOr=166
    PlusPlus=167
    MinusMinus=168
    Comma=169
    ArrowStar=170
    Arrow=171
    Question=172
    Colon=173
    Doublecolon=174
    Semi=175
    Dot=176
    DotStar=177
    Ellipsis=178
    Identifier=179
    DecimalLiteral=180
    OctalLiteral=181
    HexadecimalLiteral=182
    BinaryLiteral=183
    IntegerSuffix=184
    UserDefinedIntegerLiteral=185
    UserDefinedFloatingLiteral=186
    UserDefinedStringLiteral=187
    UserDefinedCharacterLiteral=188
    Whitespace=189
    Newline=190
    BlockComment=191
    LineComment=192

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrument_definition(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_definitionContext,0)


        def EOF(self):
            return self.getToken(McInstrParser.EOF, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = McInstrParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.instrument_definition()
            self.state = 79
            self.match(McInstrParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Define(self):
            return self.getToken(McInstrParser.Define, 0)

        def Instrument(self):
            return self.getToken(McInstrParser.Instrument, 0)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def instrument_parameters(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_parametersContext,0)


        def instrument_trace(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_traceContext,0)


        def End(self):
            return self.getToken(McInstrParser.End, 0)

        def shell(self):
            return self.getTypedRuleContext(McInstrParser.ShellContext,0)


        def search(self):
            return self.getTypedRuleContext(McInstrParser.SearchContext,0)


        def instrument_metadata(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_metadataContext,0)


        def dependency(self):
            return self.getTypedRuleContext(McInstrParser.DependencyContext,0)


        def declare(self):
            return self.getTypedRuleContext(McInstrParser.DeclareContext,0)


        def uservars(self):
            return self.getTypedRuleContext(McInstrParser.UservarsContext,0)


        def initialize(self):
            return self.getTypedRuleContext(McInstrParser.InitializeContext,0)


        def save(self):
            return self.getTypedRuleContext(McInstrParser.SaveContext,0)


        def finally_(self):
            return self.getTypedRuleContext(McInstrParser.Finally_Context,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_definition" ):
                listener.enterInstrument_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_definition" ):
                listener.exitInstrument_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_definition" ):
                return visitor.visitInstrument_definition(self)
            else:
                return visitor.visitChildren(self)




    def instrument_definition(self):

        localctx = McInstrParser.Instrument_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrument_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(McInstrParser.Define)
            self.state = 82
            self.match(McInstrParser.Instrument)
            self.state = 83
            self.match(McInstrParser.Identifier)
            self.state = 84
            self.instrument_parameters()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 85
                self.shell()


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 88
                self.search()


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 91
                self.instrument_metadata()


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 94
                self.dependency()


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 97
                self.declare()


            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 100
                self.uservars()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 103
                self.initialize()


            self.state = 106
            self.instrument_trace()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 107
                self.save()


            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 110
                self.finally_()


            self.state = 113
            self.match(McInstrParser.End)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._instrument_parameter = None # Instrument_parameterContext
            self.params = list() # of Instrument_parameterContexts

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def instrument_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Instrument_parameterContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Instrument_parameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Comma)
            else:
                return self.getToken(McInstrParser.Comma, i)

        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_parameters" ):
                listener.enterInstrument_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_parameters" ):
                listener.exitInstrument_parameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_parameters" ):
                return visitor.visitInstrument_parameters(self)
            else:
                return visitor.visitChildren(self)




    def instrument_parameters(self):

        localctx = McInstrParser.Instrument_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instrument_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(McInstrParser.LeftParen)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 43)) & ~0x3f) == 0 and ((1 << (_la - 43)) & 1125934274969601) != 0) or _la==179:
                self.state = 116
                localctx._instrument_parameter = self.instrument_parameter()
                localctx.params.append(localctx._instrument_parameter)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==169:
                    self.state = 117
                    self.match(McInstrParser.Comma)
                    self.state = 118
                    localctx._instrument_parameter = self.instrument_parameter()
                    localctx.params.append(localctx._instrument_parameter)
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 126
            self.match(McInstrParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_parameter

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstrumentParameterIntegerContext(Instrument_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instrument_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Int(self):
            return self.getToken(McInstrParser.Int, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def instrument_parameter_unit(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_parameter_unitContext,0)

        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrumentParameterInteger" ):
                listener.enterInstrumentParameterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrumentParameterInteger" ):
                listener.exitInstrumentParameterInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrumentParameterInteger" ):
                return visitor.visitInstrumentParameterInteger(self)
            else:
                return visitor.visitChildren(self)


    class InstrumentParameterDoubleContext(Instrument_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instrument_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Double(self):
            return self.getToken(McInstrParser.Double, 0)
        def instrument_parameter_unit(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_parameter_unitContext,0)

        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrumentParameterDouble" ):
                listener.enterInstrumentParameterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrumentParameterDouble" ):
                listener.exitInstrumentParameterDouble(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrumentParameterDouble" ):
                return visitor.visitInstrumentParameterDouble(self)
            else:
                return visitor.visitChildren(self)


    class InstrumentParameterStringContext(Instrument_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instrument_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def String(self):
            return self.getToken(McInstrParser.String, 0)
        def instrument_parameter_unit(self):
            return self.getTypedRuleContext(McInstrParser.Instrument_parameter_unitContext,0)

        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def Char(self):
            return self.getToken(McInstrParser.Char, 0)
        def Star(self):
            return self.getToken(McInstrParser.Star, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)
        def Null(self):
            return self.getToken(McInstrParser.Null, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrumentParameterString" ):
                listener.enterInstrumentParameterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrumentParameterString" ):
                listener.exitInstrumentParameterString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrumentParameterString" ):
                return visitor.visitInstrumentParameterString(self)
            else:
                return visitor.visitChildren(self)



    def instrument_parameter(self):

        localctx = McInstrParser.Instrument_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instrument_parameter)
        self._la = 0 # Token type
        try:
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [78, 179]:
                localctx = McInstrParser.InstrumentParameterDoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==78:
                    self.state = 128
                    self.match(McInstrParser.Double)


                self.state = 131
                self.match(McInstrParser.Identifier)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==141:
                    self.state = 132
                    self.instrument_parameter_unit()


                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==148:
                    self.state = 135
                    self.match(McInstrParser.Assign)
                    self.state = 136
                    self.expr(0)


                pass
            elif token in [93]:
                localctx = McInstrParser.InstrumentParameterIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(McInstrParser.Int)
                self.state = 140
                self.match(McInstrParser.Identifier)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==141:
                    self.state = 141
                    self.instrument_parameter_unit()


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==148:
                    self.state = 144
                    self.match(McInstrParser.Assign)
                    self.state = 145
                    self.expr(0)


                pass
            elif token in [43, 66]:
                localctx = McInstrParser.InstrumentParameterStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [43]:
                    self.state = 148
                    self.match(McInstrParser.String)
                    pass
                elif token in [66]:
                    self.state = 149
                    self.match(McInstrParser.Char)
                    self.state = 150
                    self.match(McInstrParser.Star)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 153
                self.match(McInstrParser.Identifier)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==141:
                    self.state = 154
                    self.instrument_parameter_unit()


                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==148:
                    self.state = 157
                    self.match(McInstrParser.Assign)
                    self.state = 158
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4785074604081154) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_parameter_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Div(self):
            return self.getToken(McInstrParser.Div, 0)

        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_parameter_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_parameter_unit" ):
                listener.enterInstrument_parameter_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_parameter_unit" ):
                listener.exitInstrument_parameter_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_parameter_unit" ):
                return visitor.visitInstrument_parameter_unit(self)
            else:
                return visitor.visitChildren(self)




    def instrument_parameter_unit(self):

        localctx = McInstrParser.Instrument_parameter_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instrument_parameter_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(McInstrParser.Div)
            self.state = 164
            self.match(McInstrParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_traceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Trace(self):
            return self.getToken(McInstrParser.Trace, 0)

        def component_instance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Component_instanceContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Component_instanceContext,i)


        def search(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.SearchContext)
            else:
                return self.getTypedRuleContext(McInstrParser.SearchContext,i)


        def instrument_trace_include(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Instrument_trace_includeContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Instrument_trace_includeContext,i)


        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_trace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_trace" ):
                listener.enterInstrument_trace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_trace" ):
                listener.exitInstrument_trace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_trace" ):
                return visitor.visitInstrument_trace(self)
            else:
                return visitor.visitChildren(self)




    def instrument_trace(self):

        localctx = McInstrParser.Instrument_traceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instrument_trace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(McInstrParser.Trace)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 143177029779584) != 0):
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 170
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [7, 35, 36, 37]:
                        self.state = 167
                        self.component_instance()
                        pass
                    elif token in [41]:
                        self.state = 168
                        self.search()
                        pass
                    elif token in [47]:
                        self.state = 169
                        self.instrument_trace_include()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 172 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 143177029779584) != 0)):
                        break



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_metadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metadata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.MetadataContext)
            else:
                return self.getTypedRuleContext(McInstrParser.MetadataContext,i)


        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_metadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_metadata" ):
                listener.enterInstrument_metadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_metadata" ):
                listener.exitInstrument_metadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_metadata" ):
                return visitor.visitInstrument_metadata(self)
            else:
                return visitor.visitChildren(self)




    def instrument_metadata(self):

        localctx = McInstrParser.Instrument_metadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instrument_metadata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 176
                self.metadata()
                self.state = 179 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==42):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrument_trace_includeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Include(self):
            return self.getToken(McInstrParser.Include, 0)

        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_instrument_trace_include

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrument_trace_include" ):
                listener.enterInstrument_trace_include(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrument_trace_include" ):
                listener.exitInstrument_trace_include(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrument_trace_include" ):
                return visitor.visitInstrument_trace_include(self)
            else:
                return visitor.visitChildren(self)




    def instrument_trace_include(self):

        localctx = McInstrParser.Instrument_trace_includeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instrument_trace_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(McInstrParser.Include)
            self.state = 182
            self.match(McInstrParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_instanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Component(self):
            return self.getToken(McInstrParser.Component, 0)

        def instance_name(self):
            return self.getTypedRuleContext(McInstrParser.Instance_nameContext,0)


        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)

        def component_type(self):
            return self.getTypedRuleContext(McInstrParser.Component_typeContext,0)


        def place(self):
            return self.getTypedRuleContext(McInstrParser.PlaceContext,0)


        def Removable(self):
            return self.getToken(McInstrParser.Removable, 0)

        def Cpu(self):
            return self.getToken(McInstrParser.Cpu, 0)

        def split(self):
            return self.getTypedRuleContext(McInstrParser.SplitContext,0)


        def instance_parameters(self):
            return self.getTypedRuleContext(McInstrParser.Instance_parametersContext,0)


        def when(self):
            return self.getTypedRuleContext(McInstrParser.WhenContext,0)


        def orientation(self):
            return self.getTypedRuleContext(McInstrParser.OrientationContext,0)


        def groupref(self):
            return self.getTypedRuleContext(McInstrParser.GrouprefContext,0)


        def extend(self):
            return self.getTypedRuleContext(McInstrParser.ExtendContext,0)


        def jumps(self):
            return self.getTypedRuleContext(McInstrParser.JumpsContext,0)


        def metadata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.MetadataContext)
            else:
                return self.getTypedRuleContext(McInstrParser.MetadataContext,i)


        def getRuleIndex(self):
            return McInstrParser.RULE_component_instance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_instance" ):
                listener.enterComponent_instance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_instance" ):
                listener.exitComponent_instance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent_instance" ):
                return visitor.visitComponent_instance(self)
            else:
                return visitor.visitChildren(self)




    def component_instance(self):

        localctx = McInstrParser.Component_instanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_component_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 184
                self.match(McInstrParser.Removable)


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 187
                self.match(McInstrParser.Cpu)


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 190
                self.split()


            self.state = 193
            self.match(McInstrParser.Component)
            self.state = 194
            self.instance_name()
            self.state = 195
            self.match(McInstrParser.Assign)
            self.state = 196
            self.component_type()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==132:
                self.state = 197
                self.instance_parameters()


            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 200
                self.when()


            self.state = 203
            self.place()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 204
                self.orientation()


            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 207
                self.groupref()


            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 210
                self.extend()


            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 213
                self.jumps()


            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 216
                self.metadata()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_instance_name

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstanceNameCopyIdentifierContext(Instance_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceNameCopyIdentifier" ):
                listener.enterInstanceNameCopyIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceNameCopyIdentifier" ):
                listener.exitInstanceNameCopyIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceNameCopyIdentifier" ):
                return visitor.visitInstanceNameCopyIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class InstanceNameCopyContext(Instance_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Myself(self):
            return self.getToken(McInstrParser.Myself, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceNameCopy" ):
                listener.enterInstanceNameCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceNameCopy" ):
                listener.exitInstanceNameCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceNameCopy" ):
                return visitor.visitInstanceNameCopy(self)
            else:
                return visitor.visitChildren(self)


    class InstanceNameIdentifierContext(Instance_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceNameIdentifier" ):
                listener.enterInstanceNameIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceNameIdentifier" ):
                listener.exitInstanceNameIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceNameIdentifier" ):
                return visitor.visitInstanceNameIdentifier(self)
            else:
                return visitor.visitChildren(self)



    def instance_name(self):

        localctx = McInstrParser.Instance_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_instance_name)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InstanceNameCopyIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(McInstrParser.Copy)
                self.state = 223
                self.match(McInstrParser.LeftParen)
                self.state = 224
                self.match(McInstrParser.Identifier)
                self.state = 225
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 2:
                localctx = McInstrParser.InstanceNameCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = McInstrParser.InstanceNameIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(McInstrParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_component_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComponentTypeIdentifierContext(Component_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Component_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentTypeIdentifier" ):
                listener.enterComponentTypeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentTypeIdentifier" ):
                listener.exitComponentTypeIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponentTypeIdentifier" ):
                return visitor.visitComponentTypeIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ComponentTypeCopyContext(Component_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Component_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def component_ref(self):
            return self.getTypedRuleContext(McInstrParser.Component_refContext,0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponentTypeCopy" ):
                listener.enterComponentTypeCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponentTypeCopy" ):
                listener.exitComponentTypeCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponentTypeCopy" ):
                return visitor.visitComponentTypeCopy(self)
            else:
                return visitor.visitChildren(self)



    def component_type(self):

        localctx = McInstrParser.Component_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_component_type)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                localctx = McInstrParser.ComponentTypeCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(McInstrParser.Copy)
                self.state = 231
                self.match(McInstrParser.LeftParen)
                self.state = 232
                self.component_ref()
                self.state = 233
                self.match(McInstrParser.RightParen)
                pass
            elif token in [179]:
                localctx = McInstrParser.ComponentTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(McInstrParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._instance_parameter = None # Instance_parameterContext
            self.params = list() # of Instance_parameterContexts

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def instance_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Instance_parameterContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Instance_parameterContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Comma)
            else:
                return self.getToken(McInstrParser.Comma, i)

        def getRuleIndex(self):
            return McInstrParser.RULE_instance_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_parameters" ):
                listener.enterInstance_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_parameters" ):
                listener.exitInstance_parameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_parameters" ):
                return visitor.visitInstance_parameters(self)
            else:
                return visitor.visitChildren(self)




    def instance_parameters(self):

        localctx = McInstrParser.Instance_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instance_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(McInstrParser.LeftParen)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==179:
                self.state = 239
                localctx._instance_parameter = self.instance_parameter()
                localctx.params.append(localctx._instance_parameter)
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==169:
                    self.state = 240
                    self.match(McInstrParser.Comma)
                    self.state = 241
                    localctx._instance_parameter = self.instance_parameter()
                    localctx.params.append(localctx._instance_parameter)
                    self.state = 246
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 249
            self.match(McInstrParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_instance_parameter

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstanceParameterExprContext(Instance_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceParameterExpr" ):
                listener.enterInstanceParameterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceParameterExpr" ):
                listener.exitInstanceParameterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceParameterExpr" ):
                return visitor.visitInstanceParameterExpr(self)
            else:
                return visitor.visitChildren(self)


    class InstanceParameterNullContext(Instance_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def Null(self):
            return self.getToken(McInstrParser.Null, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceParameterNull" ):
                listener.enterInstanceParameterNull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceParameterNull" ):
                listener.exitInstanceParameterNull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceParameterNull" ):
                return visitor.visitInstanceParameterNull(self)
            else:
                return visitor.visitChildren(self)


    class InstanceParameterVectorContext(Instance_parameterContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_parameterContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def initializerlist(self):
            return self.getTypedRuleContext(McInstrParser.InitializerlistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceParameterVector" ):
                listener.enterInstanceParameterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceParameterVector" ):
                listener.exitInstanceParameterVector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceParameterVector" ):
                return visitor.visitInstanceParameterVector(self)
            else:
                return visitor.visitChildren(self)



    def instance_parameter(self):

        localctx = McInstrParser.Instance_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_instance_parameter)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InstanceParameterExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(McInstrParser.Identifier)
                self.state = 252
                self.match(McInstrParser.Assign)
                self.state = 253
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = McInstrParser.InstanceParameterNullContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(McInstrParser.Identifier)
                self.state = 255
                self.match(McInstrParser.Assign)
                self.state = 256
                self.match(McInstrParser.Null)
                pass

            elif la_ == 3:
                localctx = McInstrParser.InstanceParameterVectorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(McInstrParser.Identifier)
                self.state = 258
                self.match(McInstrParser.Assign)
                self.state = 259
                self.initializerlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Split(self):
            return self.getToken(McInstrParser.Split, 0)

        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_split

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplit" ):
                listener.enterSplit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplit" ):
                listener.exitSplit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplit" ):
                return visitor.visitSplit(self)
            else:
                return visitor.visitChildren(self)




    def split(self):

        localctx = McInstrParser.SplitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(McInstrParser.Split)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 264
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def When(self):
            return self.getToken(McInstrParser.When, 0)

        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_when

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhen" ):
                listener.enterWhen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhen" ):
                listener.exitWhen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhen" ):
                return visitor.visitWhen(self)
            else:
                return visitor.visitChildren(self)




    def when(self):

        localctx = McInstrParser.WhenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_when)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(McInstrParser.When)
            self.state = 268
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def At(self):
            return self.getToken(McInstrParser.At, 0)

        def coords(self):
            return self.getTypedRuleContext(McInstrParser.CoordsContext,0)


        def reference(self):
            return self.getTypedRuleContext(McInstrParser.ReferenceContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_place

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlace" ):
                listener.enterPlace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlace" ):
                listener.exitPlace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlace" ):
                return visitor.visitPlace(self)
            else:
                return visitor.visitChildren(self)




    def place(self):

        localctx = McInstrParser.PlaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_place)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(McInstrParser.At)
            self.state = 271
            self.coords()
            self.state = 272
            self.reference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrientationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Rotated(self):
            return self.getToken(McInstrParser.Rotated, 0)

        def coords(self):
            return self.getTypedRuleContext(McInstrParser.CoordsContext,0)


        def reference(self):
            return self.getTypedRuleContext(McInstrParser.ReferenceContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_orientation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrientation" ):
                listener.enterOrientation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrientation" ):
                listener.exitOrientation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrientation" ):
                return visitor.visitOrientation(self)
            else:
                return visitor.visitChildren(self)




    def orientation(self):

        localctx = McInstrParser.OrientationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_orientation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(McInstrParser.Rotated)
            self.state = 275
            self.coords()
            self.state = 276
            self.reference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrouprefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Group(self):
            return self.getToken(McInstrParser.Group, 0)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_groupref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupref" ):
                listener.enterGroupref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupref" ):
                listener.exitGroupref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupref" ):
                return visitor.visitGroupref(self)
            else:
                return visitor.visitChildren(self)




    def groupref(self):

        localctx = McInstrParser.GrouprefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_groupref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(McInstrParser.Group)
            self.state = 279
            self.match(McInstrParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def jump(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.JumpContext)
            else:
                return self.getTypedRuleContext(McInstrParser.JumpContext,i)


        def getRuleIndex(self):
            return McInstrParser.RULE_jumps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumps" ):
                listener.enterJumps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumps" ):
                listener.exitJumps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumps" ):
                return visitor.visitJumps(self)
            else:
                return visitor.visitChildren(self)




    def jumps(self):

        localctx = McInstrParser.JumpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_jumps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 281
                self.jump()
                self.state = 284 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==29):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Jump(self):
            return self.getToken(McInstrParser.Jump, 0)

        def jumpname(self):
            return self.getTypedRuleContext(McInstrParser.JumpnameContext,0)


        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def When(self):
            return self.getToken(McInstrParser.When, 0)

        def Iterate(self):
            return self.getToken(McInstrParser.Iterate, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump" ):
                return visitor.visitJump(self)
            else:
                return visitor.visitChildren(self)




    def jump(self):

        localctx = McInstrParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_jump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(McInstrParser.Jump)
            self.state = 287
            self.jumpname()
            self.state = 288
            _la = self._input.LA(1)
            if not(_la==30 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 289
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_jumpname

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class JumpPreviousContext(JumpnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.JumpnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Previous(self):
            return self.getToken(McInstrParser.Previous, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)
        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpPrevious" ):
                listener.enterJumpPrevious(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpPrevious" ):
                listener.exitJumpPrevious(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpPrevious" ):
                return visitor.visitJumpPrevious(self)
            else:
                return visitor.visitChildren(self)


    class JumpMyselfContext(JumpnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.JumpnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Myself(self):
            return self.getToken(McInstrParser.Myself, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpMyself" ):
                listener.enterJumpMyself(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpMyself" ):
                listener.exitJumpMyself(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpMyself" ):
                return visitor.visitJumpMyself(self)
            else:
                return visitor.visitChildren(self)


    class JumpIdentifierContext(JumpnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.JumpnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpIdentifier" ):
                listener.enterJumpIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpIdentifier" ):
                listener.exitJumpIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpIdentifier" ):
                return visitor.visitJumpIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class JumpNextContext(JumpnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.JumpnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Next(self):
            return self.getToken(McInstrParser.Next, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)
        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpNext" ):
                listener.enterJumpNext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpNext" ):
                listener.exitJumpNext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpNext" ):
                return visitor.visitJumpNext(self)
            else:
                return visitor.visitChildren(self)



    def jumpname(self):

        localctx = McInstrParser.JumpnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_jumpname)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = McInstrParser.JumpPreviousContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(McInstrParser.Previous)
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==132:
                    self.state = 292
                    self.match(McInstrParser.LeftParen)
                    self.state = 293
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 294
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [33]:
                localctx = McInstrParser.JumpMyselfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.match(McInstrParser.Myself)
                pass
            elif token in [31]:
                localctx = McInstrParser.JumpNextContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 298
                self.match(McInstrParser.Next)
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==132:
                    self.state = 299
                    self.match(McInstrParser.LeftParen)
                    self.state = 300
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 301
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [179]:
                localctx = McInstrParser.JumpIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 304
                self.match(McInstrParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)

        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_extend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtend" ):
                listener.enterExtend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtend" ):
                listener.exitExtend(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtend" ):
                return visitor.visitExtend(self)
            else:
                return visitor.visitChildren(self)




    def extend(self):

        localctx = McInstrParser.ExtendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_extend)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(McInstrParser.Extend)
            self.state = 308
            self.unparsed_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Component_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Previous(self):
            return self.getToken(McInstrParser.Previous, 0)

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)

        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_component_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComponent_ref" ):
                listener.enterComponent_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComponent_ref" ):
                listener.exitComponent_ref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComponent_ref" ):
                return visitor.visitComponent_ref(self)
            else:
                return visitor.visitChildren(self)




    def component_ref(self):

        localctx = McInstrParser.Component_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_component_ref)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(McInstrParser.Previous)
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==132:
                    self.state = 311
                    self.match(McInstrParser.LeftParen)
                    self.state = 312
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 313
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [179]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(McInstrParser.Identifier)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Comma)
            else:
                return self.getToken(McInstrParser.Comma, i)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_coords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoords" ):
                listener.enterCoords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoords" ):
                listener.exitCoords(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoords" ):
                return visitor.visitCoords(self)
            else:
                return visitor.visitChildren(self)




    def coords(self):

        localctx = McInstrParser.CoordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_coords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(McInstrParser.LeftParen)
            self.state = 320
            self.expr(0)
            self.state = 321
            self.match(McInstrParser.Comma)
            self.state = 322
            self.expr(0)
            self.state = 323
            self.match(McInstrParser.Comma)
            self.state = 324
            self.expr(0)
            self.state = 325
            self.match(McInstrParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Absolute(self):
            return self.getToken(McInstrParser.Absolute, 0)

        def Relative(self):
            return self.getToken(McInstrParser.Relative, 0)

        def component_ref(self):
            return self.getTypedRuleContext(McInstrParser.Component_refContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = McInstrParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_reference)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(McInstrParser.Absolute)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(McInstrParser.Relative)
                self.state = 331
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 329
                    self.match(McInstrParser.Absolute)
                    pass
                elif token in [22, 179]:
                    self.state = 330
                    self.component_ref()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DependencyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dependency(self):
            return self.getToken(McInstrParser.Dependency, 0)

        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_dependency

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDependency" ):
                listener.enterDependency(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDependency" ):
                listener.exitDependency(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDependency" ):
                return visitor.visitDependency(self)
            else:
                return visitor.visitChildren(self)




    def dependency(self):

        localctx = McInstrParser.DependencyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_dependency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(McInstrParser.Dependency)
            self.state = 336
            self.match(McInstrParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_declare

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclareBlockContext(DeclareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.DeclareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Declare(self):
            return self.getToken(McInstrParser.Declare, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareBlock" ):
                listener.enterDeclareBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareBlock" ):
                listener.exitDeclareBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareBlock" ):
                return visitor.visitDeclareBlock(self)
            else:
                return visitor.visitChildren(self)


    class DeclareBlockCopyContext(DeclareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.DeclareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Declare(self):
            return self.getToken(McInstrParser.Declare, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareBlockCopy" ):
                listener.enterDeclareBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareBlockCopy" ):
                listener.exitDeclareBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareBlockCopy" ):
                return visitor.visitDeclareBlockCopy(self)
            else:
                return visitor.visitChildren(self)



    def declare(self):

        localctx = McInstrParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.DeclareBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(McInstrParser.Declare)
                self.state = 339
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.DeclareBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(McInstrParser.Declare)
                self.state = 341
                self.match(McInstrParser.Copy)
                self.state = 342
                self.match(McInstrParser.Identifier)
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 343
                    self.match(McInstrParser.Extend)
                    self.state = 344
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UservarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UserVars(self):
            return self.getToken(McInstrParser.UserVars, 0)

        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_uservars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUservars" ):
                listener.enterUservars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUservars" ):
                listener.exitUservars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUservars" ):
                return visitor.visitUservars(self)
            else:
                return visitor.visitChildren(self)




    def uservars(self):

        localctx = McInstrParser.UservarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_uservars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(McInstrParser.UserVars)
            self.state = 350
            self.unparsed_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_initialize

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InitializeBlockContext(InitializeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.InitializeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Initialize(self):
            return self.getToken(McInstrParser.Initialize, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializeBlock" ):
                listener.enterInitializeBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializeBlock" ):
                listener.exitInitializeBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializeBlock" ):
                return visitor.visitInitializeBlock(self)
            else:
                return visitor.visitChildren(self)


    class InitializeBlockCopyContext(InitializeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.InitializeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Initialize(self):
            return self.getToken(McInstrParser.Initialize, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializeBlockCopy" ):
                listener.enterInitializeBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializeBlockCopy" ):
                listener.exitInitializeBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializeBlockCopy" ):
                return visitor.visitInitializeBlockCopy(self)
            else:
                return visitor.visitChildren(self)



    def initialize(self):

        localctx = McInstrParser.InitializeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_initialize)
        self._la = 0 # Token type
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InitializeBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(McInstrParser.Initialize)
                self.state = 353
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.InitializeBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(McInstrParser.Initialize)
                self.state = 355
                self.match(McInstrParser.Copy)
                self.state = 356
                self.match(McInstrParser.Identifier)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 357
                    self.match(McInstrParser.Extend)
                    self.state = 358
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_save

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SaveBlockCopyContext(SaveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.SaveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Save(self):
            return self.getToken(McInstrParser.Save, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveBlockCopy" ):
                listener.enterSaveBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveBlockCopy" ):
                listener.exitSaveBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveBlockCopy" ):
                return visitor.visitSaveBlockCopy(self)
            else:
                return visitor.visitChildren(self)


    class SaveBlockContext(SaveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.SaveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Save(self):
            return self.getToken(McInstrParser.Save, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveBlock" ):
                listener.enterSaveBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveBlock" ):
                listener.exitSaveBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveBlock" ):
                return visitor.visitSaveBlock(self)
            else:
                return visitor.visitChildren(self)



    def save(self):

        localctx = McInstrParser.SaveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_save)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SaveBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(McInstrParser.Save)
                self.state = 364
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.SaveBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(McInstrParser.Save)
                self.state = 366
                self.match(McInstrParser.Copy)
                self.state = 367
                self.match(McInstrParser.Identifier)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 368
                    self.match(McInstrParser.Extend)
                    self.state = 369
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Finally_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_finally_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FinallyBlockContext(Finally_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Finally_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def Finally(self):
            return self.getToken(McInstrParser.Finally, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyBlock" ):
                listener.enterFinallyBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyBlock" ):
                listener.exitFinallyBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyBlock" ):
                return visitor.visitFinallyBlock(self)
            else:
                return visitor.visitChildren(self)


    class FinallyBlockCopyContext(Finally_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Finally_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def Finally(self):
            return self.getToken(McInstrParser.Finally, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyBlockCopy" ):
                listener.enterFinallyBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyBlockCopy" ):
                listener.exitFinallyBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyBlockCopy" ):
                return visitor.visitFinallyBlockCopy(self)
            else:
                return visitor.visitChildren(self)



    def finally_(self):

        localctx = McInstrParser.Finally_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_finally_)
        self._la = 0 # Token type
        try:
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.FinallyBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(McInstrParser.Finally)
                self.state = 375
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.FinallyBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(McInstrParser.Finally)
                self.state = 377
                self.match(McInstrParser.Copy)
                self.state = 378
                self.match(McInstrParser.Identifier)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26:
                    self.state = 379
                    self.match(McInstrParser.Extend)
                    self.state = 380
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.mime = None # Token
            self.name = None # Token

        def MetaData(self):
            return self.getToken(McInstrParser.MetaData, 0)

        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Identifier)
            else:
                return self.getToken(McInstrParser.Identifier, i)

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.StringLiteral)
            else:
                return self.getToken(McInstrParser.StringLiteral, i)

        def getRuleIndex(self):
            return McInstrParser.RULE_metadata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata" ):
                listener.enterMetadata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata" ):
                listener.exitMetadata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadata" ):
                return visitor.visitMetadata(self)
            else:
                return visitor.visitChildren(self)




    def metadata(self):

        localctx = McInstrParser.MetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_metadata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(McInstrParser.MetaData)
            self.state = 386
            localctx.mime = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==52 or _la==179):
                localctx.mime = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 387
            localctx.name = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==52 or _la==179):
                localctx.name = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 388
            self.unparsed_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CategoryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Category(self):
            return self.getToken(McInstrParser.Category, 0)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_category

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCategory" ):
                listener.enterCategory(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCategory" ):
                listener.exitCategory(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCategory" ):
                return visitor.visitCategory(self)
            else:
                return visitor.visitChildren(self)




    def category(self):

        localctx = McInstrParser.CategoryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_category)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(McInstrParser.Category)
            self.state = 391
            _la = self._input.LA(1)
            if not(_la==52 or _la==179):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializerlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext
            self.values = list() # of ExprContexts

        def LeftBrace(self):
            return self.getToken(McInstrParser.LeftBrace, 0)

        def RightBrace(self):
            return self.getToken(McInstrParser.RightBrace, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Comma)
            else:
                return self.getToken(McInstrParser.Comma, i)

        def getRuleIndex(self):
            return McInstrParser.RULE_initializerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializerlist" ):
                listener.enterInitializerlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializerlist" ):
                listener.exitInitializerlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializerlist" ):
                return visitor.visitInitializerlist(self)
            else:
                return visitor.visitChildren(self)




    def initializerlist(self):

        localctx = McInstrParser.InitializerlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_initializerlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(McInstrParser.LeftBrace)
            self.state = 394
            localctx._expr = self.expr(0)
            localctx.values.append(localctx._expr)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==169:
                self.state = 395
                self.match(McInstrParser.Comma)
                self.state = 396
                localctx._expr = self.expr(0)
                localctx.values.append(localctx._expr)
                self.state = 401
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 402
            self.match(McInstrParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)

        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = McInstrParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(McInstrParser.Identifier)
            self.state = 405
            self.match(McInstrParser.Assign)
            self.state = 406
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionBinaryModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Mod(self):
            return self.getToken(McInstrParser.Mod, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryMod" ):
                listener.enterExpressionBinaryMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryMod" ):
                listener.exitExpressionBinaryMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryMod" ):
                return visitor.visitExpressionBinaryMod(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryLessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Less(self):
            return self.getToken(McInstrParser.Less, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryLess" ):
                listener.enterExpressionBinaryLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryLess" ):
                listener.exitExpressionBinaryLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryLess" ):
                return visitor.visitExpressionBinaryLess(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryGreaterContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Greater(self):
            return self.getToken(McInstrParser.Greater, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryGreater" ):
                listener.enterExpressionBinaryGreater(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryGreater" ):
                listener.exitExpressionBinaryGreater(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryGreater" ):
                return visitor.visitExpressionBinaryGreater(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryLessEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def LessEqual(self):
            return self.getToken(McInstrParser.LessEqual, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryLessEqual" ):
                listener.enterExpressionBinaryLessEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryLessEqual" ):
                listener.exitExpressionBinaryLessEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryLessEqual" ):
                return visitor.visitExpressionBinaryLessEqual(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionArrayAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def LeftBracket(self):
            return self.getToken(McInstrParser.LeftBracket, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)

        def RightBracket(self):
            return self.getToken(McInstrParser.RightBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionArrayAccess" ):
                listener.enterExpressionArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionArrayAccess" ):
                listener.exitExpressionArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionArrayAccess" ):
                return visitor.visitExpressionArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)

        def AndAnd(self):
            return self.getToken(McInstrParser.AndAnd, 0)
        def OrOr(self):
            return self.getToken(McInstrParser.OrOr, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryLogic" ):
                listener.enterExpressionBinaryLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryLogic" ):
                listener.exitExpressionBinaryLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryLogic" ):
                return visitor.visitExpressionBinaryLogic(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionIntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionInteger" ):
                listener.enterExpressionInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionInteger" ):
                listener.exitExpressionInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionInteger" ):
                return visitor.visitExpressionInteger(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryRightShiftContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryRightShift" ):
                listener.enterExpressionBinaryRightShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryRightShift" ):
                listener.exitExpressionBinaryRightShift(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryRightShift" ):
                return visitor.visitExpressionBinaryRightShift(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionMyselfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Myself(self):
            return self.getToken(McInstrParser.Myself, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionMyself" ):
                listener.enterExpressionMyself(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionMyself" ):
                listener.exitExpressionMyself(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionMyself" ):
                return visitor.visitExpressionMyself(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionPreviousContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Previous(self):
            return self.getToken(McInstrParser.Previous, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionPrevious" ):
                listener.enterExpressionPrevious(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionPrevious" ):
                listener.exitExpressionPrevious(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionPrevious" ):
                return visitor.visitExpressionPrevious(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionIdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionIdentifier" ):
                listener.enterExpressionIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionIdentifier" ):
                listener.exitExpressionIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionIdentifier" ):
                return visitor.visitExpressionIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStructAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Dot(self):
            return self.getToken(McInstrParser.Dot, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStructAccess" ):
                listener.enterExpressionStructAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStructAccess" ):
                listener.exitExpressionStructAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStructAccess" ):
                return visitor.visitExpressionStructAccess(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionFunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Comma)
            else:
                return self.getToken(McInstrParser.Comma, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionFunctionCall" ):
                listener.enterExpressionFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionFunctionCall" ):
                listener.exitExpressionFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionFunctionCall" ):
                return visitor.visitExpressionFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryMDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)

        def Star(self):
            return self.getToken(McInstrParser.Star, 0)
        def Div(self):
            return self.getToken(McInstrParser.Div, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryMD" ):
                listener.enterExpressionBinaryMD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryMD" ):
                listener.exitExpressionBinaryMD(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryMD" ):
                return visitor.visitExpressionBinaryMD(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionStringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self._StringLiteral = None # Token
            self.args = list() # of Tokens
            self.copyFrom(ctx)

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.StringLiteral)
            else:
                return self.getToken(McInstrParser.StringLiteral, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionString" ):
                listener.enterExpressionString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionString" ):
                listener.exitExpressionString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionString" ):
                return visitor.visitExpressionString(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionGroupingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionGrouping" ):
                listener.enterExpressionGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionGrouping" ):
                listener.exitExpressionGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionGrouping" ):
                return visitor.visitExpressionGrouping(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionExponentiationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.base = None # ExprContext
            self.exponent = None # ExprContext
            self.copyFrom(ctx)

        def Caret(self):
            return self.getToken(McInstrParser.Caret, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionExponentiation" ):
                listener.enterExpressionExponentiation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionExponentiation" ):
                listener.exitExpressionExponentiation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionExponentiation" ):
                return visitor.visitExpressionExponentiation(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryLeftShiftContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryLeftShift" ):
                listener.enterExpressionBinaryLeftShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryLeftShift" ):
                listener.exitExpressionBinaryLeftShift(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryLeftShift" ):
                return visitor.visitExpressionBinaryLeftShift(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryGreaterEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def GreaterEqual(self):
            return self.getToken(McInstrParser.GreaterEqual, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryGreaterEqual" ):
                listener.enterExpressionBinaryGreaterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryGreaterEqual" ):
                listener.exitExpressionBinaryGreaterEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryGreaterEqual" ):
                return visitor.visitExpressionBinaryGreaterEqual(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionZeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionZero" ):
                listener.enterExpressionZero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionZero" ):
                listener.exitExpressionZero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionZero" ):
                return visitor.visitExpressionZero(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionUnaryPMContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)

        def Plus(self):
            return self.getToken(McInstrParser.Plus, 0)
        def Minus(self):
            return self.getToken(McInstrParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionUnaryPM" ):
                listener.enterExpressionUnaryPM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionUnaryPM" ):
                listener.exitExpressionUnaryPM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionUnaryPM" ):
                return visitor.visitExpressionUnaryPM(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionTrinaryLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.test = None # ExprContext
            self.true = None # ExprContext
            self.false = None # ExprContext
            self.copyFrom(ctx)

        def Question(self):
            return self.getToken(McInstrParser.Question, 0)
        def Colon(self):
            return self.getToken(McInstrParser.Colon, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionTrinaryLogic" ):
                listener.enterExpressionTrinaryLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionTrinaryLogic" ):
                listener.exitExpressionTrinaryLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionTrinaryLogic" ):
                return visitor.visitExpressionTrinaryLogic(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionFloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FloatingLiteral(self):
            return self.getToken(McInstrParser.FloatingLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionFloat" ):
                listener.enterExpressionFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionFloat" ):
                listener.exitExpressionFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionFloat" ):
                return visitor.visitExpressionFloat(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionPointerAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Arrow(self):
            return self.getToken(McInstrParser.Arrow, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionPointerAccess" ):
                listener.enterExpressionPointerAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionPointerAccess" ):
                listener.exitExpressionPointerAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionPointerAccess" ):
                return visitor.visitExpressionPointerAccess(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Equal(self):
            return self.getToken(McInstrParser.Equal, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryEqual" ):
                listener.enterExpressionBinaryEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryEqual" ):
                listener.exitExpressionBinaryEqual(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryEqual" ):
                return visitor.visitExpressionBinaryEqual(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionBinaryPMContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)

        def Plus(self):
            return self.getToken(McInstrParser.Plus, 0)
        def Minus(self):
            return self.getToken(McInstrParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionBinaryPM" ):
                listener.enterExpressionBinaryPM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionBinaryPM" ):
                listener.exitExpressionBinaryPM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionBinaryPM" ):
                return visitor.visitExpressionBinaryPM(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionUnaryLogicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(McInstrParser.Not, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionUnaryLogic" ):
                listener.enterExpressionUnaryLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionUnaryLogic" ):
                listener.exitExpressionUnaryLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionUnaryLogic" ):
                return visitor.visitExpressionUnaryLogic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = McInstrParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.ExpressionZeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 409
                self.match(McInstrParser.T__0)
                pass

            elif la_ == 2:
                localctx = McInstrParser.ExpressionIntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 410
                self.match(McInstrParser.IntegerLiteral)
                pass

            elif la_ == 3:
                localctx = McInstrParser.ExpressionFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 411
                self.match(McInstrParser.FloatingLiteral)
                pass

            elif la_ == 4:
                localctx = McInstrParser.ExpressionStringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 415
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 412
                        localctx._StringLiteral = self.match(McInstrParser.StringLiteral)
                        localctx.args.append(localctx._StringLiteral) 
                    self.state = 417
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

                pass

            elif la_ == 5:
                localctx = McInstrParser.ExpressionPointerAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 418
                self.match(McInstrParser.Identifier)
                self.state = 419
                self.match(McInstrParser.Arrow)
                self.state = 420
                self.expr(23)
                pass

            elif la_ == 6:
                localctx = McInstrParser.ExpressionStructAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 421
                self.match(McInstrParser.Identifier)
                self.state = 422
                self.match(McInstrParser.Dot)
                self.state = 423
                self.expr(22)
                pass

            elif la_ == 7:
                localctx = McInstrParser.ExpressionArrayAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 424
                self.match(McInstrParser.Identifier)
                self.state = 425
                self.match(McInstrParser.LeftBracket)
                self.state = 426
                self.expr(0)
                self.state = 427
                self.match(McInstrParser.RightBracket)
                pass

            elif la_ == 8:
                localctx = McInstrParser.ExpressionFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 429
                self.match(McInstrParser.Identifier)
                self.state = 430
                self.match(McInstrParser.LeftParen)
                self.state = 431
                localctx._expr = self.expr(0)
                localctx.args.append(localctx._expr)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==169:
                    self.state = 432
                    self.match(McInstrParser.Comma)
                    self.state = 433
                    localctx._expr = self.expr(0)
                    localctx.args.append(localctx._expr)
                    self.state = 438
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 439
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 9:
                localctx = McInstrParser.ExpressionGroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 441
                self.match(McInstrParser.LeftParen)
                self.state = 442
                self.expr(0)
                self.state = 443
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 10:
                localctx = McInstrParser.ExpressionUnaryPMContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 445
                _la = self._input.LA(1)
                if not(_la==138 or _la==139):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 446
                self.expr(18)
                pass

            elif la_ == 11:
                localctx = McInstrParser.ExpressionIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 447
                self.match(McInstrParser.Identifier)
                pass

            elif la_ == 12:
                localctx = McInstrParser.ExpressionUnaryLogicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 448
                self.match(McInstrParser.Not)
                self.state = 449
                self.expr(5)
                pass

            elif la_ == 13:
                localctx = McInstrParser.ExpressionPreviousContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 450
                self.match(McInstrParser.Previous)
                pass

            elif la_ == 14:
                localctx = McInstrParser.ExpressionMyselfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 451
                self.match(McInstrParser.Myself)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 498
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 496
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                    if la_ == 1:
                        localctx = McInstrParser.ExpressionExponentiationContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 454
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 455
                        self.match(McInstrParser.Caret)
                        self.state = 456
                        localctx.exponent = self.expr(17)
                        pass

                    elif la_ == 2:
                        localctx = McInstrParser.ExpressionBinaryMDContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 457
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 458
                        _la = self._input.LA(1)
                        if not(_la==140 or _la==141):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 459
                        localctx.right = self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = McInstrParser.ExpressionBinaryPMContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 460
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 461
                        _la = self._input.LA(1)
                        if not(_la==138 or _la==139):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 462
                        localctx.right = self.expr(16)
                        pass

                    elif la_ == 4:
                        localctx = McInstrParser.ExpressionBinaryModContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 463
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 464
                        self.match(McInstrParser.Mod)
                        self.state = 465
                        localctx.right = self.expr(15)
                        pass

                    elif la_ == 5:
                        localctx = McInstrParser.ExpressionBinaryRightShiftContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 466
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 467
                        self.match(McInstrParser.T__1)
                        self.state = 468
                        localctx.right = self.expr(14)
                        pass

                    elif la_ == 6:
                        localctx = McInstrParser.ExpressionBinaryLeftShiftContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 469
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 470
                        self.match(McInstrParser.T__2)
                        self.state = 471
                        localctx.right = self.expr(13)
                        pass

                    elif la_ == 7:
                        localctx = McInstrParser.ExpressionBinaryEqualContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 472
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 473
                        self.match(McInstrParser.Equal)
                        self.state = 474
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 8:
                        localctx = McInstrParser.ExpressionBinaryLessEqualContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 475
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 476
                        self.match(McInstrParser.LessEqual)
                        self.state = 477
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 9:
                        localctx = McInstrParser.ExpressionBinaryGreaterEqualContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 478
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 479
                        self.match(McInstrParser.GreaterEqual)
                        self.state = 480
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 10:
                        localctx = McInstrParser.ExpressionBinaryLessContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 481
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 482
                        self.match(McInstrParser.Less)
                        self.state = 483
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 11:
                        localctx = McInstrParser.ExpressionBinaryGreaterContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 484
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 485
                        self.match(McInstrParser.Greater)
                        self.state = 486
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 12:
                        localctx = McInstrParser.ExpressionBinaryLogicContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 487
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 488
                        _la = self._input.LA(1)
                        if not(_la==165 or _la==166):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 489
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 13:
                        localctx = McInstrParser.ExpressionTrinaryLogicContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.test = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 490
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 491
                        self.match(McInstrParser.Question)
                        self.state = 492
                        localctx.true = self.expr(0)
                        self.state = 493
                        self.match(McInstrParser.Colon)
                        self.state = 494
                        localctx.false = self.expr(4)
                        pass

             
                self.state = 500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Shell(self):
            return self.getToken(McInstrParser.Shell, 0)

        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_shell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShell" ):
                listener.enterShell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShell" ):
                listener.exitShell(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShell" ):
                return visitor.visitShell(self)
            else:
                return visitor.visitChildren(self)




    def shell(self):

        localctx = McInstrParser.ShellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_shell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(McInstrParser.Shell)
            self.state = 502
            self.match(McInstrParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_search

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SearchPathContext(SearchContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.SearchContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Search(self):
            return self.getToken(McInstrParser.Search, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchPath" ):
                listener.enterSearchPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchPath" ):
                listener.exitSearchPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearchPath" ):
                return visitor.visitSearchPath(self)
            else:
                return visitor.visitChildren(self)


    class SearchShellContext(SearchContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.SearchContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Search(self):
            return self.getToken(McInstrParser.Search, 0)
        def Shell(self):
            return self.getToken(McInstrParser.Shell, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchShell" ):
                listener.enterSearchShell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchShell" ):
                listener.exitSearchShell(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearchShell" ):
                return visitor.visitSearchShell(self)
            else:
                return visitor.visitChildren(self)



    def search(self):

        localctx = McInstrParser.SearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_search)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SearchPathContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.match(McInstrParser.Search)
                self.state = 505
                self.match(McInstrParser.StringLiteral)
                pass

            elif la_ == 2:
                localctx = McInstrParser.SearchShellContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 506
                self.match(McInstrParser.Search)
                self.state = 507
                self.match(McInstrParser.Shell)
                self.state = 508
                self.match(McInstrParser.StringLiteral)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unparsed_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_unparsed_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnparsed_block" ):
                listener.enterUnparsed_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnparsed_block" ):
                listener.exitUnparsed_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnparsed_block" ):
                return visitor.visitUnparsed_block(self)
            else:
                return visitor.visitChildren(self)




    def unparsed_block(self):

        localctx = McInstrParser.Unparsed_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_unparsed_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(McInstrParser.UnparsedBlock)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 3)
         




