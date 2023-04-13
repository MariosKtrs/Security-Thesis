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
        <script><?php include "index.js" ?></script>
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
        <p id ="email-message"></p>
        <form class="index-box" method="post">
                <p>My emails</p>
                <div class="search">
                    <input class="search-bar" name="email_password" type="text">
                    <input class="submit" type="submit" name="submit_email_password" value="Submit"> 
                </div>
               <p> <?php 
                    if(isset($_POST['submit_email_password'])){ 
                        $email_password = $_POST['email_password'];  
                        $query = "select * from user_table where email_password =  ('$email_password')";
                        $result = mysqli_query($con, $query);
                        if($result){
                            
                            if(mysqli_num_rows($result) > 0){
                                $query = "SELECT email,text from Emails";
                                $result2 = mysqli_query($con, $query);
                                $emails = mysqli_fetch_all($result2, MYSQLI_ASSOC);
                        ?>
                                <table>
                                    <tr>
                                        <th>Email</th>
                                        <th>Text</th>
                                    </tr>
                                    <?php foreach ($emails as $email) : ?>
                                    <tr>
                                        <td><?=$email['email']?></td>
                                        <td><?=$email['text']?></td>
                                    </tr>
                                    <?php endforeach; ?>
                                </table>
                        <?php
                            }
                        } else {
                            $msg =  "wrong username or password!";
                        }
                        
                    }
                        echo "<p> Hello $name !</p>";
                    
                ?> </p>
            </form>
        <img src="./images/index_bg.jpg">
    </body>
</html>

