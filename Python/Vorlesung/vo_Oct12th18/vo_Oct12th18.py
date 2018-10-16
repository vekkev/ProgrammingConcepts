#! /usr/bin/env python3

# Py03 "Pattern Matching" 12. October 2018 20:30-22:00 ONL 2 https://meet.lync.com/fhjoanneum-edu/lynctest10/KPL4JFMQ
# execute this etherpad at your computer in the terminal using:
#  curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.VLe80279GOgv0lTn$moodle/export/txt' > /tmp/tst.py 2>/dev/null; python3 /tmp/tst.py

# Hear you soon at 20:30 :)

students = """john feiner,Walzl Martin,Manuel Leitold,Bernd Maderer,Dominic Gross,Kevin Schmid,Lukas Haidacher,David Reindl,Nicoletta Kaehling,Maximilian Gurdet,Natalya Sucher,Andreas Kraus,Alexander Schadler,Markus Prem,Nimrod Olah,Raffael Rehberger,Christian Fressl,Christian Radlingmayer,Patrick Dürnberger,Angelika Sauer,Aldin Bektas,Kerstin Koch,Elvira Katic,Michael Klug,Alexander Wagner,Ingo Grasenick,Anastasiia Kozlova,Richard Großschädl,Markus Konrad,Agnieszka Sowinska,Leonhard Leopold,Kevin Gruber,doris spanner,Maximilian Feil,Andreas Feichtinger,Stefan Filipovic,Anna Klautzer,Jennifer Gassner,Jasmin Baier,Lucca Ladinig,Lukas Wechtitsch,Hannes Gschwend,Markus Tomberger,Lejla Sarcevic,Dvorak Philip""".split(
    ",")
print("Looking forward to hearing from you: {}".format(" and ".join(students)))

# https://www.parlament.gv.at/PAKT/VHG/XXVI/NRSITZ/NRSITZ_00006/fnameorig_681358.html
html = """
<html><head><meta http-equiv="Content-Type" content="text/html; charset=us-ascii"><meta name="Generator" content="Microsoft Word 14 (filtered)"><title>Parlamentarische Materialien</title><style></style><link rel="stylesheet" type="text/css" href="/PAKT/VHG/XXVI/NRSITZ/NRSITZ_00006/NRSP_006.css"><link rel="stylesheet" type="text/css" href="/styles/PDSteno.css"></head><body lang="DE-AT" link="blue" vlink="purple"><div class="WordSection1"><p class="DBl00r"><img width="209" height="106" id="Bild 5" src="NRSITZ00006__681358_image001.jpg" alt="Parlament Österreich"></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl01"><b><span lang="DE">Stenographisches</span></b><span lang="DE"> <b>Protokoll</b></span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00z"><img width="813" height="368" id="Grafik 3" src="NRSITZ00006__681358_image002.jpg"></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl00"><span lang="DE">&nbsp;</span></p><p class="DBl02"><b><span lang="DE" style="font-size:1.60em">6. Sitzung desNationalrates der Republik Österreich</span></b></p>

<p class="MsoNormal"><b><i><span style="layout-grid-mode:line">Ausschuss fürPetitionen und Bürgerinitiativen:</span></i></b></p><p class="MsoNormal"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 1 betreffend „Informationspflicht bei Unterbezahlungen undVerlän­gerung der Verfallfristen“</span></i></p><p class="MsoNormal"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 2 betreffend „Handy- und Internetnutzung von Kindern und Jugend­lichen“</span></i></p><p class="MsoNormal"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 3 betreffend „Erhaltung der Hausapotheken in derWildschönau“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 4 „Verbesserung der Lehrlingsausbildung“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">Bürgerinitiative Nr.5 betreffend „die längst fällige Einrichtung eines Unterstufenreal­gymnasiumsam BORG Hermagor ab dem Schuljahr 2015/2016“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 6 betreffend „Verpflichtung zur Abgabe unverkäuflicher Ware andie Zivilgesellschaft vor der Müllentsorgung – Anti-Wegwerf-Gesetz“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 7 betreffend „Gleiche Rechte für chronisch kranke Kinder“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 8 betreffend „die Abschaffung des Pensionssicherungsbeitragesfür PensionistInnen sowie BezieherInnen von Witwen/Witwer- und Waisenpensionen“</span></i></p><p class
="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 9 betreffend „Aufstockung der Vorbereitungsstunden bei dermündli­chen Matura der standardisierten kompetenzorientierten Reife-und Diplomprüfung“</span></i></p><p class="MsoNormal" style="margin-top:.70em;margin-right:0cm;margin-bottom:.70em; margin-left:0cm"><i><span style="layout-grid-mode:line">BürgerinitiativeNr. 10 betreffend „Fakten helfen! Einführung einer bundesweiten ano­<span style="letter-spacing:-.1pt">nymisierten Statistik überSchwangerschaftsabbrüche und Erforschung der Gründe/Mo­</span>tivedafür“</span></i></p>
"""


# Agenda:
# (1) 20:30 Review by Students: L->Z
# 1a lambda vs. function <= urls + top-level-domain, return number of occurrency, shortest domain, longest domain
def func(urls, topLevel):
    count = 0
    for url in urls:
        if url.endswith(topLevel):
            count += 1
    return count


urls = ["http://www.orf.at", "http://www.fh-joanneum.at"]
print("We test func: ", func(urls, ".at"))


def filterUrls(urls, urlFilter):
    return list(filter(lambda url: urlFilter in url, urls))


# 1b filter <= demo data: list of urls, list of emails filter ".at"
print("Filter Urls after orf: ", filterUrls(urls, "orf"))


# 1c map <= ... map email "a.b@c.org" -> domain "www.c.org"
def mapUrls(urls):
    return list(map(lambda url: url.replace("http", "https", 1), urls))


print("urls with https", mapUrls(urls))
# 1d reduce <= ... count number of "www"

from functools import reduce


def reduceUrls(urls):
    return reduce(lambda urlCurrent, urlNext: urlCurrent + urlNext.count("www"), urls, 0)


print("count of urls with www: ", reduceUrls(urls))
print(reduce(lambda a, b: b + " and " + b, urls))


# (2) 20:45 Input by jf
# Generator: (vs. function) for each... "yield" = ?? <= e.g. new filenames for generated list of images
def numberGen(maxVal):
    for no in range(maxVal):
        yield 2018 + no + 1


for n in numberGen(7):
    print(n)

# Pattern Matching: html-code <= For example you MUST KNOW: . \w \s \d [] + * ? {} Why Groups ?? Greedy = ? optional: ^, $, Backreferences \1 \2

# (2) 21:25 Read Code:
# 2a Generator: <= http://tuttlem.github.io/2015/02/03/using-yield-to-create-generators-in-python.html
# 2b RegEx: search re. find constants, patterns, methods, ...  <= https://github.com/pallets/werkzeug/blob/master/werkzeug/routing.py

# (3) Test on your own: in interactive python shell or with some other tool ( https://regex101.com )
# 3a strip html of ... <= https://www.parlament.gv.at/PAKT/VHG/XXVI/NRSITZ/NRSITZ_00006/fnameorig_681358.html
# 3b extract <= e.g. number and title of "Bürgerinitiative" ...
# 3c find text between tags e.g. in <p> </p>, <i>...</i>... <= https://www.parlament.gv.at/PAKT/VHG/XXVI/I/I_00205/fnameorig_699858.html

# ?============
# See you at 21:45
# =============

# (4) 21:45 All-together: we (re-)work on the mini-tasks from above

import re

# Frage: warum compile ??
# TODO all together at 21:45: try out to strip html
print("Some examples: ... ", re.findall(r'p', html))
# TODO all together at 21:45: extract url of a link


# (5) 22:00 Good night, sleep tight!






