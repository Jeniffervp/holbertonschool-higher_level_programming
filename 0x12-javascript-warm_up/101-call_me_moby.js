#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let mo = 0; mo < x; mo++) {
    theFunction();
  }
};
