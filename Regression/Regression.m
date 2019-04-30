close all;
data = load('dataLinReg2D.txt');
figure;
plot3(data(:,1),data(:,2),data(:,3),'r.','MarkerSize',9);
N = size(data,1); %number of inputs (rows)
F = size(data,2); %number of features
X=[ones(N,1),data(:,1:2)];  %append the bias term [1 x x^2]
Y=data(:,3);
%beta = (X'*X)\(X'*Y); %left division : alternative -> beta = inv(X'*X)*(X'*Y)
beta = inv(X'*X)*(X'*Y);
Y_predicted = X*beta;
SE = sum((Y-Y_predicted).^2);  %SE without regularization
hold on;

%Regularization
lambda=10;
I=eye(F);
I(1,1)=0;
beta1 = (X'*X+lambda*I)\(X'*Y);
plot_line(beta1);
Y_predicted = X*beta1;
SE1 = sum((Y-Y_predicted).^2);  %SE with regularization

function plot_line(beta)

%Plotting the Regression line
x1=linspace(-3,3,100);
x2=linspace(-3,3,100);
X1=transpose(combvec(x1,x2));
X1=[ones(size(X1,1),1),X1];
Y_predicted = X1*beta;
scatter3(X1(:,2),X1(:,3),Y_predicted,'.');

end