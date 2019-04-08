close all;
size=100;
lambda=linspace(0,20,10);
x=linspace(-10,10,size);
y=linspace(-10,10,size);
[x,y]=meshgrid(x,y);
f1=  (x+y);
f2 = (x.^2 + y.^2 - 1);


contour(x,y,f1);
hold on;
contour(x,y,f2);
xlabel('x');
ylabel('y');
zlabel('z');
plot(1,0,'rx');
plot(-1,0,'rx');
plot(0,1,'rx');
plot(0,-1,'rx');

figure();
surf(x,y,f1);
hold on;
surf(x,y,f2,'EdgeColor','None');
xlabel('x');
ylabel('y');
zlabel('z');
