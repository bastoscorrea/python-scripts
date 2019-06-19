search_string = 'BRAZIL'
with open('TestPython.m3u', 'r') as infile, open(''+search_string+'.m3u', 'w') as outfile:
for line in infile:
if "group-title=\"" + search_string +"" in line:
outfile.writelines([line, next(infile), next(infile)])