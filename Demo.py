# 56 STUDENTS RECORD HICAO
Student_arrName = [
    ["Abayog, Joanaa Mae P."],["Abique, Maurine R."],["Amarra, Eugene A."],["Andojar, Rizza Mae B."],["Angeles, Brian Steven V."],["Angeles, Princess Jane E."],
    ["Avila, Jhon Mark G."],["Bangcaray, Reniel C."],["Baxal, Rosmarie m."],["Busa, Tzeistel kienna C."],["Buzon, Rica L."],["Cabato, Jonathan R."],
    ["Camposano, James Calro P."],["Dacles, Zyrel C."],["Dela, Serna Lyka N."],["Delmonte, Rina Grace D."],["Desalin, Lhe Ann C."],["Dilao, Jully Mae Q."],
    ["Dingrat, Maria Teresa O."],["Doligon, Jhon Donard M."],["Doneza, Jillian L."],["Doron, curly Ann A."],["Geroy, Ariane Kate"],["Geroy, kent James C."],
    ["Goden, Randy Y."],["Gornes, Christian P."],["Gudes, Karen Joy S."],["Hicao, Allan Kris B."],["Jaromay, Marian Angelic J."],["Jaromay, Mary Angel J."],
    ["Ladic, Monique R."],["Lazzara, Mary Grace R."],["Legria, Kyla Shine P."],["Lobenia, Edje B."],["Lomuntad, Riza Mae R."],["Madrigal, Mark Dever T."],
    ["Mengullo, Jose O."],["Menguria, Ecy N."],["Montalla, Aldrich L."],["Morallos, Mariane Franzcess B."],["Morallos, Michael Jude B."],["Obiasca, Bon Ryan C."],
    ["Oblino, Daneil O."],["Orale, Kenneth T."],["Orbista, Xander B."],["Paano, Aljhon B."],["Patriarca, Denver B."],["Perona, Shena Mae A."],
    ["Picardal, Precious Ann A."],["Porton, Elmo C."],["Rivera, Jhon Denzel A."],["Rivera, Kim alexis N."],["Robredillo, April Mae A."],["Sederia, Ken Syrus L."],
    ["Tan, John Patrick A."],["Tegio, Mark Lester B."]
] # 2D ARRAY HAN MGA NAME

Student_arrID = [
    ["25-11652"],["25-11712"],["25-11677"],["25-11679"],["25-11661"],["25-11650"],["25-11657"],["25-11636"],["25-12275"],["25-11710"],["25-11707"],["25-12327"],
    ["25-11671"],["25-11693"],["25-11627"],["25-11888"],["25-12192"],["25-11670"],["25-12493"],["25-11715"],["25-11648"],["25-11816"],["25-11703"],["25-11668"],
    ["25-12334"],["25-12424"],["25-11758"],["25-12250"],["25-11697"],["25-11669"],["25-11760"],["25-12245"],["25-11877"],["25-12330"],["25-11643"],["25-11649"],
    ["25-11626"],["25-12243"],["25-12331"],["25-11646"],["25-12423"],["25-12568"],["25-12436"],["25-11714"],["25-11665"],["25-11691"],["25-11759"],["25-12537"],
    ["25-11706"],["25-11656"],["25-11692"],["25-11653"],["25-11717"],["25-12276"],["25-11642"],["25-06793"]
] # 2D ARRAY HAN ID

Student_arrGender = [
    ["F"],["F"],["M"],["F"],["M"],["F"],["M"],["M"],["F"],["F"],
    ["F"],["M"],["M"],["M"],["F"],["F"],["F"],["F"],["F"],["M"],
    ["F"],["F"],["F"],["M"],["M"],["M"],["F"],["M"],["F"],["F"],
    ["F"],["F"],["F"],["M"],["F"],["M"],["M"],["F"],["M"],["F"],
    ["M"],["M"],["M"],["M"],["M"],["M"],["M"],["F"],["F"],["M"],
    ["M"],["F"],["F"],["M"],["M"],["M"]
] # 2D ARRAY HAN GENDER

Program_End = True    # BOOLEAN NGA MAYDA VALUE NA TRUE PARA HAN PAG-GAMIT HAN WHILE LOOP

while Program_End :

    print("\n====================================")
    print("   STUDENT RECORD SYSTEM ( 1B )")
    print("======================================\n")

    print("\n1. Add Student")
    print("2. Find Student Info. Using ( ID NUMBER )")
    print("3. Display All Students Record")
    print("4. Exit\n")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1 :
            print("Your Choice Is Adding Student!")
            FullName = input("Enter Your Fullname: ")
            Student_arrName.append([FullName])

            Id = input("Enter ID Number: ")
            Student_arrID.append([Id])

            Sex = input("Enter Gender ( M/F ): ")
            Student_arrGender.append([Sex])

            print("Congrats Student Record Added successfully!")

        case 2 :
            print("Your Choice Is Find Student Record By Entering ( ID NUMBER )!")
            Number = input("Please Enter your ID NUMBER EX.( 25-00000 ): ")
            Boll = True

            for i in range(len(Student_arrID)):             # ROW
                for j in range(len(Student_arrID[i])):      # COLUMN
                    if Boll:
                        if Number == Student_arrID[i][j]:
                            print("STUDENT FOUNDED!")
                            print("STUDENT ID: ", Student_arrID[i][j], "   ", Student_arrGender[i][j], "     ",Student_arrName[i][j])
                    else:
                        print("NO STUDENTS RECORD BASED ON YOUR ID!")

        case 3 :
            print("Your Choice Is Display All Student Record In ( BSIT 1B )")
            print("BSIT 1B CLASS RECORDS\n")

            for row in range(len(Student_arrName)):
                for col in range(len(Student_arrName[row])):
                    print("STUDENT ID: ", Student_arrID[row][col], "   ",Student_arrGender[row][col], "     ", Student_arrName[row][col])

        case 4 :
            print("Program Finished!")
            Program_End = False

        case _:
            print("INVALID INPUT PLEASE SELECT ( 1-4 )!")
            print("PLEASE TRY AGAIN NA KUPAL KA!")

print("=================================")
print("   TANKS FOR YOU'RE PATIENT      ")
print("         GOOD BYE!               ")
print("=================================")