import streamlit as st
from Janome.tokenizer import Tokenizer
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