<?php

set_time_limit(900);

$myfile = fopen("meus_fundos.txt", "r") or die("Unable to open file!");
$fundos = fread($myfile,filesize("meus_fundos.txt"));
fclose($myfile);
$myfile = fopen("meus_fundos.txt", "w") or die("Unable to open file!");
fwrite($myfile, $fundos);
fclose($myfile);


echo '<!DOCTYPE html>
<html>
<head>
	<title>Resultados</title>
	<style>
		table, th, td {
		  border: 1px solid black;
		  border-collapse: collapse;
		  font-family: century gothic
		}
		th, td {
		  padding: 5px;
		  text-align: center;
		}
		table#t01 tr:nth-child(even) {
		  background-color: #eee;
		}
		table#t01 tr:nth-child(odd) {
		 background-color: #fff;
		}
		table#t01 th {
		  background-color: black;
		  color: white;
		}
	</style>
</head>

<body>
<div align="center">
	<h1 style="border-style: solid; color: #0000ff; font-family:courier; width:360px; height:40px;">Meus Fundos!</h1>
	<p style="border-style: solid; color: #33cc33; font-family:courier; width:550px; height:40px;">Para verificar os relatórios gerenciais, basta clicar nos nomes dos fundos</p>

	<table id="t01" style="width:100%">
	  <tr>
	    <th>Nome do fundo</th>
	    <th>Data</th>
	    <th>Yield (%)</th>
	    <th>PVP</th>
	    <th>Preço</th>
	  </tr>';


echo exec("relatorios.py $fundos");


echo "
	</table>
</div>
</body>
</html>";

#print($space);

#print($fundos);

?>