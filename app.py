import PyPDF2
import os


directory = "./input"
for filename in os.listdir(directory):
    if filename.endswith(".pdf"): 
         # print(os.path.join(directory, filename))

        inputfile=directory+"/"+filename

        watermark='watermark.pdf'


        outputfile = "./output/"+filename


        with open(inputfile,'rb') as inputfile:
            pdf = PyPDF2.PdfFileReader(inputfile)
            pages=pdf.getNumPages()
            # print(pages)
            with open(watermark,'rb') as watermarkfile:
                pdfwriter = PyPDF2.PdfFileWriter()
                watermarkpdf = PyPDF2.PdfFileReader(watermark)
                for page in range(pages):
                    #print(page)
                    p = pdf.getPage(page)

                    w = watermarkpdf.getPage(0)

                    p.mergePage(w)
                
                    

                    pdfwriter.addPage(p)

                with open(outputfile,'wb') as outputfilecontent:
                    pdfwriter.write(outputfilecontent)
                print("DONE:"+ filename)
