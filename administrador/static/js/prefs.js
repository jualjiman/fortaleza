//=======================================CargandoPreferencias=================================================
$(function(){
	cargarPreferencias();
});

function cargarPreferencias(){

	jlocal = JSON.parse(localStorage.getItem(nstorange));
	if(jlocal !== null){

	    prefs = jlocal.f1.i + "-" + jlocal.f2.i;
	    $.ajax({
	        type: "POST",
	        url: "/preferencias/",  // or just url: "/my-url/path/"
	        data: {
	            prefs: prefs
	        },
	        success: function(data) {
	            $('#asking-block-row').html(data).hide().fadeIn();
	        },
	        error: function(xhr, textStatus, errorThrown) {
	        	$('#asking-block-row').html(xhr).hide().fadeIn();  
	        }
	    });
	}
}