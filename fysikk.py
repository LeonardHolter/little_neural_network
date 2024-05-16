# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:47:09 2023

@author: dagfi
"""
import random as rd


questions={
1	:	"Hva er naturvitenskapelig metode?"	,	
2	:	"Hva er gyldighetsområde og antagelser i fysikk?	"	,	
3	:	"Hva er en måling i fysikk og hvor nøyaktige kan vi være når vi bruker de?	"	,	
4	:	"Når kan vi bruke bevegelsesligningene?	"	,	
5	:	"Skriv opp de fire bevegelsesligningene	"	,	
6	:	"Hva er en vektor? Nevn 3 vektorstørrelser	"	,	
7	:	"Om en ball flyter med 25% av volumet nedsunket i vann? Hvor stor er tettheten til ballen?	"	,	
8	:	"Hvordan gjør du om fra km/h til m/s og hvordan gjør du om fra 1 km^3 til m^3?	"	,	
9	:	"Om du starter i ro og kjører med en akselerasjon på 1 m/s^2 hva er farten etter og strekningen tilbakelagt på 10 sekunder?	"	,	
10	:	"Om du kjører i 10 m/s i 10 sekunder, 20 m/s i 20 s og 30 m/s i 30 sekunder, hva er gjennomsnittsfarten og hvor lang er den totale tilbakelagte strekningen?	"	,	

11	:	"Hva sier newtons 1. og 3. lov?	"	,
12	:	"Hva er enhetene til kraft, masse og akselerasjon?	"	,	
13	:	"Tegn alle kreftene som virker på en bil som kjører med konstant fart	"	,	
14	:	"Tegn kreftene som virker på en kloss på et skråplan	"	,	
15	:	"Tegn kreftene som virker på to bokser som ligger oppå hverandre på et bord	"	,	
16	:	"Hva er fritt fall?	"	,	
17	:	"Tegn kreftene på en ball som har oppnådd terminalfart og finn et utrykk for denne?	"	,	
18	:	"Luftmotstanden L sier å være L=kv^2, hva påvirker k?	"	,	
19	:	"Hvis friksjonskraften er R=μN, finn et utrykk for arbeidet over en strekning s	"	,	
20	:	"Forklar hvordan vi kan gå frem for å beregne farten til en kloss på et skråplan med friksjon og luftmotstand	"	,	

21	:	"Vi slipper en kule fra en høyde h, hva er farten når kulen treffer bakken om vi ignorerer luftmotstand? 	"	,	
22	:	"Vi slipper en kule fra en høyde h, hvordan kan vi gå frem om vi ønsker å finne farten når kulen treffer bakken med luftmotstand inkludert? 	"	,	
23	:	"Hva sier energibevaringsloven og hva er virkningsgrad?	"	,	
24	:	"Når er mekanisk energi bevart og når er den ikke?	"	,	
25  :	"Gravitasjonskraften virker på en kule når du holder den og når den faller, i hvilket tilfelle gjør kraften et arbeid?	"	,

26	:	"Hva skjer om to objekter med samme masse kolliderer i et elastisk sentralt støt?	"	,
27	:	"Når er bevegelsesmengde bevart?	"	,	
28	:	"Hva er forskjellen på elastiske og uelastiske støt?	"	,	
29	:	"Hva er et fullstendig uelastisk støt og hva er en eksplosjon (i fysikk)?	"	,	
30	:	"Hvordan beskriver vi bevegelsesmengden til et legeme og hva er enheten?	"	,	
31	:	"Om vi plotter bevegelsesmengde mot tid hvilken størrelse representerer stigningstallet?	"	,	
32	:	"Hvordan kan vi regne ut sluttfarten til to objekter som kolliderer i et uelastisk støt? Hva trenger vi å vite?	"	,	
33	:	"Hva er effekt og hvilken enhet bruker vi for dette?	"	,	

34	:	"Skriv opp to viktige formler for effekt	"	,	
35	:	"Hva er virkningsgrad og vet du noe om virkningsgrad til en bensinmotor, solcelle eller elektrisk ovn?	"	,	
36	:	"Hvor mye strøm bruker en ovn som er merket 1000 W om den står på i 10 timer? Og hvor mye bruker en lyspære som er merket med 50 W	"	,	
37	:	"Hva sier ohms lov og for hvilke materialer gjelder denne typisk for?	"	,	
38	:	"Hva blir den totale resistansen om vi kobler to motstander med resistans r i serie og hva blir den i parallell?	"	,	
39	:	"Hva er totalresistansen om vi kobler tre motstander på 1 ohm, 2 ohm og 3 ohm i serie og hva blir resistansen om vi kobler de i parallell?	"	,	
40	:	"Hva er forskjellen på å seriekoble og parallellkabel batterier?	"	,	
41	:	"Hvilke antagelser gjør vi når vi regner på kretser?	"	,	
42	:	"Hva er definisjonen på elektrisk strøm?	"	,	
43	:	"Hva er definisjonen på spenning?	"	,	
44	:	"Hvordan definerer vi strømretningen i en krets? 	"	,

45  :   "Hva er forskjellen på temperatur og varme?",
46  :   "Forklar forskjellen på mikroskopiske og makroskopiske størrelser?",
47  :   "Hvorfor føles en metallbit kaldere enn en trebit i samme rom?",
48  :   "Hva er indre energi?",
49  :   "Finn et utrykk for farten til partiklene i en gass om partiklene har masse m og temperatur T",
50  :   "Hva er forskjellen på varmekapasitet og spesifikk varmekapasitet og hva sier enheten for spesifikk varmekapasitet",
51  :   "Hva betyr isoterm og hva betyr adiabatisk?",
52  :   "Hva er definisjonen på trykk og hvilke enheter brukes for det?",
53  :   "Hvordan klarer et fly å holde seg i luften?",
54  :   "Hvorfor må en bonde åpne luftelukene på låven om det er varslet storm?",
55  :   "Anslå kraften som virker fra luftrykket ned på en kvadratmeter på jorden",
56  :   "Forklar kort mekanismene i en varmepumpe",
57  :   "Hva koster mest energi av å varme opp en liter vann fra 20 grader til 100 grader eller å fordampe den samme mengden til gassform?",
58  :   "Hva sier termofysikkens 0., 1. og 2. lov?",
59  :   "forklar hvordan vi kan blåse opp en ballong fra mikro- og makroperspektiv",
60  :   "Hva sier Bernoulli om luft i bevegelse?",
61  :   "Hvorfor blåser vi på varm kaffe, svetter en varm sommerdag eller sprayer vann på epler som er i ferd med å fryse?",
62  :   "Diskuter fordeler og ulemper med å elektrifisere norsk sokkel?",

63  :   "hva er en svingning og hva er en bølge?",
64  :   "Hva er forskjellen på periode og bølgelengde?",
65  :   "Hva er lydens hastighet i luft og lyses hastighet i vakuum sånn ca. ?",
66  :   "Hva er forskjellen på mekaniske- og elektromagnetiske bølger?",
67  :   "hva er sammenhengen mellom frekvens, bølgelengde og bølgefart?",
68  :   "Hva er forskjellen på absorbsjons- og emisjonsspekter?",
69	:	"Forklar transmisjon, refleksjon, absorbsjon og emisjon av lys	"	,	
70	:	"Forklar kort om de ulike delene av det elektromagnetiske spekteret	"	,	
71	:	"Forklar grovt fysikken bak drivhuseffekten	"	,		
72	:	"Hvilke typer stråling har energi til å eksitere elektroner og hvilke har energi til å løsrive de helt?	"	,
73	:	"Hva er et sort legeme?	",	
74  :   "nevn tre ulike drivhusgasser og forklar hvordan de påvirker spekteret vi får fra sola    "   ,
75  :   "Hva er utstrålingstetthet og hvordan kan vi anslå energien fra sola som treffer en kvadratmeter på jorda",
76  :   "Forklar forskjellen på emisjonsspekter fra gasser, væsker og faste stoffer   "   , 
77  :   "Hvordan avtar strålingstettheten fra en lyspære med avstand?",
78  :   "Hva er utstrålingstetthet og hvordan avhenger det av temperatur?",
79  :   "Hvordan avhenger forholdet mellom utstrålte bølgelengder med overflatetemperatur?",
80  :   "Hva var resultatet av Youngs dobbelspalteeksperiment?",

81  :   "Hva besto Thompsons atommodell av og hvilken partikkel fant Thompson?",
82  :   "Fortell litt om Rutherfords atommodell, hvilken del av atomet fant han",	
83  :   "Hva sier Bohrs atommodell og hvilke prediksjoner gjør den om virkeligheten? ",
84  :   "Hvilke eksperimenter ble brukt til å påvise elektroner, atomkjernen og ionisering?",
85  :   "Hva var problemene som gjensto etter Bohr lanserte sin atommodell og vet du noe om veien videre?",
86  :   "Hva er et foton og hva er energien?",
87  :   "Hva kan eksitere elektroner og hvilke energinivåer svarer ofte til synlig lys?",

88  :   "Hvilke deler består et atom av?",
89  :   "Hva betyr nukleon, nuklide og isotop?",
90  :   "Forklar forholdet mellom kreftene i atomkjernen",
91  :   "Hva sier Einsteins berømte ligning E=mc^2",
92  :   "Hva er bindingsenergi og hvor i periodesystemet er denne høy og lav?",
93  :   "Hva er en kjernereaksjonsligning og hvilke bevaringslover gjelder der?",
94  :   "Hva er karbon 14 og hvordan kan vi avgjøre alder av biologiske gjenstander med det? ",
95  :   "Hva er fusjon og fisjon?",
96  :   "Hvordan er forholdet mellom nøytroner og protoner i kjernen når vi beveger oss oppover i periodesystemet?",
97  :   "Hvordan kan vi få energi ut av et kjernekraftverk og hvilke former er energien i?",
98  :   "Hva er et nøytrino og hva er et positron?",
99  :   "Hva er radioaktiv stråling og hvorfor er navnet litt misvisende?",
100 :   "Hva skjer med en atomkjerne som sender ut alfa, beta eller gamma stråling?",

101 :   "Hva er skjer med små, middels og store stjerner når de dør?",
102 :   "Hvor og når blir de ulike stoffene i periodesystemet dannet?",
103 :   "Hva er HR-serien og hva forteller den om stjerners livssyklus?",
104 :   "Hvilke krefter virker inni en stjerne?",
105 :   "Hvordan kan vi måle overflatetemperatur og avstand til stjerner lagt unna?",
}


hard_questions={}

while len(list(questions.keys()))>0:
    a=rd.choice(list(questions.keys()))
    print("__________________________________________________________________")
    print(questions[a][0:-1])
    print("")
    answer=input("kan du denne? - Skriv ja, nei, avslutt eller slumre:\n\n")
    if answer.lower()=="ja" or answer.lower()=="j":
        print("\nBra, neste spørsmål kommer her..\n")
        questions.pop(a)
    elif answer.lower()=="nei" or answer.lower()=="n":
        print("\nOkey, da legger jeg dette spørsmålet i listen av ting du må øve på..\n")
        hard_questions[a]=questions.pop(a)[0:-1]
    elif answer.lower()=="avslutt":
        break
    else:
        print("\nAntar du mener slumre, legger tilbake og trekker et nytt..\n")
print("")
print("Må øve mer på disse:\n")
print("\n" + "\n".join(f"    {repr(k)}: {repr(v)}" for k, v in hard_questions.items()) + "\n")
        
    
