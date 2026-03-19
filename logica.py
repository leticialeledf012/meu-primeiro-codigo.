# Pergunta sobre hidratação (Texto)
bebeu_agua = input("Já bebeu pelo menos 1 litro de água hoje? (sim/nao): ")

if bebeu_agua.lower() == "nao":
    print("⚠️ PARE TUDO! Vá beber um copo de água antes de começar a estudar.")

# Pergunta sobre o cansaço (Número)
cansaco = int(input("De 1 a 10, o quanto você está cansada hoje? "))

if cansaco < 5:
    print("🚀 Boa! O foco está alto. Vamos codar por 1 hora.")
elif cansaco >= 5 and cansaco <= 8:
    print("⚖️ Equilíbrio é a chave. Estude 30 minutos e faça uma pausa.")
else:
    print("😴 O dia foi pesado. Leia apenas um artigo técnico e descanse.")
  
