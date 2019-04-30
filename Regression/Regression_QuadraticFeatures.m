close all;
data = load('dataQuadReg2D.txt');
figure;
plot3(data(:,1),data(:,2),data(:,3),'r.','MarkerSize',9);
N = size(data,1); %number of inputs (rows)

X=[ones(N,1),data(:,1:2),data(:,1).^2,data(:,1).*data(:,2),data(:,2).^2]; % ?(x)=[1 x1 x2 x1^2 x1*x2 x2^2]
F = size(X,2); %number of features
Y=data(:,3);
beta = (X'*X)\(X'*Y); %left division : alternative -> inv(X'*X)*(X'*Y)
Y_predicted = X*beta;
SE = sum((Y-Y_predicted).^2);  %SE without regularization
hold on;

%Regularization
lambda=0;
I=eye(F);
I(1,1)=0;
beta = (X'*X+lambda*I)\(X'*Y);
plot_line(beta);
Y_predicted = X*beta;
SE1 = sum((Y-Y_predicted).^2);   %SE without regularization

function plot_line(beta)

%Plotting the Regression line
x1=linspace(-3,3,100);
x2=linspace(-3,3,100);
X1=transpose(combvec(x1,x2));
X=[ones(size(X1,1),1),X1(:,1:2),X1(:,1).^2,X1(:,1).*X1(:,2),X1(:,2).^2];
Y_predicted = X*beta;
scatter3(X(:,2),X(:,3),Y_predicted,'.');

end

