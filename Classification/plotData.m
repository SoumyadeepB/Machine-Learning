function plotData(x,y)

pos=find(y==1);
neg=find(y==0);

plot(x(pos, 1), x(pos, 2), 'r.','MarkerSize',6)
hold on
plot(x(neg, 1), x(neg, 2), 'b.','MarkerSize',6)


end

