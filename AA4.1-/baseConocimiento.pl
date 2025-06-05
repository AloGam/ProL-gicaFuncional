%Estado actual de los sensores
    %La humedad del suelo esta baja
    %La temperatura es de 35 grados
    %Son las 20 horas (8pm)
    %No se espera lluvia (prob. lluvia)

%Regla del sistema
    %1.- El sistema considera que la hora adecuada para regar si es antes de las 10am o despues de las 6pm
    %2.- El riego de activa autamaticamente sí:
        %La humedad del del suelo es baja
        %no se pronostica lluvia
        %Y es una hora adecuada para regar
    %3.- Si el riego esta activo, se registra el estado como "Activado"; si no, como "No activado"
    %4.- Alerta por condiciones extremas:
        %Si la temperatura es mayor o igual a 32°C, se activa una alerta por calor extremo.
        %Si el riego se activa bajo estas condiciones, el sistema emite una recomendacion:
            %se registra como "Activado con alerta por calor extremo"
    %5.- En caso contrario:
        %indica estado "Desactivado con alreta por calor extremo"