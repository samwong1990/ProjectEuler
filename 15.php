0 0 1 1
0 1 1 0
1 1 0 0
0 1 0 1
1 0 1 0
1 0 0 1

[0,0,1,1]

so I am simply looking for distinguishable perms of this list

so it is 40P40/(20!*20!)

<?php
function factorial($n){
	$product = 1;
	while($n>0){
		$product *= $n;
		$n--;
	}
	return $product;
}

echo "Answer = " . factorial(40)/(factorial(20)*factorial(20)) . "\n";
