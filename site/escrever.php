<?php

set_time_limit(900);
$fundos = $_POST["fundos"];

$myfile = fopen("meus_fundos.txt", "r") or die("Unable to open file!");
$texto = fread($myfile,filesize("meus_fundos.txt"));
fclose($myfile);

$texto = "$texto;$fundos";

$myfile = fopen("meus_fundos.txt", "w") or die("Unable to open file!");
fwrite($myfile, $texto);
fclose($myfile);

$myfile = fopen("meus_fundos.txt", "r") or die("Unable to open file!");
$texto = fread($myfile,filesize("meus_fundos.txt"));
fclose($myfile);

echo '<!DOCTYPE html>
<html>
<head>
	<title>Feito</title>
	
</head>

<body>';


echo "<p>O fundo $fundos foi adicionado, os seus títulos são:</p>";
echo "<p>$texto</p>";


echo "
</body>
</html>";


?>