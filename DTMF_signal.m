%% Read the audio file
%
info = audioinfo('DTMF-r-0.wav');
audio_input = audioread('DTMF-r-0.wav');
%% Gather data and set the axes for both domains
%
Fs = info.SampleRate;
tstep = 1/Fs;
len = info.TotalSamples;
nfft = 2^(nextpow2(len));
f = (0:nfft/2)*(Fs/nfft);
t = 0:tstep:(len - 1)*tstep;
%% Calculate the amplitude of the audio via FFT, only for greater and 
%  equal to zero frequencies
fftx = fft(audio_input, nfft);
fftx = fftx(1:(nfft/2 + 1));
amp = abs(fftx)/nfft;
amp(2:nfft/2) = sqrt(2)*amp(2:nfft/2);
%% Downsample the audio signal and find calculate its FFT
%
less_audio = audio_input(1:4:end);
td = 0:tstep*4:(length(less_audio) - 1)*tstep*4;
nfftd = 2^(nextpow2(length(less_audio)));
fd = (0:nfftd/2)*(Fs/nfftd);
fftxd = fft(less_audio, nfftd);
fftxd = fftxd(1:(nfftd/2 + 1));
ampd = abs(fftxd)/nfftd;
ampd(2:nfftd/2) = sqrt(2)*amp(2:nfftd/2);
%% Plotting
%
subplot(2, 2, 1);
plot(t, audio_input);
title('Input audio');
xlabel('t(sec)');
ylabel('Amplitude')
subplot(2, 2, 2);
plot(f, amp);
title('Spectrum of the audio');
xlabel('f(Hz)');
ylabel('Amplitude')
subplot(2, 2, 3);
plot(td, less_audio);
title('Input audio downsampled by 4');
xlabel('t(sec)');
ylabel('Amplitude')
subplot(2, 2, 4);
plot(fd, ampd);
title('Spectrum of the downsampled audio');
xlabel('f(Hz)');
ylabel('Amplitude')

