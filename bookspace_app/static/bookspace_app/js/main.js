$(() => {

    $(".contenedor_Encabezado").fadeOut();
    $(".logo").fadeOut();
    $(".contenedor_Enlaces").fadeOut();
    $(".contenedor_Imagen").fadeOut();
    $(".contenedor_Footer").fadeOut();
    

    
    $(".contenedor_Encabezado").fadeIn(1000);
    $(".logo").fadeIn(3000);
    $(".contenedor_Encabezado").fadeIn(1000);   
    $(".contenedor_Enlaces").fadeIn(1100);
    $(".contenedor_Imagen").fadeIn(1150);
    $(".contenedor_Footer").fadeIn(1200);


    $('.contenedor_Imagen img').hover(
        function () {
            $(this).css({
                transform: 'scale(1.05)',
                filter: 'brightness(1.2)',
                transition: 'transform 0.3s ease, filter 0.3s ease'
            });
        },
        function () {
            $(this).css({
                transform: 'scale(1)',
                filter: 'brightness(1)',
                transition: 'transform 0.3s ease, filter 0.3s ease'
            });
        }
    );


})

