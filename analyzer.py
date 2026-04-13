from textblob import TextBlob
from collections import Counter
from  nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re

#Classe de que realiza toda a análise do texto
class TextMindAnalyzer:
    def __init__(self, text):
        self.text = text
        self.blob = TextBlob(text=text)

        #Stopwords para tratar as palavras-chave
        try:
            self.stop_words = set(stopwords.words('portuguese'))
        except:
            self.stop_words = set()


    def _clean_word(self, word):
        return re.sub(r'[^\w]', '', word.lower())
    

    #Status básicos e remove stopwords
    def get_basic_stats(self):
        words = re.findall(r'\w+', self.text.lower())
        meaningful_words = [
            w for w in words 
            if w.isalnum() and w not in self.stop_words and len(w) > 3
        ]

        return {
            "total_words": len(words),
            "unique_words": len(set(words)),
            "top_words": Counter(meaningful_words).most_common(5)
        }
    


    #Obtem o sentimento do texto
    def get_sentiment(self):
        polarity = self.blob.sentiment.polarity
        if polarity > 0.1: return "Positivo"
        if polarity < -0.1: return "Negativo"
        return "Neutro"
    


    def get_summary(self, num_sentences=3):
        sentences = sent_tokenize(self.text)
        if len(sentences) <= num_sentences:
            return self.text

        # Calcular frequência de palavras 
        words = word_tokenize(self.text.lower())
        freq_table = Counter([w for w in words if w.isalnum() and w not in self.stop_words])
        
        if not freq_table:
            return sentences[0]

        max_freq = max(freq_table.values())

        # Normaliza as frequências
        for word in freq_table:
            freq_table[word] = freq_table[word] / max_freq


        # Pontuar frases pela relevância das palavras
        sentence_scores = {}
        for sent in sentences:
            sentence_words = word_tokenize(sent.lower())
            for word in sentence_words:
                if word in freq_table:
                    if sent not in sentence_scores:
                        sentence_scores[sent] = freq_table[word]
                    else:
                        sentence_scores[sent] += freq_table[word]



        # Pega a melhor frase de cada terço do texto 
        chunk_size = len(sentences) // num_sentences
        final_summary_sentences = []
        
        for i in range(num_sentences):
            start = i * chunk_size
            # No último terço, pega até o final
            end = (i + 1) * chunk_size if i < num_sentences - 1 else len(sentences)
            chunk = sentences[start:end]
            
            if chunk:
                # Escolhe a frase com maior score dentro deste bloco
                best_in_chunk = max(chunk, key=lambda s: sentence_scores.get(s, 0))
                final_summary_sentences.append(best_in_chunk)

        return " ".join(final_summary_sentences)

        
