# property tax calculator 1
def part1():
    """Calculates the miscellaneous tax rate."""
    nheac = 0.004
    mwrdc = 0.406
    pmab = 0.006
    cpd = 0.362
    MiscTx = nheac + mwrdc + pmab + cpd
    return MiscTx

def part2():
    """Calculates the school tax rate."""
    bec = 3.726
    cccd = 0.169
    Schooltax = bec + cccd
    return Schooltax

def part3():
    """Calculates the city tax rate."""
    csbif = 0.128
    clf = 0.122
    city_base = 1.630
    City = csbif + clf + city_base
    return City

def part4():
    """Calculates the county tax rate."""
    ccfpd = 0.063
    cook = 0.316
    ccps = 0.130
    cchf = 0.087
    CookCty = ccfpd + cook + ccps + cchf
    return CookCty

def main():
    """Calculates and prints the total property tax rate."""
    print('----------------------------')
    mt = part1()
    st = part2()
    ct = part3()
    cc = part4()
    TotalTaxRate = mt + st + ct + cc
    print('Property Tax Rate is:', TotalTaxRate)

if __name__ == "__main__":
    main()
