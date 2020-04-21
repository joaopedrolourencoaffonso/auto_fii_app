import sys, webbrowser, requests, bs4

fundos = str(sys.argv[1])
#fundos = 'alzr11;visc11;mxrf11'
fundos = fundos.split(';')
#fundos = fundos.remove('')

string = "                                      LINK                                         | NOME  |   DATA   | YIELD | P/PVP | PREÇO\n"
          
for fii in fundos:
        temp = fii.lower()
        target = "Gerencial"
        target1 = "Yield (a.a.)"
        target2 = "P/VP"
        target3 = "Dividend Yield"
        temp1 = temp.split("11")
        temp1 = temp1[0]             
         ###############################

        
        res = requests.get("https://www.meusdividendos.com/fundo-imobiliario/" + temp1 + "")
        res.raise_for_status()
        obj = bs4.BeautifulSoup(res.text, features="html.parser")
        objeto = obj.select('span')
        lenght = len(objeto)
        i = 0
        while i < lenght:
                info_fii = str(objeto[i])
                i = i + 1
                pos = info_fii.find(target1)
                if pos > 0:
                        vyield = str(objeto[i])
                        vyield = vyield.split('>')
                        vyield = vyield[1].split('<')
                        vyield = vyield[0]
                        vyield = vyield[:5]
                        vyield = float(vyield)
                        vyield = 100*vyield
                        vyield = str(vyield)
                        vyield = vyield[:4]
                #################################
                pos = info_fii.find(target2)
                if pos > 0:
                        pvp = str(objeto[i-2])
                        pvp = pvp.split('>')
                        pvp = pvp[1].split('<')
                        pvp = pvp[0]
                        pvp = pvp[:4]
                        #################################
                        break
                        
        ###############################
        res = requests.get("https://fiis.com.br/" + temp + "/")
        if res.status_code == 404:
                string = string + ' ' +  temp + ' Não encontrado '
        else:               
                res.raise_for_status()
                obj = bs4.BeautifulSoup(res.text, features="html.parser")
                objeto = obj.select('li a')
                lenght = len(objeto)
                i = 0
                while i < lenght:
                        info_fii = str(objeto[i])
                        i = i + 1
                        pos = info_fii.find(target)
                        if pos > 0:
                                data = info_fii.split('\n', 1)
                                site = ' ' + str(data[0][9:90]) + '/'
                                break
                ###############################

                res.raise_for_status()
                obj = bs4.BeautifulSoup(res.text, features="html.parser")
                objeto = obj.select('span')
                lenght = len(objeto)
                i = 0
                while i < lenght:
                        info_fii = str(objeto[i])
                        i = i + 1
                        pos = info_fii.find(target3)
                        if pos > 0:
                                preco = str(objeto[i+11])
                                preco = preco.split('>')
                                preco = preco[1].split('<')
                                #################################
                                break
                        
                ###############################





        string = string + " " + site + ' ' + str(temp) + '  ' + data[1][19:27] + "    " + str(vyield) + '   ' + str(pvp) + "   " + str(preco[0]) + " \n"

print(string)



