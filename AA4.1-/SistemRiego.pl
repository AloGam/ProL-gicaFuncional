%Estado de sensores
humedad_suelo(baja).
temperatura(35).
hora(20).
prob_lluvia(false).

%Regla: ¿es la hora adecuada para regar?
hora_adecuada :- hora(H), (H < 10 ; H > 18).

%Regla principal: ¿Cuando se activa el riego?
activar_riego :-
    humedad_suelo(baja),
    prob_lluvia(false),
    hora_adecuada.

%Diagnostico del sistema
estado_riego('Activado') :- activar_riego.
estado_riego('No Activado') :- \+ activar_riego.

%Regla para alerta de temperatura extrema
alerta_calor :-
    temperatura(T),
    T >= 32.

%Mensaje de alerta si se activa el riego por calor extremo
recomendacion :-
    activar_riego,
    alerta_calor, !,
    writeln('Alerta: Activado con alerta por calor extremo').

recomendacion :- 
    activar_riego, !,
    writeln('Activado sin alerta de calor').

recomendacion :-
    writeln('Alerta: Desactivado').