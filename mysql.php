<?php
	include "config.php";
	$baglanti = mysql_connect($mysql_server,$mysql_user,$mysql_password);
	mysql_select_db($mysql_dbname,$baglanti);
	print mysql_error();
	$query = mysql_query("SHOW COLUMNS FROM my_table;");
	print mysql_error();
?>