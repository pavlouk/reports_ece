x = -50:0.01:50;
y = 1i*exp(-1i*x)./x + exp(-1i*x)./x.^2 - 1./x.^2;
f = sqrt(real(y).^2 + imag(y).^2);
subplot(1,2,1)
plot(x,f), xlabel('\Omega'), ylabel('|X(\Omega)|'), axis([-50 50 0 2.5])
y = 1i*exp(-1i*x)./x + exp(-1i*x)./x.^2 - 1./x.^2 +...
    1i*exp(-1i*(-x))./(-x) + exp(-1i*(-x))./x.^2 - 1./x.^2 +...
    exp(1i*x).*(1i*exp(-1i*x)./x + exp(-1i*x)./x.^2 - 1./x.^2) +...
    exp(-1i*x).*(1i*exp(-1i*(-x))./(-x) + exp(-1i*(-x))./x.^2 - 1./x.^2);
f = sqrt(real(y).^2 + imag(y).^2);
subplot(1,2,2)
plot(x,f), xlabel('\Omega'), ylabel('|G(\Omega)|'), axis([-50 50 0 2.5])
