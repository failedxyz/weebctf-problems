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
				background-image: url(angel-player.png);
				background-size: cover;
				background-position: center;
			}
			#panel {
				position: absolute;
				left: 0;
				top: 0;
				transform: translateX(-50%) translateY(-50%);
			}
		</style>
	</head>
	<body>
		<div id="panel">
			<form method="POST">
				<input type="hidden" name="token" value="<?php md5(random_bytes(128)); ?>" />
				<input type="password" name="password" placeholder="Password" />
			</form>
		</div>
	</body>
</html>