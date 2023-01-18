Function Generate-DummyPPT {
    Add-Type -AssemblyName Microsoft.Office.Interop.PowerPoint
    $ppt = New-Object -ComObject PowerPoint.Application
    $ppt.Visible = $True
    $presentation = $ppt.Presentations.Add()
    $slide = $presentation.Slides.Add(1, [Microsoft.Office.Interop.PowerPoint.PpSlideLayout]::ppLayoutTitle)
    $shape = $slide.Shapes.AddTextbox(1, 50, 100, 100)
    $textRange = $shape.TextFrame.TextRange
    $textRange.Text = "Filler text"
    $textRange.Font.Size = 20
    $textRange.Font.Color.RGB = [System.Drawing.Color]::DarkBlue.ToArgb()
    $presentation.SaveAs("dummy.ppt")
    $ppt.Quit()
}
