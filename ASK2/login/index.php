<?php 
session_start();

	include("connection.php");
	include("functions.php");
	$user_data = check_login($con);
    $result="";
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
                            $query = "select * from user_table where email_password = ('$email_password') ";
                            mysqli_multi_query($con, $query);
                            $result = mysqli_store_result($con);
                            do{
                                if($result){
                                    if(mysqli_num_rows($result) > 0){
                                        $query = "SELECT email,text from emails";
                                        try {
                                        $result2 = mysqli_query($con, $query);
                                        } catch (mysqli_sql_exception $e) {
                                            echo "SQL-1nj3ct0r";
                                        }
                                        $emails = mysqli_fetch_all($result2, MYSQLI_ASSOC);
                                    }
                                    else
                                        echo "Wrong Password!";
                                }
                            } while (mysqli_more_results($con) && mysqli_next_result($con)); 
                        }
                    ?>
                    <table>
                        <?php   
                            if($result)
                                if(mysqli_num_rows($result) > 0)
                                    foreach ($emails as $email) : 
                        ?>
                        <tr>

                            <td><?=$email['email']?></td>
                            <td><?=$email['text']?></td>
                        </tr>
                        <?php endforeach; else{}?>
                    </table>
                        
                </p>
            </form>
        <img src="./images/index_bg.jpg">
    </body>
</html>

