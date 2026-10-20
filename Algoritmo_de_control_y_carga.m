% Reto 3
% Jose Alirio Benavides
% Algoritmo de control y cargas para una micro-red eléctrica (24h)

clear; clc;

% 1. Parámetros del sistema
Capacidad_Bat = 100;          % Capacidad total de la batería en kWh
SOC_actual = 50;              % Estado de carga inicial (50%)

% 2. Vectores de Generación y Demanda
E_gen = [0, 0, 0, 0, 0, 5, 15, 30, 45, 60, 75, 80, 85, 80, 70, 50, 30, 10, 2, 0, 0, 0, 0, 0];
E_dem = [20, 18, 15, 15, 18, 25, 40, 50, 45, 40, 35, 35, 40, 45, 50, 55, 60, 65, 50, 40, 30, 25, 22, 20];

% Inicialización de vectores para almacenar resultados hora a hora
SOC_vector = zeros(1, 24);

% Encabezado del reporte por consola
fprintf('Hora | E_gen | E_dem | Balance | SOC(%%) | Escuela | Bombeo | Alumbrado\n');
fprintf('---------------------------------------------------------------------\n');

% 3. Bucle principal de 24 horas (t = 1 hasta 24)
for t = 1:24

    % Balance energético en la hora t
    Balance = E_gen(t) - E_dem(t);

    if Balance >= 0

        Excedente = Balance;

        % Cargar la batería con el excedente
        SOC_nuevo = SOC_actual + (Excedente / Capacidad_Bat) * 100;

        % Limitar el SOC máximo al 100%
        if SOC_nuevo > 100
            SOC_nuevo = 100;
        end

        % Cargas activas (Ruta Segura / Todas activas)
        Cargas_Escuela = true;
        Cargas_Bombeo = true;
        Cargas_Alumbrado = true;

    else
        % --- CASO DE DÉFICIT (Balance < 0) ---
        Deficit = abs(Balance);

        % Descargar la batería para cubrir el faltante
        SOC_nuevo = SOC_actual - (Deficit / Capacidad_Bat) * 100;

        % Aplicación de reglas de desconexión de cargas
        if SOC_nuevo > 40
            % Ruta Segura: Todos los servicios activos
            Cargas_Escuela = true;
            Cargas_Bombeo = true;
            Cargas_Alumbrado = true;

        elseif SOC_nuevo > 20 && SOC_nuevo <= 40
            % Ruta de Alerta: Apagar alumbrado público
            Cargas_Escuela = true;
            Cargas_Bombeo = true;
            Cargas_Alumbrado = false;

        else
            % Ruta de Emergencia: Prioridad escuela (Apagar bombeo y alumbrado)
            Cargas_Escuela = true;
            Cargas_Bombeo = false;
            Cargas_Alumbrado = false;

            % Evitar que el SOC baje del 0%
            if SOC_nuevo < 0
                SOC_nuevo = 0;
            end
        end
    end

    % Actualizar el valor del SOC para la siguiente hora
    SOC_actual = SOC_nuevo;
    SOC_vector(t) = SOC_actual;

    % --- REPORTE POR HORA A HORA  ---
    if Cargas_Escuela, esc = 'true'; else, esc = 'false'; end
    if Cargas_Bombeo, bom = 'true'; else, bom = 'false'; end
    if Cargas_Alumbrado, alu = 'true'; else, alu = 'false'; end

    fprintf('%4d | %5.1f | %5.1f | %7.1f | %7.1f | %7s | %6s | %9s\n', ...
        t, E_gen(t), E_dem(t), Balance, SOC_actual, ...
        esc, bom, alu);
end