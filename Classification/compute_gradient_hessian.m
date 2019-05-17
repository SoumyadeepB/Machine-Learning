function [grad,H] = compute_gradient_hessian(X,p,y,beta,lambda,m,n)

I=eye(n+1);
I(1,1)=0; % not regularizing the bias term

%% Gradient
grad = X'*(p-y) + 2*lambda*I*beta;

%% Hessian
H = X'* diag(p.*(1-p))*X + 2*lambda*I;

end
