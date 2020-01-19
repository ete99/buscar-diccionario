import urllib.request
import unicodedata
import time

#salta hasta el primer try/catch




def ilizq(t):
    i=0
    x=-1
    for v in range(len(t)):
        if t[i] == 'o' and t[i + 1] == 'n' and t[i + 2] == '"'and t[i + 3] == '>':
            x=i+4
            break
        i+=1
    return x

def ilder(t):
    i=0
    x=-1
    for v in range(len(t)):
        if t[i] == '.' and t[i + 1] == '<' and t[i + 2] == '/'and t[i + 3] == 's':
            x=i+1
            break
        i+=1
    return x

def illus(t):
    aux=''
    xd=''
    ini=ilizq(t)
    fin=ilder(t)
    for i in range(ini,fin):
        xd=xd+t[i]
    xd= 'Ejemplo: "' + xd + '"'
    for i in range(0, ini):
        aux=aux+t[i]
    '''
        for i in range(fin+1, len(t)):
        aux=aux+t[i]
        pos+=1
    '''
    aux=aux + xd
    return aux

def hayp(t):
    c=0
    x = -1
    for i in range(len(t)):
        if t[i] == '<':
                x = c
        c+=1
    return x

def pder(t):
    c=0
    x=-1
    for i in range(len(t)):
        if t[i] == 'i':
            if t[i+1] == '>':
                x = c
                break
        c+=1
    return x

def pderr(t):
    x=-1
    for i in range(len(t)):
        if t[i] == '>':
            x = i
            break
    return x

def pdersp(t):
    c=0
    x=-1
    for i in range(len(t)):
        if t[i] == '>':
            x = c
            break
        c+=1
    return x

def noSpan(t):
    aux=''
    error=0
    primero=1
    #while hayp(aux) != 0 and error<100 or primero==1:
    #if hayp(aux)!=-1:
    pos=0
    primero=2
    error+=1
    ini=pizq(t)
    fin=pdersp(t)
    for i in range(0,ini):
        aux=aux+t[i]

        pos += 1
    for i in range(fin+1, len(t)):
        aux=aux+t[i]
        pos+=1
    return aux

def noSpanf(t):
    aux=''
    error=0
    primero=1
    #while hayp(aux) != 0 and error<100 or primero==1:
    #if hayp(aux)!=-1:
    pos=0
    primero=2
    error+=1
    ini=pfizq(t)
    fin=pdersp(t)
    for i in range(0,ini):
        aux=aux+t[i]
        pos += 1
    for i in range(fin+1, len(t)):
        aux=aux+t[i]
        pos+=1
    return aux

def realNoSpan(t):
    aux=t
    while hayp(aux)!=-1:
        if(pizq(aux)!=-1):
            aux=noSpan(aux)
        else:
            aux=noSpanf(aux)
    return aux


def pizq(t):
    i=0
    x=-1
    for v in range(len(t)):
        if t[i] == '<':
            x=i
            break
        i+=1
    return x

def pfizq(t):
    i=0
    x=-1
    for v in range(len(t)):
        if t[i] == '<':
            x=i
            break
        i+=1
    return x

def limpiar_resp(respuesta):
    cont = 0
    txt = ''
    res = ''
    ini = fin = 0
    for i in range(len(respuesta)):
        if respuesta[i] == 'd':
            if respuesta[i + 1] == 's':
                if respuesta[i + 2] == '-':
                    ini = 1
        if respuesta[i] == 'r':
            if respuesta[i+1] == 'u':
                if respuesta[i+2] == 'n':
                    ini = 1
        if ini == 1:
            if respuesta[i] == '<' and respuesta[i + 1] == '/' and respuesta[i + 2] == 'd':
                break
            else:
                txt = txt + respuesta[i]
    if pderr(txt) != -1:
        cont = pderr(txt) + 1

    for i in range(cont, len(txt)):
        res = res + txt[i]
    if ilizq(res) != -1:
        res = illus(res)
    res=realNoSpan(res)
    return res

# **************************************** Desde aca comenza a leer ****************************************


# El programa busca el significado de palabras y guarda en un archivo
try:
    '''
    Aca leia un archivo con varias palabras, por eso el try/catch de arriba
    #with open("palabras.txt") as f:
    #   mylist = f.read().splitlines()
    '''
    
    cant = 0
    mylist = ["hola", "agua", "termo"]  # lista de palabras a buscar su significado
    for i in range(0, len(mylist)):

        try:
            respuesta=''
            res = ''
            pal = mylist[i]
            pal= unicodedata.normalize('NFKD', pal).encode('ascii', 'ignore')  
            pal = pal.decode('utf-8')  # normaliza la palabra, quitando acentos y eso
            url = 'https://es.thefreedictionary.com/' + pal
            # headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'  # esto era para pasar unas cosas de seguridad que no hacen falta
            try:
                req = urllib.request.Request(url)
                resp = urllib.request.urlopen(req)  # .decode('utf-8')

                respuesta = resp.read().decode('utf-8')
                res = limpiar_resp(respuesta)  # limpia para sacar solo los significados del html

            except Exception as e:
                print(str(e), "No se pudo cargar a la pagina")
                
            finally:
                nro_de_pal = str(cant+1)
                res = nro_de_pal + '-' + pal + '-' + res + '\n'
                print(res)
                saveFile = open('significados.txt', 'a')  # Abre para actualizar o creo si no existe un archivo para guardar los significados
                saveFile.write(res)  # Escribe los significados en el archivo
                saveFile.close()  # cierra el archivo
            time.sleep(4)  # pone a dormir por un tiempo, pq habia errores si spameabas
        except Exception as e:
            print(str(e))
        finally:
            cant=cant+1  # aumenta el nro de palabras encontradas
except Exception as e:
    print(str(e))
