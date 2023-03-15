def cc(amINR,curr):
    if curr=="Euro":
        print(amINR*0.01417)
    elif curr =="BP":
        print(amINR*0.0100)
    elif curr=="AD":
        print(amINR*0.02140)
    elif curr=="CD":
        print(amINR*0.02027)
    else:
        print("-1")
cc(300,"Euro")
cc(300,"BP")
cc(300,"AD")
cc(300,"CD")
