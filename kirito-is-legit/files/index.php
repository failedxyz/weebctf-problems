<?php
include("flag.php"); // import $flag
if (isset($_POST["legit"]) && $_POST["legit"] === "is-legit") {
	echo "<!-- flag is $flag -->";
}
?>

<!DOCTYPE html>
<html>
	<head>
		<title>Is Kirito Legit?</title>
	</head>
	<body>
		<center>
			<img src="kirito.jpg" />
			<form method="POST">
				Kirito is
				<select name="legit">
					<option value="not-legit">not</option>
				</select>
				legit.
			</p>
		</center>
	</body>
</html>

<!-- source at /source.php -->