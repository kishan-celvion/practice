const soap = require('soap');

const url = "http://www.dneonline.com/calculator.asmx?WSDL";

soap.createClient(url, function(err, client) {
  if (err) throw err;

  client.Add({ intA: 5, intB: 3 }, function(err, result) {
    if (err) throw err;

    console.log(result.AddResult); // Output: 8
  });
});