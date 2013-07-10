<?php
$result = bcpow('2', '1000');
$sum = 0;
for($i=0; $i<strlen($result); $i++){
	$sum += $result[$i];
}
echo "Answer = $sum;";