def sqInRect(lng, wdth):
    area=1
    answer=[]
    if lng != wdth:
        while area!=0:
            short = min(lng,wdth)
            long = max(lng,wdth)
            area = lng*wdth
            lng = long-short
            wdth = short
            area = area - (lng*wdth)
            if wdth>0:
                answer.append(wdth)
        return(answer)
    else: return (None)

sqInRect(37,14)