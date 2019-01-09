Attribute VB_Name = "Check"

Option Explicit

Sub Check_Shift()
    Dim r As Integer
    Dim num As Integer
    Dim p As Integer
    p = 0

    For r = 33 To 36
        For num = 2 To 26
            If r = 33 Then
                If Sheets("Sheet1").Cells(num,r) > 15 Then 
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                Else
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                End If
            End If

            If r = 34 Then
                If Sheets("Sheet1").Cells(num,r) > 6 Then 
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                ElseIf Sheets("Sheet1").Cells(num,r) < 4 Then
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                Else
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                End If
            End If

            If r = 35 Then
                If Sheets("Sheet1").Cells(num,r) > 4 Then 
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                ElseIf Sheets("Sheet1").Cells(num,r) < 2 Then
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                Else
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                End If
            End If

            If r = 36 Then
                If Sheets("Sheet1").Cells(num,r) < 9 Then 
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 10
                Else
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                End If
            End If
        Next
    Next
    Sheets("Sheet1").Cells(28,1).Value = "Hard" 
    Sheets("Sheet1").Cells(29,1).Value = p
End Sub


Sub Check_A()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 1

    For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,2).Value = "A" 
    Sheets("Sheet1").Cells(29,2).Value = p

End Sub

Sub Check_A_SS()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 13

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,3).Value = "A_SS" 
    Sheets("Sheet1").Cells(29,3).Value = p


End Sub

Sub Check_B()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 25

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,4).Value = "B" 
    Sheets("Sheet1").Cells(29,4).Value = p


End Sub

Sub Check_B_SS()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 37

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,5).Value = "B_SS" 
    Sheets("Sheet1").Cells(29,5).Value = p


End Sub

Sub Check_B_SS_s()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 49

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,6).Value = "B_SS_s" 
    Sheets("Sheet1").Cells(29,6).Value = p


End Sub

Sub Check_B_rq_s()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 61

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,7).Value = "B_rq_s" 
    Sheets("Sheet1").Cells(29,7).Value = p


End Sub

Sub Check_o_n()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 73

     For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,8).Value = "o_n" 
    Sheets("Sheet1").Cells(29,8).Value = p


End Sub

Sub Check_Staff()

    Dim r As Integer
    Dim s As Integer
    Dim p As Integer
    p = 0
    s = 85

    For r = 2 To 31
        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 1,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 2,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 3,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 5,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 6,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 7,r).Interior.Color = RGB(0,250,0)
        End If

        If Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) > Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 8,r) Then 
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(250,0,0)
            p = p + 1
        ElseIf Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r) < Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 9,r) Then
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,0,250)
            p = p + 1
        Else
            Workbooks("penalty.xlsm").Sheets("sheet1").Cells(s + 10,r).Interior.Color = RGB(0,250,0)
        End If
    Next
    Sheets("Sheet1").Cells(28,9).Value = "All" 
    Sheets("Sheet1").Cells(29,9).Value = p

End Sub

Sub All_Check()

    Call Check_A
    Call Check_A_SS
    Call Check_B
    Call Check_B_SS
    Call Check_B_SS_s
    Call Check_B_rq_s
    Call Check_o_n
    Call Check_Staff
    Call Check_Shift


End Sub

Sub Calc_p()
    Dim sum As Integer
    Call All_Count
    Call All_Check

    sum = WorksheetFunction.Sum(Workbooks("penalty 20.xlsm").Sheets("sheet1").Range("A29:I29"))
    Sheets("Sheet1").Cells(28,10).Value = "Total" 
    Sheets("Sheet1").Cells(29,10).Value = sum
End Sub