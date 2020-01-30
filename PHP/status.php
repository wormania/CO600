<?php
if(isset($_GET["id"])){
  $id = htmlspecialchars($_GET["id"]);
  $response = file_get_contents('http://localhost:8080/status?id='.$id);
  echo $response;
}
?>