from solfege import Scale
cmaj=Scale("C")
html="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Scale</title>
    <link rel="stylesheet" href="http://www.vexflow.com/releases/vextab.css">
    <script src="http://www.vexflow.com/releases/vextab-div.js"></script>
  </head>
  <body>
	<div class="vex-tabdiv"
    width=680 scale=1.0 editor="true"
    editor_width=680 editor_height=330>""" + cmaj.vextab() + """
	</div>
  </body>
</html>
"""
test_file = open("test.html",'w')
test_file.write(html)
test_file.close()