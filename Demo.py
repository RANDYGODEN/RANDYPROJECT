print("====================================")
print("   STUDENT RECORD SYSTEM ( 1B )"     )
print("====================================\n")

Student_arrID = [
    [25-11652],[25-11712],[25-11677],[25-11679],[25-11661],[25-11650],[25-11657],[25-11636],[25-12275],[25-11710],[25-11707],[25-12327],[25-11671],[25-11693],
    [25-11627],[25-11888],[25-12192],[25-11670],[25-12493],[25-11715],[25-11648],[25-11816],[25-11703],[25-11668],[25-12334],[25-12424],[25-11758],[25-12250],

]

# 27 STUDENTS RECORD
Student_arrName = [
    ["Abayog, Joanaa Mae P."],["Abique, Maurine R."],["Amarra, Eugene A."],["Andojar, Rizza Mae B."],["Angeles, Brian Steven V."],["Angeles, Princess Jane E."],
    ["Avila, Jhon Mark G."],["Bangcaray, Reniel C."],["Baxal, Rosmarie m."],["Busa, Tzeistel kienna C."],["Buzon, Rica L."],["Cabato, Jonathan R."],
    ["Camposano, James Calro P."],["Dacles, Zyrel C."],["Dela, Serna Lyka N."],["Delmonte, Rina Grace D."],["Desalin, Lhe Ann C."],["Dilao, Jully Mae Q."],
    ["Dingrat, Maria Teresa O."],["Doligon, Jhon Donard M."],["Doneza, Jillian L."],["Doron, curly Ann A."],["Geroy, Ariane Kate"],["Geroy, kent James C."],
    ["Goden, Randy Y."],["Gornes, Christian P."],["Gudes, Karen Joy S."],["Hicao, Allan Kris B."]
]

Program_End = True

while Program_End :
    print("\n1. Add Student")
    print("2. Find Student Info. Using ( ID NUMBER )")
    print("3. Display All Students Record")
    print("4. Exit\n")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1 :
            print("Your Choice Is Adding Student!")
            FullName = input("Enter Your Fullname: ")
            Id = input("Enter ID Number: ")
            Student_arrName.append([FullName, Id])
            print("Student Added Successfully!")

        case 2 :
            print("Your Choice Is Find Student Record By Entering ( ID NUMBER )!")

        case 3 :
            print("Your Is Display All Student Record In ( BSIT 1B )")

        case 4 :
            print("Program Finished!")
            Program_End = False

        case _:
            print("INVALID INPUT PLEASE SELECT ( 1-4 )!")
            print("PLEASE TRY AGAIN NA KUPAL KA!")