<?php

	include_once 'connect.php';

	$type = $_GET['type'];

	if ($type == 'login'){
				$user_name = $_GET['user_name'];
				$user_password = $_GET['user_password'];

				$result = $dbcon->query("SELECT * FROM users WHERE user_name='$user_name' AND user_password='$user_password'");

				if($result->num_rows> 0) {
					while ($row = $result->fetch_assoc()){
						echo $row["f_name"];
					}
				} else {
					echo "login_error";
				}
	}

	else if ($type == 'register'){
				$f_name = $_GET['f_name'];
				$l_name = $_GET['l_name'];
				$user_name = $_GET['user_name'];
				$user_password = $_GET['user_password'];

				$result = $dbcon->query("SELECT * FROM users WHERE user_name='$user_name'");
				if(mysqli_num_rows($result) >0 ){
		        echo "register_error";
		    } else {
						$result = $dbcon->query("INSERT INTO users (f_name,l_name,user_name,user_password) VALUE ('$f_name','$l_name','$user_name','$user_password')");

						if ($result) {
				      echo "register_ok";
				    } else {
				      echo "register_error";
				   	}
				}
	}

	else if ($type == 'set_highscore'){
				$user_name = $_GET['user_name'];
				$equation = $_GET['equation'];
				$new_total = $_GET['new_total'];

				$result = $dbcon->query("UPDATE users SET ".$equation."= ".$equation." + ".$new_total.", ".$equation."_total = ".$equation."_total + 1 WHERE user_name = '$user_name'");
	}

	else if ($type == 'get_highscore'){
				$user_name = $_GET['user_name'];

				$result = $dbcon->query("SELECT
							(prosthesi + afairesi + pollaplasiasmo + diairesi) as sum1,
							(prosthesi_total + afairesi_total + pollaplasiasmo_total + diairesi_total) as sum2,
							prosthesi, prosthesi_total,
							afairesi, afairesi_total,
							pollaplasiasmo, pollaplasiasmo_total,
							diairesi, diairesi_total
							FROM users WHERE user_name='$user_name'");

				if($result->num_rows> 0) {
					while ($row = $result->fetch_assoc()){
						echo $row["sum1"]."-".$row["sum2"]
						."-".$row["prosthesi"]."-".$row["prosthesi_total"]
						."-".$row["afairesi"]."-".$row["afairesi_total"]
						."-".$row["pollaplasiasmo"]."-".$row["pollaplasiasmo_total"]
						."-".$row["diairesi"]."-".$row["diairesi_total"];
					}
				}

	}

	else if ($type == 'get_top_ten'){
				$equation = $_GET['equation'];

				$result = $dbcon->query("SELECT user_name, ".$equation." as equation FROM users ORDER BY ".$equation." DESC LIMIT 10");

				if($result->num_rows> 0) {
					while ($row = $result->fetch_assoc()){
						echo $row["user_name"]." : ".$row['equation']."\n";
					}
				}
	}

?>
