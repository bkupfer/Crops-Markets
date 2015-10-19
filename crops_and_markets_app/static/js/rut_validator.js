/* returns:	true if given rut is valid, false otherwise */
function validateRut(input){
	re = new RegExp(/(\.|-|\s)/, 'g');
	input = input.replace(re, '');
	var digits = input.substring(0, input.length-1);
	var verifyingDigit = input.charAt(input.length-1);
	var products = [];
	var multiplier = 2;
	for (var i=digits.length-1; i>=0;i--){
		if (multiplier > 7)
			multiplier = 2;
		products[i] = multiplier * parseInt(digits[i]);
		multiplier ++;
	}
	var sum = 0;
	for (var i=0; i<products.length; i++)
		sum += products[i];
	var rem = 11 - (sum % 11);
	if (rem == verifyingDigit)
		return true;
	if (rem == 0 && verifyingDigit == '0')
		return true;
	if (rem == 10 && verifyingDigit == 'k')
		return true;
	return false;
}

function formatDigits(digits){
	return (digits.length <= 3) ? digits : formatDigits(digits.substring(0, digits.length-3)) + "." + digits.substring(digits.length-3, digits.length);
}

/* transforms a rut into xx.xxx.xxx-x format */
function formatRut(input){
	input = input.toLowerCase().trim();
	re = new RegExp(/(\.|-|\s)/, 'g');
	input = input.replace(re, '');
	var digits = input.substring(0,input.length-1);
	formatedDigits = formatDigits(digits);
	var verifyingDigit = input.charAt(input.length-1);
	return formatedDigits + '-' + verifyingDigit;
}

/* validates and gives format to ruts */
$(".rut").change(function(){
	var formatedInput = formatRut($(this).val());
	$(this).val(formatedInput);
	if (!validateRut(formatedInput))
		alert("Rut ingresado no es válido");
});