import os
import shutil
import time

print("=== RATARIA MUDANÇAS ===")

pasta_origem = input("Digite o caminho da pasta de ORIGEM: ").strip()
pasta_destino = input("Digite o caminho da pasta de DESTINO: ").strip()

if not os.path.isdir(pasta_origem):
    print("rataria não achou a pasta")
    exit()

os.makedirs(pasta_destino, exist_ok=True)

print("\nRateando... Pressione CTRL + C para parar.\n")

try:
    while True:
        for arquivo in os.listdir(pasta_origem):

            if not arquivo.lower().endswith(".mp3"):
                continue

            caminho_origem = os.path.join(pasta_origem, arquivo)
            caminho_destino = os.path.join(pasta_destino, arquivo)

            if not os.path.isfile(caminho_origem):
                continue

            if os.path.exists(caminho_destino):
                continue

            shutil.copy2(caminho_origem, caminho_destino)
            print(f"rataria copiou: {arquivo}")

        time.sleep(2)  

except KeyboardInterrupt:
    print("\n rataria interrompida")
