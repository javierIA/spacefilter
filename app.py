import glob
from io import StringIO
from itertools import count
import tools.ScanPDFChecker as ScanPDFChecker
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import spacy_transformers
import spacy
import tools.PdfReader as PdfReader
import tools.ScanPDFChecker as ScanPDFChecker
def main():
    path = glob.glob('facturas/**/*.pdf')
    nlp_ner_model = spacy.load('model-best')
    for file in path:
        if ScanPDFChecker.ispdfa(file):
            textPDF=PdfReader.reader(file)
            doc = nlp_ner_model(textPDF)
            f=open("taxID.txt", "a+")

            for ent in doc.ents:
                print(ent.text, ent.start_char, ent.end_char, ent.label_)
                f.write("text:"+ent.text+"label:"+str(ent.label)+"file:"+str(file)+"\n")
    
    None
    
def count_files():
    path = glob.glob('facturas/**/*.pdf')
    print(len(path))
    
if __name__ == "__main__":
    main()
   