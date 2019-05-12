%% Load Data
data = load('data2class.txt');
x=data(:,1:2);
[m,n]=size(x);
y=data(:,3);
figure;
plotData(x,y);

%% Forming Feature Matrix
X=[ones(m,1),x];
beta = zeros((n+1),1);
lambda=10;

%% Newton's method to calculate beta
for i=1:10
    fx1=X*beta;
    p=sigmoid(fx1);
    [grad,H]= compute_gradient_hessian(X,p,y,beta,lambda,m,n);
    beta = beta - inv(H)*grad;
end

%% Plot decision boundary
% Define the ranges of the grid
u = linspace(min(x1), max(x1), 200);
v = linspace(min(x2),max(x2), 200);

% Initialize space for the values to be plotted
z = zeros(length(u), length(v));

% Evaluate z = theta*x over the grid
for i = 1:length(u)
    for j = 1:length(v)
        % Notice the order of j, i here!
        feature_vector=[1,u(i),v(j)];
        z(i,j) = feature_vector*beta;
    end
end

% Because of the way that contour plotting works
% in Matlab, we need to transpose z, or
% else the axis orientation will be flipped!
z = z';
% Plot z = 0 by specifying the range [0, 0]
contour(u,v,z, [0, 0], 'LineWidth', 2);
legend('y=1','y=0','Decision boundary');
xlabel('x1');
ylabel('x2');
beta
figure;
plotData(x,y);
for i = 1:length(u)
    for j = 1:length(v)
        % Notice the order of j, i here!
        feature_vector=[1,u(i),v(j)];
        z(i,j) = sigmoid(feature_vector*beta);
    end
end
[U,V]=meshgrid(u);
surf(U,V,z,'EdgeColor','None');
