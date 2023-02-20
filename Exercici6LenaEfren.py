TotalJugadors=int(input("Quants jugadors han juat: "))

PuntuacióJugador1=0
CartesJugador=int

for i in range(0,TotalJugadors):
    print("JUGADOR",i+1)
    Nom=str(input("Nom: "))
    
    while CartesJugador!=0:

            CartesJugador=int(input("Quines cartes tens?:"))
            
            
            if CartesJugador==1:
                PuntuacióJugador1==PuntuacióJugador1+11
            elif CartesJugador==3:
                PuntuacióJugador1==PuntuacióJugador1+10
            elif CartesJugador==10:
                PuntuacióJugador1==PuntuacióJugador1+2
            elif CartesJugador==11:
                PuntuacióJugador1==PuntuacióJugador1+3
            elif CartesJugador==12:
                PuntuacióJugador1==PuntuacióJugador1+4
            else:
                PuntuacióJugador1==PuntuacióJugador1+0
                break
            
    print(PuntuacióJugador1)    