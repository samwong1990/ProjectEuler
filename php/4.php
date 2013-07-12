<?php
function is_palindromic($number){
	$str = "$number";
	$strlen = strlen($str);
	$limit = $strlen % 2 == 0	?	$strlen/2	:	$strlen/2 - 1;
	for($i=0; $i<$limit; $i++){
		if($str[$i] != $str[$strlen-$i-1]){
			// echo "$number is not polindromic\n";
			return false;
		}
	}
	// echo "$number is polindromic\n";
	return true;
}
/*test
is_palindromic(12321);
is_palindromic(123321);
is_palindromic(123211);
is_palindromic(112321);
endtest*/

$max = 0;
for($a = 100; $a<1000; $a++){
	for($b = 100; $b<1000; $b++){
		$subject = $a*$b;
		if(is_palindromic($subject) && $subject > $max){
			$max = $subject;
		}	
	}
}
echo $max . "is the answer";

