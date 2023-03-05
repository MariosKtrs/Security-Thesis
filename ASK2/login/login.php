<?php 
session_id("Ch4ll3ng3-S0lv3d");
session_start();

	include("connection.php");
	include("functions.php");

	if($_SERVER['REQUEST_METHOD'] == "POST"){
		
		//something was posted
		$user_name = $_POST['user_name'];
		$password = $_POST['password'];
		//read from database

		//safe
		//$query = "select * from user_table where user_name = '$user_name'";
			
		//vulnerable
		$query = "select * from user_table where user_name = '$user_name' and password='$password'";
		$result = mysqli_query($con, $query);

		if($result){
			
			if(mysqli_num_rows($result) > 0){

				$user_data = mysqli_fetch_assoc($result);
				//if ($user_data['password']=== $password){
					$_SESSION['user_id'] = $user_data['user_id'];
					header("Location: index.php");
					die;
				//}
			}
		}
			
			echo "wrong username or password!";
	}

?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="./styles.css">
		<link rel="icon" href="data:,">
		<style><?php include "styles.css" ?></style>
    </head>
    <body>
		<div class="login-page">
			<?php include_once "nav.php" ?>
			<h2>Welcome back</h2>
			<form class="box" method="post">
				<div class="user">
					<p class = "username">Username: </p>
					<input name="user_name" type= "text" class="user-text">
				</div>
				<div class = "pass">
					<p class = "password">Password: </p>  
					<input name="password" type = "password" class = "pass-text">   
				</div>
				<input class="log-in-button" type="submit" value="Log in">
			</form> 
		</div>
	</body>
</html>
