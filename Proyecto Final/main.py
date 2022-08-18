
Aliemtentos=[]
canasta=[]
deuda=()
Pan=5
doritos=5
huelistas=5
papa_fritas=5
agua=5
platanos_verde=5
platanos_maduro=5
chocolate=5
malta_morena=5
choco_rica=5


def volver():
  pagar()
def lista():
  opciones=int(input("✩Maquina Dispensadora Edo✩\n\n***Alimentos Disponibles***\n1.Chocolate🍫 35$\n2.Choco-Rica🧃 40$\n3.Papas fritas🍟 50$\n4.Agua🥤 15$\n5.Pan🍞 10$\n6.Platanitos maduros🍌 35$\n7.Platanitos verdes🍌 35$\n8.Doritos🍟 35$\n9.Hojuelistas🍟 20$\n10.Malta Morena🥤 40$\n¿Que Opcion deseas comprar?\nDigite->"))
  if opciones==1:
    Aliemtentos.append(f"{chocolate-1} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} platanos maduros,{platanos_verde} platanos verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Chocolate🍫")
    pagar()
  if opciones ==2:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica-1} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Choco Rica🧃")
    pagar()
    
  if opciones ==3:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas-1} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Papas fritas🍟")
    pagar()
    
  if opciones ==4:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua-4} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Agua🥤")
    
    pagar()
  if opciones ==5:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan-1} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Pan🍞")
    
    pagar()
  if opciones ==6:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro-1} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Platanos maduros🍌")
    
    pagar()
  if opciones ==7:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde-1} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Platanos verdes🍌")
  
    pagar()
  if opciones ==8:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos-1} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Doritos🍟")
    
    pagar()
  if opciones ==9:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas-1} Hojuelistas,{malta_morena} Malta Morena")
    canasta.append("Hojuelistas🍟")
    
    pagar()
  if opciones ==10:
    Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena-1} Malta Morena")
    canasta.append("Malta Morena🥤")
    pagar()
  if opciones>10: 
    print("Esa Opcion no existe.")
def pagar():
  dinero=int(input("Solo se pude pagar con monedas de 5,10 & 25 o puedes pagar con billetes de 50,100 & 200\nDigite->"))
  if dinero==5:
    print("No puedes pagar")
  if dinero==10:
    print("Solo puedes comprar:\n5.nPan 10$")
    p1=int(input("1.Pagar 2.salir\n->"))
    compra_inventario()

    if p1 ==1:
      Aliemtentos.append(f"{chocolate} Chocolate,{choco_rica} Choco rica,{papa_fritas} papa fritas,{agua} Agua,{Pan-1} panes,{platanos_maduro} plaranos maduros,{platanos_verde} Platanos Verdes,{doritos} doritos,{huelistas} Hojuelistas,{malta_morena} Malta Morena")
      canasta.append("Pan🍞")
    else:
      print("Has salido.")
  if dinero==25:
    print("Solo puedes comprar:\n4.Pan 10$\n4.Agua🥤 15$\n9.Hojuelistas🍟 20$")
    p2=int(input("1.Comprar Pan.\n2.Comprar agua.\n3.comprar hojuelistas.\n->"))
    if p2==1:
      print(f"Le ha sobrado: {dinero-10}")
    if p2==2:
      print(f"Le ha sobrado: {dinero-15}")
    if p2==3:
      print(f"Le ha sobrado: {dinero-20}")
    else:
      print("Esta opcion no existe.")
  if dinero==50:
    compra_inventario() 
  if dinero==100:
    compra_inventario()
  if dinero==200:
    compra_inventario()
  if dinero>200:
    print("Ese billete o moneda no se acepta aqui.")
def compra_inventario():
  print(f"Has comprado:{canasta}") 
  print(f"Quedan disponibles:\n{Aliemtentos}")
  print("Has pagado con correctamente.")
    
 
  

lista()




  
 