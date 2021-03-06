from AssitentTypeEnum import AssitentTypeEnum
from Assistent import Assistent
from ssml_builder.core import Speech
import random

exercicios = [
    "Alongar os braços para frente 15 segundos",
    "Alongar os braços atrás do pescoço 15 segundos ",
    "Mexer o pescoço para baixo e para cima 15 segundos",
    "Girando as mãos 15 segundos",
    "Alongando os dedos 15 segundos",
    "Alongando as pernas 15 segundos",
    "Flexionando as pernas 15 segundos",
    "Joelho na frente 15 segundos",
    "Flexionar o Joelho 15 segundos"]

half_1 = [1,2,3,4,5,6,7]
half_2 = [8,9,10,11,12,13,14,15]

mylist = [
    "Qilson",
    "O que não te desafia não faz você mudar!", 
    "",
    "",
    "",
    "",
    "O corpo alcança o que a mente acredita."
    "",
    "",
    "",
    ""]

speech = Speech()

for item in exercicios:
    speech.add_text(item)
    speech.pause(time="2s")
    for n in half_1:
        speech.add_text(str(n))
        speech.pause(time="1s")

    speech.add_text(random.choice(mylist))
    speech.pause(time="1s")

    for n in half_2:
        speech.add_text(str(n))
        speech.pause(time="1s")

type_asistente = AssitentTypeEnum.AWS

assist = Assistent.factory(type_asistente)
mp3 = assist.synthesize_speech(speech.speak())

with open("out/{}.mp3".format(type_asistente.name), 'wb') as out:
    out.write(mp3)