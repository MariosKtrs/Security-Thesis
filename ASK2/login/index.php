<?php 
session_start();

	include("connection.php");
	include("functions.php");
	$user_data = check_login($con);
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Welcome!</title>
        <link rel="stylesheet" href="index.css">
        <style><?php include "index.css" ?></style>     
    </head>
    <body>
        <div class="top">
            <a class="logout" href="logout.php">Logout</a>
            <h1>Welcome to your Super Secure Account <?php echo $user_data['user_name']?>!</h1>
            <form class="index-box" method="post">
                <p>Enter your name below and we'll say hi!</p>
                <div class="search">
                    <input class="search-bar" name="sender" type="text">
                    <input class="submit" type="submit" name="submit" value="Submit"> 
                </div>
               <p> <?php 
                    if(isset($_POST['submit'])){ 
                        $name = $_POST['sender'];  
                        echo "<p> Hello $name !</p>";
                    } 
                ?> </p>
            </form>
        </div>
        <img src="./images/index_bg.jpg">
    </body>
</html>

