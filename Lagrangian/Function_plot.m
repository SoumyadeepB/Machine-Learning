close all;
size=100;
lambda=linspace(0,20,10);
x=linspace(0,20,size);
f1=  @(x) (x*x+1);
f2 = @(x) ((x-2)*(x-4));
F1=zeros(1,size);
F2=zeros(1,size);

for j=1:size
    F1(j)=f1(x(j));
    F2(j)=f2(x(j));
end
plot(x,F1,'b');
xlabel('x');
ylabel('f(x)');
hold on;
plot(x,F2,'r');
