
arquivos = ['exemplo1.pdf', 'exemplo2.pdf', 'exemplo3.pdf', 'exemplo4.pdf', 'exemplo.mp3']
pdfs = []

for arquivo in arquivos:
	if arquivo[-3:] == "pdf":
		pdfs.append(arquivo)
	else:
		print (arquivo, "não é um arquivo PDF")

print ("Essa é a lista de arquivos PDF: ", pdfs)

