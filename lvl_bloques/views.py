from django.shortcuts import render

def todos(request):

    all = {
           "nombre1":"Items De Hierro",
           "nombre2":"Items Con Obsidiana",
           "nombre3":"Items Caros",
           "img1":"../static/images/hierro_bloque.png",
           "img2":"../static/images/obsi_llorosa.png",
           "img3":"../static/images/netherita.png"
           }    
    
    return render(request, 'lvl_bloques/index.html',all)

def bloque_Hierro(request):

    iron = {
            "nombre":"Bloque De Hierro",
            "nivel":"3,648",
            "expansion":"140 x 140",
            "img":"../static/images/hierro_bloque.png",

            "otros1":"Puerta Hierro",
            "nivel1":"1,260",
            "img1":"../static/images/iron_door.png",

            "otros2":"Yunque",
            "nivel2":"1,151",
            "img2":"../static/images/anvil.png"
            }
    
    return render(request,'lvl_bloques/bloque.html',iron)

def obsidiana_Llorosa(request):

    obsidiand = {
                 "nombre":"Obsidiana Llorosa",
                 "nivel":"7,300",
                 "expansion":"140 x 140",
                 "img":"../static/images/obsi_llorosa.png",

                 "otros1":"Obsidiana",
                 "nivel1":'"Aun no es calculado"',
                 "img1":"../static/images/obsidiand.png",
 
                 "otros2":"Faros",
                 "nivel2":"2,045",
                 "img2":"../static/images/beacon.png"
                 }
    
    return render(request, 'lvl_bloques/bloque.html',obsidiand)

def bloques_caros(request):

    caros = {
             "nombre":"Bloque De Netherita",
             "nivel":"72,512",
             "expansion":"140 x 140",
             "img":"../static/images/netherita.png",

             "otros1":"Bloque De Diamante",
             "nivel1":"10,418",
             "img1":"../static/images/diamond.png",

             "otros2":"Bloques De Esmeralda",
             "nivel2":"6,290",
             "img2":"../static/images/emerald.png"
             }
    
    return render(request,'lvl_bloques/bloque.html',caros)
