from tkinter import *
from tkinter import messagebox
 
window = Tk()
window.title("Divicio interactiva v0.1 ")
window.geometry('560x550')
 
Divisor = Label(window, text="Divisor")
Divisor.grid(column=0, row=0)
inpDivisor = Entry(window,width=10)
inpDivisor.grid(column=1, row=0)
aux1 = inpDivisor.get()
tamDivisor = len(aux1)

Dividendo = Label(window, text="Dividendo")
Dividendo.grid(column=0, row=1)
inpDividendo = Entry(window,width=10)
inpDividendo.grid(column=1, row=1)

pista = Label(window, text="pista")
pista.grid(column=1, row=2)

proceso = Label(window, text="Operacion")
proceso.grid(column=0, row=2)

def clicked():
    valDivisor = int(inpDivisor.get())
    valDividendo = int(inpDividendo.get())

    res = valDividendo//valDivisor
    strRes = str(res)
    txtpista = ''
    for p in strRes:
        txtpista += '? '
    messpista = """Pista -> {} 
(cifras de tu resultado)""".format(txtpista)
    pista.configure(text=messpista)
    txt_Res = str(res)
    strDividendo = str(valDividendo)

    mess_procss ="""     _______
 {}|{}
""".format(valDivisor, valDividendo)
    proceso.configure(text=mess_procss)
    
    message = """Recuerdas como se hace la divicion? 
si tienes 'X' cifras de divisor,tomas 'X' cifras del dividendo
dime cuantas veces cabe el {} en {}?
""".format(valDivisor, strDividendo[:2])

    txtmess = Label(window, text=message)
    txtmess.grid(column=0, row=3)

    inpresp1 = Entry(window,width=5)
    inpresp1.grid(column=1, row=3)

    def resp_1():
        comRes1 = txt_Res[0]
        #comRes1 = int(comRes1)
        valueintresp1 = int(inpresp1.get())
        strvalueintresp1 = str(valueintresp1)

        if strvalueintresp1 in comRes1:
            dividendo_1_2 = strDividendo[:2]
            dividendo_1_2 = int(dividendo_1_2)
            residuo = dividendo_1_2 - valDivisor

            txtmess_R1_conf = 'Bien !!! y nos sobra {}'.format(residuo)
            messr2 = Label(window, text=txtmess_R1_conf)
            messr2.grid(column=0, row=7)

            if residuo > valDivisor:
                txtR3 = Label(window, text='Cuantas veces cabe el {} en {}?'.format(valDivisor, residuo))
                txtR3.grid(column=0, row=8)
            elif residuo < valDivisor:
                dividendo_3 = strDividendo[2]
                strresiduo = str(residuo)
                new_num = strresiduo + dividendo_3
                new_num = int(new_num)
                mess = """Aqui ya no cabe el {} en {} verdad?
entonces ocupamos una cifra mas del dividendo, para formar un 
nuevo numero, quedaria asi: {}; cuantas veces cabe {} el en {} 
                """.format(valDivisor, residuo, new_num, valDivisor, new_num)
                message = Label(window, text=mess)
                message.grid(column=0, row=8)

            inpresp2 = Entry(window,width=5)
            inpresp2.grid(column=1, row=8)
            new_num_2 = new_num
# HER <<<<<<<<<<------------------->>>>>>>

            def resp_2():
                comRes2 = txt_Res[1]
                #comRes1 = int(comRes1)
                valueintresp2 = int(inpresp2.get())
                strvalueintresp2 = str(valueintresp2)
                residuo_resp_2 = new_num_2 - (valDivisor * valueintresp2)
                mess = """Bien !!! ahora nos sobran {}
                """.format(residuo_resp_2)
                dividendo_4 = strDividendo[3]
                new_num2 = str(residuo_resp_2) + dividendo_4
                new_num2 = int(new_num2)

                if strvalueintresp2 in comRes2:
                    txtresp2 = Label(window, text = mess)
                    txtresp2.grid(column=0, row=9)
                    
                    errormess = """Aqui tampoco cabe el {} verdad?, volvemos a ocupar una cifra mas
de nuestro dividendo y formar un nuevo numero el {}; ahora cuantas
veces cabe el {} en {}""".format(valDivisor, new_num2, valDivisor, new_num2)

                    if residuo_resp_2 < valDivisor:
                        txtresp2 = Label(window, text =errormess)
                        txtresp2.grid(column=0, row=10)

                        inpresp3 = Entry(window,width=5)
                        inpresp3.grid(column=1, row=10)

                        def resp_3():
                            valueintresp3 = int(inpresp3.get())
                            comp_resp3 = txt_Res[-2]
                            
                            if str(valueintresp3) in comp_resp3: 
                                resto_r_3p = valDivisor * valueintresp3
                                resto_r_3 =  new_num2 - resto_r_3p
                                mess = """Bien !!! y sobran {}""".format(resto_r_3)
                                message_res3 = Label(window, text=mess)
                                message_res3.grid(column=0, row=11)
                                
                                if resto_r_3 < valDivisor:
                                    last_cifra = strDividendo[-1]
                                    new_num3 = str(last_cifra) + str(resto_r_3)
                                    mess = """
Pero aqui tampoco cabe el {} en {}, volvemos a bajar una cifra, 
ocuparemos la {} para formar un nuevo numero el {},cunatas 
veces cabe el {} aqui?""".format(valDivisor, resto_r_3, last_cifra, new_num3, valDivisor)
                                    message_r_3 = Label(window, text=mess)
                                    message_r_3.grid(column=0, row=12)

                                    inpresp_3 = Entry(window,width=5)
                                    inpresp_3.grid(column=1, row=12)

                                    def resp_4():
                                        last_txtres = txt_Res[-1]
                                        resp4 = int(inpresp_3.get())
                                        str_resp4 = str(resp4)
                                        if str(resp4) in last_txtres:
                                            mess = """
Muy Bien !!! el resultado es: {}, sige practicando 
y seras un genio de las Mates !!!
App by PabloJRJ""".format(res)
                                            messagebox.showinfo("Exito", mess)
                                            message_res4 = Label(window, text = mess)
                                            message_res4.grid(column=0, row=13)
                                        else:
                                            messagebox.showerror("Error", "Casi ... intentalo de nuevo")    


                                    btn_resp1 = Button(window, text="Enviar", command=resp_4)
                                    btn_resp1.grid(column=2, row=12)

                            else:
                                message_res3 = Label(window, text='............')
                                message_res3.grid(column=0, row=11)
                                messagebox.showerror("Error", "Casi ... intenta de nuevo")

                        btn_resp1 = Button(window, text="Enviar", command=resp_3)
                        btn_resp1.grid(column=2, row=10)                         

                else:
                    txtresp2 = Label(window, text = '...........')
                    txtresp2.grid(column=0, row=11)
                    messagebox.showerror("Error", "Casi ... intenta de nuevo")

            btn_resp1 = Button(window, text="Enviar", command=resp_2)
            btn_resp1.grid(column=2, row=8) 
        else:
            txtmess_R1_conf = '..................'
            messr2 = Label(window, text=txtmess_R1_conf)
            messr2.grid(column=0, row=7)
            messagebox.showerror("Error", """Casi ... intenta de nuevo
puede que sea un bumero mas chico 
o mas grande""")

    btn_resp1 = Button(window, text="Enviar", command=resp_1)
    btn_resp1.grid(column=2, row=3)



btn = Button(window, text="Calcular", command=clicked)
btn.grid(column=2, row=1)


window.mainloop()