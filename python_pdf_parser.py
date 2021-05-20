# Visual tools
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import pdfplumber
import re


pdf = pdfplumber.open('braiding_sweetgrass.pdf')
pages = pdf.pages[9:458]
comment_words = ''
stopwords = set(STOPWORDS)
words = []
for page in pages:
    val = str(page.extract_text())
    word = re.findall(r"[\w']+", val)
    for w in word:
        w = w.lower()
        if len(w) <=2:
            w=""
    comment_words+= " ".join(word)+" "
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)

# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
  
plt.show()