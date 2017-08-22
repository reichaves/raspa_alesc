def arquivos_pdf(lista_diretorio):
	# Retorna a lista de arquivos PDF de um determinado diretório
	# lista_diretorio: lista
	# retorna: lista
	pdfs = []
	for arquivo in lista_diretorio:
		if arquivo[-3:] == "pdf":
			pdfs.append(arquivo)
	return pdfs

arquivos = ['arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf', 'arquivo4.mp3']

lista_final = arquivos_pdf(arquivos)
print (lista_final)


def arquivos_geral(lista, ext):
	# Retorna a lista de arquivos PDF de um determinado diretório
	# lista: lista
	# ext: string de três caracteres que representa a extensão do arquivo
	# retorna: lista

	pdfs = []
	for arquivo in lista:
		if arquivo[-3:] == ext:
			pdfs.append(arquivo)
	return pdfs

arquivos = ['arquivo1.pdf', 'arquivo2.jpg', 'arquivo3.pdf', 'arquivo4.mp3']
lista_final = arquivos_geral(arquivos, "jpg")
print (lista_final)

lista_final = arquivos_geral(arquivos, "pdf")
print (lista_final)
