media_semestral = float(input ("digite a sua média semestral:"))
avaliacao_final= float (input("digite a sua nota da avaliação final:"))
media_semestral = media_semestral*6
avaliacao_final = avaliacao_final*4
media_final=(avaliacao_final + media_semestral )/10
print(f"A sua média final é {media_final:.2f}") 