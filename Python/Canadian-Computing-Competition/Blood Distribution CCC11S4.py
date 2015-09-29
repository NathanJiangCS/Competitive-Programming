blood = map(int,raw_input().split())
bloodneed = map(int,raw_input().split())
number = 0

if blood[0] >= bloodneed[0]: #O negative
    number += bloodneed[0]
    blood[0] = (blood[0] - bloodneed[0])
    bloodneed[0] = 0
else:
    number += blood[0]
    bloodneed[0] = (bloodneed[0] - blood[0])
    blood[0] = 0

if blood[2] >= bloodneed[2]: #A negative
    number += bloodneed[2]
    blood[2] = (blood[2] - bloodneed[2])
    bloodneed[2] = 0
else:
    number += blood[2]
    bloodneed[2] = (bloodneed[2] - blood[2])
    blood[2] = 0
    if blood[0] >= bloodneed[2]: 
        number += bloodneed[2]
        blood[0] = (blood[0] - bloodneed[2])
        bloodneed[2] = 0
    else:
        number += blood[0]
        bloodneed[2] = (bloodneed[2] - blood[0])
        blood[0] = 0

if blood[4] >= bloodneed[4]: #B negative
    number += bloodneed[4]
    blood[4] = (blood[4] - bloodneed[4])
    bloodneed[4] = 0
else:
    number += blood[4]
    bloodneed[4] = (bloodneed[4] - blood[4])
    blood[4] = 0
    if blood[0] >= bloodneed[4]: 
        number += bloodneed[4]
        blood[0] = (blood[0] - bloodneed[4])
        bloodneed[4] = 0
    else:
        number += blood[0]
        bloodneed[4] = (bloodneed[4] - blood[0])
        blood[0] = 0

if blood[6] >= bloodneed[6]: #Type AB negative
    number += bloodneed[6]
    blood[6] = (blood[6] - bloodneed[6])
    bloodneed[6] = 0
else:
    number += blood[6]
    bloodneed[6] = (bloodneed[6] - blood[6])
    blood[6] = 0
    
    if blood[0] >= bloodneed[6]: #O negative
        number += bloodneed[6]
        blood[0] = (blood[0] - bloodneed[6])
        bloodneed[6] = 0
    else:
        number += blood[0]
        bloodneed[6] = (bloodneed[6] - blood[0])
        blood[0] = 0

    if blood[2] >= bloodneed[6]: #A negative
        number += bloodneed[6]
        blood[2] = (blood[2] - bloodneed[6])
        bloodneed[6] = 0
    else:
        number += blood[2]
        bloodneed[6] = (bloodneed[6] - blood[2])
        blood[2] = 0

    if blood[4] >= bloodneed[6]: #B negative
        number += bloodneed[6]
        blood[4] = (blood[4] - bloodneed[6])
        bloodneed[6] = 0
    else:
        number += blood[4]
        bloodneed[6] = (bloodneed[6] - blood[4])
        blood[4] = 0

############################################################################

        
if blood[1] >= bloodneed[1]: #O positive
    number += bloodneed[1]
    blood[1] = (blood[1] - bloodneed[1])
    bloodneed[1] = 0
else:
    number += blood[1]
    bloodneed[1] = (bloodneed[1] - blood[1])
    blood[1] = 0

    if blood[0] >= bloodneed[1]:
        number += bloodneed[1]
        blood[0] = (blood[0] - bloodneed[1])
        bloodneed[1] = 0
    else:
        number += blood[0]
        bloodneed[1] = (bloodneed[1] - blood[0])
        blood[0] = 0

if blood[3] >= bloodneed[3]: #A positive
    number += bloodneed[3]
    blood[3] = (blood[3] - bloodneed[3])
    bloodneed[3] = 0
else:
    number += blood[3]
    bloodneed[3] = (bloodneed[3] - blood[3])
    blood[3] = 0

    if blood[0] >= bloodneed[3]: #O negative
        number += bloodneed[3]
        blood[0] = (blood[0] - bloodneed[3])
        bloodneed[3] = 0
    else:
        number += blood[0]
        bloodneed[3] = bloodneed[3] - blood[0]
        blood[0] = 0

    if blood[1] >= bloodneed[3]: #O Positive
        number += bloodneed[3]
        blood[1] = (blood[1] - bloodneed[3])
        bloodneed[3] = 0
    else:
        number += blood[1]
        bloodneed[3] = bloodneed[3] - blood[1]
        blood[1] = 0

    if blood[2] >= bloodneed[3]: #A negative
        number += bloodneed[3]
        blood[2] = (blood[2] - bloodneed[3])
        bloodneed[3] = 0
    else:
        number += blood[2]
        bloodneed[3] = bloodneed[3] - blood[2]
        blood[2] = 0
        
if blood[5] >= bloodneed[5]: #B positive
    number += bloodneed[5]
    blood[5] = (blood[5] - bloodneed[5])
    bloodneed[5] = 0
else:
    number += blood[5]
    bloodneed[5] = (bloodneed[5] - blood[5])
    blood[5] = 0

    if blood[0] >= bloodneed[5]: #O negative
        number += bloodneed[5]
        blood[0] = (blood[0] - bloodneed[5])
        bloodneed[5] = 0
    else:
        number += blood[0]
        bloodneed[5] = bloodneed[5] - blood[0]
        blood[0] = 0

    if blood[1] >= bloodneed[5]: #O Positive
        number += bloodneed[5]
        blood[1] = (blood[1] - bloodneed[5])
        bloodneed[5] = 0
    else:
        number += blood[1]
        bloodneed[5] = bloodneed[5] - blood[1]
        blood[1] = 0

    if blood[4] >= bloodneed[5]: #B negative
        number += bloodneed[5]
        blood[4] = (blood[4] - bloodneed[5])
        bloodneed[5] = 0
    else:
        number += blood[4]
        bloodneed[5] = bloodneed[5] - blood[2]
        blood[4] = 0

if blood[7] >= bloodneed[7]: #AB Positive
    number += bloodneed[7]
    blood[7] -= bloodneed[7]
    bloodneed[7] = 0
else:
    number += blood[7]
    bloodneed[7] -= blood[7]
    blood[7] = 0

    if blood[0] >= bloodneed[7]:
        number += bloodneed[7]
        blood[0] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[0]
        bloodneed[7] -= blood[0]
        blood[0] = 0
#####
    if blood[1] >= bloodneed[7]:
        number += bloodneed[7]
        blood[1] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[1]
        bloodneed[7] -= blood[1]
        blood[1] = 0
#####
    if blood[2] >= bloodneed[7]:
        number += bloodneed[7]
        blood[2] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[2]
        bloodneed[7] -= blood[2]
        blood[2] = 0

    if blood[3] >= bloodneed[7]:
        number += bloodneed[7]
        blood[3] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[3]
        bloodneed[7] -= blood[3]
        blood[3] = 0

    if blood[4] >= bloodneed[7]:
        number += bloodneed[7]
        blood[4] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[4]
        bloodneed[7] -= blood[4]
        blood[4] = 0

    if blood[5] >= bloodneed[7]:
        number += bloodneed[7]
        blood[5] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[5]
        bloodneed[7] -= blood[5]
        blood[5] = 0

    if blood[6] >= bloodneed[7]:
        number += bloodneed[7]
        blood[6] -= bloodneed[7]
        bloodneed[7] = 0
    else:
        number += blood[6]
        bloodneed[7] -= blood[6]
        blood[6] = 0

print number
