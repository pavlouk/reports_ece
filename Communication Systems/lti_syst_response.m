%% starting point 
%
clc;
clear all;
close all;
scrsz = get(0, 'ScreenSize');

%% axis parameters
%
Td = 10e-3;
T0 = 0;
Te = 10e-3;
tstep = 50e-6;

t = T0:tstep:Te;

%% creating signal 
%
f1 = 0.5e3;
f2 = 2.5e3;

inputs = sin(2*pi*f1*t) + sin(2*pi*f2*t);

ht = [-0.031 0.0586 0.0743 0.1018 0.129 0.1484 0.155 ...
    0.1484 0.129 0.1018 0.0743 0.0586 -0.031];

%% calculate convolution
%
[outputs, len] = convolute(ht, inputs);

out = conv(ht, inputs);

%% graphing outputs
% 
figure('Position', [50 100 scrsz(3)*0.7 scrsz(4)*0.75]);
set(gcf, 'color', 'white');
FontSize = 14;
set(gcf,'DefaultLineLineWidth',2);
set(gcf,'DefaultTextFontSize', FontSize, 'DefaultAxesFontSize', FontSize,...
    'DefaultLineMarkerSize', 0.25*FontSize);
subplot(1, 2, 1);
plot(t, inputs);
grid on
xlabel('Time [msecs]');
ylabel('Amplitude [Volts]');


t2 = T0:tstep:(length(out) - 1)*tstep;
subplot(1, 2, 2);
plot(t2, out);
grid on
xlabel('Time [msecs]');
ylabel('Amplitude [Volts]');