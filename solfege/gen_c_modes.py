from solfege import Scale
cmaj=Scale("C")
ddor=Scale("D", 2)
ephr=Scale("E", 3)
flyd=Scale("F", 4)
gmix=Scale("G", 5)
aaeo=Scale("A", 6)
bloc=Scale("B", 7)
html="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>C Major Scale Modes</title>
    <link rel="stylesheet" href="http://www.vexflow.com/releases/vextab.css">
    <script src="http://www.vexflow.com/releases/vextab-div.js"></script>
  </head>
  <body>
	<div class="vex-tabdiv"
    width=680 scale=1.0 editor="true"
    editor_width=680 editor_height=330>options space=10
""" + cmaj.vextab(7) + """
text """ + cmaj.name + """
options space=20
""" + ddor.vextab(6) + """
text """ + ddor.name + """
options space=20
""" + ephr.vextab(5) + """
text """ + ephr.name + """
options space=20
""" + flyd.vextab(4) + """
text """ + flyd.name + """
options space=20
""" + gmix.vextab(3) + """
text """ + gmix.name + """
options space=20
""" + aaeo.vextab(2) + """
text """ + aaeo.name + """
options space=20
""" + bloc.vextab(1) + """
text """ + bloc.name + """
	</div>
  </body>
</html>
"""
test_file = open("test_c_modes.html",'w')
test_file.write(html)
test_file.close()
