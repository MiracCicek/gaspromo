<?php
	include "mysql.php";
	$date = date('Y-m-d H:i:s');
	$addQuery = "INSERT INTO transactions (date,mid) values ('$date',$mid)";
	mysql_query($addQuery);
	print mysql_error();
	print "OK";
?>