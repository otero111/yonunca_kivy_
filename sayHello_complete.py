from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random



word = [
"Nunca he vuelto con mi ex.",
" He mandado nudes.",
" He aparentado no  estar borracho para no discutir con mi madre.",
" Yo nunca me he liado con el ex de un amig@",
"  he escrito a mi ex una noche de fiesta",
"  he fingido que me llamaban para escapar de una cita o lugar",
" he estado más de tres días sin ducharme ",
" me he imaginado siendo del sexo opuesto ",
"  he  perdido un movil",
"  mentí en el Yo Nunca",
"  he estornudado y me ha salido un moco",
"  he indicado mal un camino cuando me han preguntado",
"  he olido mi propio pedo",
"  he intentado mover cosas con la mente (sin resultado)",
"  he mirado el papel después de ir al baño",
" he mandado un audio \n subidito de tono a mi madre por error", 
" he amanecido en un parque borracho", 
"He salido con ropa interior rota", 
"He pasado pena al \n acostarme con alguien desconocid@", 
"Me fugue de la escuela", 
"Hice fraude", 
"He tratado de entrar \n al Facebook de alguien", 
"He visto desnud@ por error a alguien", 
"No me he confundido de \n contacto en WhatSapp y le he dicho algo ofencivo", 
"He visto porno", 
"He sido infiel", 
" He pensado que nadie me quiere", 
"He intentado suicidarme", 
"Nunca he mirado escondido a \n alguien mientras se cambiaba", 
"He pasado años atras de una\n persona y no le dije que me gustaba", 
"He hecho un baile sexy \n para alguien en \n las redes", 
"He he sentido atraid@ ,\n  por alguien con quien chateo  \n en las redes", 
"He estado detenido", 
"Me he mojado la punta de los labios \n para aparentar que estoy \n tomando porque estoy borracho", 
"He sido estafado", 
"He publicado por equivocacion \n una foto comprometedora", 
"He dicho que voy a casa  \n de un@ amig@ para\n escaparme de fiestas", 
"Me he ido sin pagar de un lugar \n (por equivocacion o a proposito)", 
"He visto a dos amigos \n mios teniendo sexo", 
"He follado en publico", 
"He usado ropa del sexo opuesto", 
"He ido a salir con un piquete \n y he regresado con otro", 
"Me he juntado con un piquete \n que ni conozco solo para  \n emborracharme y pasar la noche", 
"Me he masturbado en una casa agena", 
"He sido asaltad@", 
"Me he tocado el celular \n despues de tirarme un pedo para aparentar", 
"Me mirado hacia atras \n despues de tirarme un pedo", 
"He cagado en la calle", 
"Me he acostado con una \n persona mucho mayor que yo \n (+ de 20 años)", 
"He visto porno en la escuela",
"Yo nunca he aparentado \n estar tomando para que no vean \n que estoy borracho", 
"He sateado con mas de 2 personas \n a la vez por mensajes", 
"He mentido por amor ", 
"Tuve  una fantasía rara", 
"He traicionado a un amigo \n para beneficiarme", 
"Me he fijado en alguien que no debo", 
"He tenido un orgasmo", 
"He follado más de 3 veces seguidas ", 
"He estado con más de un@ \n chic@ en un día", 
"He hecho una orgía", 
"He tenido sexo oral",
"He tenido sexo anal", 
"Le he deseado la muerte alguien", 
"He sentido envidia", 
"Me he alegrado de la desgracia de alguien", 
"He fingido un orgasmo ", 
"He mentido a mi madre", 
"He deseado irme lejos por un tiempo", 
"He tenido ganas de morirme", 
"Me he sentido sol@", 
"He dudado de mi", 
"He fantaseado con alguien mientras  \n converso con esa persona", 
"He desconfiado de mis amistades", 
"He sentido vergüenza de mi cuerpo ", 
"He tenido complejos", 
"Me he enamorado", 
"Me he fijado en otra persona \n q no sea mi pareja ", 
"Me he sentido atraída por alguien \n del sexo opuesto", 
"Me he sentido atraíd@ por alguien del mismo sexo", 
"He fingido estar borracho", 
"He dejado tirado a alguien \n que me necesita", 
"He llegado tarde a una cita", 
"He tenido una experiencia \n sexual interesante", 
"He follado delante de alguien", 
"He follado con un familiar", 
"Me he enamorado de un familiar", 
"He tenido sexo en la escuela", 
"He sido humillado en publico", 
"Me he caido de la silla", 
"Me he caido en publico", 
"He llorado en publico", 
"Me he exitado pensando en cosas \n pervertidas en un luagr publico", 
"Le he hecho bromas \n pesadas a desconocidos", 
"He sentido curiosidad sobre \n que se siente estar con alguien de tu propio sexo", 
"Me he orinado mientras dormia \n despues de grande", 
"He visto porno gay", 
"He vendido algo ilegal", 
"Me he drogado", 
"He inventado excusas para no follar", 
"He matado a un familiar en \n las mentiras a los profesores", 
"Le dije compañera a un \n compañero sin querer",
"He sido estafado",
"me he excitado en público",
"he tenido sexo borracho",
"he deseado follar con más \n de una persona a la vez.",
"he pensado que soy mala hoja.",
"he tragado semen ",
"he salido con ropa interior rota.",
"he pensado en cosas hot\n estando rodeada de personas ", "tenido sexo en la playa.",
"he follado con mas de una persona \n un mismo día.",
"he pasado una pena en casa \n d la familia de mi pareja.",
"he hecho un papelazo borracho.",
"me he sentido atraído por alguien q no debo.",
"he tenido más de tres orgasmos en un día.",
"he tomado para emborracharme \n y dejar de sentir nervios.",
"me he embrrachado  en un lugar \n o momento q no debía ",
"he follado borracho",
"me he masturbado mientras chateo.",
"me he mojado por alguna situación \n ,estando en un lugar público .",
"he mentido sobre alguien para \n quedar bien yo.",
"he preferido a mi pareja antes \n de mis amistades.",
"he fantaseado con hacer una orgía ",
"me he imaginado soñando con un famoso.",
"he pasado una pena en el acto sexual.",
"me he mojado solo con un beso.",
"he jugado al yo nunca",
"he fingido estar borracho.",
"he mentido para ligar.",
"me he masturbado en una casa \n q no es la mía.",
"me he sentido atraíd@ por alguno \n de los presentes.",
"he fantaseado con alguien mayor q yo.",
"me he levantado mojad@.",
"he tenido un gatillazo haciendo el amor",
" he besado a una persona \n de mi mismo sexo",
"yo nunca he tenido ganas \n de acostarme con una amiga \n o amigo de mi novio o novia",
"He carecido de deseo sexual",
"He sido visto en el baño defencando",
"He mentido para encajar en un grupo",
"Le he contado algo a alguien \n y luego me he arrepentido",
"Me he bañado desnud@ en la playa",
"Me he enamorado de un familiar de mi novi@",
"Yo Nunca Me Eh Caído De La Cama",
"Yo nunca eh jugado de Mano \n con mi Novi@ En La Cama",
"Yo nunca he ayudado a un amigo \n a cubrir una infidelidad",
"Yo nunca he visto a mi herman@ desnud@",
"Yo nunca le he escupido en la cara a alguien",
"Yo nunca he dormido en la playa",
"Yo nunca he chupado sangre ",
"Yo nunca le he dicho a alguien: \n ¿te casarías conmigo?",
"Yo nunca he comido en \n clases a escondidas",
"Yo Nunca me había reído \n tan fuerte que me tirara un pedo",
"Yo Nunca he vomitado a un amigo",
"Nunca he revisado las redes \n para recordar la noche anterior.",
"Yo Nunca me he reído\n tan fuerte que oriné un poco ",
"Yo nunca he intentado bañarme en una fuente ",
"Yo nunca he intentado impresionar \n a alguien que me odia",
"A mí nunca se me ha caído \n algún objeto al inodoro ",
" he peleado porque se han \n comido algo mío ",
" me he sacado los mocos en público.",
" he sido arrestado",
" he comido una hormiga.",
" he sido perseguido por un perro. ",
" he cambiado un neumático de coche.",
" he sentido asco por besar al alguien",
"he comido una banana u otra fruta \n de forma sexy ",
"he buscado pornografía en internet ",
"he utilizado la foto de mi pareja \n como fondo de pantalla",
"he salido del baño mojad@ a \n cambiar un canción ",
"he mantenido una relación \n con alguien de otro país por interés",
"he metido los dedos en un tomacorrientes",
"Yo nunca he pagado por un \n masaje con final feliz, \n Te gustaria que alguno \n de los presentes te de uno? ",
"Yo nunca he discutido con mi suegra",
"Yo nunca he pensado meterme \n  un pepino en el ano",
"Yo nunca he mentido sobre mi virginidad",
"Yo nunca he pensado en alguien \n del mismo sexo para masturbarme \n sin ser homosexual",
"Yo nunca le pedido a mi novio \n que me folle por atrás ",
"Yo nunca he zorreado con el o la vecina ",
"Yo nunca he comparado en mi \n mente las vaginas o los penes d mis ex",
"Yo nunca me he acostado con hambre ",
"Yo nunca he dicho te amo a alguien",
"Nunca he ayudado a un/una \n amig@ a estar con alguien \n que tambien me gusta",
"Yo nunca he ofendido a alguien \n y me he arrepentido",
"Yo nunca he amado mucho a alguien ",
"Yo nunca he tenido sexo en una escalera",
"Yo nunca he pensado como follan mis amigos ",
"Yo nunca me he masturbado \n pensando en un@ de los presentes",
"Yo nunca me he hecho pasaron \npor otra persona y le he escrito \n a mi pareja",
"Yo nunca he escrito mi nombre \n en la mesa de un restaurante, \n cafetería, bar",
"Yo nunca he subido fotos hot \n a las redes para que me \n den like y comenten",
"Yo nunca me he metido un lápiz en el oído ",
"A mí nunca se me ha ofrecido \n la o el ex de un amig@ ",
"Yo nunca he tenido pensamientos \n  eróticos con alguien que acabo \n de ver en la calle ",
"Yo nunca he creado mi propia bebida especial",
"Yo nunca he pensado que no voy \n a madurar nunca ",
"Yo nunca he esperado a que \n la fiesta termine para poder \n llevarme los globos",
"Yo nunca he cocinado desnud@",
"Yo nunca he tenido relaciones sexuales con un extrañ@ sin condon",
"Yo nunca he estado de mal humor por llevar tiempo sin follar ",
"Yo nunca he mantenido un tatuaje en secreto",
"Yo nunca perdido pelo por la ansiedad ",
"Yo nunca le he cobrado a mis padres por hacer tareas",
"Yo nunca he tenido relaciones con mi herman@",
"Yo nunca me he ahogado tomando ron",
"Yo nunca he forzado a mi pareja a tener sexo",
"Yo nunca he usado rompa interior del sexo contrario",
"Yo nunca me he grabado follando",
"Yo nunca me he grabado masturbandome",
"Yo nunca he follado con alguien por un reto",
"Yo nunca he hecho un trío por un reto",
"Yo nunca he odiado a mi cuñado",
"Yo nunca he mantenido una relación por un buen tiempo con una persona que conocí por redes",
"Yo nunca he ofendido mucho a alguien y después me he arrepentido mucho",
"Yo nunca estaba chismeando por la ventana y me cogieron",
"Yo nunca dije estar con la regla para no tener sexo",
"Yo nunca rechacé a alguien porque siempre olía mal",
"Yo nunca me he sentido inseguro de mi mismo",
"Yo nunca evité a toda costa responder a una pregunta",
"Yo nunca he guardado un secreto que me ha estado consumiendo por mucho tiempo",
"Yo nunca le hice sexo oral a mi pareja cuando alguien estaba muy cerca",
"Yo nunca me puse de mal humor por no llegar al orgasmo",
"Yo nunca he he querido ver a mi prim@ desnud@ ",
"Nunca me ha gustado una persona menor de edad",
"Yo nunca he terminado follando con alguien que al inicio de conocerl@ me ha caído muy mal",
"Yo nunca he querido ser muy popular",
"Yo nunca me he desmotivado de lograr un sueño",
"Yo nunca he salido con alguien solo porque tiene mucho dinero",
"Yo nunca he sido la persona q vive poniendo estados en whatsspp a toda hora",
"Yo nunca he salido sin ropa interior a la calle ",
"Yo nunca he peleado por un pedazo de pizza",
"Yo nunca he caminado descalz@ por la calle tras haber roto mis zapatos",
"Yo nunca me he orinado de la risa",
"Yo nunca he tropezado en la calle frente a todos",
"Yo nunca he llorado frente a todos",
"Yo nunca he besado a una mascota en la boca ",
"Yo nunca me enamoré de mi mejor amig@ ",
"Yo nunca miré la Polla de mi amigo mientras meábamos para saber si la tenia más grande que yo...",
" me he excitado con una mirada.Explica como fue ,que sientes",
 " he tenido un orgasmo mientras duermo.Describe la sensación",
 " he sentido excitación mientras veo porno de dos personas del mismo sexo , Explícate",
 " me he mojado con solo leer algo que me han escrito.",
 " me he acostado con alguien sin que me guste ,solo por pena .",
 " me he tocado yo misma creyendo que lo hace otra persona.",
 " me he excitado viendo cómo mi pareja se masturba.",
 " me he excitado viendo a mi pareja observando mineras me tocó",
"Yo nunca he hablado mal de alguien para quedar bien yo",
" he dejando mis sentimientos a un lado para no herir a otras personas",
" me he imaginado haciendo un trio",
"me he excitado porque me toquen la cintura",
 "he sentido ganas de tener sexo estando en un lugar público",
 "he usado juguetes sexuales",
 "he sentido atracción por alguien de mi mismo sexo",
 "me he masturbado mientras chateo",
 "he querido tener sexo salvaje",
 "he sentido ganas de follarme a un/una profe",
 "he estado más de 3 días sin apetito sexual",
 "he fingido un orgasmo",
 "he follado en una cocina",
 "he tragado semen",
 "he hecho una orgia",
'''Bonus .Tomate un trago y 
cuéntanos en qué piensas mientras 
te masturbas''',
'''Bonus .Toma un trago y dinos
 si te gustaría hacer un trio ,
 de qué tipo y por qué ?''',
'''Bonus .Tomate un trago y dinos
si tienes ganas de follarte a 
alguien ahora mismo 
y en dónde te gustaría hacerlo''',
"Bonus .Toma y di que es lo que más te excita de follar",




]
result = []


class SayHello(App):
    
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
                        text= "Bienvenido. Tiene que tomar un trago por cada cosa que SI haya hecho",
                        font_size='10sp',
                        color= '#00FFCE',
                        
                        
                       
                        
                        )
        self.window.add_widget(self.greeting)
        self.size_hint = (1, 0.8)

       

        # button widget
        self.button = Button(
                      text= "Proximo",
                      size_hint= (0.8,0.2),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
 

        return self.window

    
    def callback(self,intance):
        try:
        
            element = random.choice(word)
     
        
            self.greeting.text = str(element)
            word.remove(element)
        except:
            self.greeting.text = "Fin"
        
        
        
        
        
        
    
        
     

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
