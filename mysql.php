<?php
	include "config.php";
	$baglanti = mysql_connect($mysql_server,$mysql_user,$mysql_password);
	mysql_select_db($mysql_dbname,$baglanti);
	print mysql_error();
?>
