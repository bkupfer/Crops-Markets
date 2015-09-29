
var regions = [
	{
		name: "Seleccione una region"
	},
	{
		name: "ARICA Y PARINACOTA",
		provinces: [
			{name: "Arica",			 communes: ["Arica", "Camarones"]},
			{name: "Parinacota",	 communes: ["Putre", "General Lagos"]}
		]
	},
	{
		name: "TARAPACÁ",
		provinces: [
			{name: "Iquique",		 communes: ["Iquique", "Alto Hospicio"]},
			{name: "Tamarugal",		 communes: ["Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]}
		]
	},
	{
		name: "ANTOFAGASTA",
		provinces: [
			{name: "Antofagasta",	 communes: ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal"]},
			{name: "El Loa",		 communes: ["Calama", "Ollagüe", "San Pedro de Atacama"]},
			{name: "Tocopilla",		 communes: ["Tocopilla", "María Elena"]}
		]
	},
	{
		name: "ATACAMA",
		provinces: [
			{name: "Copiapó",		 communes: ["Copiapó", "Caldera", "Tierra Amarilla"]},
			{name: "Chañaral",		 communes: ["Chañaral", "Diego de Almagro"]},
			{name: "Huasco",		 communes: ["Vallenar", "Alto del Carmen", "Freirina", "Huasco"]}
		]
	},
	{
		name: "COQUIMBO",
		provinces: [
			{name: "Elqui",			 communes: ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña"]},
			{name: "Choapa",		 communes: ["Illapel", "Canela", "Los Vilos", "Salamanca"]},
			{name: "Limarí",		 communes: ["Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]}
		]
	},
	{
		name: "VALPARAÍSO",
		provinces: [
			{name: "Valparaíso",	 communes: ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar"]},
			{name: "Isla de Pascua", communes: ["Isla de Pascua"]},
			{name: "Los Andes",		 communes: ["Los Andes", "Calle Larga", "Rinconada", "San Esteban"]},
			{name: "Petorca",		 communes: ["La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar"]},
			{name: "Quillota",		 communes: ["Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales"]},
			{name: "San Antonio",	 communes: ["San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo"]},
			{name: "San Felipe de Aconcagua",	 communes: ["San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María"]},
			{name: "Marga Marga",	 communes: ["Limache", "Quilpué", "Villa Alemana", "Olmué"]}
		]
	},
	{
		name: "DEL LIBERTADOR GRAL. BERNARDO O'HIGGINS",
		provinces: [
			{name: "Cachapoal",		 communes: ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente"]},
			{name: "Cardenal Caro",	 communes: ["Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones"]},
			{name: "Colchagua",		 communes: ["San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]}
		]
	},
	{
		name: "DEL MAULE",
		provinces: [
			{name: "Talca",			 communes: ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael"]},
			{name: "Cauquenes",		 communes: ["Cauquenes", "Chanco", "Pelluhue", ]},
			{name: "Curicó",		 communes: ["Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén"]},
			{name: "Linares",		 communes: ["Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]}
		]
	},
	{
		name: "DEL BIOBÍO",
		provinces: [
			{name: "Concepción",	 communes: ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén"]},
			{name: "Arauco",		 communes: ["Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Alamos", "Tirúa"]},
			{name: "Biobío",		 communes: ["Los Angeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"]},
			{name: "Ñuble",			 communes: ["Chillán", "Bulnes", "Cobquecura", "Coelemu", "Coihueco", "Chillán Viejo", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Treguaco", "Yungay"]}
		]
	},
	{
		name: "DE LA ARAUCANÍA",
		provinces: [
			{name: "Cautín",		 communes: ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol"]},
			{name: "Malleco",		 communes: ["Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"]}
		]
	},
	{
		name: "DE LOS RÍOS",
		provinces: [
			{name: "Valdivia",		 communes: ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli"]},
			{name: "Ranco",			 communes: ["La Unión", "Futrono", "Lago Ranco", "Río Bueno"]}
		]
	},
	{
		name: "DE LOS LAGOS",
		provinces: [
			{name: "Llanquihue",	 communes: ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas"]},
			{name: "Chiloé",		 communes: ["Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao"]},
			{name: "Osorno",		 communes: ["Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo"]},
			{name: "Palena",		 communes: ["Chaitén", "Futaleufú", "Hualaihué", "Palena"]}
		]
	},
	{
		name: "AISÉN DEL GRAL. CARLOS IBAÑEZ DEL CAMPO",
		provinces: [
			{name: "Coihaique",		 communes: ["Coihaique", "Lago Verde"]},
			{name: "Aisén",			 communes: ["Aisén", "Cisnes", "Guaitecas"]},
			{name: "Capitán Prat",	 communes: ["Cochrane", "O'Higgins", "Tortel"]},
			{name: "General Carrera",communes: ["Chile Chico", "Río Ibáñez"]}
		]
	},
	{
		name: "MAGALLANES Y DE LA ANTÁRTICA CHILENA",
		provinces: [
			{name: "Magallanes",		 communes: ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio"]},
			{name: "Antártica Chilena",	 communes: ["Cabo de Hornos (Ex-Navarino)", "Antártica"]},
			{name: "Tierra del Fuego",	 communes: ["Porvenir", "Primavera", "Timaukel"]},
			{name: "Ultima Esperanza",	 communes: ["Natales", "Torres del Paine"]}
		]
	},
	{
		name: "REGIÓN METROPOLITANA DE SANTIAGO",
		provinces: [
			{name: "Santiago",		 communes: ["Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura"]},
			{name: "Cordillera",	 communes: ["Puente Alto", "Pirque", "San José de Maipo"]},
			{name: "Chacabuco",		 communes: ["Colina", "Lampa", "Tiltil"]},
			{name: "Maipo",			 communes: ["San Bernardo", "Buin", "Calera de Tango", "Paine", ]},
			{name: "Melipilla",		 communes: ["Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro"]},
			{name: "Talagante",		 communes: ["Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]}
		]
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
