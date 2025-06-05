% Estado actual de sensores por zona
% Formato: humedad_suelo(Zona, Nivel).
humedad_suelo(zona1, baja).
humedad_suelo(zona2, media).

% Formato: temperatura(Zona, GradosC).
temperatura(zona1, 35).
temperatura(zona2, 30).

% Hora (misma hora para todas las zonas)
hora(20).  % 8 PM

% Probabilidad de lluvia global
prob_lluvia(false).


% Reglas del sistema por zona
% Hora adecuada
hora_adecuada :-
    hora(H),
    (H < 10 ; H > 18).

% Calor extremo por zona
alerta_calor(Zona) :-
    temperatura(Zona, T),
    T >= 32.

% Activación de riego por zona
activar_riego(Zona) :-
    humedad_suelo(Zona, baja),
    prob_lluvia(false),
    hora_adecuada.

% Evaluar estado del riego por zona
estado_riego(Zona, 'Activado') :-
    activar_riego(Zona),
    \+ alerta_calor(Zona).

estado_riego(Zona, 'Activado con alerta por calor extremo') :-
    activar_riego(Zona),
    alerta_calor(Zona).

estado_riego(Zona, 'Desactivado con alerta por calor extremo') :-
    \+ activar_riego(Zona),
    alerta_calor(Zona).

estado_riego(Zona, 'No activado') :-
    \+ activar_riego(Zona),
    \+ alerta_calor(Zona).

% Recomendación final por zona
recomendacion(Zona) :-
    estado_riego(Zona, Estado),
    format('Zona ~w: ~w~n', [Zona, Estado]).