var nstorange = "clfFavs1134253563585236726482564348237";

$(function(){
    //
});

function ocultandoInfo(){
	$('.alert-info').hide();
	$('.alert-danger').hide();
	$('.alert-warning').hide();
}

function limpiandoFormulario(){
	$('#id_nombre').val("");
    $('#id_email').val("");
    $('#id_mensaje').val("");
}

$("#btnSearch").click(function(e){
    if($("#id_pista").val() === ""){
        e.preventDefault();
        return false;
    }
});

$("#btnSend").click(function(e){
    e.preventDefault();
    ocultandoInfo();
     var name = $('#id_nombre').val();
     var email = $('#id_email').val();
     var message = $('#id_mensaje').val();
     var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if( name !== "" && email !== "" && message !== ""){
    	if( email_regex.test(email) === true ){
            $.ajax({
                type: "POST",
                url: "/contacto/",  // or just url: "/my-url/path/"
                data: {								    
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    name: name,
                    email: email,
                    message: message
                },
                success: function(data) {
                	limpiandoFormulario();
                    $('.alert-info').text('Mensaje enviado, en breve le atenderemos. Muchas gracias!').hide().fadeIn();
                },
                error: function(xhr, textStatus, errorThrown) {
                    $('.alert-danger').text("Ups! Algo fallo, por favor intente más tarde").hide().fadeIn();
                }
            });
    	}
    	else{
			$('.alert-warning').text('El formato de email que ingreso es invalido').hide().fadeIn();
		}	
    }
    else{
        $('.alert-warning').text('Todos los campos son requeridos').hide().fadeIn();
    }
});

$(".modalbtn").click(function(e){
    e.preventDefault();
    var info = $(this).attr("href");
    var vals = info.split("-");

    var idp = vals[0];
    var nim = vals[1];

    $.ajax({
        type: "POST",
        url: "/imgProducto/",  // or just url: "/my-url/path/"
        data: {	
        	csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),							    
            idp: idp,
            nim: nim
        },
        success: function(data) {
             $('#modal-cont').html(data);
             $('.bs-example-modal-lg').modal('show');
        },
        error: function(xhr, textStatus, errorThrown) {
            // $('#modal-cont').text(xhr.responseText);
            $('#modal-cont').text("Error al cargar la imagen");
        }
    });
});

//opacity navbar menu
$(document).on("scroll",function(){
    if($(document).scrollTop()>100){
        $("header").addClass("navbar-opacity");
        // $("#mainContent").addClass("smallTopAutoPadding").removeClass("topAutoPadding");

    } else{
        $("header").removeClass("navbar-opacity");
        // $("#mainContent").addClass("topAutoPadding").removeClass("smallTopAutoPadding");
    }
});
