Attribute VB_Name = "Count"

Option Explicit


Sub Count_A()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 2

    Dim l As Integer
    l = 14

    Dim r_num As Integer
    r_num = 1

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "A"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"


    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_A_SS()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 2

    Dim l As Integer
    l = 7

    Dim r_num As Integer
    r_num = 13

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "A_SS"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_B()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 15

    Dim l As Integer
    l = 26

    Dim r_num As Integer
    r_num = 25

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "B"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_B_SS()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 15

    Dim l As Integer
    l = 19

    Dim r_num As Integer
    r_num = 37

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "B_SS"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

   For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_B_SS_s()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 15

    Dim l As Integer
    l = 19

    Dim r_num As Integer
    r_num = 49

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "B_SS_s"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
    
        If Sheets("Sheet1").Cells(26,r).Value = 1 Then
            d = d + 1
        ElseIf Sheets("Sheet1").Cells(26,r).Value = 2 Then
            e = e + 1
        ElseIf Sheets("Sheet1").Cells(26,r).Value = 3 Then
            n = n + 1
        ElseIf Sheets("Sheet1").Cells(26,r).Value = 4 Then
            o = o + 1
        Else

        End If
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_B_rq_s()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 20

    Dim l As Integer
    l = 26

    Dim r_num As Integer
    r_num = 61

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "B_rq_s"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

Sub Count_o_n()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer
    Dim r_num As Integer
    r_num = 73

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "o_n"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"

    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        If Sheets("Sheet1").Cells(2,r).Value = 1 Then
            d = d + 1
        ElseIf Sheets("Sheet1").Cells(2,r).Value = 2 Then
            e = e + 1
        ElseIf Sheets("Sheet1").Cells(2,r).Value = 3 Then
            n = n + 1
        ElseIf Sheets("Sheet1").Cells(2,r).Value = 4 Then
            o = o + 1
        Else

        End If

        If Sheets("Sheet1").Cells(10,r).Value = 1 Then
            d = d + 1
        ElseIf Sheets("Sheet1").Cells(10,r).Value = 2 Then
            e = e + 1
        ElseIf Sheets("Sheet1").Cells(10,r).Value = 3 Then
            n = n + 1
        ElseIf Sheets("Sheet1").Cells(10,r).Value = 4 Then
            o = o + 1
        Else

        End If 
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
   
End Sub

sub Copy()
    Dim file_name As String
    file_name = "penalty.xlsm"
    ' A
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B2:AE3").copy Workbooks(file_name).Sheets("sheet1").Range("B2")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B4:AE5").copy Workbooks(file_name).Sheets("sheet1").Range("B6")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B6:AE7").copy Workbooks(file_name).Sheets("sheet1").Range("B9")
    ' A_SS
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B9:AE10").copy Workbooks(file_name).Sheets("sheet1").Range("B14")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B11:AE12").copy Workbooks(file_name).Sheets("sheet1").Range("B18")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B13:AE14").copy Workbooks(file_name).Sheets("sheet1").Range("B21")
    ' B
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B16:AE17").copy Workbooks(file_name).Sheets("sheet1").Range("B26")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B18:AE19").copy Workbooks(file_name).Sheets("sheet1").Range("B30")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B20:AE21").copy Workbooks(file_name).Sheets("sheet1").Range("B33")
    ' B_SS
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B23:AE24").copy Workbooks(file_name).Sheets("sheet1").Range("B38")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B25:AE26").copy Workbooks(file_name).Sheets("sheet1").Range("B42")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B27:AE28").copy Workbooks(file_name).Sheets("sheet1").Range("B45")
    ' B_SS_s
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B30:AE31").copy Workbooks(file_name).Sheets("sheet1").Range("B50")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B32:AE33").copy Workbooks(file_name).Sheets("sheet1").Range("B54")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B34:AE35").copy Workbooks(file_name).Sheets("sheet1").Range("B57")
    'B_rq_s
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B37:AE38").copy Workbooks(file_name).Sheets("sheet1").Range("B62")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B39:AE40").copy Workbooks(file_name).Sheets("sheet1").Range("B66")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B41:AE42").copy Workbooks(file_name).Sheets("sheet1").Range("B69")
    ' 1_9
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B44:AE45").copy Workbooks(file_name).Sheets("sheet1").Range("B74")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B46:AE47").copy Workbooks(file_name).Sheets("sheet1").Range("B78")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B48:AE49").copy Workbooks(file_name).Sheets("sheet1").Range("B81")
    ' All
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B51:AE52").copy Workbooks(file_name).Sheets("sheet1").Range("B86")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B53:AE54").copy Workbooks(file_name).Sheets("sheet1").Range("B90")
    Workbooks("error_list.xlsm").Sheets("Sheet1").Range("B55:AE56").copy Workbooks(file_name).Sheets("sheet1").Range("B93")
End Sub

Sub Count_Staff()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim o As Integer

    Dim start As Integer
    start = 2

    Dim l As Integer
    l = 26

    Dim r_num As Integer
    r_num = 85

    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  0,1).Value = "All"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  1,1).Value = "D_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  2,1).Value = "D_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  3,1).Value = "D_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  4,1).Value = "O_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  5,1).Value = "E_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  6,1).Value = "E_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  7,1).Value = "E_Prov"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  8,1).Value = "N_Max"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num +  9,1).Value = "N_Min"
    Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,1).Value = "N_Prov"


    For r = 8 To 37
        d = 0
        e = 0
        n = 0
        o = 0
        For num = start To l
           
            If Sheets("Sheet1").Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 3 Then
                n = n + 1
            ElseIf Sheets("Sheet1").Cells(num,r).Value = 4 Then
                o = o + 1
            Else

            End If
        Next
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 3,r).Value = d
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 4,r).Value = o
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 7,r).Value = e
        Workbooks("penalty.xlsm").Sheets("sheet1").Cells(r_num + 10,r).Value = n
    Next
End Sub

sub Shift_Count()
    Dim i As Integer
    Dim j As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer
    Dim f As Integer
    d = 0
    n = 0
    e = 0
    f = 0

    Cells(1,39).Value = "d"
    Cells(1,40).Value = "e"
    Cells(1,41).Value = "n"
    Cells(1,42).Value = "f"

    For i = 2 To 26
        For j = 2 To 31
            If Cells(i,j).Value = 1 Then
                d = d + 1
            ElseIf Cells(i,j).Value = 2 Then
                e = e + 1
            ElseIf Cells(i,j).Value = 3 Then
                n = n + 1
            ElseIf Cells(i,j).Value = 0 or Cells(i,j).Value = 5 Then
                f = f + 1
            Else
            End If
        Next

        Cells(i,39).Value = d
        Cells(i,40).Value = e
        Cells(i,41).Value = n
        Cells(i,42).Value = f
        d = 0
        n = 0
        e = 0
        f = 0
    Next

End sub

Sub All_Count()

    Workbooks("penalty.xlsm").Sheets("sheet1").Range("A1:AE93").Delete
    Workbooks(ActiveWorkbook.Name).Sheets("sheet1").Range("A28:J29").Delete
    Call Copy
    Call Count_A
    Call Count_A_SS
    Call Count_B
    Call Count_B_SS
    Call Count_B_SS_s
    Call Count_B_rq_s
    Call Count_o_n
    Call Count_Staff
    Call Shift_Count

End Sub