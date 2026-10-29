# Contenido de la demo Hotel Alameda Palace (Salamanca) (es/ca/en/fr). Hechos de hotelalamedapalace.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble cama de matrimonio','Doble de 2 camas','Suite'],
'ca':['Doble de llit de matrimoni','Doble de 2 llits','Suite'],
'en':['Double with a double bed','Twin room','Suite'],
'fr':['Double à lit double','Double à 2 lits','Suite']}
RD={
'es':['Hasta 2 personas, con una cama doble de 150 cm, wifi gratuita, TV, minibar, ventanas insonorizadas y caja fuerte.','Hasta 2 personas, 20 m², con dos camas individuales que pueden estar juntas o separadas, según disponibilidad.','Hasta 2 personas, 40 m², con sala de estar, bañera de hidromasaje y servicio de habitaciones.'],
'ca':['Fins a 2 persones, amb un llit doble de 150 cm, wifi gratuïta, TV, minibar, finestres insonoritzades i caixa forta.','Fins a 2 persones, 20 m², amb dos llits individuals que poden estar junts o separats, segons disponibilitat.','Fins a 2 persones, 40 m², amb sala d\'estar, banyera d\'hidromassatge i servei d\'habitacions.'],
'en':['Up to 2 guests, with a 150 cm double bed, free wifi, TV, minibar, soundproof windows and a safe.','Up to 2 guests, 20 m², with two single beds that can be together or apart, depending on availability.','Up to 2 guests, 40 m², with a living area, hydromassage bathtub and room service.'],
'fr':['Jusqu\'à 2 personnes, avec un lit double de 150 cm, wifi gratuit, TV, minibar, fenêtres insonorisées et coffre-fort.','Jusqu\'à 2 personnes, 20 m², avec deux lits simples pouvant être joints ou séparés, selon disponibilité.','Jusqu\'à 2 personnes, 40 m², avec salon, baignoire d\'hydromassage et service en chambre.']}
ART={
'hero':('arches',9801,['#efe0c8','#d6b27c','#a98235','#7a2d3b','#4f1a26']),
'intro':('columns',9802,['#f0e2ca','#f6ead4','#b08d3c','#8a3a49','#4f1a26']),
'r1':('arches',9811,['#efe1c9','#d8b57f','#a77f33','#74293a','#4a1823']),
'r2':('columns',9812,['#ede0c7','#f5e9d3','#b38f3e','#823647','#531d29']),
'r3':('skyline',9813,['#3d2b47','#e8935f','#fbd9a0','#3b2a45','#2b1e35','#1c1424']),
'g1':('arches',9821,['#f1e3ca','#dbb985','#a98234','#7a2d3d','#4e1a26']),
'g2':('skyline',9822,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('columns',9823,['#eee0c6','#f5e9d2','#b08d3c','#8c3d4c','#561f2c']),
'g4':('hills',9824,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',9825,['#f0e2ca','#d9b680','#a98233','#772c3c','#4d1a25']),
'g6':('skyline',9826,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Alameda Palace · Hotel de 5 estrellas en el Palacete de los Prada, Salamanca',see_rooms='Ver habitaciones',hero_k='Salamanca · Paseo de la Estación',hero_t='Historia y confort en el corazón de Salamanca',hero_s='Un hotel de 5 estrellas en el antiguo Palacete de los Prada, a 10 minutos a pie de la Plaza Mayor.',
 intro_t='Tradición y elegancia en un antiguo palacete',intro_p1='El Hotel Alameda Palace ocupa el antiguo Palacete de los Prada, en el Paseo de la Estación 1, con 103 habitaciones de 7 tipos.',
 intro_p2='Tiene restaurante, salones para bodas y eventos, y una ubicación a 10 minutos a pie de la Plaza Mayor, la Universidad y las Catedrales. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['5 estrellas','103 habitaciones','Restaurante Venecia','Salones y eventos'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Restaurante Venecia','Bodas y eventos','Wifi gratuita','Caja fuerte en todas las habitaciones','Servicio de habitaciones en las suites','Ventanas insonorizadas','Minibar','Club Alameda Palace Rewards'],
 loc_p='Paseo de la Estación 1, 37004 Salamanca.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay restaurante?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Alameda Palace · Hotel de 5 estrelles al Palauet dels Prada, Salamanca',see_rooms='Veure habitacions',hero_k='Salamanca · Paseo de la Estación',hero_t='Història i confort al cor de Salamanca',hero_s='Un hotel de 5 estrelles a l\'antic Palauet dels Prada, a 10 minuts a peu de la Plaza Mayor.',
 intro_t='Tradició i elegància en un antic palauet',intro_p1='L\'Hotel Alameda Palace ocupa l\'antic Palauet dels Prada, al Paseo de la Estación 1, amb 103 habitacions de 7 tipus.',
 intro_p2='Té restaurant, salons per a noces i esdeveniments, i una ubicació a 10 minuts a peu de la Plaza Mayor, la Universitat i les Catedrals. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['5 estrelles','103 habitacions','Restaurant Venecia','Salons i esdeveniments'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Restaurant Venecia','Noces i esdeveniments','Wifi gratuïta','Caixa forta a totes les habitacions','Servei d\'habitacions a les suites','Finestres insonoritzades','Minibar','Club Alameda Palace Rewards'],
 loc_p='Paseo de la Estación 1, 37004 Salamanca.',
 chips=['Quantes habitacions té?','Hi ha restaurant?','On és?','Com es reserva?']),
'en':dict(title='Hotel Alameda Palace · 5-star hotel in the Prada Mansion, Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Paseo de la Estación',hero_t='History and comfort in the heart of Salamanca',hero_s='A 5-star hotel in the former Prada Mansion, a 10-minute walk from the Plaza Mayor.',
 intro_t='Tradition and elegance in a former mansion',intro_p1='Hotel Alameda Palace occupies the former Prada Mansion at Paseo de la Estación 1, with 103 rooms of 7 types.',
 intro_p2='It has a restaurant, rooms for weddings and events, and a location 10 minutes on foot from the Plaza Mayor, the University and the Cathedrals. To book, contact the hotel by phone or email.',
 stats=['5 stars','103 rooms','Venecia restaurant','Event rooms'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Venecia restaurant','Weddings and events','Free wifi','Safe in every room','Room service in the suites','Soundproof windows','Minibar','Club Alameda Palace Rewards'],
 loc_p='Paseo de la Estación 1, 37004 Salamanca.',
 chips=['How many rooms does it have?','Is there a restaurant?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Alameda Palace · Hôtel 5 étoiles dans le Palacete de los Prada, Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Paseo de la Estación',hero_t='Histoire et confort au cœur de Salamanque',hero_s='Un hôtel 5 étoiles dans l\'ancien Palacete de los Prada, à 10 minutes à pied de la Plaza Mayor.',
 intro_t='Tradition et élégance dans un ancien palacete',intro_p1='L\'Hotel Alameda Palace occupe l\'ancien Palacete de los Prada, au Paseo de la Estación 1, avec 103 chambres de 7 types.',
 intro_p2='Il dispose d\'un restaurant, de salons pour mariages et événements, et d\'un emplacement à 10 minutes à pied de la Plaza Mayor, de l\'Université et des Cathédrales. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['5 étoiles','103 chambres','Restaurant Venecia','Salons et événements'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Restaurant Venecia','Mariages et événements','Wifi gratuit','Coffre-fort dans chaque chambre','Service en chambre dans les suites','Fenêtres insonorisées','Minibar','Club Alameda Palace Rewards'],
 loc_p='Paseo de la Estación 1, 37004 Salamanque.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un restaurant ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='recepcion@hotelalamedapalace.com')
D=dict(name='Hotel Alameda Palace',ac='#5a1f2b',ac2='#b08d3c',ac2_a11y='#7a5c12',book=BOOK,around=[],foot=FOOT,
 address='Paseo de la Estación 1 · 37004 Salamanca',phones=['923 28 26 26'],emails=['recepcion@hotelalamedapalace.com'],maps='Hotel Alameda Palace, Paseo de la Estación 1, Salamanca',t=T)
META=dict(repo='demo-hotel-alameda-palace-salamanca',name='Hotel Alameda Palace',legal_name='HOTALPA S.L.',registry_ids=['CIF B83867515'],
 url='https://www.hotelalamedapalace.com/',domain='hotelalamedapalace.com',municipality='Salamanca',province='Salamanca',sector='hotel de 5 estrellas en un antiguo palacete',
 read_at='2026-10-29T05:40:00+01:00',created_at='2026-10-29T05:42:00+01:00',built_at='2026-10-29T05:43:00+01:00',audit_date='2026-10-29T05:42:00+01:00',
 rating=dict(value=4.2,coincide=['telefono','web'],date='2026-10-29T04:55:01+01:00',url='https://www.google.com/maps/place/Hotel+Alameda+Palace/@40.9689255,-5.6577396,17z/data=!4m9!3m8!1s0xd3f26104adbadfd:0xafd5263150aeb6ad!5m2!4m1!1i2!8m2!3d40.9689255!4d-5.6577396!16s%2Fg%2F1tf5lyz1'),
 book=dict(mode='mail',email='recepcion@hotelalamedapalace.com',note='La web del negocio tiene su propio motor de reservas cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay restaurante?','K03'),('¿Tienen salones para eventos?','K04'),('¿Dónde está el hotel?','K05'),('¿Qué historia tiene el edificio?','K06'),('¿Qué hay para visitar cerca?','K07'),('¿Cómo reservo?','K08'),('¿Cuál es el teléfono?','K09'),('¿Quién es el titular?','K10'),('¿Hay parking?',None),('¿Hay desayuno?',None),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Tienen suites?','K01')],
'ca':[('Quantes habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha restaurant?','K03'),('Teniu salons per a esdeveniments?','K04'),('On és l\'hotel?','K05'),('Quina història té l\'edifici?','K06'),('Què hi ha per visitar a prop?','K07'),('Com reservo?','K08'),('Quin és el telèfon?','K09'),('Qui és el titular?','K10'),('Hi ha pàrquing?',None),('Hi ha esmorzar?',None),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Teniu suites?','K01')],
'en':[('How many rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there a restaurant?','K03'),('Do you have event rooms?','K04'),('Where is the hotel?','K05'),('What history does the building have?','K06'),('What is there to visit nearby?','K07'),('How do I book?','K08'),('What is the phone number?','K09'),('Who is the owner?','K10'),('Is there parking?',None),('Is there breakfast?',None),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K08'),('Do you have suites?','K01')],
'fr':[('Combien de chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un restaurant ?','K03'),('Avez-vous des salons pour événements ?','K04'),('Où est l\'hôtel ?','K05'),('Quelle histoire a le bâtiment ?','K06'),('Que visiter à proximité ?','K07'),('Comment réserver ?','K08'),('Quel est le téléphone ?','K09'),('Qui est le titulaire ?','K10'),('Y a-t-il un parking ?',None),('Y a-t-il un petit-déjeuner ?',None),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Avez-vous des suites ?','K01')]}
