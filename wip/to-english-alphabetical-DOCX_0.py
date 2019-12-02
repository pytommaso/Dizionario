#### about CSV
import csv
f = open('list_of_words2.csv', newline='')
reader = csv.reader(f)

#### about English dictionary
import enchant
eng = enchant.Dict("en_US")

#### about Excell writing
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet Name")
style1 = xlwt.easyxf()
style2 = xlwt.easyxf('align: horiz center')


#### the LOGIC
eng_words = []
other_words = []
locutions = []
for row in reader:
    word = (''.join(row))  #trasformo in stringa effettiva
    if word == '':
        continue
    if ' ' in word:
        locutions.append(word)
    elif eng.check(word) == True:
        eng_words.append(word.capitalize())
    else:
        other_words.append(word)

# print(eng_words)
# print(other_words)
# print(locutions)

## Google trans API
from googletrans import Translator  # Import Translator module from googletrans package

translator = Translator() # Create object of Translator.


b =''
for item in eng_words:
    b = b + item + '\n'

translated = translator.translate(b, src='en', dest = 'it')

# Output
print(translated.text)
