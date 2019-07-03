clear all;
close all;
tic;
%Intialization
a=0.001; theta=[0.0001;0.0001]; mu=1;t=1;n=1;flag=0;x=0.5;y=0.5;x_opt=x;y_opt=y;grad_F = [10;10]; mu_opt=mu;

f=  @(x,y)(x+y);  % Objective function
grad_f = [1;1];  % Gradient 
g1 = @(x,y)(x.^2 + y.^2 - 1);  % Constraints
g2 = @(x) (-x);

while true
    flag=0;
    while (grad_F > theta & g1(x,y)<=0 & g2(x)<=0)
        flag=1;
        grad_F = grad_f - mu*(1/g1(x,y))*([2*x;2*y]) - mu*(1/g2(x))*[-1;0];
        x_opt=x;  y_opt=y;
        x= x - a*grad_F(1);
        y= y - a*grad_F(2);
        n=n+1;  %Iteration Counter for inner loop
        mu_opt=mu;
    end
    
    if(flag==0)
        break;
    end
    mu=mu/2;
    t=t+1; %Iteration Counter for outer loop
    grad_F = [10;10];
end


opt=[x_opt;y_opt]
lambda=[-(mu_opt/g1(x_opt,y_opt));-(mu_opt/g2(x_opt))]
opt_function_value=f(x_opt,y_opt)
toc;