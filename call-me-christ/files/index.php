<?php
	include("flag.php"); // import $flag
	if (isset($_POST["token"]) && isset($_POST["password"])) {
		$padded = $flag . str_repeat("\x00", 64 - strlen($flag));
		if ($_POST["token"] === $_POST["password"]) {
			die("Your token must not match your password.");
		}
		$salted_token = $padded . $_POST["token"];
		$salted_password = $padded . $_POST["password"];
		if (md5($salted_token) !== md5($salted_password)) {
			die("Wrong password.");
		}
		?>
		<h1>Congratulations!</h1>
		<p>The flag is <?php echo $flag; ?></p>
		<?php
	}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>Angel Player</title>
		<style>
			body {
				background-image: url(angel-player.jpg);
				background-size: cover;
				background-repeat: no-repeat;
			}
			#panel {
				position: absolute;
				left: 50%;
				top: 50%;
				transform: translateX(-50%) translateY(-50%);
			}
			input[name=password] {
				border: 0;
				outline: 0;
				padding: 16px;
				font-size: 15pt;
			}
		</style>
	</head>
	<body>
		<div id="panel">
			<form method="POST">
				<input type="hidden" name="token" value="<?php echo md5(openssl_random_pseudo_bytes(128)); ?>" />
				<input type="password" name="password" placeholder="Password" autofocus />
			</form>
		</div>
	</body>
</html>