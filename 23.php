<?php
function properDivisors($subject){
	$divisors = array(1 => 1);
	$n = 2;
	for($n=2; $n*$n <= $subject; $n++){
		if($subject % $n == 0){	
			$divisors[$n] = 1;
			$divisors[$subject/$n] = 1;
		}
	}
	return array_keys($divisors);
}

function numType($subject){
	$divisors = properDivisors($subject);
	$arraysum = array_sum($divisors);
	// echo "subject = $subject";
	// print_r($divisors);
	// echo $arraysum . "\n";
	$diff = $subject - $arraysum;
	if($diff == 0){
		return "Perfect";
	}else if($diff < 0){
		return "Abundant";
	}else{
		return "Deficient";
	}
}

$upperLimit = 28123;
$perfect = array();
$abundant = array();
$deficient = array();

for($i=1; $i<$upperLimit; $i++){
	// echo "i = $i\n";
	switch(numType($i)){
		case "Perfect": $perfect[] = $i; break;
		case "Abundant": $abundant[] = $i; break;
		case "Deficient": $deficient[] = $i; break;
	}
}

$sumOfA = array();
foreach($abundant as $a){
	// echo "a = $a\n";
	foreach($abundant as $b){
		$sumOfA[$a+$b] = true;
	}
}

$notSumOfA = array();
for($i=1; $i<=$upperLimit; $i++){
	$notSumOfA[$i] = true;
}

foreach(array_keys($sumOfA) as $key){
	unset($notSumOfA[$key]);
};

$notSumOfA = array_keys($notSumOfA);
echo "Answer = " . array_sum($notSumOfA);
