fr_LOW = [697 770 852 941];
fr_HIGH = [1209 1336 1477 1633];
cf_LOW = [1.703275 1.635585 1.562297 1.482867];
cf_HIGH = [1.163138 1.008835 0.790074 0.559454];
tone = ['1','2','3','A';
		'4','5','6','B';
		'7','8','9','C';
		'*','0','#','D'];
spect_LOW = [0 0 0 0];
spect_HIGH = [0 0 0 0];

for i = 1:4
    for j = 1:4
		% composing every freq combination to produce 16 signals, 205 samples
		% 8kHz sampling freq
        X = sin(2 * pi * (1:205) * fr_LOW(i) / 8000)
		+ sin(2 * pi * (1:205) * fr_HIGH(j) / 8000);
		for k = 1:4
			% compute spectrum 
            spect_LOW(k) = Goertzel(X, cf_LOW(k));
            spect_HIGH(k) = Goertzel(X, cf_HIGH(k));
			% tone position based on the max amplitude 
			[frH, posH] = max(spect_HIGH);
			[frL, posL] = max(spect_LOW);
			disp(sprintf(('Tone is %c\n'), tone(posL, posH)));    
		end
	end
end
