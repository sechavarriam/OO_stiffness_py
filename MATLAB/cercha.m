%% 0. Malla

l0 = 1.32; % [m]

coord = [   ... 
       0  0;... nodo 1
       0 l0;... nodo 2
      l0  0;... nodo 3
      l0 l0;... nodo 4
    2*l0  0;... nodo 5
    2*l0 l0;... nodo 6
    3*l0  0;... nodo 7
    3*l0 l0;... nodo 8
    4*l0  0;... nodo 9
    4*l0 l0];%  nodo 10

nodos = [...
    1 2;... 1
    2 4;... 2
    1 4;... 3
    1 3;... 4
    3 4;... 5
    4 6;... 6
    3 6;... 7
    3 5;... 8
    5 6;... 9
    6 8;... 10
    6 7;... 11
    5 7;... 12
    7 8;... 13
    8 10;...14
    8 9;... 15
    7 9;... 16
    9 10]; %17

n_nodos = size(coord,1);
n_elem = size(nodos,1);

DoF = 2*n_nodos; % Grados de libertad totales de la estructura.

% === GRAFICA DE LA ESTRUCTURA ================
plot_struct(coord,nodos)
% =============================================

% axis equal
%% 1. Asignación de propiedades

E = 200;   % [GPa] - Módulo de elasticidad.
E = E*1e6; % [kPa]

A = 5e-4; % [m]^2 - Área de la seccion transversal de los elementos.


Ke =  cell (n_elem,1); % Arreglo para almacenar las matrices globales por elemento

for e=1:n_elem

    i = nodos(e,1); % Indice de nodo inicial
    j = nodos(e,2); % Indice de nodo final
    
    xi = coord(i,1); % Coordenada x del nodo inicial
    xj = coord(j,1); % Coordenada x del nodo fianl
    
    yi = coord(i,2); % Coordenada y del nodo inicial
    yj = coord(j,2); % Coordenada y del nodo final

    L = sqrt((xj-xi)^2+(yj-yi)^2);
    theta = atan2d((yj-yi),(xj-xi));

    Ke{e} = K_glob_cercha(E, A, L, theta);

end




%% Ensamble matriz global de la estructura





K = zeros(DoF);

for e=1:n_elem
    % Elemento e ====================

    ni = nodos(e,1); % índice del nodo inicial del elemento 1.
    nj = nodos(e,2); % índice del nodo final del elemento 1
    
    % indices de posición de los grados de libertad en la matriz.
    
    % Para nodo i (inicial)
    i_2 = 2*ni;
    i_1 = 2*ni - 1;
    %pos_i_1 = pos_i_2 - 1; % Formulación equivalente
      
    % Para nodo j (final)
    j_2 = 2*nj;
    j_1 = 2*nj - 1;
    
    K(i_1:i_2,i_1:i_2)...
       = K(i_1:i_2,i_1:i_2) + Ke{e}(1:2,1:2);
    
    K(i_1:i_2,j_1:j_2)...
       = K(i_1:i_2,j_1:j_2) + Ke{e}(1:2,3:4);
    
    K(j_1:j_2,i_1:i_2)...
       = K(j_1:j_2,i_1:i_2) + Ke{e}(3:4,1:2);
    
    K(j_1:j_2,j_1:j_2)...
       = K(j_1:j_2,j_1:j_2) + Ke{e}(3:4,3:4);
end

% Acá ya tenemos lista nuestra matriz de rigidez

rest_index = [5 6 10 13 14 19];

free_index = [1 2 3 4 7 8 9 11 12 15 16 17 18 20];


K_nn = K(free_index,free_index);

K_aa = K(rest_index,rest_index);

K_na = K(free_index,rest_index);
K_an = K(rest_index,free_index); % = K_na'


K_reordenada = ...
    [K_nn, K_na;...
     K_an, K_aa];

% figure
% spy(sparse(K))
% figure
% spy(sparse(K_reordenada))

%% Vector de fuerzas

qa = [0 0 0 0 0 0]'; % Vector de desplazamientos conocidos

Qn = [10 -5 0 0 0 0 0 0 7 0 0 12 0 0]'; % Vector de fuerzas conocidas.

%% Solución 

% Cálculo de los desplazamientos desconocidos.

% x = A/b; (Sintaxis del solver de MATLAB) para resolver Ax=b.

qn = K_nn\(Qn-K_na*qa);

% Cálculo de las reacciones.

Qa = K_an*qn + K_aa*qa;


% Cálculo de la gráfica deformada

new_coord = coord;

for n = 1:n_nodos

 %free_index    

end




