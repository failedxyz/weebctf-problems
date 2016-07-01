<?php
	include("flag.php"); // import $flag
	if (isset($_POST["token"]) && isset($_POST["password"])) {
		if (isset($_POST["debug"])) echo md5($flag) . "\n"; // debug
		$padded = $flag . str_repeat("\x00", 64 - strlen($flag));
		if ($_POST["token"] === $_POST["password"]) {
			die("Your token must not match your password.");
		}
		$salted_token = $padded . hex2bin($_POST["token"]);
		$salted_password = $padded . hex2bin($_POST["password"]);
		if (md5($salted_token) !== md5($salted_password)) {
			die("Wrong password.");
		}
		?>
		<h1>Congratulations!</h1>
		<p>The flag is <?php echo $flag; ?></p>
		<?php
		die();
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
				text-align: center;
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
				<input type="hidden" name="token" value="<?php echo bin2hex(openssl_random_pseudo_bytes(128)); ?>" />
				<input type="password" name="password" placeholder="Password" autocomplete="off" autofocus />
				<br />
				<small><a href="/source.php">source</a></small>
			</form>
		</div>
	</body>
</html>