<?php
function factorial($n){
	$product = '1';
	while($n>0){
		$product = bcmul($product, "$n");
		$n--;
	}
	return $product;
}

function sumDigits($str){
	$sum=0;
	for($i=0; $i<strlen($str); $i++){
		$sum += $str[$i];
	}
	return $sum;
}
echo "Answer = " . sumDigits(factorial(100)) . "\n";
