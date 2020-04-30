import requests

f = open("plik.txt", "w")
r = requests.get('https://www.realmadryt.pl')

f.write("Url: " + r.url + '\n\n')
f.write("Status code: " + str(r.status_code) + '\n\n')
f.write("Headers: " + str(r.headers) + '\n\n')
f.write("Content: " + str(r.content) + '\n\n')
f.write("Text: " + str(r.text) + '\n\n')

f.close()