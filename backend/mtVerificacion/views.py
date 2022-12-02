from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from turing_machine import TuringMachine
from automata.fa.dfa import DFA
from nltk import CFG
from nltk.parse.generate import generate
from nltk.corpus import words
import random

# Create your views here.

class Calculo(APIView):
    def createJson(self,message,data,status):
        custom={"messages":message,"pay_load":data,"status":status}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk

    def get(self, request, format=None):
        responseOk=self.createJson("succes","202","funciona")
        return Response(responseOk)

    def post(self, request, format=None):
        serializer = request.data
        data = str(serializer)
        tam=14-len(data)
        data=(data[tam:])
        tam2=len(data)-2
        data=(data[:tam2])

        llaves = TuringMachine(
        {
            ('q0', '{'): ('q1', '*', 'R'), 
            ('q1', '{'): ('q1', '*', 'R'), ('q1', '}'): ('q1', '}', 'R'), ('q1', ''): ('q2', '', 'L'), 
            ('q2', '}'): ('q2', '}', 'L'), ('q2', '#'): ('q2', '#', 'L'), ('q2', '{'): ('q2', '{', 'L'), ('q2', ''): ('q6', '', 'R'), ('q2', '*'): ('q3', '{', 'R'), 
            ('q3', '*'): ('q3', '*', 'R'), ('q3', '{'): ('q3', '{', 'R'), ('q3', '}'): ('q3', '}', 'R'), ('q3', '#'): ('q3', '#', 'R'), ('q3', ''): ('q4', '', 'L'), 
            ('q4', '*'): ('q4', '*', 'L'), ('q4', '{'): ('q4', '{', 'L'), ('q4', '#'): ('q4', '#', 'L'), ('q4', '}'): ('q5', '#', 'R'), 
            ('q5', '*'): ('q5', '*', 'R'), ('q5', '{'): ('q5', '{', 'R'), ('q5', '#'): ('q5', '#', 'R'), ('q5', '}'): ('q5', '}', 'R'), ('q5', ''): ('q2', '', 'L'),
            ('q6', '*'): ('q6', '*', 'R'), ('q6', '{'): ('q6', '{', 'R'), ('q6', '#'): ('q6', '#', 'R'), ('q6', '}'): ('q8', '}', 'R'), ('q6', ''): ('q7', '', 'L'),
            ('q7', '*'): ('q7', '*', 'L'), ('q7', '{'): ('q7', '{', 'L'), ('q7', '#'): ('q7', '}', 'L'), ('q7', '}'): ('q7', '}', 'L'), ('q7', ''): ('qa', '', 'R'),  
        }
        )

        paren = TuringMachine(
        {
            ('q0', '('): ('q1', '*', 'R'), 
            ('q1', '('): ('q1', '*', 'R'), ('q1', ')'): ('q1', ')', 'R'), ('q1', ''): ('q2', '', 'L'), 
            ('q2', ')'): ('q2', ')', 'L'), ('q2', '#'): ('q2', '#', 'L'), ('q2', '('): ('q2', '(', 'L'), ('q2', ''): ('q6', '', 'R'), ('q2', '*'): ('q3', '(', 'R'), 
            ('q3', '*'): ('q3', '*', 'R'), ('q3', '('): ('q3', '(', 'R'), ('q3', ')'): ('q3', ')', 'R'), ('q3', '#'): ('q3', '#', 'R'), ('q3', ''): ('q4', '', 'L'), 
            ('q4', '*'): ('q4', '*', 'L'), ('q4', '('): ('q4', '(', 'L'), ('q4', '#'): ('q4', '#', 'L'), ('q4', ')'): ('q5', '#', 'R'), 
            ('q5', '*'): ('q5', '*', 'R'), ('q5', '('): ('q5', '(', 'R'), ('q5', '#'): ('q5', '#', 'R'), ('q5', ')'): ('q5', ')', 'R'), ('q5', ''): ('q2', '', 'L'),
            ('q6', '*'): ('q6', '*', 'R'), ('q6', '('): ('q6', '(', 'R'), ('q6', '#'): ('q6', '#', 'R'), ('q6', ')'): ('q8', ')', 'R'), ('q6', ''): ('q7', '', 'L'),
            ('q7', '*'): ('q7', '*', 'L'), ('q7', '('): ('q7', '(', 'L'), ('q7', '#'): ('q7', ')', 'L'), ('q7', ')'): ('q7', ')', 'L'), ('q7', ''): ('qa', '', 'R'),  
        }
        )

        dfa = DFA(
            states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7'},
            input_symbols={
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '0','1','2','3','4','5','6','7','8','9',
                ' ','{','}','(',')',','
                },
            transitions={
                'q0': {'{': 'q1'},
                'q1': {' ': 'q1', '{': 'q1', '(':'q1', ')':'q5', '}':'q7',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q2': {' ': 'q2', '}': 'q6', ')':'q3', ',':'q4', '{':'q1', '(':'q1',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q3': {')':'q3', ',':'q2', ' ':'q3', '}':'q6'},
                'q4': {' ':'q4', '{':'q1', '(':'q1',
                    'a':'q2','b':'q2','c':'q2','d':'q2','e':'q2','f':'q2','g':'q2','h':'q2','i':'q2','j':'q2','k':'q2','l':'q2','m':'q2','n':'q2','o':'q2','p':'q2','q':'q2','r':'q2','s':'q2','t':'q2','u':'q2','v':'q2','w':'q2','x':'q2','y':'q2','z':'q2',
                    'A':'q2','B':'q2','C':'q2','D':'q2','E':'q2','F':'q2','G':'q2','H':'q2','I':'q2','J':'q2','K':'q2','L':'q2','M':'q2','N':'q2','O':'q2','P':'q2','Q':'q2','R':'q2','S':'q2','T':'q2','U':'q2','V':'q2','W':'q2','X':'q2','Y':'q2','Z':'q2',
                    '0':'q2','1':'q2','2':'q2','3':'q2','4':'q2','5':'q2','6':'q2','7':'q2','8':'q2','9':'q2'
                    },
                'q5': {')':'q5', ' ':'q5', '}':'q7'},
                'q6': {',':'q2', '}':'q6'},
                'q7': {',':'q1', '}':'q7'}
            },
            allow_partial=True,
            initial_state='q0',
            final_states={'q6','q7'}
        )

        resultante1 = ''
        resultante2 = ''
        aux=True
        for indice in range(len(data)):
            caracter = data[indice]
            if (caracter=='{' or caracter=='}'):
                resultante1 = resultante1 + caracter
                
        for indice2 in range(len(data)):
            caracter = data[indice2]
            if (caracter=='(' or caracter==')'):
                resultante2 = resultante2 + caracter
        if (len(resultante2)==0):
            aux=False

        if (llaves.accepts(resultante1) == True):
            if(aux==False):
                #return Response('Conjunto valido')
                if dfa.accepts_input(data):
                    #return Response('Conjunto valido')
                    responseOk=self.createJson("succes","202","Valido")
                    return Response(responseOk)
                else:
                    #return Response('conjunto no valido')
                    responseOk=self.createJson("succes","202","No valido")
                    return Response(responseOk)
            else:
                if (paren.accepts(resultante2)==True):
                    #return Response('Conjunto valido')
                    if dfa.accepts_input(data):
                        responseOk=self.createJson("succes","202","Valido")
                        return Response(responseOk)
                    else:
                        responseOk=self.createJson("succes","202","No valido")
                        return Response(responseOk)
                else:
                    print(resultante2)
                    responseOk=self.createJson("succes","202","No valido")
                    return Response(responseOk)
        else:
                responseOk=self.createJson("succes","202","No valido")
                return Response(responseOk)


class Quiz(APIView): 
    # def consultar(p1,p2,p3,p4,p5,value):
    #     if value == 0:
    #         r1 = p1
    #         r2 = p2
    #         r3 = p3
    #         r4 = p4
    #         r5 = p5

    def createJson(self,p1,p2,p3,p4,p5):
        custom={"p1":p1,"p2":p2,"p3":p3,"p4":p4,"p5":p5,}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk

    def get(self, request, format=None):
        # Crear preguntas
        correctos = CFG.fromstring("""
            S -> KI VC VC V KF 
            KI -> '{' 
            VC -> V C
            KF -> '}'
            V -> ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0'
            C -> ','
        """)

        erroneos = CFG.fromstring("""
            S -> KI VE KF 
            KI -> '{' | '['
            VE -> VX VC V | VC VX V | VC VC VX | VC VC VC
            KF ->  '}' | ' '
            VX -> ' a)' | ' b,' | ', c' | ' (e,)' | ' f(,' | ' 4),' | ' 5)' | ' 6,' | ' 7,,' | ' (8),'
            VC -> V C
            V -> ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0'
            C -> ','
        """)
        cBuenos = []
        cMalos = []
        valor=0
        vran1=random.randint(1,4095)
        vran2=random.randint(1,4095)
        vran3=random.randint(1,4095)
        for s in generate(correctos,n=4095):
            #print(''.join(s))
            valor = ''.join(s)
            cBuenos.append(valor)

        for s in generate(erroneos,n=6095):
            #print(''.join(s))
            valor = ''.join(s)
            cMalos.append(valor)
        print('hola')

        p1 = random.randint(1,4)
        p2 = cBuenos[vran1] + '|' + cBuenos[vran2] + '|' + cMalos[vran3] + '|' + str(random.randint(1,4))
        p3 = random.randint(1,4)
        p4 = cMalos[vran1] + '|' + cMalos[vran2] + '|' + cBuenos[vran3] + '|' + str(random.randint(1,3))
        p5 = random.randint(1,4)
        print(p4)
        responseOk=self.createJson(p1,p2,p3,p4,p5)
        return Response(responseOk) 

        