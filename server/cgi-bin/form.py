import cgi
import html
import cgi
import server.get_friends as gf

form = cgi.FieldStorage()


text1 = form.getfirst("t1", "gt")
text2 = form.getfirst("t2", "gt")


lister = []
lister.append(text1)
lister.append(text2)
try:
    for counter in range(3,999):

        name = 't' + str(counter)
        lister.append((form.getfirst(name, '-1')))
        if lister[-1] == '-1':
            lister.pop(-1)
            break
except:
    print('lzlz')



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>t1: {}</p>".format(gf.get_friends(lister)))


print("""</body>
        </html>""")

