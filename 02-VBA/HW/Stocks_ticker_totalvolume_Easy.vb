Attribute VB_Name = "Module2"
Sub Stock_ticker_volume():
    
    Dim Total_Volume As Double
    Dim a, b As Integer
    Dim ws As Worksheet
    
    For Each ws In Worksheets
    
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Total Stock Volume"
    
    a = 2
    b = 2
    Total_Volume = ws.Cells(2, 7).Value
    
    Do While ws.Cells(a, 1).Value <> ""
        If ws.Cells(a, 1).Value = ws.Cells(a + 1, 1).Value Then
            Total_Volume = Total_Volume + ws.Cells(a + 1, 7).Value
        Else
            ws.Cells(b, 9).Value = ws.Cells(a, 1).Value
            ws.Cells(b, 10).Value = Total_Volume
            b = b + 1
            TotalVolume = ws.Cells(a + 1, 7).Value
        End If
        
        a = a + 1
        
    Loop
    
    Next ws
    
End Sub


