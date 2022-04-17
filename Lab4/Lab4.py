# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:13:38 2022

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt

#Lambda*V= Derivada de la masa con respecto al tiempo por velocidad
#Lambda*V= dm(t)/dt * v
#En momento Lineal:
#ma=F=dP/dt = d(mv)/dt = dm(t)/dt * v +m*dv/dt 

#Las fuerzas dependen del ejercicio, pero en su mayoria son:
#Empuje, peso, derivada de la masa con respecto al tiempo x velocidad

'''
|----------------------------|
|---Ejercicio 01 taller 9---|
|----------------------------|
'''

# interval = 0.001
# # Constantes
# y_0=0
# m_0 = 48800
# v_0x = 0
# E=163000
# lamb=129.4
# #Importante: La masa depende del tiempo

# a_0 = (E + lamb*v_0x)/m_0

# t_0 = 0 # tiempo ini



# #METODO DE EULER-CROMER

# y_t=[y_0]
# m_t=[m_0]
# v_x = [v_0x]
# t_n = [t_0]
# a_n = [a_0]
# vx  = v_0x
# t   = t_0
# m=m_0
# y_new=y_0


# while m>40000:
#     a = (E - lamb*vx)/m
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     m=m_0-lamb*t
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t) 
#     m_t=np.append(m_t,m)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO
#     print(y)



# plt.plot(t_n,y_t,"mediumslateblue")
# plt.title("y(m) vs t(s)")
# plt.xlabel("t(s)")
# plt.ylabel("y(m)")
# plt.show()

# # print("Aceleracion: ")
# # print(*a_n)
# # print("Velocidad")
# # print(*v_x)
# plt.plot(t_n,v_x,"brown")
# plt.title("v(m/s) vs t(s)")
# plt.xlabel("t(s)")
# plt.ylabel("v(m/s)")
# plt.show()


'''
|----------------------------|
|---Ejercicio 02 taller 9---|
|----------------------------|
'''

# interval = 0.001
# # Constantes
# y_0=0
# m_0 = 12800
# v_0x = 0
# g=9.81
# E=163000
# lamb=129.4
# #Importante: La masa depende del tiempo

# a_0 = (E - m_0*g - lamb*v_0x)/m_0
# # print("soy acelaracion inicial: ", a_0)
# t_0 = 0 # tiempo ini


# #METODO DE EULER-CROMER

# y_t=[y_0]
# m_t=[m_0]
# v_x = [v_0x]
# t_n = [t_0]
# a_n = [a_0]
# vx  = v_0x
# t   = t_0
# m=m_0
# y_new=y_0


# while m>4000:
#     a = (E - m*g - lamb*vx)/m
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     m=m_0-lamb*t
#     m_t=np.append(m_t,m)
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO 
#     print("While 1")


# #Formula para calcular la velocidad maxima:
# #Hmax: Vi^2/2g

# #Nuestro de referencia es el siguiente
# #y=0 cuando m=4000 
# #(En este momento tomamos la velocidad del cohete cuando m=4000)->while anterior

# #De esta manera encontramos la distancia que el cohete
# #permanecerá subiendo (vel disminuyendo)
# #hasta llegar a su altura maxima (vel=0,a=-g)
  
# l_vx1=len(v_x)

# # Sabemos que en hmax, v=0, pero con la condicion de 
# # este while no se cumple. Ademas este while lo ejecuta 180 veces (muy poco).
# # Por esto: ** REVISAR LA CONDICION **

# # while y<(vx**2)/(2*g):
# #     a = -g
# #     vx = vx + interval *a # aqui esta la aceleracion 
# #     y=y_new+vx*interval
# #     a_n = np.append(a_n,a)
# #     v_x =np.append(v_x,vx)
# #     t_n = np.append(t_n,t)
# #     y_t=np.append(y_t,y)
# #     y_new=y 
# #     t = t + interval # INCREMENTA EL TIEMPO 
# #     print("While 2")

# #Otra posible condicion para el while es: v>=0
# #Sabemos que mientras la velocidad sea positiva el cohete se desplazará
# #hacia arriba. Ademas, cuando v=0 se ha alcanzado hmax

# while vx>=0:
#     a = -g
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO 
#     print("While 2")

# l_vx=len(v_x)

# while y>0:
#     a = -g
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO 
#     print("While 3")



# plt.plot(t_n[:l_vx1],v_x[:l_vx1],"green")
# plt.plot(t_n[l_vx1:l_vx],v_x[l_vx1:l_vx],"darkorange")
# plt.plot(t_n[l_vx:],v_x[l_vx:],"indigo")
# plt.title("Velocidad vs Tiempo")
# plt.xlabel("t(s)")
# plt.ylabel("v(m/s)")
# plt.show()

# plt.plot(t_n[:l_vx1],y_t[:l_vx1],"green")
# plt.plot(t_n[l_vx1:l_vx],y_t[l_vx1:l_vx],"darkorange")
# plt.plot(t_n[l_vx:],y_t[l_vx:],"indigo")
# plt.title("Posición vs Tiempo") 
# plt.xlabel("t(s)")
# plt.ylabel("y(m)")
# plt.show() 


'''
|----------------------------|
|---Ejercicio 03 taller 9---|
|----------------------------|
'''

'''
Como calcular la gravedad a partir de las constantes:  (pag 2)
    
https://imagine.gsfc.nasa.gov/observatories/learning/swift/classroom/docs/law_grav_guide_spanish.pdf

'''

# interval = 0.001
# # Constantes
# G=6.67* (10**-11) #Cte gravitacional (N * m^2/kg^2)
# Mt=5.972*(10**24) #Masa tierra (kg)
# Rt=6375000 #Radio tierra (m) 
# y_0=0
# m_0 = 12800
# v_0x = 0
# E=163000
# lamb=129.4

# #Importante: La masa depende del tiempo
# #La gravedad depende de la distancia a la que está el cohete de la tierra

# g=(G*Mt)/(Rt-y_0)**2
# a_0 = (E - m_0*g - lamb*v_0x)/m_0
# # print("soy acelaracion inicial: ", a_0)
# t_0 = 0 # tiempo ini


# #METODO DE EULER-CROMER

# y_t=[y_0]
# m_t=[m_0]
# g_t=[g]
# v_x = [v_0x]
# t_n = [t_0]
# a_n = [a_0]
# vx  = v_0x
# t   = t_0
# m=m_0
# y_new=y_0


# while m>4000:
#     a = (E - m*g - lamb*vx)/m
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     m=m_0-lamb*t
#     g=(G*Mt)/(Rt-y)**2
#     m_t=np.append(m_t,m)
#     g_t=np.append(g_t,g)
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO
#     print("while 1")
#     print("Gravedad: ",g)

# l_vx1=len(v_x)

# #Notese que en el punto anterior (2) usamos la formula de altura maxima.
# #De esa manera encontrabamos la distancia que el cohete permanecia subiendo
# #hasta que llegará a su punto maximo (vel=0, a=-g). 

# #Sin embargo, la formula de aluta maxima tiene involucrada la variable g, que 
# #en dicho ejercicio era constante, pero en este problema, la gravedad no es
# #constante, por lo que para aplicar la formula de altura maxima tendriamos que 
# #darle un valor estricto a la gravedad.

# #Una manera para solucionar esto, es cambiar la condicion del while
# #Sabemos que, una vez el empuje es cero, el cohete seguirá moviendose
# #con el impulso que lleva, es decir, su velocidad empezará a disminuir hasta
# #llegar a cero y luego volverse negativa

# while vx>=0:
#     a = -g
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     g=(G*Mt)/(Rt-y)**2
#     g_t=np.append(g_t,g)
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO 
#     print("while 2")

# l_vx=len(v_x)

# while y>0:
#     a = -g
#     vx = vx + interval *a # aqui esta la aceleracion 
#     y=y_new+vx*interval
#     g=(G*Mt)/(Rt-y)**2
#     g_t=np.append(g_t,g)
#     a_n = np.append(a_n,a)
#     v_x =np.append(v_x,vx)
#     t_n = np.append(t_n,t)
#     y_t=np.append(y_t,y)
#     y_new=y 
#     t = t + interval # INCREMENTA EL TIEMPO 
#     print("While 3")


# plt.plot(t_n[:l_vx1],v_x[:l_vx1],"navy")
# plt.plot(t_n[l_vx1:l_vx],v_x[l_vx1:l_vx],"lightgreen")
# plt.plot(t_n[l_vx:],v_x[l_vx:],"purple")
# plt.title("Velocidad vs Tiempo")
# plt.xlabel("t(s)")
# plt.ylabel("v(m/s)")
# plt.show()


# plt.plot(t_n[:l_vx1],y_t[:l_vx1],"navy")
# plt.plot(t_n[l_vx1:l_vx],y_t[l_vx1:l_vx],"lightgreen")
# plt.plot(t_n[l_vx:],y_t[l_vx:],"purple")
# plt.title("Posición vs Tiempo") 
# plt.xlabel("t(s)")
# plt.ylabel("y(m)")
# plt.show() 


'''
|----------------------------|
|---Ejercicio 04 taller 9---|
|----------------------------|
'''

#Para este ejercicio haremos uso del punto 2, es decir, con gravedad cte

#Fuerza de friccion: kv^2
interval = 0.001
# Constantes
y_0=0
m_0 = 12800
v_0x = 0
g=9.81
E=163000
lamb=129.4
K=0.3
#Importante: La masa depende del tiempo

a_0 = (E - m_0*g -K*v_0x**2 -lamb*v_0x)/m_0
# print("soy acelaracion inicial: ", a_0)
t_0 = 0 # tiempo ini


#METODO DE EULER-CROMER

y_t=[y_0]
m_t=[m_0]
v_x = [v_0x]
t_n = [t_0]
a_n = [a_0]
vx  = v_0x
t   = t_0
m=m_0
y_new=y_0


while m>4000:
    a = (E - m*g -K*vx**2 - lamb*vx)/m
    vx = vx + interval *a # aqui esta la aceleracion 
    y=y_new+vx*interval
    m=m_0-lamb*t
    m_t=np.append(m_t,m)
    a_n = np.append(a_n,a)
    v_x =np.append(v_x,vx)
    t_n = np.append(t_n,t)
    y_t=np.append(y_t,y)
    y_new=y 
    t = t + interval # INCREMENTA EL TIEMPO 
    print("While 1")


# ** REVISAR LA SIGUIENTE FORMULA **
#Formula para calcular la velocidad maxima:
#Hmax: Vi^2/2g

#Nuestro de referencia es el siguiente
#y=0 cuando m=4000 
#(En este momento tomamos la velocidad del cohete cuando m=4000)->while anterior

#De esta manera encontramos la distancia que el cohete
#permanecerá subiendo (vel disminuyendo)
#hasta llegar a su altura maxima (vel=0,a=-g)
  
l_vx1=len(v_x)

#peso+friccion=F=m*a
# -m*g - k*vx**" = m*a
#a= -g - (k*v**2)/m

while vx>=0:
    a = -g -(K*vx**2)/m
    vx = vx + interval *a # aqui esta la aceleracion 
    y=y_new+vx*interval
    a_n = np.append(a_n,a)
    v_x =np.append(v_x,vx)
    t_n = np.append(t_n,t)
    y_t=np.append(y_t,y)
    y_new=y 
    t = t + interval # INCREMENTA EL TIEMPO 
    print("While 2")


l_vx=len(v_x)

while y>0:
    a = -g+(K*vx**2)/m
    vx = vx + interval *a # aqui esta la aceleracion 
    y=y_new+vx*interval
    a_n = np.append(a_n,a)
    v_x =np.append(v_x,vx)
    t_n = np.append(t_n,t)
    y_t=np.append(y_t,y)
    y_new=y 
    t = t + interval # INCREMENTA EL TIEMPO 
    print("While 3")
    print(f"y={y}")
    print(f"a= {a}")
    print(f"vx={vx}")

plt.plot(t_n[:l_vx1],v_x[:l_vx1],"skyblue")
plt.plot(t_n[l_vx1:l_vx],v_x[l_vx1:l_vx],"springgreen")
plt.plot(t_n[l_vx:],v_x[l_vx:],"slategray")
plt.title("velocidad vs tiempo")
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()

plt.plot(t_n[:l_vx1],y_t[:l_vx1],"skyblue")
plt.plot(t_n[l_vx1:l_vx],y_t[l_vx1:l_vx],"springgreen")
plt.plot(t_n[l_vx:],y_t[l_vx:],"slategray")
plt.title("posicion vs tiempo") 
plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.show() 
