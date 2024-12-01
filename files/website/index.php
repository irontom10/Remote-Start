<?php
if (isset($_POST['start'])) {
    exec('sudo systemctl start remote_start.service');
}
if (isset($_POST['stop'])) {
    exec('sudo systemctl stop remote_start.service');
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Remote Start Interface</title>
</head>
<body>
    <h1>Vehicle Remote Start</h1>
    <form method="post">
        <button type="submit" name="start">Start Vehicle</button>
    </form>
    <form method="post">
        <button type="submit" name="stop">Stop Vehicle</button>
    </form>
</body>
</html>
