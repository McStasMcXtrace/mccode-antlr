# Generated from /home/gst/PycharmProjects/mccode4/mccode/grammar/McInstr.g4 by ANTLR 4.13.0
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
        4,1,187,443,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,1,
        3,1,82,8,1,1,1,3,1,85,8,1,1,1,3,1,88,8,1,1,1,3,1,91,8,1,1,1,3,1,
        94,8,1,1,1,1,1,3,1,98,8,1,1,1,3,1,101,8,1,1,1,1,1,1,2,1,2,1,2,1,
        2,5,2,109,8,2,10,2,12,2,112,9,2,3,2,114,8,2,1,2,1,2,1,3,3,3,119,
        8,3,1,3,1,3,1,3,3,3,124,8,3,1,3,1,3,3,3,128,8,3,1,3,1,3,1,3,1,3,
        3,3,134,8,3,1,3,1,3,3,3,138,8,3,1,3,1,3,1,3,3,3,143,8,3,1,3,1,3,
        1,3,3,3,148,8,3,1,3,1,3,3,3,152,8,3,3,3,154,8,3,1,4,1,4,1,4,1,4,
        4,4,160,8,4,11,4,12,4,161,3,4,164,8,4,1,5,1,5,1,5,1,6,3,6,170,8,
        6,1,6,3,6,173,8,6,1,6,3,6,176,8,6,1,6,1,6,1,6,1,6,1,6,3,6,183,8,
        6,1,6,1,6,3,6,187,8,6,1,6,3,6,190,8,6,1,6,3,6,193,8,6,1,6,3,6,196,
        8,6,1,6,3,6,199,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,208,8,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,218,8,8,1,9,1,9,1,9,1,9,5,9,224,
        8,9,10,9,12,9,227,9,9,3,9,229,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,3,11,241,8,11,1,11,3,11,244,8,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,258,8,13,3,13,
        260,8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,
        272,8,15,3,15,274,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,283,
        8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,295,
        8,18,3,18,297,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,306,8,
        19,3,19,308,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,317,8,20,
        3,20,319,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,328,8,21,3,
        21,330,8,21,1,22,1,22,3,22,334,8,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,
        1,28,1,28,1,28,4,28,358,8,28,11,28,12,28,359,1,29,1,29,1,29,1,29,
        3,29,366,8,29,1,29,1,29,1,29,1,29,1,29,3,29,373,8,29,1,29,3,29,376,
        8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,386,8,30,1,31,
        1,31,1,31,1,31,5,31,392,8,31,10,31,12,31,395,9,31,1,31,1,31,1,31,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,420,8,32,1,32,1,32,1,32,
        1,32,1,32,1,32,5,32,428,8,32,10,32,12,32,431,9,32,1,33,1,33,1,33,
        1,34,1,34,1,34,1,34,1,34,3,34,441,8,34,1,34,1,393,1,64,35,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,0,4,2,0,25,25,27,27,2,0,46,46,174,
        174,1,0,133,134,1,0,135,136,479,0,70,1,0,0,0,2,73,1,0,0,0,4,104,
        1,0,0,0,6,153,1,0,0,0,8,155,1,0,0,0,10,165,1,0,0,0,12,169,1,0,0,
        0,14,207,1,0,0,0,16,217,1,0,0,0,18,219,1,0,0,0,20,232,1,0,0,0,22,
        243,1,0,0,0,24,245,1,0,0,0,26,259,1,0,0,0,28,261,1,0,0,0,30,273,
        1,0,0,0,32,282,1,0,0,0,34,284,1,0,0,0,36,296,1,0,0,0,38,307,1,0,
        0,0,40,318,1,0,0,0,42,329,1,0,0,0,44,331,1,0,0,0,46,335,1,0,0,0,
        48,338,1,0,0,0,50,342,1,0,0,0,52,346,1,0,0,0,54,349,1,0,0,0,56,357,
        1,0,0,0,58,375,1,0,0,0,60,385,1,0,0,0,62,387,1,0,0,0,64,419,1,0,
        0,0,66,432,1,0,0,0,68,440,1,0,0,0,70,71,3,2,1,0,71,72,5,0,0,1,72,
        1,1,0,0,0,73,74,5,5,0,0,74,75,5,12,0,0,75,76,5,174,0,0,76,78,3,4,
        2,0,77,79,3,66,33,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,
        82,3,68,34,0,81,80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,3,28,
        14,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,3,30,15,0,87,
        86,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,91,3,34,17,0,90,89,1,0,
        0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,3,36,18,0,93,92,1,0,0,0,93,
        94,1,0,0,0,94,95,1,0,0,0,95,97,3,8,4,0,96,98,3,38,19,0,97,96,1,0,
        0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,101,3,40,20,0,100,99,1,0,0,0,
        100,101,1,0,0,0,101,102,1,0,0,0,102,103,5,8,0,0,103,3,1,0,0,0,104,
        113,5,127,0,0,105,110,3,6,3,0,106,107,5,164,0,0,107,109,3,6,3,0,
        108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,
        111,114,1,0,0,0,112,110,1,0,0,0,113,105,1,0,0,0,113,114,1,0,0,0,
        114,115,1,0,0,0,115,116,5,128,0,0,116,5,1,0,0,0,117,119,5,72,0,0,
        118,117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,123,5,174,0,
        0,121,122,5,136,0,0,122,124,5,46,0,0,123,121,1,0,0,0,123,124,1,0,
        0,0,124,127,1,0,0,0,125,126,5,143,0,0,126,128,3,64,32,0,127,125,
        1,0,0,0,127,128,1,0,0,0,128,154,1,0,0,0,129,130,5,87,0,0,130,133,
        5,174,0,0,131,132,5,136,0,0,132,134,5,46,0,0,133,131,1,0,0,0,133,
        134,1,0,0,0,134,137,1,0,0,0,135,136,5,143,0,0,136,138,3,64,32,0,
        137,135,1,0,0,0,137,138,1,0,0,0,138,154,1,0,0,0,139,143,5,38,0,0,
        140,141,5,60,0,0,141,143,5,135,0,0,142,139,1,0,0,0,142,140,1,0,0,
        0,143,144,1,0,0,0,144,147,5,174,0,0,145,146,5,136,0,0,146,148,5,
        46,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,151,1,0,0,0,149,150,5,
        143,0,0,150,152,5,46,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,154,
        1,0,0,0,153,118,1,0,0,0,153,129,1,0,0,0,153,142,1,0,0,0,154,7,1,
        0,0,0,155,163,5,19,0,0,156,160,3,12,6,0,157,160,3,68,34,0,158,160,
        3,10,5,0,159,156,1,0,0,0,159,157,1,0,0,0,159,158,1,0,0,0,160,161,
        1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,159,
        1,0,0,0,163,164,1,0,0,0,164,9,1,0,0,0,165,166,5,41,0,0,166,167,5,
        46,0,0,167,11,1,0,0,0,168,170,5,31,0,0,169,168,1,0,0,0,169,170,1,
        0,0,0,170,172,1,0,0,0,171,173,5,32,0,0,172,171,1,0,0,0,172,173,1,
        0,0,0,173,175,1,0,0,0,174,176,3,44,22,0,175,174,1,0,0,0,175,176,
        1,0,0,0,176,177,1,0,0,0,177,178,5,3,0,0,178,179,3,14,7,0,179,180,
        5,143,0,0,180,182,3,16,8,0,181,183,3,46,23,0,182,181,1,0,0,0,182,
        183,1,0,0,0,183,184,1,0,0,0,184,186,3,48,24,0,185,187,3,50,25,0,
        186,185,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,190,3,52,26,
        0,189,188,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,193,3,54,27,
        0,192,191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,196,3,56,28,
        0,195,194,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,199,3,60,30,
        0,198,197,1,0,0,0,198,199,1,0,0,0,199,13,1,0,0,0,200,201,5,29,0,
        0,201,202,5,127,0,0,202,203,5,174,0,0,203,208,5,128,0,0,204,208,
        5,28,0,0,205,208,5,29,0,0,206,208,5,174,0,0,207,200,1,0,0,0,207,
        204,1,0,0,0,207,205,1,0,0,0,207,206,1,0,0,0,208,15,1,0,0,0,209,210,
        5,29,0,0,210,211,5,127,0,0,211,212,3,22,11,0,212,213,5,128,0,0,213,
        214,3,18,9,0,214,218,1,0,0,0,215,216,5,174,0,0,216,218,3,18,9,0,
        217,209,1,0,0,0,217,215,1,0,0,0,218,17,1,0,0,0,219,228,5,127,0,0,
        220,225,3,20,10,0,221,222,5,164,0,0,222,224,3,20,10,0,223,221,1,
        0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,229,1,
        0,0,0,227,225,1,0,0,0,228,220,1,0,0,0,228,229,1,0,0,0,229,230,1,
        0,0,0,230,231,5,128,0,0,231,19,1,0,0,0,232,233,5,174,0,0,233,234,
        5,143,0,0,234,235,3,64,32,0,235,21,1,0,0,0,236,240,5,17,0,0,237,
        238,5,127,0,0,238,239,5,43,0,0,239,241,5,128,0,0,240,237,1,0,0,0,
        240,241,1,0,0,0,241,244,1,0,0,0,242,244,5,174,0,0,243,236,1,0,0,
        0,243,242,1,0,0,0,244,23,1,0,0,0,245,246,5,127,0,0,246,247,3,64,
        32,0,247,248,5,164,0,0,248,249,3,64,32,0,249,250,5,164,0,0,250,251,
        3,64,32,0,251,252,5,128,0,0,252,25,1,0,0,0,253,260,5,1,0,0,254,257,
        5,15,0,0,255,258,5,1,0,0,256,258,3,22,11,0,257,255,1,0,0,0,257,256,
        1,0,0,0,258,260,1,0,0,0,259,253,1,0,0,0,259,254,1,0,0,0,260,27,1,
        0,0,0,261,262,5,34,0,0,262,263,5,46,0,0,263,29,1,0,0,0,264,265,5,
        6,0,0,265,274,5,40,0,0,266,267,5,6,0,0,267,268,5,29,0,0,268,271,
        5,174,0,0,269,270,5,21,0,0,270,272,5,40,0,0,271,269,1,0,0,0,271,
        272,1,0,0,0,272,274,1,0,0,0,273,264,1,0,0,0,273,266,1,0,0,0,274,
        31,1,0,0,0,275,276,5,20,0,0,276,283,5,40,0,0,277,278,5,20,0,0,278,
        279,5,29,0,0,279,280,5,174,0,0,280,281,5,21,0,0,281,283,5,40,0,0,
        282,275,1,0,0,0,282,277,1,0,0,0,283,33,1,0,0,0,284,285,5,4,0,0,285,
        286,5,40,0,0,286,35,1,0,0,0,287,288,5,11,0,0,288,297,5,40,0,0,289,
        290,5,11,0,0,290,291,5,29,0,0,291,294,5,174,0,0,292,293,5,21,0,0,
        293,295,5,40,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,297,1,0,0,0,
        296,287,1,0,0,0,296,289,1,0,0,0,297,37,1,0,0,0,298,299,5,23,0,0,
        299,308,5,40,0,0,300,301,5,23,0,0,301,302,5,29,0,0,302,305,5,174,
        0,0,303,304,5,21,0,0,304,306,5,40,0,0,305,303,1,0,0,0,305,306,1,
        0,0,0,306,308,1,0,0,0,307,298,1,0,0,0,307,300,1,0,0,0,308,39,1,0,
        0,0,309,310,5,10,0,0,310,319,5,40,0,0,311,312,5,10,0,0,312,313,5,
        29,0,0,313,316,5,174,0,0,314,315,5,21,0,0,315,317,5,40,0,0,316,314,
        1,0,0,0,316,317,1,0,0,0,317,319,1,0,0,0,318,309,1,0,0,0,318,311,
        1,0,0,0,319,41,1,0,0,0,320,321,5,9,0,0,321,330,5,40,0,0,322,323,
        5,9,0,0,323,324,5,29,0,0,324,327,5,174,0,0,325,326,5,21,0,0,326,
        328,5,40,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,330,1,0,0,0,329,
        320,1,0,0,0,329,322,1,0,0,0,330,43,1,0,0,0,331,333,5,30,0,0,332,
        334,3,64,32,0,333,332,1,0,0,0,333,334,1,0,0,0,334,45,1,0,0,0,335,
        336,5,25,0,0,336,337,3,64,32,0,337,47,1,0,0,0,338,339,5,2,0,0,339,
        340,3,24,12,0,340,341,3,26,13,0,341,49,1,0,0,0,342,343,5,16,0,0,
        343,344,3,24,12,0,344,345,3,26,13,0,345,51,1,0,0,0,346,347,5,22,
        0,0,347,348,5,174,0,0,348,53,1,0,0,0,349,350,5,21,0,0,350,351,5,
        40,0,0,351,55,1,0,0,0,352,353,5,24,0,0,353,354,3,58,29,0,354,355,
        7,0,0,0,355,356,3,64,32,0,356,358,1,0,0,0,357,352,1,0,0,0,358,359,
        1,0,0,0,359,357,1,0,0,0,359,360,1,0,0,0,360,57,1,0,0,0,361,365,5,
        17,0,0,362,363,5,127,0,0,363,364,5,43,0,0,364,366,5,128,0,0,365,
        362,1,0,0,0,365,366,1,0,0,0,366,376,1,0,0,0,367,376,5,28,0,0,368,
        372,5,26,0,0,369,370,5,127,0,0,370,371,5,43,0,0,371,373,5,128,0,
        0,372,369,1,0,0,0,372,373,1,0,0,0,373,376,1,0,0,0,374,376,5,174,
        0,0,375,361,1,0,0,0,375,367,1,0,0,0,375,368,1,0,0,0,375,374,1,0,
        0,0,376,59,1,0,0,0,377,378,5,37,0,0,378,379,7,1,0,0,379,380,5,174,
        0,0,380,386,5,40,0,0,381,382,5,37,0,0,382,383,7,1,0,0,383,384,5,
        46,0,0,384,386,5,40,0,0,385,377,1,0,0,0,385,381,1,0,0,0,386,61,1,
        0,0,0,387,393,5,131,0,0,388,389,3,64,32,0,389,390,5,164,0,0,390,
        392,1,0,0,0,391,388,1,0,0,0,392,395,1,0,0,0,393,394,1,0,0,0,393,
        391,1,0,0,0,394,396,1,0,0,0,395,393,1,0,0,0,396,397,3,64,32,0,397,
        398,5,132,0,0,398,63,1,0,0,0,399,400,6,32,-1,0,400,401,7,2,0,0,401,
        420,3,64,32,9,402,403,5,127,0,0,403,404,3,64,32,0,404,405,5,128,
        0,0,405,420,1,0,0,0,406,420,5,174,0,0,407,408,5,174,0,0,408,409,
        5,129,0,0,409,410,3,64,32,0,410,411,5,130,0,0,411,420,1,0,0,0,412,
        413,5,174,0,0,413,414,5,127,0,0,414,415,3,64,32,0,415,416,5,128,
        0,0,416,420,1,0,0,0,417,420,5,45,0,0,418,420,5,43,0,0,419,399,1,
        0,0,0,419,402,1,0,0,0,419,406,1,0,0,0,419,407,1,0,0,0,419,412,1,
        0,0,0,419,417,1,0,0,0,419,418,1,0,0,0,420,429,1,0,0,0,421,422,10,
        8,0,0,422,423,7,3,0,0,423,428,3,64,32,9,424,425,10,7,0,0,425,426,
        7,2,0,0,426,428,3,64,32,8,427,421,1,0,0,0,427,424,1,0,0,0,428,431,
        1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,65,1,0,0,0,431,429,1,
        0,0,0,432,433,5,35,0,0,433,434,5,46,0,0,434,67,1,0,0,0,435,436,5,
        36,0,0,436,441,5,46,0,0,437,438,5,36,0,0,438,439,5,35,0,0,439,441,
        5,46,0,0,440,435,1,0,0,0,440,437,1,0,0,0,441,69,1,0,0,0,61,78,81,
        84,87,90,93,97,100,110,113,118,123,127,133,137,142,147,151,153,159,
        161,163,169,172,175,182,186,189,192,195,198,207,217,225,228,240,
        243,257,259,271,273,282,294,296,305,307,316,318,327,329,333,359,
        365,372,375,385,393,419,427,429,440
    ]

class McInstrParser ( Parser ):

    grammarFileName = "McInstr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ABSOLUTE'", "'AT'", "'COMPONENT'", "'USERVARS'", 
                     "'DEFINE'", "'DECLARE'", "'DEFINITION'", "'END'", "<INVALID>", 
                     "'FINALLY'", "<INVALID>", "'INSTRUMENT'", "<INVALID>", 
                     "'PARAMETERS'", "'RELATIVE'", "'ROTATED'", "'PREVIOUS'", 
                     "'SETTING'", "'TRACE'", "'SHARE'", "'EXTEND'", "'GROUP'", 
                     "'SAVE'", "'JUMP'", "'WHEN'", "'NEXT'", "'ITERATE'", 
                     "'MYSELF'", "'COPY'", "'SPLIT'", "'REMOVABLE'", "'CPU'", 
                     "'NOACC'", "'DEPENDENCY'", "'SHELL'", "'SEARCH'", "'METADATA'", 
                     "'string'", "'vector'", "<INVALID>", "'%include'", 
                     "'NULL'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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

    symbolicNames = [ "<INVALID>", "Absolute", "At", "Component", "UserVars", 
                      "Define", "Declare", "Definition", "End", "McDisplay", 
                      "Finally", "Initialize", "Instrument", "Output", "Parameters", 
                      "Relative", "Rotated", "Previous", "Setting", "Trace", 
                      "Share", "Extend", "Group", "Save", "Jump", "When", 
                      "Next", "Iterate", "Myself", "Copy", "Split", "Removable", 
                      "Cpu", "NoAcc", "Dependency", "Shell", "Search", "MetaData", 
                      "String", "Vector", "UnparsedBlock", "Include", "Null", 
                      "IntegerLiteral", "CharacterLiteral", "FloatingLiteral", 
                      "StringLiteral", "BooleanLitteral", "PointerLiteral", 
                      "UserDefinedLiteral", "MultiLineMacro", "Directive", 
                      "Alignas", "Alignof", "Asm", "Auto", "Bool", "Break", 
                      "Case", "Catch", "Char", "Char16", "Char32", "Class", 
                      "Const", "Constexpr", "Const_cast", "Continue", "Decltype", 
                      "Default", "Delete", "Do", "Double", "Dynamic_cast", 
                      "Else", "Enum", "Explicit", "Export", "Extern", "False_", 
                      "Final", "Float", "For", "Friend", "Goto", "If", "Inline", 
                      "Int", "Long", "Mutable", "Namespace", "New", "Noexcept", 
                      "Nullptr", "Operator", "Override", "Private", "Protected", 
                      "Public", "Register", "Reinterpret_cast", "Return", 
                      "Short", "Signed", "Sizeof", "Static", "Static_assert", 
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
    RULE_instrument_trace = 4
    RULE_instrument_trace_include = 5
    RULE_component_instance = 6
    RULE_instance_name = 7
    RULE_component_type = 8
    RULE_instance_parameters = 9
    RULE_instance_parameter = 10
    RULE_component_ref = 11
    RULE_coords = 12
    RULE_reference = 13
    RULE_dependency = 14
    RULE_declare = 15
    RULE_share = 16
    RULE_uservars = 17
    RULE_initialize = 18
    RULE_save = 19
    RULE_finally_ = 20
    RULE_display = 21
    RULE_split = 22
    RULE_when = 23
    RULE_place = 24
    RULE_orientation = 25
    RULE_groupref = 26
    RULE_extend = 27
    RULE_jump = 28
    RULE_jumpname = 29
    RULE_metadata = 30
    RULE_initializerlist = 31
    RULE_simple_expression = 32
    RULE_shell = 33
    RULE_search = 34

    ruleNames =  [ "prog", "instrument_definition", "instrument_parameters", 
                   "instrument_parameter", "instrument_trace", "instrument_trace_include", 
                   "component_instance", "instance_name", "component_type", 
                   "instance_parameters", "instance_parameter", "component_ref", 
                   "coords", "reference", "dependency", "declare", "share", 
                   "uservars", "initialize", "save", "finally_", "display", 
                   "split", "when", "place", "orientation", "groupref", 
                   "extend", "jump", "jumpname", "metadata", "initializerlist", 
                   "simple_expression", "shell", "search" ]

    EOF = Token.EOF
    Absolute=1
    At=2
    Component=3
    UserVars=4
    Define=5
    Declare=6
    Definition=7
    End=8
    McDisplay=9
    Finally=10
    Initialize=11
    Instrument=12
    Output=13
    Parameters=14
    Relative=15
    Rotated=16
    Previous=17
    Setting=18
    Trace=19
    Share=20
    Extend=21
    Group=22
    Save=23
    Jump=24
    When=25
    Next=26
    Iterate=27
    Myself=28
    Copy=29
    Split=30
    Removable=31
    Cpu=32
    NoAcc=33
    Dependency=34
    Shell=35
    Search=36
    MetaData=37
    String=38
    Vector=39
    UnparsedBlock=40
    Include=41
    Null=42
    IntegerLiteral=43
    CharacterLiteral=44
    FloatingLiteral=45
    StringLiteral=46
    BooleanLitteral=47
    PointerLiteral=48
    UserDefinedLiteral=49
    MultiLineMacro=50
    Directive=51
    Alignas=52
    Alignof=53
    Asm=54
    Auto=55
    Bool=56
    Break=57
    Case=58
    Catch=59
    Char=60
    Char16=61
    Char32=62
    Class=63
    Const=64
    Constexpr=65
    Const_cast=66
    Continue=67
    Decltype=68
    Default=69
    Delete=70
    Do=71
    Double=72
    Dynamic_cast=73
    Else=74
    Enum=75
    Explicit=76
    Export=77
    Extern=78
    False_=79
    Final=80
    Float=81
    For=82
    Friend=83
    Goto=84
    If=85
    Inline=86
    Int=87
    Long=88
    Mutable=89
    Namespace=90
    New=91
    Noexcept=92
    Nullptr=93
    Operator=94
    Override=95
    Private=96
    Protected=97
    Public=98
    Register=99
    Reinterpret_cast=100
    Return=101
    Short=102
    Signed=103
    Sizeof=104
    Static=105
    Static_assert=106
    Static_cast=107
    Struct=108
    Switch=109
    Template=110
    This=111
    Thread_local=112
    Throw=113
    True_=114
    Try=115
    Typedef=116
    Typeid_=117
    Typename_=118
    Union=119
    Unsigned=120
    Using=121
    Virtual=122
    Void=123
    Volatile=124
    Wchar=125
    While=126
    LeftParen=127
    RightParen=128
    LeftBracket=129
    RightBracket=130
    LeftBrace=131
    RightBrace=132
    Plus=133
    Minus=134
    Star=135
    Div=136
    Mod=137
    Caret=138
    And=139
    Or=140
    Tilde=141
    Not=142
    Assign=143
    Less=144
    Greater=145
    PlusAssign=146
    MinusAssign=147
    StarAssign=148
    DivAssign=149
    ModAssign=150
    XorAssign=151
    AndAssign=152
    OrAssign=153
    LeftShiftAssign=154
    RightShiftAssign=155
    Equal=156
    NotEqual=157
    LessEqual=158
    GreaterEqual=159
    AndAnd=160
    OrOr=161
    PlusPlus=162
    MinusMinus=163
    Comma=164
    ArrowStar=165
    Arrow=166
    Question=167
    Colon=168
    Doublecolon=169
    Semi=170
    Dot=171
    DotStar=172
    Ellipsis=173
    Identifier=174
    DecimalLiteral=175
    OctalLiteral=176
    HexadecimalLiteral=177
    BinaryLiteral=178
    IntegerSuffix=179
    UserDefinedIntegerLiteral=180
    UserDefinedFloatingLiteral=181
    UserDefinedStringLiteral=182
    UserDefinedCharacterLiteral=183
    Whitespace=184
    Newline=185
    BlockComment=186
    LineComment=187

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
            self.state = 70
            self.instrument_definition()
            self.state = 71
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
            self.state = 73
            self.match(McInstrParser.Define)
            self.state = 74
            self.match(McInstrParser.Instrument)
            self.state = 75
            self.match(McInstrParser.Identifier)
            self.state = 76
            self.instrument_parameters()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 77
                self.shell()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 80
                self.search()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 83
                self.dependency()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 86
                self.declare()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 89
                self.uservars()


            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 92
                self.initialize()


            self.state = 95
            self.instrument_trace()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 96
                self.save()


            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 99
                self.finally_()


            self.state = 102
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
            self.state = 104
            self.match(McInstrParser.LeftParen)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & 562967137484801) != 0) or _la==174:
                self.state = 105
                self.instrument_parameter()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==164:
                    self.state = 106
                    self.match(McInstrParser.Comma)
                    self.state = 107
                    self.instrument_parameter()
                    self.state = 112
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 115
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
        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)


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
        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)


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
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [72, 174]:
                localctx = McInstrParser.InstrumentParameterDoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==72:
                    self.state = 117
                    self.match(McInstrParser.Double)


                self.state = 120
                self.match(McInstrParser.Identifier)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==136:
                    self.state = 121
                    self.match(McInstrParser.Div)
                    self.state = 122
                    self.match(McInstrParser.StringLiteral)


                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==143:
                    self.state = 125
                    self.match(McInstrParser.Assign)
                    self.state = 126
                    self.simple_expression(0)


                pass
            elif token in [87]:
                localctx = McInstrParser.InstrumentParameterIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(McInstrParser.Int)
                self.state = 130
                self.match(McInstrParser.Identifier)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==136:
                    self.state = 131
                    self.match(McInstrParser.Div)
                    self.state = 132
                    self.match(McInstrParser.StringLiteral)


                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==143:
                    self.state = 135
                    self.match(McInstrParser.Assign)
                    self.state = 136
                    self.simple_expression(0)


                pass
            elif token in [38, 60]:
                localctx = McInstrParser.InstrumentParameterStringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 139
                    self.match(McInstrParser.String)
                    pass
                elif token in [60]:
                    self.state = 140
                    self.match(McInstrParser.Char)
                    self.state = 141
                    self.match(McInstrParser.Star)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144
                self.match(McInstrParser.Identifier)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==136:
                    self.state = 145
                    self.match(McInstrParser.Div)
                    self.state = 146
                    self.match(McInstrParser.StringLiteral)


                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==143:
                    self.state = 149
                    self.match(McInstrParser.Assign)
                    self.state = 150
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
            self.state = 155
            self.match(McInstrParser.Trace)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2275258925064) != 0):
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 159
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 30, 31, 32]:
                        self.state = 156
                        self.component_instance()
                        pass
                    elif token in [36]:
                        self.state = 157
                        self.search()
                        pass
                    elif token in [41]:
                        self.state = 158
                        self.instrument_trace_include()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 161 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2275258925064) != 0)):
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
            self.state = 165
            self.match(McInstrParser.Include)
            self.state = 166
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
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 168
                self.match(McInstrParser.Removable)


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 171
                self.match(McInstrParser.Cpu)


            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 174
                self.split()


            self.state = 177
            self.match(McInstrParser.Component)
            self.state = 178
            self.instance_name()
            self.state = 179
            self.match(McInstrParser.Assign)
            self.state = 180
            self.component_type()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 181
                self.when()


            self.state = 184
            self.place()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 185
                self.orientation()


            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 188
                self.groupref()


            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 191
                self.extend()


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 194
                self.jump()


            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 197
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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InstanceNameCopyIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(McInstrParser.Copy)
                self.state = 201
                self.match(McInstrParser.LeftParen)
                self.state = 202
                self.match(McInstrParser.Identifier)
                self.state = 203
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 2:
                localctx = McInstrParser.InstanceNameMyselfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(McInstrParser.Myself)
                pass

            elif la_ == 3:
                localctx = McInstrParser.InstanceNameCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(McInstrParser.Copy)
                pass

            elif la_ == 4:
                localctx = McInstrParser.InstanceNameIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 206
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                localctx = McInstrParser.ComponentTypeCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(McInstrParser.Copy)
                self.state = 210
                self.match(McInstrParser.LeftParen)
                self.state = 211
                self.component_ref()
                self.state = 212
                self.match(McInstrParser.RightParen)
                self.state = 213
                self.instance_parameters()
                pass
            elif token in [174]:
                localctx = McInstrParser.ComponentTypeIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(McInstrParser.Identifier)
                self.state = 216
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
            self.state = 219
            self.match(McInstrParser.LeftParen)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 220
                self.instance_parameter()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==164:
                    self.state = 221
                    self.match(McInstrParser.Comma)
                    self.state = 222
                    self.instance_parameter()
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 230
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

        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)


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
            self.state = 232
            self.match(McInstrParser.Identifier)
            self.state = 233
            self.match(McInstrParser.Assign)
            self.state = 234
            self.simple_expression(0)
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
        self.enterRule(localctx, 22, self.RULE_component_ref)
        self._la = 0 # Token type
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(McInstrParser.Previous)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==127:
                    self.state = 237
                    self.match(McInstrParser.LeftParen)
                    self.state = 238
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 239
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [174]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
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

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,i)


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
        self.enterRule(localctx, 24, self.RULE_coords)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(McInstrParser.LeftParen)
            self.state = 246
            self.simple_expression(0)
            self.state = 247
            self.match(McInstrParser.Comma)
            self.state = 248
            self.simple_expression(0)
            self.state = 249
            self.match(McInstrParser.Comma)
            self.state = 250
            self.simple_expression(0)
            self.state = 251
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
        self.enterRule(localctx, 26, self.RULE_reference)
        try:
            self.state = 259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(McInstrParser.Absolute)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(McInstrParser.Relative)
                self.state = 257
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 255
                    self.match(McInstrParser.Absolute)
                    pass
                elif token in [17, 174]:
                    self.state = 256
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
        self.enterRule(localctx, 28, self.RULE_dependency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(McInstrParser.Dependency)
            self.state = 262
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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 30, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.DeclareBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(McInstrParser.Declare)
                self.state = 265
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.DeclareBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(McInstrParser.Declare)
                self.state = 267
                self.match(McInstrParser.Copy)
                self.state = 268
                self.match(McInstrParser.Identifier)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 269
                    self.match(McInstrParser.Extend)
                    self.state = 270
                    self.match(McInstrParser.UnparsedBlock)


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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 32, self.RULE_share)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.ShareBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(McInstrParser.Share)
                self.state = 276
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.ShareBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(McInstrParser.Share)
                self.state = 278
                self.match(McInstrParser.Copy)
                self.state = 279
                self.match(McInstrParser.Identifier)

                self.state = 280
                self.match(McInstrParser.Extend)
                self.state = 281
                self.match(McInstrParser.UnparsedBlock)
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

        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 34, self.RULE_uservars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(McInstrParser.UserVars)
            self.state = 285
            self.match(McInstrParser.UnparsedBlock)
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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 36, self.RULE_initialize)
        self._la = 0 # Token type
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.InitializeBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(McInstrParser.Initialize)
                self.state = 288
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.InitializeBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(McInstrParser.Initialize)
                self.state = 290
                self.match(McInstrParser.Copy)
                self.state = 291
                self.match(McInstrParser.Identifier)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 292
                    self.match(McInstrParser.Extend)
                    self.state = 293
                    self.match(McInstrParser.UnparsedBlock)


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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 38, self.RULE_save)
        self._la = 0 # Token type
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SaveBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(McInstrParser.Save)
                self.state = 299
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.SaveBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(McInstrParser.Save)
                self.state = 301
                self.match(McInstrParser.Copy)
                self.state = 302
                self.match(McInstrParser.Identifier)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 303
                    self.match(McInstrParser.Extend)
                    self.state = 304
                    self.match(McInstrParser.UnparsedBlock)


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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 40, self.RULE_finally_)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.FinallyBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.match(McInstrParser.Finally)
                self.state = 310
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.FinallyBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.match(McInstrParser.Finally)
                self.state = 312
                self.match(McInstrParser.Copy)
                self.state = 313
                self.match(McInstrParser.Identifier)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 314
                    self.match(McInstrParser.Extend)
                    self.state = 315
                    self.match(McInstrParser.UnparsedBlock)


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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 42, self.RULE_display)
        self._la = 0 # Token type
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.DisplayBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(McInstrParser.McDisplay)
                self.state = 321
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.DisplayBlockCopyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(McInstrParser.McDisplay)
                self.state = 323
                self.match(McInstrParser.Copy)
                self.state = 324
                self.match(McInstrParser.Identifier)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 325
                    self.match(McInstrParser.Extend)
                    self.state = 326
                    self.match(McInstrParser.UnparsedBlock)


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

        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)


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
        self.enterRule(localctx, 44, self.RULE_split)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(McInstrParser.Split)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43 or _la==45 or ((((_la - 127)) & ~0x3f) == 0 and ((1 << (_la - 127)) & 140737488355521) != 0):
                self.state = 332
                self.simple_expression(0)


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

        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)


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
        self.enterRule(localctx, 46, self.RULE_when)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(McInstrParser.When)
            self.state = 336
            self.simple_expression(0)
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
        self.enterRule(localctx, 48, self.RULE_place)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(McInstrParser.At)
            self.state = 339
            self.coords()
            self.state = 340
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
        self.enterRule(localctx, 50, self.RULE_orientation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(McInstrParser.Rotated)
            self.state = 343
            self.coords()
            self.state = 344
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
        self.enterRule(localctx, 52, self.RULE_groupref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(McInstrParser.Group)
            self.state = 347
            self.match(McInstrParser.Identifier)
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

        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)

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
        self.enterRule(localctx, 54, self.RULE_extend)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(McInstrParser.Extend)
            self.state = 350
            self.match(McInstrParser.UnparsedBlock)
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


        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,i)


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
        self.enterRule(localctx, 56, self.RULE_jump)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 352
                self.match(McInstrParser.Jump)
                self.state = 353
                self.jumpname()
                self.state = 354
                _la = self._input.LA(1)
                if not(_la==25 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 355
                self.simple_expression(0)
                self.state = 359 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
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
        self.enterRule(localctx, 58, self.RULE_jumpname)
        self._la = 0 # Token type
        try:
            self.state = 375
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(McInstrParser.Previous)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==127:
                    self.state = 362
                    self.match(McInstrParser.LeftParen)
                    self.state = 363
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 364
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(McInstrParser.Myself)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
                self.match(McInstrParser.Next)
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==127:
                    self.state = 369
                    self.match(McInstrParser.LeftParen)
                    self.state = 370
                    self.match(McInstrParser.IntegerLiteral)
                    self.state = 371
                    self.match(McInstrParser.RightParen)


                pass
            elif token in [174]:
                self.enterOuterAlt(localctx, 4)
                self.state = 374
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


    class MetadataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_metadata

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MetadataSimpleNameContext(MetadataContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.MetadataContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MetaData(self):
            return self.getToken(McInstrParser.MetaData, 0)
        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.Identifier)
            else:
                return self.getToken(McInstrParser.Identifier, i)
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)
        def StringLiteral(self):
            return self.getToken(McInstrParser.StringLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadataSimpleName" ):
                listener.enterMetadataSimpleName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadataSimpleName" ):
                listener.exitMetadataSimpleName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadataSimpleName" ):
                return visitor.visitMetadataSimpleName(self)
            else:
                return visitor.visitChildren(self)


    class MetadataStringNameContext(MetadataContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.MetadataContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MetaData(self):
            return self.getToken(McInstrParser.MetaData, 0)
        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(McInstrParser.StringLiteral)
            else:
                return self.getToken(McInstrParser.StringLiteral, i)
        def UnparsedBlock(self):
            return self.getToken(McInstrParser.UnparsedBlock, 0)
        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadataStringName" ):
                listener.enterMetadataStringName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadataStringName" ):
                listener.exitMetadataStringName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMetadataStringName" ):
                return visitor.visitMetadataStringName(self)
            else:
                return visitor.visitChildren(self)



    def metadata(self):

        localctx = McInstrParser.MetadataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_metadata)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.MetadataSimpleNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(McInstrParser.MetaData)
                self.state = 378
                _la = self._input.LA(1)
                if not(_la==46 or _la==174):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 379
                self.match(McInstrParser.Identifier)
                self.state = 380
                self.match(McInstrParser.UnparsedBlock)
                pass

            elif la_ == 2:
                localctx = McInstrParser.MetadataStringNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(McInstrParser.MetaData)
                self.state = 382
                _la = self._input.LA(1)
                if not(_la==46 or _la==174):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 383
                self.match(McInstrParser.StringLiteral)
                self.state = 384
                self.match(McInstrParser.UnparsedBlock)
                pass


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

        def LeftBrace(self):
            return self.getToken(McInstrParser.LeftBrace, 0)

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,i)


        def RightBrace(self):
            return self.getToken(McInstrParser.RightBrace, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(McInstrParser.LeftBrace)
            self.state = 393
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 388
                    self.simple_expression(0)
                    self.state = 389
                    self.match(McInstrParser.Comma) 
                self.state = 395
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

            self.state = 396
            self.simple_expression(0)
            self.state = 397
            self.match(McInstrParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return McInstrParser.RULE_simple_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SimpleExpressionUnaryPMContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)

        def Plus(self):
            return self.getToken(McInstrParser.Plus, 0)
        def Minus(self):
            return self.getToken(McInstrParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionUnaryPM" ):
                listener.enterSimpleExpressionUnaryPM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionUnaryPM" ):
                listener.exitSimpleExpressionUnaryPM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionUnaryPM" ):
                return visitor.visitSimpleExpressionUnaryPM(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionGroupingContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionGrouping" ):
                listener.enterSimpleExpressionGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionGrouping" ):
                listener.exitSimpleExpressionGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionGrouping" ):
                return visitor.visitSimpleExpressionGrouping(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionBinaryMDContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,i)

        def Star(self):
            return self.getToken(McInstrParser.Star, 0)
        def Div(self):
            return self.getToken(McInstrParser.Div, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionBinaryMD" ):
                listener.enterSimpleExpressionBinaryMD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionBinaryMD" ):
                listener.exitSimpleExpressionBinaryMD(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionBinaryMD" ):
                return visitor.visitSimpleExpressionBinaryMD(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionBinaryPMContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(McInstrParser.Simple_expressionContext)
            else:
                return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,i)

        def Plus(self):
            return self.getToken(McInstrParser.Plus, 0)
        def Minus(self):
            return self.getToken(McInstrParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionBinaryPM" ):
                listener.enterSimpleExpressionBinaryPM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionBinaryPM" ):
                listener.exitSimpleExpressionBinaryPM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionBinaryPM" ):
                return visitor.visitSimpleExpressionBinaryPM(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionArrayAccessContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def LeftBracket(self):
            return self.getToken(McInstrParser.LeftBracket, 0)
        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)

        def RightBracket(self):
            return self.getToken(McInstrParser.RightBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionArrayAccess" ):
                listener.enterSimpleExpressionArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionArrayAccess" ):
                listener.exitSimpleExpressionArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionArrayAccess" ):
                return visitor.visitSimpleExpressionArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionIntegerContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IntegerLiteral(self):
            return self.getToken(McInstrParser.IntegerLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionInteger" ):
                listener.enterSimpleExpressionInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionInteger" ):
                listener.exitSimpleExpressionInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionInteger" ):
                return visitor.visitSimpleExpressionInteger(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionFunctionCallContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)
        def LeftParen(self):
            return self.getToken(McInstrParser.LeftParen, 0)
        def simple_expression(self):
            return self.getTypedRuleContext(McInstrParser.Simple_expressionContext,0)

        def RightParen(self):
            return self.getToken(McInstrParser.RightParen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionFunctionCall" ):
                listener.enterSimpleExpressionFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionFunctionCall" ):
                listener.exitSimpleExpressionFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionFunctionCall" ):
                return visitor.visitSimpleExpressionFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionIdentifierContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(McInstrParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionIdentifier" ):
                listener.enterSimpleExpressionIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionIdentifier" ):
                listener.exitSimpleExpressionIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionIdentifier" ):
                return visitor.visitSimpleExpressionIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class SimpleExpressionFloatContext(Simple_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a McInstrParser.Simple_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FloatingLiteral(self):
            return self.getToken(McInstrParser.FloatingLiteral, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpressionFloat" ):
                listener.enterSimpleExpressionFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpressionFloat" ):
                listener.exitSimpleExpressionFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleExpressionFloat" ):
                return visitor.visitSimpleExpressionFloat(self)
            else:
                return visitor.visitChildren(self)



    def simple_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = McInstrParser.Simple_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_simple_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SimpleExpressionUnaryPMContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 400
                _la = self._input.LA(1)
                if not(_la==133 or _la==134):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 401
                self.simple_expression(9)
                pass

            elif la_ == 2:
                localctx = McInstrParser.SimpleExpressionGroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 402
                self.match(McInstrParser.LeftParen)
                self.state = 403
                self.simple_expression(0)
                self.state = 404
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 3:
                localctx = McInstrParser.SimpleExpressionIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 406
                self.match(McInstrParser.Identifier)
                pass

            elif la_ == 4:
                localctx = McInstrParser.SimpleExpressionArrayAccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 407
                self.match(McInstrParser.Identifier)
                self.state = 408
                self.match(McInstrParser.LeftBracket)
                self.state = 409
                self.simple_expression(0)
                self.state = 410
                self.match(McInstrParser.RightBracket)
                pass

            elif la_ == 5:
                localctx = McInstrParser.SimpleExpressionFunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 412
                self.match(McInstrParser.Identifier)
                self.state = 413
                self.match(McInstrParser.LeftParen)
                self.state = 414
                self.simple_expression(0)
                self.state = 415
                self.match(McInstrParser.RightParen)
                pass

            elif la_ == 6:
                localctx = McInstrParser.SimpleExpressionFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 417
                self.match(McInstrParser.FloatingLiteral)
                pass

            elif la_ == 7:
                localctx = McInstrParser.SimpleExpressionIntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 418
                self.match(McInstrParser.IntegerLiteral)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                    if la_ == 1:
                        localctx = McInstrParser.SimpleExpressionBinaryMDContext(self, McInstrParser.Simple_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_expression)
                        self.state = 421
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 422
                        _la = self._input.LA(1)
                        if not(_la==135 or _la==136):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 423
                        self.simple_expression(9)
                        pass

                    elif la_ == 2:
                        localctx = McInstrParser.SimpleExpressionBinaryPMContext(self, McInstrParser.Simple_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_expression)
                        self.state = 424
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 425
                        _la = self._input.LA(1)
                        if not(_la==133 or _la==134):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 426
                        self.simple_expression(8)
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_shell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(McInstrParser.Shell)
            self.state = 433
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
        self.enterRule(localctx, 68, self.RULE_search)
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                localctx = McInstrParser.SearchPathContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(McInstrParser.Search)
                self.state = 436
                self.match(McInstrParser.StringLiteral)
                pass

            elif la_ == 2:
                localctx = McInstrParser.SearchShellContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.match(McInstrParser.Search)
                self.state = 438
                self.match(McInstrParser.Shell)
                self.state = 439
                self.match(McInstrParser.StringLiteral)
                pass


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
        self._predicates[32] = self.simple_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def simple_expression_sempred(self, localctx:Simple_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




