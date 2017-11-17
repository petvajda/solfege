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
""" + cmaj.vextab("bass", 7, 3) + """
text """ + cmaj.name + """
options space=20
""" + ddor.vextab("bass", 6, 3) + """
text """ + ddor.name + """
options space=20
""" + ephr.vextab("bass", 5, 3) + """
text """ + ephr.name + """
options space=20
""" + flyd.vextab("bass", 4, 3) + """
text """ + flyd.name + """
options space=20
""" + gmix.vextab("bass", 3, 3) + """
text """ + gmix.name + """
options space=20
""" + aaeo.vextab("bass", 2, 3) + """
text """ + aaeo.name + """
options space=20
""" + bloc.vextab("bass", 1, 3) + """
text """ + bloc.name + """
	</div>
  </body>
</html>
"""
test_file = open("test_c_modes.html",'w')
test_file.write(html)
test_file.close()
