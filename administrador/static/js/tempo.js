$(function(){
	analisandoPreferencias();
});

var enableShowLog = false;

var id = 0;
var tPermanencia = 0;

var local;
var favs = {
	f1:{t:0,i:0},
	f2:{t:0,i:0},
	init: false
};

function analisandoPreferencias(){
	id = $("#mid").val();
	local = JSON.parse(localStorage.getItem(nstorange));
	if(local !== null){
		favs = local;
		if(id === favs.f1.i)
			tPermanencia = favs.f1.t;
		else if(id === favs.f2.i)
			tPermanencia = favs.f2.t;
		showPreferences();
	}
    setInterval(temporizador,2000);
}

function temporizador(){
    tPermanencia++;
    guardarPermanencia();
}

function guardarPermanencia(){
	// Check browser support
	if (typeof(Storage) != "undefined") {

	    if(tPermanencia > favs.f1.t){
	    	if(favs.f2.t == favs.f1.t){
	    		favs.f2.i = favs.f1.i;
	    	}
	    	favs.f1.t = tPermanencia;
	    	favs.f1.i = id;
	    	favs.init = true;
	    }
	    else if(tPermanencia > favs.f2.t && id !== favs.f1.i){
	    	favs.f2.t = tPermanencia;
	    	favs.f2.i = id;
	    	favs.init = true;
	    }
	    // Store
	    localStorage.setItem(nstorange, JSON.stringify(favs));
	    showPreferences();
	}
}

function enableShowPreferences(opt){
	enableShowLog = opt;
}

function showPreferences(){
	if(enableShowLog)
	console.log("[i:" +favs.f1.i + " t:" + favs.f1.t + "][i:" + favs.f2.i + " t:" + favs.f2.t + "] init:" + favs.init);
}

