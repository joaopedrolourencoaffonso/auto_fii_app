import sys, webbrowser, requests, bs4


def filters(fpreco, fyield, pvp):
        pos1 = fpreco.find(";")
        pos2 = fyield.find(";")
        pos3 = pvp.find(";")
        if (pos1 > 0 and pos2 > 0 and pos3 > 0):
                fpreco = fpreco.split(";")
                fyield = fyield.split(";")
                pvp = pvp.split(";")
                fpreco0 = float(fpreco[0])
                fpreco1 = float(fpreco[1])
                fyield0 = float(fyield[0])
                fyield1 =float(fyield[1])
                pvp0 = float(pvp[0])
                pvp1 = float(pvp[1])
                if (fpreco0 < fpreco1) and (fyield0 < fyield1) and (pvp0 < pvp1):
                        funciona = 0
                        return funciona, fpreco0, fpreco1, fyield0, fyield1, pvp0, pvp1
                else:
                        funciona = 1
                        return funciona, fpreco0, fpreco1, fyield0, fyield1, pvp0, pvp1
        else:
                funciona = 2
                return funciona, fpreco0, fpreco1, fyield0, fyield1, pvp0, pvp1




fpreco = str(sys.argv[1])
fyield = str(sys.argv[2])
pvp = str(sys.argv[3])

#####fpreco
#pos1 = fpreco.find(";")
#####fyield
#pos2 = fyield.find(";")
#####pvp
#pos3 = pvp.find(";")
##########################

funciona = filters(fpreco, fyield, pvp)
if funciona[0] == 2:
        print("<p>Erro, faltou o ';' em algum dos filtros</p>")
elif funciona[0] == 1:
        print("<p>Erro, um dos filtros tem limite inferior maior que o superior</p>")
else:
        #print("<p>" + str(funciona[0]) + "</p>")
        string = ""
        res = requests.get("https://fiis.com.br/lista-de-fundos-imobiliarios/")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto = obj.select('.ticker')
        target = "Cotação atual de"
        target1 = "."

        for item in objeto:
                txt = str(item)
                temp1 = txt.split('span', 1)
                temp1 = temp1[1].split('>', 1)
                temp1 = temp1[1].split('<', 1)
                res = requests.get("https://fiis.com.br/" + temp1[0] +"/")
                res.raise_for_status()
                obj = bs4.BeautifulSoup(res.text, features="html.parser")
                objeto1 = obj.select("div span")
                tamanho = len(objeto1)
                for i in range(0,tamanho):
                        temp4 = str(objeto1[i])
                        pos = temp4.find(target)
                        if pos > 0:
                                nome = temp1[0]
                                preco = str(objeto1[i-2])
                                preco = preco.split('>')
                                preco = preco[1].split('<')
                                preco = preco[0]
        
                ###########################################
                objeto1 = obj.select("#informations--indexes")
                objeto1 = str(objeto1)
                objeto1 = objeto1.split("\n")
                temp1 = objeto1[2].split('>')                   ####yield
                temp1 = temp1[1].split('<')
                yield_value = temp1[0]
                #
                yield_filter = yield_value.split(',')      
                yield_filter = yield_filter[0] + "." + yield_filter[1] #yield para o filtro
                yield_filter = float(yield_filter)
                #
                temp1 = objeto1[6].split('<')
                temp1 = temp1[3].split('>')             #ultimo rendimento
                ultimo_rend = temp1[1]
                #
                temp1 = objeto1[10].split('<')
                temp1 = temp1[3].split('>')             #patrimonio liquido
                patrimonio = temp1[1]
                #
                temp1 = objeto1[14].split('<')
                temp1 = temp1[3].split('>')             #patrimonio liquido
                valor_patr = temp1[1]
                #
                pos = valor_patr.find(".")
        
                if pos > 0:
                        temp1 = valor_patr.split(".")           #usar prints para descobrir o que está errado
                        temp1 = temp1[0] + "" + temp1[1]
                        temp1 = temp1.split(",")
                        temp1 = temp1[0] + "." + temp1[1]       #calculo de valor float de valor_patr por cota
                        temp1 = float(temp1)
                else:
                        temp1 = valor_patr.split(",")
                        temp1 = temp1[0] + "." + temp1[1]       #calculo de valor float de valor_patr  #dessa maneira funciona
                        temp1 = float(temp1)
                #
                pos = preco.find(".")
        
                if pos > 0:
                        temp2 = preco.split(".")
                        temp2 = temp2[0] + "" + temp2[1]
                        temp2 = temp2.split(",")
                        temp2 = temp2[0] + "." + temp2[1]       #calculo de valor float de valor_patr valor_patr por cota
                        temp2 = float(temp2)
                else:
                        temp2 = preco.split(",")
                        temp2 = temp2[0] + "." + temp2[1]       #calculo de valor float de preco #dessa maneira funciona
                        temp2 = float(temp2)
                        
                #
                if temp1 == 0:
                        pvp = "0"
                else:
                        pvp = temp2 / temp1
                        pvp = '%.2f' % pvp
                        
                ##########################################
                if (temp2 < funciona[1]):   #===>continuar daqui
                        continue
                elif (temp2 > funciona[2]):
                        continue
                else:
                        if (float(pvp) < funciona[5]):
                                continue
                        elif (float(pvp) > funciona[6]):
                                continue
                        else:
                             if (yield_filter < funciona[3]):
                                     continue
                             elif (yield_filter > funciona[4]):
                                     continue
                             else:
                                     site = ' href="https://fiis.com.br/' + nome + '/" target="_blank"'
                                     string = string + "<tr> <td> <a" + site + ">" + str(nome) + "</td> <td>" + str(preco) + "</td> <td>" + str(yield_value) + "</td> <td>" + str(ultimo_rend) + "</td> <td>" + str(patrimonio) + "</td> <td>" + str(valor_patr) + "</td> <td>" + str(pvp) + "</td> </tr>"

        

#string = string + " </tr>"
print(string)


#C:\xampp\htdocs\auto_fii --> diretório



