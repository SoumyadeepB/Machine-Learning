function plotData(x,y)

pos=find(y==1);
neg=find(y==0);

% plot3(x(pos,1),x(pos,2),y(pos,1),'rx','MarkerSize',6);
% hold on;
% plot3(x(neg,1),x(neg,2),y(neg,1),'bo','MarkerSize',6);

plot(x(pos, 1), x(pos, 2), 'r+','MarkerSize',3)
hold on
plot(x(neg, 1), x(neg, 2), 'bo','MarkerSize',3)


end

