function [conv_sign, n] = convolute(sign_A, sign_B)
% convolute.m 
%   Calculate the convolution of the discrete input signals 
%   The output will return both the signal and its length

N1 = length(sign_A);
N2 = length(sign_B);

extsign_A = [zeros(1, N2 - 1) sign_A zeros(1, N2 - 1)];
conv_sign = zeros(1, N1 + N2 - 1);
for m = 1:N1 + N2 - 1
    cval = 0;
    for n = 1:N2
        cval = cval + extsign_A(m + n -1)*sign_B(N2 - n + 1);
    end
    conv_sign(m) = cval;
end
n = N1 + N2 - 1;

end

