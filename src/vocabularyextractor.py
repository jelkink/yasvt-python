import PyPDF2
import nltk
import string
import argostranslate.package
import argostranslate.translate

from urllib import request
import pymorphy2

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_ru')

languages = {
    "english": ("english", "en", "eng"),
    "russian": ("russian", "ru", "rus")
}

from helpers import uri_validator

class VocabularyExtractor:

    def read(self, filename, language):

        if language == "":
            raise ValueError("ERROR: Need to specify a language with -l")

        self.input = filename
        self.language = languages[language]
        self.text = ""
        
        if uri_validator(filename):
            self.read_url()
        elif filename.endswith(".pdf"):
            self.read_pdf()
        else:
            self.read_text()

        translate_table = dict((ord(char), None) for char in string.punctuation + "\":0123456789")  
        self.text = self.text.translate(translate_table)
        
        morph = pymorphy2.MorphAnalyzer()

        tokens = list(set(nltk.word_tokenize(self.text.lower(), language = self.language[0])))
        tokens = [w for w in tokens if len(w) > 2]
        self.lemmas = list(set([morph.parse(token)[0].normal_form for token in tokens]))
        self.translations = self.lemmas

    def read_text(self):
        with open(self.input, "r", encoding="utf-8") as infile:
            self.text = infile.read()

    def read_url(self):
        response = request.urlopen(self.input)
        self.text = response.read().decode('utf8')

    def read_pdf(self):
           
        with open(self.input, "rb") as infile:

            pdf_reader = PyPDF2.PdfReader(infile)

            num_pages = len(pdf_reader.pages)
            for page in range(num_pages):
        
                pdf_page = pdf_reader.pages[page]
                self.text += pdf_page.extract_text()

    def write(self, filename):
        with open(filename, "w", encoding = "utf-8") as outfile:
            outfile.write(self.language[0] + ",english\n")
            for word, trans in zip(self.lemmas, self.translations):
                outfile.write(word + "," + trans + "\n")

    def translate(self):
        self.translations = [argostranslate.translate.translate(w, self.language[1], "en") if w is not None else '' for w in self.lemmas]