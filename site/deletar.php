<?php

set_time_limit(900);
$fundos = $_POST["fundos"];
$fundos = strtolower($fundos);

$myfile = fopen("meus_fundos.txt", "r") or die("Unable to open file!");
$texto = fread($myfile,filesize("meus_fundos.txt"));
fclose($myfile);

$vetor = explode(";", $texto);
$tamanho = sizeof($vetor);
$var = "";

for ($x = 0; $x < $tamanho; $x+=1) {
	if ($vetor[$x] != $fundos) {
		$var = "$var;".$vetor[$x];
	}
}

$var = substr($var,1);

$myfile = fopen("meus_fundos.txt", "w") or die("Unable to open file!");
fwrite($myfile, $var);
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


echo "<p>$texto</p>";


echo "
</body>
</html>";


?>