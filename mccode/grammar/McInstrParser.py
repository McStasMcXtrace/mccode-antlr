# Generated from /home/g/Code/mccode-antlr/mccode/grammar/McInstr.g4 by ANTLR 4.13.0
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
        4,1,189,460,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,3,1,83,8,1,1,1,3,1,86,8,1,1,1,3,1,89,8,1,1,1,3,1,92,8,1,1,
        1,3,1,95,8,1,1,1,3,1,98,8,1,1,1,1,1,3,1,102,8,1,1,1,3,1,105,8,1,
        1,1,1,1,1,2,1,2,1,2,1,2,5,2,113,8,2,10,2,12,2,116,9,2,3,2,118,8,
        2,1,2,1,2,1,3,3,3,123,8,3,1,3,1,3,1,3,3,3,128,8,3,1,3,1,3,3,3,132,
        8,3,1,3,1,3,1,3,1,3,3,3,138,8,3,1,3,1,3,3,3,142,8,3,1,3,1,3,1,3,
        3,3,147,8,3,1,3,1,3,1,3,3,3,152,8,3,1,3,1,3,3,3,156,8,3,3,3,158,
        8,3,1,4,1,4,1,4,1,4,4,4,164,8,4,11,4,12,4,165,3,4,168,8,4,1,5,1,
        5,1,5,1,6,3,6,174,8,6,1,6,3,6,177,8,6,1,6,3,6,180,8,6,1,6,1,6,1,
        6,1,6,1,6,3,6,187,8,6,1,6,1,6,3,6,191,8,6,1,6,3,6,194,8,6,1,6,3,
        6,197,8,6,1,6,3,6,200,8,6,1,6,3,6,203,8,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,212,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,222,8,8,1,
        9,1,9,1,9,1,9,5,9,228,8,9,10,9,12,9,231,9,9,3,9,233,8,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,11,1,11,3,11,243,8,11,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,4,16,264,8,16,11,16,12,16,265,1,17,1,17,1,17,1,17,3,17,
        272,8,17,1,17,1,17,1,17,1,17,1,17,3,17,279,8,17,1,17,3,17,282,8,
        17,1,18,1,18,1,18,1,18,3,18,288,8,18,1,18,3,18,291,8,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,3,20,305,8,20,
        3,20,307,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,319,8,22,3,22,321,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,
        23,330,8,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,
        25,342,8,25,3,25,344,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        353,8,26,3,26,355,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,364,
        8,27,3,27,366,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,375,8,
        28,3,28,377,8,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,
        31,1,31,1,31,5,31,391,8,31,10,31,12,31,394,9,31,1,31,1,31,1,32,1,
        32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,422,8,33,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,433,8,33,10,33,12,
        33,436,9,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,3,35,446,8,35,
        1,36,1,36,1,36,5,36,451,8,36,10,36,12,36,454,9,36,3,36,456,8,36,
        1,36,1,36,1,36,0,1,66,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        0,4,2,0,27,27,29,29,2,0,48,48,176,176,1,0,135,136,1,0,137,138,496,
        0,74,1,0,0,0,2,77,1,0,0,0,4,108,1,0,0,0,6,157,1,0,0,0,8,159,1,0,
        0,0,10,169,1,0,0,0,12,173,1,0,0,0,14,211,1,0,0,0,16,221,1,0,0,0,
        18,223,1,0,0,0,20,236,1,0,0,0,22,240,1,0,0,0,24,244,1,0,0,0,26,247,
        1,0,0,0,28,251,1,0,0,0,30,255,1,0,0,0,32,263,1,0,0,0,34,281,1,0,
        0,0,36,290,1,0,0,0,38,292,1,0,0,0,40,306,1,0,0,0,42,308,1,0,0,0,
        44,320,1,0,0,0,46,329,1,0,0,0,48,331,1,0,0,0,50,343,1,0,0,0,52,354,
        1,0,0,0,54,365,1,0,0,0,56,376,1,0,0,0,58,378,1,0,0,0,60,381,1,0,
        0,0,62,386,1,0,0,0,64,397,1,0,0,0,66,421,1,0,0,0,68,437,1,0,0,0,
        70,445,1,0,0,0,72,447,1,0,0,0,74,75,3,2,1,0,75,76,5,0,0,1,76,1,1,
        0,0,0,77,78,5,7,0,0,78,79,5,14,0,0,79,80,5,176,0,0,80,82,3,4,2,0,
        81,83,3,68,34,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,86,
        3,70,35,0,85,84,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,89,3,42,21,
        0,88,87,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,92,3,44,22,0,91,90,
        1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,95,3,48,24,0,94,93,1,0,0,
        0,94,95,1,0,0,0,95,97,1,0,0,0,96,98,3,50,25,0,97,96,1,0,0,0,97,98,
        1,0,0,0,98,99,1,0,0,0,99,101,3,8,4,0,100,102,3,52,26,0,101,100,1,
        0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,3,54,27,0,104,103,
        1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,10,0,0,107,3,1,
        0,0,0,108,117,5,129,0,0,109,114,3,6,3,0,110,111,5,166,0,0,111,113,
        3,6,3,0,112,110,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,
        1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,117,109,1,0,0,0,117,118,
        1,0,0,0,118,119,1,0,0,0,119,120,5,130,0,0,120,5,1,0,0,0,121,123,
        5,74,0,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,127,
        5,176,0,0,125,126,5,138,0,0,126,128,5,48,0,0,127,125,1,0,0,0,127,
        128,1,0,0,0,128,131,1,0,0,0,129,130,5,145,0,0,130,132,3,66,33,0,
        131,129,1,0,0,0,131,132,1,0,0,0,132,158,1,0,0,0,133,134,5,89,0,0,
        134,137,5,176,0,0,135,136,5,138,0,0,136,138,5,48,0,0,137,135,1,0,
        0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,140,5,145,0,0,140,142,3,
        66,33,0,141,139,1,0,0,0,141,142,1,0,0,0,142,158,1,0,0,0,143,147,
        5,40,0,0,144,145,5,62,0,0,145,147,5,137,0,0,146,143,1,0,0,0,146,
        144,1,0,0,0,147,148,1,0,0,0,148,151,5,176,0,0,149,150,5,138,0,0,
        150,152,5,48,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,155,1,0,0,0,
        153,154,5,145,0,0,154,156,5,48,0,0,155,153,1,0,0,0,155,156,1,0,0,
        0,156,158,1,0,0,0,157,122,1,0,0,0,157,133,1,0,0,0,157,146,1,0,0,
        0,158,7,1,0,0,0,159,167,5,21,0,0,160,164,3,12,6,0,161,164,3,70,35,
        0,162,164,3,10,5,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,0,
        0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,
        0,167,163,1,0,0,0,167,168,1,0,0,0,168,9,1,0,0,0,169,170,5,43,0,0,
        170,171,5,48,0,0,171,11,1,0,0,0,172,174,5,33,0,0,173,172,1,0,0,0,
        173,174,1,0,0,0,174,176,1,0,0,0,175,177,5,34,0,0,176,175,1,0,0,0,
        176,177,1,0,0,0,177,179,1,0,0,0,178,180,3,22,11,0,179,178,1,0,0,
        0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,5,5,0,0,182,183,3,14,7,
        0,183,184,5,145,0,0,184,186,3,16,8,0,185,187,3,24,12,0,186,185,1,
        0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,190,3,26,13,0,189,191,
        3,28,14,0,190,189,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,192,194,
        3,30,15,0,193,192,1,0,0,0,193,194,1,0,0,0,194,196,1,0,0,0,195,197,
        3,58,29,0,196,195,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,200,
        3,32,16,0,199,198,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,203,
        3,60,30,0,202,201,1,0,0,0,202,203,1,0,0,0,203,13,1,0,0,0,204,205,
        5,31,0,0,205,206,5,129,0,0,206,207,5,176,0,0,207,212,5,130,0,0,208,
        212,5,30,0,0,209,212,5,31,0,0,210,212,5,176,0,0,211,204,1,0,0,0,
        211,208,1,0,0,0,211,209,1,0,0,0,211,210,1,0,0,0,212,15,1,0,0,0,213,
        214,5,31,0,0,214,215,5,129,0,0,215,216,3,36,18,0,216,217,5,130,0,
        0,217,218,3,18,9,0,218,222,1,0,0,0,219,220,5,176,0,0,220,222,3,18,
        9,0,221,213,1,0,0,0,221,219,1,0,0,0,222,17,1,0,0,0,223,232,5,129,
        0,0,224,229,3,20,10,0,225,226,5,166,0,0,226,228,3,20,10,0,227,225,
        1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,233,
        1,0,0,0,231,229,1,0,0,0,232,224,1,0,0,0,232,233,1,0,0,0,233,234,
        1,0,0,0,234,235,5,130,0,0,235,19,1,0,0,0,236,237,5,176,0,0,237,238,
        5,145,0,0,238,239,3,66,33,0,239,21,1,0,0,0,240,242,5,32,0,0,241,
        243,3,66,33,0,242,241,1,0,0,0,242,243,1,0,0,0,243,23,1,0,0,0,244,
        245,5,27,0,0,245,246,3,66,33,0,246,25,1,0,0,0,247,248,5,4,0,0,248,
        249,3,38,19,0,249,250,3,40,20,0,250,27,1,0,0,0,251,252,5,18,0,0,
        252,253,3,38,19,0,253,254,3,40,20,0,254,29,1,0,0,0,255,256,5,24,
        0,0,256,257,5,176,0,0,257,31,1,0,0,0,258,259,5,26,0,0,259,260,3,
        34,17,0,260,261,7,0,0,0,261,262,3,66,33,0,262,264,1,0,0,0,263,258,
        1,0,0,0,264,265,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,33,1,
        0,0,0,267,271,5,19,0,0,268,269,5,129,0,0,269,270,5,45,0,0,270,272,
        5,130,0,0,271,268,1,0,0,0,271,272,1,0,0,0,272,282,1,0,0,0,273,282,
        5,30,0,0,274,278,5,28,0,0,275,276,5,129,0,0,276,277,5,45,0,0,277,
        279,5,130,0,0,278,275,1,0,0,0,278,279,1,0,0,0,279,282,1,0,0,0,280,
        282,5,176,0,0,281,267,1,0,0,0,281,273,1,0,0,0,281,274,1,0,0,0,281,
        280,1,0,0,0,282,35,1,0,0,0,283,287,5,19,0,0,284,285,5,129,0,0,285,
        286,5,45,0,0,286,288,5,130,0,0,287,284,1,0,0,0,287,288,1,0,0,0,288,
        291,1,0,0,0,289,291,5,176,0,0,290,283,1,0,0,0,290,289,1,0,0,0,291,
        37,1,0,0,0,292,293,5,129,0,0,293,294,3,66,33,0,294,295,5,166,0,0,
        295,296,3,66,33,0,296,297,5,166,0,0,297,298,3,66,33,0,298,299,5,
        130,0,0,299,39,1,0,0,0,300,307,5,3,0,0,301,304,5,17,0,0,302,305,
        5,3,0,0,303,305,3,36,18,0,304,302,1,0,0,0,304,303,1,0,0,0,305,307,
        1,0,0,0,306,300,1,0,0,0,306,301,1,0,0,0,307,41,1,0,0,0,308,309,5,
        36,0,0,309,310,5,48,0,0,310,43,1,0,0,0,311,312,5,8,0,0,312,321,3,
        72,36,0,313,314,5,8,0,0,314,315,5,31,0,0,315,318,5,176,0,0,316,317,
        5,23,0,0,317,319,3,72,36,0,318,316,1,0,0,0,318,319,1,0,0,0,319,321,
        1,0,0,0,320,311,1,0,0,0,320,313,1,0,0,0,321,45,1,0,0,0,322,323,5,
        22,0,0,323,330,3,72,36,0,324,325,5,22,0,0,325,326,5,31,0,0,326,327,
        5,176,0,0,327,328,5,23,0,0,328,330,3,72,36,0,329,322,1,0,0,0,329,
        324,1,0,0,0,330,47,1,0,0,0,331,332,5,6,0,0,332,333,3,72,36,0,333,
        49,1,0,0,0,334,335,5,13,0,0,335,344,3,72,36,0,336,337,5,13,0,0,337,
        338,5,31,0,0,338,341,5,176,0,0,339,340,5,23,0,0,340,342,3,72,36,
        0,341,339,1,0,0,0,341,342,1,0,0,0,342,344,1,0,0,0,343,334,1,0,0,
        0,343,336,1,0,0,0,344,51,1,0,0,0,345,346,5,25,0,0,346,355,3,72,36,
        0,347,348,5,25,0,0,348,349,5,31,0,0,349,352,5,176,0,0,350,351,5,
        23,0,0,351,353,3,72,36,0,352,350,1,0,0,0,352,353,1,0,0,0,353,355,
        1,0,0,0,354,345,1,0,0,0,354,347,1,0,0,0,355,53,1,0,0,0,356,357,5,
        12,0,0,357,366,3,72,36,0,358,359,5,12,0,0,359,360,5,31,0,0,360,363,
        5,176,0,0,361,362,5,23,0,0,362,364,3,72,36,0,363,361,1,0,0,0,363,
        364,1,0,0,0,364,366,1,0,0,0,365,356,1,0,0,0,365,358,1,0,0,0,366,
        55,1,0,0,0,367,368,5,11,0,0,368,377,3,72,36,0,369,370,5,11,0,0,370,
        371,5,31,0,0,371,374,5,176,0,0,372,373,5,23,0,0,373,375,3,72,36,
        0,374,372,1,0,0,0,374,375,1,0,0,0,375,377,1,0,0,0,376,367,1,0,0,
        0,376,369,1,0,0,0,377,57,1,0,0,0,378,379,5,23,0,0,379,380,3,72,36,
        0,380,59,1,0,0,0,381,382,5,39,0,0,382,383,7,1,0,0,383,384,7,1,0,
        0,384,385,3,72,36,0,385,61,1,0,0,0,386,387,5,133,0,0,387,392,3,66,
        33,0,388,389,5,166,0,0,389,391,3,66,33,0,390,388,1,0,0,0,391,394,
        1,0,0,0,392,390,1,0,0,0,392,393,1,0,0,0,393,395,1,0,0,0,394,392,
        1,0,0,0,395,396,5,134,0,0,396,63,1,0,0,0,397,398,5,176,0,0,398,399,
        5,145,0,0,399,400,3,66,33,0,400,65,1,0,0,0,401,402,6,33,-1,0,402,
        403,5,176,0,0,403,404,5,131,0,0,404,405,3,66,33,0,405,406,5,132,
        0,0,406,422,1,0,0,0,407,408,5,176,0,0,408,409,5,129,0,0,409,410,
        3,66,33,0,410,411,5,130,0,0,411,422,1,0,0,0,412,413,5,129,0,0,413,
        414,3,66,33,0,414,415,5,130,0,0,415,422,1,0,0,0,416,417,7,2,0,0,
        417,422,3,66,33,7,418,422,5,176,0,0,419,422,5,47,0,0,420,422,5,45,
        0,0,421,401,1,0,0,0,421,407,1,0,0,0,421,412,1,0,0,0,421,416,1,0,
        0,0,421,418,1,0,0,0,421,419,1,0,0,0,421,420,1,0,0,0,422,434,1,0,
        0,0,423,424,10,6,0,0,424,425,5,140,0,0,425,433,3,66,33,6,426,427,
        10,5,0,0,427,428,7,3,0,0,428,433,3,66,33,6,429,430,10,4,0,0,430,
        431,7,2,0,0,431,433,3,66,33,5,432,423,1,0,0,0,432,426,1,0,0,0,432,
        429,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,434,435,1,0,0,0,435,
        67,1,0,0,0,436,434,1,0,0,0,437,438,5,37,0,0,438,439,5,48,0,0,439,
        69,1,0,0,0,440,441,5,38,0,0,441,446,5,48,0,0,442,443,5,38,0,0,443,
        444,5,37,0,0,444,446,5,48,0,0,445,440,1,0,0,0,445,442,1,0,0,0,446,
        71,1,0,0,0,447,455,5,1,0,0,448,456,1,0,0,0,449,451,9,0,0,0,450,449,
        1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,453,1,0,0,0,453,456,
        1,0,0,0,454,452,1,0,0,0,455,448,1,0,0,0,455,452,1,0,0,0,456,457,
        1,0,0,0,457,458,5,2,0,0,458,73,1,0,0,0,62,82,85,88,91,94,97,101,
        104,114,117,122,127,131,137,141,146,151,155,157,163,165,167,173,
        176,179,186,190,193,196,199,202,211,221,229,232,242,265,271,278,
        281,287,290,304,306,318,320,329,341,343,352,354,363,365,374,376,
        392,421,432,434,445,452,455
    ]

class McInstrParser ( Parser ):

    grammarFileName = "McInstr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'%{'", "'%}'", "'ABSOLUTE'", "'AT'", 
                     "'COMPONENT'", "'USERVARS'", "'DEFINE'", "'DECLARE'", 
                     "'DEFINITION'", "'END'", "<INVALID>", "'FINALLY'", 
                     "<INVALID>", "'INSTRUMENT'", "<INVALID>", "'PARAMETERS'", 
                     "'RELATIVE'", "'ROTATED'", "'PREVIOUS'", "'SETTING'", 
                     "'TRACE'", "'SHARE'", "'EXTEND'", "'GROUP'", "'SAVE'", 
                     "'JUMP'", "'WHEN'", "'NEXT'", "'ITERATE'", "'MYSELF'", 
                     "'COPY'", "'SPLIT'", "'REMOVABLE'", "'CPU'", "'NOACC'", 
                     "'DEPENDENCY'", "'SHELL'", "'SEARCH'", "'METADATA'", 
                     "'string'", "'vector'", "'symbol'", "'%include'", "'NULL'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'alignas'", "'alignof'", "'asm'", "'auto'", 
                     "'bool'", "'break'", "'case'", "'catch'", "'char'", 
                     "'char16_t'", "'char32_t'", "'class'", "'const'", "'constexpr'", 
                     "'const_cast'", "'continue'", "'decltype'", "'default'", 
                     "'delete'", "'do'", "'double'", "'dynamic_cast'", "'else'", 
                     "'enum'", "'explicit'", "'export'", "'extern'", "'false'", 
                     "'final'", "'float'", "'for'", "'friend'", "'goto'", 
                     "'if'", "'inline'", "'int'", "'long'", "'mutable'", 
                     "'namespace'", "'new'", "'noexcept'", "'nullptr'", 
                     "'operator'", "'override'", "'private'", "'protected'", 
                     "'public'", "'register'", "'reinterpret_cast'", "'return'", 
                     "'short'", "'signed'", "'sizeof'", "'static'", "'static_assert'", 
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

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Absolute", 
                      "At", "Component", "UserVars", "Define", "Declare", 
                      "Definition", "End", "McDisplay", "Finally", "Initialize", 
                      "Instrument", "Output", "Parameters", "Relative", 
                      "Rotated", "Previous", "Setting", "Trace", "Share", 
                      "Extend", "Group", "Save", "Jump", "When", "Next", 
                      "Iterate", "Myself", "Copy", "Split", "Removable", 
                      "Cpu", "NoAcc", "Dependency", "Shell", "Search", "MetaData", 
                      "String", "Vector", "Symbol", "Include", "Null", "IntegerLiteral", 
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
                      "Override", "Private", "Protected", "Public", "Register", 
                      "Reinterpret_cast", "Return", "Short", "Signed", "Sizeof", 
                      "Static", "Static_assert", "Static_cast", "Struct", 
                      "Switch", "Template", "This", "Thread_local", "Throw", 
                      "True_", "Try", "Typedef", "Typeid_", "Typename_", 
                      "Union", "Unsigned", "Using", "Virtual", "Void", "Volatile", 
                      "Wchar", "While", "LeftParen", "RightParen", "LeftBracket", 
                      "RightBracket", "LeftBrace", "RightBrace", "Plus", 
                      "Minus", "Star", "Div", "Mod", "Caret", "And", "Or", 
                      "Tilde", "Not", "Assign", "Less", "Greater", "PlusAssign", 
                      "MinusAssign", "StarAssign", "DivAssign", "ModAssign", 
                      "XorAssign", "AndAssign", "OrAssign", "LeftShiftAssign", 
                      "RightShiftAssign", "Equal", "NotEqual", "LessEqual", 
                      "GreaterEqual", "AndAnd", "OrOr", "PlusPlus", "MinusMinus", 
                      "Comma", "ArrowStar", "Arrow", "Question", "Colon", 
                      "Doublecolon", "Semi", "Dot", "DotStar", "Ellipsis", 
                      "Identifier", "DecimalLiteral", "OctalLiteral", "HexadecimalLiteral", 
                      "BinaryLiteral", "IntegerSuffix", "UserDefinedIntegerLiteral", 
                      "UserDefinedFloatingLiteral", "UserDefinedStringLiteral", 
                      "UserDefinedCharacterLiteral", "Whitespace", "Newline", 
                      "BlockComment", "LineComment" ]

    RULE_prog = 0
    RULE_instrument_definition = 1
    RULE_instrument_parameters = 2
    RULE_instrument_parameter = 3
    RULE_instrument_trace = 4
    RULE_instrument_trace_include = 5
    RULE_component_instance = 6
    RULE_instance_name = 7
    RULE_component_type = 8
    RULE_instance_parameters = 9
    RULE_instance_parameter = 10
    RULE_split = 11
    RULE_when = 12
    RULE_place = 13
    RULE_orientation = 14
    RULE_groupref = 15
    RULE_jump = 16
    RULE_jumpname = 17
    RULE_component_ref = 18
    RULE_coords = 19
    RULE_reference = 20
    RULE_dependency = 21
    RULE_declare = 22
    RULE_share = 23
    RULE_uservars = 24
    RULE_initialize = 25
    RULE_save = 26
    RULE_finally_ = 27
    RULE_display = 28
    RULE_extend = 29
    RULE_metadata = 30
    RULE_initializerlist = 31
    RULE_assignment = 32
    RULE_expr = 33
    RULE_shell = 34
    RULE_search = 35
    RULE_unparsed_block = 36

    ruleNames =  [ "prog", "instrument_definition", "instrument_parameters", 
                   "instrument_parameter", "instrument_trace", "instrument_trace_include", 
                   "component_instance", "instance_name", "component_type", 
                   "instance_parameters", "instance_parameter", "split", 
                   "when", "place", "orientation", "groupref", "jump", "jumpname", 
                   "component_ref", "coords", "reference", "dependency", 
                   "declare", "share", "uservars", "initialize", "save", 
                   "finally_", "display", "extend", "metadata", "initializerlist", 
                   "assignment", "expr", "shell", "search", "unparsed_block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Absolute=3
    At=4
    Component=5
    UserVars=6
    Define=7
    Declare=8
    Definition=9
    End=10
    McDisplay=11
    Finally=12
    Initialize=13
    Instrument=14
    Output=15
    Parameters=16
    Relative=17
    Rotated=18
    Previous=19
    Setting=20
    Trace=21
    Share=22
    Extend=23
    Group=24
    Save=25
    Jump=26
    When=27
    Next=28
    Iterate=29
    Myself=30
    Copy=31
    Split=32
    Removable=33
    Cpu=34
    NoAcc=35
    Dependency=36
    Shell=37
    Search=38
    MetaData=39
    String=40
    Vector=41
    Symbol=42
    Include=43
    Null=44
    IntegerLiteral=45
    CharacterLiteral=46
    FloatingLiteral=47
    StringLiteral=48
    BooleanLitteral=49
    PointerLiteral=50
    UserDefinedLiteral=51
    MultiLineMacro=52
    Directive=53
    Alignas=54
    Alignof=55
    Asm=56
    Auto=57
    Bool=58
    Break=59
    Case=60
    Catch=61
    Char=62
    Char16=63
    Char32=64
    Class=65
    Const=66
    Constexpr=67
    Const_cast=68
    Continue=69
    Decltype=70
    Default=71
    Delete=72
    Do=73
    Double=74
    Dynamic_cast=75
    Else=76
    Enum=77
    Explicit=78
    Export=79
    Extern=80
    False_=81
    Final=82
    Float=83
    For=84
    Friend=85
    Goto=86
    If=87
    Inline=88
    Int=89
    Long=90
    Mutable=91
    Namespace=92
    New=93
    Noexcept=94
    Nullptr=95
    Operator=96
    Override=97
    Private=98
    Protected=99
    Public=100
    Register=101
    Reinterpret_cast=102
    Return=103
    Short=104
    Signed=105
    Sizeof=106
    Static=107
    Static_assert=108
    Static_cast=109
    Struct=110
    Switch=111
    Template=112
    This=113
    Thread_local=114
    Throw=115
    True_=116
    Try=117
    Typedef=118
    Typeid_=119
    Typename_=120
    Union=121
    Unsigned=122
    Using=123
    Virtual=124
    Void=125
    Volatile=126
    Wchar=127
    While=128
    LeftParen=129
    RightParen=130
    LeftBracket=131
    RightBracket=132
    LeftBrace=133
    RightBrace=134
    Plus=135
    Minus=136
    Star=137
    Div=138
    Mod=139
    Caret=140
    And=141
    Or=142
    Tilde=143
    Not=144
    Assign=145
    Less=146
    Greater=147
    PlusAssign=148
    MinusAssign=149
    StarAssign=150
    DivAssign=151
    ModAssign=152
    XorAssign=153
    AndAssign=154
    OrAssign=155
    LeftShiftAssign=156
    RightShiftAssign=157
    Equal=158
    NotEqual=159
    LessEqual=160
    GreaterEqual=161
    AndAnd=162
    OrOr=163
    PlusPlus=164
    MinusMinus=165
    Comma=166
    ArrowStar=167
    Arrow=168
    Question=169
    Colon=170
    Doublecolon=171
    Semi=172
    Dot=173
    DotStar=174
    Ellipsis=175
    Identifier=176
    DecimalLiteral=177
    OctalLiteral=178
    HexadecimalLiteral=179
    BinaryLiteral=180
    IntegerSuffix=181
    UserDefinedIntegerLiteral=182
    UserDefinedFloatingLiteral=183
    UserDefinedStringLiteral=184
    UserDefinedCharacterLiteral=185
    Whitespace=186
    Newline=187
    BlockComment=188
    LineComment=189

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
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
            self.state = 74
            self.instrument_definition()
            self.state = 75
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
            self.state = 77
            self.match(McInstrParser.Define)
            self.state = 78
            self.match(McInstrParser.Instrument)
            self.state = 79
            self.match(McInstrParser.Identifier)
            self.state = 80
            self.instrument_parameters()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 81
                self.shell()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 84
                self.search()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 87
                self.dependency()


            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 90
                self.declare()


            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 93
                self.uservars()


            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 96
                self.initialize()


            self.state = 99
            self.instrument_trace()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 100
                self.save()


            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 103
                self.finally_()


            self.state = 106
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
            self.state = 108
            self.match(McInstrParser.LeftParen)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 40)) & ~0x3f) == 0 and ((1 << (_la - 40)) & 562967137484801) != 0) or _la==176:
                self.state = 109
                self.instrument_parameter()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==166:
                    self.state = 110
                    self.match(McInstrParser.Comma)
                    self.state = 111
                    self.instrument_parameter()
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 119
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
        def Div(self):
            return self.getToken(McInstrParser.Div, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)
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
        def Div(self):
            return self.getToken(McInstrParser.Div, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)
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
        def Div(self):
            return self.getToken(McInstrParser.Div, 0)
        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.StringLiteral)
            else:
                return self.getToken(McInstrParser.StringLiteral, i)
        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)
        def Char(self):
            return self.getToken(McInstrParser.Char, 0)
        def Star(self):
            return self.getToken(McInstrParser.Star, 0)

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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [74, 176]:
                localctx = McInstrParser.InstrumentParameterDoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==74:
                    self.state = 121
                    self.match(McInstrParser.Double)


                self.state = 124
                self.match(McInstrParser.Identifier)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==138:
                    self.state = 125
                    self.match(McInstrParser.Div)
                    self.state = 126
                    self.match(McInstrParser.StringLiteral)


                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==145:
                    self.state = 129
                    self.match(McInstrParser.Assign)
                    self.state = 130
                    self.expr(0)


                pass
            elif token in [89]:
                localctx = McInstrParser.InstrumentParameterIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(McInstrParser.Int)
                self.state = 134
                self.match(McInstrParser.Identifier)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==138:
                    self.state = 135
                    self.match(McInstrParser.Div)
                    self.state = 136
                    self.match(McInstrParser.StringLiteral)


                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==145:
                    self.state = 139
                    self.match(McInstrParser.Assign)
                    self.state = 140
                    self.expr(0)


                pass
            elif token in [40, 62]:
                localctx = McInstrParser.InstrumentParameterStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [40]:
                    self.state = 143
                    self.match(McInstrParser.String)
                    pass
                elif token in [62]:
                    self.state = 144
                    self.match(McInstrParser.Char)
                    self.state = 145
                    self.match(McInstrParser.Star)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 148
                self.match(McInstrParser.Identifier)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==138:
                    self.state = 149
                    self.match(McInstrParser.Div)
                    self.state = 150
                    self.match(McInstrParser.StringLiteral)


                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==145:
                    self.state = 153
                    self.match(McInstrParser.Assign)
                    self.state = 154
                    self.match(McInstrParser.StringLiteral)


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
        self.enterRule(localctx, 8, self.RULE_instrument_trace)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(McInstrParser.Trace)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 9101035700256) != 0):
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 163
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [5, 32, 33, 34]:
                        self.state = 160
                        self.component_instance()
                        pass
                    elif token in [38]:
                        self.state = 161
                        self.search()
                        pass
                    elif token in [43]:
                        self.state = 162
                        self.instrument_trace_include()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 165 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 9101035700256) != 0)):
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
        self.enterRule(localctx, 10, self.RULE_instrument_trace_include)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(McInstrParser.Include)
            self.state = 170
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


        def when(self):
            return self.getTypedRuleContext(McInstrParser.WhenContext,0)


        def orientation(self):
            return self.getTypedRuleContext(McInstrParser.OrientationContext,0)


        def groupref(self):
            return self.getTypedRuleContext(McInstrParser.GrouprefContext,0)


        def extend(self):
            return self.getTypedRuleContext(McInstrParser.ExtendContext,0)


        def jump(self):
            return self.getTypedRuleContext(McInstrParser.JumpContext,0)


        def metadata(self):
            return self.getTypedRuleContext(McInstrParser.MetadataContext,0)


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
        self.enterRule(localctx, 12, self.RULE_component_instance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 172
                self.match(McInstrParser.Removable)


            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 175
                self.match(McInstrParser.Cpu)


            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 178
                self.split()


            self.state = 181
            self.match(McInstrParser.Component)
            self.state = 182
            self.instance_name()
            self.state = 183
            self.match(McInstrParser.Assign)
            self.state = 184
            self.component_type()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 185
                self.when()


            self.state = 188
            self.place()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 189
                self.orientation()


            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 192
                self.groupref()


            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 195
                self.extend()


            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 198
                self.jump()


            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 201
                self.metadata()


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


    class InstanceNameMyselfContext(Instance_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Instance_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Myself(self):
            return self.getToken(McInstrParser.Myself, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceNameMyself" ):
                listener.enterInstanceNameMyself(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceNameMyself" ):
                listener.exitInstanceNameMyself(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceNameMyself" ):
                return visitor.visitInstanceNameMyself(self)
            else:
                return visitor.visitChildren(self)



    def instance_name(self):

        localctx = McInstrParser.Instance_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instance_name)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InstanceNameCopyIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(McInstrParser.Copy)
                self.state = 205
                self.match(McInstrParser.LeftParen)
                self.state = 206
                self.match(McInstrParser.Identifier)
                self.state = 207
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 2:
                localctx = McInstrParser.InstanceNameMyselfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(McInstrParser.Myself)
                pass

            elif la_ == 3:
                localctx = McInstrParser.InstanceNameCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(McInstrParser.Copy)
                pass

            elif la_ == 4:
                localctx = McInstrParser.InstanceNameIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 210
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
        def instance_parameters(self):
            return self.getTypedRuleContext(McInstrParser.Instance_parametersContext,0)


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
        def instance_parameters(self):
            return self.getTypedRuleContext(McInstrParser.Instance_parametersContext,0)


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
        self.enterRule(localctx, 16, self.RULE_component_type)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = McInstrParser.ComponentTypeCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(McInstrParser.Copy)
                self.state = 214
                self.match(McInstrParser.LeftParen)
                self.state = 215
                self.component_ref()
                self.state = 216
                self.match(McInstrParser.RightParen)
                self.state = 217
                self.instance_parameters()
                pass
            elif token in [176]:
                localctx = McInstrParser.ComponentTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(McInstrParser.Identifier)
                self.state = 220
                self.instance_parameters()
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
        self.enterRule(localctx, 18, self.RULE_instance_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(McInstrParser.LeftParen)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==176:
                self.state = 224
                self.instance_parameter()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==166:
                    self.state = 225
                    self.match(McInstrParser.Comma)
                    self.state = 226
                    self.instance_parameter()
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 234
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

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def Assign(self):
            return self.getToken(McInstrParser.Assign, 0)

        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)


        def getRuleIndex(self):
            return McInstrParser.RULE_instance_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_parameter" ):
                listener.enterInstance_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_parameter" ):
                listener.exitInstance_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_parameter" ):
                return visitor.visitInstance_parameter(self)
            else:
                return visitor.visitChildren(self)




    def instance_parameter(self):

        localctx = McInstrParser.Instance_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instance_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(McInstrParser.Identifier)
            self.state = 237
            self.match(McInstrParser.Assign)
            self.state = 238
            self.expr(0)
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
        self.enterRule(localctx, 22, self.RULE_split)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(McInstrParser.Split)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45 or _la==47 or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & 140737488355521) != 0):
                self.state = 241
                self.expr(0)


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
        self.enterRule(localctx, 24, self.RULE_when)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(McInstrParser.When)
            self.state = 245
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
        self.enterRule(localctx, 26, self.RULE_place)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(McInstrParser.At)
            self.state = 248
            self.coords()
            self.state = 249
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
        self.enterRule(localctx, 28, self.RULE_orientation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(McInstrParser.Rotated)
            self.state = 252
            self.coords()
            self.state = 253
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
        self.enterRule(localctx, 30, self.RULE_groupref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(McInstrParser.Group)
            self.state = 256
            self.match(McInstrParser.Identifier)
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

        def Jump(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Jump)
            else:
                return self.getToken(McInstrParser.Jump, i)

        def jumpname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.JumpnameContext)
            else:
                return self.getTypedRuleContext(McInstrParser.JumpnameContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.ExprContext)
            else:
                return self.getTypedRuleContext(McInstrParser.ExprContext,i)


        def When(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.When)
            else:
                return self.getToken(McInstrParser.When, i)

        def Iterate(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Iterate)
            else:
                return self.getToken(McInstrParser.Iterate, i)

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
        self.enterRule(localctx, 32, self.RULE_jump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 258
                self.match(McInstrParser.Jump)
                self.state = 259
                self.jumpname()
                self.state = 260
                _la = self._input.LA(1)
                if not(_la==27 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 261
                self.expr(0)
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==26):
                    break

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

        def Previous(self):
            return self.getToken(McInstrParser.Previous, 0)

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)

        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def Myself(self):
            return self.getToken(McInstrParser.Myself, 0)

        def Next(self):
            return self.getToken(McInstrParser.Next, 0)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def getRuleIndex(self):
            return McInstrParser.RULE_jumpname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpname" ):
                listener.enterJumpname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpname" ):
                listener.exitJumpname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpname" ):
                return visitor.visitJumpname(self)
            else:
                return visitor.visitChildren(self)




    def jumpname(self):

        localctx = McInstrParser.JumpnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_jumpname)
        self._la = 0 # Token type
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(McInstrParser.Previous)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==129:
                    self.state = 268
                    self.match(McInstrParser.LeftParen)
                    self.state = 269
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 270
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(McInstrParser.Myself)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.match(McInstrParser.Next)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==129:
                    self.state = 275
                    self.match(McInstrParser.LeftParen)
                    self.state = 276
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 277
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [176]:
                self.enterOuterAlt(localctx, 4)
                self.state = 280
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
        self.enterRule(localctx, 36, self.RULE_component_ref)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(McInstrParser.Previous)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==129:
                    self.state = 284
                    self.match(McInstrParser.LeftParen)
                    self.state = 285
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 286
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [176]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
        self.enterRule(localctx, 38, self.RULE_coords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(McInstrParser.LeftParen)
            self.state = 293
            self.expr(0)
            self.state = 294
            self.match(McInstrParser.Comma)
            self.state = 295
            self.expr(0)
            self.state = 296
            self.match(McInstrParser.Comma)
            self.state = 297
            self.expr(0)
            self.state = 298
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
        self.enterRule(localctx, 40, self.RULE_reference)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(McInstrParser.Absolute)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(McInstrParser.Relative)
                self.state = 304
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 302
                    self.match(McInstrParser.Absolute)
                    pass
                elif token in [19, 176]:
                    self.state = 303
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
        self.enterRule(localctx, 42, self.RULE_dependency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(McInstrParser.Dependency)
            self.state = 309
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
        self.enterRule(localctx, 44, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.DeclareBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.match(McInstrParser.Declare)
                self.state = 312
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.DeclareBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(McInstrParser.Declare)
                self.state = 314
                self.match(McInstrParser.Copy)
                self.state = 315
                self.match(McInstrParser.Identifier)
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 316
                    self.match(McInstrParser.Extend)
                    self.state = 317
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_share

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ShareBlockContext(ShareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ShareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Share(self):
            return self.getToken(McInstrParser.Share, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShareBlock" ):
                listener.enterShareBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShareBlock" ):
                listener.exitShareBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShareBlock" ):
                return visitor.visitShareBlock(self)
            else:
                return visitor.visitChildren(self)


    class ShareBlockCopyContext(ShareContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ShareContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Share(self):
            return self.getToken(McInstrParser.Share, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShareBlockCopy" ):
                listener.enterShareBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShareBlockCopy" ):
                listener.exitShareBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShareBlockCopy" ):
                return visitor.visitShareBlockCopy(self)
            else:
                return visitor.visitChildren(self)



    def share(self):

        localctx = McInstrParser.ShareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_share)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.ShareBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(McInstrParser.Share)
                self.state = 323
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.ShareBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(McInstrParser.Share)
                self.state = 325
                self.match(McInstrParser.Copy)
                self.state = 326
                self.match(McInstrParser.Identifier)

                self.state = 327
                self.match(McInstrParser.Extend)
                self.state = 328
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
        self.enterRule(localctx, 48, self.RULE_uservars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(McInstrParser.UserVars)
            self.state = 332
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
        self.enterRule(localctx, 50, self.RULE_initialize)
        self._la = 0 # Token type
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InitializeBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(McInstrParser.Initialize)
                self.state = 335
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.InitializeBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.match(McInstrParser.Initialize)
                self.state = 337
                self.match(McInstrParser.Copy)
                self.state = 338
                self.match(McInstrParser.Identifier)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 339
                    self.match(McInstrParser.Extend)
                    self.state = 340
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
        self.enterRule(localctx, 52, self.RULE_save)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SaveBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(McInstrParser.Save)
                self.state = 346
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.SaveBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(McInstrParser.Save)
                self.state = 348
                self.match(McInstrParser.Copy)
                self.state = 349
                self.match(McInstrParser.Identifier)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 350
                    self.match(McInstrParser.Extend)
                    self.state = 351
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
        self.enterRule(localctx, 54, self.RULE_finally_)
        self._la = 0 # Token type
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.FinallyBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(McInstrParser.Finally)
                self.state = 357
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.FinallyBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(McInstrParser.Finally)
                self.state = 359
                self.match(McInstrParser.Copy)
                self.state = 360
                self.match(McInstrParser.Identifier)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 361
                    self.match(McInstrParser.Extend)
                    self.state = 362
                    self.unparsed_block()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisplayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_display

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DisplayBlockCopyContext(DisplayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.DisplayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def McDisplay(self):
            return self.getToken(McInstrParser.McDisplay, 0)
        def Copy(self):
            return self.getToken(McInstrParser.Copy, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def Extend(self):
            return self.getToken(McInstrParser.Extend, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayBlockCopy" ):
                listener.enterDisplayBlockCopy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayBlockCopy" ):
                listener.exitDisplayBlockCopy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayBlockCopy" ):
                return visitor.visitDisplayBlockCopy(self)
            else:
                return visitor.visitChildren(self)


    class DisplayBlockContext(DisplayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.DisplayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def McDisplay(self):
            return self.getToken(McInstrParser.McDisplay, 0)
        def unparsed_block(self):
            return self.getTypedRuleContext(McInstrParser.Unparsed_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisplayBlock" ):
                listener.enterDisplayBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisplayBlock" ):
                listener.exitDisplayBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisplayBlock" ):
                return visitor.visitDisplayBlock(self)
            else:
                return visitor.visitChildren(self)



    def display(self):

        localctx = McInstrParser.DisplayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_display)
        self._la = 0 # Token type
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.DisplayBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(McInstrParser.McDisplay)
                self.state = 368
                self.unparsed_block()
                pass

            elif la_ == 2:
                localctx = McInstrParser.DisplayBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(McInstrParser.McDisplay)
                self.state = 370
                self.match(McInstrParser.Copy)
                self.state = 371
                self.match(McInstrParser.Identifier)
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 372
                    self.match(McInstrParser.Extend)
                    self.state = 373
                    self.unparsed_block()


                pass


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
        self.enterRule(localctx, 58, self.RULE_extend)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(McInstrParser.Extend)
            self.state = 379
            self.unparsed_block()
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
        self.enterRule(localctx, 60, self.RULE_metadata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(McInstrParser.MetaData)
            self.state = 382
            localctx.mime = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==48 or _la==176):
                localctx.mime = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 383
            localctx.name = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==48 or _la==176):
                localctx.name = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 384
            self.unparsed_block()
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
        self.enterRule(localctx, 62, self.RULE_initializerlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(McInstrParser.LeftBrace)
            self.state = 387
            localctx._expr = self.expr(0)
            localctx.values.append(localctx._expr)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==166:
                self.state = 388
                self.match(McInstrParser.Comma)
                self.state = 389
                localctx._expr = self.expr(0)
                localctx.values.append(localctx._expr)
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
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
        self.enterRule(localctx, 64, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(McInstrParser.Identifier)
            self.state = 398
            self.match(McInstrParser.Assign)
            self.state = 399
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


    class ExpressionFunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def expr(self):
            return self.getTypedRuleContext(McInstrParser.ExprContext,0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = McInstrParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.ExpressionArrayAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 402
                self.match(McInstrParser.Identifier)
                self.state = 403
                self.match(McInstrParser.LeftBracket)
                self.state = 404
                self.expr(0)
                self.state = 405
                self.match(McInstrParser.RightBracket)
                pass

            elif la_ == 2:
                localctx = McInstrParser.ExpressionFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 407
                self.match(McInstrParser.Identifier)
                self.state = 408
                self.match(McInstrParser.LeftParen)
                self.state = 409
                self.expr(0)
                self.state = 410
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 3:
                localctx = McInstrParser.ExpressionGroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 412
                self.match(McInstrParser.LeftParen)
                self.state = 413
                self.expr(0)
                self.state = 414
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 4:
                localctx = McInstrParser.ExpressionUnaryPMContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 416
                _la = self._input.LA(1)
                if not(_la==135 or _la==136):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 417
                self.expr(7)
                pass

            elif la_ == 5:
                localctx = McInstrParser.ExpressionIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 418
                self.match(McInstrParser.Identifier)
                pass

            elif la_ == 6:
                localctx = McInstrParser.ExpressionFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 419
                self.match(McInstrParser.FloatingLiteral)
                pass

            elif la_ == 7:
                localctx = McInstrParser.ExpressionIntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 420
                self.match(McInstrParser.IntegerLiteral)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 432
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                    if la_ == 1:
                        localctx = McInstrParser.ExpressionExponentiationContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 423
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 424
                        self.match(McInstrParser.Caret)
                        self.state = 425
                        localctx.exponent = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = McInstrParser.ExpressionBinaryMDContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 426
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 427
                        _la = self._input.LA(1)
                        if not(_la==137 or _la==138):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 428
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = McInstrParser.ExpressionBinaryPMContext(self, McInstrParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 429
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 430
                        _la = self._input.LA(1)
                        if not(_la==135 or _la==136):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 431
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

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
        self.enterRule(localctx, 68, self.RULE_shell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(McInstrParser.Shell)
            self.state = 438
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
        self.enterRule(localctx, 70, self.RULE_search)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SearchPathContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(McInstrParser.Search)
                self.state = 441
                self.match(McInstrParser.StringLiteral)
                pass

            elif la_ == 2:
                localctx = McInstrParser.SearchShellContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.match(McInstrParser.Search)
                self.state = 443
                self.match(McInstrParser.Shell)
                self.state = 444
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
            self.content = None # Token


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
        self.enterRule(localctx, 72, self.RULE_unparsed_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(McInstrParser.T__0)
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 449
                        localctx.content = self.matchWildcard() 
                    self.state = 454
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

                pass


            self.state = 457
            self.match(McInstrParser.T__1)
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
        self._predicates[33] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




