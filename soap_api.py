import zeep

# WSDL URL (defines the API contract)
wsdl = "http://www.dneonline.com/calculator.asmx?WSDL"

client = zeep.Client(wsdl=wsdl)

# Call the SOAP method
result = client.service.Add(intA=5, intB=3)

print(result)  # Output: 8