fam = ["Mike", 1.70, "Dayo", 1.80, "Tomiwa", 1.50] #These lists are numbered automatically. In this case from 0 to 5"
fam1 = [["Mike", 1.70], ["Dayo", 1.80], ["Tomiwa", 1.50]]
fam2 = fam1
fam [3]
fam [-4]
fam [2:5] #This is a slicer but it leaves the last number out"
fam [:3] #Also a slicer from the begining to the fourth term"
fam [3:] #Another slicer from the fourth term to the last term"
fam [2] = 1.75 #changimg Mike's age in the fam list"
fam
fam + ["me", 2.90] #adds this list to the fam list "
del(fam[2]) # this deletes the string Dayo from our list "
tallest = max (fam)
