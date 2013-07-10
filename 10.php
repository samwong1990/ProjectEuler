<?php
$stopAt = 2000000;
//gmp not available >_<
//let's do it with Sieve_of_Eratosthenes
//This
$primes = array();
$primes[] = 1;
for($i=1; $i<$stopAt; $i++){
	if($i % 2 != 1) continue; 
	$d = 3; 
	$x = sqrt($i); 
	while ($i % $d != 0 && $d < $x) $d += 2; 
	if((($i % $d == 0 && $i != $d) * 1) == 0){
		$primes[] = $i; 
	} 
}
echo array_sum($primes) . "\n";