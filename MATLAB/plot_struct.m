function [] = plot_struct(coordenadas,indices_nodos)
%plot_struct. Esta función grafica la malla de la estructura. Su sintaxis
% es: plot_struct(coordenadas,indices_nodos) donde "coordenadas" es el
% arreglo con las coordenadas de los nodos y ....

figure
hold on

n_elem = size(indices_nodos,1);

for e=1:n_elem

    i = indices_nodos(e,1); % Indice de nodo inicial
    j = indices_nodos(e,2); % Indice de nodo final
    
    xi = coordenadas(i,1); % Coordenada x del nodo inicial
    xj = coordenadas(j,1); % Coordenada x del nodo fianl
    
    yi = coordenadas(i,2); % Coordenada y del nodo inicial
    yj = coordenadas(j,2); % Coordenada y del nodo final
    
    plot([xi xj],[yi yj], '-ok')
end

axis equal

end