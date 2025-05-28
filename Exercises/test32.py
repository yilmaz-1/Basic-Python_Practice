def faktoriyel(sayi):
    faktoriyell = 1
    if sayi == 0 or sayi == 1:
        print(f"fakötriyel = {faktoriyell}'dir")
    else:
        while sayi >= 1:
            faktoriyell *= sayi
            sayi -= 1
        print(f"faktöriyel = {faktoriyell}'dir")


faktoriyel(5)
# çıktı:
# faktöriyel = 120'dir
