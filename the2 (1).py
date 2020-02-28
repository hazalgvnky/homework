def isCovered(cp_bl, cp_tr, t1_bl, t1_tr, t2_bl, t2_tr):

   #alttan üstten birbirini tamamlayan
    if t1_bl[0] <= cp_bl[0] \
            and t1_bl[1] <= cp_bl[1]\
            and t1_tr[0] >= cp_tr[0] \
            and t1_tr[1] >= t2_bl[1] \
            and t2_tr[0] >= cp_tr[0] \
            and t2_bl[0] <= cp_bl[0] \
            and t2_tr[1] >= cp_tr[1] :
        return "COMPLETELY COVERED"
    if t2_bl[0] <= cp_bl[0] \
            and t2_bl[1] <= cp_bl[1] \
            and t2_tr[0] >= cp_tr[0] \
            and t2_tr[1] >= t1_bl[1] \
            and t1_bl[0] <= cp_bl[0] \
            and t1_tr[0] >= cp_tr[0] \
            and t1_tr[1] >= cp_tr[1] :
        return "COMPLETELY COVERED"

    #yan yana birbirini tamamlayanlar
    if t1_bl[0] <= cp_bl[0] \
            and t1_bl[1] <= cp_bl[1] \
            and not t2_tr[0] <= cp_tr[0] \
            and t2_tr[0] >= cp_tr[0] \
            and t2_tr[1] >= cp_tr[1] \
            and t1_tr[0] >= t2_bl[0] \
            and t1_tr[1] >= cp_tr[1] \
            and t2_bl[1] <= cp_bl[1] :
        return "COMPLETELY COVERED"
    if t2_bl[0] <= cp_bl[0] \
            and t2_bl[1] <= cp_bl[1] \
            and t1_tr[0] >= cp_tr[0] \
            and not t1_tr[0] <= cp_tr[0] \
            and t1_tr[1] >= cp_tr[1] \
            and t2_tr[0] >= t1_bl[0] \
            and t2_tr[1] >= cp_tr[1] \
            and t1_bl[1] <= cp_bl[1] :
        return "COMPLETELY COVERED"

    #birinci kaplarsa sedece
    if t1_bl[0] <= cp_bl[0] \
            and t1_bl[1] <= cp_bl[1] \
            and t1_tr[0] >= cp_tr[0] \
            and t1_tr[1] >= cp_tr[1] :
        return "COMPLETELY COVERED"

    #ikinci kaplarsa
    if t2_bl[0] <= cp_bl[0] \
            and t2_bl[1] <= cp_bl[1] \
            and t2_tr[0] >= cp_tr[0] \
            and t2_tr[1] >= cp_tr[1] :
        return "COMPLETELY COVERED"

    else:
        return "NOT COMPLETELY COVERED"



