<?php
$stop = 1000000;

function chainLength($n){
	$length = 1;
	while($n != 1){
		if($n % 2 == 0){
			$n = $n/2;
		}else{
			$n = 3*$n + 1;
		}
		$length++;
	}
	return $length;
}

$maxSeed = 0;
$max = 0;
for($i=1; $i<$stop; $i++){
	echo "Looking at $i\n";
	$current = chainLength($i);
 	if($current > $max){
		$maxSeed = $i;
		$max = $current;
	}
}

echo "Answer = $maxSeed\n";