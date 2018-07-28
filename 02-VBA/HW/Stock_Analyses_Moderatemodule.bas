Sub Stock_Analyses():

    Dim TotalVolume As Double
    Dim i, j As Integer
    Dim Op, Cs As Double
    Dim ws As Worksheet
    
    For Each ws In Worksheets
    
    
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"
    
    i = 2
    j = 2
    Op = Cells(2, 3).Value
    Cs = 0
    TotalVolume = Cells(2, 7).Value
    
    Range("A1").Interior.Color = RGB(50, 200, 100)
    
    Do While Cells(i, 1).Value <> ""
        If Cells(i, 1).Value = Cells(i + 1, 1).Value Then
            TotalVolume = TotalVolume + Cells(i + 1, 7).Value
        Else
            Cells(j, 9).Value = Cells(i, 1).Value
            
            Cs = Cells(i, 6).Value
            Cells(j, 10).Value = Cs - Op
            If Cs - Op < 0 Then
                Cells(j, 10).Interior.ColorIndex = 3
            Else
                Cells(j, 10).Interior.ColorIndex = 4
            End If
            
            
            Cells(j, 11).Value = (Cs - Op) / Op
            Cells(j, 11).NumberFormat = "0.00%"
            
            Op = Cells(i + 1, 3).Value
            
            
            
            Cells(j, 12).Value = TotalVolume
            j = j + 1
            TotalVolume = Cells(i + 1, 7).Value
        End If
        
        i = i + 1
    Loop
    
    Next ws
    
End Sub

