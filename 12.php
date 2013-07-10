<?php
$currentTriNum = 1;
$triangleAdd = 2;
while(divisors($currentTriNum) <= 500){
	$currentTriNum += $triangleAdd;
	$triangleAdd++;
}
echo "Ans = $currentTriNum\n";

function divisors($num){
	$divisors = 0;
	for($i=1; $i<=sqrt($num); $i++){
		if($num % $i == 0)	$divisors++;
	}
	// echo "$num has $divisors divisors\n";
	return $divisors*2;
	
}