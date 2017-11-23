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
amp(2:nfft/2) = 2*amp(2:nfft/2);
%% Find the dominant amplitudes and their respective frequencies
%  after splitting the domain due to noise
[A, F] = sort(amp, 'descend');
f1 = (F(1) - 1)*(Fs/nfft);
f2 = (F(2) - 1)*(Fs/nfft);
%% Gross plotting
%
plot(f, amp);