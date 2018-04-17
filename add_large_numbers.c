#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
int addHugeNumbers(char *a1, char *a2);
void carry(int pos, char *sum);
int main(int argc, char *argv[]) {
	char a[1000]="939023920930290392039209302930293092032323298889+6623909090999232321190999232323292930930923902", a1[1000]="", a2[1000]="";
	int i=0;
	while (isdigit(a[i])){
		i++;
	}
	strncpy(a1, &a[0], i);
	strncpy(a2, &a[i+1], 1000-i+1);
	addHugeNumbers(a1, a2);
	system("Pause");
	return 0;
}

int addHugeNumbers(char *a1, char *a2){
	int i=0, len1=strlen(a1), len2=strlen(a2), tempres, krat=0;
	char temp[1000]="", sum[1000]="";
	for (i=0; i<1000; i++){
		sum[i]='0';
	}
	if  (len1>len2){
		strncpy(temp, a2, len2);
		for (i=0; i<len1-len2; i++){
			a2[i]='0';
		}
		strcpy(&a2[len1-len2], temp);
	}
	else if (len2>len1){
		strncpy(temp, a1, len1);
		for (i=0; i<len2-len1; i++){
			a1[i]='0';
		}
		strcpy(&a1[len2-len1], temp);
	}
	printf("a1 %s\na2 %s\n", a1, a2);
	for (i=0; i<strlen(a1); i++){
		tempres=(a1[strlen(a1)-1-i]-'0')+(a2[strlen(a2)-1-i]-'0')+krat;
		if (tempres>=10){
			tempres-=10;
			krat=1;
			sum[strlen(a1)-1-i]=tempres+'0';
		}
		else{
		krat=0;
		sum[strlen(a1)-1-i]=tempres+'0';
		}	
	}
	sum[strlen(a1)]='\0';
	printf("re %s\n", sum);
}
