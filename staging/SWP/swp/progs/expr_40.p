OBJECT tree L_SYSTEM:
    ROOT G
    structure Stk = struct :
        exception EmptyStack_exception
        datatype 'x stack = EmptyStack | push of ('x * 'x stack)
        shape square:
            repeat 4:
                forward 10
                rotate 90
            end
        end
    end
    RULES:
        G -> T { A G } { C G } (0.70 .. 0.80)
        G -> T { A G } { B G } (0.80 .. 0.95)
        G -> T { A G } (0.95 .. 1.00)
    ENDRULES
ENDOBJECT

if (__name__ == "__main__"):
    import sys
    assign lexonly False
    assign trace False
    for fields in using query:
        SELECT fname, lname, t.phone, tsite.name :
            FROM tcontact, tsite
            WHERE table_contact.objid = "CONTID"
            AND table_site.objid = "SITEID"
        ENDSELECT
    endfor
    if sys.argv[1]:
        assign source open(sys.argv[1]).read()
    else:
        assign source "junk"
    end
end
