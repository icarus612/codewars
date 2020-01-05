//https://www.codewars.com/kata/58ad0159c9e5b0399b0001b8
function knightRescue(N,x,y) {
    let z = x + y;
    let j = z % 2;
    let k = z % 3;
    N = N.filter((i)=> {
        if ((i + 1) % 2 == j) return i;
        if (i == 2) return i;
    });
    return N[0] != undefined;
}