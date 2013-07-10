<?php
//Plain lcm, googled lcm algo.
//Credits: tembenite at gmail dot com, cornelius at skjoldhoej dot dk
echo lcm_arr(range(1,20)) . "\n";

function lcm_arr($items){
    //Input: An Array of numbers
    //Output: The LCM of the numbers
    while(2 <= count($items)){
        array_push($items, lcm(array_shift($items), array_shift($items)));
    }
    return reset($items);
}

function gcd($n, $m) {
   $n=abs($n); $m=abs($m);
   if ($n==0 and $m==0)
       return 1; //avoid infinite recursion
   if ($n==$m and $n>=1)
       return $n;
   return $m<$n?gcd($n-$m,$n):gcd($n,$m-$n);
}

function lcm($n, $m) {
   return $m * ($n/gcd($n,$m));
}