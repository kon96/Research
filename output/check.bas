Attribute VB_Name = "Check"

Option Explicit

Sub Check_Shift()
    Dim r As Integer
    Dim num As Integer
    Dim p As Integer
    Dim g1 As Variant
    Dim g2 As Variant
    Dim i As Variant
    Dim j As Variant
    g1 = Array(2,8,9,10,11,12,14,21,22,23,23,25)
    g2 = Array(3,4,5,6,7,15,16,17,18,19,26)

    p = 0

    For r = 33 To 36
        For num = 2 To 26
            i = Application.Match(num,g1,0)
            j = Application.Match(num,g2,0)
            If Not IsError(i) Then
                If r = 33 Then
                    If Sheets("Sheet1").Cells(num,r) > 15 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 34 Then
                    If Sheets("Sheet1").Cells(num,r) > 6 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    ElseIf Sheets("Sheet1").Cells(num,r) < 4 Then
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 35 Then
                    If Sheets("Sheet1").Cells(num,r) > 4 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    ElseIf Sheets("Sheet1").Cells(num,r) < 2 Then
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If
            ElseIf Not IsError(j) Then
                If r = 33 Then
                    If Sheets("Sheet1").Cells(num,r) > 14 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 34 Then
                    If Sheets("Sheet1").Cells(num,r) > 6 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    ElseIf Sheets("Sheet1").Cells(num,r) < 4 Then
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 35 Then
                    If Sheets("Sheet1").Cells(num,r) > 6 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    ElseIf Sheets("Sheet1").Cells(num,r) < 3 Then
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If
            ElseIf num = 14 Then
                If r = 33 Then
                    If Sheets("Sheet1").Cells(num,r) > 17 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 34 Then
                    If Sheets("Sheet1").Cells(num,r) <> 2 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 35 Then
                    If Sheets("Sheet1").Cells(num,r) <> 2 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If
            ElseIf num = 20 Then
                If r = 33 Then
                    If Sheets("Sheet1").Cells(num,r) > 17 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 34 Then
                    If Sheets("Sheet1").Cells(num,r) > 4 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    ElseIf Sheets("Sheet1").Cells(num,r) < 2 Then
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If

                If r = 35 Then
                    If Sheets("Sheet1").Cells(num,r) <> 4 Then 
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                        p = p + 1
                    Else
                        Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(0,250,0)
                    End If
                End If
            Else
            
            End If

            If r = 36 Then
                If Sheets("Sheet1").Cells(num,r) < 9 Then 
                    Sheets("Sheet1").Cells(num,r).Interior.Color = RGB(250,0,0)
                    p = p + 1
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
    Call Check_Hard


End Sub

Sub Check_Hard()
    Dim i As Integer
    Dim j As Integer
    Dim k As Integer
    Dim count As Integer

    Dim p1 As Integer
    Dim p2 As Integer
    Dim p3 As Integer
    Dim p4 As Integer
    Dim p5 As Integer
    Dim p6 As Integer
    Dim p7 As Integer
    Dim p8 As Integer
    Dim p9 As Integer
    Dim p10 As Integer
    Dim p11 As Integer
    Dim p12 As Integer
    Dim p13 As Integer
    Dim p14 As Integer
    Dim p15 As Integer
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p7 = 0
    p8 = 0
    p9 = 0
    p10 = 0
    p11 = 0
    p12 = 0
    p13 = 0
    p14 = 0
    p15 = 0
    
    For i = 2 To 26
        For j = 2 To 31
            Cells(i,j).Interior.Color = Cells(i,1).Interior.Color
            If Cells(i,j).Value = 0 or Cells(i,j).Value = 5 Then
                p2 = 0
                p3 = p3 + 1
                p6 = 0
                p7 = 0
                p8 = 0

                If p1 = 0 Then 
                    p1 = p1 + 1
                ElseIf p1 = 1 Then
                    p1 = 0
                ElseIf p1 = 2 Then
                    Cells(i,j).Interior.Color = RGB(250,0,0)
                    Cells(i,j - 1).Interior.Color = RGB(250,0,0)
                    Cells(i,j - 2).Interior.Color = RGB(250,0,0)
                    p1 = 0
                    count = count + 1
                End If

                If p3 = 5 Then
                    For k = (j - p3 + 1) To j
                        Cells(i,k).Interior.Color = RGB(0,250,0)
                    Next
                    p3 = 0
                    count = count + 1
                End If

                If p4 >= 1 Then
                    p4 = p4 + 1
                End If

                If p5 > 0 Then
                    p5 = p5 + 1
                End If

                If p14 = 1 Then
                    p14 = p14 + 1
                End If

                If p15 = 1 Then
                    p15 = p15 + 1
                End If

            ElseIf Cells(i,j).Value = 1 Then
                p2 = p2 + 1
                p3 = 0
                p6 = 0
                p7 = p7 + 1
                p8 = 0

                If p1 = 1 Then
                    p1 = p1 + 1
                End If
                
                If p4 = 0 Then
                    p4 = p4 + 1
                ElseIf p4 > 1 Then
                    p4 = 1
                End If

                If p5 > 0 Then
                    p5 = p5 + 1
                End If

                If p7 = 5 Then
                    For k = (j - p7 + 1) To j
                        Cells(i,k).Interior.Color = RGB(0,0,250)
                    Next
                    p7 = 0
                    count = count + 1
                End If

                If p9 = 1 Then
                    Cells(i,j).Interior.Color = RGB(255,255,0)
                    Cells(i,j - 1).Interior.Color = RGB(255,255,0)
                    p9 = 0
                    count = count + 1
                End If

                If p12 = 1 Then
                    Cells(i,j).Interior.Color = RGB(124,83,53)
                    Cells(i,j -1).Interior.Color = RGB(124,83,53)
                    p12 = 0
                    count = count + 1
                End If

                If p14 = 2 Then
                    Cells(i,j).Interior.Color = RGB(255,129,25)
                    Cells(i,j - 1).Interior.Color = RGB(255,129,25)
                    Cells(i,j - 2).Interior.Color = RGB(255,129,25)
                    p14 = 0
                    count = count + 1
                End If
            ElseIf Cells(i,j).Value = 2 Then
                p2 = p2 + 1
                p3 = 0
                p6 = 0
                p7 = 0
                p8 = p8 + 1
                p12 = p12 + 1
                p13 = p13 + 1

                If p1 = 1 Then
                    p1 = p1 + 1
                End If

                If p4 >= 1 Then
                    p4 = p4 + 1
                End If

                If p5 > 0 Then
                    p5 = p5 + 1
                End If

                If p8 = 4 Then
                    Cells(i,j).Interior.Color = RGB(71,234,126)
                    Cells(i,j - 1).Interior.Color = RGB(71,234,126)
                    Cells(i,j - 2).Interior.Color = RGB(71,234,126)
                    Cells(i,j - 3).Interior.Color = RGB(71,234,126)
                    p8 = 0
                    count = count + 1
                End If

                If p11 = 1 Then
                    Cells(i,j).Interior.Color = RGB(50,204,18)
                    Cells(i,j -1).Interior.Color = RGB(50,204,18)
                    p11 = 0
                    count = count + 1
                End If
            ElseIf Cells(i,j).Value = 3 Then
                p2 = p2 + 1
                p3 = 0
                p6 = p6 + 1
                p7 = 0
                p8 = 0
                p9 = p9 + 1
                p10 = p10 + 1
                p11 = p11 + 1

                If p1 = 1 Then
                    p1 = p1 + 1
                End If

                If p4 >= 1 Then
                    p4 = p4 + 1
                End If

                If p6 = 3 Then
                    For k = (j - p6 + 1) To j
                        Cells(i,k).Interior.Color = RGB(151,128,131)
                    Next
                    p6 = 0
                    count = count + 1  
                End If

                If p5 > 2 and p5 < 7 Then
                    For k = (j - p5) To j
                        Cells(i,k).Interior.Color = RGB(255,0,119)
                    Next
                    p5 = 0
                    count = count + 1 
                ElseIf p5 = 0 Then
                    p5 = p5 + 1
                ElseIf p5 = 1 Then
                    p5 = 1
                End If

                If p14 = 0 Then
                    p14 = p14 + 1
                End If

                If p15 = 0 Then
                    p15 = p15 + 1
                End If

            ElseIf Cells(i,j).Value = 4 Then
                p2 = p2 + 1
                p3 = 0
                p6 = 0
                p7 = 0
                p8 = 0

                If p1 = 1 Then
                    p1 = p1 + 1
                End If

                If p4 >= 1 Then
                    p4 = p4 + 1
                End If

                If p5 > 0 Then
                    p5 = p5 + 1
                End If

                If p10 = 1 Then
                    Cells(i,j).Interior.Color = RGB(209,232,41)
                    Cells(i,j - 1).Interior.Color = RGB(209,232,41)
                    p10 = 0
                    count = count + 1
                End If
                    
                If p13 = 1 Then
                    Cells(i,j).Interior.Color = RGB(57,3,124)
                    Cells(i,j - 1).Interior.Color = RGB(57,3,124)
                    p13 = 0
                    count = count + 1
                End If

                If p15 = 2 Then
                    Cells(i,j).Interior.Color = RGB(226,159,167)
                    Cells(i,j -1).Interior.Color = RGB(226,159,167)
                    Cells(i,j -2).Interior.Color = RGB(226,159,167)
                    p15 = 0
                    count = count + 1
                End If

            Else
            End If

            If p1 = 2 Then
                p1 = 0
            End If

            If p2 = 7 Then
                For k = (j - p2 + 1) To j
                    Cells(i,k).Interior.Color = RGB(142,0,204)
                Next
                p2 = 0
                count = count + 1
            End If

            If p4 = 8 Then
                For k = (j - p4 + 1) To j
                    Cells(i,k).Interior.Color = RGB(229,0,18)
                Next
                p4 = 0
                count = count + 1
            End If

            If p9 = 1 Then
                p9 = 0
            End If

            If p10 = 1 Then
                p10 = 0
            End If

            If p11 = 1 Then
                p11 = 0
            End If

            If p12 = 1 Then
                p12 = 0
            End If

            If p13 = 1 Then
                p13 = 0
            End If

            If p14 = 2 Then
                p14 = 0
            End If

            If p15 = 2 Then
                p15 = 0
            End If
        Next
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        p6 = 0
        p7 = 0
        p8 = 0
        p9 = 0
        p10 = 0
        p11 = 0
        p12 = 0
        p13 = 0
        p14 = 0
        p15 = 0
    Next

    Sheets("Sheet1").Cells(29,1).Value =  Sheets("Sheet1").Cells(29,1).Value + count

End Sub

Sub Calc_p()
    Dim sum As Integer
    Call All_Count
    Call All_Check

    sum = WorksheetFunction.Sum(Workbooks(ActiveWorkbook.Name).Sheets("sheet1").Range("A29:I29"))
    Sheets("Sheet1").Cells(28,10).Value = "Total" 
    Sheets("Sheet1").Cells(29,10).Value = sum
End Sub