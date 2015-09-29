
var regions = [
	{
		name: "Seleccione una region"
	},
	{
		name: "Arica y Parinacota", 
		provinces: [{name: "Arica", communes: ["Arica", "Camarones"]},
					{name: "Parinacota", communes: ["Putre", "General Lagos"]}]
	},
	{
		name: "Tarapacá",
		provinces: [{name: "Iquique", communes: ["Iquique", "Alto Hospicio"]},
					{name: "Tamarugal", communes: ["Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]}]
	},
	{
		name: "Antofagasta",
		provinces: [{name: "Antofagasta", communes: ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal"]},
					{name: "El Loa", communes: ["Calama", "Ollagüe", "San Pedro de Atacama"]},
					{name: "Tocopilla", communes: ["Tocopilla", "María Elena"]}]
	}
];



$("#id_region").change( function(){
	var region = regions[$(this).val()];
	var provinceSelector = document.getElementById("id_province"); // $("#id_province");
	provinceSelector.length = 0;
	provinceSelector.options[0] = new Option('Seleccione provincia', '');
	provinceSelector.selectedIndex = 0;
	for (var i=0; i<region.provinces.length; i++){
		provinceSelector.options[i+1] = new Option( region.provinces[i].name, i );
	}
});

$("#id_province").change( function(){
	var region = regions[$("#id_region").val()];
	var province = region.provinces[$(this).val()];
	$("#province_trick").val(province.name);
	var communeSelector = document.getElementById("id_commune");
	communeSelector.length = 0;
	communeSelector.options[0] = new Option('Seleccione comuna', '');
	communeSelector.selectedIndex = 0;
	for (var i=0; i<province.communes.length; i++){
		communeSelector.options[i+1] = new Option( province.communes[i], province.communes[i] );
	}
});

/*
var chile = new Array[15];

chile[0] = "";
chile[1] = Region(
	
	)




////////////////////////////////////

var region_arr = new Array["ARICA Y PARINACOTA ", "TARAPACÁ ","TARAPACÁ ", "ANTOFAGASTA "]; 

var s_a = new Array();
s_a[0] = "Arica|Parinacota";
s_a[1] = "Iquique|Tamarugal";
s_a[2] = "Iquique|Alto Hospicio";
s_a[3] = "Pozo Almonte";
s_a[4] = "";
s_a[5] = "";
s_a[6] = "";
s_a[7] = "";
s_a[8] = "";
s_a[9] = "";
s_a[10] = "";
s_a[11] = "";
s_a[12] = "";
s_a[13] = "";
// s_a[] = "";
// s_a[] = "";

function print_region(region){

}


function print_province(province, selectedIntex){


}


function print_commune(commune, selectedIndex){

}



var country_arr = new Array("Afghanistan", "India", "USA", "Vietnam");

var s_a = new Array();
s_a[0]="";
s_a[1]="Badakhshan|Badghis|Baghlan|Balkh|Bamian|Farah|Faryab|Ghazni|Ghowr|Helmand|Herat|Jowzjan|Kabol|Kandahar|Kapisa|Konar|Kondoz|Laghman|Lowgar|Nangarhar|Nimruz|Oruzgan|Paktia|Paktika|Parvan|Samangan|Sar-e Pol|Takhar|Vardak|Zabol";
s_a[2]="Andhra Pradesh|Arunachal Pradesh|Assam|Bihar|Chhattisgarh|Goa|Gujarat|Haryana|Himachal Pradesh|Jammu and Kashmir|Jharkhand|Karnataka|Kerala|Madhya Pradesh|Maharashtra|Manipur|Meghalaya|Mizoram|Nagaland|Odisha(Orissa)|Punjab|Rajasthan|Sikkim|Tamil Nadu|Tripura|Uttar Pradesh|Uttarakhand|West Bengal";
s_a[3]="Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|ansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming";

s_a[4]="Ba Ria|Bạc Liêu|Bắc Giang|Bắc Ninh|Bảo Lộc|Biên Hòa|Bến Tre|Buôn Ma Thuột|Cà Mau|Cam Pha|Cao Lãnh|Đà Lạt|Điện Biên Phủ|Đông Hà|Đồng Hới|Hà Tĩnh|Hạ Long|Hải Dương|Hòa Bình|Hội An|Huế|Hưng Yên|Kon Tum|Lạng Sơn|Lào Cai|Long Xuyên|Móng Cái|Mỹ Tho|Nam Định|Ninh Bình|Nha Trang|Cam Ranh|Phan Rang-Tháp Chàm|Phan Thiết|Phủ Lý|Pleiku|Quảng Ngãi|Quy Nhơn|Rạch Giá|Sóc Trăng|Sơn La|Tam Kỳ|Tân An|Thái Bình|Thái Nguyên|Thanh Hóa|Trà Vinh|Tuy Hòa|Tuyen Quang|Uong Bi|Việt Trì|Vinh|Vĩnh Yên|Vĩnh Lon|Vũng Tàu|Yên Bái";

function print_country(country){
	//given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(country);
	option_str.length=0;
	option_str.options[0] = new Option('Select Country','');
	option_str.selectedIndex = 0;
	for (var i=0; i<country_arr.length; i++) {
	option_str.options[option_str.length] = new Option(country_arr[i],country_arr[i]);
	}
}

function print_state(state, selectedIndex){
	var option_str = document.getElementById(state);
	option_str.length=0;    // Fixed by Julian Woods
	option_str.options[0] = new Option('Select State','');
	option_str.selectedIndex = 0;
	var state_arr = s_a[selectedIndex].split("|");
	for (var i=0; i<state_arr.length; i++) {
	option_str.options[option_str.length] = new Option(state_arr[i],state_arr[i]);
	}
}
*/