  
<html>
<head>
  <title>Bill Calculator</title>
</head>
<body>

  <h1><h1>
  
  <?php
    $internet = $_POST['internet'];
    $carI = $POST['carI'];
    $energy = $POST['energy'];
    $phone = $POST['phone'];
    $rent = $POST['rent'];
    $misc = $POST['misc'];
    $total = $internet + $carI + $energy + $phone + $rent + $misc;
    
    print("<p>Your total is $total</p>");
  

?>
<p><a href="travel_JDS.html">Calculate another trip?</a></p>

</body>
</html>