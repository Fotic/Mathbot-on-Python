<?php
	$host = "localhost";
	$username = "";
	$password = "";
	$db_name = "";

	$dbcon = new MySQLi("$host","$username","$password","$db_name");

	if($dbcon-> connect_error) {
		echo "connection_error";
	}
	// else{
	// 	echo "connection_ok";
	// }
?>
