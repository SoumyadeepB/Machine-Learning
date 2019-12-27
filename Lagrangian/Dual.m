%% Lagrangian Dual  %%
close all;
clear all;
size=100;
size_lambda=20;
lambda=linspace(1,20,size_lambda);
x=linspace(0,20,size);
dual = @(y) (9*y - y*y + 1)/(1+y);
L=zeros(1,size);
D=zeros(1,size_lambda);


for i=1:20
    D(i)=dual(lambda(i));
end
plot(lambda,D,'r');
xlabel('lambda');
ylabel('Dual');
hold on;
dual_max=max(D)
lambda_max=lambda(find(D==dual_max))
plot(lambda_max,dual_max,'bo');
