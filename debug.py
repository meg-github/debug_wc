import streamlit as st
#import MeCab
from janome.tokenizer import Tokenizer
import collections
from matplotlib import pyplot as plt
from wordcloud import WordCloud

text = "これはテスト用のテキストです．この解析結果がワードクラウドによって表示されるはずです"

tk = Tokenizer(wakati=True)
tokens = tk.tokenize(text)
words = " ".join(list(tokens))

wc = WordCloud(font_path = "SourceHanSerifK-Light.otf").generate(words)



fig = plt.figure(figsize=(12,9))
ax = plt.axes()
st.set_option('deprecation.showPyplotGlobalUse', True)
plt.tight_layout()
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
st.pyplot(fig)


import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()