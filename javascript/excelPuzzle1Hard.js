// https://www.codewars.com/kata/571b93687beb0a8ade000a80/train/javascript

function solveIt(excel){
    let w = {};
    row = excel.map(i => i.slice(0, i.length - 1).reduce((x,y) => x + y) - i[i.length -1]);
    col = [];
    for (let x = 0; x < excel.length; x++) {
        col.push(excel.map((val) => val[x]).slice(0, excel.length - 1).reduce((x,y) => x + y) - excel[excel.length -1][x]);
    }
    for (let i = 0; i < excel.length; i++) {
      if (col[i] != 0) w["c"] = [i, col[i]];
      if (row[i] != 0) w["r"] = [i, row[i]];
    }
    if (w.c[0] == excel.length - 1) {
      return excel[w.r[0]][w.c[0]] + (w.r[1]);
    } else if (w.r[0] == excel.length - 1) {
      return excel[w.r[0]][w.c[0]] + (w.c[1]);
    } else {
      return excel[w.r[0]][w.c[0]] - (w.r[1]);
    }
  
  }