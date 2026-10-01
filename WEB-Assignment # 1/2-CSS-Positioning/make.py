import os
files = {
"01-static": {
"html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Static Positioning</title><link rel="stylesheet" href="style.css"></head>
<body><h2>1. Static (Default)</h2><p>Normal document flow. top/left/right/bottom does not work.</p><div class="parent"><div class="box">Box 1</div><div class="box static">Box 2 Static - top:50px will NOT work</div><div class="box">Box 3</div></div></body></html>""",
"css": """body{font-family:Arial;}.parent{background:#f0f0f0;padding:20px;border:2px solid #333;}.box{background:#87ceeb;padding:20px;margin:10px;border:2px solid blue;}.static{position:static; top:50px; left:50px; background:#ffcccc;}"""
},
"02-relative": {
"html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Relative</title><link rel="stylesheet" href="style.css"></head>
<body><h2>2. Relative Positioning</h2><p>Moves from its original position. Original space remains reserved.</p><div class="parent"><div class="box">Box 1</div><div class="box relative">Box 2 Relative (top:20px; left:30px)</div><div class="box">Box 3 - Space is still reserved for Box 2</div></div></body></html>""",
"css": """body{font-family:Arial;}.parent{background:#f0f0f0;padding:20px;border:2px solid #333;}.box{background:#87ceeb;padding:20px;margin:10px;border:2px solid blue;}.relative{position:relative; top:20px; left:30px; background:orange;}"""
},
"03-absolute": {
"html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Absolute</title><link rel="stylesheet" href="style.css"></head>
<body><h2>3. Absolute Positioning</h2><p>Removed from document flow. Positioned relative to closest positioned ancestor.</p><div class="parent"><div class="box">Box 1</div><div class="box absolute">Absolute - top:0 right:0</div><p>Parent is position:relative so absolute box is inside it.</p></div></body></html>""",
"css": """body{font-family:Arial;}.parent{position:relative; background:#f0f0f0;padding:20px;border:2px solid #333;height:200px;}.box{background:#87ceeb;padding:20px;margin:10px;border:2px solid blue;}.absolute{position:absolute; top:0; right:0; background:orange;}"""
},
"04-fixed": {
"html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Fixed</title><link rel="stylesheet" href="style.css"></head>
<body><h2>4. Fixed Positioning</h2><p>Fixed relative to viewport. Stays same on scroll.</p><div class="fixed-nav">This is Fixed Navbar - top:0 width:100%</div><div style="height:1000px; background:linear-gradient(white,gray); padding-top:80px;"><p>Scroll down - navbar will stay fixed.</p><div class="box">Content Box</div></div></body></html>""",
"css": """body{font-family:Arial;margin:0;}.fixed-nav{position:fixed; top:0; left:0; width:100%; background:#333; color:white; padding:15px; text-align:center; z-index:1000;}.box{background:#87ceeb;padding:20px;margin:100px;border:2px solid blue;}"""
},
"05-sticky": {
"html": """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Sticky</title><link rel="stylesheet" href="style.css"></head>
<body><h2>5. Sticky Positioning</h2><p>Mix of relative and fixed. Becomes fixed when scrolling reaches top:0</p><div class="content"><p>Scroll down to see sticky effect</p><div class="sticky-header">I am Sticky Header - I will stick at top:0</div><div style="height:800px;"><p>Long content...</p><p>Long content...</p><p>Long content...</p><p>Keep scrolling...</p></div></div></body></html>""",
"css": """body{font-family:Arial;}.content{background:#f0f0f0;padding:20px;border:2px solid #333;}.sticky-header{position:sticky; top:0; background:orange; padding:15px; border:2px solid red; font-weight:bold;}"""
}
}
for f in files:
    os.makedirs(f, exist_ok=True)
    open(f"{f}/index.html","w",encoding="utf-8").write(files[f]["html"])
    open(f"{f}/style.css","w",encoding="utf-8").write(files[f]["css"])
print("Q2 - 5 Positioning folders done!")