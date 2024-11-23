function [spectrum] = Goertzel(input, coeff)
	Qn_1 = [0];
	Qn_2 = [0];
	for i = 1:205
		Qn = input(i) + coeff * Qn_1 - Qn_2;
		Qn_2 = Qn_1;
		Qn_1 = Qn;
	end
	Q1 = Qn.^2;
	Q2 = Qn_1.^2;
	spectrum = Q1 + Q2 - coeff * Qn * Qn_1;
end

