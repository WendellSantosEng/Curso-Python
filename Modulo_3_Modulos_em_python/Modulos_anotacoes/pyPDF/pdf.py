from pathlib import Path
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter


ROOT_FILE = Path(__file__).parent
CAMINHO_PDFS_ORIGINAIS = ROOT_FILE / "pdf"
NOVOS_PDFS = ROOT_FILE / "novos_pdfs"

if NOVOS_PDFS.exists() is not True:
    Path.mkdir(NOVOS_PDFS)

RELATORIO_BANCE = CAMINHO_PDFS_ORIGINAIS / "R20240105.pdf"

reader = PdfReader(RELATORIO_BANCE)

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())

# esta dando erro ->
# with open (NOVOS_PDFS / image0.name , "w") as fp:
#     fp.write(image0.data)

writer = PdfWriter()
writer.add_page(page0)

with open(NOVOS_PDFS / "page0.pdf", "wb") as fp:
    writer.write(fp)

for image_file_object in page0.images:
    with open(image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)