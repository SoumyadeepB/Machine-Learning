clear all;
close all;
size=100;
lambda=linspace(1,10,10);
x=linspace(0,20,size);
f = @(x,l) (x*x+1)+l*(x*x-6*x+8);
L=zeros(1,size);
L_opt=L;

for i=1:10
    for j=1:size
        L(j)=f(x(j),lambda(i));
        
    end 
    if(lambda(i)==2)
            L_opt=L;
    end
    plot(x,L,'r');
    xlabel('x');
    ylabel('L');
    hold on;
    %plot(x,L,'r');
    %L=zeros(1,size);
end
optimal=min(L_opt)

