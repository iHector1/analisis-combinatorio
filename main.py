from math import factorial
def menu():
    print('----Bienvenido----\n')
    print('Inserte el numero de preguntas de su examen: ')
    numAsk=int(input())
    print('Inserte el numero de opciones que tiene cada pregunta')
    numOptions=int(input())
    print(numAsk,numOptions)
    porcentage(numAsk,numOptions)

def porcentage(numAsk,numOptions):
    cal=(0,10,20,30,40,50,60,70,80,90,100)
    incorrectAnswers=numOptions-1
    corectAnswerers=1
    correctQuestions=0
    incorrectQuestions=0
    porcentaje=0
    calculado=0
    combination=pow(numOptions,numAsk)
    i=0
    fact=factorial(numAsk)
    for i in cal:
        incorrectQuestions=round(numAsk*((100-i)/100))
        print("\n\nPreguntas incorrectas:",incorrectQuestions)
        correctQuestions=numAsk-incorrectQuestions 
        print("Preguntas correctas:",correctQuestions)
        calculado=calculatedPorcentage(corectAnswerers,incorrectAnswers,correctQuestions,incorrectQuestions,fact,combination)*100
        porcentaje+=calculatedPorcentage(corectAnswerers,incorrectAnswers,correctQuestions,incorrectQuestions,fact,combination)
        print("La probabilidad de sacar {} es de {:.6f}%".format(i,calculado))

def calculatedPorcentage(correctAnswer,incorrectAnswers,rc,ri,fact,combination):
    permutations=0
    vrc=pow(correctAnswer,rc)
    vri=pow(incorrectAnswers,ri)
    result=vrc*vri
    if correctAnswer==0 or incorrectAnswers==0:
        return result/combination
    permutations=fact/(factorial(rc)*factorial(ri))
    return result*permutations/combination

    
class Exam():
    def __init__(self) -> None:
        pass
menu()
