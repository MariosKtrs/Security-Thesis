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
        <a class="logout" href="logout.php">Logout</a>
        <h1>Welcome to your Super Secure Account <?php echo $user_data['user_name']?>!</h1>
        <form class="index-box" method="post">
            <p>Want to stay informed and get updates? Just enter your email below!</p>
            <div class="search">
                <input class="search-bar" name="sender" type="email">
                <input class="submit" type="submit" name="submit" value="Search"> 
            </div>
            <p id="error-text"></p>
            <?php 
                if(isset($_POST['submit'])){ 
                    $name = $_POST['sender'];  
                    echo "<p> Email $name successfully added!</p>";
                } 
            ?>
        </form>
        <img src="./images/index_bg.jpg">
    </body>
</html>

