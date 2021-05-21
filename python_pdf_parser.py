# Visual tools
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import pdfplumber
import re


pdf = pdfplumber.open('ch05.pdf')
pages = pdf.pages[2:]
comment_words = ''
stopwords = set(STOPWORDS)
words = []
for page in pages:
    print(page.extract_text())
#     val = str(page.extract_text())
#     word = re.findall(r"[\w']+", val)
    
#     for w in word:# filter for numbers, single letters, chapter. Make everything lowercase
#         if w.isupper():
#             # print(w)
#             word.remove(w)
#         if w.isdigit() and len(w)<4:
#             word.remove(w)
#         #print(w)
#     comment_words+= " ".join(word)+" "

# print(comment_words)
# wordcloud = WordCloud(width = 800, height = 800,
#                 background_color ='white',
#                 stopwords = stopwords,
#                 min_font_size = 10).generate(comment_words)

# # plot the WordCloud image                       
# plt.figure(figsize = (8, 8), facecolor = None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad = 0)
  
# plt.show()