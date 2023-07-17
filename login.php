<?php
$servername = "hostingmysql156.amen.pt";
$username = "JV214_jvarandas";
$password = "wate4606";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>