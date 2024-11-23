%% starting point 
%
clc;
clear all;
close all;
scrsz = get(0, 'ScreenSize');

%% axis parameters
%
Td = 1;
T0 = 0;
Te = 1;
Ta1 = 0.3;
Ta2  = 0.7;
tstep = 0.01;

t = T0:tstep:Te;

N = Td/tstep + 1;

%% initialisation of both Pi pulses
%
P = zeros(1, N);
na1 = (Ta1 - T0)/tstep + 1;
na2 = (Ta2 - T0)/tstep + 1;

P(ceil(na1):ceil(na2)) = 1;

P1 = P;
P2 = P;
%% convolution process
%
N1 = length(P1);
N2 = length(P2);

extP1 = [zeros(1, N2 - 1) P1 zeros(1, N2 - 1)];
convP1P2 = zeros(1, N1 + N2 - 1);
for m=1:N1 + N2 - 1
    cval = 0;
    for n=1:N2
        cval = cval + extP1(m + n -1)*P2(N2 - n + 1);
    end
    convP1P2(m) = cval;
end

realconv = conv(P1, P2);

%% setting the window of the results
%
figure('Position', [50 100 scrsz(3)*0.75 scrsz(4)*0.75]);
set(gcf, 'color', 'white');
FontSize = 14;
set(gcf,'DefaultLineLineWidth',2);
set(gcf,'DefaultTextFontSize', FontSize, 'DefaultAxesFontSize', FontSize,...
    'DefaultLineMarkerSize', 0.25*FontSize);

%% figure 1
%
myfugures(1) = subplot(1, 3, 1);
plot(t, P1, '.-b');
grid on
xlabel('Time [secs]');
ylabel('Amplitude [Volts]');
axis([min(floor(t)) max(ceil(t)) min(P1) max(P1)]);

%% figure 2
%
myfigures(2) = subplot(1, 3, 2);
t1 = T0:tstep:(length(convP1P2) - 1)*tstep;
plot(t1, convP1P2, '.-k');
grid on
xlabel('Time [secs]');
ylabel('Amplitude [Volts]');
axis([min(floor(t1)) max(ceil(t1)) min(convP1P2) max(convP1P2)]);

%% figure 3
%
myfigures(2) = subplot(1, 3, 3);
t2 = T0:tstep:(length(realconv) - 1)*tstep;
plot(t2, realconv, '.-r');
grid on
xlabel('Time [secs]');
ylabel('Amplitude [Volts]');
axis([min(floor(t2)) max(ceil(t2)) min(realconv) max(realconv)]);


