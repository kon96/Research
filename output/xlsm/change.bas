Attribute VB_Name = "Chenge"

Public flg As Integer
Public n1 As Integer, n2 As Integer, b1 As Integer, b2 As Integer

Option Explicit

Sub Worksheet_BeforeDoubleClick(ByVal Target As Range, Cancel As Boolean)
'左ダブルクリックで交換対象指定
'
ActiveCell.Select
If flg = 1 Then GoTo lblKOKAN        '２回目のクリックで交換作業に跳ぶ

b1 = ActiveCell.Address          '最初のセル位置　記憶
n1 = ActiveCell.Value            ' 内容　　記憶

flg = 1                              '１回目通過したFLAG

GoTo lblMOTO　　　　　　'１回目は覚えるだけなので、交換作業をSKIP

lblKOKAN:                            '２回目のクリックで交換開始
b2 = ActiveCell.Address
n2 = ActiveCell.Value
ActiveCell = n1

Range(b1).Select              'セルのデータを最初の場所に移動させる
ActiveCell = n2

flg = 0                            'FLAGの初期化

lblMOTO:

End Sub
