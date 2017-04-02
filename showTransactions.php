<?php
	include "mysql.php";
?>
<html>

	<head><title>Transaction List</title></head>
	<body>
	<font face=verdana>
	<center>
	<center><img src="logo1.png"></center><br>
	<p>&nbsp;</p>
	<table border=1 width=70%>
	
		
	<thead>
	<tr>
		<th>Müşteri ID</th>
		<th>Müşteri Adı ve Soyadı</th>
		<th>Tarih</th>
		<th>Ücret</th>
	</tr>
</thead>
<?
	$query = mysql_query("select * from transactions");
	while ($transaction = mysql_fetch_array($query)) {
		print mysql_error();
		$query = mysql_query("select * from musteriler where mid = $transaction[mid]");
		$customer = mysql_fetch_array($query);
		print mysql_error();
		print "<tr>";
		print "<td align=center>$transaction[mid]</td>";
		print "<td align=center>$customer[adsoyad]</td>";
		print "<td align=center>$transaction[date]</td>";
		print "<td align=center>$transaction[price]</td>";
		print "</tr>";
	} 
?>
</table>
</body>
</html>
	
