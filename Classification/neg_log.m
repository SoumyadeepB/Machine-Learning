function NLL=neg_log(X,y,beta,lambda)

[m,n]=size(X);
NLL=0;
for i=1:m
    p_i = sigmoid(X(i,:)*beta);
    NLL = NLL + (y(i)*log(p_i) + (1-y(i))*log(1-p_i));
end
NLL = -NLL + lambda*norm(beta);
NLL= (1/m)*log(NLL);
end

