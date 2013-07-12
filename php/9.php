<?php

for($m=1; $m<1000; $m++){
	for($n=1; $n<$m; $n++){
		$a=$m*$m-$n*$n;
		$b=2*$m*$n;
		$c=$m*$m+$n*$n;
		$sum = $a+$b+$c;
		$k = 1;
		while($sum <= 1000){
			if($a+$b+$c == 1000){
				echo "a=$a b=$b c=$c\n";
				$prod = $a*$b*$c;
				echo "$prod\n";
				die();
			}
			$a *= $k;
			$b *= $k;
			$c *= $k;
			$k++;
			$sum = $a+$b+$c;
		}
	}
}
echo "no solution";