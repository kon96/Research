Attribute VB_Name = "Count"

Option Explicit


Sub Count_A()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer

    Cells(28,1).Value = "A_d"
    Cells(29,1).Value = "A_e"
    Cells(30,1).Value = "A_n"

    For r = 2 To 31
        d = 0
        e = 0
        n = 0
        For num = 2 To 14
           
            If Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Cells(num,r).Value = 3 Then
                n = n + 1
            Else

            End If
        Next
        Cells(28,r).Value = d
        Cells(29,r).Value = e
        Cells(30,r).Value = n
    Next
End Sub

Sub Count_B()
    Dim num As Integer
    Dim r As Integer
    Dim d As Integer
    Dim e As Integer
    Dim n As Integer

    For r = 2 To 31
        d = 0
        e = 0
        n = 0
        For num = 15 To 
           
            If Cells(num,r).Value = 1 Then
                d = d + 1
            ElseIf Cells(num,r).Value = 2 Then
                e = e + 1
            ElseIf Cells(num,r).Value = 3 Then
                n = n + 1
            Else

            End If
        Next
        Cells(28,r).Value = d
        Cells(29,r).Value = e
        Cells(30,r).Value = n
    Next
End Sub