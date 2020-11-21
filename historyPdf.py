from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=15)


def convertTuple(tup):
    str1 = '  |  '.join(tup)
    return str1


def createPdf(inp):
    lineNo = 4
    pdf.cell(200, 10, txt='HISTORY',
             ln=1, align='C')
    pdf.cell(200, 10, txt='Time  |  user  |  query  |  date',
             ln=3, align='C')
    for i in inp:
        a = convertTuple(i)
        pdf.cell(200, 10, txt=a,
                 ln=lineNo, align='C')
        lineNo += 1
    pdf.output("resources\\history.pdf")
