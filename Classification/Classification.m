
%% Load Data
data = load('data2class.txt');
x=data(:,1:2); %features
y=data(:,3); %classes
[m,n]=size(x);
figure;
plotData(x,y);

%% Feature Matrix
x1=x(:,1);
x2=x(:,2);
X=[ones(m,1),x]; %Linear features
beta = zeros((n+1),1);
lambda=10; %Regularization param

%% Newton steps to calculate beta
for i=1:10
    fx1=X*beta;
    p=sigmoid(fx1);
    [grad,H]= compute_gradient_hessian(X,p,y,beta,lambda,m,n);
    beta = beta - inv(H)*grad;
end

%% Compute mean neg-log likelihood
mean_NLL=neg_log(X,y,beta,lambda)

%% Plot decision boundary
% Define the ranges of the grid within the bounds of the dataset [min,max]
u = linspace(min(x1), max(x1), 200);
v = linspace(min(x2),max(x2), 200);
z = zeros(length(u), length(v));

% Evaluate z = x*beta over the grid
for i = 1:length(u)
    for j = 1:length(v)
        feature_vector=[1,u(i),v(j)];
        z(i,j) = feature_vector*beta;
    end
end

z = z';
% Plot z = 0 by specifying the range [0, 0]
contour(u,v,z, [0, 0], 'LineWidth', 2);
legend('y=1','y=0','Decision boundary');
xlabel('x1');
ylabel('x2');
beta

%% Plotting P(y=1|x)
figure;
plotData(x,y);
for i = 1:length(u)
    for j = 1:length(v)
        feature_vector=[1,u(i),v(j)];
        z(i,j) = sigmoid(feature_vector*beta);
    end
end
[U,V]=meshgrid(u);
surf(U,V,z,'EdgeColor','None');
