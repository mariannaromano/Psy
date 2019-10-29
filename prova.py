import xml.etree.ElementTree as ET
import fileinput
import os,sys,time
import uuid
import os.path
from os import path
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
file="Items.xml"
count=0

def ttoggle(value):
    value=str(not eval(value))
    return value

class Titolo:
    
    def __init__(self):
        global count
        self.id= count
        count=count+1
        self.title=""
        self.done=False
        self.timestamp= time.time()        
    def add(self):
        if path.exists(file):
            tree = ET.parse(file)
            root=tree.getroot()
            item = ET.Element('item')
            itemid=ET.SubElement(item, 'id')
            itemid.text = str(self.id)
            titolo = ET.SubElement(item, 'titolo')
            titolo.text = self.title 
            timestamp = ET.SubElement(item, 'timestamp')
            timestamp.text = str(self.timestamp)
            done=ET.SubElement(item, 'done')
            done.text=str(self.done)
            root.append(item)
            tree.write(file)
        else:
            root= ET.Element('ITEMS')
            item = ET.SubElement(root,'item')
            itemid=ET.SubElement(item, 'id')
            itemid.text = str(self.id)
            titolo = ET.SubElement(item, 'titolo')
            titolo.text = self.title 
            timestamp = ET.SubElement(item, 'timestamp')
            timestamp.text = str(self.timestamp)
            done=ET.SubElement(item, 'done')
            done.text=str(self.done)
            tree = ET.ElementTree(root)
            tree.write(file)
    def delete(self):
        if path.exists(file):
            tree = ET.parse(file)
            root=tree.getroot()
            items= tree.findall('item')
            for item in items:
                if (item[0].text==str(self.id)):
                    root.remove(item)
            tree.write(file)
        else:
            print ("file non trovato")            
    def replace(self,stringrep):
        if path.exists(file):
            tree = ET.parse(file)
            root=tree.getroot()
            items= tree.findall('item')
            for item in items:
                if (item[0].text==str(self.id)):
                    item[1].text= stringrep
            tree.write(file)
        else:
            print ("file non trovato")
    def toggle(self):
        if path.exists(file):
            tree = ET.parse(file)
            root=tree.getroot()
            items= tree.findall('item')
            for item in items:
                if (item[0].text==str(self.id)):
                    item[3].text= ttoggle(item[3].text)
            tree.write(file)
        else:
            print ("file non trovato")




            

def main():
    print ("Prova ")
    os.system("cls")
       

    while True :
        try:   
            partet=input ("Cosa vuoi fare?")                  
            if  partet[:1] == "h":   #h >>> mostra tutti le possibili action"    
                print ("ls >>> mostra tutti i todos ordinati per data di inserimento decrescente")
                print ("a (params: title) >>> aggiunge un todo")
                print ("e (params: id, title) >>> edita un todo")
                print ("d (params: id) >>> cancella un todo")
                print ("t (params: id) >>> fa il toggle del todo (done: true VS done: false)")
                print ("s (params: il termine da cercare) >>> cerca tra i todos e ritorna i todos contenenti il termine ricercato nel titolo")
                  
            elif partet == "ls": #ls >>> mostra tutti i todos ordinati per data di inserimento decrescente
                if path.exists(file):
                    tree = ET.parse(file)
                    root=tree.getroot()
                    children = root.getchildren()
                    for child in children:
                        print(child[0].text +" "+ child[1].text+" "+child[2].text+" "+child[3].text )
                else:
                     print ("file non trovato")
            elif partet[:1] == "a": #a (params: title) >>> aggiunge un todo
                a,tit = partet.split()            
                myobjectx = Titolo()
                myobjectx.title=tit
                myobjectx.add()               
            elif partet[:1] == "e": #e (params: id, title) >>> edita un todo
                a,id,strtit = partet.split()
                myobjectx = Titolo()
                myobjectx.id=id
                myobjectx.replace(strtit)
            elif partet[:1] == "d": #d (params: id) >>> cancella un todo
                a,id = partet.split()
                myobjectx = Titolo()
                myobjectx.id=id
                myobjectx.delete()
            elif partet[:1] == "t": #t (params: id) >>> fa il toggle del todo (done: true VS done: false)
                a,id = partet.split()
                myobjectx = Titolo()
                myobjectx.id=id
                myobjectx.toggle()                
            elif partet[:1] == "s": #s (params: il termine da cercare) >>> cerca tra i todos e ritorna i todos contenenti il termine ricercato nel titolo
                a,search = partet.split()
                if path.exists(file):
                    tree = ET.parse(file)
                    root=tree.getroot()
                    items= tree.findall('item')
                    for item in items:
                        if (search in item[1].text):
                            print(item[0].text +" "+ item[1].text+" "+item[2].text+" "+item[3].text )                   
                else:
                    print ("file non trovato")
            elif partet == "4":
                os.system("cls")
                print ("Stai per uscire!")
                os.remove(file)            
                sys.exit()
            else:
                os.system("cls")
                print ("Input non valido")                
                os.system("cls")
        except(Exception):
             print ("Input non valido"  )
             
if __name__ == "__main__":
    main()
        
        
        
    
