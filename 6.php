<?php
function sum_of_squares($items){
	$sum = 0;
	foreach($items as $n){
		$sum += $n*$n;
	}
	return $sum;
}

function sum_then_square($items){
	$sum = array_sum($items);
	return $sum*$sum;
}

$items = range(1,100);
echo sum_then_square($items) - sum_of_squares($items) . "\n";