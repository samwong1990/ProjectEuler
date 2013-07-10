<?php
function properDivisors($subject){
	$divisors = array();
	$n = $subject-1;
	while($n>0){
		if($subject % $n == 0)	$divisors[] = $n;
		$n--;
	}
	return $divisors;
}

function sumOfProperDivisors($divisors){
	return array_sum(properDivisors($divisors));
}

// print_r( properDivisors(220)	);
// echo array_sum(properDivisors(220));

$amicableNums = array();
for($i=1; $i<=10000; $i++){
	$seed = sumOfProperDivisors($i);
	$out = sumOfProperDivisors($seed);
	if(	$out == $i	&& $seed != $i) $amicableNums[$seed] = $i;
}
print_r($amicableNums);
echo "Answer = " . array_sum($amicableNums) . "\n";

// foreach($amicableNums as $num){
// 	print_r(properDivisors($num));
// }