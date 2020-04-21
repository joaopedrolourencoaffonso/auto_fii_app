<!DOCTYPE html>
<html>
<head>
	<title>Editando</title>
	<style>
		
	</style>
</head>

<body>


<div align="center">
	<h1 style="border-style: solid; color: #0000ff; font-family:courier; width:360px; height:40px;">Editar!</h1>
	<p style="border-style: solid; color: #33cc33; font-family:courier; width:450px; height:20px;">Abaixo, você pode ver seus fundos</p>

	<?php
	$myfile = fopen("meus_fundos.txt", "r") or die("Unable to open file!");
	$fundos = fread($myfile,filesize("meus_fundos.txt"));
	fclose($myfile);
	
	#echo '<p style="border-style: solid; color: #003300; font-family:courier; width:300px; height:20px;">Os fundos registrados são:</p>';
	echo '<p style="border-style: solid; color: #003300; font-family:courier">';
	echo "$fundos</p>";
	?>

	<p style="border-style: solid; color: #003300; font-family:courier; width:600px; height:20px;">Escreva o nome do fundo que você quer adicionar:</p>
	<form method="POST" action="escrever.php">
			<input size="90" type="text" placeholder="ABCP11;VISC11" name="fundos"/><br>
			<br>
			<input type="submit" style="background-color: #4CAF50; font-family:arial; font-size:15px; color: white; text-align: center; width:150px; height:40px" value="Adcionar"/>
	</form>

	<p style="border-style: solid; color: #003300; font-family:courier; width:600px; height:20px;">Escreva o nome do fundo que você quer deletar:</p>
	<form method="POST" action="deletar.php">
			<input size="90" type="text" placeholder="ABCP11;VISC11" name="fundos"/><br>
			<br>
			<input type="submit" style="background-color: #4CAF50; font-family:arial; font-size:15px; color: white; text-align: center; width:150px; height:40px" value="Deletar"/>
	</form>




</div>
</body>
</html>
