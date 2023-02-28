<?php

$dbhost = "db";
$dbuser = "root";
$dbpass = "password";
$dbname = "login_db";
echo $con;
if(!$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname))
{
	
	die("failed to connect!");
}
