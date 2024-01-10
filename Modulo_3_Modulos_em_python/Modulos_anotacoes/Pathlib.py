

# CODIGO APENAS DE EXEMPLO !!!


# from pathlib import Path

# caminho_projeto = Path()
# # print(caminho_projeto.absolute())

# caminho_arquivo = Path(__file__)
# # print(caminho_arquivo)

# ideias = caminho_arquivo.parent / "ideias"
# # print(ideias / "arquivo.txt")

# caminho_arquivo = Path.home() / "Exemplo" / "arquivo.txt"
# caminho_arquivo.touch()
# caminho_arquivo.write_text("Ola mundo")
# caminho_arquivo.unlink()

# caminho_pasta = Path.home() / "Exemplo" / "Python é legal"
# caminho_pasta.mkdir(exist_ok=True)
# subpasta = caminho_pasta / "subpasta"
# subpasta.mkdir(exist_ok=True)



# files = caminho_pasta / "files"
# files.mkdir(exist_ok=True)

# for i in range(10):
#     file = files / f"fiel_{i}.txt"
#     if file.exists():
#         file.unlink()
#     else:
#         file.touch()

#     with file.open("a+") as text_file:
#         text_file.write("Ola mundo\n")
#         text_file.write(f"file_{i}.txt")


# def rmtree(root: Path, remove_root= True):
#     for file in root.glob("*"):
#         if file.is_dir():
#             print("DIR: ", file)
#             rmtree(file, False)
#             file.rmdir()
#         else:
#             print("FILE: ", file)
#             file.unlink()
#     if remove_root:
#         root.rmdir()

# rmtree(caminho_pasta)
