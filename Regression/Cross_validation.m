close all;
clear all;

data = load('dataQuadReg2D_noisy.txt');

N=size(data,1);  %total #of inputs
k=10;
n=N/k; %size of each block
lambda=0;
lambda_y=[];
MSE_testData=[];
Var_testData=[];
MSE_trainData=[];
Var_trainData=[];


for z=1:100  % iterations for varying lambda
    
    test_loss=[];
    train_loss=[];
    
    for j=1:k  % k blocks
        
        train = data;
        train((j-1)*5+1:j*5,:)=[];  %removing the test block
        test = data((j-1)*5+1:j*5,:);
        n=size(train,1); %number of rows/inputs in the training set
        X=[ones(n,1),train(:,1:2),train(:,1).^2,train(:,1).*train(:,2),train(:,2).^2];
        F = size(X,2); %number of features
        Y=train(:,3);
        I=eye(F);
        I(1,1)=0;
        beta = (X'*X+lambda*I)\(X'*Y); %left division : alternative -> inv(X'*X)*(X'*Y)
        
        Y_predicted = X*beta;
        train_SE = sum((Y-Y_predicted).^2);
        
        %Test Data
        n=size(test,1);
        X=[ones(n,1),test(:,1:2),test(:,1).^2,test(:,1).*test(:,2),test(:,2).^2];
        Y_test=test(:,3);
        Y_predicted = X*beta;
        test_SE = sum((Y_test-Y_predicted).^2);
        
        test_loss=[test_loss,test_SE];
        train_loss=[train_loss,train_SE];
    end
    MSE_testData = [MSE_testData,(1/k)*sum(test_loss)];
    Var_testData = [Var_testData,(1/(k-1))*(sum(test_loss.^2)-k*MSE_testData(1,z))];
    
    MSE_trainData = [MSE_trainData,(1/k)*sum(train_loss)];
    Var_trainData = [Var_trainData,(1/(k-1))*(sum(train_loss.^2)-k*MSE_trainData(1,z))];
    
    lambda_y = [lambda_y,lambda];
    lambda=lambda+1;
end


%Bar plots
min_index=find(MSE_testData==min(MSE_testData));  % optimal lambda
opt_lambda=(min_index-1)*1
errorbar(lambda_y,MSE_trainData,sqrt(Var_trainData)./100,'b.');  % scaled down SD
xlabel('\lambda');
ylabel('MSE');
title('Training Error');
figure;
errorbar(lambda_y,MSE_testData,sqrt(Var_testData)./100,'r.');
xlabel('\lambda');
ylabel('MSE');
title('CV Error');







