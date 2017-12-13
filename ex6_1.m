%--------------------------------------------------------------------------
%   Πανεπιστήμιο Πατρών
%   Τμήμα Ηλεκτρολόγων Μηχανικών και Τεχνολογίας Υπολογιστών
%   Εργαστήριο του μαθήματος ΣΥΣΤΗΜΑΤΑ ΕΠΙΚΟΙΝΩΝΙΩΝ 
%--------------------------------------------------------------------------
%   Παράδειγμα 6.1
%   Έκδοση:      1.0       
%   Ημερομηνία:  1/10/2015
%--------------------------------------------------------------------------
%   Σχόλια:   Παράδειγμα δημιουργίας σήματος 2PAM με RC ή RRC φίλτρο
%--------------------------------------------------------------------------
close all;
clear all;
clc;

%%      Parameters
Nbits = 5000;            % Πλήθος bits
Rbits = 1000;            % Ρυθμός μετάδοσης  (bps)

%  Φίλτρο RC/RRC
    rr = 0.05;               %  RC roll-off factor
    Nup = 4;                 %  Upsampling rate
    rgd = 4;                 %  RC group delay
    Rsam = Nup*Rbits;        %  Clock rate στον DAC
    
    disp_ind = 1;            % 0 : RRC, ~0 : RC
    disp_delay = 0.001;        % display delay in secs
    
%  Display parameters
    Ndisp = 24*Nup;               %  Display update parameters
    Nfft = 512;                   %  FFT points
    Nmax = max(Nfft, Ndisp);
    SWcoefs = spectrum.welch('Rectangular', Nfft);
    avind = 1;                   % PSD averaging,  0 = no averaging
    aval = 0;                    %  averaging initial value
    Dpsd = psd(SWcoefs, zeros(Nfft, 1), 'Fs', Rsam);
    
%  DAC
    Bdac = 8;                %  DAC bits  (δεν χρησιμοποιείται στην παρούσα έκδοση)
    DRdac = 2;               %  DAC dynamic range,  in Volts

%   Arrays initialization
    Bits = zeros(Nbits,1);           
    Sym  = zeros(Nbits,1);
    Sym1 = zeros(Nbits, 1);
    Sam  = zeros(Nbits*Nup,1);
    Sam1  = zeros(Nbits*Nup,1);
    SNup = zeros(2*Nup*rgd+Nbits*Nup,1);
    SNup1 = zeros(2*Nup*rgd+Nbits*Nup,1);
    Vpsd = zeros(Nfft/2+1, 1);
    Vpsd1 = zeros(Nfft/2+1, 1);
    

%   Calculate RRC coefficients
if disp_ind == 0
    disp('Root Raised Cosine filter - Channel output');
    rcosSpec = fdesign.pulseshaping(Nup, 'Square Root Raised Cosine', 'Nsym,beta', 2*rgd, rr);
else
    disp('Raised Cosine filter - Channel output');
    rcosSpec = fdesign.pulseshaping(Nup, 'Raised Cosine', 'Nsym,beta', 2*rgd, rr);
end
    rcosFlt = design(rcosSpec);
    norm_val = max(rcosFlt.Numerator);
    rcosFltcoefs = rcosFlt.Numerator'/norm_val;

%   Scope
scrsz = get(0,'ScreenSize');
figure('Position',[scrsz(4)/20 scrsz(4)/8 scrsz(3)/1  6*scrsz(4)/8]);
set(gcf, 'color', 'white');
FontSize = 13;
set(gcf,'DefaultLineLineWidth',2);
set(gcf,'DefaultTextFontSize', FontSize, 'DefaultAxesFontSize', FontSize, 'DefaultLineMarkerSize', FontSize);

%%       Modulator Model
disp('2-PAM Modulator ....');
disp(' ');
disp('AMI Modulator ....');
disp(' ');
index = 0;
for ns = 1:Nbits
    %--------
    Bits(ns) =  randi([0, 1]);              % Data bits
    Sym(ns) =  2*Bits(ns)-1;                % Symbols
    % AMI Symbols
    if ~Bits(ns)
        Sym1(ns) = Bits(ns);
    else
        Sym1(ns) = Bits(ns)*((-1)^index);
        index = index + 1;
    end
        
    %--------
    SNup(2*Nup*rgd+(ns-1)*Nup+1:2*Nup*rgd+ns*Nup) = [Sym(ns) zeros(1, Nup-1)];         %  Insert  (Nup-1) zeros
    SNup1(2*Nup*rgd+(ns-1)*Nup+1:2*Nup*rgd+ns*Nup) = [Sym1(ns) zeros(1, Nup-1)];
    for m=1:Nup                                                                        %  Pulse shape  (Direct FIR)
        len = 2*Nup*rgd+ns*Nup;
        tmp = SNup(len+m-Nup-2*Nup*rgd:len+m-Nup);
        tmp1 = SNup1(len+m-Nup-2*Nup*rgd:len+m-Nup);
        Sam((ns-1)*Nup+m) = sum(tmp.*rcosFltcoefs);
        Sam1((ns-1)*Nup+m) = sum(tmp1.*rcosFltcoefs);
    end
  
%  Display   
    if (Ndisp*round(ns*Nup/Ndisp) == ns*Nup) && (ns >= Nmax) && (ns*Nup >= Nfft)
        len = ns*Nup;
        tim = 1000*(len-Nup*Ndisp+1:len)/(Rbits*Nup);      % msecs
        subplot(2,2,1);  
        plot(tim-tim(1), Sam(len-Nup*Ndisp+1:len), '.-');
        hold on;
        plot(tim(1:Nup:length(tim))-tim(1), round(Sam(len-Nup*Ndisp+1:Nup:len)), '.r');
        grid on;
        axis([0 1000*(Ndisp)/(Nup*Rbits) -2*DRdac/2 2*DRdac/2]);
        xlabel('Time [msecs]');
        ylabel('Output Voltage [Volts]');
        snapnow
        hold off;
        
        subplot(2,2,2);  
        plot(tim-tim(1), Sam1(len-Nup*Ndisp+1:len), '.-');
        hold on;
        plot(tim(1:Nup:length(tim))-tim(1), round(Sam1(len-Nup*Ndisp+1:Nup:len)), '.r');
        grid on;
        axis([0 1000*(Ndisp)/(Nup*Rbits) -2*DRdac/2 2*DRdac/2]);
        xlabel('Time [msecs]');
        ylabel('Output Voltage [Volts]');
        snapnow
        hold off;
        
        pause(disp_delay);
        
        subplot(2,2,3);
        NewData = Sam(len-Nfft+1:len);
        if avind ~= 0
            tmp = psd(SWcoefs, NewData, 'Fs', Rsam);
            Vpsd = (Vpsd*aval + tmp.data)/(aval+1);
            aval = aval+1;
        else
            Dpsd=psd(SWcoefs, NewData, 'Fs', Rsam);
            Vpsd = Dpsd.data;
        end
        Fpsd = Dpsd.frequencies;
        plot(Fpsd, Vpsd);
        grid on;
        axis([0 Rsam/4 0 4e-3]);
        xlabel('Frequency [Hz]');
        ylabel('PSD [dB/Hz]');
        snapnow
        % AMI 
        subplot(2,2,4);
        NewData1 = Sam1(len-Nfft+1:len);
        if avind ~= 0
            tmp1 = psd(SWcoefs, NewData1, 'Fs', Rsam);
            Vpsd1 = (Vpsd1*aval + tmp1.data)/(aval+1);
            aval = aval+1;
        else
            Dpsd=psd(SWcoefs, NewData1, 'Fs', Rsam);
            Vpsd1 = Dpsd.data;
        end
        Fpsd1 = Dpsd.frequencies;
        plot(Fpsd1, Vpsd1);
        grid on;
        axis([0 Rsam/4 0 4e-3]);
        xlabel('Frequency [Hz]');
        ylabel('PSD [dB/Hz]');
        snapnow
        
    end
end

%%     
disp('Done! ....');
disp(' ');
