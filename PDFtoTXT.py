
import os
import re


from pdfminer.pdfparser import PDFParser
import pdfdocument
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextState
import pdftextract


# 1. convert PDF into TXT
class PDFtoTxt():
    def __init__(self, pdfpapth):
        self.pdfPath = pdfpapth

    #Parse PDF document
    def GetContentFromPdf(self):
        with open(self.pdfPath,'rb') as f:
            parser = PDFParser(f)
        pdf = pdfdocument()

        #connect parser with document
        parser.set_document(pdf)
        pdf.set_parser(parser)
        pdf.initialize()

        #check for ConvertAble
        if not pdf.is_extractable:
            raise PDFTextState
        else:
            return list(pdf.get_pages())

    def SaveContent(self, PageIndex= None, SavePath = None):
        pages = self.GetContentFromPdf()
        NumPage = 0
        pdfResourceManager = PDFResourceManager()
        laParams = LAParams()
        pdfPageAggregator = PDFPageAggregator(pdfResourceManager, laparams= laParams) #process PDF content

        interpreter = PDFPageInterpreter(pdfResourceManager,pdfPageAggregator) #create PDF interpreter
        #PageIndex: specific page information
        if PageIndex:
            pages = list(pages[i-1] for i in PageIndex) #specify the path
        SavePath = SavePath if SavePath else self.pdfpath.replace('pdf','txt')
        # save page information
        with open(SavePath,'w',encoding='utf-8') as f:
            for page in pages:
                NumPage +=1
                interpreter.process_page(page)
                layout = pdfPageAggregator.get_result()
                for x in layout:
                    if isinstance(x,LTTextBoxHorizontal): #get one row text
                        #save
                        results = x.get_text()
                        f.write(results)
                        f.write('\n')

if __name__ == '__main__':
    pdfToText11 = PDFtoTxt(r"CSR11.pdf")
    pdfToText11.SaveContent()
    pdfToText12 = PDFtoTxt(r"CSR12.pdf")
    pdfToText12.SaveContent()
    pdfToText13 = PDFtoTxt(r"CSR13.pdf")
    pdfToText13.SaveContent()
    pdfToText14 = PDFtoTxt(r"CSR14.pdf")
    pdfToText14.SaveContent()
    pdfToText15 = PDFtoTxt(r"B1.pdf")
    pdfToText15.SaveContent()
    pdfToText16 = PDFtoTxt(r"B1.pdf")
    pdfToText16.SaveContent()
    pdfToText17 = PDFtoTxt(r"B1.pdf")
    pdfToText17.SaveContent()
    pdfToText18 = PDFtoTxt(r"B1.pdf")
    pdfToText18.SaveContent()
    pdfToText19 = PDFtoTxt(r"B1.pdf")
    pdfToText19.SaveContent()
    pdfToText20 = PDFtoTxt(r"B20.pdf")
    pdfToText20.SaveContent()


























