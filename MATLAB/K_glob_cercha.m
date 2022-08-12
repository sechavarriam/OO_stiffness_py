function [K] = K_glob_cercha(E, A, L, theta)
% [K] = K_glob_cercha(E, A, e)
%   e: Indice del elemento


K_local = (E*A/L)* [1 0 -1 0; 0 0 0 0;-1 0 1 0; 0 0 0 0];

T = [        cosd(theta)  sind(theta)  0 0;...
            -sind(theta)  cosd(theta)  0 0;... 
        0 0  cosd(theta)  sind(theta); ...
        0 0 -sind(theta)  cosd(theta) ];

K = T'* K_local*T;

end